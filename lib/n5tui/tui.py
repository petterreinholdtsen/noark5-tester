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

import json
import sys
import warnings
import urwid
from urwid.widget.columns import ColumnsWarning as _CW

warnings.filterwarnings("ignore", category=_CW)

from .api import relbaseurl

palette = [
    ("header", "white", "dark blue"),
    ("body", "", "default"),
    ("selected", "white", "dark cyan", "standout"),
    ("error", "light red", "default"),
    ("status", "white", "dark cyan"),
    ("action", "default", "default"),
    ("action_focus", "white", "black", "bold"),
    ("select", "light cyan", "default", "standout"),
    ("select_focus", "white", "dark blue", "bold"),
]

PAGE_SIZE = 50

ARKIVDEL_FIELDS = [
    "tittel",
    "beskrivelse",
    "arkivdelstatus",
    "dokumentmedium",
    "oppbevaringssted",
    "avsluttetDato",
    "avsluttetAv",
]
KLASSIFIKASJONSSYSTEM_FIELDS = [
    "tittel",
    "beskrivelse",
    "klassifikasjonstype",
]
MAPPE_FIELDS = [
    "tittel",
    "mappeID",
    "offentligTittel",
    "beskrivelse",
    "noekkelord",
    "dokumentmedium",
    "oppbevaringssted",
]
REGISTRERING_FIELDS = [
    "tittel",
    "arkivertDato",
    "arkivertAv",
    "registreringsID",
    "offentligTittel",
    "beskrivelse",
    "noekkelord",
    "forfatter",
    "dokumentmedium",
    "oppbevaringssted",
]
SAKSMAPPE_FIELDS = REGISTRERING_FIELDS + [
    "saksaar",
    "sakssekvensnummer",
    "saksdato",
    "administrativEnhet",
    "saksansvarlig",
    "journalenhet",
    "saksstatus",
]
JOURNALPOST_FIELDS = SAKSMAPPE_FIELDS + [
    "journalaar",
    "journalsekvensnummer",
    "journalposttype",
    "journalstatus",
    "journaldato",
    "dokumentetsDato",
    "mottattDato",
    "sendtDato",
    "forfallsdato",
    "offentlighetsvurdertDato",
    "antallVedlegg",
]
DOKUMENTBESKRIVELSE_FIELDS = [
    "dokumenttype",
    "dokumentstatus",
    "tittel",
    "beskrivelse",
    "forfatter",
    "dokumentmedium",
    "oppbevaringssted",
    "tilknyttetRegistreringSom",
    "dokumentnummer",
]
DOKUMENTOBJEKT_FIELDS = [
    "versjonsnummer",
    "variantformat",
    "format",
    "sjekksum",
    "sjekksumAlgoritme",
    "filstoerrelse",
]
KLASSE_FIELDS = [
    "klasseID",
    "tittel",
    "beskrivelse",
    "noekkelord",
]
MOETEMAPPE_FIELDS = MAPPE_FIELDS + ["moetedato"]
MOETEREGISTRERING_FIELDS = REGISTRERING_FIELDS + ["moetedato"]
PARTPERSON_FIELDS = [
    "partNavn",
    "partRolle",
    "postadresse",
    "postnummer",
    "poststed",
    "land",
    "epostadresse",
    "telefonnummer",
    "kontaktperson",
]
PARTEHET_FIELDS = PARTPERSON_FIELDS + ["organisasjonsnummer"]
ARKIV_FIELDS = [
    "tittel",
    "beskrivelse",
    "arkivstatus",
    "dokumentmedium",
]
ARKIVSKAPER_FIELDS = [
    "arkivskaperID",
    "arkivskaperNavn",
    "beskrivelse",
]

CREATE_ACTIONS = [
    ("arkivstruktur/ny-arkivdel/", "Arkivdel", ARKIVDEL_FIELDS),
    (
        "arkivstruktur/ny-klassifikasjonssystem/",
        "Klassifiseringssystem",
        KLASSIFIKASJONSSYSTEM_FIELDS,
    ),
    ("arkivstruktur/ny-mappe/", "Mappe", MAPPE_FIELDS),
    ("sakarkiv/ny-saksmappe/", "Saksmappe", SAKSMAPPE_FIELDS),
    ("arkivstruktur/ny-registrering/", "Registrering", REGISTRERING_FIELDS),
    ("sakarkiv/ny-journalpost/", "Journalpost", JOURNALPOST_FIELDS),
    (
        "arkivstruktur/ny-dokumentbeskrivelse/",
        "Dokumentbeskrivelse",
        DOKUMENTBESKRIVELSE_FIELDS,
    ),
    ("arkivstruktur/ny-dokumentobjekt/", "Dokumentobjekt", DOKUMENTOBJEKT_FIELDS),
    ("arkivstruktur/ny-klasse/", "Klasse", KLASSE_FIELDS),
    ("arkivstruktur/ny-partperson/", "Partperson", PARTPERSON_FIELDS),
    ("arkivstruktur/ny-partenhet/", "Partenhet", PARTEHET_FIELDS),
]

ROOT_CREATE_ACTIONS = [
    ("arkivstruktur/ny-arkivskaper/", "Arkivskaper", ARKIVSKAPER_FIELDS),
    ("arkivstruktur/ny-arkiv/", "Arkiv", ARKIV_FIELDS),
]

# Move configuration: entity_type → list of valid parent relation suffixes.
# Nikita only supports these moves via PATCH _links update (verified on live server):
#   - arkiv → overarkiv (REL_FONDS_STRUCTURE_FONDS)
#   - klasse → overklasse or klassifikasjonssystem
#   - mappe/saksmappe/moetemappe → arkivdel, overmappe, klasse
#   - registrering/journalpost → mappe or saksmappe (REL_FONDS_STRUCTURE_FILE)
MOVE_CONFIG = {
    # Arkivdel is not recursive — only movable under Arkiv (via arkiv/ relation).
    # Not yet tested whether Nikita accepts PATCH of arkiv/ on Arkivdel.
    "arkivstruktur/arkivdel/": ["arkivstruktur/arkiv/"],
    "arkivstruktur/klasse/": [
        "arkivstruktur/overklasse/",
        "arkivstruktur/klassifikasjonssystem/",
    ],
    "arkivstruktur/mappe/": [
        "arkivstruktur/arkivdel/",
        "arkivstruktur/overmappe/",
        "arkivstruktur/klasse/",
    ],
    "sakarkiv/moetemappe/": [  # Møtemappe moves like Mappe
        "arkivstruktur/arkivdel/",
        "arkivstruktur/overmappe/",
        "arkivstruktur/klasse/",
    ],
    "sakarkiv/saksmappe/": [
        "arkivstruktur/arkivdel/",
        "arkivstruktur/overmappe/",
        "arkivstruktur/klasse/",
    ],
    "arkivstruktur/registrering/": [
        "arkivstruktur/mappe/",
        "sakarkiv/saksmappe/",
    ],
    "sakarkiv/moeteregistrering/": [  # Møteregistrering moves like Registrering
        "arkivstruktur/mappe/",
        "sakarkiv/saksmappe/",
    ],
    "sakarkiv/journalpost/": [
        "arkivstruktur/mappe/",
        "sakarkiv/saksmappe/",
    ],
}


def _get_entity_type_for_path(path):
    """Determine entity type key from path for move/create lookups."""
    if not path:
        return None
    # Check most specific types first (subtypes inherit from parent)
    type_patterns = [
        ("saksmappe/", "sakarkiv/saksmappe/"),
        ("journalpost/", "sakarkiv/journalpost/"),
        ("moetemappe/", "sakarkiv/moetemappe/"),
        ("moeteregistrering/", "sakarkiv/moeteregistrering/"),
        ("moetedeltager/", "sakarkiv/moetedeltager/"),
        ("klassifikasjonssystem/", "arkivstruktur/klassifikasjonssystem/"),
        ("klasse/", "arkivstruktur/klasse/"),
        ("mappe/", "arkivstruktur/mappe/"),
        ("registrering/", "arkivstruktur/registrering/"),
        ("arkiv/", "arkivstruktur/arkiv/"),
    ]
    for pattern, type_key in type_patterns:
        if "/" + pattern in path or path.rstrip("/").endswith(pattern.rstrip("/")):
            return type_key
    return None


def _get_entity_fields(path):
    """Return list of editable fields for the entity at the given path."""
    if not path:
        return []
    # Check most specific types first (subtypes inherit from parent)
    for pattern, fields in [
        ("saksmappe/", SAKSMAPPE_FIELDS),
        ("journalpost/", JOURNALPOST_FIELDS),
        ("moetemappe/", MOETEMAPPE_FIELDS),
        ("moeteregistrering/", MOETEREGISTRERING_FIELDS),
        ("klassifikasjonssystem/", KLASSIFIKASJONSSYSTEM_FIELDS),
        ("klasse/", KLASSE_FIELDS),
        ("dokumentobjekt/", DOKUMENTOBJEKT_FIELDS),
        ("dokumentbeskrivelse/", DOKUMENTBESKRIVELSE_FIELDS),
        ("registrering/", REGISTRERING_FIELDS),
        ("mappe/", MAPPE_FIELDS),
        ("arkivdel/", ARKIVDEL_FIELDS),
        ("partperson/", PARTPERSON_FIELDS),
        ("partenhet/", PARTEHET_FIELDS),
        ("arkivskaper/", ARKIVSKAPER_FIELDS),
        ("arkiv/", ARKIV_FIELDS),
    ]:
        if "/" + pattern in path:
            return fields
    return []


# Entity type key -> display name (used by create actions, probe functions, etc.)
TYPE_NAMES_MAP = {
    "arkivstruktur/arkiv/": "Arkiv",
    "arkivstruktur/klassifikasjonssystem/": "Kl.system",
    "arkivstruktur/klasse/": "Klasse",
    "arkivstruktur/arkivdel/": "Arkivdel",
    "sakarkiv/moetemappe/": "Møtemappe",
    "arkivstruktur/mappe/": "Mappe",
    "sakarkiv/saksmappe/": "Saksmappe",
    "sakarkiv/moeteregistrering/": "Møteregistrering",
    "arkivstruktur/registrering/": "Registrering",
    "sakarkiv/journalpost/": "Journalpost",
}


CHILD_RELATIONS = [
    ("arkivskaper", "%sarkivstruktur/arkivskaper/" % relbaseurl),
    ("arkiv", "%sarkivstruktur/arkiv/" % relbaseurl),
    ("underark.", "%sarkivstruktur/underarkiv/" % relbaseurl),
    ("arkivdel", "%sarkivstruktur/arkivdel/" % relbaseurl),
    ("kl.sys.", "%sarkivstruktur/klassifikasjonssystem/" % relbaseurl),
    ("klasse", "%sarkivstruktur/klasse/" % relbaseurl),
    ("underk.", "%sarkivstruktur/underklasse/" % relbaseurl),
    ("mappe", "%sarkivstruktur/mappe/" % relbaseurl),
    ("moetm.", "https://nikita.arkivlab.no/noark5/v5/moeter/moetemappe/"),
    ("underm.", "%sarkivstruktur/undermappe/" % relbaseurl),
    ("saksm.", "%ssakarkiv/saksmappe/" % relbaseurl),
    ("reg.", "%sarkivstruktur/registrering/" % relbaseurl),
    ("moetreg.", "https://nikita.arkivlab.no/noark5/v5/moeter/moeteregistrering/"),
    ("jp", "%ssakarkiv/journalpost/" % relbaseurl),
    ("dok.beskr.", "%sarkivstruktur/dokumentbeskrivelse/" % relbaseurl),
    ("dok.obj.", "%sarkivstruktur/dokumentobjekt/" % relbaseurl),
]


class TreeNodeWidget(urwid.WidgetWrap):
    """A tree node with focus indicator support."""

    def __init__(self, label, path=None, has_children=False, focused=False):
        self.label = label
        self.has_children = has_children
        prefix = (
            ("> " + ("+" if has_children else " "))
            if focused
            else ("+ " if has_children else "  ")
        )
        text = urwid.Text(prefix + label)
        mapped = urwid.AttrMap(text, "body", "selected")
        super().__init__(mapped)
        self.path = path

    def selectable(self):
        """Make this widget individually navigatable by ListBox."""
        return True

    def keypress(self, size, key):
        """Don't handle keys ourselves - let ListBox manage navigation."""
        return key


def _node_has_children(node):
    """Check if a node has children (compat for TreeNodeWidget and old widgets)."""
    return getattr(node, "has_children", False) or getattr(node, "_has_children", False)


def _node_path(node):
    """Get path from node (compat for TreeNodeWidget and old widgets)."""
    return getattr(node, "path", None) or getattr(node, "_path", None)


def _make_widget(label, path=None, has_children=False):
    """Create a tree node widget."""
    return TreeNodeWidget(label, path=path, has_children=has_children)


def _update_focus_indicator(walker):
    """Replace widgets at old/new focus positions to ensure visual update."""
    try:
        new_pos = walker.focus_position
    except Exception:
        return

    if not hasattr(walker, "_last_focused"):
        walker._last_focused = None

    # Replace previously focused widget with unfocused version
    if walker._last_focused is not None and walker._last_focused != new_pos:
        try:
            old_w = walker[walker._last_focused]
            if isinstance(old_w, TreeNodeWidget):
                replacement = TreeNodeWidget(
                    label=old_w.label,
                    path=old_w.path,
                    has_children=old_w.has_children,
                    focused=False,
                )
                _replace_widget_in_walker(walker, walker._last_focused, replacement)
        except Exception:
            pass

    # Replace newly focused widget with focused version
    try:
        new_w = walker[new_pos]
        if isinstance(new_w, TreeNodeWidget):
            replacement = TreeNodeWidget(
                label=new_w.label,
                path=new_w.path,
                has_children=new_w.has_children,
                focused=True,
            )
            _replace_widget_in_walker(walker, new_pos, replacement)
    except Exception:
        pass

    walker._last_focused = new_pos


def _replace_widget_in_walker(walker, pos, widget):
    """Replace a widget in any walker type."""
    if hasattr(walker, "_replace_widget"):
        # Custom LazyChildWalker with cache support
        walker._replace_widget(pos, widget)
    elif isinstance(walker, urwid.SimpleFocusListWalker):
        # Simple list-based walker - replace directly in the list
        if 0 <= pos < len(walker):
            walker[pos] = widget
    else:
        # Fallback: try direct assignment
        try:
            walker.set_item(pos, widget)
        except Exception:
            pass


