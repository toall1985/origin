import re
import requests

domain = ['vidlox.tv']
name = 'Vidlox'
sources = []

def resolve(url):
    html = requests.get(url).content
    m = re.compile('sources:.+?\[(.+?)\]').findall(html)
    for s in m:
        single = re.findall('"(.+?)"',str(s))
        for playlink in single:
            sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources
