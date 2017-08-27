# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.footballorgin/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.footballorgin/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
   FAV = open(favourites).read()
else:
   FAV = []

def Main_Menu():
   Menu('Full Match Replay','http://www.footballorgin.com/category/full-match-replay/',1,ICON,FANART,'','')
   Menu('Review Show','http://www.footballorgin.com/category/review-show/',1,ICON,FANART,'','')
   Menu('Premier League','http://www.footballorgin.com/category/leagues/premier-league-epl/',1,ICON,FANART,'','')
   Menu('Other Leagues','',3,ICON,FANART,'','')
   Menu('Shows','http://www.footballorgin.com/category/tv-show/',1,ICON,FANART,'','')
   Menu('Cup Games','http://www.footballorgin.com',4,ICON,FANART,'','')
   Menu('UFC','http://www.footballorgin.com/category/ufc/',1,ICON,FANART,'','')
   Menu('Search','',2,ICON,FANART,'','')
   
def other_leagues():
	Menu('UCL','http://www.footballorgin.com/category/cup-games/uefa-champions-league-ucl/',1,ICON,FANART,'','')
	Menu('LA LIGA','http://www.footballorgin.com/category/leagues/la-liga/',1,ICON,FANART,'','')
	Menu('SCOTTISH PREMIERSHIP','http://www.footballorgin.com/category/leagues/scottish-premiership/',1,ICON,FANART,'','')
	Menu('CHAMPIONSHIP','http://www.footballorgin.com/category/leagues/championship/',1,ICON,FANART,'','')
	Menu('SERIE A','http://www.footballorgin.com/category/leagues/serie-a/',1,ICON,FANART,'','')
	Menu('BUNDESLIGA','http://www.footballorgin.com/category/leagues/bundesliga/',1,ICON,FANART,'','')
	Menu('LIGUE 1','http://www.footballorgin.com/category/leagues/ligue-1/',1,ICON,FANART,'','')
	
def cup_games(url):
	html = requests.get(url).content
	block = re.compile('Cup Games</a>(.+?)</ul>',re.DOTALL).findall(html)
	for b in block:
		match = re.compile('href="(.+?)">(.+?)</a>').findall(str(b))
		for url,name in match:
			Menu(name.replace('&#8211;','-'),url,1,ICON,FANART,'','')
	
def get_info(url):
	html = requests.get(url).content
	match = re.compile('<div class="thumbnail">.+?href="(.+?)".+?img.+?src="(.+?)".+?rel="bookmark">(.+?)</a>',re.DOTALL).findall(html)
	for u,image,name in match:
		Menu(name.replace('&#8211;','-'),u,5,image,FANART,'','')
	Menu('Next Page','',6,ICON,FANART,url,'1')
	
def get_links(url):
	html = requests.get(url).content
	link = re.compile('"entry-subtitle">(.+?)</h2>.+?src="(.+?)"',re.DOTALL).findall(html)
	for name,l in link:
		Play('Play',l,20,ICON,FANART,'','')
	other_links = re.compile('<span class="numbers">(.+?)</span> <a href="(.+?)">(.+?)</a></li>').findall(html)
	for no, u, n in other_links:
		if not url == u:
			Menu(n,u,5,ICON,FANART,'','')
	link = re.compile('<video autoplay preload="metadata">.+?src="(.+?)"',re.DOTALL).findall(html)
	for li in link:
		Play('Play',li,20,ICON,FANART,'','')
	iframe = re.compile('iframe.+?src="(.+?)"').findall(html)
	for i in iframe:
		Play('Play',i,20,ICON,FANART,'','')
	
def next_page_loop(referer,page):
	if page == None:
		page = 2
	else:
		page = int(page)+1
	next_page = 'http://www.footballorgin.com/wp-admin/admin-ajax.php'
	headers = {
				'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
				'host':'www.footballorgin.com',
				'Referer':referer,
				}
	data = {
			'page_no':str(page),
			'action':'infinite_scroll'
			}
	h = requests.post(next_page,headers=headers,data=data).content
	match = re.compile('href="(.+?)" rel="bookmark">.+?src="(.+?)".+?rel="bookmark">(.+?)</a>',re.DOTALL).findall(h)
	for url,image,name in match:
		Menu(name.replace('&#8211;','-'),url,5,image,FANART,'','')
	Menu('Next Page','',6,ICON,FANART,referer,str(page))
	

def Search():
   Search_url = 'http://www.footballorgin.com/?s='
   Dialog = xbmcgui.Dialog()
   Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
   Search_name = Search_title.replace(' ','+').lower()
   url = Search_url+Search_name
   get_info(url)
	
def setView(content, viewType):
   # set content type so library shows more views and info
   if content:
      xbmcplugin.setContent(int(sys.argv[1]), content)
   if ADDON.getSetting('auto-view')=='true':
      xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
		
		
