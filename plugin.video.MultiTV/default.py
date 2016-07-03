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
import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon
from threading import Thread
Main = 'http://www.watchseries.li'
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.MultiTV/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
Dialog = xbmcgui.Dialog()
addon_id = 'plugin.video.MultiTV'
ADDON = xbmcaddon.Addon(id=addon_id)
PATH = 'Test Piece'
VERSION = '0.0.1'
favourites = ADDON_PATH + 'favourites.txt'
favourites_read = open(favourites).read()
dp = xbmcgui.DialogProgress()
addon_handle = int(sys.argv[1])
List = []


def Main_Menu():
    OPEN = Open_Url(Main)
    Menu('Latest Episodes','http://www.watchseries.li/latest',1,ICON,FANART,'')
    Menu('Popular Episodes','http://www.watchseries.li/new',2,ICON,FANART,'')
    Menu('Genres','http://www.watchseries.li/',3,ICON,FANART,'')
    Menu('Tv Schedule','http://www.watchseries.li/tvschedule',7,ICON,FANART,'')
    Menu('Search','',9,ICON,FANART,'')
    Menu('Favourites','',12,ICON,FANART,'')

def Search():
    Search_name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_url = 'http://www.watchseries.li/search/' + (Search_name).replace(' ','%20')
    OPEN = Open_Url(Search_url)
    block = re.compile('<div class="home-page">.+?<div class="block-left-home responsive-lg-full">(.+?)<div class="block-left-home responsive-lg-full">',re.DOTALL).findall(OPEN)
    match = re.compile('<div class="block-left-home-inside col-sm-6 col-xs-12" title=".+?<a href="(.+?)".+?<img src="(.+?)".+?<b>(.+?)</b></a><br>(.+?)<br>.+?div class="block-left-home-inside-line"></div>',re.DOTALL).findall(str(block))
    for url,img,name,desc in match:
        url = Main + url
        Menu(name,url,5,img,FANART,desc)		
	
def Tv_Schedule(url):
    OPEN = Open_Url(url)
    match = re.compile('<li><a href="(.+?)">(.+?)</a></li>',re.DOTALL).findall(OPEN)
    for url,date in match:
        url = Main + url
        if date in List:
            pass
        elif 'Home' in date:
            pass
        elif 'Series' in date:
            pass
        elif 'TV Show' in date:
            pass
        elif 'This Week' in date:
            pass
        elif 'Newest' in date:
            pass
        else:
            Menu(date,url,8,ICON,FANART,'')
            List.append(date)
			
def Schedule_Grab(url):
    OPEN = Open_Url(url)
    match = re.compile('<li style="float.+?<a href="(.+?)" title="(.+?)" class="title-series"><b style="font-size:14px;">.+?</b>(.+?)</a>.+?<img src="(.+?)".+?<br>.+?<b>(.+?)</b>.+?<br>.+?<br>(.+?)</div>',re.DOTALL).findall(OPEN)
    for url,name,year,img,season,desc in match:
        url = Main + url
        image = Main + img
        Menu(name + ' ' + year + ' - [COLORred]'+season+'[/COLOR]',url,10,img,FANART,desc)
		
def Genres():
    OPEN = Open_Url(Main)
    block = re.compile('<li><a href="/genres/drama">TV Show Genres</a>(.+?)</li>',re.DOTALL).findall(OPEN)
    match = re.compile('<a href="(.+?)" class="sr-header">(.+?)</a>').findall(str(block))
    for url,name in match:
        url = Main + url
        Menu(name,url,4,ICON,FANART,'')			

def Genres_Page(url):
    OPEN = Open_Url(url)
    Next_Page = re.compile('<ul class="pagination">.+?<li><a href=".+?" style="font-weight: bold; color:#000;">.+?</a></li>.+?<li><a href="(.+?)">.+?</a></li>',re.DOTALL).findall(OPEN)
    for url in Next_Page:
        if 'Next_Page' in List:
            pass
        else:
            url = Main+url
            Menu('NEXT PAGE',url,4,ICON,FANART,'')
            List.append('Next_Page')
    match = re.compile('<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">(.+?)</span></a></li>').findall(OPEN)
    for url,name,year in match:
        name = (name).replace('&#039;','\'').replace('&quot;','"')
        url = Main + url
        if 'hack/' in name:
            pass
        elif '.hack' in name:
            pass
        elif '.Hack' in name:
            pass
        elif '\'t' in name:
            pass
        else:
            Menu(name+' - [COLORred]'+year+'[/COLOR]',url,5,ICON,FANART,'')

def Popular(url):
    OPEN = Open_Url(url)
    match = re.compile('<div class="block-left-home-inside-image">.+?<img src="(.+?)".+?<a href="(.+?)".+?<b>(.+?)</b>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>',re.DOTALL).findall(OPEN)
    for img,url,name,season,desc in match:
        url = Main + url
        Menu(name+' - '+season,url,10,img,FANART,desc)		
  
def Grab_Prog(url):
    OPEN = Open_Url(url)
    match = re.compile('<div class="home-page">.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b></a><br>(.+?)<br>',re.DOTALL).findall(OPEN)
    for img,url,name,desc in match:
        url = Main + url
        Menu(name,url,2,img,FANART,desc)
		
def Grab_Season(url):
    OPEN = Open_Url(url)
    match = re.compile('<h2 class="lists"><a href="(.+?)" itemprop="url"><span itemprop="name">(.+?)</span></a></h2>').findall(OPEN)
    for url,season in match:
        url = Main + url
        Menu(season,url,6,ICON,FANART,'')
		
def Grab_Episode(url):
    OPEN = Open_Url(url)
    image = re.compile('<img src="(.+?)" alt').findall(OPEN)
    for image in image:
        image = image
    match = re.compile('<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>',re.DOTALL).findall(OPEN)
    for url,name,date in match:
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        url = Main+url
        date = date
        Menu(name+' - [COLORred]'+date+'[/COLOR]',url,10,image,FANART,'Aired : '+date)
	
def Latest_Eps(url):
    OPEN = Open_Url(url)
    match = re.compile('<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">(.+?)</span></a></li>').findall(OPEN)
    for url,name,date in match:
        url = Main + url
        name = (name).replace('Seas.','Season').replace('Ep.','Episode')
        Menu(name+' - [COLORred]'+date+'[/COLOR]',url,10,ICON,FANART,'')
		
def Write_Favourite(name,url,mode):
    print_text_file = open(favourites,"a")
    print_text_file.write('url="'+str(url)+'">name="'+str(name)+'"'+'>mode="'+str(mode)+'"<END>\n')
    print_text_file.close

def Read_Favourite(name,url,mode):
    Fav = open(favourites).read()
    Fav_Regex = re.compile('url="(.+?)">name="(.+?)">mode="(.+?)"<END>').findall(Fav)
    for url,name,mode in Fav_Regex:
        if not mode == '20':
            Menu(name,url,mode,ICON,FANART,'','','')
        elif mode == '20':
            Play(name,url,mode,ICON,FANART,'','','')
    else:
        Menu('[COLORred]If empty you need to add Favourites![/COLOR]','','','','','','','')
        Menu('By bringing up context menu then adding to favourites','','','','','','','')
        Menu('[COLORblue]Press C/Menu/Right click to bring up context menu[/COLOR]','','','','','','','')

#####################################GET PLAYLINKS...WILL TRY SPEED UP WHEN I WORK OUT THREADING################################		
class Watchseries():

        List = []
        source_list = []   
        Sources = ['daclips','filehoot','thevideo','allmyvideos','vidspot','vodlocker']		
        def __init__(self,name,url):

            season_name = name
            self.Get_Sources(url,season_name)
			

        def Get_Sources(self,URL,season_name):
            dp = xbmcgui.DialogProgress()
            HTML = Open_Url(URL)
            match = re.compile('<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n',re.DOTALL).findall(HTML)
            for url,name in match:
                URL = 'http://www.watchseries.li/link/' + url
                self.Get_site_link(URL,season_name)
            if len(match)<=0:
                Menu('[COLORred]NO STREAMS AVAILABLE[/COLOR]','','','','','')

				
        def Get_site_link(self,url,season_name):
            HTML = Open_Url(url)
            match = re.compile('<iframe style=.+?" src="(.+?)"').findall(HTML)
            match2 = re.compile('<IFRAME SRC="(.+?)"').findall(HTML)
            match3 = re.compile('<IFRAME style=".+?" SRC="(.+?)"').findall(HTML)
            for url in match:
                for item in self.Sources:
                    if item in url:
                        if item not in List:
                            s1=Thread(target=self.main,args=(url,season_name))
                            s1.start()
                            List.append(item)
                        else:
                            pass
                    else:
                        pass
            for url in match2:
                for item in self.Sources:
                    if item in url:
                        if item not in List:
                            s2=Thread(target=self.main,args=(url,season_name))
                            s2.start()
                            List.append(item)
                        else:
                            pass
                    else:
                        pass
            for url in match3:
                for item in self.Sources:
                    if item in url:
                        if item not in List:
                            s3=Thread(target=self.main,args=(url,season_name))
                            s3.start()
                            List.append(item)
                        else:
                            pass
                    else:
                        pass

        def main(self,url,season_name):
                dp.create("[COLORwhite]Origin[/COLOR]","Getting Sources",'','Please Wait')
                if 'daclips.in' in url:
                    source_name = 'DACLIPS'
                    if source_name in Watchseries.source_list:
					    pass
                    else:
                        t1 = Thread(target=self.daclips,args=(url,season_name,source_name))
                        dp.update(0,"", "Getting Daclips Links")
                        t1.start()
                else:
                    if 'filehoot.com' in url:
                        source_name = 'FILEHOOT'
                        if source_name in Watchseries.source_list:
					        pass
                        else:         
                            dp.update(0,"", "Getting Filehoot Links")
                            t2 = Thread(target=self.filehoot,args=(url,season_name,source_name))
                            t2.start()
                    else:
                        if 'thevideo.me' in url:
                            source_name = 'THEVIDEO'
                            if source_name in Watchseries.source_list:
					            pass					        
                            else:                           
                                t3=Thread(target=self.thevideo,args=(url,season_name,source_name))
                                dp.update(0,"", "Getting Thevideo Links")
                                t3.start()								
                        else:
                            if 'allmyvideos.net' in url:
                                source_name = 'ALLMYVIDEOS'
                                if source_name in Watchseries.source_list:
                                    pass                    
                                else:						
                                    t4=Thread(target=self.allmyvid,args=(url,season_name,source_name))
                                    dp.update(0,"", "Getting Allmyvideo Links")
                                    t4.start()
                            else:
                                if 'vidspot.net' in url:
                                    source_name = 'VIDSPOT'
                                    if source_name in Watchseries.source_list:
					                    pass                            
                                    else:
                                        t5=Thread(target=self.vidspot,args=(url,season_name,source_name))
                                        dp.update(0,"", "Getting Vidspot Links")
                                        t5.start()
                                else:
                                    if 'vodlocker' in url:
                                        source_name = 'VODLOCKER'
                                        if source_name in Watchseries.source_list:
					                        pass                                
                                        else:
                                            t6=Thread(target=self.vodlocker,args=(url,season_name,source_name))
                                            dp.update(0,"", "Getting Vodlocker Links")
                                            t6.start()	
                        
                   
        def allmyvid(self,url,season_name,source_name):
            HTML = Open_Url(url)
            match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"',re.DOTALL).findall(HTML)
            for Link,name in match:
                    self.Printer(Link,season_name,source_name)

        def vidspot(self,url,season_name,source_name):
            HTML = Open_Url(url)
            match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"').findall(HTML)
            for Link,name in match:
                    self.Printer(Link,season_name,source_name)

        def thevideo(self,url,season_name,source_name):
            HTML = Open_Url(url)
            match = re.compile("{ label: '.+?', file: '(.+?)' }").findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)

        def vodlocker(self,url,season_name,source_name):
            HTML = Open_Url(url)
            match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)

        def daclips(self,url,season_name,source_name):
            HTML = Open_Url(url)
            match = re.compile('{ file: "(.+?)", type:"video" }').findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)

        def filehoot(self,url,season_name,source_name):
            HTML = Open_Url(url)
            match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)

        def Printer(self,Link,season_name,source_name):

                if Link in Watchseries.List:
                    pass
                elif source_name in Watchseries.source_list:
				    pass
                else:
                    Play(source_name,Link,20,ICON,FANART,'')
                    dp.update(100,"", "Got Source")
                    Watchseries.List.append(Link)                    
                    Watchseries.source_list.append(source_name)
					
		    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

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
elif mode == 1 : Latest_Eps(url)
elif mode == 2 : Popular(url)
elif mode == 3 : Genres()
elif mode == 4 : Genres_Page(url)
elif mode == 5 : Grab_Season(url)
elif mode == 6 : Grab_Episode(url)
elif mode == 7 : Tv_Schedule(url)
elif mode == 8 : Schedule_Grab(url)
elif mode == 9 : Search()
elif mode == 10: Watchseries(name,url)
elif mode == 11: Write_Favourite(name,url,fav_mode)
elif mode == 12: Read_Favourite(name,url,fav_mode)
elif mode == 20: resolve(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
