# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
import yt
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.fullmatchesandshows/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.fullmatchesandshows/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
   FAV = open(favourites).read()
else:
   FAV = []

def Main_Menu():
	Menu('Highlights','http://www.fullmatchesandshows.com/category/highlights/',1,ICON,FANART,'','')
	Menu('Shows','http://www.fullmatchesandshows.com/category/show/',1,ICON,FANART,'','')
	Menu('Latest News','http://www.fullmatchesandshows.com/category/latest-news/',1,ICON,FANART,'','')
	Menu('Leagues','',3,ICON,FANART,'','')
	Menu('Search','',2,ICON,FANART,'','')
	
	
def Leagues():	
    Menu('Premier League','http://www.fullmatchesandshows.com/premier-league/',1,'https://footballseasons.files.wordpress.com/2013/05/premier-league.png',FANART,'','')
    Menu('La Liga','http://www.fullmatchesandshows.com/la-liga/',1,'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png',FANART,'','')
    Menu('Bundesliga','http://www.fullmatchesandshows.com/bundesliga/',1,'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg',FANART,'','')
    Menu('Champions League','http://www.fullmatchesandshows.com/champions-league/',1,'http://www.ecursuri.ro/images/teste/test-champions-league.jpg',FANART,'','')
    Menu('Serie A','http://www.fullmatchesandshows.com/category/serie-a/',1,'http://files.jcriccione.it/200000223-2484526782/serie%20a.png',FANART,'','')
    Menu('Ligue 1','http://www.fullmatchesandshows.com/category/ligue-1/',1,'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg',FANART,'','')
	
def Search():
    Dialog = xbmcgui.Dialog()
    Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search_title.replace(' ','%20').lower()
    url = 'http://www.fullmatchesandshows.com/?s='+Search_name.replace(' ','+')
    Get_info(url,ICON)
	
def Get_info(url,iconimage):
    HTML = requests.get(url).content
    match2 = re.compile('<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)"(.+?)</div>').findall(HTML)
    for url,name,rest in match2:
        image = re.compile('src="(.+?)"').findall(str(rest))
        for i in image:
            if '.jpg' in i:
                img = i
            elif '.png' in i:
                img = i
            else:
                img = ICON
        if 'Full Match' in name:
            Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            Menu(Name,url,4,img,'','','')
        else:
    	    Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            Menu(Name,url,4,img,'','','')
    Next = re.compile('<span class="current">.+?</span><a href="(.+?)" class="page" title=".+?">(.+?)</a>').findall(HTML)
    for url,name in Next:
        Menu('Next Page',url,1,iconimage,FANART,'','')
		
def get_Multi_Links(name,url,iconimage):
    try:
        List = []
        HTML = requests.get(url).content
        block = re.findall('<ul class="paging_btns" id="acp_paging_menu">(.+?)</ul>',HTML)[0]
        match2 = re.findall('<div class="acp_title">(.+?)</div>',HTML)
        match = re.compile('<li.+?href="(.+?)".+?<div class="acp_title">(.+?)</div>').findall(str(block))
        for url2,name in match:
            name = (name).replace('HL English','English Highlights')
            List.append(name)
            Menu(name,url2,5,iconimage,FANART,'','')
        for n in match2:
            name = (n).replace('HL English','English Highlights')
            if name not in List:
                Menu(name,url,5,iconimage,FANART,'','')
    except:
        get_PLAYlink(name,url)
		
		
def get_PLAYlink(name,url):
    Play('[COLORred]Allow up to 1 min for streams to play[/COLOR]','',20,'','','','')
    HTML = requests.get(url).content
    match_youtube = re.compile('<iframe.+?src="https://www.youtube.com/embed/(.+?)"').findall(HTML)
    for url in match_youtube:
        Play('Play - Youtube',url,6,ICON,FANART,'','')
    iframe = re.compile('<iframe(.+?)</iframe>').findall(HTML)
    for i in iframe:
		src = re.compile('src="(.+?)"').findall(str(i))
		for playlink in src:
			if 'div' in playlink:
				pass
			elif 'weshare' in playlink:
				if not 'mp4' in playlink:
					h = requests.get(playlink).content
					match = re.compile('source src="(.+?)"').findall(h)
					for p in match:
						Play('Play - Weshare',p,20,ICON,FANART,'','')
				else:
					Play('Play - Weshare',p,20,ICON,FANART,'','')
			elif 'rutube.ru' in playlink:
				playlink = 'https:'+playlink
				api = 'https://rutube.ru/api/play/options/'+playlink.replace('https://rutube.ru/play/embed/','')+'/?format=json&sqr4374_compat=1&no_404=true&referer='+playlink
				xbmc.log('api:'+api,xbmc.LOGNOTICE)
				headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
						   "Referer": playlink,
						   "Host":"rutube.ru"
						   }				
				html = requests.get(api,headers=headers).content
				m3u8 = re.compile('"m3u8": "(.+?)"').findall(str(html))
				for link in m3u8:
					xbmc.log('link:'+link,xbmc.LOGNOTICE)
					last = link+'&referer='+playlink
					h = requests.get(last).content
					m = re.compile('".+?"\n(.+?)\n',re.DOTALL).findall(h)
					for l in m:
						Play('Play - Rutube',l,20,ICON,FANART,'','')
			elif 'streamable' in playlink:
				html = requests.get(playlink).content
				m = re.compile('source src="(.+?)"').findall(html)
				for s in m:
					Play('Play - Streamable','http:'+s,20,ICON,FANART,'','')
			elif 'ooyala' in playlink:
				pass
				
			
#				Playlink = (playlink).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')


	
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
            contextMenu.append(('Remove from watchcartoononline Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to watchcartoononline Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
            contextMenu.append(('Remove from watchcartoononline Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                           %(sys.argv[0], urllib.quote_plus(name))))
         if not name in FAV:
            contextMenu.append(('Add to watchcartoononline Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
      favList.append(('watchcartoononline Favourites Section', '', '', '', '', '', ''))
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
elif mode == 1 : Get_info(url,iconimage)
elif mode == 2 : Search()
elif mode == 3 : Leagues()
elif mode == 4 : get_Multi_Links(name,url,iconimage)
elif mode == 5 : get_PLAYlink(name,url)
elif mode == 6 : yt.PlayVideo(url)
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