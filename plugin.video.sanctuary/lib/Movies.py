# -*- coding: utf-8 -*-
import urllib,re,xbmcgui,xbmcplugin,xbmc,sys,process,requests


def Movie_Main():
    process.Menu('Genre','',202,'','','','')
    process.Menu('New Movies','http://www.pubfilm.biz/lastnews',203,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
def Movie_Genre(url):
	html = requests.get('http://www.imdb.com/genre/').text
	match = re.compile('<h3><a href="(.+?)">(.+?)<span class="normal">').findall(html)
	for url, name in match:
		url = 'http://www.imdb.com/search/title?genres='+name.replace(' ','').lower()+'&title_type=feature&sort=moviemeter,asc'
		process.Menu(name,url,203,'','','','')

def IMDB_Grab(url):
	html = requests.get(url).text
	match = re.compile('<div class="lister-item-image float-left">.+?<a href="(.+?)".+?<img alt="(.+?)".+?loadlate="(.+?)".+?<span class="lister-item-year text-muted unbold">(.+?)</span>',re.DOTALL).findall(html)
	for url,name,image,year in match:
		try:
			process.Menu(name+' '+year,url,9,image,'','',year)
		except:
			pass
			
def Check_Link(name,url,image):
    HTML = process.OPEN_URL(url)
    match = re.compile('<iframe width="660" height="400" scrolling="no" frameborder="0" src="http://mystream.la/external/(.+?)" allowFullScreen></iframe>').findall(HTML)
    for end in match:
        url = 'http://mystream.la/external/'+end
        process.Play(name,url,205,image,FANART,'','')        

def Get_playlink(url):
    HTML = process.OPEN_URL(url)
    match = re.compile('file:"(.+?)",label:"(.+?)"}').findall(HTML)
    for playlink,quality in match:
        process.Resolve(playlink)
		