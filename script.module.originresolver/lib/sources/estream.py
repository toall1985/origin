import re
import requests

domain = ['estream.to']
name = 'Estream'
sources = []

def resolve(url):
    html = requests.get(url).content
    m = re.findall('source src="(.+?)"',html)
    for playlink in m:
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources

