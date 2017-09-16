import re
import requests

domain = ['']
name = ''
sources = []
url = ''

def resolve(url):
    html = requests.get(url).content
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    print sources

resolve(url)
