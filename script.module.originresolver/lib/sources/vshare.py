import re
import requests

domain = ['vshare.eu']
name = 'Vshare'
sources = []

def resolve(url):
    html = requests.get(url).content
    m = re.findall("file:.+?'(.+?)'",html)
    for playlink in m:
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    n = re.findall('file:.+?"(.+?)"',html)
    for playlink in n:
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources
