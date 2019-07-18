# -*- coding: utf-8 -*-
# Copyright (C) 2019 Petter Reinholdtsen <pere@hungry.com>
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
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

def pickUnlessOne(json, type):
    """
Check the array in the json structure, if there is only one elemet, return it.
If there are more than one elemet, ask the user to pick one.
"""
    #print("Found %d %s entries" % (len(json), type))
    if 'results' in json:
        count = len(json['results'])
    else:
        count = 0
    if 0 == count:
        return None
    if 1 == count:
        if 'tittel' in json['results'][0]:
            print("using %s: %s" % (type, json['results'][0]['tittel']))
        else:
            print("using %s: %s" % (type, json['results'][0]['systemID']))
        return json['results'][0]
    else:
        print("")
        n = -1
        while -1 == n:
            i = 0
            for entry in json['results']:
                if 'tittel' in entry:
                    print(" %d - %s" % (i, entry['tittel']))
                else:
                    print(" %d - %s systemID %s" % (i, type, entry['systemID']))
                i = i + 1
            answer = raw_input("Select which %s you want (or search term): " % type)
            try:
                n = int(answer)
                if n < 0 or n >= count:
                    print("error: Invalid selection %d" % n)
                    n = -1
                else:
                    return json['results'][int(n)]
            except Exception as e:
                # FIXME search instead
                pass

