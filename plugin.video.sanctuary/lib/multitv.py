# -*- coding: utf-8 -*-

import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, time, process
from threading import Thread

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
addon_handle = int(sys.argv[1])
Main = 'http://www.watchseriesgo.to/'
List = []
IMDB = 'http://www.imdb.com'
genre_list = ['Drama','Horror','Adventure','Fantasy','Sci-Fi','Thriller','Comedy','Romance','Mystery','Action','Family','Music','Crime','Animation']
Sources = ['daclips','filehoot','allmyvideos','vidspot','vodlocker']		



def multiv_Main_Menu():
    process.Menu('Latest Episodes',Main + 'latest',301,ICON,FANART,'','')
    process.Menu('Popular Episodes',Main + 'new',302,ICON,FANART,'','')
    process.Menu('Genres',Main + '',303,ICON,FANART,'','')
    process.Menu('Tv Schedule',Main + 'tvschedule',307,ICON,FANART,'','')
    process.Menu('Search','',309,ICON,FANART,'','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

def Search():
    Dialog = xbmcgui.Dialog()
    image = ICON
    description = ''
    fanart = FANART
    Search_name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_url = Main + 'search/' + (Search_name).replace(' ','%20')
    if Search_name == '':
        pass
    else:
        OPEN = process.OPEN_URL(Search_url)
        match = re.compile('<div class="block-left-home-inside col-sm-9 col-xs-12" title=".+?">.+?<a href="(.+?)" title=.+?<img src="(.+?)" alt=.+?<b>(.+?)</b></a><br>(.+?)<br>',re.DOTALL).findall(OPEN)
        for url,img,name,desc in match:
            name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
            url = Main + url
            image = Main + img
            description = (desc).replace('<b>','').replace('</b>','').replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"').replace('Description: ','').replace('  ','')
            process.Menu(name,url,305,image,fanart,description,name)		
            process.setView('Movies', 'INFO')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
	
def Tv_Schedule(url):
    OPEN = process.OPEN_URL(url)
    match = re.compile('<li><a href="/tvschedule/(.+?)".*?>(.+?)</a></li>').findall(OPEN)
    for url,date in match:
        date = (date).replace('&amp;','&').replace('&#039','\'')
        url = Main + '/tvschedule/' + url
        if date in List:
            pass
        elif 'TV Schedule' in date:
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
            process.Menu(date,url,308,ICON,FANART,'','')
            List.append(date)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
			
def Schedule_Grab(url):
    OPEN = process.OPEN_URL(url)
    match = re.compile('<li style="float.+?<a href="(.+?)" title="(.+?)" class="title-series"><b style="font-size:14px;">.+?</b>(.+?)</a>.+?<img src="(.+?)".+?<br>.+?<b>(.+?)</b>.+?<br>.+?<br>(.+?)</div>',re.DOTALL).findall(OPEN)
    for url,name,year,img,season,desc in match:
        url = Main + url
        image = Main + img
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"').replace('(2014)','')
        process.Menu(name + ' ' + year + ' - [COLORred]'+season+'[/COLOR]',url,305,img,FANART,'',name)
    if len(match) <= 0:
        process.Menu('No Data Available Unfortunately','','','','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
		
def Genres():
    OPEN = process.OPEN_URL(Main)
    match = re.compile('<li><a href="/genres/(.+?)" class="sr-header">(.+?)</a></li>').findall(OPEN)
    for url,name in match:
        url = Main +'/genres/'+ url
        process.Menu(name,url,304,ICON,FANART,'','')			
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

def Genres_Page(url):
    OPEN = process.OPEN_URL(url)
    match = re.compile('<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">(.+?)</span></a></li>').findall(OPEN)
    for url,name,year in match:
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
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
            process.Menu(name+' - [COLORred]'+year+'[/COLOR]',url,305,ICON,FANART,'',name)
    Next_Page = re.compile('<ul class="pagination">.+?<li><a href=".+?" style="font-weight: bold; color:#000;">.+?</a></li>.+?<li><a href="(.+?)">.+?</a></li>',re.DOTALL).findall(OPEN)
    for url in Next_Page:
        if 'Next_Page' in List:
            pass
        else:
            url = Main+url
            process.Menu('NEXT PAGE',url,304,ICON,FANART,'','')
            List.append('Next_Page')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
			
def Popular(url):
    OPEN = process.OPEN_URL(url)
    match = re.compile('<div class="block-left-home-inside-image">.+?<img src="(.+?)".+?<a href="(.+?)".+?<b>(.+?)</b>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>',re.DOTALL).findall(OPEN)
    for img,url,name,season,desc in match:
        url = Main + url
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        process.Menu(name+' - '+season,url,310,img,FANART,desc,name)		
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

		
def Grab_Season(url,extra):
    image = ' '
    description = ' '
    fanart = ' '
    season = ' '
    OPEN = process.OPEN_URL(url)
    image = re.compile('<img src="(.+?)">').findall(OPEN)
    for image in image:
        image = image	
    background = re.compile('style="background-image: url\((.+?)\)">').findall(OPEN)
    for fanart in background:
        fanart = fanart	
    match = re.compile('itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>',re.DOTALL).findall(OPEN)
    for url,season in match:
        season = 'S'+(season).replace('  ','').replace('\n','').replace('    ','').replace('	','')
        url = Main + url
        process.Menu((season).replace('  ',''),url,306,image,fanart,description,'')
        process.setView('Movies', 'INFO')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
	
def Grab_Episode(url,name,fanart,extra,iconimage):
    main_name = extra 
    season = name
    OPEN = process.OPEN_URL(url)
    image = iconimage
    match = re.compile('<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>',re.DOTALL).findall(OPEN)
    for url,name,date in match:
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        url = Main+url
        date = date
        full_name = name+' - [COLORred]'+date+'[/COLOR]'
        process.Menu(full_name,url,310,image,fanart,'Aired : '+date,full_name)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

	
def Latest_Eps(url):
    OPEN = process.OPEN_URL(url)
    match = re.compile('<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">(.+?)</span></a></li>').findall(OPEN)
    for url,name,date in match:
        url = Main + url
        name = (name).replace('Seas.','Season').replace('Ep.','Episode').replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        process.Menu(name+' - [COLORred]'+date+'[/COLOR]',url,310,ICON,FANART,'','')
    	process.setView('Movies', 'INFO')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
		


#####################################GET PLAYLINKS...WILL TRY SPEED UP WHEN I WORK OUT THREADING################################		

def Get_Sources(name,URL,iconimage,fanart):
    HTML = process.OPEN_URL(URL)
    match = re.compile('<td>.+?<a href="/link/(.+?)".+?title="(.+?)"',re.DOTALL).findall(HTML)
    for url,name in match:
        for item in Sources:
            if item in url:
                URL = Main + 'link/' + url
                List.append(name)
                selector(name,URL)
    if len(match)<=0:
        process.Menu('[COLORred]NO STREAMS AVAILABLE[/COLOR]','','','','','','')

def selector(name, URL):
    qty_check = List.count(name)
    if str(qty_check)>1:
        name = name + ' - Link '+ str(qty_check)
        process.Play(name,URL,313,ICON,FANART,'','')
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
    else:
        process.Play(name,URL,313,ICON,FANART,'','')

'''def Get_Sources(name,URL,iconimage,fanart):
    HTML = process.OPEN_URL(URL)
    match = re.compile('<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n',re.DOTALL).findall(HTML)
    for url,name in match:
        for item in Sources:
            if item in url:
                URL = Main + 'link/' + url
                process.Play(name,URL,313,ICON,FANART,'','')
    if len(match)<=0:
        process.Menu('[COLORred]NO STREAMS AVAILABLE[/COLOR]','','','','','','')'''
		
		
def Get_site_link(url,name):
    season_name = name
    HTML = process.OPEN_URL(url)
    match = re.compile('<iframe style=.+?" src="(.+?)"').findall(HTML)
    match2 = re.compile('<IFRAME SRC="(.+?)"').findall(HTML)
    match3 = re.compile('<IFRAME style=".+?" SRC="(.+?)"').findall(HTML)
    for url in match:
        main(url,season_name)
    for url in match2:
        main(url,season_name)
    for url in match3:
        main(url,season_name)

def main(url,season_name):
    if 'daclips.in' in url:
        daclips(url,season_name)
    elif 'filehoot.com' in url:
        filehoot(url,season_name)
    elif 'allmyvideos.net' in url:
        allmyvid(url,season_name)
    elif 'vidspot.net' in url:
        vidspot(url,season_name)
    elif 'vodlocker' in url:
        vodlocker(url,season_name)	
    elif 'vidto' in url:
        vidto(url,season_name)	


def vidto(url,season_name):
    HTML = process.OPEN_URL(url)
    match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"',re.DOTALL).findall(HTML)
    for Link,name in match:
        Printer(Link,season_name)

												
def allmyvid(url,season_name):
    HTML = process.OPEN_URL(url)
    match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"',re.DOTALL).findall(HTML)
    for Link,name in match:
        Printer(Link,season_name)

def vidspot(url,season_name):
    HTML = process.OPEN_URL(url)
    match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"').findall(HTML)
    for Link,name in match:
        Printer(Link,season_name)

def vodlocker(url,season_name):
    HTML = process.OPEN_URL(url)
    match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
    for Link in match:
        Printer(Link,season_name)

def daclips(url,season_name):
    HTML = process.OPEN_URL(url)
    match = re.compile('{ file: "(.+?)", type:"video" }').findall(HTML)
    for Link in match:
        Printer(Link,season_name)

def filehoot(url,season_name):
    HTML = process.OPEN_URL(url)
    match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
    for Link in match:
        Printer(Link,season_name)

def Printer(Link,season_name):
    if 'http:/' in Link:
        process.resolve_playercore(Link)

####################################################################PROCESSES###################################################
	
	
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
try:        
        trailer=urllib.unquote_plus(params["trailer"])
except:
        pass

#####################################################END PROCESSES##############################################################		
		
