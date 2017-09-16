import re
import requests

domain = ['vidzi.tv','vidzi.cc']
name = 'Vidzi'
sources = []

def resolve(url):
    if '.cc' in url:
        try:
            html = requests.get(url).content
            url = re.findall('<iframe src="(.+?)"',html.lower())[0]
        except:
            url = url
    print url
    html = requests.get(url).content
    match = re.compile('file: "(.+?)"').findall(html)
    for playlink in match:
        if 'mp4' in playlink or 'm3u8' in playlink:
            sources.append({'source': name, 'quality': 'HD', 'scraper': name, 'url': playlink,'direct': True})
    return sources
