import re
import requests
import xbmc
from resources.jsunpack import unpack

domain = ['thevideo.me']
name = 'Thevideo'
sources = []

def resolve(url):
    if not 'embed' in url:
        url = url.replace('thevideo.me/','thevideo.me/embed-')+'.html'
    xbmc.log(url,xbmc.LOGNOTICE)
    html = requests.get(url).content
    m = re.findall("var lets_play_a_game='(.+?)'",html)[0]
    player_url = 'https://thevideo.me/vsign/player/'+m
    h = requests.get(player_url).content
    info_get = unpack(h)
    info = re.findall('vt=(.+?)"',info_get)[0]
    if info == 'return':
        info = re.findall('function\|(.+?)\|',h)[0]
    File = re.findall('{"file":"(.+?)","label":"(.+?)"',html)
    for f,qual in File:
        playlink = f+'?direct=false&ua=1&vt='+info
        sources.append({'source': name, 'quality': qual, 'scraper': name, 'url': playlink,'direct': True})
    return sources


