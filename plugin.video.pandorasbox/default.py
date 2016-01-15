'''
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

import sys
import urlparse
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver
import time
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
from datetime import datetime

Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
CAT=Decode('LnBocA==')
Base_Pand = (Decode('aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi8='))
addon_id='plugin.video.pandorasbox'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Pandoras Box"
VERSION = "1.0.1"
IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'

ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))



def Home_Menu():
    
    addDirPand2('Open Pandora\'s Box','',400,ART + 'icon.png',ART + 'fanart.jpg','')
    addDirPand2('Search','',1,ART + 'icon.png',ART + 'fanart.jpg','')

def Search_Menu():
	addDirPand2('Search Pandoras Films','',424,ART + 'icon.png',ART + 'fanart.jpg','')
	addDirPand2('Search Pandoras TV','',425,ART + 'icon.png',ART + 'fanart.jpg','')

	
def Pandoras_Box():

    html=OPEN_URL(Decode('aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA=='))
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
            addDirPand2(name,url,mode,img,fanart,desc)

def Pandora_Menu(url):
        
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,desc,background,name in match:
            addDirPand(name,url,401,iconimage,background,desc)

            xbmcplugin.setContent(addon_handle, 'movies')			
            xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def Search_Pandoras_Films():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    filenames = ['mova', 'movb', 'movc', 'movd', 'move', 'movf', 'movg', 'movh', 'movi', 'movj', 'movk', 'movl', 'movm', 'movn', 'movo', 'movp', 'movq', 'movr', 'movs', 'movt', 'movu', 'movv', 'movw', 'movx', 'movy', 'movz']

    for file_Name in filenames:
        search_URL = Base_Pand + file_Name + CAT
        HTML = OPEN_URL(search_URL)
        match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML)
        for url,iconimage,desc,fanart,name in match:
            if Search_Name in name.lower():
                addDirPand(name,url,401,iconimage,fanart,desc)
				
                xbmcplugin.setContent(addon_handle, 'movies')
                xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
				
				
def Search_Pandoras_TV():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    filenames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for file_Name in filenames:
        search_URL2 = Base_Pand + file_Name + CAT
        HTML = OPEN_URL(search_URL2)
        match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(HTML)
        for name,desc,url,img,fanart,mode in match:
            if Search_Name in name.lower():
                addDirPand2(name,url,mode,img,fanart,desc)
				
                xbmcplugin.setContent(addon_handle, 'movies')
                xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

			
def open_Menu(url):

    html=OPEN_URL(url)
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
            addDirPand2(name,url,mode,img,fanart,desc)

            xbmcplugin.setContent(addon_handle, 'movies')
            xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def addDirPand(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDirPand2(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
		
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
 

def Resolve(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('LOADING','Opening %s Now'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve() 
    if dp.iscanceled(): 
        print "[COLORred]STREAM CANCELLED[/COLOR]" # need to get this part working    
        dialog = xbmcgui.Dialog()
        if dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
	         return
    else:
        try: play.play(url)
        except: pass
        try: ADDON.resolve_url(url) 
        except: pass 
        dp.close()

def OPEN_URL(url):
        req = urllib2.Request(url)
        IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
        FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
        IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
        ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)


if mode == None     : Home_Menu()
elif mode == 1 		: Search_Menu()
elif mode == 400 	: Pandoras_Box()
elif mode == 401    : Resolve(url)
elif mode == 423 	: open_Menu(url)
elif mode == 424 	: Search_Pandoras_Films()
elif mode == 425 	: Search_Pandoras_TV()
elif mode == 426 	: Pandora_Menu(url)
elif mode == 427 	: addDirPand(name,url,mode,iconimage,fanart,description)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
