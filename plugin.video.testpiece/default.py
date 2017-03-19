# -*- coding: utf-8 -*-

'''
    Template Add-on
    Copyright (C) 2016 Demo

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, time
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.TomBraiderMovies/')
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/MultiTV/'
if not os.path.exists(ADDON_DATA):
    os.makedirs(ADDON_DATA)
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
Dialog = xbmcgui.Dialog()
addon_id = 'plugin.video.TomBraiderMovies'
ADDON = xbmcaddon.Addon(id=addon_id)
PATH = 'Test Piece'
VERSION = '0.0.1'
watched = ADDON_DATA + 'watched.txt'
if not os.path.exists(watched):
    open(watched,'w+')
favourites = ADDON_DATA + 'favourites.txt'
watched_read = open(watched).read()
if not os.path.exists(favourites):
    open(favourites,'w+')
favourites_read = open(favourites).read()
dp = xbmcgui.DialogProgress()
addon_handle = int(sys.argv[1])
List = []
watched_list = []
temp_file = ADDON_PATH + 'Temp.txt'
Base_Url = 'http://tombraiderbuilds.co.uk/addon/'
ART = 'http://tombraiderbuilds.co.uk/Icons/'


def Main_Menu():
    Menu('[COLORgold]TOMB RAIDER FAVOURITES[/COLOR]','',1,ICON,FANART,desc)
    Menu('[COLORgold]TOMB RAIDER SEARCH[/COLOR]','',1,ICON ,FANART,desc)
    Menu('[COLORred]CONTENT ADDED DAILY. REPORT DEAD[/COLOR]','',1,ICON,FANART,desc)
    Menu('[COLORred]LINKS AND REQUEST MOVIES @[/COLOR]','',1,ICON,FANART,desc)
    Menu('[COLORred]FACEBOOK.COM/GROUPS/TOMBRAIDERMOVIES[/COLOR]','',1,ICON,FANART,desc)
    Menu('[COLORblue]BOXSETS[/COLOR]',Base_Url + 'boxsets/boxsets.txt',1,ART + 'boxsets.jpg',FANART,desc)
    Menu('[COLORblue]3D[/COLOR]',Base_Url + '3d/3d.txt',1,ART + '3dmovies.jpg',FANART,desc)
    Menu('[COLORblue]NEW RELEASES[/COLOR]',Base_Url + 'New%20Releaes/newreleases.txt',1,ART + 'newreleases.jpg',FANART,desc)
    Menu('[COLORblue]POPULAR[/COLOR]',Base_Url + 'popular/popular.txt',1,ART + 'popular.jpg',FANART,desc)
    Menu('[COLORblue]REQUESTS[/COLOR]',Base_Url + 'Your%20Requessts/requests.txt',1,ART + 'requests.jpg',FANART,desc)
    Menu('[COLORblue]ACTION/ADVENTURE[/COLOR]',Base_Url + 'action/action.txt',1,ART + 'actionadventure.jpg',FANART,desc)
    Menu('[COLORblue]CLASSICS[/COLOR]',Base_Url + 'classic/classic.txt',1,ART + 'classic.jpg',FANART,desc)
    Menu('[COLORblue]COMEDY[/COLOR]',Base_Url + 'comedy/comedy.txt',1,ART + 'comedy.jpg',FANART,desc)
    Menu('[COLORblue]DRAMA/THRILLER[/COLOR]',Base_Url + 'thriller/thriller.txt',1,ART + 'dramathriller.jpg',FANART,desc)
    Menu('[COLORblue]FAMILY[/COLOR]',Base_Url + 'family/family.txt',1,ART + 'family.jpg',FANART,desc)
    Menu('[COLORblue]HORROR[/COLOR]',Base_Url + 'Horror/horror.txt',1,ART + 'horror.jpg',FANART,desc)
    Menu('[COLORblue]KIDS[/COLOR]',Base_Url + 'Kids%20Movies/kidsmovies.txt',1,ART + 'kids.jpg',FANART,desc)
    Menu('[COLORblue]SCI-FI[/COLOR]',Base_Url + 'scifi/scifi.txt',1,ART + 'scifi.jpg',FANART,desc)

    setView('tvshows', 'Media Info 3')			
	
def Second_Menu(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>.+?</fanart>.+?</item>').findall(OPEN)
    for name,link,img in match:
        Play(name,link,7,img,FANART,'','')

    setView('tvshows', 'Media Info 3')			
def Search():
    Dialog = xbmcgui.Dialog()
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = Search_Name.lower
    search_list = ['http://tombraiderbuilds.co.uk/addon/boxsets/boxsets.txt','http://tombraiderbuilds.co.uk/addon/3d/3d.txt','http://tombraiderbuilds.co.uk/addon/New%20Releaes/newreleases.txt','http://tombraiderbuilds.co.uk/addon/popular/popular.txt','http://tombraiderbuilds.co.uk/addon/Your%20Requests/requests.txt','http://tombraiderbuilds.co.uk/addon/action/action.txt','http://tombraiderbuilds.co.uk/addon/classic/classic.txt','http://tombraiderbuilds.co.uk/addon/comedy/comedy.txt','http://tombraiderbuilds.co.uk/addon/thriller/thriller.txt','http://tombraiderbuilds.co.uk/addon/family/family.txt','http://tombraiderbuilds.co.uk/addon/Horror/horror.txt','http://tombraiderbuilds.co.uk/addon/Kids%20Movies/kidsmovies.txt','http://tombraiderbuilds.co.uk/addon/scifi/scifi.txt']
    for item in search_list:
        HTML = OPEN_Search(item)
        Play('','','','','','','')
        match = re.compile('<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>.+?</fanart>.+?</item>').findall(HTML)
        for name,link,img in match:
            if Search_Clean_Name in name:
                Play(name,link,7,img,FANART,'','')
				
		setView('tvshows', 'Media Info 3')
####################################################################PROCESSES###################################################
def Open_Url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = ''
    link = ''
    try: 
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    except: pass
    if link != '':
        return link
    else:
        link = 'Opened'
        return link

def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)
		
		
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
                contextMenu.append(('Remove from TombRaider Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in favourites_read:
                contextMenu.append(('Add to TombRaider Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
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
                contextMenu.append(('Remove from TombRaider Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in favourites_read:
                contextMenu.append(('Add to TombRaider Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
		
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
		

def resolve(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
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
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
#####################################################END PROCESSES##############################################################		
		
if mode == None: Main_Menu()
elif mode == 1 : Second_Menu(url)
elif mode == 2 : resolve(url)
elif mode == 3 : Search()

		
xbmcplugin.endOfDirectory(int(sys.argv[1]))
