# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from bs4 import BeautifulSoup as bs
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.f1fullraces/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.f1fullraces/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
   FAV = open(favourites).read()
else:
   FAV = []

def Main_Menu():
   Menu('Latest','http://f1fullraces.com/',1,ICON,FANART,'','')
   Menu('Years','',3,ICON,FANART,'','')
   Menu('Search','',2,ICON,FANART,'','')

def Search():
   Search_url = 'https://f1fullraces.com/?s='
   Dialog = xbmcgui.Dialog()
   Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
   Search_name = Search_title.replace(' ','+').lower()
   url = Search_url+Search_name
   get_info(url)
   
def years():
    Menu('2017','https://f1fullraces.com/category/full-races/2017/',1,ICON,FANART,'','')
    Menu('2016','https://f1fullraces.com/category/full-races/2016/',1,ICON,FANART,'','')
    Menu('2015','https://f1fullraces.com/category/full-races/2015/',1,ICON,FANART,'','')
    Menu('2014','https://f1fullraces.com/category/full-races/2014/',1,ICON,FANART,'','')
    Menu('2013','https://f1fullraces.com/category/full-races/2013/',1,ICON,FANART,'','')
    Menu('2012','https://f1fullraces.com/category/full-races/2012/',1,ICON,FANART,'','')
    Menu('2011','https://f1fullraces.com/category/full-races/2011/',1,ICON,FANART,'','')
    Menu('2010','https://f1fullraces.com/category/full-races/2010/',1,ICON,FANART,'','')
    Menu('2009','https://f1fullraces.com/category/full-races/2009/',1,ICON,FANART,'','')
    Menu('2008','https://f1fullraces.com/category/full-races/2008/',1,ICON,FANART,'','')
    Menu('2007','https://f1fullraces.com/category/full-races/2007/',1,ICON,FANART,'','')
    Menu('2006','https://f1fullraces.com/category/full-races/2006/',1,ICON,FANART,'','')
    Menu('2005','https://f1fullraces.com/category/full-races/2005/',1,ICON,FANART,'','')
    Menu('2004','https://f1fullraces.com/category/full-races/2004/',1,ICON,FANART,'','')
    Menu('2003','https://f1fullraces.com/category/full-races/2003/',1,ICON,FANART,'','')
    Menu('2002','https://f1fullraces.com/category/full-races/2002/',1,ICON,FANART,'','')
    Menu('2001','https://f1fullraces.com/category/full-races/2001/',1,ICON,FANART,'','')
    Menu('2000','https://f1fullraces.com/category/full-races/2000/',1,ICON,FANART,'','')
    Menu('1999','https://f1fullraces.com/category/full-races/1999/',1,ICON,FANART,'','')
    Menu('1998','https://f1fullraces.com/category/full-races/1998/',1,ICON,FANART,'','')
    Menu('1997','https://f1fullraces.com/category/full-races/1997/',1,ICON,FANART,'','')
    Menu('1996','https://f1fullraces.com/category/full-races/1996/',1,ICON,FANART,'','')
    Menu('1995','https://f1fullraces.com/category/full-races/1995/',1,ICON,FANART,'','')
    Menu('1994','https://f1fullraces.com/category/full-races/1994/',1,ICON,FANART,'','')
    Menu('1993','https://f1fullraces.com/category/full-races/1993/',1,ICON,FANART,'','')
    Menu('1992','https://f1fullraces.com/category/full-races/1992/',1,ICON,FANART,'','')
    Menu('1991','https://f1fullraces.com/category/full-races/1991/',1,ICON,FANART,'','')
    Menu('1990','https://f1fullraces.com/category/full-races/1990/',1,ICON,FANART,'','')
    Menu('1989','https://f1fullraces.com/category/full-races/1989/',1,ICON,FANART,'','')
    Menu('1988','https://f1fullraces.com/category/full-races/1988/',1,ICON,FANART,'','')
    Menu('1987','https://f1fullraces.com/category/full-races/1987/',1,ICON,FANART,'','')
    Menu('1986','https://f1fullraces.com/category/full-races/1986/',1,ICON,FANART,'','')
    Menu('1985','https://f1fullraces.com/category/full-races/1985/',1,ICON,FANART,'','')
    Menu('1984','https://f1fullraces.com/category/full-races/1984/',1,ICON,FANART,'','')
    Menu('1983','https://f1fullraces.com/category/full-races/1983/',1,ICON,FANART,'','')
    Menu('1982','https://f1fullraces.com/category/full-races/1982/',1,ICON,FANART,'','')
    Menu('1981','https://f1fullraces.com/category/full-races/1981/',1,ICON,FANART,'','')
    Menu('1980','https://f1fullraces.com/category/full-races/1980/',1,ICON,FANART,'','')

   
def get_info(url):
	html = requests.get(url).content
	m = re.compile('<div class="content-list-thumb">.+?href="(.+?)" title="(.+?)">.+?<img.+?src="(.+?)"',re.DOTALL).findall(html)
	for u,n,i in m:
		n = n.replace('&#8211;','-')
		Menu(n,u,4,i,FANART,'','')
	next = re.findall('<a class="next page-numbers" href="(.+?)"',html)[0]
	if next:
		Menu('Next Page',next,1,ICON,FANART,'','')
		
def get_link(url,img):
	List = []
	html = requests.get(url).content
	p = re.compile('<p>(.+?)</p>',re.DOTALL).findall(html)
	for i in p:
		try:
			name = re.findall('(.+?)<br />',str(i))[0]
			name = name.replace('<em>','').replace('</em>','').replace('<strong>','').replace('</strong>','')
		except:
			name = 'PLAY'
		try:
			u = re.findall('iframe src="(.+?)"',str(i))[0]
		except:
			try:
				u = re.findall('href="(.+?)"',str(i))[0]
			except:
				pass
		if 'drive' in u:
			h = requests.get(u).content
			m = re.compile('"(.+?)"').findall(h)
			for z in m:
				if 'googleuser' in z:
					playlink = z
					if playlink not in List:
						Play(name,playlink,20,img,FANART,'','')
						List.append(playlink)
		elif 'streamango' in u:
			t = requests.get(u).content
			l = re.compile('"video/mp4",src:"(.+?)",height:(.+?),').findall(t)
			for s,q in l:
				playlink = 'http:'+s
				qual = q
				if playlink not in List:
					Play(name.replace('(720p)','')+' ('+qual+'p)',playlink,20,img,FANART,'','')
					List.append(playlink)
		elif 'openload' in u:
			playlink = u
			if playlink not in List:
				Play(name,playlink,20,img,FANART,'','')
				List.append(playlink)

	
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
            contextMenu.append(('Remove from f1fullraces Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to f1fullraces Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
            contextMenu.append(('Remove from f1fullraces Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to f1fullraces Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
      favList.append(('f1fullraces Favourites Section', '', '', '', '', '', ''))
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
elif mode == 3 : years()
elif mode == 4 : get_link(url,iconimage)

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