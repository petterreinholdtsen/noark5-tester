# -*- coding: utf-8 -*-

# Copyright (C) 2026 Petter Reinholdtsen
#
# Licensed under the GNU General Public License Version 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import argparse
import json
import sys

from .api import relbaseurl


def build_parser():
    parser = argparse.ArgumentParser(
        prog="tui-api-client",
        description="Noark 5 v5 REST API client with TUI and CLI modes",
    )
    parser.add_argument(
        "--baseurl",
        default=None,
        help="API base URL (default: http://arkiv.local:8092/noark5v5/)",
    )
    parser.add_argument("--username", default=None, help="Username (default: pereadm)")
    parser.add_argument("--password", default=None, help="Password (default: secret)")
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run in non-interactive CLI mode (requires subcommand)",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument(
        "--validate-tui",
        action="store_true",
        help="Run automated TUI validation tests (requires pexpect)",
    )

    subparsers = parser.add_subparsers(dest="subcommand", help="CLI command")

    # list-arkiv
    sp = subparsers.add_parser("list-arkiv", help="List top-level archives")
    sp.set_defaults(func=cmd_list_arkiv)

    # list-children
    sp = subparsers.add_parser("list-children", help="List children of an entity path")
    sp.add_argument("--path", required=True, help="Entity URL or self link")
    sp.set_defaults(func=cmd_list_children)

    # get-entity
    sp = subparsers.add_parser("get-entity", help="Get entity JSON")
    sp.add_argument("--path", required=True, help="Entity URL or self link")
    sp.set_defaults(func=cmd_get_entity)

    # create-mappe
    sp = subparsers.add_parser("create-mappe", help="Create a mappe")
    sp.add_argument(
        "--parent", required=True, help="Parent entity path (klasse or mappe)"
    )
    sp.add_argument("--tittel", required=True, help="Mappe title")
    sp.add_argument("--beskrivelse", default=None, help="Description")
    sp.set_defaults(func=cmd_create_mappe)

    # create-saksmappe
    sp = subparsers.add_parser("create-saksmappe", help="Create a saksmappe (case)")
    sp.add_argument("--parent", required=True, help="Parent entity path")
    sp.add_argument("--tittel", required=True, help="Case title")
    sp.set_defaults(func=cmd_create_saksmappe)

    # create-registrering
    sp = subparsers.add_parser("create-registrering", help="Create a registrering")
    sp.add_argument("--parent", required=True, help="Parent mappe path")
    sp.add_argument("--tittel", required=True, help="Title")
    sp.set_defaults(func=cmd_create_registrering)

    # create-journalpost
    sp = subparsers.add_parser("create-journalpost", help="Create a journalpost")
    sp.add_argument("--parent", required=True, help="Parent saksmappe path")
    sp.add_argument("--tittel", required=True, help="Title")
    sp.set_defaults(func=cmd_create_journalpost)

    # create-dokumentbeskrivelse
    sp = subparsers.add_parser(
        "create-dok-beskrivelse", help="Create a dokumentbeskrivelse"
    )
    sp.add_argument("--parent", required=True, help="Parent registrering path")
    sp.add_argument("--tittel", required=True, help="Title")
    sp.set_defaults(func=cmd_create_dokumentbeskrivelse)

    # create-dokumentobjekt
    sp = subparsers.add_parser("create-dok-objekt", help="Create a dokumentobjekt")
    sp.add_argument("--parent", required=True, help="Parent dokumentbeskrivelse path")
    sp.set_defaults(func=cmd_create_dokumentobjekt)

    # upload-file
    sp = subparsers.add_parser("upload-file", help="Upload file to a dokumentobjekt")
    sp.add_argument(
        "--dokumentobjekt",
        required=True,
        help="Dokumentobjekt path (to get fil/ URL from)",
    )
    sp.add_argument("--file", required=True, help="Path to local file")
    sp.set_defaults(func=cmd_upload_file)

    # move-mappe
    sp = subparsers.add_parser("move-mappe", help="Move a mappe to new parent")
    sp.add_argument("--mappe", required=True, help="Mappe path to move")
    sp.add_argument("--new-parent", required=True, help="New parent mappe path")
    sp.set_defaults(func=cmd_move_mappe)

    # update-entity
    sp = subparsers.add_parser("update-entity", help="Update entity fields")
    sp.add_argument("--path", required=True, help="Entity path")
    sp.add_argument(
        "--set",
        required=True,
        nargs="+",
        help='Field=value pairs to update (e.g., tittel="New title")',
    )
    sp.set_defaults(func=cmd_update_entity)

    # close-mappe
    sp = subparsers.add_parser("close-mappe", help="Close a mappe")
    sp.add_argument("--mappe", required=True, help="Mappe path to close")
    sp.set_defaults(func=cmd_close_mappe)

    # delete-entity
    sp = subparsers.add_parser("delete-entity", help="Delete an entity")
    sp.add_argument("--path", required=True, help="Entity path to delete")
    sp.set_defaults(func=cmd_delete_entity)

    return parser


