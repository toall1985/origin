import re
import requests

domain = ['vidzi.tv']
name = 'Vidzi'
sources = []

def resolve(url):
    html = requests.get(url).content
    match = re.compile('file: "(.+?)"').findall(html)
    for playlink in match:
        sources.append({'source': name, 'quality': 'HD', 'scraper': name, 'url': playlink,'direct': True})
    return sources
