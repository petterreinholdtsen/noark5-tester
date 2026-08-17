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

import urwid


class EntityTreeWidget(urwid.TreeWidget):
    """Tree widget that displays the Noark 5 archive hierarchy."""

    def __init__(self, api, top_path=None):
        self.api = api
        self.top_path = top_path
        super().__init__(self._top_node, self._load_children)

    def _top_node(self):
        return urwid.TreeNode(self._render_root, expandable=True, expanded=False)

    def _render_root(self):
        return urwid.Text(("bold", "[Arkiv]"))

    def _load_children(self, parent_node):
        """Load children for a tree node."""
        path = parent_node.user_data

        if path is None:
            # Root level — list archives
            try:
                archives = self.api.list_archives()
            except Exception:
                archives = []
            for arkiv in archives:
                self_url = arkiv.get("_links", {}).get("self", {}).get("href")
                label = "%s - %s" % (
                    arkiv.get("tittel", "?"),
                    arkiv.get("systemID", ""),
                )
                yield urwid.TreeNode(
                    urwid.Text(label),
                    user_data=self_url,
                    expandable=True,
                    expanded=False,
                )
            return

        # Determine entity type and load appropriate children
        try:
            entity = self.api.get_entity(path)
            links = self.api.parselinks(entity.get("_links", {}))
        except Exception:
            return

        from .api import relbaseurl

        child_rels = []
        # Priority order for listing children
        if "%sarkivstruktur/arkivdel/" % relbaseurl in links:
            child_rels.append(("arkivdel", "%sarkivstruktur/arkivdel/" % relbaseurl))
        if "%ssakarkiv/saksmappe/" % relbaseurl in links:
            child_rels.append(("saksmappe", "%ssakarkiv/saksmappe/" % relbaseurl))
        if "%sarkivstruktur/klassifikasjonssystem/" % relbaseurl in links:
            child_rels.append(
                ("klassif.", "%sarkivstruktur/klassifikasjonssystem/" % relbaseurl)
            )
        if "%sarkivstruktur/mappe/" % relbaseurl in links:
            child_rels.append(("mappe", "%sarkivstruktur/mappe/" % relbaseurl))
        if "%ssakarkiv/journalpost/" % relbaseurl in links:
            child_rels.append(("journalpost", "%ssakarkiv/journalpost/" % relbaseurl))
        if "%sarkivstruktur/registrering/" % relbaseurl in links:
            child_rels.append(
                ("registrering", "%sarkivstruktur/registrering/" % relbaseurl)
            )
        if "%sarkivstruktur/dokumentbeskrivelse/" % relbaseurl in links:
            child_rels.append(
                ("dok.beskr.", "%sarkivstruktur/dokumentbeskrivelse/" % relbaseurl)
            )

        for label, rel_key in child_rels:
            children = self.api.get_entity(links[rel_key]).get("results", [])
            for child in children:
                c_self = child.get("_links", {}).get("self", {}).get("href")
                tittel = child.get("tittel", child.get("klasseID", "?"))
                sysid = child.get("systemID", "")
                text = "%s [%s] %s" % (label, sysid, tittel)
                yield urwid.TreeNode(
                    urwid.Text(text),
                    user_data=c_self,
                    expandable=True,
                    expanded=False,
                )


class DetailPane(urwid.Pile):
    """Shows metadata for the selected entity."""

    def __init__(self):
        super().__init__([urwid.Text("Select an entity to see details.")])

    def set_entity(self, entity):
        if not entity:
            self.contents = [(urwid.Text("No entity selected."), None)]
            return

        lines = []
        for key in (
            "systemID",
            "tittel",
            "beskrivelse",
            "mappeID",
            "klasseID",
            "registreringsID",
            "opprettetDato",
            "avsluttetDato",
            "dokumenttype",
            "journalstatus",
        ):
            if key in entity:
                val = entity[key]
                if isinstance(val, dict):
                    val = json.dumps(val, ensure_ascii=False)
                lines.append(urwid.Text("%-20s %s" % (key + ":", str(val))))

        # Show _links summary
        links = entity.get("_links", {})
        from .api import relbaseurl

        interesting_rels = (
            "self",
            "%sarkivstruktur/overmappe/" % relbaseurl,
            "%ssakarkiv/saksmappe/" % relbaseurl,
        )
        link_lines = []
        for rel, info in links.items():
            short = rel.replace(relbaseurl, "").rstrip("/")
            if "href" in info:
                link_lines.append(urwid.Text("  %-35s %s" % (short, info["href"])))

        if link_lines:
            lines.append(urwid.Text("_links:"))
            lines.extend(link_lines)

        if not lines:
            lines = [urwid.Text(json.dumps(entity, indent=2, ensure_ascii=False))]

        self.contents = [(urwid.AttrWrap(l, "body"), None) for l in lines]


class StatusBar(urwid.Text):
    """Status bar at the bottom."""

    def __init__(self):
        super().__init__("tui-api-client | Enter: select | q: quit")

    def set_message(self, msg):
        self.set_text(msg)


import json