def _make_api(args):
    from .api import N5API

    api = N5API(baseurl=args.baseurl, username=args.username, password=args.password)
    api.ensure_login()
    return api


def cmd_list_arkiv(api, args):
    for arkiv in api.list_archives():
        self_href = arkiv.get("_links", {}).get("self", {}).get("href", "?")
        print("%s - %s" % (arkiv.get("tittel", "?"), self_href))


def cmd_list_children(api, args):
    path = args.path
    entity = api.get_entity(path)

    # Determine what this entity is and list appropriate children
    links = api.parselinks(entity.get("_links", {}))

    for rel_suffix in (
        "arkivstruktur/arkivdel/",
        "arkivstruktur/klassifikasjonssystem/",
        "arkivstruktur/mappe/",
        "arkivstruktur/undermappe/",
        "sakarkiv/saksmappe/",
        "arkivstruktur/registrering/",
        "sakarkiv/journalpost/",
        "arkivstruktur/dokumentbeskrivelse/",
        "arkivstruktur/dokumentobjekt/",
    ):
        rel = "%s%s" % (relbaseurl, rel_suffix)
        if rel in links:
            url = api.clean_url(links[rel])
            children = api.get_entity(url).get("results", [])
            for child in children:
                self_href = child.get("_links", {}).get("self", {}).get("href", "?")
                print("%s - %s" % (child.get("tittel", "?"), self_href))


def cmd_get_entity(api, args):
    entity = api.get_entity(args.path)
    print(json.dumps(entity, indent=2, ensure_ascii=False))


def cmd_create_mappe(api, args):
    result = api.create_mappe(args.parent, args.tittel, args.beskrivelse)
    self_url = result.get("_links", {}).get("self", {}).get("href", "?")
    print("Created mappe: %s (%s)" % (result.get("tittel", "?"), self_url))


def cmd_create_saksmappe(api, args):
    result = api.create_saksmappe(args.parent, args.tittel)
    self_url = result.get("_links", {}).get("self", {}).get("href", "?")
    print("Created saksmappe: %s (%s)" % (result.get("tittel", "?"), self_url))


def cmd_create_registrering(api, args):
    result = api.create_registrering(args.parent, args.tittel)
    self_url = result.get("_links", {}).get("self", {}).get("href", "?")
    print("Created registrering: %s (%s)" % (result.get("tittel", "?"), self_url))


def cmd_create_journalpost(api, args):
    result = api.create_journalpost(args.parent, args.tittel)
    self_url = result.get("_links", {}).get("self", {}).get("href", "?")
    print("Created journalpost: %s (%s)" % (result.get("tittel", "?"), self_url))


def cmd_create_dokumentbeskrivelse(api, args):
    result = api.create_dokumentbeskrivelse(args.parent, args.tittel)
    self_url = result.get("_links", {}).get("self", {}).get("href", "?")
    print(
        "Created dokumentbeskrivelse: %s (%s)" % (result.get("tittel", "?"), self_url)
    )


def cmd_create_dokumentobjekt(api, args):
    result = api.create_dokumentobjekt(args.parent)
    self_url = result.get("_links", {}).get("self", {}).get("href", "?")
    fil_rel = "%sarkivstruktur/fil/" % relbaseurl
    links = api.parselinks(result.get("_links", {}))
    fil_url = links.get(fil_rel, "N/A")
    print("Created dokumentobjekt: %s (fil upload URL: %s)" % (self_url, fil_url))


