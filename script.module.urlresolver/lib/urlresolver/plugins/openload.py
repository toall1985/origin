"""
openload.io urlresolver plugin
Copyright (C) 2015 tknorris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from t0mm0.common.net import Net
from urlresolver.plugnplay.interfaces import UrlResolver
from urlresolver.plugnplay.interfaces import PluginSettings
from urlresolver.plugnplay import Plugin
from urlresolver import common
import json
import re
import xbmc
import urllib
from lib import captcha_lib

class OpenLoadResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver, PluginSettings]
    name = "openload"
    domains = ["openload.io", "openload.co"]

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)
        self.net = Net()
        self.pattern = '//((?:www.)?openload\.(?:io|co))/(?:embed|f)/([0-9a-zA-Z-_]+)'

    def get_media_url(self, host, media_id):
        try:
            ticket_url = 'https://api.openload.io/1/file/dlticket?file=%s' % (media_id)
            result = self.net.http_GET(ticket_url).content
            js_result = json.loads(result)
            if js_result['status'] != 200:
                raise UrlResolver.ResolverError(js_result['msg'])
            video_url = 'https://api.openload.io/1/file/dl?file=%s&ticket=%s' % (media_id, js_result['result']['ticket'])
            captcha_url = js_result['result'].get('captcha_url', None)
            if captcha_url:
                captcha_response = captcha_lib.get_response(captcha_url)
                if captcha_response:
                    video_url += '&captcha_response=%s' % urllib.quote(captcha_response)
            xbmc.sleep(js_result['result']['wait_time'] * 1000)
            result = self.net.http_GET(video_url).content
            js_result = json.loads(result)
            if js_result['status'] != 200:
                raise UrlResolver.ResolverError(js_result['msg'])
            
            return js_result['result']['url'] + '?mime=true'
        except Exception as e:
            raise UrlResolver.ResolverError('Exception in openload: %s' % (e))
        
        raise UrlResolver.ResolverError('Unable to resolve openload.io link. Filelink not found.')

    def get_url(self, host, media_id):
            return 'http://openload.io/embed/%s' % (media_id)

    def get_host_and_id(self, url):
        r = re.search(self.pattern, url)
        if r:
            return r.groups()
        else:
            return False

    def valid_url(self, url, host):
        return re.search(self.pattern, url) or self.name  in host
