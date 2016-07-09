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
import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, yt
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.pilkified/')
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/Pilkified/'
if not os.path.exists(ADDON_DATA):
    os.makedirs(ADDON_DATA)
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
Dialog = xbmcgui.Dialog()
addon_id = 'plugin.video.pilkified'
ADDON = xbmcaddon.Addon(id=addon_id)
PATH = 'Test Piece'
VERSION = '0.0.1'
favourites = ADDON_DATA + 'favourites.txt'
if not os.path.exists(favourites):
    open(favourites,'w+')
favourites_read = open(favourites).read()
dp = xbmcgui.DialogProgress()
addon_handle = int(sys.argv[1])
List = []


def Main_Menu():
    Menu('XFM','',1,ICON,FANART,'')
    Menu('The Ricky Gervais Show','https://www.youtube.com/watch?v=vH2-sXTmzWI&list=PLj-sGZK2R0VkUZo6KdX761v1OLqE2_qRx',10,'http://i3.ytimg.com/vi/pe0g7lIRikw/mqdefault.jpg','https://i.ytimg.com/vi/Cbx4BjNbjGU/maxresdefault.jpg','')
    Menu('An Idiot Abroad','',2,ICON,FANART,'')
    Menu('Moaning of Life','',3,ICON,FANART,'')
    Menu('Derek','',4,ICON,FANART,'')
    Menu('[COLORred]For any missing check out Multi Tv or Youtube addons[/COLOR]','',4,ICON,FANART,'')

def XFM():
    Menu('Series 1','https://www.youtube.com/watch?v=W35J565_F-A&list=PLMtVekbZxaUdCmwIAso_acdu2TK0wk9kk',10,'https://i.ytimg.com/vi/i5LhurDx4vA/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=gRB3UoiHW9hnepc91VM4nccrrfk',FANART,'')
    Menu('Series 2','https://www.youtube.com/watch?v=3Mn_NUhm_0Y&list=PLsloMxqwTl71ORbE9wRPeO8l-qi_wsSUB',10,'https://i.ytimg.com/vi/3Mn_NUhm_0Y/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=b03kMkmsctq-ov16Bp8HrgFuSqc',FANART,'')
    Menu('Series 3','https://www.youtube.com/watch?v=WHGbOkjfSPI&list=PLsloMxqwTl721XHA6i6iAdQ6MO_h8Gmhm',10,'https://i.ytimg.com/vi/WHGbOkjfSPI/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=sV4QQGZ2Xpv9e_L700pQ7pV4EAw',FANART,'')
    Menu('Series 4','https://www.youtube.com/watch?v=2av9oRIy5XY&list=PLMtVekbZxaUdOEqH2oJpCnL-Kb8iJLkoS',10,'https://i.ytimg.com/vi/2av9oRIy5XY/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=9KmtwAJTDdbLOpt4QETGSQKy8gQ',FANART,'')
    Menu('Rarities, Specials and Compilations','https://www.youtube.com/watch?v=aV2xtE-CSUE&list=PLyXWmr6hs7HD6KcRbcMfvMJayHKPwhEy2',10,'https://i.ytimg.com/vi/aV2xtE-CSUE/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=PyOqq1Gnypgw-7aKJjl1r4qHSFI',FANART,'')

def Idiot_Abroad():
    Menu('Series 1','',7,ICON,'https://s-media-cache-ak0.pinimg.com/736x/0a/87/ae/0a87ae843cd573f998a17f49ab747895.jpg','')	
    Menu('Series 2','',8,ICON,'https://s3.amazonaws.com/promotionalcodes.ae/bucketlist/the-bucketlist-karl-pilkington.jpg','')	
    Menu('Series 3','',9,ICON,'https://i.ytimg.com/vi/WasM71_mYb8/maxresdefault.jpg','')

def Idiot_1(fanart):
    Play('Episode 1 - China','7BDPp3ac4Vs',21,ICON,fanart,'')
    Play('Episode 2 - Trans Siberian Express','2M2Q_mD-MIA',21,ICON,fanart,'')
    Play('Episode 3 - Jordan','tq4luhR69GY',21,ICON,fanart,'')
    Play('Episode 4 - Mexico','zB_TGCjTReg',21,ICON,fanart,'')
    Play('Episode 5 - Egypt','LrXk7uKQpQk',21,ICON,fanart,'')
    Play('Episode 6 - Brazil','KZV5szppnzo',21,ICON,fanart,'')
    Play('Episode 7 - Peru','gx9y18g7kHc',21,ICON,fanart,'')
    Play('Episode 8 - Karl Comes Home','KfRI5H-I1f4',21,ICON,fanart,'')

def Idiot_2(fanart):
    Play('Episode 1 - Desert Island','vheVf8uSBx8',21,ICON,fanart,'')
    Play('Episode 2 - Trans Siberian Railway','Uiyr5hD6RrI',21,ICON,fanart,'')
    Play('Episode 3 - Dolphin Swim','SfL7HiLdxrg',21,ICON,fanart,'')
    Play('Episode 4 - Whale Watching','1V4WQBstADc',21,ICON,fanart,'')
    Play('Episode 5 - Meet a Gorilla','SafYGSdOWw4',21,ICON,fanart,'')
    Play('Episode 6 - Route 66','L-LM_z7a_yg',21,ICON,fanart,'')
    Play('Episode 7 - Climb Mount Fuji','mo3KGcJpIY8',21,ICON,fanart,'')
    Play('Episode 8 - Karl Comes Home','O6TFza5Oq9s',21,ICON,fanart,'')

