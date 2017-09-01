# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.project-free-tv/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.project-free-tv/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
   FAV = open(favourites).read()
else:
   FAV = []

def Main_Menu():
   Menu('Tv Shows','http://project-free-tv.ag/watch-series/',4,ICON,FANART,'','')
#   Menu('Movies','http://project-free-tv.ag/movies/',1,ICON,FANART,'','')
   Menu('Search','',3,ICON,FANART,'','')
   
def Movies(url):
	Menu('Latest Movies','http://project-free-tv.ag/movies/',9,ICON,FANART,'','')
	Menu('Years','http://project-free-tv.ag/movies/',9,ICON,FANART,'','')
	Menu('Genres','http://project-free-tv.ag/movies/',9,ICON,FANART,'','')
	
def get_movies_info(url):
	html = requests.get(url).content
	m = re.compile('<div style="float:left;width:124px;text-align:center;height:220px;">.+?<a href="(.+?)".+?title="(.+?)".+?img src="(.+?)"',re.DOTALL).findall(html)
	for u,n,i in m:
		Menu(n,'http://project-free-tv.ag'+u,8,i,FANART,'','')
	next = re.findall("class='pagination'>.+?<li.+?</li><li><a rel='nofollow' href='(.+?)'",html)
	for n in next:
		Menu('Next Page',n,9,ICON,FANART,'','')
	
def Tv_Shows(url):
	letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
	for letter in letters:
		try:
			letter = letter.upper()
		except:
			letter = letter
		Menu(letter,url,5,ICON,FANART,'','')
		
def tv_alpha(name,url):
	html = requests.get(url).content
	match = re.findall('<li><a href="(.+?)" title=".+?">(.+?)</a></li>',html)
	for u,n in match:
		if n.lower().startswith(name.lower()):
			Menu(n,'http://project-free-tv.ag'+u,6,ICON,FANART,'','')
			
def tv_seasons(url):
	try:
		html = requests.get(url).content
		block = re.compile('All Seasons</div>(.+?)<div',re.DOTALL).findall(html)
		for b in block:
			match = re.findall('href="(.+?)" >(.+?)</a>',str(b))
			for u,name in match:
				Menu(name,u,7,ICON,FANART,'','')
	except:
		tv_episodes(url)
		
def tv_episodes(url):
	html = requests.get(url).content
	match = re.compile('<div align="left">.+?href="(.+?)">(.+?)</a>',re.DOTALL).findall(html)
	for u,n in match:
		Menu(n,u,8,ICON,FANART,'','')
		
def playlinks(url):
	html = requests.get(url).content
	block = re.compile('<tr>(.+?)</tr>',re.DOTALL).findall(html)
	for b in block:
		if 'aff_id' in str(b):
			m = re.compile('<img src="(.+?)".+?>(.+?)</a>.+?\'http(.+?)\'',re.DOTALL).findall(str(b))
			for img,name,u in m:
				name = name.replace('&nbsp;','').replace('&nbsp','').replace('  ','')
				u = 'http'+u
				Play(name,u,20,img,FANART,'','')
		
	
def search_choice():
   Menu('Search Movies','',2,ICON,FANART,'','Movies')
   Menu('Search Tv Shows','',2,ICON,FANART,'','TV')
	
def Search(extra):
	if extra == 'Movies':
		Search_url = 'http://project-free-tv.ag/movies/search-form/?free='
	elif extra == 'TV':
		Search_url = 'http://project-free-tv.ag/search-tvshows/?free='
	Dialog = xbmcgui.Dialog()
	Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
	Search_name = Search_title.replace(' ','%20').lower()
	url = Search_url+Search_name
	if extra == 'Movies':
		get_movies_info(url)
	elif extra == 'TV':
		tv_search(url)
		
def tv_search(url):
	html = requests.get(url).content
	match = re.compile('<div align="left">.+?href="(.+?)".+?>(.+?)</a>',re.DOTALL).findall(html)
	for u,n in match:
		if 'season' in n.lower():
			Menu( n,'http://project-free-tv.ag'+u,7,ICON,FANART,'','')
		else:
			Menu( n,'http://project-free-tv.ag'+u,6,ICON,FANART,'','')
	
def setView(content, viewType):
   # set content type so library shows more views and info
   if content:
      xbmcplugin.setContent(int(sys.argv[1]), content)
   if ADDON.getSetting('auto-view')=='true':
      xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
		
		
def Menu(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
      fav_mode = mode
      u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
      ok=True
      liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
      liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
      liz.setProperty( "Fanart_Image", fanart )
      if showcontext:
         contextMenu = []
         if showcontext == 'fav':
            contextMenu.append(('Remove from project-free-tv Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to project-free-tv Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
            contextMenu.append(('Remove from project-free-tv Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to project-free-tv Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
      favList.append(('project-free-tv Favourites Section', '', '', '', '', '', ''))
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
elif mode == 1 : Movies(url)
elif mode == 2 : Search(extra)
elif mode == 3 : search_choice()
elif mode == 4 : Tv_Shows(url)
elif mode == 5 : tv_alpha(name,url)
elif mode == 6 : tv_seasons(url)
elif mode == 7 : tv_episodes(url)
elif mode == 8 : playlinks(url)
elif mode == 9 : get_movies_info(url)
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

xbmcplugin.endOfDirectory(int(sys.argv[1]))