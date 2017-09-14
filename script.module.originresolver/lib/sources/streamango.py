import re
import requests

domain = ['streamango.com']
name = 'Streamango'

sources = []

def resolve(url):
    html = requests.get(url).content
    match = re.compile('type:"video/mp4",src:"(.+?)",height:(.+?),').findall(html)
    for p,qual in match:
        url = 'http:'+url
        sources.append({'source': 'Streamango', 'quality': qual, 'scraper':name, 'url': p,'direct': True})
    return sources
