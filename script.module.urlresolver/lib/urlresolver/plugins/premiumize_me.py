"""
    urlresolver XBMC Addon
    Copyright (C) 2013 Bstrdsmkr

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from urlresolver.plugnplay.interfaces import UrlResolver
from urlresolver.plugnplay.interfaces import SiteAuth
from urlresolver.plugnplay.interfaces import PluginSettings
from urlresolver.plugnplay import Plugin
from urlresolver import common
from t0mm0.common.net import Net

import re
import urllib
try:
    import simplejson as json
except ImportError:
    import json

class PremiumizeMeResolver(Plugin, UrlResolver, SiteAuth, PluginSettings):
    implements = [UrlResolver, PluginSettings]
    name = "Premiumize.me"
    domains = ["*"]
    media_url = None

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.hosts = []
        self.patterns = []
        self.priority = int(p)
        self.net = Net()
        self.scheme = 'https' if self.get_setting('use_https') == 'true' else 'http'

    def get_media_url(self, host, media_id):
        username = self.get_setting('username')
        password = self.get_setting('password')
        url = '%s://api.premiumize.me/pm-api/v1.php?' % (self.scheme)
        query = urllib.urlencode({'method': 'directdownloadlink', 'params[login]': username, 'params[pass]': password, 'params[link]': media_id})
        url = url + query
        response = self.net.http_GET(url).content
        response = json.loads(response)
        if 'status' in response:
            if response['status'] == 200:
                link = response['result']['location']
            else:
                raise UrlResolver.ResolverError('Link Not Found: Error Code: %s' % response['status'])
        else:
            raise UrlResolver.ResolverError('Unexpected Response Received')

        common.addon.log_debug('Premiumize.me: Resolved to %s' % link)
        return link

    def get_url(self, host, media_id):
        return media_id

    def get_host_and_id(self, url):
        return 'premiumize.me', url

    def get_all_hosters(self):
        try:
            if not self.patterns or not self.hosts:
                username = self.get_setting('username')
                password = self.get_setting('password')
                url = '%s://api.premiumize.me/pm-api/v1.php?' % (self.scheme)
                query = urllib.urlencode({'method': 'hosterlist', 'params[login]': username, 'params[pass]': password})
                url = url + query
                response = self.net.http_GET(url).content
                response = json.loads(response)
                result = response['result']
                log_msg = 'Premiumize.me patterns: %s hosts: %s' % (result['regexlist'], result['tldlist'])
                common.addon.log_debug(log_msg)
                self.hosts = result['tldlist']
                self.patterns = [re.compile(regex) for regex in result['regexlist']]
        except Exception as e:
            common.addon.log_error('Error getting Premiumize hosts: %s' % (e))

    def valid_url(self, url, host):
        if self.get_setting('enabled') == 'false': return False
        if self.get_setting('login') == 'false': return False

        self.get_all_hosters()
        if url:
            if not url.endswith('/'): url += '/'
            for pattern in self.patterns:
                if pattern.findall(url):
                    return True
        elif host:
            if host.startswith('www.'): host = host.replace('www.', '')
            if any(host in item for item in self.hosts):
                return True

        return False

    def get_settings_xml(self):
        xml = PluginSettings.get_settings_xml(self)
        xml += '<setting id="%s_use_https" type="bool" label="Use HTTPS" default="false"/>\n' % (self.__class__.__name__)
        xml += '<setting id="%s_login" type="bool" label="login" default="false"/>\n' % (self.__class__.__name__)
        xml += '<setting id="%s_username" enable="eq(-1,true)" type="text" label="Customer ID" default=""/>\n' % (self.__class__.__name__)
        xml += '<setting id="%s_password" enable="eq(-2,true)" type="text" label="PIN" option="hidden" default=""/>\n' % (self.__class__.__name__)
        return xml

    def isUniversal(self):
        return True
