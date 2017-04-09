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
        if path is None:
            raise ValueError("asked to expand undefined URL path")
        url = urlparse.urljoin(self.baseurl, path)
        if self.verbose:
            print(url)
        return url

    def login(self, username = 'admin', password = 'password'):
        data = {
            'username': username,
            'password': password,
        }
        jsondata = json.dumps(data)
        url = self.findRelation("http://nikita.arkivlab.no/noark5/v4/login/rfc7519/")
        (c,r) = self.post(url, jsondata, 'application/json', length=None)
        j = json.loads(c)
        self.token = j['token']

    def findRelation(self, relation):
        """
Recursively look for relation in API.
"""
        if 'self' == relation: # Do not make sense to look for self relations
            return None
        urlsleft = ['.']
        urlseen = {}
        while 0 < len(urlsleft):
            url = urlsleft.pop(0)
            if url in urlseen:
                continue
            urlseen[url] = 1
            try:
                (content, res) = self.json_get(url)
                ctype = res.info().getheader('Content-Type')
                if 0 == ctype.find('application/vnd.noark5-v4+json'):
                    baseref = json.loads(content)
                    #print "J:", baseref
                    if type(baseref) is list:
                        pass # Ignore lists
                    elif '_links' in baseref:
                        for l in baseref['_links']:
                            if 'href' in l:
                                href = l['href']
                                if href not in urlseen:
                                    urlsleft.append(href)
                                if 'rel' in l and l['rel'] != 'self' and \
                                   l['rel'] == relation:
                                   return href
                    else:
                        pass # ignore URLs without _links
            except urllib2.HTTPError, e:
                pass
                self.failure("unable to GET %s" % url)

    def post(self, path, data, mimetype, length=None):
        url = self.expandurl(path)
        if length is None:
            length = len(data)
        headers = {
            'Accept' : 'application/vnd.noark5-v4+json',
            'Content-Type': mimetype,
            'Content-Length' : length,
        }
        if hasattr(self, 'token'):
            headers['Authorization'] = self.token
        if self.verbose:
            print("POST %s: %s" % (url, headers))
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
        if self.verbose:
            print("GET %s" % url)
        if headers is None:
            headers = {}
        if hasattr(self, 'token'):
            headers['Authorization'] = self.token
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
