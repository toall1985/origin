# -*- coding: UTF-8 -*-
"""
    Copyright (C) 2014  smokdpi

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
import urllib
import re
import xbmcgui


class UpToBoxResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver, PluginSettings]
    name = "uptobox"
    domains = ["uptobox.com", "uptostream.com"]

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)
        self.net = Net()
        self.pattern = 'http[s]*://(upto(?:box|stream)\.com)/([a-zA-Z0-9]+)'
        self.user_agent = common.IE_USER_AGENT
        self.net.set_user_agent(self.user_agent)
        self.headers = {'User-Agent': self.user_agent}

    def get_url(self, host, media_id):
        """
        return url for uptostream, less country restrictions and no time limit on link generation
            (90%+ of random links tested had streaming links)
        check if file has not been made available for streaming in get_media_url and fail-back to uptobox if necessary
        """
        return 'http://uptostream.com/%s' % media_id

    def get_host_and_id(self, url):
        r = re.search(self.pattern, url)
        if r: return r.groups()
        else: return False

    def valid_url(self, url, host):
        if self.get_setting('enabled') == 'false': return False
        return re.match(self.pattern, url) or host in self.domains

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        stream_url = None
        self.headers['Referer'] = web_url
        html = self.net.http_GET(web_url, headers=self.headers).content
        if isinstance(html, unicode):
            html = html.encode('utf-8', 'ignore')
        if 'This file is not available to stream yet' in html:
            web_url = 'http://uptobox.com/%s' % media_id
            self.headers['Referer'] = web_url
            html = self.net.http_GET(web_url, headers=self.headers).content
            if isinstance(html, unicode):
                html = html.encode('utf-8', 'ignore')
            if 'Uptobox.com is not available in your country' in html:
                raise UrlResolver.ResolverError('Uptobox.com is not available in your country')
            else:
                r = re.search('(You have to wait (?:[0-9]+ minute[s]*, )*[0-9]+ second[s]*)', html)
                if r:
                    raise UrlResolver.ResolverError(r.group(1))
            r = re.search('<form\sname\s*=[\'"]F1[\'"].+?>(.+?)<br\s*/*>', html, re.DOTALL)
            if r:
                r = r.group(1)
                form_data = {}
                form_inputs = re.compile('input\stype\s*=\s*[\'"]hidden[\'"]\sname\s*=\s*[\'"](.+?)[\'"]\svalue\s*=\s*[\'"](.+?)[\'"]\s*>').findall(r)
                if form_inputs:
                    for key, value in form_inputs:
                        form_data[key] = value
                html = self.net.http_POST(web_url, form_data=form_data, headers=self.headers).content
                if isinstance(html, unicode):
                    html = html.encode('utf-8', 'ignore')
                r = re.search('<a\shref\s*=[\'"](.+?)[\'"]\s*>\s*<span\sclass\s*=\s*[\'"]button_upload green[\'"]\s*>', html)
                if r:
                    stream_url = r.group(1)
        else:
            r = re.search('<video\sid.+?>(.+?)</video>', html, re.DOTALL)
            if r:
                r = r.group(1)
                sources = re.compile('<source.+?src\s*=\s*[\'"](.+?)[\'"].+?data-res\s*=\s*[\'"](.+?)[\'"].*?/>').findall(r)
                if sources:
                    if len(sources) == 1:
                        stream_url = sources[0][0]
                    elif len(sources) > 1:
                        vid_list = []
                        for source, quality in sources:
                            vid_list.extend(['Uptobox - %s' % quality])
                        if self.get_setting('auto_pick') == 'true':
                            stream_url = sources[-1][0]
                        else:
                            result = xbmcgui.Dialog().select('Choose Quality', vid_list)
                            if result != -1:
                                stream_url = sources[result][0]
                            else:
                                raise UrlResolver.ResolverError('No quality selected')
        if stream_url:
            return stream_url
        else:
            raise UrlResolver.ResolverError('File not found')

    def get_settings_xml(self):
        xml = PluginSettings.get_settings_xml(self)
        xml += '<setting id="%s_auto_pick" type="bool" label="Automatically pick best quality" default="false" visible="true"/>' % (self.__class__.__name__)
        return xml
