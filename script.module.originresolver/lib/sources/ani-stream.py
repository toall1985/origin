import re
import requests

domain = ['ani-stream.com']
name = 'Anistream'
sources = []

def resolve(url):
    html = requests.get(url).content
    match = re.compile('file: "(.+?)".+?label: "',re.DOTALL).findall(html)
    for playlink in match:
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources
