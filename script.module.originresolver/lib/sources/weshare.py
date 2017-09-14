import re
import requests

domain = ['weshare.me']
name = 'Weshare'
sources = []

def resolve(url):
    if not 'mp4' in url:
        h = requests.get(url).content
	match = re.compile('source src="(.+?)"').findall(h)
	for p in match:
            sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': p,'direct': True})
    else:
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': url,'direct': True})
    return sources