def Menu(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={},referer=None,page=None):
      fav_mode = mode
      u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
      ok=True
      liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
      liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
      liz.setProperty( "Fanart_Image", fanart )
      if showcontext:
         contextMenu = []
         if showcontext == 'fav':
            contextMenu.append(('Remove from footballorgin Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to footballorgin Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                   %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
         liz.addContextMenuItems(contextMenu)
      ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
      return ok
      xbmcplugin.endOfDirectory(int(sys.argv[1]))
      

		
def Play(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
      fav_mode = mode
      u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
      ok=True
      liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
      liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
      liz.setProperty( "Fanart_Image", fanart )
      if showcontext:
         contextMenu = []
         if showcontext == 'fav':
            contextMenu.append(('Remove from footballorgin Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to footballorgin Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                   %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
         liz.addContextMenuItems(contextMenu)
         contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=14)' % sys.argv[0]))
      ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
      return ok
      xbmcplugin.endOfDirectory(int(sys.argv[1]))
		
		
# ===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------

def addFavorite(name, url, mode, iconimage, fanart, description, extra):
   favList = []
   xbmc.log(extra)
   try:
      name = name.encode('utf-8', 'ignore')
   except:
      pass
   if os.path.exists(favourites) == False:
      favList.append((name, url, mode, iconimage, fanart, description, extra))
      a = open(favourites, "w")
      a.write(json.dumps(favList))
      a.close()
   else:
      a = open(favourites).read()
      data = json.loads(a)
      data.append((name, url, mode, iconimage, fanart, description, extra))
      b = open(favourites, "w")
      b.write(json.dumps(data))
      b.close()


def getFavourites():
   if not os.path.exists(favourites):
      favList = []
      favList.append(('footballorgin Favourites Section', '', '', '', '', '', ''))
      a = open(favourites, "w")
      a.write(json.dumps(favList))
      a.close()
   else:
      items = json.loads(open(favourites).read())
      for i in items:
         name = i[0]
         url = i[1]
         try:
			   iconimage = i[3]
         except:
            iconimage = ''
         try:
            fanart = i[4]
         except:
            fanart = ''
         try:
            description = i[5]
         except:
            description = ''
         try:
            extra = i[6]
         except:
            extra = ''

         if i[2] == 20:
            Play(name, url, i[2], iconimage, fanart, description, extra, 'fav')
         else:
            Menu(name, url, i[2], iconimage, fanart, description, extra, 'fav')


def rmFavorite(name):
   data = json.loads(open(favourites).read())
   for index in range(len(data)):
      if data[index][0] == name:
         del data[index]
         b = open(favourites, "w")
         b.write(json.dumps(data))
         b.close()
         break
   xbmc.executebuiltin("XBMC.Container.Refresh")		

def resolve(name,url):
	if not url.startswith('http:'):
		if not url.startswith('https'):
			url = 'http:'+url
	if 'playlist.m3u8' in url:
		xbmc.Player().play(url, xbmcgui.ListItem(name))
	else:
		import originresolver
		originresolver.originresolver(name,url)
	xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
def get_params():
      param=[]
      paramstring=sys.argv[2]
      if len(paramstring)>=2: 
            params=sys.argv[2] 
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                  params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}   
            for i in range(len(pairsofparams)):
                  splitparams={}
                  splitparams=pairsofparams[i].split('=')
                  if (len(splitparams))==2:
                        param[splitparams[0]]=splitparams[1]
                        
      return param
      
params=get_params()
url=None
name=None
iconimage=None
mode=None
fanart=None
description=None
trailer=None
fav_mode=None
extra=None

try:
   extra=urllib.unquote_plus(params["extra"])
except:
   pass

try:
   fav_mode=int(params["fav_mode"])
except:
   pass

try:
      url=urllib.unquote_plus(params["url"])
except:
      pass
try:
      name=urllib.unquote_plus(params["name"])
except:
      pass
try:
      iconimage=urllib.unquote_plus(params["iconimage"])
except:
      pass
try:      
      mode=int(params["mode"])
except:
      pass
try:      
      fanart=urllib.unquote_plus(params["fanart"])
except:
      pass
try:      
      description=urllib.unquote_plus(params["description"])
except:
      pass

#####################################################END PROCESSES##############################################################		
		
if mode == None: Main_Menu()
elif mode == 1 : get_info(url)
elif mode == 2 : Search()
elif mode == 3 : other_leagues()
elif mode == 4 : cup_games(url)
elif mode == 5 : get_links(url)
elif mode == 6 : next_page_loop(description,extra)

elif mode == 10: getFavourites()
elif mode==11:
   try:
      name = name.split('\\ ')[1]
   except:
      pass
   try:
      name = name.split('  - ')[0]
   except:
      pass
   addFavorite(name, url, fav_mode, iconimage, fanart, description, extra)
elif mode==12:
   try:
      name = name.split('\\ ')[1]
   except:
      pass
   try:
      name = name.split('  - ')[0]
   except:
      pass
   rmFavorite(name)
elif mode == 14 : queueItem()	
elif mode == 20: resolve(name,url)
elif mode == 21: xbmc.Player().play(url, xbmcgui.ListItem(name))

xbmcplugin.endOfDirectory(int(sys.argv[1]))