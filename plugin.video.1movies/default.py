# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.1movies/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.1movies/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
   FAV = open(favourites).read()
else:
   FAV = []

def Main_Menu():
    Menu('Genre','',3,ICON,FANART,'','')
    Menu('Hot Movies','http://1movies.tv/movies/hot',1,ICON,FANART,'','')
    Menu('TV Series','http://1movies.tv/movies/series',1,ICON,FANART,'','')
    Menu('Most Watched','http://1movies.tv/movies/mostviewed',1,ICON,FANART,'','')
    Menu('Latest','http://1movies.tv/movies/latest',1,ICON,FANART,'','')
    Menu('Search','',2,ICON,FANART,'','')
	
def Genre():
    Menu(' Action','http://1movies.tv/genre/action',1,ICON,FANART,'','')
    Menu(' Adventure','http://1movies.tv/genre/adventure',1,ICON,FANART,'','')
    Menu(' Animation','http://1movies.tv/genre/animation',1,ICON,FANART,'','')
    Menu(' Biography','http://1movies.tv/genre/biography',1,ICON,FANART,'','')
    Menu(' Comedy','http://1movies.tv/genre/comedy',1,ICON,FANART,'','')
    Menu(' Crime','http://1movies.tv/genre/crime',1,ICON,FANART,'','')
    Menu(' Documentary','http://1movies.tv/genre/documentary',1,ICON,FANART,'','')
    Menu(' Drama','http://1movies.tv/genre/drama',1,ICON,FANART,'','')
    Menu(' Family','http://1movies.tv/genre/family',1,ICON,FANART,'','')
    Menu(' Fantasy','http://1movies.tv/genre/fantasy',1,ICON,FANART,'','')
    Menu(' Game show','http://1movies.tv/genre/game-show',1,ICON,FANART,'','')
    Menu(' History','http://1movies.tv/genre/history',1,ICON,FANART,'','')
    Menu(' Horror','http://1movies.tv/genre/horror',1,ICON,FANART,'','')
    Menu(' Movie horror','http://1movies.tv/genre/movie-horror',1,ICON,FANART,'','')
    Menu(' Music','http://1movies.tv/genre/music',1,ICON,FANART,'','')
    Menu(' Musical','http://1movies.tv/genre/musical',1,ICON,FANART,'','')
    Menu(' Mystery','http://1movies.tv/genre/mystery',1,ICON,FANART,'','')
    Menu(' News','http://1movies.tv/genre/news',1,ICON,FANART,'','')
    Menu(' Reality TV','http://1movies.tv/genre/reality-tv',1,ICON,FANART,'','')
    Menu(' Romance','http://1movies.tv/genre/romance',1,ICON,FANART,'','')
    Menu(' Sci-fi','http://1movies.tv/genre/sci-fi',1,ICON,FANART,'','')
    Menu(' Short','http://1movies.tv/genre/short',1,ICON,FANART,'','')
    Menu(' Sport','http://1movies.tv/genre/sport',1,ICON,FANART,'','')
    Menu(' Talk show','http://1movies.tv/genre/talk-show',1,ICON,FANART,'','')
    Menu(' Thriller','http://1movies.tv/genre/thriller',1,ICON,FANART,'','')
    Menu(' TV Series','http://1movies.tv/genre/tv-series',1,ICON,FANART,'','')
    Menu(' War','http://1movies.tv/genre/war',1,ICON,FANART,'','')
    Menu(' Western','http://1movies.tv/genre/western',1,ICON,FANART,'','')

def get_info(url):
	html = requests.get(url).content
	match = re.compile('<div class="item_movie">.+?href="(.+?)".+?title="(.+?)".+?img src="(.+?)".+?<span class="res">(.+?)</span>',re.DOTALL).findall(html)
	for url,name,image,qual in match:
		url = 'http:'+url
		if 'season' in name.lower():
			Menu(name,url,4,image,FANART,'',qual)
		elif 's0' in name.lower():
			Menu(name,url,4,image,FANART,'',qual)
		elif 's1' in name.lower():
			Menu(name,url,4,image,FANART,'',qual)
		elif 's2' in name.lower():
			Menu(name,url,4,image,FANART,'',qual)
		elif 's3' in name.lower():
			Menu(name,url,4,image,FANART,'',qual)
		else:
			Play(name+' ('+qual+')',url,5,image,FANART,'',qual)
	Next = re.compile('<li class="c-active">.+?href=".+?href="(.+?)"').findall(html)
	for n in Next:
		Menu('Next Page','http:'+n,1,ICON,FANART,'','')

def tv_show(url,qual):
	html = requests.get(url).content
	block = re.compile('<div class="ep_link full">(.+?)</div>',re.DOTALL).findall(html)
	for b in block:
		match = re.compile('<a href="(.+?)".+?>(.+?)<').findall(str(b))
		for u,n in match:
			Play(n+' ('+qual+')','http:'+u,5,ICON,FANART,'',qual)

		
def get_source(link,qual):
	xbmc.log('link:'+link,xbmc.LOGNOTICE)
	qual = qual
	html = requests.get(link).content
	match = re.compile('load_player\((.+?)\)').findall(html)
	for i in match:
		u = i
		headers = {
					"referer":link,
					"user-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
					"host":"1movies.tv"
				}
		item = 'http://1movies.tv/ajax/movie/load_player_v3?id='+u
		xbmc.log('item:'+item,xbmc.LOGNOTICE)
		head_req = requests.post(item,headers=headers).content
		xbmc.log('head_req:'+head_req,xbmc.LOGNOTICE)
		resp = re.compile('value":"(.+?)"').findall(head_req)
		for r in resp:
			new_headers = {
			"referer":link,
			"user-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
			"host":"xplay.1movies.tv"
			}
			newurl = 'http:'+r.replace('\\','')
			xbmc.log('newurl:'+newurl,xbmc.LOGNOTICE)
			response = requests.post(newurl,headers=new_headers).json()
			results = response["playlist"]
			for item in results:
				playlink = item["file"]
				resolve('Gvideo | ('+qual+')',playlink)
	
	
def Search():
   Search_url = 'http://1movies.tv/movies/search?s='
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
            contextMenu.append(('Remove from 1movies Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to 1movies Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
            contextMenu.append(('Remove from 1movies Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to 1movies Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
      favList.append(('1movies Favourites Section', '', '', '', '', '', ''))
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
	import urlresolver
	try:
		resolved_url = urlresolver.resolve(url)
		xbmc.Player().play(resolved_url, xbmcgui.ListItem(name))
	except:
		xbmc.Player().play(url, xbmcgui.ListItem(name))
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
elif mode == 3 : Genre()
elif mode == 4 : tv_show(url,extra)
elif mode == 5 : get_source(url,extra)
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