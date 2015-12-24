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
import xml.etree.ElementTree as ET
import re

class MediaPlayBoxResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver]
    name = "MediaPlayBox"
    domains = ["mediaplaybox.com"]

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)
        self.net = Net()
        self.pattern = 'http[s]*://((?:www\.)?mediaplaybox.com)/video/(.*)'
        self.net.set_user_agent(common.IE_USER_AGENT)
        self.headers = {'User-Agent': common.IE_USER_AGENT}

    def get_url(self, host, media_id):
        return 'http://mediaplaybox.com/video/%s' % media_id

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
        patterns = [
            'property="og:video"\s+content="[^"]+\?f=([^"]+)',
            'itemprop="embedURL"\s+content="[^"]+\?f=([^"]+)',
            '<embed[^>]+src="[^"]+\?f=([^"]+)'
        ]
        for pattern in patterns:
            match = re.search(pattern, html)
            if match:
                xml = self.net.http_GET(match.group(1)).content
                root = ET.fromstring(xml)
                result = root.find('./video/src')
                if result is not None:
                    return result.text
        
        raise UrlResolver.ResolverError('Unable to find mediaplaybox video')
