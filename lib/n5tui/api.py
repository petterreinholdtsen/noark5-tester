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
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from n5core.endpoint import Endpoint, HTTPError

relbaseurl = Endpoint.relbaseurl


class N5API(Endpoint):
    """Convenience wrapper around the base Endpoint class."""

    def __init__(self, baseurl=None, username=None, password=None):
        if baseurl is None:
            baseurl = "http://arkiv.local:8092/noark5v5/"
        Endpoint.__init__(self, baseurl)
        self.username = username or "pereadm"
        self.password = password or "secret"
        self.logged_in = False

    def ensure_login(self):
        """Login if not already logged in. Must be called before any API use."""
        if not self.logged_in:
            self.login(username=self.username, password=self.password)
            self.logged_in = True

    # ---- helpers ----

    @staticmethod
    def parselinks(links):
        rels = {}
        for rel in links.keys():
            if "href" in links[rel]:
                rels[rel] = links[rel]["href"]
        return rels

    @staticmethod
    def clean_url(url):
        """Strip OData template parameters from URL (e.g., {?$filter...})."""
        idx = url.find("{")
        if idx >= 0:
            return url[:idx]
        return url

    def get_children(self, entity_dict, child_relations, limit=None):
        """Discover and fetch child entities for the given parent.

        Returns list of (type_label, base_url) tuples — one per child relation type found.
        The caller is responsible for fetching actual child items from each URL.

        Args:
            entity_dict: Parent entity dict with _links
            child_relations: List of (display_label, rel_suffix) like CHILD_RELATIONS
            limit: Optional max children to fetch per type (None = all via pagination)
        """
        try:
            links = self.parselinks(entity_dict.get("_links", {}))
            parent_path = entity_dict.get("_links", {}).get("self", {}).get("href", "")

            # Determine current entity type from parent_path to only include CHILD relations
            current_type_idx = -1
            for i, (_, rel_suffix) in enumerate(child_relations):
                type_name = rel_suffix.rstrip("/").rsplit("/", 1)[-1]
                if "/" + type_name + "/" in parent_path or parent_path.endswith(
                    "/" + type_name
                ):
                    current_type_idx = i

            relations_found = []
            for i, (child_type, rel_suffix) in enumerate(child_relations):
                # Skip ancestor types — only show relations that are children of current entity
                if current_type_idx >= 0 and i <= current_type_idx:
                    continue
                if rel_suffix not in links:
                    continue
                child_url = self.clean_url(links[rel_suffix])
                if not child_url or child_url.rstrip("/") == parent_path.rstrip("/"):
                    continue
                relations_found.append((child_type, child_url))

            return relations_found
        except Exception:
            return []

    def get_entity(self, path):
        """GET a JSON entity at the given path and return parsed dict."""
        self.ensure_login()
        content, _res = self.json_get(path)
        return json.loads(content)

    def get_entity_with_etag(self, path):
        """GET a JSON entity and return (dict, etag_string).

        The ETag is read from the response's ETag header for optimistic locking.
        Returns None as etag if not present.
        """
        self.ensure_login()
        content, res = self.json_get(path)
        etag = res.getheader("ETag")
        return json.loads(content), etag

    # ---- list operations ----

    def list_archives(self):
        url = self.findRelation("%sarkivstruktur/arkiv/" % relbaseurl)
        if not url:
            return []
        info = self.get_entity(url)
        return info.get("results", [])

    def list_arkivskapere(self):
        url = self.findRelation("%sarkivstruktur/arkivskaper/" % relbaseurl)
        if not url:
            return []
        info = self.get_entity(url)
        return info.get("results", [])

    def _list_children(self, parent_path, rel_suffix):
        """Generic helper to list children of a given relation type."""
        links = self.parselinks(self.get_entity(parent_path).get("_links", {}))
        rel = "%s%s" % (relbaseurl, rel_suffix)
        if rel not in links:
            return []
        url = self.clean_url(links[rel])
        info = self.get_entity(url)
        return info.get("results", [])

    def list_arkivdeler(self, arkiv_path):
        return self._list_children(arkiv_path, "arkivstruktur/arkivdel/")

    def list_klassifikasjonssystemer(self, arkivdel_path):
        return self._list_children(
            arkivdel_path, "arkivstruktur/klassifikasjonssystem/"
        )

    def list_klasser(self, klass_sys_path):
        return self._list_children(klass_sys_path, "arkivstruktur/klasse/")

    def list_mapper(self, parent_path):
        """List mapper under a klasse, mappe, or arkivdel."""
        return self._list_children(parent_path, "arkivstruktur/mappe/")

    def list_saksmapper(self, parent_path):
        """List saksmapper under an arkivdel."""
        return self._list_children(parent_path, "sakarkiv/saksmappe/")

    def list_registreringer(self, mappe_path):
        """List registrerings under a mappe/saksmappe."""
        return self._list_children(mappe_path, "arkivstruktur/registrering/")

    def list_journalposter(self, saksmappe_path):
        """List journalposter under a saksmappe."""
        return self._list_children(saksmappe_path, "sakarkiv/journalpost/")

    def list_dokumentbeskrivelser(self, registrering_path):
        """List dokumentbeskrivelser under a registrering."""
        return self._list_children(
            registrering_path, "arkivstruktur/dokumentbeskrivelse/"
        )

    def list_dokumentobjekter(self, dokbeskr_path):
        """List dokumentobjekter under a dokumentbeskrivelse."""
        return self._list_children(dokbeskr_path, "arkivstruktur/dokumentobjekt/")

    # ---- search operations ----

    def search_entities(self, query):
        """Search all entity collections by title using OData $filter.

        Returns list of (path, label) tuples for matching entities."""
        from urllib.parse import quote_plus as _qp

        self.ensure_login()

        collection_rels = [
            "%sarkivstruktur/arkiv/" % relbaseurl,
            "%sarkivstruktur/arkivdel/" % relbaseurl,
            "%sarkivstruktur/klassifikasjonssystem/" % relbaseurl,
            "%sarkivstruktur/mappe/" % relbaseurl,
            "%sarkivstruktur/registrering/" % relbaseurl,
            "%sarkivstruktur/dokumentbeskrivelse/" % relbaseurl,
            "%sarkivstruktur/dokumentobjekt/" % relbaseurl,
            "%sakarkiv/saksmappe/" % relbaseurl,
            "%sakarkiv/journalpost/" % relbaseurl,
        ]

        # Nikita möter collections (separate namespace)
        nikita_moter_base = "https://nikita.arkivlab.no/noark5/v5/moeter/"
        for mt in ["moetemappe", "moeteregistrering"]:
            collection_rels.append(nikita_moter_base + mt + "/")

        filter_str = "tittel eq " + _qp(query)
        results = []

        for rel in collection_rels:
            try:
                url = self.findRelation(rel)
                if not url:
                    continue
                url = self.clean_url(url) + "?" + "$filter=" + filter_str
                content, _res = self.json_get(url)
                info = json.loads(content)
                for item in info.get("results", []):
                    href = item.get("_links", {}).get("self", {}).get("href")
                    tittel = item.get("tittel", "?")
                    if href:
                        results.append((href, tittel))
            except Exception:
                pass

        return results

    # ---- create operations ----

    def _create_entity(self, parent_path, ny_rel, data):
        """Create an entity under the given parent.

        GETs the creation URL for defaults, merges with data, POSTs back.
        Returns the created entity JSON dict.
        """
        self.ensure_login()
        parent_links = self.parselinks(self.get_entity(parent_path).get("_links", {}))
        if ny_rel not in parent_links:
            raise HTTPError(parent_path, 404, "No %s relation found" % ny_rel, {}, None)
        url = parent_links[ny_rel]
        # Try fetching template; some nikita endpoints return 404 on GET
        try:
            gc, gres = self.json_get(url)
            default = json.loads(gc)
            for k in default:
                if k != "_links" and k not in data:
                    data[k] = default[k]
        except Exception:
            pass  # Template unavailable — post with minimal data
        content, res = self.json_post(url, data)
        return json.loads(content)

    # ---- top-level creation (no parent needed) ----

    def _create_at_root(self, ny_rel_suffix, data):
        """Create an entity at the root level (arkivskaper, arkiv)."""
        self.ensure_login()
        url = self.findRelation("%s%s" % (relbaseurl, ny_rel_suffix))
        if not url:
            raise HTTPError(
                relbaseurl,
                404,
                "No %s relation found at root" % ny_rel_suffix,
                {},
                None,
            )
        # Try fetching template; some nikita endpoints return 404 on GET
        try:
            gc, _gres = self.json_get(url)
            default = json.loads(gc)
            for k in default:
                if k != "_links" and k not in data:
                    data[k] = default[k]
        except Exception:
            pass  # Template unavailable — post with minimal data
        content, res = self.json_post(url, data)
        return json.loads(content)

    def create_arkivskaper(self, arkivskaper_id, navn):
        """Create an arkivskaper at the root level."""
        return self._create_at_root(
            "arkivstruktur/ny-arkivskaper/",
            {
                "arkivskaperID": arkivskaper_id,
                "arkivskaperNavn": navn,
            },
        )

    def create_arkiv(self, tittel):
        """Create an archive at the root level."""
        return self._create_at_root("arkivstruktur/ny-arkiv/", {"tittel": tittel})

    # ---- hierarchical creation (under a parent) ----

    def create_mappe(self, parent_path, tittel, beskrivelse=None):
        """Create a mappe under the given parent (klasse or mappe)."""
        data = {"tittel": tittel}
        if beskrivelse:
            data["beskrivelse"] = beskrivelse
        return self._create_entity(
            parent_path, "%sarkivstruktur/ny-mappe/" % relbaseurl, data
        )

    def create_arkivdel(self, arkiv_path, tittel):
        """Create an arkivdel under an archive."""
        return self._create_entity(
            arkiv_path, "%sarkivstruktur/ny-arkivdel/" % relbaseurl, {"tittel": tittel}
        )

    def create_saksmappe(
        self, parent_path, tittel, saksaar=None, sakssekvensnummer=None
    ):
        """Create a saksmappe under the given parent."""
        self.ensure_login()
        parent_links = self.parselinks(self.get_entity(parent_path).get("_links", {}))
        ny_rel_sak = "%ssakarkiv/ny-saksmappe/" % relbaseurl
        if ny_rel_sak not in parent_links:
            raise HTTPError(
                parent_path, 404, "No ny-saksmappe relation found", {}, None
            )
        url = parent_links[ny_rel_sak]
        data = {"tittel": tittel}
        if saksaar:
            data["saksaar"] = saksaar
        if sakssekvensnummer:
            data["sakssekvensnummer"] = sakssekvensnummer
        gc, _gres = self.json_get(url)
        default = json.loads(gc)
        for k in default:
            if k != "_links" and k not in data:
                data[k] = default[k]
        content, res = self.json_post(url, data)
        return json.loads(content)

    def create_registrering(self, mappe_path, tittel):
        """Create a registrering under a mappe."""
        return self._create_entity(
            mappe_path,
            "%sarkivstruktur/ny-registrering/" % relbaseurl,
            {"tittel": tittel},
        )

    def create_journalpost(self, saksmappe_path, tittel):
        """Create a journalpost under a saksmappe."""
        self.ensure_login()
        parent_links = self.parselinks(
            self.get_entity(saksmappe_path).get("_links", {})
        )
        ny_rel = "%ssakarkiv/ny-journalpost/" % relbaseurl
        if ny_rel not in parent_links:
            raise HTTPError(
                saksmappe_path, 404, "No ny-journalpost relation found", {}, None
            )
        url = parent_links[ny_rel]
        data = {"tittel": tittel}
        gc, _gres = self.json_get(url)
        default = json.loads(gc)
        for k in default:
            if k != "_links" and k not in data:
                data[k] = default[k]
        content, res = self.json_post(url, data)
        return json.loads(content)

    def create_dokumentbeskrivelse(self, registrering_path, tittel):
        """Create a dokumentbeskrivelse under a registrering."""
        return self._create_entity(
            registrering_path,
            "%sarkivstruktur/ny-dokumentbeskrivelse/" % relbaseurl,
            {"tittel": tittel},
        )

    def create_dokumentobjekt(self, dokbeskr_path):
        """Create a dokumentobjekt under a dokumentbeskrivelse."""
        return self._create_entity(
            dokbeskr_path, "%sarkivstruktur/ny-dokumentobjekt/" % relbaseurl, {}
        )

    # ---- file upload ----

    def upload_file(self, fil_url, filepath):
        """Upload a file to the dokumentfil relation URL.

        Returns (content, response) from POST.
        """
        self.ensure_login()
        mime = "application/octet-stream"
        try:
            import magic as python_magic

            # Use mime=True to get standard MIME type (e.g., text/plain), not description
            mg = python_magic.Magic(mime=True)
            mime = mg.from_file(filepath) or mime
        except Exception:
            pass
        with open(filepath, "rb") as fh:
            data = fh.read()
        content, res = self.post(fil_url, data, mime)
        return content, res

    def upload_to_parent(self, parent_path, filepath):
        """Upload a file to an entity, creating dokumentobjekt if needed.

        If the entity already has arkivstruktur/fil/ relation (dokumentobjekt),
        uploads directly there. Otherwise creates a new dokumentobjekt via
        ny-dokumentobjekt/ first, then uploads to it.

        Returns the created/updated dokumentobjekt entity dict.
        """
        self.ensure_login()
        parent_data = self.get_entity(parent_path)
        parent_links = self.parselinks(parent_data.get("_links", {}))

        fil_rel = "%sarkivstruktur/fil/" % relbaseurl
        ny_docobj_rel = "%sarkivstruktur/ny-dokumentobjekt/" % relbaseurl
        dokobj_rel = "%sarkivstruktur/dokumentobjekt/" % relbaseurl

        # If entity already has fil/ relation (dokumentobjekt), upload directly
        if fil_rel in parent_links:
            fil_url = self.clean_url(parent_links[fil_rel])
            content, res = self.upload_file(fil_url, filepath)
        else:
            # Otherwise create dokumentobjekt first via ny-dokumentobjekt/
            if ny_docobj_rel not in parent_links:
                raise RuntimeError(
                    "Parent entity has no fil/ or ny-dokumentobjekt/ relation"
                )

            docobj_result = self.create_dokumentobjekt(parent_path)

            # Re-fetch parent to get the new fil/ relation
            parent_data = self.get_entity(parent_path)
            parent_links = self.parselinks(parent_data.get("_links", {}))

            if fil_rel not in parent_links:
                raise RuntimeError("Created dokumentobjekt but no fil/ relation found")

            fil_url = self.clean_url(parent_links[fil_rel])
            content, res = self.upload_file(fil_url, filepath)

        # Re-fetch parent to get the updated dokumentobjekt collection
        parent_data = self.get_entity(parent_path)
        parent_links = self.parselinks(parent_data.get("_links", {}))

        if dokobj_rel in parent_links:
            dokobjs_url = self.clean_url(parent_links[dokobj_rel])
            dokobjs = self.get_entity(dokobjs_url).get("results", [])
            if dokobjs:
                return self.get_entity(dokobjs[0]["_links"]["self"]["href"])

        return self.get_entity(parent_path)

    # ---- update / move operations ----

    def update_entity(self, entity_path, changes):
        """PUT an entity with the given field changes.

        GETs current entity, merges in changes, PUTs back.
        Returns updated entity dict.
        """
        self.ensure_login()
        raw, res = self.json_get(entity_path)
        etag = res.getheader("ETag")
        current = json.loads(raw)
        for k, v in changes.items():
            current[k] = v
        data_str = json.dumps(current)
        content, res = self.put(
            entity_path, data_str, "application/vnd.noark5+json", etag=etag
        )
        return json.loads(content)

    def close_mappe(self, mappe_path):
        """Close (avslutt) a mappe via the avslutt-mappe endpoint."""
        self.ensure_login()
        entity = self.get_entity(mappe_path)
        links = self.parselinks(entity.get("_links", {}))
        # Nikita uses its own namespace for avslutt-mappe relation
        nikita_relbase = "https://nikita.arkivlab.no/noark5/v5/"
        avslutt_rel = "%savslutt-mappe/" % nikita_relbase
        if avslutt_rel not in links:
            raise HTTPError(
                mappe_path, 404, "No avslutt-mappe relation found", {}, None
            )
        # The endpoint accepts PUT (verified via OPTIONS)
        self.put(links[avslutt_rel], "", "application/vnd.noark5+json")
        return self.get_entity(mappe_path)

    def move_entity(
        self, entity_path: str, parent_rel_key: str, new_parent_self_href: str
    ):
        """Move an entity to a new parent via RFC 7396 merge-PATCH with _links.

        Uses PATCH on entity self-href with 'application/merge-patch+json' content type
        and If-Match ETag header — matches Nikita PatchTest.java move implementations.

        Args:
            entity_path: API path of the entity to move (e.g., api/arkivstruktur/mappe/{id})
            parent_rel_key: The _links key for the parent relation. Per N5TG, this is a full
                IANA relation URI like REL_FONDS_STRUCTURE_SERIES or REL_FONDS_STRUCTURE_FILE.
            new_parent_self_href: self-href URL of the new parent container

        Returns:
            Full entity dict returned by server after successful move.

        Raises:
            HTTPError: 400 if Nikita version doesn't support _links merge-patch moves yet,
                412 if ETag conflict (entity modified since fetch).
        """
        self.ensure_login()

        # Fetch current entity to get ETag for optimistic locking
        _, resp = self.json_get(entity_path)
        etag = resp.getheader("ETag") or ""

        # RFC 7396 merge-patch: set href to new parent, or null to remove link (top-level move)
        if new_parent_self_href is None:
            payload = {"_links": {parent_rel_key: None}}
        else:
            payload = {"_links": {parent_rel_key: {"href": new_parent_self_href}}}

        content, resp = self.patch(
            entity_path,
            payload,
            mimetype="application/merge-patch+json",
            etag=etag if etag else "*",
        )
        return json.loads(content.decode("utf-8"))

    # IANA relation keys from N5TG / Nikita constants (PatchTest.java)
    REL_FONDS_STRUCTURE_SERIES = "%sarkivstruktur/arkivdel/" % relbaseurl
    REL_FONDS_STRUCTURE_FILE = "%sarkivstruktur/mappe/" % relbaseurl

    def move_mappe(self, mappe_path: str, new_parent_self_href: str):
        """Move a mappe to a new parent (arkivdel or another mappe)."""
        if "/arkivdel/" in new_parent_self_href:
            return self.move_entity(
                mappe_path, self.REL_FONDS_STRUCTURE_SERIES, new_parent_self_href
            )
        # Default: move under another mappe (undermappe)
        return self.move_entity(
            mappe_path, self.REL_FONDS_STRUCTURE_FILE, new_parent_self_href
        )

    def move_saksmappe(self, saksmappe_path: str, new_parent_self_href: str):
        """Move a saksmappe to a new parent (arkivdel or another saksmappe)."""
        if "/arkivdel/" in new_parent_self_href:
            return self.move_entity(
                saksmappe_path, self.REL_FONDS_STRUCTURE_SERIES, new_parent_self_href
            )
        # Default: move under another saksmappe
        return self.move_entity(
            saksmappe_path, "%ssakarkiv/saksmappe/" % relbaseurl, new_parent_self_href
        )

    def move_registrering(self, registrering_path: str, new_parent_self_href: str):
        """Move a registrering to a new mappe or saksmappe parent."""
        if "/saksmappe/" in new_parent_self_href:
            return self.move_entity(
                registrering_path,
                "%ssakarkiv/saksmappe/" % relbaseurl,
                new_parent_self_href,
            )
        return self.move_entity(
            registrering_path, self.REL_FONDS_STRUCTURE_FILE, new_parent_self_href
        )

    def move_journalpost(self, journalpost_path: str, new_parent_self_href: str):
        """Move a journalpost to a new saksmappe parent."""
        if "/saksmappe/" in new_parent_self_href:
            return self.move_entity(
                journalpost_path,
                "%ssakarkiv/saksmappe/" % relbaseurl,
                new_parent_self_href,
            )
        # Fallback: treat as regular mappe parent
        return self.move_entity(
            journalpost_path, self.REL_FONDS_STRUCTURE_FILE, new_parent_self_href
        )

    # ---- delete ----

    def delete_entity(self, entity_path):
        """Delete an entity."""
        self.ensure_login()
        content, res = self.delete(entity_path)
        return content, res
