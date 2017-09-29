# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.gostreams/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.gostreams/'
favourites = ADDON_DATA + 'favourites'
base_link = 'https://cartoonhd.in'
if os.path.exists(favourites) == True:
   FAV = open(favourites).read()
else:
   FAV = []

def Main_Menu():
   Menu('TV-Series','https://cartoonhd.in/tv-shows',1,ICON,FANART,'','')
   Menu('Movies','https://cartoonhd.in/full-movies',1,ICON,FANART,'','')
   Menu('Cinema Movies','https://cartoonhd.in/box-office-movies',1,ICON,FANART,'','')
   Menu('Just Added','https://cartoonhd.in/new-movies',1,ICON,FANART,'','')
   Menu('Cinema Movies','https://cartoonhd.in/box-office-movies',1,ICON,FANART,'','')
   Menu('Search','',2,ICON,FANART,'','')
 
def Get_Info(url):
	List = []
	html = requests.get(url,verify=False).content
	block = re.compile('<section class="cardBox flip">(.+?)</section>',re.DOTALL).findall(html)
	for b in block:
		image = re.compile('img src="(.+?)"').findall(str(b))
		for i in image:
			if 'jpg' in i:
				image = i
		name = re.findall('alt="(.+?)"',str(b))[0]
		url = re.findall('href="(.+?)"',str(b))[0]
		trailer = re.findall('<div class="ribbon-wrapper"><div class="ribbon black">(.+?)</div></div>',str(b))
		for t in trailer:
			name = name + ' : '+t
		Menu(name,url,3,image,FANART,'','')
	Next = re.compile('<ul class="pagination">.+?<li class="active">.+?href.+?href="(.+?)"',re.DOTALL).findall(html)
	for u in Next:
		if u not in List:
			Menu('Next Page',u,1,ICON,FANART,'','')
			List.append(u)
		
def get_page_info(url,iconimage):
	count = 0
	html = requests.get(url).content
	try:
		fanart = re.findall('<div id="watch".+?url\(\'(.+?)\'',html)[0]
	except:
		fanart = FANART
	match = re.compile('<b>Season\(s\):</b>(.+?)</p>',re.DOTALL).findall(html)
	for block in match:
		match2 = re.compile('href="(.+?)".+?title="(.+?)"').findall(str(block))
		for url2, name in match2:
			Menu(name,url2,4,iconimage,fanart,'','')
			count+=1
	if count==0:
		get_playlink(url)
			
def get_season_info(url,fanart):
	html = requests.get(url).content
	m = re.compile('<div class="episode ">.+?href="(.+?)" title="(.+?)">.+?img="(.+?)"',re.DOTALL).findall(html)
	for url,name,image in m:
		Menu(name,url,5,image,fanart,'','')


def get_playlink(url):			
	ajax_url = 'https://cartoonhd.in/ajax/tnembedr.php'
	get_info = requests.get(url).content
	token = re.findall("var tok.+?= '(.+?)'",get_info)[0]
	elid = re.findall('elid = "(.+?)"',get_info)[0]
	actions = ['getMovieEmb','getEpisodeEmb']
	for action in actions:
	
		headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
			'Referer':url,
			'X-Requested-With':'XMLHttpRequest',
			}

		data = {
				'action':action,
				'idEl':elid,
				'token':token,
				}

		html = requests.post(ajax_url,headers=headers,data=data).json()
		for single in html:
			item = html[single]
			try:
				playlink = re.findall('src="(.+?)"',str(item['embed']))[0]
			except:
				playlink = re.findall('SRC="(.+?)"',str(item['embed']))[0]
			qual = item['type']
			if '360p' in qual:
				quality = '360p'
			elif '720p' in qual:
				quality = '720p'
			elif '1080p' in qual:
				quality = '1080p'
			else:
				quality = 'unknown quality'
			if 'openload' in playlink:
				quality = 'openload ('+quality+')'
			elif 'streamango' in playlink:
				quality = 'streamango ('+quality+')'
			elif 'blogspot' in playlink:
				quality = 'google video ('+quality+')'
			elif 'google' in playlink:
				quality = 'google video ('+quality+')'
			Play(quality,playlink,20,ICON,FANART,'','')

def Search():
	Search_url = 'https://api.cartoonhd.in/api/v1/0A6ru35yevokjaqbb3'
	Dialog = xbmcgui.Dialog()
	Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
	Search_name = Search_title.replace(' ','+').lower()
	url = 'https://api.cartoonhd.in/api/v1/0A6ru35yevokjaqbb3'
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
           }
	data = {'q':Search_name.replace(' ','+'),
			'sl':'evokjaqbb3'
			}
	html = requests.post(url,headers=headers,data=data).json()
	for single in html:
		url = base_link+single['permalink']
		image = base_link+single['image']
		if single['type']!='actor':
			try: 
				name = single['title']+' ('+str(single['year'])+')'
			except: 
				try:
					name = single['title']
				except:
					name = 'naming error'
			try:
				Menu(name,url,3,image,FANART,'','')
			except:
				pass
	
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
elif mode == 1 : Get_Info(url)
elif mode == 2 : Search()
elif mode == 3 : get_page_info(url,iconimage)
elif mode == 4 : get_season_info(url,fanart)
elif mode == 5 : get_playlink(url)
elif mode == 6 : genre(url)


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