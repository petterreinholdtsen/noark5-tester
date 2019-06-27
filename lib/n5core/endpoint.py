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

import base64
import json
import mechanize
import urllib
import urllib2
import urlparse

class LoginFailure(RuntimeError):
    """Report a login failure"""
    pass

class Endpoint:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self._browser = mechanize.Browser()
        self.verbose = False
        self.relbaseurl = 'https://rel.arkivverket.no/noark5/v4/api/'
        self.nikitarelbaseurl = "https://nikita.arkivlab.no/noark5/v4/"

    def expandurl(self, path):
#        print(self.baseurl, path)
        if path is None:
            raise ValueError("asked to expand undefined URL path")
        url = urlparse.urljoin(self.baseurl, path)
        return url
    def login(self, username = None, password = None):
        url7519 = self.findRelation("%slogin/rfc7519/" % self.nikitarelbaseurl)
        url6749 = self.findRelation("%slogin/rfc6749/" % self.nikitarelbaseurl)
        if url7519 is not None:
            url = url7519
            try:
                if username is None:
                    username = 'admin'
                if password is None:
                    password = 'password'
                data = {
                    'username': username,
                    'password': password,
                }
                jsondata = json.dumps(data)
                (c,r) = self.post(url, jsondata, 'application/json')
            except urllib2.HTTPError as e:
                raise LoginFailure("Posting to login relation %s failed: %s" % (url, e))
            j = json.loads(c)
            self.token = j['token']
        elif url6749 is not None:
            url = url6749
            try:
                if username is None:
                    username = 'admin@example.com'
                if password is None:
                    password = 'password'
                data = {
                    'grant_type': 'password',
                    'username': username,
                    'password': password,
                }
                datastr = urllib.urlencode(data)
                a = '%s:%s' % ('nikita-client', 'secret')
                self.token = 'Basic %s' % base64.encodestring(a).strip()
                (c,r) = self.post(url, datastr, 'application/x-www-form-urlencoded')
            except urllib2.HTTPError as e:
                raise LoginFailure("Posting to login relation %s failed: %s (%s)" % (url, str(e), e.read()))
            j = json.loads(c)
            self.token = "%s %s" % (j['token_type'], j['access_token'])
        else:
            raise LoginFailure("Unable to find login relation")

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
                        for rel in baseref['_links'].keys():
                            if 'href' in baseref['_links'][ref]:
                                href = baseref['_links']['href']
                                if href not in urlseen:
                                    urlsleft.append(href)
                                if rel != 'self' and \
                                   rel == relation:
                                   return href
                    else:
                        pass # ignore URLs without _links
            except urllib2.HTTPError as e:
                # Ignore errors from GET, we only try to locate links, not detect problems.
                pass

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

    def put(self, path, data, mimetype, length=None, etag=None):
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
        if etag is not None:
            headers['ETag'] = etag
        if self.verbose:
            print("PUT %s: %s" % (url, headers))
        if self.verbose:
            print(headers)
        request = urllib2.Request(url, data, headers)
        request.get_method = lambda: 'PUT'
        response = self._browser.open(request)
        content = response.read()
        if self.verbose:
            print(content)
        return (content, response)

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

    def delete(self, path, headers = None):
        url = self.expandurl(path)
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        if headers is None:
            headers = {}
        if hasattr(self, 'token'):
            headers['Authorization'] = self.token
        request = urllib2.Request(url, None, headers)
        request.get_method = lambda: 'DELETE'
        response = opener.open(request)
        content = response.read()
        return (content, response)
