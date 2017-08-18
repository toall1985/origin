# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
from jsunpack import unpack
import base64

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.kingmovies/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.kingmovies/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
   FAV = open(favourites).read()
else:
   FAV = []

def Main_Menu():
   Menu('Movies','https://kingmovies.is/free-movies',1,ICON,FANART,'','')
   Menu('TV-Series','https://kingmovies.is/tv-series',1,ICON,FANART,'','')
   Menu('Top IMDb','https://kingmovies.is/top-imdb',1,ICON,FANART,'','')
   Menu('Cinema','https://kingmovies.is/cinema',1,ICON,FANART,'','')
   Menu('A-Z','',4,ICON,FANART,'','')
   Menu('Genre','',3,ICON,FANART,'','')
   Menu('Year','',5,ICON,FANART,'','')
   Menu('Search','',2,ICON,FANART,'','')

def genre():
   Menu('Comedy','https://kingmovies.is/genre/comedy',1,ICON,FANART,'','')
   Menu('Crime','https://kingmovies.is/genre/crime',1,ICON,FANART,'','')
   Menu('Action','https://kingmovies.is/genre/action',1,ICON,FANART,'','')
   Menu('Adventure','https://kingmovies.is/genre/adventure',1,ICON,FANART,'','')
   Menu('Animation','https://kingmovies.is/genre/animation',1,ICON,FANART,'','')
   Menu('Documentary','https://kingmovies.is/genre/documentary',1,ICON,FANART,'','')
   Menu('Family','https://kingmovies.is/genre/family',1,ICON,FANART,'','')
   Menu('Fantasy','https://kingmovies.is/genre/fantasy',1,ICON,FANART,'','')
   Menu('History','https://kingmovies.is/genre/history',1,ICON,FANART,'','')
   Menu('Horror','https://kingmovies.is/genre/horror',1,ICON,FANART,'','')
   Menu('Kids','https://kingmovies.is/genre/kids',1,ICON,FANART,'','')
   Menu('Music','https://kingmovies.is/genre/music',1,ICON,FANART,'','')
   Menu('Mystery','https://kingmovies.is/genre/mystery',1,ICON,FANART,'','')
   Menu('News','https://kingmovies.is/genre/news',1,ICON,FANART,'','')
   Menu('Romance','https://kingmovies.is/genre/romance',1,ICON,FANART,'','')
   Menu('Sport','https://kingmovies.is/genre/sport',1,ICON,FANART,'','')
   Menu('Thriller','https://kingmovies.is/genre/thriller',1,ICON,FANART,'','')
   Menu('War','https://kingmovies.is/genre/war',1,ICON,FANART,'','')
   Menu('Western','https://kingmovies.is/genre/western',1,ICON,FANART,'','')
   Menu('Sci-Fi','https://kingmovies.is/genre/scr-fi',1,ICON,FANART,'','')
   Menu('Drama','https://kingmovies.is/genre/drama',1,ICON,FANART,'','')
   Menu('Biography','https://kingmovies.is/genre/biography',1,ICON,FANART,'','')
   
def a_z():
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		Menu(letter.upper(),'https://kingmovies.is/az-list/'+letter,1,ICON,FANART,'','')
		
def year():
	year = ['2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','older']
	for y in year:
		Menu(y,'https://kingmovies.is/release-'+y,1,ICON,FANART,'','')
		
def Get_Info(url):
	html = requests.get(url).content
	match = re.compile('<li class="movie-item".+?data-title="(.+?)".+?href="(.+?)".+?img.+?src="(.+?)"').findall(html)
	for name,u,img in match:
		Menu(name,u,6,img,FANART,'','')
	Next = re.compile('<ul class="pagination"><li class="active">.+?href=".+?href="(.+?)"').findall(html)
	for n in Next:
		Menu('Next Page',n,1,ICON,FANART,'','')
		
def movie_check(url):
	url = url+'/watching.html'
	if '-season-' in url:
		tv_show(url)
	else:
		get_links(url)
		
def tv_show(url):
    List = []
    html2 = requests.get(url).content
    match2 = re.compile('<li class="ep-item">.+?<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(html2)
    for url3,name2 in match2:
        if name2 not in List:
            Menu(name2,url3,7,ICON,FANART,'','')
            List.append(name2)
		

	
def get_links(url):
	html2 = requests.get(url).text
	match2 = re.compile('<div id="content-embed">.+?src="(.+?)"',re.DOTALL).findall(html2)                                
	for link in match2:
		if not link.startswith('http:'):
			link = 'http:'+link
			get_source(link,url)
			
def get_source(url,u):
    List = []
    html3 = requests.get(url).content
    match3 = re.compile('JuicyCodes.Run\((.+?)\);',re.DOTALL).findall(html3)
    for i in match3:
        single = re.compile('"(.+?)"').findall(str(i))
        for s in single:
            List.append(s)
        html2 = base64.decodestring(str(List).replace('[','').replace(']','').replace('\'','').replace(',','').replace(' ',''))
        try:
            string= unpack(html2)
        except:
            pass
        ep_id = re.findall('"episodeID":"(.+?)"',string)[0]
        ep_name = re.findall('"episodeName":"(.+?)"',string)[0]
        ep_backup = re.findall('"episodeBackup":"(.+?)"',string)[0]
        ep_hot = re.findall('"episodeHOT":(.+?),',string)[0]
        File = re.findall('"file":"(.+?)"',string)[0]
        headers = {"origin":"https://embed.streamdor.co",
                   "referer":u,
                   "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
                   }
                
        data = {"episodeID":ep_id,
                "episodeName":ep_name,
                "episodeBackup":ep_backup,
                "episodeHOT":ep_hot,
                "file":File
                }
        try:
            xbmc.log('hi',xbmc.LOGNOTICE)
            response = requests.post('https://api.streamdor.co/sources',headers=headers,data=data).json()
            results = response["sources"]
            ur = 'http:'+results
            z = requests.get(ur).json()
            s = re.findall("'sources'.+?\[(.+?)\]",str(z))[0]
            single = re.compile('{(.+?)}').findall(s)
            for item in single:
                xbmc.log(item,xbmc.LOGNOTICE)
                playlink = re.findall("'file':.+?'(.+?)'",item)[0]
                quality = re.findall("'label':.+?'(.+?)'",item)[0]
                if '=m' in playlink:
                    source = 'Gvideo'
                else:
                    source = 'Streamdor'
                Play(source + ' ('+quality+')',playlink,20,ICON,FANART,'','')
        except:
            Play('No response from stream, please try again','',20,'','','','')
            Play('If it fails again it may be worth trying another addon','',20,'','','','')

			
def Search():
   Search_url = 'https://kingmovies.is/search?q='
   Dialog = xbmcgui.Dialog()
   Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
   Search_name = Search_title.replace(' ','+').lower()
   url = Search_url+Search_name
   Get_Info(url)
   
	
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
            contextMenu.append(('Remove from kingmovies Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to kingmovies Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
            contextMenu.append(('Remove from kingmovies Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to kingmovies Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
      favList.append(('kingmovies Favourites Section', '', '', '', '', '', ''))
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
elif mode == 1 : Get_Info(url)
elif mode == 2 : Search()
elif mode == 3 : genre()
elif mode == 4 : a_z()
elif mode == 5 : year()
elif mode == 6 : movie_check(url)
elif mode == 7 : get_links(url)
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