def Idiot_3(fanart):
    Play('Episode 1 - Venice & Macedonia','J3gmQglwcog',21,ICON,fanart,'')
    Play('Episode 2 - India','TGoyBsb8QLk',21,ICON,fanart,'')
    Play('Episode 3 - China','XlU9mpHsXk8',21,ICON,fanart,'')

	
def Moaning():
    Menu('Series 1','https://www.youtube.com/watch?v=nrDtEJc8JnU&list=PLfRZV8vTKBCZfm4hD83C7RvWQw9dJ9nAH',11,ICON,'https://i.ytimg.com/vi/m76xkW1rQQQ/maxresdefault.jpg','')	
    Menu('Series 2','https://www.youtube.com/watch?v=k0JSMAh75eA&list=PLoCm2w312egNE_ANZca_YI785XnMrjIHI',12,ICON,'https://i.ytimg.com/vi/l-0PHVtrm1w/maxresdefault.jpg','')	

def Moaning_1(fanart):
    Menu('[COLORred]Check Multi Tv addon for these[/COLOR]','','',ICON,fanart,'')

def Moaning_2(fanart):
    Play('Episode 1','http://31.14.252.94:8777/zwcepyl3ok4pcnokakashmg347ugipgt3tvnppwwscwlmmwyhykcgx7qu4/v.mp4',21,ICON,fanart,'')
    Play('Episode 2 - Identity','G72MTe0obvQ',21,ICON,fanart,'')
    Play('Episode 3 - How to live your life','4KzTUGR4sbs',21,ICON,fanart,'')
    Play('Episode 4 - The Body','86ZsozlcyM0',21,ICON,fanart,'')
    Play('Episode 5','nrDtEJc8JnU',21,ICON,fanart,'')
    Play('Episode 6 - Time','k0JSMAh75eA',20,ICON,fanart,'')


	
def Derek():
    Menu('Series 1','',5,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')	
    Menu('Series 2','',6,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')

def Derek_1():
    Play('Episode 1','dEcqklfwSkU',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 2','sv9_GA1tDLE',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 3','tAF199cG-uA',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 4','8KNmZT53rWw',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 5','V5sVwkicDhE',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 6','5VFdsZGPpLc',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
	
def Derek_2():
    Play('Episode 1','SQj-pLEaU1k',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 2','Lz9Fol3GA9w',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 3','BLiloh-nNsM',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 4','9n_9JoRCx9s',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 5','dEcqklfwSkU',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
    Play('Episode 6','dEcqklfwSkU',21,ICON,'http://p3.no/filmpolitiet/wp-content/thumbs/?src=http://p3.no/filmpolitiet/wp-content/uploads/2013/09/Derek-bilde-2.jpg&w=1150','')
	
def Youtube_Playlist_Scrape(url,iconimage,fanart):
    HTML = Open_Url(url)
    first = re.compile('<title>(.+?)</title>.+?href="https://www.youtube.com/watch?v=(.+?)&amp;').findall(HTML)
    for name,url in first:
        name = (name).replace(' - YouTube','')
        Play(name,url,21,iconimage,fanart,'')
    match = re.compile('data-video-id="(.+?)" data.+?data-video-title="(.+?)"',re.DOTALL).findall(HTML)
    for url,name in match:
        if 'rivate' in name:
            pass
        else:
			Play(name,url,21,iconimage,fanart,'')


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
		
		
def Menu(name,url,mode,iconimage,fanart,description,showcontext=True,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if not name in favourites_read:
                contextMenu.append(('Add to MultiTV Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        

		
def Play(name,url,mode,iconimage,fanart,description,showcontext=True,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if not name in favourites_read:
                contextMenu.append(('Add to Multi TV Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode)))
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
trailer=None
fav_mode=None
choice=None

try:
    choice=int(params["choice"])
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
try:        
        trailer=urllib.unquote_plus(params["trailer"])
except:
        pass

        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
print "Trailer: "+str(trailer)

#####################################################END PROCESSES##############################################################		
		
if mode == None: Main_Menu()
elif mode == 1 : XFM()
elif mode == 2 : Idiot_Abroad()
elif mode == 3 : Moaning()
elif mode == 4 : Derek()
elif mode == 5 : Derek_1()
elif mode == 6 : Derek_2()
elif mode == 7 : Idiot_1(fanart)
elif mode == 8 : Idiot_2(fanart)
elif mode == 9 : Idiot_3(fanart)
elif mode == 10: Youtube_Playlist_Scrape(url,iconimage,fanart)
elif mode == 11: Moaning_1(fanart)
elif mode == 12: Moaning_2(fanart)
elif mode == 20: resolve(url)
elif mode == 21: yt.PlayVideo(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
