# Copyright (C) 2017 Petter Reinholdtsen <pere@hungry.com>
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

import json
import mechanize
import urllib2
import urlparse

class Endpoint:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self._browser = mechanize.Browser()
        self.verbose = False

    def expandurl(self, path):
#        print(self.baseurl, path)
        url = urlparse.urljoin(self.baseurl, path)
        if self.verbose:
            print(url)
        return url

    def login(self, username = 'admin', password = 'password'):
        url = self.expandurl('login')
#        print(url)
        self._browser.open(url)
        self._browser.select_form(nr=0)
#        self._browser.form.set_all_readonly(False)
        self._browser['username'] = username
        self._browser['password'] = password
        self._browser.submit()
        html = self._browser.response().read()

    def post(self, path, data, mimetype):
        url = self.expandurl(path)
        print("POST %s to %s" % (mimetype, url))
        headers = {
            'Accept' : mimetype,
            'Content-Type': mimetype,
            'Content-Length' : len(data),
        }
        request = urllib2.Request(url, data, headers)
        response = self._browser.open(request)
        content = response.read()
        if self.verbose:
            print(content)
        return (content, response)

    def json_post(self, path, data):
        jsondata = json.dumps(data)
        return self.post(path, jsondata, 'application/vnd.noark5-v4+json')

    def _get(self, path, headers = None):
        url = self.expandurl(path)
#        print(url)
        request = urllib2.Request(url, None, headers)
        response = self._browser.open(request)
        content = response.read()
        if self.verbose:
            print(content)
        return (content, response)

    def json_get(self, path):
        headers = {
            'X_REQUESTED_WITH' :'XMLHttpRequest',
            'Accept' : 'application/json, application/vnd.noark5-v4+json, text/javascript, */*; q=0.01',
            }
        return self._get(path, headers)

    def xml_get(self, path):
        headers = {
            'Accept' : 'application/vnd.noark5-v4+xml',
        }
        return self._get(path, headers)

    def options(self, path):
        url = self.expandurl(path)
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url)
        request.get_method = lambda: 'OPTIONS'
        response = opener.open(request)
        content = response.read()
        return (content, response)
