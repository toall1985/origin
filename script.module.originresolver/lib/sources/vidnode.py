import re
import requests

domain = ['vidnode.net']
name = 'Vidnode'
sources = []

def resolve(url):
    html = requests.get(url).content
    match = re.compile("file: '(.+?)'.+?label: '(.+?)'").findall(html)
    for playlink,quality in match:
        quality = quality.replace(' P','p')
        if 'auto' in quality.lower():
            if '=m22':
                quality = '720p'
            elif '=m18' in quality.lower():
                quality = '360p'
            elif '=m37' in quality.lower():
                quality = '1080p'
            elif '=m59' in quality.lower():
                quality = '480p'
            else:
                quality = 'SD'
        sources.append({'source': name, 'quality': quality, 'scraper': name, 'url': playlink,'direct': True})
    print sources
