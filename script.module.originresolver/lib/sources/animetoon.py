import re
import requests
import xbmc

domain = ['animetoon.org']
name = 'Animetoon'
sources = []

def resolve(url):
    html3 = requests.get(url).text
    match2 = re.compile('<iframe src="(.+?)"').findall(html3)
    for play in match2:
        xbmc.log(play,xbmc.LOGNOTICE)
        if 'zoo' in play:
            playname = 'videozoo'
        elif 'bb' in play:
            playname = 'playbb'
        elif 'easy' in play:
            playname = 'easyvideo'
        elif 'panda' in play:
            playname = 'playpanda'
        html4 = requests.get(play).content
        p = re.compile('"link":"(.+?)"').findall(html4)
        for link in p:
            xbmc.log(link,xbmc.LOGNOTICE)
            playlink = link.replace('\\','')
            sources.append({'source': playname, 'quality': playname, 'scraper': name, 'url': playlink,'direct': True})
        _url = re.compile('_url = "(.+?)"').findall(html4)
        for i in _url:
            xbmc.log(i,xbmc.LOGNOTICE)
            playlink = i.replace('\\','')
            sources.append({'source': playname, 'quality': playname, 'scraper': name, 'url': playlink,'direct': True})
    return sources