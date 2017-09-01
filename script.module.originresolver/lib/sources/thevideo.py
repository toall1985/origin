import re
import requests
import xbmc

domain = 'thevideo.me'
name = 'Thevideo'
sources = []

def resolve(url):
    if not 'embed' in url:
        url = url.replace('thevideo.me/','thevideo.me/embed-')+'.html'
    xbmc.log(url,xbmc.LOGNOTICE)
    html = requests.get(url).content
    m = re.findall("var lets_play_a_game='(.+?)'",html)[0]
    url = 'https://thevideo.me/vsign/player/'+m
    h = requests.get(url).content
    print h
    info = re.findall('jwConfig\|(.+?)\|',h)[0]
    if info == 'return':
        info = re.findall('function\|(.+?)\|',h)[0]
    File = re.findall('{"file":"(.+?)","label":"(.+?)"',html)
    for f,qual in File:
        playlink = f+'?direct=false&ua=1&vt='+info
        sources.append({'source': name, 'quality': qual, 'scraper': name, 'url': playlink,'direct': True})
    return sources


