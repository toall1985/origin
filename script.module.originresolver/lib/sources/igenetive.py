import re
import requests

domain = ['igenetive.com']
name = 'Igenetive'
sources = []

def resolve(url):
    html = requests.get(url).content
    playlink = re.findall('iframe src="(.+?)"')[0]
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources


