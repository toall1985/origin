'''
Hugefiles urlresolver plugin
Copyright (C) 2013 Vinnydude

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
'''

from t0mm0.common.net import Net
from urlresolver.plugnplay.interfaces import UrlResolver
from urlresolver.plugnplay.interfaces import PluginSettings
from urlresolver.plugnplay import Plugin
import re
from lib import jsunpack
from urlresolver import common
from lib import captcha_lib

class HugefilesResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver, PluginSettings]
    name = "hugefiles"
    domains = ["hugefiles.net"]

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)
        self.net = Net()

    def get_media_url(self, host, media_id):
        return self.__get_link(self.get_url(host, media_id))

    def __get_link(self, url):
        headers = {
            'User-Agent': common.IE_USER_AGENT
        }
        common.addon.log_debug('HugeFiles: get_link: %s' % (url))
        html = self.net.http_GET(url, headers).content
        
        # Re-grab data values
        data = {}
        r = re.findall(r'type="hidden" name="(.+?)" value="(.+?)"', html)
        
        if r:
            for name, value in r:
                data[name] = value
        else:
            raise UrlResolver.ResolverError('Unable to resolve link')
        
        data.update(captcha_lib.do_captcha(html))
        
        common.addon.log_debug('HugeFiles - Requesting POST URL: %s with data: %s' % (url, data))
        data['referer'] = url
        html = self.net.http_POST(url, data, headers).content
        
        # try download link
        link = re.search('id="lnk_download[^"]*" href="([^"]+)', html)
        stream_url = None
        if link:
            common.addon.log_debug('HugeFiles Download Found: %s' % link.group(1))
            stream_url = link.group(1)
        else:
            # try flash player link
            packed = re.search('id="player_code".*?(eval.*?)</script>', html, re.DOTALL)
            if packed:
                js = jsunpack.unpack(packed.group(1))
                js = js.replace('\\', '')
                patterns = ["name=[\"']src[\"']\s*value=['\"]([^'\"]+)", "['\"]file['\"]\s*,\s*['\"]([^'\"]+)", "<source[^>]+src=['\"]([^'\"]+)"]
                for pattern in patterns:
                    link = re.search(pattern, js)
                    if link:
                        common.addon.log_debug('Hugefiles Src Found: %s' % link.group(1))
                        stream_url = link.group(1)
                        break
                        
        if stream_url:
            return stream_url + '|User-Agent=%s&Referer=%s' % (common.IE_USER_AGENT, url)
        else:
            raise UrlResolver.ResolverError('Unable to resolve link')
        
    def get_url(self, host, media_id):
        return 'http://hugefiles.net/embed-%s.html' % media_id

    def get_host_and_id(self, url):
        r = re.search('//(.+?)/([0-9a-zA-Z]+)', url)
        if r:
            return r.groups()
        else:
            return False
        return('host', 'media_id')

    def valid_url(self, url, host):
        if self.get_setting('enabled') == 'false': return False
        return (re.match('http://(www.)?hugefiles.net/' +
                         '[0-9A-Za-z]+', url) or
                         'hugefiles' in host)
