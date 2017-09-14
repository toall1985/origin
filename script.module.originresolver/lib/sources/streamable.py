import re
import requests

domain = ['streamable.com']
name = 'Streamable'
sources = []

def resolve(url):
    html = requests.get(url).content
    m = re.compile('source src="(.+?)"').findall(html)
    for s in m:
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': 'http:'+s,'direct': True})
    return sources
