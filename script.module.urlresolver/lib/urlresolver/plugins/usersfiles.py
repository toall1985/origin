# -*- coding: UTF-8 -*-
"""
    Copyright (C) 2015  tknorris

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


from t0mm0.common.net import Net
from urlresolver.plugnplay.interfaces import UrlResolver
from urlresolver.plugnplay.interfaces import PluginSettings
from urlresolver.plugnplay import Plugin
from urlresolver import common
import re
from lib import jsunpack

class UsersFilesResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver]
    name = "UsersFiles"
    domains = ["usersfiles.com"]

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)
        self.net = Net()
        self.pattern = 'http[s]*://((?:www\.)?usersfiles.com)/(.*)'
        self.net.set_user_agent(common.IE_USER_AGENT)
        self.headers = {'User-Agent': common.IE_USER_AGENT}

    def get_url(self, host, media_id):
        return 'http://usersfiles.com/%s' % media_id

    def get_host_and_id(self, url):
        r = re.search(self.pattern, url)
        if r: return r.groups()
        else: return False

    def valid_url(self, url, host):
        if self.get_setting('enabled') == 'false': return False
        return re.match(self.pattern, url) or host in self.domains

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        html = self.net.http_GET(web_url).content
        match = re.search('<script[^>]*>(eval.*?)</script>', html, re.DOTALL)
        if match:
            js_data = jsunpack.unpack(match.group(1))
            print js_data
            match = re.search('<param\s+name="src"\s*value="([^"]+)', js_data)
            if match:
                return match.group(1)
        
        raise UrlResolver.ResolverError('Unable to find userfiles video')
