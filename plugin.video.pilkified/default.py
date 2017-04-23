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
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
PATH = 'Pilk-ified'
VERSION = '0.0.1'
favourites = ADDON_DATA + 'favourites.txt'
if not os.path.exists(favourites):
    open(favourites,'w+')
favourites_read = open(favourites).read()
dp = xbmcgui.DialogProgress()
addon_handle = int(sys.argv[1])
List = []
addons = xbmc.translatePath('special://home/addons/')

ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
addon_id='plugin.video.pilkified'
current_folder = ADDONS+'/'+addon_id+'/'
full_file = current_folder.replace('\\','/') + '/final.txt'

def TextBoxes(heading,announce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(announce); text=f.read()
      except: text=announce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()
  TextBox()

if not os.path.exists(full_file):
    Open = open(full_file,'w+')
    TextBoxes('Final Version','The time has come to call it a day. I\'ve been studying lots of other stuff outside of Kodi and unfortunately am at a point where i feel i have too many commitments so Kodi stuff being a hobby will have to be the one getting the chop. I\'ll not delete any addons as if they still work you may aswell enjoy them. All the code is open for anyone to use or addons to fork just do them justice and a little credit is never a bad thing. Don\'t forget to visit kodification.co.uk as the site will hopefully be getting a nice new look in the coming weeks. \n\nThe addon\'s will work as long as they work i cannot promise any time scale just enjoy them while they are there, but there will be no future updates to any addons. Its been a long and enjoyable learning curve and hope some have enjoyed my addons. All the best to everyone thats helped me along the way.\n\nOrigin')


import os, shutil, xbmcgui
def check_for_nobs():
	for root, dirs, file in os.walk(addons):
		for dir in dirs:
			if 'anonymous' in dir.lower():
				if ADDON.getSetting('Delete')=='true':
					delete_stuff(dir)
				else:
					Dialog.ok('Something has to go','A addon has been found that is leeching content','your next choice is up to you','if you cancel '+addon_id+' will be removed')
					choices = ['Remove '+dir,'Remove '+addon_id,'Remove both']
					choice = xbmcgui.Dialog().select('What is going to be removed?', choices)
					if choice==0:
						delete_stuff(dir)
					elif choice==1:
						delete_stuff(addon_id)
					elif choice==2:
						delete_stuff(dir)
						delete_stuff(addon_id)
					else:
						delete_stuff(addon_id)
						
def delete_stuff(dir):
	path = addons + dir
	shutil.rmtree(path) 



def Main_Menu():
    check_for_nobs()
    Menu('XFM','',1,ICON,FANART,'')
    Menu('The Ricky Gervais Show','https://www.youtube.com/watch?v=vH2-sXTmzWI&list=PLj-sGZK2R0VkUZo6KdX761v1OLqE2_qRx',10,'http://i3.ytimg.com/vi/pe0g7lIRikw/mqdefault.jpg','https://i.ytimg.com/vi/Cbx4BjNbjGU/maxresdefault.jpg','')
    Menu('An Idiot Abroad','',2,ICON,FANART,'')
    Menu('Moaning of Life','',3,ICON,FANART,'')

def XFM():
    Menu('Series 1','https://www.youtube.com/watch?v=INfVabuCCSY&list=PLyXWmr6hs7HBvJO63tHC8Lyt1KOp2pm8b',10,'https://i.ytimg.com/vi/i5LhurDx4vA/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=gRB3UoiHW9hnepc91VM4nccrrfk',FANART,'')
    Menu('Series 2','https://www.youtube.com/watch?v=kmoMyEYU4zc&list=PLyXWmr6hs7HA-ZREpeUTSxcm76_XVrfiH',10,'https://i.ytimg.com/vi/3Mn_NUhm_0Y/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=b03kMkmsctq-ov16Bp8HrgFuSqc',FANART,'')
    Menu('Series 3','https://www.youtube.com/watch?v=eXgGZ4MzTkU&list=PLyXWmr6hs7HB4o17q-6Tbo-eJvlkRek_S',10,'https://i.ytimg.com/vi/WHGbOkjfSPI/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=sV4QQGZ2Xpv9e_L700pQ7pV4EAw',FANART,'')
    Menu('Series 4','https://www.youtube.com/watch?v=1s_efTYLGp4&list=PLyXWmr6hs7HC_-CluC_IB17TyWR21Xfk3',10,'https://i.ytimg.com/vi/2av9oRIy5XY/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=9KmtwAJTDdbLOpt4QETGSQKy8gQ',FANART,'')
    Menu('Rarities, Specials and Compilations','https://www.youtube.com/watch?v=4g-Ydn9PoUU&list=PLyXWmr6hs7HD6KcRbcMfvMJayHKPwhEy2',10,'https://i.ytimg.com/vi/aV2xtE-CSUE/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=PyOqq1Gnypgw-7aKJjl1r4qHSFI',FANART,'')

def Idiot_Abroad():
    Menu('Series 1','',7,ICON,'https://s-media-cache-ak0.pinimg.com/736x/0a/87/ae/0a87ae843cd573f998a17f49ab747895.jpg','')	
    Menu('Series 2','',8,ICON,'https://s3.amazonaws.com/promotionalcodes.ae/bucketlist/the-bucketlist-karl-pilkington.jpg','')	
    Menu('Series 3','',9,ICON,'https://i.ytimg.com/vi/WasM71_mYb8/maxresdefault.jpg','')

def Idiot_1(fanart):
    Play('Episode 1 - China','http://daclips.in/q0zu6vps78jp',20,ICON,fanart,'')
    Play('Episode 2 - Trans Siberian Express','http://vidzi.tv/h9pdkak07j8b.html',20,ICON,fanart,'')
    Play('Episode 3 - Jordan','http://vidzi.tv/rul398iz65j3.html',20,ICON,fanart,'')
    Play('Episode 4 - Mexico','http://vidzi.tv/1sk2yk7inzbs.html',20,ICON,fanart,'')
    Play('Episode 5 - Egypt','http://vidzi.tv/e1rfx0voy8i3.html',20,ICON,fanart,'')
    Play('Episode 6 - Brazil','http://vidzi.tv/9ibj61s4plf0.html',20,ICON,fanart,'')
    Play('Episode 7 - Peru','http://vidzi.tv/3o3g6bsaltoe.html',20,ICON,fanart,'')
    Play('Episode 8 - Karl Comes Home','http://vidzi.tv/cwwog3r3hg7d.html',20,ICON,fanart,'')

def Idiot_2(fanart):
    Play('Episode 1 - Desert Island','http://vidzi.tv/qprbodke58wo.html',20,ICON,fanart,'')
    Play('Episode 2 - Trans Siberian Railway','http://vidzi.tv/s9ukc1b9d0pr.html',20,ICON,fanart,'')
    Play('Episode 3 - Dolphin Swim','http://vidzi.tv/1uo9linmn8rs.html',20,ICON,fanart,'')
    Play('Episode 4 - Whale Watching','http://vidzi.tv/t9zsgbv1pbeu.html',20,ICON,fanart,'')
    Play('Episode 5 - Meet a Gorilla','http://vidzi.tv/q93qeclvdm5e.html',20,ICON,fanart,'')
    Play('Episode 6 - Route 66','http://vidzi.tv/177g7qkzca2y.html',20,ICON,fanart,'')
    Play('Episode 7 - Climb Mount Fuji','http://vidzi.tv/nzyqie977tn1.html',20,ICON,fanart,'')
    Play('Episode 8 - Karl Comes Home','http://vidzi.tv/ypi00ep9jkct.html',20,ICON,fanart,'')

def Idiot_3(fanart):
    Play('Episode 1 - Venice & Macedonia','https://www.youtube.com/watch?v=KwW5xIn0X50',20,ICON,fanart,'')
    Play('Episode 2 - India','https://www.youtube.com/watch?v=xRglMfnG4_g',20,ICON,fanart,'')
    Play('Episode 3 - China','https://www.youtube.com/watch?v=MB4-kZneZhQ',20,ICON,fanart,'')

	
def Moaning():
    Menu('Series 1','',11,ICON,'https://i.ytimg.com/vi/m76xkW1rQQQ/maxresdefault.jpg','')	
    Menu('Series 2','',12,ICON,'https://i.ytimg.com/vi/l-0PHVtrm1w/maxresdefault.jpg','')	

def Moaning_1(fanart):
    Play('Episode 1 - Marraige','http://vidzi.tv/cix7u0ojy48h.html',20,ICON,fanart,'')
    Play('Episode 2 - Happiness','http://vidzi.tv/r64okh84zldm.html',20,ICON,fanart,'')
    Play('Episode 3 - Children','http://vidzi.tv/l5qsqrzkbybb.html',20,ICON,fanart,'')
    Play('Episode 4 - Jobs','http://vidzi.tv/tlv81s7bq50e.html',20,ICON,fanart,'')
    Play('Episode 5 - Death','http://vidzi.tv/tuzon6qwf87p.html',20,ICON,fanart,'')

def Moaning_2(fanart):
    Play('Episode 1 - Art','http://vidzi.tv/nkjojrorunkr.html',20,ICON,fanart,'')
    Play('Episode 2 - Identity','http://vidzi.tv/53cl2rdvn2n5.html',20,ICON,fanart,'')
    Play('Episode 3 - How to live your life','http://vidzi.tv/53cl2rdvn2n5.html',20,ICON,fanart,'')
    Play('Episode 4 - The Body','http://vidzi.tv/hg5so6wwu34t.html',20,ICON,fanart,'')
    Play('Episode 5 - Waste','http://vidzi.tv/47hlxpgxzgu1.html',20,ICON,fanart,'')
    Play('Episode 6 - Time','http://daclips.in/h9iksp7sjkti',20,ICON,fanart,'')
	
def Youtube_Playlist_Scrape(url,iconimage,fanart):
    HTML = Open_Url(url)
    first = re.compile('<title>(.+?)</title>.+?href="https://www.youtube.com/watch?v=(.+?)&amp;').findall(HTML)
    for name,url in first:
        url = 'https://www.youtube.com/watch?v='+url
        name = (name).replace(' - YouTube','')
        Play(name,url,20,iconimage,fanart,'')
    match = re.compile('data-video-id="(.+?)" data.+?data-video-title="(.+?)"',re.DOTALL).findall(HTML)
    for url,name in match:
        url = 'https://www.youtube.com/watch?v='+url
        name = name.replace('&#39;','\'')
        if 'rivate' in name:
            pass
        elif 'eleted' in name:
            pass
        else:
			Play(name,url,20,iconimage,fanart,'')


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
elif mode == 7 : Idiot_1(fanart)
elif mode == 8 : Idiot_2(fanart)
elif mode == 9 : Idiot_3(fanart)
elif mode == 10: Youtube_Playlist_Scrape(url,iconimage,fanart)
elif mode == 11: Moaning_1(fanart)
elif mode == 12: Moaning_2(fanart)
elif mode == 20: resolve(name,url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))