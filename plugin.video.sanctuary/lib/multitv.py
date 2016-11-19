# -*- coding: utf-8 -*-

import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, time, process, requests
from threading import Thread

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
addon_handle = int(sys.argv[1])
Main = 'http://www.watchseriesgo.to/'
List = []
IMDB = 'http://www.imdb.com'

def Search():
	pass
def Tv_Schedule(url):
	pass
					
def Genres():
	html = requests.get('http://www.imdb.com/genre/').text
	match = re.compile('<h3><a href="(.+?)">(.+?)<span class="normal">').findall(html)
	for url, name in match:
		process.Menu(name,url,304,'','','','')

def Genres_Page(url):
	pass

def Grab_Season(url,extra):
	pass

def Grab_Episode(url,name,fanart,extra,iconimage):
	pass
	
def Latest_Eps(url):
    OPEN = process.OPEN_URL(url)
    match = re.compile('<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">(.+?)</span></a></li>').findall(OPEN)
    for url,name,date in match:
        url = Main + url
        name = (name).replace('Seas.','Season').replace('Ep.','Episode').replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        process.Menu(name+' - [COLORred]'+date+'[/COLOR]',url,310,ICON,FANART,'','')
    	process.setView('Movies', 'INFO')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
		
def Popular(url):
    OPEN = process.OPEN_URL(url)
    match = re.compile('<div class="block-left-home-inside-image">.+?<img src="(.+?)".+?<a href="(.+?)".+?<b>(.+?)</b>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>',re.DOTALL).findall(OPEN)
    for img,url,name,season,desc in match:
        url = Main + url
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        process.Menu(name+' - '+season,url,310,img,FANART,desc,name)		
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	