def cmd_upload_file(api, args):
    entity = api.get_entity(args.dokumentobjekt)
    links = api.parselinks(entity.get("_links", {}))
    from .api import relbaseurl

    fil_rel = "%sarkivstruktur/fil/" % relbaseurl
    if fil_rel not in links:
        print("Error: No fil/ relation on dokumentobjekt", file=sys.stderr)
        sys.exit(1)
    content, res = api.upload_file(links[fil_rel], args.file)
    print("Upload complete. HTTP code: %d" % res.code)


def cmd_move_mappe(api, args):
    result = api.move_mappe(args.mappe, args.new_parent)
    links = api.parselinks(result.get("_links", {}))
    for rel_key in [
        "%sarkivstruktur/arkivdel/" % relbaseurl,
        "%sarkivstruktur/mappe/" % relbaseurl,
    ]:
        if rel_key in links:
            print("Moved mappe. New parent: %s" % links[rel_key])
            return
    print("Moved mappe (parent relation not in response)")


def cmd_update_entity(api, args):
    changes = {}
    for item in args.set:
        if "=" not in item:
            print("Error: '%s' is not a valid field=value pair" % item, file=sys.stderr)
            sys.exit(1)
        k, v = item.split("=", 1)
        changes[k] = v
    result = api.update_entity(args.path, changes)
    print("Updated entity. SystemID: %s" % result.get("systemID", "?"))


def cmd_close_mappe(api, args):
    result = api.close_mappe(args.mappe)
    print("Mappe closed. avsluttetDato: %s" % result.get("avsluttetDato", "N/A"))


def cmd_delete_entity(api, args):
    """Delete an entity by path."""
    try:
        api.delete_entity(args.path)
        print("Deleted entity: %s" % args.path)
    except Exception as e:
        print("Error deleting %s: %s" % (args.path, e), file=sys.stderr)


def run_cli():
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, "validate_tui") and args.validate_tui:
        from .validate import run_tui_validation as _run_validate

        res = _run_validate(
            baseurl=args.baseurl, username=args.username, password=args.password
        )
        print()
        sys.exit(0 if (res is not None and res.tests_failed == 0) else 1)

    if not args.cli and not args.subcommand:
        # No CLI flag and no subcommand — launch TUI mode (handled by caller)
        return None

    if not args.subcommand:
        parser.print_help()
        sys.exit(1)

    api = _make_api(args)
    try:
        args.func(api, args)
    except Exception as e:
        print("Error: %s" % e, file=sys.stderr)
        if args.verbose:
            raise
        sys.exit(1)


def run_tui():
    """Launch the interactive TUI."""
    import os as _os

    if _os.environ.get("N5TUI_TEST_MODE"):
        # Force select()-based polling for pexpect compatibility (avoids epoll EPERM)
        import selectors as _sel

        _sel.DefaultSelector = _sel.SelectSelector

    from .tui import create_tui

    # Patch MainLoop.draw_screen to handle urwid WidgetError during overlay transitions.
    # When a dialog closes synchronously during keypress (e.g., entity creation), urwid's
    # entering_idle() may try to render stale overlay widgets that are no longer valid,
    # causing WidgetError crashes in pexpect fake-terminal mode.
    import urwid as _urwid

    _orig_draw = _urwid.MainLoop.draw_screen

    def _safe_draw(self):
        try:
            return _orig_draw(self)
        except _urwid.widget.WidgetError:
            pass  # Suppress stale overlay render errors during dialog transitions

    _urwid.MainLoop.draw_screen = _safe_draw

    parser = build_parser()
    args = parser.parse_args()

    loop = create_tui(
        baseurl=args.baseurl, username=args.username, password=args.password
    )
    try:
        loop.run()
    except KeyboardInterrupt:
        pass


def main():
    # Check if any subcommand is given (CLI mode) or just run TUI
    argv = sys.argv[1:]
    has_subcommand = False
    skip_flags = {"--baseurl", "--username", "--password"}
    for arg in argv:
        if arg.startswith("-"):
            continue
        has_subcommand = True
        break

    parser = build_parser()

    # Check for --help before parsing to avoid exception noise
    if "--help" in argv or "-h" in argv:
        parser.parse_args(argv)  # Will print help and exit cleanly via SystemExit
        return

    try:
        args, _ = parser.parse_known_args(argv)
    except SystemExit:
        run_tui()
        return

    if (
        args.subcommand
        or args.cli
        or (hasattr(args, "validate_tui") and args.validate_tui)
    ):
        run_cli()
    else:
        run_tui()


if __name__ == "__main__":
    main()
