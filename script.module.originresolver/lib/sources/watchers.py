import re
import requests

domain = ['watchers.to']
name = 'Watchers'
sources = []

def resolve(url):
    html = requests.get(url).content
    m = re.findall('empty\|(.+?)\|',html)
    for i in m:
        playlink = 'http://file26.watchers.to/' + i + 'v.mp4'
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources















