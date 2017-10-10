# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.yesmovies/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.yesmovies/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
   FAV = open(favourites).read()
else:
   FAV = []

def Main_Menu():
   Menu('Genre','https://yesmovies.to/',1,ICON,FANART,'','')
   Menu('TV-Series','https://yesmovies.to/movie/filter/series.html',3,ICON,FANART,'','')
   Menu('Top IMDb','https://yesmovies.to/top-imdb/all.html',4,ICON,FANART,'','')
   Menu('Search','',2,ICON,FANART,'','')
   
def imdb():
   Menu('TV Shows','https://yesmovies.to/top-imdb/series.html',3,ICON,FANART,'','')
   Menu('Movies','https://yesmovies.to/top-imdb/movie.html',3,ICON,FANART,'','')
   
def Get_Info(url):
	html = requests.get(url).content
	match = re.compile('<div class="ml-item">.+?href="(.+?)".+?title="(.+?)".+?img.+?data-original="(.+?)"',re.DOTALL).findall(html)
	for url,name,image in match:
		if '-season-' in url:
			Menu(name,url,5,image,FANART,'','')
		else:
			Play(name,url,20,image,FANART,'','')
	
		
	Next = re.compile('<li class="active">.+?<li>.+?href="(.+?)"').findall(html)
	for u in Next:
		Menu('Next Page',u,3,ICON,FANART,'','')

		
		
def tv_show(url):
	xbmc.log('url:'+url,xbmc.LOGNOTICE)
	html2 = requests.get(url).content
	match2 = re.findall('favorite\((.+?),',html2)[0]
	xbmc.log('https://yesmovies.to/ajax/v4_movie_episodes/'+match2,xbmc.LOGNOTICE)
	get_ep = requests.get('https://yesmovies.to/ajax/v4_movie_episodes/'+match2).content
	block = re.compile('<ul id=.+?"episodes-sv-6(.+?)"(.+?)ul>',re.DOTALL).findall(get_ep)
	for c,u in block:
		if '9' in c:
			pass
		else:
			m = re.compile('<li class=.+?"ep-item .+?".+?data-server=.+?"(.+?)" data-id=.+?"(.+?)".+?title=.+?"(.+?)">').findall(str(u))
			for s,i,t in m:
				xbmc.log(i.replace('\\','')+'-'+s.replace('\\',''),xbmc.LOGNOTICE)
				Menu(t.replace('\\','')+' | Server 6',i.replace('\\',''),6,ICON,FANART,'',match2)
	block2 = re.compile('<ul id=.+?"episodes-sv-7(.+?)"(.+?)ul>',re.DOTALL).findall(get_ep)
	for c2,u2 in block2:
		if '9' in c2:
			pass
		else:
			m2 = re.compile('<li class=.+?"ep-item .+?".+?data-server=.+?"(.+?)" data-id=.+?"(.+?)".+?title=.+?"(.+?)">').findall(str(u2))
			for s2,i2,t2 in m2:
				xbmc.log(i2.replace('\\','')+'-'+s2.replace('\\',''),xbmc.LOGNOTICE)
				Menu(t2.replace('\\','')+' | Server 7',i2.replace('\\',''),6,ICON,FANART,'',match2)
	
def get_ep_source(m,match):
	url = 'https://yesmovies.to/ajax/movie_token?eid='+m+'&mid='+match
	xbmc.log(url+']',xbmc.LOGNOTICE)
	html3 = requests.get(url).content
	x,y = re.findall("_x='(.+?)', _y='(.+?)'",html3)[0]
	fin_url = 'https://yesmovies.to/ajax/movie_sources/'+m+'?x='+x+'&y='+y
	xbmc.log(fin_url+']',xbmc.LOGNOTICE)
	h = requests.get(fin_url).content
	source = re.findall('"sources":\[(.+?)\]',h)
	single = re.findall('{(.+?)}',str(source))
	for s in single:
		xbmc.log(s,xbmc.LOGNOTICE)
		playlink = re.findall('"file":"(.+?)"',str(s))
		try:
			qual = re.findall('"label":"(.+?)"',str(s))[0]
		except:
			qual = 'SD'
		for p in playlink:
			p = p.replace('\\','')
			if 'lemon' in p:
				p = p+'|User-Agent=Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0&Host=streaming.lemonstream.me:1443&Referer=https://yesmovies.to'
			if 'http' in p:
				Play(qual,p,21,ICON,FANART,'','')

	
	
	
	
def genre(url):
	html = requests.get(url).content
	block = re.compile('<a href="#" title="Genre">(.+?)</ul>',re.DOTALL).findall(html)
	for m in block:
		match = re.compile('href="(.+?)".+?title="(.+?)"').findall(str(m))
		for u,n in match:
			Menu(n,u,3,ICON,FANART,'','')
	
  

def Search():
	Search_url = 'https://yesmovies.to/search/'
	Dialog = xbmcgui.Dialog()
	Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
	Search_name = Search_title.replace(' ','+').lower()
	url = Search_url+Search_name
	html = requests.get(url).content
	match = re.compile('<div class="ml-item">.+?href="(.+?)".+?title="(.+?)".+?img.+?data-original="(.+?)"',re.DOTALL).findall(html)
	for url,name,image in match:
		Menu(name,url,5,image,FANART,'','')
	Next = re.compile('<li class="active">.+?<li>.+?href="(.+?)"').findall(html)
	for u in Next:
		Menu('Next Page',u,3,ICON,FANART,'','')
	
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
            contextMenu.append(('Remove from yesmovies Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to yesmovies Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
            contextMenu.append(('Remove from yesmovies Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to yesmovies Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
      favList.append(('yesmovies Favourites Section', '', '', '', '', '', ''))
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
	try:
		import originresolver
		originresolver.originresolver(name,url)
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
elif mode == 1 : genre(url)
elif mode == 2 : Search()
elif mode == 3 : Get_Info(url)
elif mode == 4 : imdb()
elif mode == 5 : tv_show(url)
elif mode == 6 : get_ep_source(url,extra)


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