import re
import requests

domain = 'watchers.to'
name = 'Watchers'
sources = []

def resolve(url):
    html = requests.get(url).content
    m = re.findall('mp4\|(.+?)\|',html)
    for i in m:
        playlink = 'http://s11.speedvid.net:8777/' + i + 'v.mp4'
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    print sources

