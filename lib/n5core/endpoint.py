# -*- coding: utf-8 -*-
# Copyright (C) 2017,2019 Petter Reinholdtsen <pere@hungry.com>
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
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import base64
import json
import time
import urllib
import urllib.request
from urllib.request import Request, urlopen
from urllib.parse import urlparse, urljoin
from urllib.error import HTTPError
from urllib.error import URLError

class LoginFailure(RuntimeError):
    """Report a login failure"""
    pass

class Endpoint:
    relbaseurl = 'https://rel.arkivverket.no/noark5/v5/api/'
    nikitarelbaseurl = "https://nikita.arkivlab.no/noark5/v5/"
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.verbose = False
        self.get_auth = \
            lambda: (
                'Authorization', self.token
            ) if hasattr(self, 'token') else (
                None, None
            )


    def expandurl(self, path):
#        print(self.baseurl, path)
        if path is None:
            raise ValueError("asked to expand undefined URL path")
        url = urljoin(self.baseurl, path)
        return url
    def login(self, username = None, password = None):
        url7519 = self.findRelation("%slogin/rfc7519/" % self.nikitarelbaseurl)
        url6749 = self.findRelation("%slogin/rfc6749/" % self.nikitarelbaseurl)
        urloidc = self.findRelation("%slogin/oidc/" % self.relbaseurl)
        client_id = 'nikita-client'
        auth_pwd = 'secret'
        if url7519 is not None:
            url = url7519
            try:
                if username is None:
                    username = 'admin@example.com'
                if password is None:
                    password = 'password'
                data = {
                    'username': username,
                    'password': password,
                }
                (j,r) = self.json_post(url, jsondata,
                                       contenttype='application/json')
            except HTTPError as e:
                raise LoginFailure("Posting to login relation %s failed: %s" % (url, e))
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
                datastr = urllib.parse.urlencode(data)
                a = '%s:%s' % (client_id, auth_pwd)
                self.token = 'Basic %s' % base64.encodebytes(a).strip()
                (c,r) = self.post(url, datastr, 'application/x-www-form-urlencoded',
                                  accept='application/json')
            except HTTPError as e:
                raise LoginFailure("Posting to login relation %s failed: %s (%s)" % (url, str(e), e.read()))
            j = json.loads(c.decode('UTF-8'))
            self.token = "%s %s" % (j['token_type'], j['access_token'])
        elif urloidc is not None:
            (content, res) = self.json_get(urloidc)
            j = json.loads(content)
            url = j['token_endpoint']
            try:
                if username is None:
                    username = 'admin@example.com'
                if password is None:
                    password = 'password'
                data = {
                    'grant_type': 'password',
                    'client_id': client_id,
                    'username': username,
                    'password': password,
                }
                datastr = urllib.parse.urlencode(data)
                a = '%s:%s' % (client_id, auth_pwd)
                key_bytes = base64.b64encode(str.encode(a))
                key_str = key_bytes.decode('ascii')
                self.token = 'Basic {}'.format(key_str)
                # Manually encode query parameters in the URL:
                (c,r) = self.post(url, datastr.encode("utf-8"), 'application/x-www-form-urlencoded',
                                  accept='application/json')
            except HTTPError as e:
                raise LoginFailure("Posting to login relation %s failed: %s (%s)" % (url, str(e), e.read()))
            te = json.loads(c.decode('UTF-8'))
            self.oidcmeta = j
            self.oidcinfo = te
            now = time.time()
            self.oidcinfo['epoc_expires_in'] = now + self.oidcinfo['expires_in']
            self.oidcinfo['epoc_refresh_expires_in'] = now + self.oidcinfo['refresh_expires_in']
            def oidc_get_auth():
                if hasattr(self, 'oidcinfo'):
                    now = time.time()
                    # Expires in 10 seconds or less and the refresh
                    # token is still valid, renew
                    if self.oidcinfo['epoc_expires_in'] - 10 < now and \
                       now < self.oidcinfo['epoc_refresh_expires_in'] - 1:
                        url = self.oidcmeta['token_endpoint']
                        data = {
                            'grant_type': 'refresh_token',
                            'refresh_token':self.oidcinfo['refresh_token'],
                            'client_id': client_id,
                        }
                        datastr = urllib.parse.urlencode(data)
                        (c,r) = self._post(url, datastr.encode("utf-8"),
                                          'application/x-www-form-urlencoded',
                                           length=0,
                                           accept='application/json',
                                           headers={},
                                          )
                        te = json.loads(c.decode('UTF-8'))
                        self.oidcinfo = te
                        self.oidcinfo['epoc_expires_in'] = \
                            now + self.oidcinfo['expires_in']
                        self.oidcinfo['epoc_refresh_expires_in'] = \
                            now + self.oidcinfo['refresh_expires_in']
                    token = "%s %s" % (self.oidcinfo['token_type'],
                                       self.oidcinfo['access_token'])
                    return ('Authorization', token)
                else:
                    return (None, None)

            self.get_auth = oidc_get_auth
        else:
            raise LoginFailure("Unable to find login relation")

    def findRelation(self, relation, templated=False):
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
                ctype = res.getheader('Content-Type')
                if 0 == ctype.find('application/vnd.noark5+json'):
                    if self.verbose:
                        print(content)
                    baseref = json.loads(content)
                    #print "J:", baseref
                    if type(baseref) is list:
                        pass # Ignore lists
                    elif '_links' in baseref:
                        for rel in baseref['_links'].keys():
                            if 'href' in baseref['_links'][rel]:
                                href = baseref['_links'][rel]['href']
                                if not templated:
                                    if 'templated' in baseref['_links'][rel] \
                                       and baseref['_links'][rel]['templated']:
                                        href = href.split('{')[0]
                                if href not in urlseen:
                                    urlsleft.append(href)
                                if rel != 'self' and \
                                   rel == relation:
                                   return href
                    else:
                        pass # ignore URLs without _links
            except HTTPError as e:
                # Ignore errors from GET, we only try to locate links, not detect problems.
                pass

    def post(self, path, data, mimetype, length=0, accept='application/vnd.noark5+json'):
        headers = {}
        h, t = self.get_auth()
        if h:
            headers[h] = t
        return self._post(path, data, mimetype, length, accept, headers);

    def _post(self, path, data, mimetype, length, accept, headers):
        url = self.expandurl(path)
        headers['Accept'] = accept
        headers['Content-Type'] = mimetype

        if data is not None and length == 0:
            length = len(data)
        headers['Content-Length'] = length
        if self.verbose:
            print("POST %s: %s" % (url, headers))
        if data is not None:
            request = Request(url, headers=headers, data=data)
            # Not printing data as it contain passwords when logging in
            #if self.verbose: print("DATA: %s" % (data))
        else:
            request = Request(url, headers=headers)
            request.get_method = lambda: 'POST'
        response = urlopen(request)
        content = response.read()
        if self.verbose:
            print(content)
        return (content, response)

    def json_post(self, path, data, contenttype='application/vnd.noark5+json'):
        jsondata = json.dumps(data).encode('UTF-8')
        content, response = self.post(path, jsondata, contenttype)
        content = content.decode("UTF-8")
        return (content, response)

    def put(self, path, data, mimetype, length=None, etag=None):
        url = self.expandurl(path)
        if length is None:
            length = len(data)
        headers = {
            'Accept' : 'application/vnd.noark5+json',
            'Content-Type': mimetype,
            'Content-Length' : length,
        }
        h, t = self.get_auth()
        if h:
            headers[h] = t
        if etag is not None:
            headers['ETag'] = etag
        if self.verbose:
            print("PUT %s: %s" % (url, headers))
        if self.verbose:
            print(headers)
        request = Request(url, str(data).encode(), headers=headers)
        request.get_method = lambda: 'PUT'
        response = urlopen(request)
        content = response.read().decode("UTF-8")
        if self.verbose:
            print(content)
        return (content, response)

    def _get(self, path, headers = None):
        url = self.expandurl(path)
        purl = urlparse(url)
        url = purl._replace(query=urllib
                            .parse.quote_plus(purl.query)).geturl()
        if self.verbose:
            print("GET %s" % url)
        if headers is None:
            headers = {}
        h, t = self.get_auth()
        if h:
            headers[h] = t
        request = Request(url, None, headers=headers)
        response = urlopen(request)
        content = response.read()
        if self.verbose:
            print(content)
        return (content, response)

    def json_get(self, path):
        headers = {
            'X_REQUESTED_WITH' :'XMLHttpRequest',
            'Accept' : 'application/json, application/vnd.noark5+json, text/javascript, */*; q=0.01',
            }
        content, response = self._get(path, headers)
        ctype = response.getheader('Content-Type')
        # Avoid trying to interpret non-json as UTF-8
        if ctype in ('application/json', 'application/vnd.noark5+json'):
            content = content.decode("UTF-8")
        return (content, response)

    def cors_options(self, path, headers=None, method=None):
        if headers is None:
            headers = {}
        if method is None:
            method = 'POST'

        headers['Access-Control-Request-Method'] = method
        headers['Origin'] = 'Origin: http://localhost:3000'
        return self.options(path, headers, method)

    def options(self, path, headers, method):
        url = self.expandurl(path)
        purl = urlparse(url)
        url = purl._replace(query=urllib
                            .parse.quote_plus(purl.query)).geturl()
        opener = urllib.request.build_opener(urllib.request.HTTPHandler)
        request = urllib.request.Request(url, None, headers)
        request.get_method = lambda: 'OPTIONS'
        response = opener.open(request)
        content = response.read()
        return (content, response)

    def delete(self, path, headers = None, etag = None):
        url = self.expandurl(path)
        purl = urlparse(url)
        url = purl._replace(query=urllib
                            .parse.quote_plus(purl.query)).geturl()
        opener = urllib.request.build_opener(urllib.request.HTTPHandler)
        if headers is None:
            headers = {}
        h, t = self.get_auth()
        if h:
            headers[h] = t
        if etag is not None:
            headers['ETag'] = etag
        request = urllib.request.Request(url, None, headers)
        request.get_method = lambda: 'DELETE'
        response = opener.open(request)
        content = response.read()
        return (content, response)


    def entity_rel(self, content):
        """Return the relation key representing the entity in question, by
looking for self, and then finding the non-self relation with the same
href.
"""
        href = content['_links']['self']['href']
        for rel, v in content['_links'].items():
            if 'self' != rel and v['href'] == href:
                return rel
        return None
