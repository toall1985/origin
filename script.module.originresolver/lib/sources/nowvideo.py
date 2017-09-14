import re
import requests

domain = ['nowvideo.sx']
name = 'Nowvideo'
sources = []

def resolve(url):
    html = requests.get(url).content
    p = re.findall('source src="(.+?)"',html)
    for playlink in p:
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources

