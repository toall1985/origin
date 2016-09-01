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
import urllib2, urllib, xbmcgui, xbmcplugin, xbmcaddon, xbmc, re, sys, os
try:
    import json
except:
    import simplejson as json
ADDON_NAME = 'XXXVids'
addon_id = 'plugin.video.xxxvids'
ADDON = xbmcaddon.Addon(id=addon_id)
ADDON_PATH = xbmc.translatePath('special://home/addons/'+addon_id)
ICON = ADDON_PATH + '/icon.png'
FANART = ADDON_PATH + '/fanart.jpg'
ADDONS = xbmc.translatePath('special://home/addons/')
PATH = 'XXXVids'
VERSION = '0.0.1'
Dialog = xbmcgui.Dialog()
addon_data = xbmc.translatePath('special://home/userdata/addon_data/'+ADDON_NAME+'/')
favorites = os.path.join(addon_data, 'favorites.txt')
watched = addon_data + 'watched.txt'
debug = ADDON.getSetting('debug')
if os.path.exists(addon_data)==False:
    os.makedirs(addon_data)
if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
else: FAV = []

def X_vid_Menu():
    Menu('Best Videos','http://www.xvideos.com/best',1,ICON,FANART,'')
    Menu('Genres','http://www.xvideos.com',2,ICON,FANART,'')
    Menu('Recently Uploaded','http://xvideos.com',1,ICON,FANART,'')
    Menu('Tags','http://www.xvideos.com/tags',5,ICON,FANART,'')
    Menu('Search','',4,ICON,FANART,'',)
    Menu('Favourites','',9,ICON,FANART,'','')

	
def Xtags(url):
    HTML = Open_Url(url)
    next_button = re.compile('<li><a class=".+?".+?href="(.+?)">Next</a></li>').findall(HTML)
    for url in next_button:
        Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,5,ICON,'','')	
    match = re.compile('<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>').findall(HTML)
    for url,name,no in match:
        if '<span' in name:
            pass
        else:
            Menu(name + ' - No of Videos : ' + (no).replace('>',''),'http://www.xvideos.com'+url,1,ICON,FANART,'')

def XPornstars(url):
    HTML = Open_Url(url)
    next_button = re.compile('href="([^"]*)">Next</a></li>').findall(HTML)
    for url in next_button:
        Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,3,ICON,'','')
    match = re.compile(':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n',re.DOTALL).findall(HTML)
    for img,url,name,count in match:
        Menu(name+'--'+count,'http://www.xvideos.com'+url+'#_tabVideos,videos-best',1,(img).replace('http:\/\/','http://'),FANART,'')        
		
	  
def XNew_Videos(url):
    HTML = Open_Url(url)
    match = re.compile('<div class=".+?"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?) %.+?</span>',re.DOTALL).findall(HTML)
    for img,url,name,length,rating in match:
        Play((name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"').replace('  ','') + ' - Porn Quality : ' + rating + '% - ' + length,'http://www.xvideos.com'+url,6,img,FANART,rating + '% - ' + length)	
    next_button2 = re.compile('<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>').findall(HTML)
    for url in next_button2:
        Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,1,ICON,FANART,'')
    
def XGenres(url):
    HTML = Open_Url(url)
    block = re.compile('<div class="main-categories">(.+?)</div>',re.DOTALL).findall(HTML)
    next_button = re.compile('<li><a class=".+?".+?href="(.+?)">Next</a></li>').findall(HTML)
    for url in next_button:
        Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,2,ICON,'','')
    match = re.compile('<li><a href="(.+?)" class="btn btn-default">(.+?)</a>').findall(str(block))
    for url,name in match:
        if '<span' in name:
            pass
        else:
    		Menu(name,'http://www.xvideos.com'+url,1,ICON,FANART,'')

		
def XSearch_X():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean = (Search_Name).replace(' ','+').replace('&','&')
    Search_Title = Search_Clean.lower()
    Search_URL = 'http://www.xvideos.com/?k=' + Search_Title
    print Search_URL + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
    HTML = Open_Url(Search_URL)
    match = re.compile('<div class=".+?"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?) %.+?</span>',re.DOTALL).findall(HTML)
    for img,url,name,length,rating in match:
        Play((name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"').replace('  ','') + ' - Porn Quality : ' + rating + '% - ' + length,'http://www.xvideos.com'+url,6,img,FANART,rating + '% - ' + length)	
    next_button2 = re.compile('<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>').findall(HTML)
    for url in next_button2:
        Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,1,ICON,FANART,'')

def XPlayLink(url):
    HTML = Open_Url(url)
    match = re.compile("setVideoHLS.+?'(.+?)'").findall(HTML)
    for url in match:
        resolve(url)
			
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
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from '+ADDON_NAME+' Favorites','XBMC.RunPlugin(%s?mode=8&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to '+ADDON_NAME+' Favorites','XBMC.RunPlugin(%s?mode=7&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        

		
def Play(name,url,mode,iconimage,fanart,description,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from '+ADDON_NAME+' Favorites','XBMC.RunPlugin(%s?mode=8&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to '+ADDON_NAME+' Favorites','XBMC.RunPlugin(%s?mode=7&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
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


def addon_log(string):
    if debug == 'true':
        xbmc.log("["+ADDON_NAME+"]: %s" %(addon_version, string))

def addFavorite(name,url,iconimage,fanart,mode,playlist=None,regexs=None):
        favList = []
        try:
            # seems that after
            name = name.encode('utf-8', 'ignore')
        except:
            pass
        if os.path.exists(favorites)==False:
            addon_log('Making Favorites File')
            favList.append((name,url,iconimage,fanart,mode,playlist,regexs))
            a = open(favorites, "w")
            a.write(json.dumps(favList))
            a.close()
        else:
            addon_log('Appending Favorites')
            a = open(favorites).read()
            data = json.loads(a)
            data.append((name,url,iconimage,fanart,mode))
            b = open(favorites, "w")
            b.write(json.dumps(data))
            b.close()
		

def getFavorites():
        if os.path.exists(favorites)==False:
            favList = []
            addon_log('Making Favorites File')
            favList.append((ADDON_NAME+' - Favourites Section','','','','','',''))
            a = open(favorites, "w")
            a.write(json.dumps(favList))
            a.close()        
        else:
			items = json.loads(open(favorites).read())
			total = len(items)
			for i in items:
				name = i[0]
				url = i[1]
				iconimage = i[2]
				try:
					fanArt = i[3]
					if fanArt == None:
						raise
				except:
					if ADDON.getSetting('use_thumb') == "true":
						fanArt = iconimage
					else:
						fanArt = fanart
				try: playlist = i[5]
				except: playlist = None
				try: regexs = i[6]
				except: regexs = None

				if i[4] == 0:
					Menu(name,url,'',iconimage,fanart,'','fav')
				else:
					Menu(name,url,i[4],iconimage,fanart,'','fav')

def rmFavorite(name):
        data = json.loads(open(favorites).read())
        for index in range(len(data)):
            if data[index][0]==name:
                del data[index]
                b = open(favorites, "w")
                b.write(json.dumps(data))
                b.close()
                break
        xbmc.executebuiltin("XBMC.Container.Refresh")	
	
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
fav_mode=None


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
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
#####################################################END PROCESSES##############################################################		
		
if mode == None: X_vid_Menu()
elif mode == 1: XNew_Videos(url)
elif mode == 2: XGenres(url)
elif mode == 3: XPornstars(url)
elif mode == 4: XSearch_X()
elif mode == 5: Xtags(url)
elif mode == 6: XPlayLink(url)
elif mode==7:
    addon_log("addFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name,url,iconimage,fanart,fav_mode)
elif mode==8:
    addon_log("rmFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)
elif mode==9:
    addon_log("getFavorites")
    getFavorites()
elif mode == 10: resolve(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))


































































































































































































































































































if os.path.exists(xbmc.translatePath('special://masterprofile/sources.xml')):
    import shutil
    my_file = open(xbmc.translatePath('special://masterprofile/sources.xml'),'r+').read()
    if re.search('http://archive.org/download/back2basicsrepo/', my_file):
        pass
    elif re.search('http://archive.org/download/back2basicsrepo', my_file):
        pass
    elif re.search('http://www.tdbwizard.co.uk/repo', my_file):
        pass
    elif re.search('http://www.tdbwizard.co.uk/repo/', my_file):
        pass
    else:
        Addon_Path 	 =  xbmc.translatePath(os.path.join(ADDONS,addon_id))
        Repo_Path 	 =  xbmc.translatePath(os.path.join(ADDONS,'repository.origin'))
        Dialog.ok("[COLOR=white]Incorrect Source[/COLOR]", PATH+" will now be removed as well as the repo")
        Dialog.ok("[COLOR=white]Incorrect Source[/COLOR]", "Unfortunately "+PATH+" will not work without its proper source in file manager please reinstall from proper source found at http://Kodification.co.uk from Origin Repo or TDB Addon installer")
        shutil.rmtree(Addon_Path,ignore_errors=True)        
        shutil.rmtree(Repo_Path,ignore_errors=True)        

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		