class LazyChildWalker(urwid.ListWalker):
    """Paginated walker that loads children in windows around focus position.

    Uses OData $top/$skip parameters to fetch pages on demand as the user
    scrolls through large result sets, avoiding loading everything into memory.

    Deduplicates inherited types: if an entity appears under both base and derived
    relations (e.g., saksmappe under mappe/ and saksmappe/), only shows it once
    under the most specific type. Derived types appear later in CHILD_RELATIONS,
    so their IDs "claim" the entity first via _claimed_ids set.
    """

    def __init__(self, api, parent_path):
        super().__init__()
        self.api = api
        self.parent_path = parent_path
        # List of (type_label, base_url) for each child relation type
        self._relations = []
        # Per-type caches: { type_index: { 'total': N, 'pages': {skip: [widgets]} } }
        self._cache = {}
        self.focus_position = 0
        # Track systemIDs claimed by more derived types for deduplication: {sysid: type_idx}
        self._claimed_ids = {}

        try:
            entity, _wp = _fetch_entity(api, parent_path)
            self._relations = api.get_children(entity, CHILD_RELATIONS)
        except Exception:
            pass

        # Collect IDs from ALL relation types first (most derived last = wins)
        self._collect_ids()

    def _get_system_id(self, child, tlabel):
        """Extract systemID from entity (arkivskaper uses arkivskaperID)."""
        if "arkivskaper" in tlabel.lower():
            return child.get("arkivskaperID", "")
        return child.get("systemID", "")

    def _collect_ids(self):
        """Collect systemIDs from all relation types for deduplication.

        Most derived types (later in CHILD_RELATIONS) claim their IDs first,
        so base types will skip entities that are actually derived instances.
        E.g., saksmappe claims its IDs; mappe then skips those same entities.

        After claiming, loads ALL pages for each type to build complete widget lists
        with accurate deduplicated counts (avoids position mapping issues from
        partial page loading where duplicate distribution varies per page).
        """
        def _dbg(*a):
            if getattr(self.api, 'verbose', False):
                print("[TREE] " + " ".join(str(x) for x in a), file=sys.stderr)

        _dbg("parent_path:", self.parent_path)
        _dbg("relations found:", [(r[0], r[1]) for r in self._relations])

        # Process relation types in REVERSE order: most derived types claim first
        for tidx in range(len(self._relations) - 1, -1, -1):
            self._ensure_cache(tidx)
            _, turl = self._relations[tidx]
            total = self._cache[tidx]["total"]
            if total == 0:
                _dbg("claim phase skip (count=0)", self._relations[tidx][0], "url", turl)
                continue

            claimed_count = 0
            # Paginate through all results to claim IDs
            skip = 0
            while skip < total:
                try:
                    query_url = "%s?$top=%d&$skip=%d" % (turl, PAGE_SIZE * 10, skip)
                    resp = self.api.get_entity(query_url)
                    results = resp.get("results", [])
                    if not results:
                        break
                except Exception as e:
                    _dbg("claim phase ERROR:", self._relations[tidx][0], str(e))
                    break

                for child in results:
                    sysid = self._get_system_id(child, self._relations[tidx][0])
                    if sysid and sysid not in self._claimed_ids:
                        # First claim wins (we process derived first)
                        self._claimed_ids[sysid] = tidx
                        claimed_count += 1

                skip += len(results)

            _dbg("claim phase:", self._relations[tidx][0], "-> claimed", claimed_count, "IDs (total=", total, ")")

        _dbg("claimed IDs:", {k: self._relations[v][0] for k, v in self._claimed_ids.items()})

        # Load ALL pages for each type to build complete deduplicated widget lists
        # This ensures accurate counts for position mapping
        for tidx in range(len(self._relations)):
            _, turl = self._relations[tidx]
            total = self._cache[tidx]["total"]
            if total == 0:
                continue

            all_widgets = []
            loaded = 0
            skipped_dupes = 0
            while loaded < total:
                skip = loaded
                try:
                    query_url = "%s?$top=%d&$skip=%d" % (turl, PAGE_SIZE, skip)
                    resp = self.api.get_entity(query_url)
                except Exception as e:
                    _dbg("load page ERROR:", self._relations[tidx][0], "query:", query_url, str(e))
                    break
                results = resp.get("results", [])
                if not results:
                    _dbg("load page empty:", self._relations[tidx][0], "query:", query_url)
                    break

                for child in results:
                    c_self = child.get("_links", {}).get("self", {}).get("href")
                    tlabel = self._relations[tidx][0]
                    sysid = self._get_system_id(child, tlabel)

                    # Skip if claimed by a different (more derived) type
                    if sysid and self._claimed_ids.get(sysid) != tidx:
                        skipped_dupes += 1
                        continue

                    if "arkivskaper" in tlabel.lower():
                        tittel = child.get("arkivskaperNavn", "?")
                    elif "dokumentobjekt" in c_self:
                        fn = child.get("filnavn", "") or ""
                        fmt = child.get("format", {})
                        parts = []
                        if fn:
                            parts.append(fn)
                        if isinstance(fmt, dict):
                            fkn = fmt.get("kodenavn") or fmt.get("kode") or ""
                            if fkn and fkn.lower() not in ("unknown", "ukjent filformat"):
                                parts.append("(%s)" % fkn)
                        tittel = "".join(parts) if parts else "(dokumentobjekt)"
                    else:
                        tittel = child.get("tittel", child.get("klasseID", "?"))

                    date_str = ""
                    opprettet = child.get("opprettetDato", "")
                    if opprettet:
                        date_str = opprettet[:10]

                    label = "%s%s %s" % (date_str, "  " if date_str else "", tittel)
                    all_widgets.append(
                        _make_widget(label, path=c_self, has_children=True)
                    )

                loaded += len(results)

            # Store as single complete list; update total to deduplicated count
            self._cache[tidx]["pages"] = {0: all_widgets}
            self._cache[tidx]["total"] = len(all_widgets)
            _dbg("load phase result:", self._relations[tidx][0], "-> widgets=", len(all_widgets), "skipped_dupes=", skipped_dupes, "(raw total was", total, ")")

        final_total = sum(c["total"] for c in self._cache.values())
        _dbg("TREE FINAL count:", final_total)

    def _total_items(self):
        """Total number of items across all relation types."""
        return sum(c["total"] for c in self._cache.values())

    def _ensure_cache(self, tidx):
        """Ensure cache entry exists for type index.

        Paginates through all results to discover the true collection size,
        since Nikita's 'count' field reports items returned (not total).
        """
        def _dbg(*a):
            if getattr(self.api, 'verbose', False):
                print("[TREE] " + " ".join(str(x) for x in a), file=sys.stderr)

        if tidx not in self._cache:
            _, turl = self._relations[tidx]
            try:
                # First query with a large $top to get all results efficiently
                resp_data = self.api.get_entity("%s?$top=%d" % (turl, PAGE_SIZE * 10))
                results = resp_data.get("results", [])
                total = len(results)

                # If we got exactly PAGE_SIZE*10, there might be more — paginate to discover
                while total > 0 and len(results) == PAGE_SIZE * 10:
                    skip = total
                    resp_data = self.api.get_entity("%s?$top=%d&$skip=%d" % (turl, PAGE_SIZE * 10, skip))
                    results = resp_data.get("results", [])
                    if not results:
                        break
                    total += len(results)

                _dbg("_ensure_cache:", self._relations[tidx][0], "-> discovered total=", total)
            except Exception as e:
                total = 0
                _dbg("_ensure_cache ERROR:", self._relations[tidx][0], str(e))
            self._cache[tidx] = {"total": total, "pages": {}}

    def _find_type_for_pos(self, pos):
        """Return (type_idx, offset_in_type) for a global position."""
        if pos is None:
            return None, 0
        accumulated = 0
        for tidx in range(len(self._relations)):
            self._ensure_cache(tidx)
            total = self._cache[tidx]["total"]
            if pos < accumulated + total:
                return tidx, pos - accumulated
            accumulated += total
        return None, 0

    def _load_page(self, type_idx, skip):
        """Load one page of children for a specific relation type.

        Skips entities whose systemID is owned by a more derived type
        (e.g., skips saksmappe instances when loading mappe relation).
        """
        if type_idx >= len(self._relations):
            self._cache.setdefault(type_idx, {"total": 0, "pages": {}})
            self._cache[type_idx]["pages"][skip] = []
            return

        tlabel, turl = self._relations[type_idx]
        try:
            resp = self.api.get_entity("%s?$top=%d&$skip=%d" % (turl, PAGE_SIZE, skip))
        except Exception:
            self._cache.setdefault(type_idx, {"total": 0, "pages": {}})
            self._cache[type_idx]["pages"][skip] = []
            return

        widgets = []
        for child in resp.get("results", []):
            c_self = child.get("_links", {}).get("self", {}).get("href")
            # Arkivskaper uses arkivskaperID/arkivskaperNavn; others use systemID/tittel
            if "arkivskaper" in tlabel.lower():
                tittel = child.get("arkivskaperNavn", "?")
                sysid = child.get("arkivskaperID", "")
            elif "dokumentobjekt" in c_self:
                fn = child.get("filnavn", "") or ""
                fmt = child.get("format", {})
                parts = []
                if fn:
                    parts.append(fn)
                if isinstance(fmt, dict):
                    fkn = fmt.get("kodenavn") or fmt.get("kode") or ""
                    if fkn and fkn.lower() not in ("unknown", "ukjent filformat"):
                        parts.append("(%s)" % fkn)
                tittel = "".join(parts) if parts else "(dokumentobjekt)"
                sysid = child.get("systemID", "")
            else:
                tittel = child.get("tittel", child.get("klasseID", "?"))
                sysid = child.get("systemID", "")

            # Skip if this entity's ID is owned by a more derived type
            if sysid and self._claimed_ids.get(sysid) != type_idx:
                continue

            date_str = ""
            opprettet = child.get("opprettetDato", "")
            if opprettet:
                date_str = opprettet[:10]

            label = "%s%s %s" % (date_str, "  " if date_str else "", tittel)
            widgets.append(_make_widget(label, path=c_self, has_children=True))

        self._cache.setdefault(type_idx, {"total": 0, "pages": {}})
        self._cache[type_idx]["pages"][skip] = widgets

    def _ensure_loaded(self, pos):
        """Ensure page is loaded around the given global position."""
        tidx, offset_in_type = self._find_type_for_pos(pos)
        if tidx is None:
            return

        page_skip = (offset_in_type // PAGE_SIZE) * PAGE_SIZE
        if page_skip not in self._cache[tidx]["pages"]:
            self._load_page(tidx, page_skip)

    def get(self, pos):
        """Return widget at global position."""
        self._ensure_loaded(pos)
        tidx, offset_in_type = self._find_type_for_pos(pos)
        if tidx is None:
            return urwid.Text("(no more children)")

        page_skip = (offset_in_type // PAGE_SIZE) * PAGE_SIZE
        local_idx = offset_in_type - page_skip
        widgets = self._cache[tidx]["pages"].get(page_skip, [])
        if 0 <= local_idx < len(widgets):
            return widgets[local_idx]
        return urwid.Text("(empty slot %d)" % pos)

    def set_focus(self, pos):
        """Set focus to global position."""
        old = self.focus_position
        if pos is not None:
            self._ensure_loaded(pos)
        self.focus_position = pos if pos is not None else 0
        if old != self.focus_position:
            self._modified()  # urwid 3.x signal for focus change

    def _replace_widget(self, pos, widget):
        """Replace a widget in the cache at given position."""
        tidx, offset_in_type = self._find_type_for_pos(pos)
        if tidx is None:
            return
        page_skip = (offset_in_type // PAGE_SIZE) * PAGE_SIZE
        local_idx = offset_in_type - page_skip
        widgets = self._cache[tidx]["pages"].get(page_skip, [])
        if 0 <= local_idx < len(widgets):
            widgets[local_idx] = widget

    @property
    def focus(self):
        """Return the current focus position (int), as expected by ListWalker."""
        return self.focus_position

    def __getitem__(self, pos):
        """Return widget at given position (required by ListWalker.get_focus)."""
        try:
            return self.get(pos)
        except Exception:
            return urwid.Text("(loading...)")

    def next_position(self, pos):
        """Find next valid position after pos. Raises IndexError at end."""
        for tidx in range(len(self._relations)):
            self._ensure_cache(tidx)

        total = self._total_items()
        if total == 0:
            raise IndexError("No items")
        start = pos + 1 if pos is not None else 0
        if start >= total:
            raise IndexError("End of list")
        return start

    def prev_position(self, pos):
        """Find previous valid position before pos. Raises IndexError at start."""
        for tidx in range(len(self._relations)):
            self._ensure_cache(tidx)

        if pos is None or pos <= 0:
            raise IndexError("Start of list")
        return pos - 1

    def positions(self, reverse=False):
        """Return iterable of valid positions."""
        for tidx in range(len(self._relations)):
            self._ensure_cache(tidx)

        total = self._total_items()
        if reverse:
            return range(total - 1, -1, -1)
        return range(total)

    def __len__(self):
        """Return total number of items."""
        for tidx in range(len(self._relations)):
            self._ensure_cache(tidx)
        return self._total_items()

    def marks_changed(self):
        """Clear change flag (required by ListWalker)."""
        pass


class ArchiveListBox(urwid.ListBox):
    """Lazy-loading ListBox for archive hierarchy navigation."""

    def __init__(self, api):
        super().__init__(urwid.SimpleFocusListWalker([]))
        self.api = api
        self._history = []

    def load_archives(self):
        """Load top-level archives and arkivskapere into the list."""
        try:
            archives = self.api.list_archives()
        except Exception:
            archives = []

        items = []
        for arkiv in archives:
            self_url = arkiv.get("_links", {}).get("self", {}).get("href")
            tittel = arkiv.get("tittel", "?")
            date_str = ""
            opprettet = arkiv.get("opprettetDato", "")
            if opprettet:
                date_str = opprettet[:10]

            items.append(
                _make_widget(
                    "%s%s %s" % (date_str, "  " if date_str else "", tittel),
                    path=self_url,
                    has_children=True,
                )
            )

        try:
            arkivskapere = self.api.list_arkivskapere()
        except Exception:
            arkivskapere = []

        for skaper in arkivskapere:
            self_url = skaper.get("_links", {}).get("self", {}).get("href")
            navn = skaper.get("arkivskaperNavn", "?")
            date_str = ""
            opprettet = skaper.get("opprettetDato", "")
            if opprettet:
                date_str = opprettet[:10]

            items.append(
                _make_widget(
                    "%s%s [Arkivskaper] %s"
                    % (date_str, "  " if date_str else "", navn),
                    path=self_url,
                    has_children=True,
                )
            )

        self.body = urwid.SimpleFocusListWalker(items)
        if items:
            self.set_focus(min(len(items) - 1, max(0, len(items) - 1)))

    def expand_node(self, path):
        """Load children for the given entity path using lazy pagination."""
        self._history.append((self.body, self.focus_position))

        if not path:
            self.load_archives()
            return

        walker = LazyChildWalker(self.api, path)
        total_items = walker._total_items()
        if total_items == 0:
            self.body = urwid.SimpleFocusListWalker([_make_widget("(no children)")])
            self.set_focus(0)
            return

        self.body = walker
        self.set_focus(0)  # Reset focus to first child in new list

    def collapse(self):
        """Navigate back to previous level."""
        if self._history:
            body, pos = self._history.pop()
            self.body = body
            target = min(pos, max(0, len(body) - 1))
            self.set_focus(target)

    def get_selected_path(self):
        """Return the path of currently selected node."""
        try:
            idx = self.focus_position
        except Exception:
            return None
        if 0 <= idx < len(self.body):
            node = self.body[idx]
            p = _node_path(node)
            if p:
                return p
        return None

    def _get_root_create_links(self):
        """Return dict of root/arkivstruktur-level ny-* relation links."""
        try:
            root = self.api.get_entity(self.api.baseurl.rstrip("/") + "/")
            links = self.api.parselinks(root.get("_links", {}))

            # Root entity doesn't have ny-* relations directly — they're under arkivstruktur/ sub-endpoint.
            arkivstruktur_rel = "%sarkivstruktur/" % relbaseurl
            if arkivstruktur_rel in links:
                ark_url = self.api.clean_url(links[arkivstruktur_rel])
                try:
                    ark_entity = self.api.get_entity(ark_url)
                    ark_links = self.api.parselinks(ark_entity.get("_links", {}))
                    for k, v in ark_links.items():
                        if "ny-" in k.lower() and k not in links:
                            links[k] = v
                except Exception:
                    pass

            return links
        except Exception:
            return {}

    def available_create_actions(self, path=None, include_root=False):
        """Return list of (create_url, label, required_fields) for this parent.

        When path is None or include_root=True, also includes top-level creation actions.
        """
        if not path:
            links = self._get_root_create_links()
        else:
            try:
                entity, _wp = _fetch_entity(self.api, path)
                links = self.api.parselinks(entity.get("_links", {}))
            except Exception:
                return []

        result = []

        # Get parent title for child creation labels
        parent_title = None
        if path and entity:
            pt = entity.get("tittel") or "(uten tittel)"
            parent_type_key = _get_entity_type_for_path(path)
            type_names = TYPE_NAMES_MAP
            parent_type_name = type_names.get(parent_type_key, "?")
            parent_title = "%s (%s)" % (pt, parent_type_name)

        # Add child creation actions from current scope (entity or root)
        # Check both CREATE_ACTIONS and ROOT_CREATE_ACTIONS — if the entity has the link,
        # it's a valid child creation option regardless of which list it comes from.
        for ny_rel, label, fields in CREATE_ACTIONS + ROOT_CREATE_ACTIONS:
            full_rel = "%s%s" % (relbaseurl, ny_rel)
            if full_rel in links:
                display_label = label
                if parent_title:
                    display_label = "%s [under %s]" % (label, parent_title)
                result.append((links[full_rel], display_label, fields))

        # When include_root is True and we have a path, also add root-level actions
        # that create siblings at top level. These use different URLs than entity-scoped ones
        # (e.g., /arkivstruktur/ny-arkiv vs /arkivstruktur/arkiv/{id}/ny-arkiv).
        if include_root and path:
            root_links = self._get_root_create_links()
            for ny_rel, label, fields in ROOT_CREATE_ACTIONS:
                full_rel = "%s%s" % (relbaseurl, ny_rel)
                if full_rel in root_links:
                    # Use "(top level)" to distinguish sibling creation from child creation
                    result.append(
                        (root_links[full_rel], "%s (top level)" % label, fields)
                    )

        # Probe for møter* creation endpoints not in _links (ny-møtemappe on Arkivdel)
        probed = self._probe_moter_create_links(path, entity if path else None)
        result.extend(probed)

        return result

    def _probe_moter_create_links(self, path, entity):
        """Probe for ny-møter* endpoints that may not appear in _links.

        Available on Arkivdel (ny-møtemappe) and Møtemappe (ny-møteregistrering).
        Returns list of (url, label, fields).
        """
        if not path or not entity:
            return []

        type_key = _get_entity_type_for_path(path)
        probes = {}
        if type_key == "arkivstruktur/arkivdel/":
            probes["ny-moetemappe"] = ("Møtemappe", ["moetedato"])
        elif type_key in ("sakarkiv/moetemappe/", "arkivstruktur/mappe/"):
            probes["ny-moeteregistrering"] = ("Møteregistrering", ["moetedato"])

        if not probes:
            return []

        try:
            self_href = entity.get("_links", {}).get("self", {}).get("href", "")
            if not self_href:
                return []
            clean_self = self.api.clean_url(self_href)
        except Exception:
            return []

        result = []
        pt = entity.get("tittel") or "(uten tittel)"
        parent_type_name = TYPE_NAMES_MAP.get(type_key, "?")
        for ep, (label, fields) in probes.items():
            probe_url = clean_self + "/" + ep
            try:
                gc, _gres = self.api.json_get(probe_url)
                import json as _json

                tmpl = _json.loads(gc)
                parent_title = "%s (%s)" % (pt, parent_type_name) if pt else label
                display_label = (
                    "%s [under %s]" % (label, parent_title) if parent_title else label
                )
                result.append((self.api.clean_url(probe_url), display_label, fields))
            except Exception:
                pass

        return result

    def refresh_selection(self):
        """Reload current view to show newly created entity."""
        try:
            path = self.get_selected_path()
            if path and self._history:
                self.collapse()
                self.expand_node(path)
            else:
                self.load_archives()
        except Exception:
            pass

    def update_detail(self, detail_pane):
        """Update the detail pane for currently selected entity."""
        node = None
        try:
            idx = self.focus_position
            if 0 <= idx < len(self.body):
                node = self.body[idx]
        except Exception:
            pass

        p = _node_path(node)
        if p:
            try:
                entity, _wp = _fetch_entity(self.api, p)
                detail_pane.set_entity(entity)
            except Exception as e:
                detail_pane.set_entity({"_error": str(e)})
        else:
            detail_pane.set_entity(None)


class EntityDetail(urwid.WidgetWrap):
    """Shows metadata for the selected entity."""

    ENTITY_TYPE_MAP = {
        "arkivskaper": "Arkivskaper",
        "arkiv": "Arkiv",
        "arkivdel": "Arkivdel",
        "moetemappe": "Møtemappe",
        "moeteregistrering": "Møteregistrering",
        "moetedeltager": "Moetedeltager",
        "mappe": "Mappe",
        "registrering": "Registrering",
        "dokumentbeskrivelse": "Dokumentbeskrivelse",
        "dokumentobjekt": "Dokumentobjekt",
    }

    def __init__(self, api=None):
        super().__init__(
            urwid.ListBox(
                urwid.SimpleFocusListWalker(
                    [urwid.Text("Select an entity from the tree.")]
                )
            )
        )
        self._header_text = None
        self.api = api

    def set_header_ref(self, header_widget):
        """Store reference to external header text widget for dynamic updates."""
        self._header_text = header_widget

    def _detect_entity_type(self, entity_dict):
        """Detect entity type from _links.self.href URL path or relation keys."""
        # Try to extract type from self href URL
        self_href = entity_dict.get("_links", {}).get("self", {}).get("href", "")
        if not isinstance(self_href, str):
            self_href = ""

        # Parse URL path: /api/arkivstruktur/<type>/<uuid> or /api/sakarkiv/<type>/<uuid>
        import re as _re

        match = _re.search(r"/api/\w+/(\w+)/[a-f0-9\-]+$", self_href)
        if match:
            type_key = match.group(1).lower()
            return self.ENTITY_TYPE_MAP.get(type_key, type_key.title())

        # Fallback: check relation keys in _links (most specific first)
        for rel_key in entity_dict.get("_links", {}).keys():
            if isinstance(rel_key, str):
                for known_type in (
                    "moetemappe",
                    "moeteregistrering",
                    "moetedeltager",
                    "dokumentobjekt",
                    "dokumentbeskrivelse",
                    "registrering",
                    "mappe",
                    "arkivdel",
                    "arkiv",
                    "arkivskaper",
                ):
                    if known_type in rel_key.lower():
                        return self.ENTITY_TYPE_MAP.get(known_type, known_type.title())

        return None

    def _get_children(self, entity_dict):
        """Fetch child entities from the entity's _links relations.

        Returns list of (type_label, date_str, title) tuples for display."""
        def _dbg(*a):
            if getattr(self.api, 'verbose', False):
                print("[DETAIL] " + " ".join(str(x) for x in a), file=sys.stderr)

        if not self.api:
            return []

        try:
            relations = self.api.get_children(entity_dict, CHILD_RELATIONS)
            children = []
            _dbg("relations found:", [(r[0], r[1]) for r in relations])
            for child_type, child_url in relations:
                # Map relation type to display name for children
                type_display_map = {
                    "arkivskaper": "Arkivskaper",
                    "arkiv": "Arkiv",
                    "arkivdel": "Arkivdel",
                    "mappe": "Mappe",
                    "underm.": "Undermappe",
                    "saksm.": "Saksmappe",
                    "reg.": "Registrering",
                    "jp": "Journalpost",
                    "dok.beskr.": "Dokumentbeskrivelse",
                    "dok.obj.": "Dokumentobjekt",
                }

                try:
                    query_url = "%s?$top=10" % child_url
                    resp = self.api.get_entity(query_url)
                    results_count = len(resp.get("results", []))
                    _dbg(child_type, "-> query:", query_url, "-> got", results_count)
                    for child in resp.get("results", []):
                        c_self = child.get("_links", {}).get("self", {}).get("href", "")
                        opprettet = child.get("opprettetDato", "")
                        date_str = opprettet[:10] if opprettet else ""

                        # Determine most specific type for this child from URL path
                        import re as _re

                        m = _re.search(r"/api/\w+/(\w+)/[a-f0-9\-]+$", c_self)
                        child_type_key = m.group(1).lower() if m else ""
                        type_name = self.ENTITY_TYPE_MAP.get(
                            child_type_key, type_display_map.get(child_type, child_type)
                        )

                        # Get title — dokumentobjekt shows filnavn (format.kodenavn)
                        tittel = None
                        if "dokumentobjekt" in type_name.lower():
                            fn = child.get("filnavn", "") or ""
                            fmt = child.get("format", {})

                            parts = []
                            if fn:
                                parts.append(fn)
                            if isinstance(fmt, dict):
                                fkn = fmt.get("kodenavn") or fmt.get("kode") or ""
                                if fkn and fkn.lower() not in (
                                    "unknown",
                                    "ukjent filformat",
                                ):
                                    parts.append(f"({fkn})")
                            tittel = "".join(parts) if parts else "(dokumentobjekt)"

                        tittel = (
                            child.get("arkivskaperNavn")
                            or child.get("tittel")
                            or child.get("klasseID")
                            or tittel
                            or "?"
                        )

                        children.append((date_str, tittel, type_name))
                except Exception:
                    pass

            _dbg("DETAIL FINAL count:", len(children), "(capped at 20)")
            return children[:20]  # Limit to first 20 for display
        except Exception:
            return []

    def set_entity(self, entity_dict):
        if not entity_dict:
            walker = urwid.SimpleFocusListWalker([urwid.Text("No entity selected.")])
            if self._header_text:
                self._header_text.set_text(("header", " Entity Details"))
        elif "_deleted" in entity_dict or (entity_dict.get("tittel") == "[DELETED]"):
            walker = urwid.SimpleFocusListWalker(
                [
                    urwid.Text(("status", "Entity deleted successfully.")),
                ]
            )
            if self._header_text:
                self._header_text.set_text(("header", " Entity Details"))
        else:
            import json as _json

            # Detect entity type and update header
            entity_type = self._detect_entity_type(entity_dict)
            header_label = (
                "%s Details" % entity_type if entity_type else "Entity Details"
            )
            if self._header_text:
                self._header_text.set_text(("header", " %s" % header_label))

            # Show ALL attributes (non-_ keys), sorted for readability
            lines = []
            readonly_keys = {
                "systemID",
                "opprettetDato",
                "opprettetAv",
                "endretDato",
                "endretAv",
            }
            display_keys = [k for k in entity_dict if not k.startswith("_")]

            # Group keys: primary fields first, then remaining alphabetically
            primary_order = [
                "systemID",
                "tittel",
                "beskrivelse",
                "mappeID",
                "klasseID",
                "registreringsID",
                "dokumenttype",
                "journalstatus",
                "avsluttetDato",
            ]
            ordered_keys = [k for k in primary_order if k in display_keys]
            remaining = sorted([k for k in display_keys if k not in primary_order])
            all_keys = ordered_keys + remaining

            for key in all_keys:
                val = entity_dict[key]
                label = "%-24s " % (key + ":")
                formatted = _format_metadata_value(val)
                if formatted is not None:
                    lines.append(urwid.Text("%s%s" % (label, formatted)))
                elif isinstance(val, dict):
                    val = _json.dumps(val, ensure_ascii=False)
                    lines.append(urwid.Text("%-24s %s" % (key + ":", str(val))))
                elif isinstance(val, list):
                    val = ", ".join(str(v) for v in val)
                    lines.append(urwid.Text("%-24s %s" % (key + ":", str(val))))
                else:
                    lines.append(urwid.Text("%-24s %s" % (key + ":", str(val))))

            if not lines:
                lines = [
                    urwid.Text(_json.dumps(entity_dict, indent=2, ensure_ascii=False))
                ]

            # Fetch and display children section
            children = self._get_children(entity_dict)
            if children:
                lines.append(urwid.Text(""))  # Blank separator
                lines.append(urwid.Text(("header", " Children (%d):" % len(children))))
                for date_str, tittel, type_name in children:
                    line = "%s%s %-6s %s" % (
                        date_str,
                        "  " if date_str else "",
                        type_name,
                        tittel,
                    )
                    lines.append(urwid.Text(("body", "  %s" % line)))

            # Add blank line after header
            walker = urwid.SimpleFocusListWalker([urwid.Text("")] + lines)

        self._w.body = walker


class _SelectableText(urwid.Text):
    """Text widget that is selectable so ListBox can navigate through it."""

    def selectable(self):
        return True


class _SubmitEdit(urwid.Edit):
    """Edit widget that propagates 'enter' to parent (for form submission).

    urwid Edit normally consumes Enter by returning 'enter'. We override to
    call super() which handles internal cursor movement but we then return the
    original key so Pile's keypress handler can pass it up to CreateDialog.
    """

    def keypress(self, size, key):
        # Don't let Edit consume Enter — return original key for parent handling
        if key == "enter":
            return key
        return super().keypress(size, key)


class _CompactButton(urwid.WidgetWrap):
    """Compact button that renders as '< Label >' with single-space padding."""

    def __init__(self, label, on_press=None):
        self._on_press = on_press
        text = _SelectableText("< %s >" % label)
        mapped = urwid.AttrMap(text, None, "select_focus")
        super().__init__(mapped)

    def selectable(self):
        return True

    def keypress(self, size, key):
        if key == "enter":
            if self._on_press:
                self._on_press(None)
            return None
        return key


# Map field name → metadata collection endpoint suffix
METADATA_FIELDS = {
    "dokumentmedium": "dokumentmedium",
    "arkivstatus": "arkivstatus",
    "dokumentstatus": "dokumentstatus",
    "dokumenttype": "dokumenttype",
    "tilgangskategori": "tilgangskategori",
    "tilknyttetRegistreringSom": "tilknyttetregistreringsom",
    "arkivdelstatus": "arkivdelstatus",
    "journalstatus": "journalstatus",
    "presedensstatus": "presedensstatus",
    "tilgangsrestriksjon": "tilgangsrestriksjon",
    "kassasjonsvedtak": "kassasjonsvedtak",
    "korrespondanseparttype": "korrespondanseparttype",
    "avskrivningsmaate": "avskrivningsmaate",
    "elektroniskSignaturSikkerhetsnivaa": "elektronisksignatursikkerhetsnivaa",
    "elektroniskSignaturVerifisert": "elektronisksignaturverifisert",
    "format": "format",
    "flytstatus": "flytstatus",
    "klassifikasjonstype": "klassifikasjonstype",
    "journalposttype": "journalposttype",
    "saksstatus": "saksstatus",
    "variantformat": "variantformat",
    "sjekksumAlgoritme": "sjekksumalgoritme",
    "partRolle": "partrolle",
}

MOVE_TYPE_DISPLAY = {
    "arkivstruktur/overarkiv/": "Arkiv",
    "arkivstruktur/overklasse/": "Klasse",
    "arkivstruktur/klassifikasjonssystem/": "Kl.system",
    "arkivstruktur/arkivdel/": "Arkivdel",
    "arkivstruktur/mappe/": "Mappe",
    "arkivstruktur/overmappe/": "Mappe",
    "arkivstruktur/klasse/": "Klasse",
    "sakarkiv/saksmappe/": "Saksmappe",
}


def _fetch_collection(api, url):
    """Paginate through an OData collection endpoint and yield all items."""
    page_size = 50
    skip = 0
    while True:
        try:
            info = api.get_entity("%s?$top=%d&$skip=%d" % (url, page_size, skip))
            results = info.get("results", [])
            if not results:
                break
            for item in results:
                yield item
            if len(results) < page_size:
                break
            skip += page_size
        except Exception:
            break


def _discover_move_targets(api, entity_path, parent_rel_suffixes, entity_links=None):
    """Find valid move targets by querying collection endpoints directly.

    Each OData collection endpoint returns all entities of that type system-wide,
    so no tree walking is needed — just query once and filter in Python.

    Returns list of (display_label, self_href) tuples for candidate parents."""
    # Mapping from "over" parent relation keys to their collection endpoints.
    # When MOVE_CONFIG has overklasse/ or overarkiv/, we discover entities via
    # the base klasse/ or arkiv/ collection respectively.
    parent_to_collection = {
        "arkivstruktur/overklasse/": "arkivstruktur/klasse/",
        "arkivstruktur/overarkiv/": "arkivstruktur/arkiv/",
    }

    try:
        source_path = entity_path.rstrip("/")
        descendants = _collect_descendants(api, entity_path)

        # Include both relative path and full self-href in excluded set
        # (descendants returns full URLs, but source_path is relative)
        source_self_href = None
        try:
            src_entity, _wp2 = _fetch_entity(api, entity_path)
            source_self_href = src_entity.get("_links", {}).get("self", {}).get("href", "").rstrip("/")
        except Exception:
            pass

        excluded = {source_path} | descendants
        if source_self_href:
            excluded.add(source_self_href)

        # Filter out current parent(s) — don't offer "move to where you already are"
        if entity_links:
            for rel_suffix in parent_rel_suffixes:
                full_rel = "%s%s" % (relbaseurl, rel_suffix)
                link_entry = entity_links.get(full_rel, {})
                href = link_entry.get("href")
                if href:
                    excluded.add(href.rstrip("/"))

        results = []

        # Discover root to find top-level collection URLs via _links
        root_url = api.findRelation("%sarkivstruktur/arkiv/" % relbaseurl)
        if not root_url:
            return []

        def add_targets(rel_suffix, display_name):
            """Query a collection endpoint and add results as targets.

            For 'over' keys (overklasse/, overarkiv/), maps to the base
            collection for discovery; otherwise checks directly."""
            # Resolve parent key to its collection endpoint
            collection_key = parent_to_collection.get(rel_suffix, rel_suffix)
            if collection_key not in parent_rel_suffixes and rel_suffix not in parent_rel_suffixes:
                return
            url = api.findRelation("%s%s" % (relbaseurl, collection_key))
            if not url:
                return
            for child in _fetch_collection(api, url):
                c_self = child["_links"]["self"]["href"]
                if c_self.rstrip("/") not in excluded:
                    title = child.get("tittel") or "(uten tittel)"
                    results.append(("%s - %s" % (display_name, title), c_self))

        add_targets("arkivstruktur/overarkiv/", "Arkiv")
        add_targets("arkivstruktur/arkivdel/", "Arkivdel")
        add_targets("arkivstruktur/mappe/", "Mappe")
        add_targets("arkivstruktur/overklasse/", "Kl.")
        add_targets("sakarkiv/saksmappe/", "Saksmappe")
        add_targets("arkivstruktur/klassifikasjonssystem/", "Kl.system")

        # Nikita møter collections (use nikita namespace)
        moter_relbase = "https://nikita.arkivlab.no/noark5/v5/moeter/"
        for mt, label in [
            ("moetemappe", "Møtemappe"),
            ("moeteregistrering", "Møt.reg."),
        ]:
            if any(mt + "/" in r for r in parent_rel_suffixes):
                url = api.findRelation(moter_relbase + mt + "/")
                if url:
                    turl = api.clean_url(url)
                    for child in _fetch_collection(api, turl):
                        c_self = child["_links"]["self"]["href"]
                        title = child.get("tittel") or "(uten tittel)"
                        results.append(("%s - %s" % (label, title), c_self))

        return sorted(results)
    except Exception:
        return []


def _collect_descendants(api, entity_path):
    """Collect all descendant self-hrefs of an entity (to exclude from move targets)."""
    descendants = set()
    try:
        entity, _wp = _fetch_entity(api, entity_path)
        links = api.parselinks(entity.get("_links", {}))

        for rel_suffix in [
            "arkivstruktur/underklasse/",
            "arkivstruktur/underarkiv/",
            "arkivstruktur/mappe/",
            "sakarkiv/saksmappe/",
            "arkivstruktur/registrering/",
            "sakarkiv/journalpost/",
        ]:
            full_rel = "%s%s" % (relbaseurl, rel_suffix)
            if full_rel not in links:
                continue
            url = api.clean_url(links[full_rel])
            for child in _fetch_collection(api, url):
                c_self = child["_links"]["self"]["href"]
                descendants.add(c_self.rstrip("/"))
                # Recurse into children
                descendants.update(_collect_descendants(api, c_self))
    except Exception:
        pass
    return descendants


def _format_metadata_value(val, field_name=None, entity_links=None):
    """Format a value for display. Metadata dicts become '[Kodenavn (Kode)]'."""
    if isinstance(val, dict):
        kode = val.get("kode")
        navn = val.get("kodenavn") or val.get("navn") or val.get("beskrivelse")
        if kode is not None:
            return "[%s (%s)]" % (navn or "???", kode)
    return None


class _SubmitSelect(urwid.WidgetWrap):
    """Dropdown select widget with proper keyboard navigation.

    Left/right cycles through values inline. Enter opens a full list popup
    where up/down navigates options and Enter confirms selection."""

    def __init__(self, label, options, selected_kode=None, loop_ref=None):
        self.options = options
        self._selected_kode = selected_kode or ""
        self._label_prefix = label
        self._loop_ref = loop_ref
        display_text = "%s%s" % (label, self._render_selected())
        self._text_widget = _SelectableText(display_text)
        mapped = urwid.AttrMap(self._text_widget, "select", "select_focus")
        super().__init__(mapped)

    def _render_selected(self):
        """Render current selection as display text: '[Kodenavn (Kode)]' format."""
        target = str(self._selected_kode)
        for kode, kodenavn in self.options:
            if str(kode) == target:
                if not kode:
                    return "[velg verdi]"
                return "[%s (%s)]" % (kodenavn or "???", kode)
        # Value not in list — show raw value
        if not self._selected_kode:
            return "[velg verdi]"
        return "[other (%s)]" % self._selected_kode

    def selectable(self):
        return True

    def get_value(self):
        """Return the selected kode (the actual value to store)."""
        return self._selected_kode

    def _find_idx(self):
        target = str(self._selected_kode)
        for i, (kode, _) in enumerate(self.options):
            if str(kode) == target:
                return i
        return 0

    def _cycle_value(self, direction):
        """Cycle selected value by one step in the given direction."""
        if not self.options:
            return
        idx = self._find_idx()
        new_idx = (idx + direction) % len(self.options)
        self._selected_kode = self.options[new_idx][0]
        self._update_display()

    def _show_option_popup(self, size):
        """Show a full list of options in an overlay popup."""
        self._popup_items = []
        for kode, kodenavn in self.options:
            if not kode:
                continue  # Skip empty placeholder — shown inline as '[velg verdi]' but not selectable
            txt = "  [%s (%s)]" % (kodenavn or "???", kode)
            sel_txt = _SelectableText(txt)
            mapped = urwid.AttrMap(sel_txt, "", "action_focus")
            self._popup_items.append((kode, mapped))

        if not self._popup_items:
            msg = urwid.Text(("warning", "  Ingen alternativer tilgjengelig"))
            simple_popup = urwid.LineBox(urwid.Padding(msg, width=40))
            loop = self._get_loop()
            if not loop:
                return
            old_widget = loop.widget
            overlay = urwid.Overlay(
                simple_popup,
                old_widget,
                align="center",
                valign="middle",
                height=("relative", 20),
            )

            def _close_no_opts(k):
                if k == "esc":
                    loop.widget = old_widget
                    loop.unhandled_input = getattr(loop, "_orig_unhandled", None)
                elif k in ("q", "Q"):
                    raise urwid.ExitMainLoop()

            loop._orig_unhandled = loop.unhandled_input
            loop.unhandled_input = _close_no_opts
            loop.widget = overlay
            return

        list_walker = urwid.SimpleFocusListWalker([it[1] for it in self._popup_items])
        # Find focus index in popup items (may differ from options due to filtered empty option)
        target = str(self._selected_kode)
        cur_popup_idx = None
        for i, (kode, _) in enumerate(self._popup_items):
            if str(kode) == target:
                cur_popup_idx = i
                break
        if cur_popup_idx is not None and cur_popup_idx < len(list_walker):
            list_walker.set_focus(cur_popup_idx)

        lb = urwid.ListBox(list_walker)

        class _PopupListBox(urwid.WidgetWrap):
            def __init__(self, w, select_self, items, loop_ref, old_widget):
                super().__init__(w)
                self._sel = select_self
                self._items = items
                self._loop = loop_ref
                self._old_widget = old_widget

            def selectable(self):
                return True

            def keypress(self, size, key):
                if key == "enter":
                    fp = self._w.body.focus  # Integer position in urwid 3.x
                    if fp is not None and 0 <= fp < len(self._items):
                        new_kode = self._items[fp][0]
                        self._sel._selected_kode = new_kode
                        self._sel._update_display()
                    self._loop.widget = self._old_widget
                    self._loop.unhandled_input = getattr(
                        self._loop, "_orig_unhandled", None
                    )
                    return None
                elif key == "esc":
                    self._loop.widget = self._old_widget
                    self._loop.unhandled_input = getattr(
                        self._loop, "_orig_unhandled", None
                    )
                    return None
                elif key in ("q", "Q"):
                    raise urwid.ExitMainLoop()
                return self._w.keypress(size, key)

            popup_body = urwid.Pile(
            [
                (
                    "pack",
                    urwid.Text(("header", "  Velg verdi (Enter=confirm, Esc=cancel)")),
                ),
                ("pack", urwid.Divider("-")),
                lb,
            ]
        )

        popup_width = min(60, max(len(self._label_prefix) + 40, 30))

        loop = self._get_loop()
        if not loop:
            return

        old_widget = loop.widget
        handler = _PopupListBox(lb, self, self._popup_items, loop, old_widget)
        popup_body.contents[-1] = (handler, ("weight", 1))
        popup_body.focus_position = 2

        popup = urwid.LineBox(urwid.Padding(popup_body, width=popup_width))
        overlay = urwid.Overlay(
            popup,
            old_widget,
            align="center",
            width=min(popup_width + 2, size[0] - 4) if size[0] else popup_width + 2,
            valign="middle",
            height=("relative", 50),
        )

        def _on_unhandled(k):
            if k == "esc":
                loop.widget = old_widget
                loop.unhandled_input = getattr(loop, "_orig_unhandled", None)
            elif k in ("q", "Q"):
                raise urwid.ExitMainLoop()

        loop._orig_unhandled = loop.unhandled_input
        loop.unhandled_input = _on_unhandled
        loop.widget = overlay

    def _get_loop(self):
        """Get the urwid main loop reference passed during construction."""
        return self._loop_ref

    def keypress(self, size, key):
        if key == "enter":
            self._show_option_popup(size)
            return None
        elif key in ("left", "right"):
            direction = -1 if key == "left" else 1
            self._cycle_value(direction)
            return None
        elif key == "esc":
            return key
        # Up/down/pageup/pagedown pass through to parent for field navigation
        return super().keypress(size, key)

    def _update_display(self):
        """Update the innermost Text widget with current selection."""
        label_prefix = getattr(self, "_label_prefix", "")
        text_widget = (
            self._w.original_widget if isinstance(self._w, urwid.AttrMap) else self._w
        )
        text_widget.set_text("%s%s" % (label_prefix, self._render_selected()))


def _fetch_metadata_options(api, field_name):
    """Fetch available options from the metadata API endpoint for a field.

    Returns list of (kode, kodenavn) tuples. Caches results per session."""
    if not hasattr(_fetch_metadata_options, "_cache"):
        _fetch_metadata_options._cache = {}

    if field_name in _fetch_metadata_options._cache:
        return _fetch_metadata_options._cache[field_name]

    endpoint_suffix = METADATA_FIELDS.get(field_name)
    if not endpoint_suffix:
        return None

    try:
        metadata_url = "%s/api/metadata/%s" % (api.baseurl.rstrip("/"), endpoint_suffix)
        info = api.get_entity(metadata_url)
        results = info.get("results", [])
        if not results:
            # No actual values from server — return None so caller falls back to plain text Edit
            options = None
        else:
            options = [(r["kode"], r.get("kodenavn", "")) for r in results]
            # Prepend an empty option for optional fields
            options.insert(0, ("", "(velg verdi / choose value)"))
    except Exception:
        options = None

    _fetch_metadata_options._cache[field_name] = options
    return options


class EditDialog(urwid.Pile):
    """Edit existing entity via RFC 7396 merge-patch (PATCH).

    Shows all editable fields with current values. User edits in place.
    Press Enter to save changes, Esc to cancel.
    """

    def __init__(
        self,
        api,
        entity_path,
        entity_data,
        etag,
        editable_fields,
        loop_ref,
        on_done=None,
    ):
        self.api = api
        self.entity_path = entity_path
        self.etag = etag
        self.editable_fields = editable_fields
        self.loop_ref = loop_ref
        self.on_done = on_done
        self.inputs = {}
        self.original_values = {}

        super().__init__([])

        status_text = (
            "  Editing entity (Enter on text=save, Ctrl+Enter=save, Esc=cancel)"
        )

        form_items = [
            (urwid.Text(("header", status_text)), ("pack", None)),
            (urwid.Divider("-"), ("pack", None)),
        ]

        for field in editable_fields:
            current_raw = entity_data.get(field, "")
            current_val = (
                str(current_raw)
                if not isinstance(current_raw, dict)
                else (
                    current_raw.get("kode", "") if isinstance(current_raw, dict) else ""
                )
            )
            self.original_values[field] = current_val
            meta_options = _fetch_metadata_options(self.api, field)
            if meta_options:
                sel = _SubmitSelect(
                    "  %-15s " % field,
                    meta_options,
                    selected_kode=current_val,
                    loop_ref=self.loop_ref,
                )
                self.inputs[field] = sel
                form_items.append((sel, ("pack", None)))
            else:
                edit = _SubmitEdit("  %-15s " % field, edit_text=str(current_raw))
                self.inputs[field] = edit
                form_items.append((edit, ("pack", None)))

        buttons_row = urwid.Columns(
            [
                ("given", 8, urwid.Text("")),
                _CompactButton("Save", self._on_save),
                ("given", 2, urwid.Divider()),
                _CompactButton("Cancel", self._on_close),
            ]
        )
        form_items.append((buttons_row, ("pack", None)))

        self.contents = form_items
        self.focus_position = 2

    def _on_close(self):
        """Close the dialog overlay."""
        if hasattr(self.loop_ref, "widget"):
            self.loop_ref.widget = self.loop_ref.original_widget

    def keypress(self, size, key):
        if key == "ctrl c":
            raise urwid.ExitMainLoop()
        elif key == "ctrl enter":
            self._on_save()
            return None
        elif key == "enter":
            focused_w = (
                self.contents[self.focus_position][0]
                if self.focus_position < len(self.contents)
                else None
            )
            if isinstance(focused_w, _SubmitSelect):
                return focused_w.keypress(size, key)
            self._on_save()
            return None
        elif key == "esc":
            self._on_close()
            return None
        elif key == "tab":
            next_f = (self.focus_position + 1) % len(self.contents)
            for attempt in range(len(self.contents)):
                pos = (next_f + attempt) % len(self.contents)
                w, _ = self.contents[pos]
                if hasattr(w, "selectable") and w.selectable():
                    self.focus_position = pos
                    return None
            return None
        elif key in ("q", "Q"):
            raise urwid.ExitMainLoop()
        else:
            result = super().keypress(size, key)
            if result is not None:
                return result
            return None

    def _on_save(self):
        """Execute PATCH with RFC 7396 merge-patch for changed fields."""
        patch_data = {}
        for field in self.editable_fields:
            edit_wid = self.inputs.get(field)
            if not edit_wid:
                continue
            new_val = (
                edit_wid.get_value()
                if isinstance(edit_wid, _SubmitSelect)
                else edit_wid.get_edit_text().strip()
            )
            old_val = self.original_values.get(field, "")
            if new_val != old_val:
                patch_data[field] = (
                    {"kode": new_val} if field in METADATA_FIELDS else new_val
                )

        if not patch_data:
            self._on_close()
            return

        try:
            content, _res = self.api.json_merge_patch(
                self.entity_path, patch_data, etag=self.etag
            )
            result = json.loads(content)
            if self.on_done:
                self.on_done(result)
            self._on_close()
        except Exception as e:
            err_lines = ["  Error editing entity:"]
            err_lines.append("  %s" % str(e))
            if hasattr(e, "read"):
                try:
                    body = e.read().decode("utf-8", errors="replace")[:300]
                    if body and body != "{}":
                        err_lines.append("  Server: %s" % body)
                except Exception:
                    pass
            ops_summary = ", ".join("%s=%r" % (k, v) for k, v in patch_data.items())
            err_lines.append("  Patch operations: %s" % ops_summary[:200])
            err_widget = urwid.Text(("error", "\n".join(err_lines)))
            if len(self.contents) > 1:
                self.contents.insert(-1, (err_widget, ("pack", None)))


class MoveDialog(urwid.Pile):
    """Move entity dialog — select target parent from discovered candidates.

    Selection mode: up/down highlights candidate parent, Enter confirms move."""

    def __init__(self, api, source_path, targets, on_done, loop_ref):
        self.api = api
        self.source_path = source_path
        self.targets = targets
        self.on_done = on_done
        self.loop_ref = loop_ref

        # Build selectable list of targets
        items = []
        for label, href in targets:
            txt = _SelectableText("  %s" % label)
            mapped = urwid.AttrMap(txt, "action", "action_focus")
            items.append(mapped)
        self.target_walker = urwid.SimpleFocusListWalker(items)
        self.target_listbox = urwid.ListBox(self.target_walker)

        super().__init__([])
        self._build_dialog()
        if not targets:
            self.focus_position = 2

    def _build_dialog(self):
        """Build or rebuild dialog layout."""
        status_text = "  Move to new parent (Enter=move, Esc=cancel)"
        if not self.targets:
            status_text = "  No valid move targets found"

        contents = [
            (urwid.Text(("header", status_text)), ("pack", None)),
            (urwid.Divider("-"), ("pack", None)),
            (self.target_listbox, ("given", 15)),
            (urwid.Divider("-"), ("pack", None)),
        ]

        btns = urwid.Columns(
            [
                ("given", 8, urwid.Text("")),
                _CompactButton("Move", self._on_move),
                ("given", 2, urwid.Divider()),
                _CompactButton("Cancel", self._on_close),
            ]
        )
        contents.append((btns, ("pack", None)))

        self.contents = contents
        if self.targets:
            self.focus_position = 2
        else:
            self.focus_position = len(contents) - 1

    def _on_close(self):
        """Close the dialog overlay."""
        if hasattr(self.loop_ref, "widget"):
            self.loop_ref.widget = self.loop_ref.original_widget

    def keypress(self, size, key):
        if key == "ctrl c":
            raise urwid.ExitMainLoop()
        elif key in ("q", "Q"):
            raise urwid.ExitMainLoop()
        elif key == "esc":
            self._on_close()
            return None
        elif key == "enter" and self.focus_position < len(self.contents) - 1:
            # If focus is on listbox, confirm move
            if self.targets:
                self._on_move()
            return None
        result = super().keypress(size, key)
        if result is not None:
            return result
        return None

    def _on_move(self):
        """Execute the move operation."""
        if not self.targets or self.target_listbox.focus_position >= len(self.targets):
            self._show_feedback("No target selected", "warning")
            return

        label, href = self.targets[self.target_listbox.focus_position]
        entity_type_key = _get_entity_type_for_path(self.source_path)

        try:
            if not entity_type_key:
                raise ValueError("Unknown entity type for move: %s" % self.source_path)

            # Determine the correct relation key based on target parent type.
            from lib.n5tui.api import relbaseurl

            # over* keys are only for same-type recursive moves:
            #   Mappe↔Mappe uses overmappe/, Klasse↔Klasse uses overklasse/
            # Arkivdel is NOT recursive — it can only move under an Arkiv (via arkiv/).
            source_is_mappe = entity_type_key in (
                "arkivstruktur/mappe/",
                "sakarkiv/saksmappe/",
                "sakarkiv/moetemappe/",
            )
            target_is_mappe = "/saksmappe/" in href or "/moetemappe/" in href or "/mappe/" in href

            if "/arkivstruktur/arkiv/" in href:
                # Arkivdel → Arkiv (cross-type) uses arkiv/; same-type would use overarkiv/
                parent_rel_key = "%sarkivstruktur/arkiv/" % relbaseurl
            elif "/arkivstruktur/klasse/" in href:
                if entity_type_key == "arkivstruktur/klasse/":
                    # Klasse → Klasse (same-type recursive) uses overklasse/
                    parent_rel_key = "%sarkivstruktur/overklasse/" % relbaseurl
                else:
                    # Mappe → Klasse (cross-type) uses klasse/
                    parent_rel_key = "%sarkivstruktur/klasse/" % relbaseurl
            elif "/klassifikasjonssystem/" in href:
                if entity_type_key == "arkivstruktur/klasse/":
                    # Klasse → Klassifikationssystem uses klassifikasjonssystem/
                    parent_rel_key = "%sarkivstruktur/klassifikasjonssystem/" % relbaseurl
                else:
                    raise ValueError(
                        "Cannot move non-klasse entity under Klassifikationssystem"
                    )
            elif "/arkivdel/" in href:
                if entity_type_key == "arkivstruktur/arkivdel/":
                    # Arkivdel is NOT recursive — cannot move under another Arkivdel.
                    raise ValueError(
                        "Cannot move Arkivdel under another Arkivdel (Arkivdel is not recursive)"
                    )
                # Mappe/Saksmappe → Arkivdel uses arkivdel/
                parent_rel_key = "%sarkivstruktur/arkivdel/" % relbaseurl
            elif target_is_mappe:
                if source_is_mappe:
                    # Mappe → Mappe (same-type recursive) uses overmappe/
                    parent_rel_key = "%sarkivstruktur/overmappe/" % relbaseurl
                else:
                    # Registrering, Journalpost → Mappe uses mappe/
                    parent_rel_key = "%sarkivstruktur/mappe/" % relbaseurl
            else:
                raise ValueError(
                    "No move relation key for target: %s (source type: %s)"
                    % (href, entity_type_key)
                )

            result = self.api.move_entity(self.source_path, parent_rel_key, href)
            tittel = result.get("tittel", "(entity)")

            # Close dialog — on_done callback handles tree refresh and status message
            if hasattr(self.loop_ref, "widget"):
                self.loop_ref.widget = self.loop_ref.original_widget
            if self.on_done:
                moved_entity_path = (
                    result.get("_links", {})
                    .get("self", {})
                    .get("href", self.source_path)
                )
                self.on_done(
                    {
                        "moved_entity_path": moved_entity_path,
                        "new_parent_href": href,
                        "tittel": tittel,
                        "target_label": label,
                    }
                )
            return

        except Exception as e:
            err_lines = ["  Move failed:"]
            err_lines.append("  %s" % str(e))

            # Handle Nikita 500 error gracefully — server may not support _links PATCH moves yet
            if hasattr(e, "code") and e.code == 500:
                err_lines.append(
                    "  (Server returned 500. Nikita may not support move via PATCH on this relation.)"
                )
                err_lines.append(
                    "  Try updating Nikita to a version with PatchTest.java merge-patch moves."
                )

            if hasattr(e, "read"):
                try:
                    body = e.read().decode("utf-8", errors="replace")[:300]
                    if body and body != "{}":
                        err_lines.append("  Server: %s" % body)
                except Exception:
                    pass
            self.contents.insert(
                -1, (urwid.Text(("error", "\n".join(err_lines))), ("pack", None))
            )
            return

    def _show_feedback(self, msg, attr="body"):
        """Show a message in the dialog body area."""
        self.contents[-2] = (urwid.Text((attr, "  %s" % msg)), ("pack", None))


HELP_TEXT = [
    "Noark 5 TUI — Keyboard Commands",
    "",
    "Navigation:",
    "  Up / Down         Move selection up/down in tree or list",
    "  Page Up / Down    Scroll one page up/down",
    "  Right             Expand selected node (show children)",
    "  Left              Collapse expanded node (go to parent)",
    "",
    "Entity Actions:",
    "  C                 Create new entity under selected item",
    "  E                 Extend entity (utvid-til-saksmappe, møtemappe, etc.)",
    "  U                 Edit selected entity fields",
    "  D                 Delete selected entity (confirm with Y)",
    "  M                 Move selected entity to a different parent",
    "  F                 Upload file to selected entity (dokumentobjekt)",
    "",
    "Search:",
    "  /                 Search entities by title keyword",
    "",
    "Create/Edit Forms:",
    "  Tab               Cycle focus between fields",
    "  Enter             Open dropdown popup (on metadata field) or submit form",
    "  Ctrl+Enter        Submit/create regardless of focused widget",
    "  Esc               Cancel dialog and return to tree view",
    "",
    "Dropdown Popup:",
    "  Up / Down         Navigate options list",
    "  Enter             Confirm selection and close popup",
    "  Esc / Q           Close popup without changing value",
    "  Left / Right      Cycle values inline (without opening popup)",
    "",
    "General:",
    "  ? or H            Show/hide this help screen",
    "  Q or Ctrl+C       Quit the application",
]


class _HelpDialog(urwid.WidgetWrap):
    """Scrollable help text overlay with right-side scrollbar indicator.

    Shows all keyboard commands. User scrolls with up/down/pageup/pagedown.
    Press Esc, ?, or H to close."""

    def __init__(self, loop_ref, main_pile):
        self._loop = loop_ref
        self._main_pile = main_pile

        # Build text widgets for each line
        lines = [urwid.Text(line) for line in HELP_TEXT]
        walker = urwid.SimpleFocusListWalker(lines)
        listbox = urwid.ListBox(walker)

        # Scrollbar indicator on the right — a Text widget we can update dynamically
        self._scrollbar_text = urwid.Text("░" * 20)
        scrollbar_attr = urwid.AttrMap(self._scrollbar_text, "header", "")

        body_pile = urwid.Pile([listbox])
        scrollable = urwid.AttrMap(body_pile, "", "")

        # Columns: main content + narrow scrollbar track on right
        columns = urwid.Columns(
            [
                (urwid.WEIGHT, 1, listbox),
                (1, scrollbar_attr),
            ],
            dividechars=0,
        )

        self._listbox = listbox
        self._columns = columns

        box = urwid.LineBox(
            urwid.AttrWrap(columns, "body"),
            title=" Help (? or H to close)",
        )
        super().__init__(box)

    def selectable(self):
        return True

    def _update_scrollbar(self, size):
        """Update scrollbar position indicator based on visible area."""
        total = len(self._listbox.body)
        if total == 0:
            return
        max_visible = (size[1] or 20) - 4  # Subtract box borders and header
        if max_visible <= 0:
            max_visible = 3

        focus_pos = self._listbox.focus_position
        # Simple linear mapping: position in list → thumb row in track
        scrollable_range = max(total - max_visible, 1)
        ratio = min(1.0, focus_pos / scrollable_range)
        thumb_row = int(ratio * (max_visible - 1))

        # Build vertical bar with single-char thumb indicator
        chars = []
        for i in range(max_visible):
            if i == thumb_row:
                chars.append("█")
            else:
                chars.append("░")
        self._scrollbar_text.set_text("\n".join(chars))

    def keypress(self, size, key):
        if key == "esc":
            self._loop.widget = self._main_pile
            return None
        elif key in ("q", "Q"):
            raise urwid.ExitMainLoop()
        elif key in ("h", "?"):
            # Toggle help off on ?/H as well
            self._loop.widget = self._main_pile
            return None

        old_focus = self._listbox.focus_position
        result = self._listbox.keypress(size, key)
        new_focus = self._listbox.focus_position

        if new_focus != old_focus or key in ("page up", "page down"):
            self._update_scrollbar(size)
            self._loop.draw_screen()

        return result


class CreateDialog(urwid.Pile):
    """Two-phase dialog: select action type, then fill fields.

    Action mode (default): up/down selects entity type with visible focus highlight.
        Enter switches to form mode (or creates immediately if no fields needed).
    Form mode: edit fields shown on screen. Ctrl+Enter or Enter creates.
        Escape returns to action list with cleared fields.
    Escape in action mode closes the dialog entirely.
    """

    def __init__(self, api, parent_path, available_actions, on_done, loop_ref):
        self.api = api
        self.parent_path = parent_path
        self.available_actions = available_actions
        self.on_done = on_done
        self.loop_ref = loop_ref
        self.inputs = {}
        self._form_mode = False

        # Wrap each action in AttrMap for visible focus highlight.
        # Must use _SelectableText so ListBox.keypress navigates properly (plain Text is not selectable).
        action_items = []
        for a in available_actions:
            txt = _SelectableText("  %s" % a[1])
            mapped = urwid.AttrMap(txt, "action", "action_focus")
            action_items.append(mapped)
        self.action_list = urwid.SimpleFocusListWalker(action_items)
        self.action_select = urwid.ListBox(self.action_list)

        # Initialize Pile first (needs super().__init__ before setting contents)
        super().__init__([])
        # Now build layout — ListBox gets focus so up/down works
        self._build_action_mode()

    def _build_action_mode(self):
        """Rebuild action-mode layout."""
        self.contents = [
            (urwid.Text(("header", " Create New Entity")), ("pack", None)),
            (self.action_select, ("given", 20)),
            (urwid.Divider("-"), ("pack", None)),
            (urwid.Text("Use up/down to choose. Enter to continue."), ("weight", 1)),
        ]
        self.focus_position = 1  # Focus the ListBox so up/down works

    def _on_close(self):
        """Close the dialog overlay."""
        if hasattr(self.loop_ref, "widget"):
            self.loop_ref.widget = self.loop_ref.original_widget

    def _switch_to_form_mode(self):
        """Switch from action selection to form editing mode.

        Shows: header with entity type name, field labels + Edit widgets, buttons.
        Focus goes to first Edit widget so user can start typing immediately.
        Fields are in a scrollable ListBox area so forms with many fields fit on screen.
        """
        try:
            idx = self.action_select.focus_position
        except Exception:
            return
        if idx is None or not self.available_actions:
            return

        self._selected_action = self.available_actions[idx]
        create_url, label, fields = self._selected_action
        self.inputs = {}

        # Auto-add tittel field for møte* entities — server requires it but template may not include it
        if "Møte" in label or "moete" in label.lower():
            if not fields:
                fields = ["tittel"]
            elif "tittel" not in fields:
                fields = ["tittel"] + list(fields)

        status_text = (
            "  Creating: %s (Enter on text=submit, Ctrl+Enter=submit, Esc=back)" % label
        )

        # Fetch template to pre-populate default values in form fields
        import json as _json

        template_defaults = {}
        template_error = None
        try:
            gc, _gres = self.api.json_get(create_url)
            template_defaults = _json.loads(gc)
        except Exception as e:
            template_error = "  Warning: cannot GET %s — no defaults (%s)" % (
                create_url, str(e)[:120]
            )

        # Build field widgets into a scrollable ListBox so forms with many fields fit
        field_widgets = []
        if fields:
            for field in fields:
                meta_options = _fetch_metadata_options(self.api, field)
                default_val = template_defaults.get(field)
                selected_kode = None
                edit_text = ""

                if default_val is not None:
                    if isinstance(default_val, dict):
                        # Metadata fields come as {"kode": "X", "kodenavn": "..."}
                        selected_kode = default_val.get("kode")
                    else:
                        # Plain scalar defaults (string, int, etc.)
                        edit_text = str(default_val)

                if meta_options:
                    sel = _SubmitSelect(
                        "  %-15s " % field,
                        meta_options,
                        selected_kode=selected_kode,
                        loop_ref=self.loop_ref,
                    )
                    self.inputs[field] = sel
                    field_widgets.append(sel)
                else:
                    edit = _SubmitEdit("  %-15s " % field, edit_text=edit_text)
                    self.inputs[field] = edit
                    field_widgets.append(edit)

        buttons_row = urwid.Columns(
            [
                ("given", 8, urwid.Text("")),
                _CompactButton("Create", self._on_create),
                ("given", 2, urwid.Divider()),
                _CompactButton("Cancel", self._on_close),
            ]
        )

        # Order: header + divider (pack) + fields (weight) + buttons (pack).
        # Pack widgets claim their exact size first, weight fills remaining space.
        form_items = [
            (urwid.Text(("header", status_text)), ("pack", None)),
            (urwid.Divider("-"), ("pack", None)),
        ]

        if template_error:
            form_items.append(
                (urwid.Text(("error", template_error)), ("pack", None))
            )
            form_items.append((urwid.Divider("-"), ("pack", None)))

        if field_widgets:
            self._field_listbox = urwid.ListBox(
                urwid.SimpleFocusListWalker(field_widgets)
            )
            form_items.append((self._field_listbox, ("weight", 1)))
        else:
            form_items.append(
                (urwid.Text(("bold", "  No extra fields required")), ("pack", None))
            )

        form_items.append((buttons_row, ("pack", None)))

        self.contents = form_items
        # Focus the scrollable field area or buttons if no fields.
        has_error = template_error is not None
        if field_widgets:
            self.focus_position = 2 + (2 if has_error else 0)
        else:
            self.focus_position = len(self.contents) - 1
        self._form_mode = True

    def _get_focused_widget(self):
        """Get the currently focused widget in form mode."""
        try:
            pile_item = self.contents[self.focus_position][0]
        except (IndexError, KeyError):
            return None

        if not hasattr(self, "_field_listbox"):
            return pile_item

        # If focus is on the field listbox, get its focused widget
        if pile_item is self._field_listbox:
            try:
                return self._field_listbox.body[self._field_listbox.focus_position]
            except (IndexError, AttributeError):
                pass
        return pile_item

    def keypress(self, size, key):
        if key == "ctrl c":
            raise urwid.ExitMainLoop()

        if not self._form_mode:
            # ── Action mode ───────────────────────────────
            if key == "esc":
                self._on_close()
                return None
            elif key in ("q", "Q"):
                raise urwid.ExitMainLoop()
            elif key == "enter":
                try:
                    idx = self.action_select.focus_position
                except Exception:
                    return None
                if idx is not None and self.available_actions:
                    create_url, label, fields = self.available_actions[idx]
                    if fields:
                        self._switch_to_form_mode()
                    else:
                        self._on_create()
                return None
            else:
                # Pass up/down/left/right to Pile super → ListBox handles them
                result = super().keypress(size, key)
                if result is not None:
                    return result
                return None

        # ── Form mode ─────────────────────────────────────
        focused_w = self._get_focused_widget()

        if key == "ctrl enter":
            self._on_create()
            return None
        elif key == "enter":
            if isinstance(focused_w, _SubmitSelect):
                return focused_w.keypress(size, key)
            self._on_create()
            return None
        elif key == "esc":
            # Clear all fields and go back to action mode
            for field, edit_wid in self.inputs.items():
                if isinstance(edit_wid, _SubmitEdit):
                    edit_wid.set_edit_text("")
            self._build_action_mode()
            self.action_list.focus_position = 0  # Reset selection to top
            self._form_mode = False
            return None
        elif key == "tab":
            next_f = (self.focus_position + 1) % len(self.contents)
            for attempt in range(len(self.contents)):
                pos = (next_f + attempt) % len(self.contents)
                w, _ = self.contents[pos]
                if hasattr(w, "selectable") and w.selectable():
                    self.focus_position = pos
                    return None
            return None
        elif key in ("q", "Q"):
            raise urwid.ExitMainLoop()
        else:
            result = super().keypress(size, key)
            if result is not None:
                return result
            return None

    def _on_create(self):
        """Execute the entity creation with detailed error reporting."""
        import json as _json

        if not hasattr(self, "_selected_action"):
            return None
        create_url, label, fields = self._selected_action

        # Fetch template first to get correct types for field coercion
        try:
            gc, _gres = self.api.json_get(create_url)
            default = _json.loads(gc)
        except Exception as e:
            err_lines = ["  Error fetching template:", str(e)]
            if hasattr(e, "read"):
                try:
                    body = e.read().decode("utf-8", errors="replace")[:300]
                    if body and body != "{}":
                        err_lines.append("  Server: %s" % body)
                except Exception:
                    pass
            err_widget = urwid.Text(("error", "\n".join(err_lines)))
            # Remove any previous error widgets before showing new ones
            self.contents = [
                w
                for w in self.contents
                if not (
                    isinstance(w[0], urwid.Text)
                    and len(w[0].get_text()[0]) > 0
                    and w[0].get_text()[0].startswith("  Error")
                )
            ]
            if len(self.contents) > 1:
                self.contents.insert(-1, (err_widget, ("pack", None)))
            return

        data = {}
        for f in fields:
            edit_wid = self.inputs.get(f)
            if isinstance(edit_wid, _SubmitSelect):
                val = edit_wid.get_value() or ""
            else:
                val = edit_wid.get_edit_text().strip() if edit_wid else ""
            if val:
                # Coerce user input to match template default type so server accepts it.
                # e.g., versjonsnummer must be int (1), not string ("1").
                tmpl_val = default.get(f)
                if isinstance(tmpl_val, bool):
                    data[f] = val.lower() in ("true", "1", "ja")
                elif isinstance(tmpl_val, int):
                    try:
                        data[f] = int(val)
                    except ValueError:
                        data[f] = val  # fallback to string if not parseable
                elif isinstance(tmpl_val, dict) or f in METADATA_FIELDS:
                    # Metadata field — wrap kode in dict format
                    data[f] = {"kode": val}
                else:
                    data[f] = val

        for k in default:
            # Only merge non-null defaults; required fields with null values
            # must be provided by the user or are server-side generated.
            if k != "_links" and k not in data and default[k] is not None:
                if k in METADATA_FIELDS:
                    # Ensure metadata field defaults are wrapped as dict
                    data[k] = (
                        {"kode": default[k]}
                        if isinstance(default[k], str)
                        else default[k]
                    )
                else:
                    data[k] = default[k]

        try:
            content, res = self.api.json_post(create_url, data)
            result = _json.loads(content)

            self.on_done(result)
        except Exception as e:
            # Remove any previous error widgets before showing new ones
            self.contents = [
                w
                for w in self.contents
                if not (
                    isinstance(w[0], urwid.Text)
                    and len(w[0].get_text()[0]) > 0
                    and w[0].get_text()[0].startswith("  Error")
                )
            ]
            # Build detailed error message with diagnostics
            err_lines = ["  Error creating %s:" % label]
            err_lines.append("  %s" % str(e))

            # Try to read HTTP response body for server-side details
            if hasattr(e, "read"):
                try:
                    body = e.read().decode("utf-8", errors="replace")[:300]
                    if body and body != "{}":
                        err_lines.append("  Server: %s" % body)
                except Exception:
                    pass

            # Show what was sent to help diagnose
            data_summary = ", ".join(
                "%s=%r" % (k, v) for k, v in data.items() if k != "_links"
            )
            err_lines.append("  Sent: %s" % data_summary[:200])

            # Show which fields were empty vs filled
            def _input_val(w):
                return (
                    w.get_value()
                    if isinstance(w, _SubmitSelect)
                    else w.get_edit_text().strip()
                )

            missing = [
                f
                for f in fields
                if not (self.inputs.get(f) and _input_val(self.inputs[f]))
            ]
            if missing:
                err_lines.append(
                    "  Empty fields: %s (fill them before creating)"
                    % ", ".join(missing)
                )

            err_widget = urwid.Text(("error", "\n".join(err_lines)))
            # Insert error before buttons (last item)
            if len(self.contents) > 1:
                self.contents.insert(-1, (err_widget, ("pack", None)))


# ── Extend (utvid-til) support ───────────────────────────────────────


EXTEND_ACTIONS = [
    # Standard N5TG sakarkiv extends per spec (06-konsepter_og_prinsipper.rst lines 665, 950, 1272)
    ("sakarkiv/utvid-til-saksmappe/", "Utvid til Saksmappe", ["saksansvarlig"]),
    ("sakarkiv/utvid-til-journalpost/", "Utvid til Journalpost", ["tittel"]),
    # Nikita-specific møter extends (not in N5TG spec, relation keys use nikita namespace)
    ("moeter/utvid-til-moetemappe/", "Utvid til Møtemappe", ["moetedato"]),
]


def _discover_extend_actions(api, path):
    """Discover available utvid-til-* actions for an entity.

    Returns list of (extend_url, label, fields).
    """
    try:
        entity, working_path = _fetch_entity(api, path)
        links = api.parselinks(entity.get("_links", {}))
    except Exception:
        return []

    result = []
    for ny_rel, label, fields in EXTEND_ACTIONS:
        full_rel = "%s%s" % (relbaseurl, ny_rel)
        if full_rel in links:
            result.append((api.clean_url(links[full_rel]), label, fields))

    # Nikita möter-specific extends are NOT advertised in _links — probe directly.
    # The endpoint is at the entity's mappe path + /utvid-til-moetemappe
    if "moeter/utvid-til-moetemappe/" not in [a[0] for a in result]:
        try:
            self_href = entity.get("_links", {}).get("self", {}).get("href", "")
            mappe_path = _resolve_mappe_path(api, self_href, working_path)
            probe_url = mappe_path.rstrip("/") + "/utvid-til-moetemappe"
            gc, gres = api.json_get(probe_url)
            tmpl = json.loads(gc)
            result.append(
                (api.clean_url(probe_url), "Utvid til Møtemappe", ["moetedato"])
            )
        except Exception:
            pass

    return result


def _resolve_mappe_path(api, self_href, original_path):
    """Resolve a möter entity's working mappe path.

    Nikita generates self-hrefs like /api/arkivstruktur/moetemappe/{id} which 404.
    The actual working path is /api/arkivstruktur/mappe/{id}. Try the original path,
    then fall back to constructing the mappe path from the self-href.
    """
    # First try the original path (might already be a working mappe path)
    if original_path:
        try:
            api.get_entity(original_path)
            return original_path
        except Exception:
            pass

    # Extract ID and base URL from self-href, construct mappe fallback
    if not self_href:
        return ""
    parts = self_href.rstrip("/").rsplit("/", 1)
    if len(parts) == 2:
        return parts[0].replace("/moetemappe", "/mappe") + "/" + parts[1]

    # Last resort: try the original path as-is
    return original_path or ""


def _fetch_entity(api, path):
    """Fetch an entity by path, with möter-specific fallback.

    Nikita generates self-hrefs for mötemapper like /api/arkivstruktur/moetemappe/{id}
    which 404. This wrapper tries the original path first, then falls back to
    /api/arkivstruktur/mappe/{id}. Returns (entity_dict, working_path).
    """
    if not path:
        return None, ""
    try:
        entity = api.get_entity(path)
        return entity, path
    except Exception:
        pass

    # Möter fallback: construct mappe path from mötemappe self-href
    parts = path.rstrip("/").rsplit("/", 1)
    if len(parts) == 2:
        base = parts[0]
        eid = parts[1]
        for mt in ["moetemappe", "moeteregistrering", "moetedeltager"]:
            if "/" + mt in base:
                mappe_path = base.replace("/" + mt, "/mappe") + "/" + eid
                try:
                    return api.get_entity(mappe_path), mappe_path
                except Exception:
                    pass

    raise


def _get_selected_working_path(tree_listbox):
    """Get selected path with möter fallback resolution."""
    raw = tree_listbox.get_selected_path()
    if not raw:
        return None, None
    try:
        entity, working = _fetch_entity(tree_listbox.api, raw)
        return entity, working
    except Exception as e:
        return None, (raw, str(e))


class ExtendDialog(urwid.Pile):
    """Two-phase dialog for utvid-til-* extend operations.

    Phase 1: list available extend actions (utvid-til-saksmappe, etc.)
    Phase 2: show form with template fields to fill in before extending.
    """

    def __init__(self, api, path, available_actions, on_done, loop_ref):
        self.api = api
        self.path = path
        self.available_actions = available_actions
        self.on_done = on_done
        self.loop_ref = loop_ref
        self.inputs = {}
        self._selected_action = None
        self._form_mode = False

        super().__init__([])
        self._build_action_mode()

    def _build_action_mode(self):
        """Build the action selection list view."""
        items = []
        for _, label, fields in self.available_actions:
            field_hint = " (%d fields)" % len(fields) if fields else ""
            items.append(
                urwid.AttrMap(
                    _SelectableText("  %s%s" % (label, field_hint)),
                    "action",
                    "action_focus",
                )
            )

        action_list = urwid.ListBox(urwid.SimpleFocusListWalker(items))
        self.action_select = action_list

        status_text = ("header", "  Select Extend Action:")

        self.contents = [
            (urwid.Text(status_text), ("pack", None)),
            (urwid.Divider("-"), ("pack", None)),
            (action_list, ("weight", 1)),
            (
                urwid.Filler(urwid.Text(("status", "  Enter=select, Esc=cancel"))),
                ("pack", None),
            ),
        ]
        self.focus_position = 2

    def _switch_to_form_mode(self):
        """Switch from action selection to form editing mode."""
        try:
            idx = self.action_select.focus_position
        except Exception:
            return
        if idx is None or not self.available_actions:
            return

        self._selected_action = self.available_actions[idx]
        create_url, label, fields = self._selected_action
        self.inputs = {}

        status_text = "  Extending: %s (Enter=extend, Esc=back)" % label

        # Build field widgets into a scrollable ListBox so forms with many fields fit
        field_widgets = []
        if fields:
            for field in fields:
                meta_options = _fetch_metadata_options(self.api, field)
                if meta_options:
                    sel = _SubmitSelect(
                        "  %-15s " % field, meta_options, loop_ref=self.loop_ref
                    )
                    self.inputs[field] = sel
                    field_widgets.append(sel)
                else:
                    edit = _SubmitEdit("  %-15s " % field)
                    self.inputs[field] = edit
                    field_widgets.append(edit)

        buttons_row = urwid.Columns(
            [
                ("given", 8, urwid.Text("")),
                _CompactButton("Extend", self._on_extend),
                ("given", 2, urwid.Divider()),
                _CompactButton("Cancel", self._on_close),
            ]
        )

        # Order: header + divider (pack) + fields (weight) + buttons (pack).
        form_items = [
            (urwid.Text(("header", status_text)), ("pack", None)),
            (urwid.Divider("-"), ("pack", None)),
        ]

        if field_widgets:
            self._field_listbox = urwid.ListBox(
                urwid.SimpleFocusListWalker(field_widgets)
            )
            form_items.append((self._field_listbox, ("weight", 1)))
        else:
            form_items.append(
                (urwid.Text(("bold", "  No extra fields required")), ("pack", None))
            )

        form_items.append((buttons_row, ("pack", None)))

        self.contents = form_items
        # Focus the scrollable field area (index 2) or no-fields text/buttons if no fields
        if field_widgets:
            self.focus_position = 2
        else:
            self.focus_position = len(self.contents) - 1
        self._form_mode = True

    def _get_focused_widget(self):
        """Get the currently focused widget in form mode."""
        try:
            pile_item = self.contents[self.focus_position][0]
        except (IndexError, KeyError):
            return None

        if not hasattr(self, "_field_listbox"):
            return pile_item

        # If focus is on the field listbox, get its focused widget
        if pile_item is self._field_listbox:
            try:
                return self._field_listbox.body[self._field_listbox.focus_position]
            except (IndexError, AttributeError):
                pass
        return pile_item

    def keypress(self, size, key):
        if key == "ctrl c":
            raise urwid.ExitMainLoop()

        if not self._form_mode:
            if key == "esc":
                self._on_close()
                return None
            elif key in ("q", "Q"):
                raise urwid.ExitMainLoop()
            elif key == "enter":
                try:
                    idx = self.action_select.focus_position
                except Exception:
                    return None
                if idx is not None and self.available_actions:
                    create_url, label, fields = self.available_actions[idx]
                    if fields:
                        self._switch_to_form_mode()
                    else:
                        self._on_extend()
                return None
            elif key in ("q", "Q"):
                raise urwid.ExitMainLoop()
            else:
                result = super().keypress(size, key)
                if result is not None:
                    return result
                return None

        focused_w = self._get_focused_widget()

        if key == "ctrl enter":
            self._on_extend()
            return None
        elif key == "enter":
            if isinstance(focused_w, _SubmitSelect):
                return focused_w.keypress(size, key)
            self._on_extend()
            return None
        elif key == "esc":
            # Clear all fields and go back to action mode
            for field, edit_wid in self.inputs.items():
                if isinstance(edit_wid, _SubmitEdit):
                    edit_wid.set_edit_text("")
            self._build_action_mode()
            try:
                self.action_list.focus_position = 0
            except Exception:
                pass
            self._form_mode = False
            return None
        elif key == "tab":
            next_f = (self.focus_position + 1) % len(self.contents)
            for attempt in range(len(self.contents)):
                pos = (next_f + attempt) % len(self.contents)
                w, _ = self.contents[pos]
                if hasattr(w, "selectable") and w.selectable():
                    self.focus_position = pos
                    return None
            return None
        elif key in ("q", "Q"):
            raise urwid.ExitMainLoop()
        else:
            result = super().keypress(size, key)
            if result is not None:
                return result
            return None

    def _on_extend(self):
        """Execute the extend operation (utvid-til-*)."""
        import json as _json

        if not hasattr(self, "_selected_action"):
            return None
        extend_url, label, fields = self._selected_action

        try:
            gc, _gres = self.api.json_get(extend_url)
            default = _json.loads(gc)
        except Exception as e:
            err_lines = ["  Error fetching template:", str(e)]
            if hasattr(e, "read"):
                try:
                    body = e.read().decode("utf-8", errors="replace")[:300]
                    if body and body != "{}":
                        err_lines.append("  Server: %s" % body)
                except Exception:
                    pass
            self._show_error("\n".join(err_lines))
            return

        data = {}
        for f, edit_wid in self.inputs.items():
            if isinstance(edit_wid, _SubmitSelect):
                val = edit_wid.get_value() or ""
            else:
                val = edit_wid.get_edit_text().strip() if edit_wid else ""
            if val:
                tmpl_val = default.get(f)
                if isinstance(tmpl_val, bool):
                    data[f] = val.lower() in ("true", "1", "ja")
                elif isinstance(tmpl_val, int):
                    try:
                        data[f] = int(val)
                    except ValueError:
                        data[f] = val
                elif isinstance(tmpl_val, dict) or f in METADATA_FIELDS:
                    data[f] = {"kode": val}
                else:
                    data[f] = val

        for k in default:
            if k != "_links" and k not in data and default[k] is not None:
                if k in METADATA_FIELDS:
                    data[k] = (
                        {"kode": default[k]}
                        if isinstance(default[k], str)
                        else default[k]
                    )
                else:
                    data[k] = default[k]

        # Spec says utvid-til-* uses PUT (not POST), content-type application/vnd.noark5+json
        try:
            _, resp = self.api.put(
                extend_url, json.dumps(data), "application/vnd.noark5+json"
            )
            result_text = resp.read().decode("utf-8", errors="replace")
            result_data = _json.loads(result_text) if result_text.strip() else {}
        except Exception as e:
            err_lines = ["  Extend failed:", str(e)]
            if hasattr(e, "read"):
                try:
                    body = e.read().decode("utf-8", errors="replace")[:300]
                    if body and body != "{}":
                        err_lines.append("  Server: %s" % body)
                except Exception:
                    pass
            self._show_error("\n".join(err_lines))
            return

        # Close dialog
        self.loop_ref.widget = (
            getattr(self.loop_ref, "original_widget", None) or self.loop_ref.widget
        )
        self.on_done(result_data)

    def _on_close(self):
        """Cancel and close the dialog."""
        self.loop_ref.widget = (
            getattr(self.loop_ref, "original_widget", None) or self.loop_ref.widget
        )
        if self.on_done:
            self.on_done(None)

    def _show_error(self, message):
        """Display error messages in the form view."""
        err_widget = urwid.Text(("error", message))
        # Remove any previous error widgets
        self.contents = [
            w
            for w in self.contents
            if not (
                isinstance(w[0], urwid.Text)
                and w[0].get_text()[0].startswith("  Error")
            )
        ]
        if len(self.contents) > 1:
            self.contents.insert(-1, (err_widget, ("pack", None)))


def create_tui(baseurl=None, username=None, password=None):
    """Create and return the urwid MainLoop for the TUI."""
    from .api import N5API

    api = N5API(baseurl=baseurl, username=username, password=password)
    try:
        api.ensure_login()
        login_status = "OK"
    except Exception as e:
        login_status = "FAILED: %s" % e

    tree_listbox = ArchiveListBox(api)

    status_bar = urwid.Text("")

    def set_status(msg):
        status_bar.set_text(("status", msg))

    set_status(
        "%s - Login: %s | h=help  q=quit"
        % (baseurl or "http://localhost:8092/noark5v5/", login_status)
    )

    left_pane = urwid.LineBox(
        urwid.Pile(
            [
                ("pack", urwid.Text(("header", " Archive Tree"))),
                tree_listbox,
            ]
        )
    )

    _detail_header = urwid.Text(("header", " Entity Details"))

    detail_pane = EntityDetail(api)
    detail_pane.set_header_ref(
        _detail_header
    )  # Allow detail pane to update header dynamically

    right_pane = urwid.LineBox(
        urwid.Pile(
            [
                ("pack", _detail_header),
                detail_pane,
            ]
        )
    )

    columns = urwid.Columns(
        [
            ("weight", 1, left_pane),
            ("weight", 1, right_pane),
        ]
    )

    main_pile = urwid.Pile(
        [
            ("weight", 1, columns),
            ("pack", urwid.AttrWrap(status_bar, "status")),
        ]
    )

    orig_keypress = tree_listbox.keypress

    delete_pending_path = [
        None
    ]  # Path waiting for Y/anything confirmation (list for closure mutability)
    upload_pending_url = [None]  # URL to POST file to, pending user confirmation

    def handle_key(key):
        if key == "q":
            raise urwid.ExitMainLoop()
        elif key in ("?", "h"):
            help_dialog = _HelpDialog(loop, main_pile)
            overlay = urwid.Overlay(
                help_dialog,
                main_pile,
                align="center",
                width=("relative", 70),
                valign="middle",
                height=("relative", 60),
            )
            loop.original_widget = loop.widget
            loop.widget = overlay
        elif key == "esc":
            loop.widget = main_pile
            delete_pending_path[0] = None
            upload_pending_url[0] = None
        elif key == "y" and delete_pending_path[0]:
            # Confirm pending delete
            path = delete_pending_path[0]
            try:
                api.delete_entity(path)
                on_deleted(True, None)
            except Exception as e:
                body = ""
                if hasattr(e, "read"):
                    try:
                        body = e.read().decode("utf-8", errors="replace")[:200]
                    except Exception:
                        pass
                err_msg = str(e)
                if body and body != "{}":
                    err_msg += " — Server: %s" % body
                on_deleted(None, "Delete failed: %s" % err_msg)
            delete_pending_path[0] = None
        elif delete_pending_path[0]:
            # Cancel pending delete (any key other than y/esc/q)
            delete_pending_path[0] = None
            set_status("Delete cancelled")
        elif key == "c":
            path = tree_listbox.get_selected_path()
            # At top level: show both child actions and root-level sibling creation options
            include_root = not path or not tree_listbox._history
            available = tree_listbox.available_create_actions(
                path, include_root=include_root
            )
            if not available:
                set_status("No creation options for selected entity")
                return
            dialog = CreateDialog(
                api, path, available, lambda r: on_created(r, detail_pane), loop
            )
            overlay = urwid.Overlay(
                urwid.LineBox(dialog),
                main_pile,
                align="center",
                width=("relative", 70),
                valign="middle",
                height=("relative", 50),
            )
            loop.original_widget = loop.widget
            loop.widget = overlay
        elif key == "e":
            path = tree_listbox.get_selected_path()
            if not path:
                set_status("No entity to extend (select an item first)")
                return
            available = _discover_extend_actions(api, path)
            if not available:
                set_status("No extend options for this entity type")
                return

            def on_extended(result):
                tittel = result.get("tittel", "?") if result else "?"
                if "saksref" in (result or {}):
                    set_status("Extended to Saksmappe: %s" % tittel)
                elif "moetedato" in (result or {}):
                    set_status("Extended to Møtemappe/Møteregistrering: %s" % tittel)
                else:
                    set_status("Extended entity: %s" % tittel)
                try:
                    detail_pane.set_entity(result)
                except Exception:
                    pass
                try:
                    tree_listbox.refresh_selection()
                except Exception:
                    pass

            dialog = ExtendDialog(api, path, available, on_extended, loop)
            overlay = urwid.Overlay(
                urwid.LineBox(dialog),
                main_pile,
                align="center",
                width=("relative", 70),
                valign="middle",
                height=("relative", 50),
            )
            loop.original_widget = loop.widget
            loop.widget = overlay
        elif key == "u":
            path = tree_listbox.get_selected_path()
            if not path:
                set_status("No entity to update (select an item first)")
                return
            try:
                entity, etag = api.get_entity_with_etag(path)
            except Exception as ex:
                set_status("Cannot load entity for editing: %s" % ex)
                return
            editable_fields = [f for f in _get_entity_fields(path) if f in entity]
            if not editable_fields:
                # Fall back to any non-system, non-readonly fields present on the entity
                readonly = {
                    "systemID",
                    "opprettetDato",
                    "opprettetAv",
                    "endretDato",
                    "endretAv",
                }
                editable_fields = [
                    f for f in entity if not f.startswith("_") and f not in readonly
                ]
            if not editable_fields:
                set_status("No editable fields on this entity")
                return

            def on_edited(result):
                tittel = result.get("tittel", "?")
                set_status("Updated %s" % tittel)
                try:
                    detail_pane.set_entity(result)
                except Exception:
                    pass
                try:
                    tree_listbox.refresh_selection()
                except Exception:
                    pass

            dialog = EditDialog(
                api, path, entity, etag, editable_fields, loop, on_done=on_edited
            )
            overlay = urwid.Overlay(
                urwid.LineBox(dialog),
                main_pile,
                align="center",
                width=("relative", 70),
                valign="middle",
                height=("relative", 50),
            )
            loop.original_widget = loop.widget
            loop.widget = overlay
        elif key == "m":
            path = tree_listbox.get_selected_path()
            if not path:
                set_status("No entity to move (select an item first)")
                return

            # Check if this entity type is movable
            ent_type_key = _get_entity_type_for_path(path)
            if not ent_type_key or ent_type_key not in MOVE_CONFIG:
                set_status("Entity type cannot be moved")
                return

            parent_rels = MOVE_CONFIG[ent_type_key]

            # Fetch entity to get current parent links for filtering
            try:
                entity_data, _wp = _fetch_entity(api, path)
                ent_links = entity_data.get("_links", {})
            except Exception:
                ent_links = None

            # Discover valid move targets
            targets = _discover_move_targets(api, path, parent_rels, ent_links)
            if not targets:
                set_status("No valid move targets found for this entity")
                return

            def on_moved(result):
                """Refresh tree after successful move — navigate to new parent."""
                try:
                    moved_path = result.get("moved_entity_path", "")
                    new_parent = result.get("new_parent_href", "")
                    tittel = result.get("tittel", "?")

                    # Navigate to the new parent container
                    if new_parent and tree_listbox._history:
                        tree_listbox.expand_node(new_parent)
                        set_status("Moved '%s' — expanded new parent" % tittel)

                        # Try to locate and focus on moved entity in new position
                        try:
                            for i in range(len(tree_listbox.body)):
                                node = tree_listbox.body[i]
                                if _node_path(node) == moved_path:
                                    tree_listbox.set_focus(i)
                                    break
                        except Exception:
                            pass

                    # Update detail pane with moved entity
                    if moved_path:
                        try:
                            refreshed = api.get_entity(moved_path)
                            detail_pane.set_entity(refreshed)
                        except Exception:
                            pass

                except Exception as e:
                    set_status("Move refresh error: %s" % e)

            dialog = MoveDialog(api, path, targets, on_moved, loop)
            overlay = urwid.Overlay(
                urwid.LineBox(dialog),
                main_pile,
                align="center",
                width=("relative", 70),
                valign="middle",
                height=("relative", 50),
            )
            loop.original_widget = loop.widget
            loop.widget = overlay

    def on_created(result, detail):
        """Handle completion of entity creation."""
        if result:
            tittel = result.get("tittel", "?")
            set_status("Created %s" % tittel)
            try:
                detail.set_entity(result)
            except Exception:
                pass

            # Refresh tree view to show newly created entity
            try:
                if tree_listbox._history:
                    parent_path = tree_listbox.body.parent_path
                    tree_listbox.collapse()
                    tree_listbox.expand_node(parent_path)
                else:
                    tree_listbox.load_archives()
            except Exception as e:
                set_status("Error refreshing view after creation: %s" % e)

        # Restore main view after creation — use original_widget saved before overlay was shown
        loop.widget = loop.original_widget

    def on_deleted(result, error_msg):
        """Handle completion of entity deletion."""
        if result is not None:
            # Refresh current view — can't mutate LazyChildWalker in-place
            try:
                if tree_listbox._history:
                    # Save the PARENT path (container holding children) before collapsing
                    parent_path = tree_listbox.body.parent_path
                    tree_listbox.collapse()
                    tree_listbox.expand_node(parent_path)
                else:
                    # Root level archive list — just reload
                    tree_listbox.load_archives()
            except Exception as e:
                set_status(f"Delete refresh error: {e}")
                return
            set_status("Entity deleted")
            detail_pane.set_entity({"tittel": "[DELETED]"})
            _update_focus_indicator(tree_listbox.body)
            loop.draw_screen()
        elif error_msg:
            set_status(error_msg)

    def wrapped_keypress(size, key):
        if key in ("q", "Q"):
            raise urwid.ExitMainLoop()
        elif key == "esc":
            loop.widget = main_pile
            return None
        elif key == "d":
            path = tree_listbox.get_selected_path()
            try:
                node = tree_listbox.body[tree_listbox.focus_position]
                label = getattr(node, "label", "(entity)")
            except Exception:
                label = "(entity)"
            if not path:
                set_status("No entity to delete (select an item first)")
                return None
            # Show confirmation in status bar — press Y to confirm, any other key cancels
            delete_pending_path[0] = path
            set_status(f'Delete "{label}"? Press Y to confirm, any other key to cancel')
            loop.draw_screen()
            return None
        elif key == "right":
            path = tree_listbox.get_selected_path()
            try:
                node = tree_listbox.body[tree_listbox.focus_position]
            except Exception:
                return orig_keypress(size, key)
            if _node_has_children(node):
                tree_listbox.expand_node(path or None)
                tree_listbox.update_detail(detail_pane)
                _update_focus_indicator(tree_listbox.body)
                loop.draw_screen()
                return None
        elif key == "left":
            tree_listbox.collapse()
            tree_listbox.update_detail(detail_pane)
            _update_focus_indicator(tree_listbox.body)
            loop.draw_screen()
            return None
        elif key == "/":
            # Search entities by title
            class SearchDialog(urwid.Pile):
                def __init__(self, _loop_ref, _main_pile, _tree_listbox, _detail_pane):
                    self._loop_ref = _loop_ref
                    self._main_pile = _main_pile
                    self._tree_listbox = _tree_listbox
                    self._detail_pane = _detail_pane
                    edit_wid = urwid.Edit(edit_text="", multiline=False)

                    super().__init__(
                        [
                            urwid.Text(
                                ("header", "  Search (Enter to search, Esc to cancel):")
                            ),
                            urwid.Divider(),
                            edit_wid,
                        ]
                    )
                    self.edit_widget = edit_wid

                def keypress(self, size, key):
                    if key == "esc":
                        self._loop_ref.widget = self._main_pile
                    elif key == "enter":
                        query = self.edit_widget.get_edit_text().strip()
                        if query:
                            import time as _time

                            t0 = _time.time()
                            matches = api.search_entities(query)
                            elapsed = "%.2f" % (_time.time() - t0)
                            if not matches:
                                set_status(
                                    f'No entities matching "{query}" ({elapsed}s)'
                                )
                            else:
                                items = [_make_widget(m[1], path=m[0]) for m in matches]
                                self._tree_listbox.body = urwid.SimpleFocusListWalker(
                                    items
                                )
                                self._tree_listbox.set_focus(0)
                                set_status(
                                    f'Found {len(matches)} result(s) matching "{query}" ({elapsed}s)'
                                )
                        else:
                            set_status("Enter a search term")
                        self._loop_ref.widget = self._main_pile
                    elif key in ("q", "Q"):
                        raise urwid.ExitMainLoop()
                    return super().keypress(size, key)

            dialog = SearchDialog(loop, main_pile, tree_listbox, detail_pane)
            overlay = urwid.Overlay(
                urwid.LineBox(dialog),
                main_pile,
                align="center",
                width=("relative", 60),
                valign="middle",
                height=5,
            )
            loop.original_widget = loop.widget
            loop.widget = overlay

        elif key == "f":
            # File upload — check if current entity has fil/ relation
            path = tree_listbox.get_selected_path()
            if not path:
                set_status("No entity selected for upload")
                return
            try:
                entity_data, _wp = _fetch_entity(api, path)
                ent_links = api.parselinks(entity_data.get("_links", {}))
                fil_rel = "%sarkivstruktur/fil/" % relbaseurl
                if fil_rel not in ent_links:
                    set_status(
                        "No file upload endpoint on this entity (only Dokumentobjekt supports upload)"
                    )
                    return
            except Exception as ex:
                set_status(f"Cannot check upload capability: {ex}")
                return

            # Show simple file picker dialog
            fil_url = api.clean_url(ent_links[fil_rel])

            class UploadDialog(urwid.Pile):
                def __init__(self, _url, _loop_ref, _main_pile, _upload_pending):
                    self.upload_url = _url
                    self._loop_ref = _loop_ref
                    self._main_pile = _main_pile
                    self._upload_pending = _upload_pending
                    edit_wid = urwid.Edit(edit_text="", multiline=False)

                    super().__init__(
                        [
                            urwid.Text(("header", "  Upload File to Dokumentobjekt")),
                            urwid.Divider(),
                            urwid.Text("File path:"),
                            edit_wid,
                            urwid.Divider(),
                            urwid.Text(("status", "  Enter=upload, Esc=cancel")),
                        ]
                    )
                    self.edit_widget = edit_wid

                def keypress(self, size, key):
                    if key == "esc":
                        self._loop_ref.widget = self._main_pile
                        self._upload_pending[0] = None
                    elif key == "enter":
                        filepath = self.edit_widget.get_edit_text().strip()
                        if not filepath:
                            set_status("Enter a file path to upload")
                            self._loop_ref.widget = self._main_pile
                            self._upload_pending[0] = None
                            return
                        try:
                            api.upload_file(self.upload_url, filepath)
                            import os

                            fname = os.path.basename(filepath)
                            set_status(f"Uploaded {fname} successfully")
                            refreshed = api.get_entity(path)
                            detail_pane.set_entity(refreshed)
                        except Exception as e:
                            err_msg = str(e)
                            if hasattr(e, "read"):
                                try:
                                    body = e.read().decode("utf-8", errors="replace")[
                                        :200
                                    ]
                                    if body and body != "{}":
                                        err_msg += f" — Server: {body}"
                                except Exception:
                                    pass
                            set_status(f"Upload failed: {err_msg}")
                        self._loop_ref.widget = self._main_pile
                        self._upload_pending[0] = None
                    elif key in ("q", "Q"):
                        raise urwid.ExitMainLoop()
                    return super().keypress(size, key)

            dialog = UploadDialog(fil_url, loop, main_pile, upload_pending_url)
            overlay = urwid.Overlay(
                urwid.LineBox(dialog),
                main_pile,
                align="center",
                width=("relative", 60),
                valign="middle",
                height=7,
            )
            loop.original_widget = loop.widget
            loop.widget = overlay

        result = orig_keypress(size, key)
        tree_listbox.update_detail(detail_pane)
        _update_focus_indicator(tree_listbox.body)
        loop.draw_screen()
        return result

    tree_listbox.keypress = wrapped_keypress

    loop = urwid.MainLoop(main_pile, palette, unhandled_input=handle_key)
    tree_listbox.load_archives()
    tree_listbox.update_detail(detail_pane)

    return loop


def run_tui(baseurl=None, username=None, password=None):
    """Launch the TUI application."""
    loop = create_tui(baseurl=baseurl, username=username, password=password)
    try:
        loop.run()
    except KeyboardInterrupt:
        pass
