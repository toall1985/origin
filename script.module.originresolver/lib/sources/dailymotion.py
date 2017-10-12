import re
import requests

domain = ['dailymotion.com']
name = 'dailymotion'
sources = []

def resolve(url):
    quality = 'SD'
    html = requests.get(url).content
    match = re.findall('"type":"video.+?mp4","url":"(.+?)"}.+?,"(.+?)"',html)
    for playlink,quality in match:
        playlink = playlink.replace('\\','')
        if quality.lower() == 'reporting':
            pass
        else:
            sources.append({'source': name, 'quality': quality, 'scraper': name, 'url': playlink,'direct': True})
    return sources
