import re
import requests

domain = 'vidtodo.com'
name = 'Vidtodo'
sources = []

def resolve(url):
    if 'embed' in url:
        u = re.findall('(.+?)-(.+?)-',str(url))
        for one,two in u:
            url = one.replace('embed','')+two
    html = requests.get(url).content
    m = re.compile('mp4\|(.+?)\|').findall(html)
    for n in m:
        playlink = 'http://94.176.148.22/'+n+'/v.mp4'
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources


