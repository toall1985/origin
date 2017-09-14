import re
import requests
import xbmc
from resources.jsunpack import unpack

domain = ['vidup.me']
name = 'Vidup'
sources = []

def resolve(url):
    if not 'embed' in url:
        url = url.replace('vidup.me/','vidup.me/embed-')+'-640x360.html'
    xbmc.log('START VIDUP:'+url,xbmc.LOGNOTICE)
    html = requests.get(url).content
    m = re.findall("var mpri_Key='(.+?)'",html)[0]
    u = 'http://vidup.me/jwv/'+m
    h = requests.get(u).content
    info_get = unpack(h)
    info = re.findall('vt=(.+?)"',info_get)[0]
    File = re.findall('{"file":"(.+?)","label":"(.+?)"',html)
    for f,qual in File:
        playlink = f+'?direct=false&ua=1&vt='+info
        sources.append({'source': name, 'quality': qual, 'scraper': name, 'url': playlink,'direct': True})
    return sources


