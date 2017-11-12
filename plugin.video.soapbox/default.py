# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.REPLACE_THIS_NAME/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.REPLACE_THIS_NAME/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
    FAV = open(favourites).read()
else:
    FAV = []

def Main_Menu():
	Menu('Coronation Street','http://uktvcatchup.com/coronation-street/',1,'https://pbs.twimg.com/profile_images/741748431622942720/5aq6_qHm_400x400.jpg','http://mace.world/media/1278/coronation-st-hero.jpg?quality=90','','')
	Menu('Eastenders','http://uktvcatchup.com/eastenders/',1,'https://a.wattpad.com/useravatar/EastEndersTales.256.330400.jpg','https://www.google.co.uk/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjg7I2hiOzWAhUQZ1AKHbCXAXYQjRwIBw&url=http%3A%2F%2Feastenders.wikia.com%2Fwiki%2FFile%3ATitle_Card_Current.jpg&psig=AOvVaw1996pWvx0NzuLy413r_6B9&ust=1507931372296116','','')
	Menu('Emmerdale','http://uktvcatchup.com/emmerdale/',1,'https://pictures.abebooks.com/TIEINS/md/md1067958050.jpg','https://i.ytimg.com/vi/cad8cHPvaSk/maxresdefault.jpg','','')
	Menu('Holby City','http://uktvcatchup.com/holby-city/',1,'https://a.wattpad.com/useravatar/marymoo2912.256.484227.jpg','http://www.gasta.org/wordpress/wp-content/uploads/2015/12/HolbyCity_Titles_900932.jpg','','')
	Menu('Hollyoaks','http://uktvcatchup.com/hollyoaks/',1,'https://pbs.twimg.com/media/BDNxB11CQAAAV9B.jpg','http://cdn.playbuzz.com/cdn/c1f38097-238d-4c83-856c-b0f65dd285a6/50036998-7f50-41ce-a8ed-fb3d0910e934.png','','')
	Menu('Home and Away','http://uktvcatchup.com/home-and-away/',1,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1EpdfPHMG8wwDYiu3px18vu8nXXlCYK2LyL4r8L7obyDE91bq6Q','https://i.ytimg.com/vi/gaF9hC27r5c/maxresdefault.jpg','','')
	Menu('Neighbours','http://uktvcatchup.com/neighbours/',1,'http://www.friendly.travel/wp-content/uploads/2017/10/18430-4efe1b52-3948-40de-a31c-518aca0f0486-thumbnail.jpg','http://www.ricforster.com/wp-content/uploads/NEIGHBS.jpg','','')

def Episode_Grab(url,fanart):
	html = requests.get(url).content
	match = re.findall('<div class="content-annina"><div class="entry-featuredImg"><a href="(.+?)">.+?data-lazy-src="(.+?)".+?rel="bookmark">(.+?)</a>',html)
	for url2, img, name in match:
		name = name.replace('&#8211;','-')
		Play(name,url2,2,img,fanart,'','')

def playlinks(name,url):
	html = requests.get(url).content
	xbmc.log('GETTING PLAYLINKS: '+url,xbmc.LOGNOTICE)	
	match = re.compile('<iframe.+?data-lazy-src="(.+?)"').findall(html)
	for source in match:
		xbmc.log(source,xbmc.LOGNOTICE)
		if 'dailymotion' in source:
			source = 'http:'+source
			resolve(name,source)

		
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
                contextMenu.append(('Remove from REPLACE_THIS_NAME Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to REPLACE_THIS_NAME Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
                contextMenu.append(('Remove from REPLACE_THIS_NAME Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to REPLACE_THIS_NAME Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=14)' % sys.argv[0]))
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
		
		
# ===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------


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
elif mode == 1 : Episode_Grab(url,fanart)
elif mode == 2 : playlinks(name,url)

elif mode == 14 : queueItem()	
elif mode == 20: resolve(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))