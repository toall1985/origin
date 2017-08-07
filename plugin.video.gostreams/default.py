# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.gostreams/')
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
   Menu('Genre','https://gostream.is',1,ICON,FANART,'','')
   Menu('TV-Series','https://gostream.is/movie/filter/series',3,ICON,FANART,'','')
   Menu('Top IMDb','https://gostream.is/movie/topimdb',4,ICON,FANART,'','')
   Menu('Search','',2,ICON,FANART,'','')
   
def imdb():
   Menu('TV Shows','https://gostream.is/movie/topimdb/series',3,ICON,FANART,'','')
   Menu('Movies','https://gostream.is/movie/topimdb/movie',3,ICON,FANART,'','')
   
def Get_Info(url):
	List = []
	html = requests.get(url).content
	match = re.compile('div data-movie-id=.+?href="(.+?)".+?title="(.+?)".+?img.+?data-original="(.+?)"',re.DOTALL).findall(html)
	for url,name,image in match:
		url = url+'watching.html'
		Menu(name,url,5,image,FANART,'','')
	Next = re.compile('<li class="active">.+?<li>.+?href="(.+?)"').findall(html)
	for u in Next:
		if u not in List:
			Menu('Next Page',u,3,ICON,FANART,'','')
			List.append(u)

def movie_check(url):
	if '-season-' in url:
		tv_show(url)
	else:
		movie(url)
		
def movie(link):
	qual = ''
	html3 = requests.get(link).text
	match3 = re.compile('<a onclick="favorite\((.+?),',re.DOTALL).findall(html3)
	for i in match3:
		html4 = requests.get('https://gostream.is/ajax/movie_episodes/'+i).json()
        data = re.findall('data-id="(.+?)"',html4['html'])
        for u in data:
			if len(u) == 6:
				s = 'https://gostream.is/ajax/movie_token?eid='+u+'&mid='+i
				html3 = requests.get(s).content
				x,y = re.findall("_x='(.+?)', _y='(.+?)'",html3)[0]
				fin_url = 'https://gostream.is/ajax/movie_sources/'+u+'?x='+x+'&y='+y
				h = requests.get(fin_url).content
				source = re.findall('"sources":\[(.+?)\]',h)
				single = re.findall('{(.+?)}',str(source))
				for l in single:
					playlink = re.findall('"file":"(.+?)"',str(l))
					qua = re.findall('"label":"(.+?)"',str(l))
					for q in qua:
						qual = q
					for p in playlink:
						if 'lemon' not in p:
							if 'http' in p:
								p = p.replace('\\','')
								Play(qual,p,20,ICON,FANART,'','')

 	
		
def tv_show(url):
	html2 = requests.get(url).content
	match2 = re.findall('favorite\((.+?),',html2)[0]
	get_ep = requests.get('https://gostream.is/ajax/movie_episodes/'+match2).content
	xbmc.log('##############https://gostream.is/ajax/movie_episodes/'+match2,xbmc.LOGNOTICE)
	block = re.compile('sv-6(.+?)"(.+?)clearfix',re.DOTALL).findall(get_ep)
	for b,c in block:
		if '9' in b:
			pass
		else:
			m = re.compile('title=.+?"(.+?)".+?data-id=.+?"(.+?)"',re.DOTALL).findall(str(c))
			for i,t in m:
				if len(t.replace('\\',''))==6:
					Menu(i.replace('\\',''),t.replace('\\',''),6,ICON,FANART,'',match2)
	
def get_ep_source(m,match):
	url = 'https://gostream.is/ajax/movie_token?eid='+m+'&mid='+match
	xbmc.log(url,xbmc.LOGNOTICE)
	html3 = requests.get(url).content
	x,y = re.findall("_x='(.+?)', _y='(.+?)'",html3)[0]
	fin_url = 'https://gomovies.is/ajax/movie_sources/'+m+'?x='+x+'&y='+y
	h = requests.get(fin_url).content
	source = re.findall('"sources":\[(.+?)\]',h)
	single = re.findall('{(.+?)}',str(source))
	for s in single:
		playlink = re.findall('"file":"(.+?)"',str(s))
		qual = re.findall('"label":"(.+?)"',str(s))[0]
		for p in playlink:
			if 'lemon' not in p:
				if 'http' in p:
					p = p.replace('\\','')
					Play(qual,p,20,ICON,FANART,'','')

	
	
	
	
def genre(url):
	html = requests.get(url).content
	block = re.compile('<a href="#" title="Genre">(.+?)</ul>',re.DOTALL).findall(html)
	for m in block:
		match = re.compile('href="(.+?)">(.+?)</a>').findall(str(m))
		for u,n in match:
			Menu(n,u,3,ICON,FANART,'','')
	
  

def Search():
	Search_url = 'https://gostream.is/movie/search/'
	Dialog = xbmcgui.Dialog()
	Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
	Search_name = Search_title.replace(' ','+').lower()
	url = Search_url+Search_name
	html = requests.get(url).content
	match = re.compile('div data-movie-id=.+?href="(.+?)".+?title="(.+?)".+?img.+?data-original="(.+?)"',re.DOTALL).findall(html)
	for url,name,image in match:
		url = url+'watching.html'
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

def resolve(url): 
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
elif mode == 1 : genre(url)
elif mode == 2 : Search()
elif mode == 3 : Get_Info(url)
elif mode == 4 : imdb()
elif mode == 5 : movie_check(url)
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
elif mode == 20: resolve(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))