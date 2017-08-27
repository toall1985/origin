import re
import requests

domain = ''
name = ''
sources = []

def resolve(url):
    html = requests.get(url).content
        sources.append({'source': name, 'quality': 'HD', 'scraper': name, 'url': playlink,'direct': True})
    return sources
