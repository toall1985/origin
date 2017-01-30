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
try:
    import json
except:
    import simplejson as json
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.indexscraper/')
source_file = ADDON_PATH + 'source_file.txt'
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
PATH = 'Index Scraper'
VERSION = '0.0.1'
Dialog = xbmcgui.Dialog()
addon_id = 'plugin.video.indexscraper'
ADDON = xbmcaddon.Addon(id=addon_id)
movie_favourites = ADDON_PATH + 'movie_favourites.txt'
tv_favourites = ADDON_PATH + 'tv_favourites.txt'
music_favourites = ADDON_PATH + 'music_favourites.txt'
movie_favourites_read = open(movie_favourites).read()
music_favourites_read = open(music_favourites).read()
tv_favourites_read = open(tv_favourites).read()
imdb = 'http://www.imdb.com'
List = []
import os, shutil, xbmcgui
Dialog = xbmcgui.Dialog()
addons = xbmc.translatePath('special://home/addons/')
ADDON = xbmcaddon.Addon(id=addon_id)
def check_for_nobs():
	for root, dirs, file in os.walk(addons):
		for dir in dirs:
			if 'anonymous' in dir.lower():
				if ADDON.getSetting('Delete')=='true':
					delete_stuff(dir)
				else:
					Dialog.ok('Something has to go','A addon has been found that is leeching content','your next choice is up to you','if you cancel sanctuary will be removed')
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
    Menu('Favourites','',5,ICON,FANART,'','','')
    Menu('List of Index\'s','',7,ICON,FANART,'','','')
#    Menu('Search','',6,ICON,FANART,'','','')
    Menu('[COLORred]Press here to add a source url[/COLOR]	','',2,'',ICON,FANART,'','')	

##################LIST OF INDEX'S########################

def Index_List():
    OPEN = open(source_file).read()
    Regex = re.compile('url="(.+?)">name="(.+?)"').findall(OPEN)
    for url,name in Regex:
        Menu(name,url,1,ICON,FANART,'','','')
    else:
        Menu('[COLORred]Press here to add a source url[/COLOR]	','',2,'',ICON,FANART,'','')	


#######################SEARCH########################
'''
def Search():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    OPEN = open(source_file).read()
    Regex = re.compile('url="(.+?)">name="(.+?)"').findall(OPEN)
    for url in Regex:
        Search_Loop('http://sv.dl-pars.in/')
    if Search_Name in name:
        Menu(name,url_search,1,ICON,FANART,'','')
    

def Search_Loop(url):
    HTML = Open_Url(url)
    match = re.compile('<a href="(.+?)">(.+?)</a>').findall(HTML)
    for url2,name in match:
        url3 = url + url2
        if '..' in url3:
            pass
        elif 'rar' in url3:
            pass
        elif 'srt' in url3:
            pass
        elif 'C=' in url2:
            pass
        elif '/' in url2:
            name = name
            url_search = url3
            Search_Loop(url)
        else:
            name = name
            url_search = url3
'''
#################################FAVOURITES#################################

def Write_Favourite(name,url,choice,mode):
    if choice == 1:
        favourite_file = movie_favourites
    elif choice == 2:
        favourite_file = tv_favourites
    elif choice == 3:
        favourite_file = music_favourites
    print_text_file = open(favourite_file,"a")
    print_text_file.write('url="'+str(url)+'">name="'+str(name)+'"'+'>mode="'+str(mode)+'"<END>\n')
    print_text_file.close

def Read_Favourite(name,url,choice,mode):
    if choice == 1:
        favourite_file = movie_favourites
    elif choice == 2:
        favourite_file = tv_favourites
    elif choice == 3:
        favourite_file = music_favourites
    Fav = open(favourite_file).read()
    Fav_Regex = re.compile('url="(.+?)">name="(.+?)">mode="(.+?)"<END>').findall(Fav)
    for url,name,mode in Fav_Regex:
        if mode == '1':
            Menu(name,url,mode,ICON,FANART,'','','')
        elif mode == '10':
            Play(name,url,mode,ICON,FANART,'','','')
    else:
        Menu('[COLORred]If empty you need to add Favourites![/COLOR]','','','','','','','')
        Menu('By bringing up context menu then adding to favourites','','','','','','','')
        Menu('[COLORblue]Press C/Menu/Right click to bring up context menu[/COLOR]','','','','','','','')
            
	
def Favourites_menu():
    Menu('Favourite Movies','',4,ICON,FANART,'','',1)
    Menu('Favourite Tv Shows','',4,ICON,FANART,'','',2)
    Menu('Favourite Music','',4,ICON,FANART,'','',3)

    		

#####################################MAIN REGEX LOOP ###############################
		
def Main_Loop(url):
    HTML = Open_Url(url)
    match = re.compile('<a href="(.+?)">(.+?)</a>').findall(HTML)
    for url2,name in match:
        url3 = url + url2
        if '..' in url3:
            pass
        elif 'rar' in url3:
            pass
        elif 'srt' in url3:
            pass
        elif 'jpg' in url3:
            pass
        elif 'metathumb' in url3:
            pass
        elif 'xml' in url3:
            pass
        elif 'nfo' in url3:
            pass
        elif 'C=' in url2:
            pass
        elif '/' in url2:
            Menu((name).replace('/',''),url3,1,ICON,FANART,'','','')
        else:
            Clean_name(name,url3)

################################### TIDY UP NAME #############################

def Clean_name(name,url3):
    name1 = (name).replace('S01E','S01 E').replace('(MovIran).mkv','').replace('The.Walking.Dead','').replace('.mkv','').replace('Tehmovies.com.mkv','').replace('Nightsdl','').replace('Ganool','')
    name2=(name1).replace('.',' ').replace(' (ParsFilm).mkv','').replace('_TehMovies.Com.mkv','').replace(' (SaberFun.IR).mkv','').replace('[UpFilm].mkv','').replace('(Bia2Movies)','')
    name3=(name2).replace('.mkv','').replace('.Film2Movie_INFO.mkv','').replace('.HEVC.Film2Movie_INFO.mkv','').replace('.ParsFilm.mkv ','').replace('(SaberFunIR)','')
    name4=(name3).replace('.INTERNAL.','').replace('.Film2Movie_INFO.mkv','').replace('.web-dl.Tehmovies.net.mkv','').replace('S01E06','S01 E06').replace('S01E07','S01 E07')
    name5=(name4).replace('S01E08','S01 E08').replace('S01E09','S01 E09').replace('S01E10','S01 E10').replace('.Tehmovies.net','').replace('.WEBRip.Tehmovies.com.mkv','')
    name6=(name5).replace('.mp4','').replace('.mkv','').replace('.Tehmovies.ir','').replace('x265HEVC','').replace('Film2Movie_INFO','').replace('Tehmovies.com.mkv','')
    name7=(name6).replace(' (ParsFilm)','').replace('Tehmovies.ir.mkv','').replace('.480p',' 480p').replace('.WEBrip','').replace('.web-dl','').replace('.WEB-DL','')
    name8=(name7).replace('.','').replace('.Tehmovies.com','').replace('480p.Tehmovies.net</',' 480p').replace('720p.Tehmovies.net','720p').replace('.480p',' 480p')
    name9=(name8).replace('.480p.WEB-DL',' 480p').replace('.mkv','').replace('.INTERNAL.','').replace('720p',' 720p').replace('.Tehmovi..&gt;','').replace('.Tehmovies.net.mkv','')
    name10=(name9).replace('..720p',' 720p').replace('.REPACK.Tehmovies..&gt;','').replace('.Tehmovies.com.mkv','').replace('.Tehmovies..&gt;','').replace('Tehmovies.ir..&gt;','')
    name11=(name10).replace('Tehmovies.ne..&gt;','').replace('.HDTV.x264-mRs','').replace('...&gt;','').replace('.Tehmovies...&gt;','').replace('.Tehmovies.com.mp4','')
    name12=(name11).replace('.Tehmovies.com.mp4','').replace('_MovieFarsi','').replace('_MovieFar','').replace('_com','').replace('&gt;','').replace('avi','').replace('(1)','')
    name13=(name12).replace('(2)','').replace('cd 2','').replace('cd 1','').replace('-dos-xvid','').replace('divx','').replace('Xvid','').replace('DVD','').replace('DVDrip','')
    name14=(name13).replace('DvDrip-aXXo','').replace('[','').replace(']','').replace('(','').replace(')','').replace('XviD-TLF-','').replace('CD1','').replace('CD2','')
    name15=(name14).replace('CD3','').replace('mp4','').replace('&amp;','&').replace('HDRip','').replace('-','').replace('  ',' ').replace('xvid','').replace('1080p','')
    name16=(name15).replace('1970','').replace('1971','').replace('1972','').replace('1973','').replace('1974','').replace('1975','').replace('1976','').replace('1977','')
    name17=(name16).replace('1978','').replace('1979','').replace('1980','').replace('1981','').replace('1982','').replace('1983','').replace('1984','').replace('1985','')
    name18=(name17).replace('1986','').replace('1987','').replace('1988','').replace('1989','').replace('1990','').replace('1991','').replace('1992','').replace('1993','')
    name19=(name18).replace('1994','').replace('1995','').replace('1996','').replace('1997','').replace('1998','').replace('1999','').replace('2000','').replace('2001','')
    name20=(name19).replace('2002','').replace('2003','').replace('2004','').replace('2005','').replace('2006','').replace('2007','').replace('2008','').replace('2009','')
    name21=(name20).replace('2010','').replace('2011','').replace('2012','').replace('2013','').replace('2014','').replace('2015','').replace('2016','').replace('720p','')
    name22=(name21).replace('360p','').replace('  ',' ').replace('BluRay','').replace('rip','').replace('WEBDL','').replace('s01','').replace('s02','').replace('S02','')
    name23=(name22).replace('s03','').replace('s04','').replace('s05','').replace('s06','').replace('s07','').replace('s08','').replace('s09','').replace('S01','')
    name24=(name23).replace('S03','').replace('S04',' ').replace('S05','').replace('S06','').replace('S07','').replace('S08','').replace('S09','').replace('E01','')
    name25=(name24).replace('E02','').replace('E03','').replace('E04','').replace('E05','').replace('E06','').replace('E07','').replace('E08','').replace('E09','').replace('e01','')
    name25=(name24).replace('e02','').replace('e03','').replace('e04','').replace('e05','').replace('e06','').replace('e07','').replace('e08','').replace('e09','').replace('e01','')
    clean_name = name15
    search_name = name25
    if ADDON.getSetting('Data')=='true':
        Imdb_Scrape(url3,clean_name,search_name)
    if ADDON.getSetting('Data')=='false':
        Play(clean_name,url3,10,ICON,FANART,'','','')

#######################IMDB GRAB#####################

def Imdb_Scrape(url3,clean_name,search_name):
    url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q=' + (search_name).replace(' ','+') + '&s=all'
    HTML = Open_Url(url)
    match = re.compile('<table class="findList">.+?<tr class="findResult odd">.+?<a href="(.+?)" >',re.DOTALL).findall(HTML)
    for url in match:
        if 'title' in url:
            Pass_It = 'Pass' + clean_name
            if not Pass_It in List:
                IMAGE = ''
                BACKGROUND=''
                DESCRIPTION=''
                final_url = imdb + url
                Final_Page = Open_Url(final_url)
                Image = re.compile('<div class="poster">.+?src="(.+?)"',re.DOTALL).findall(Final_Page)
                for image in Image:
                    IMAGE = image
                Description = re.compile('<div class="summary_text" itemprop="description">(.+?)</div>',re.DOTALL).findall(Final_Page)
                for desc in Description:
                    DESCRIPTION = (desc).replace('\n','').replace('  ','')
                Background = re.compile('<div class="mediastrip">.+?loadlate="(.+?)"',re.DOTALL).findall(Final_Page)
                for background in Background:
                    BACKGROUND = (background).replace('UY105_CR20,0,105,105','SY1000_CR0,0,1563,1000')
                Play(clean_name,url3,10,IMAGE,BACKGROUND,DESCRIPTION,'','')
                List.append(Pass_It)
                setView('movies', 'INFO')
            else:
                pass
				
#    else:
 #       Play(clean_name,url3,10,ICON,FANART,'','','')
						
#######################################SOURCE FILE EDITOR################################################

def Source_File():
    Dialog.ok('Add Source',"Enter site url next","Then a name on second window","Close and reopen addon after to see changes")
    url = Dialog.input('ENTER SITE URL', type=xbmcgui.INPUT_ALPHANUM)
    name = Dialog.input('ENTER A MEMORABLE NAME FOR SITE', type=xbmcgui.INPUT_ALPHANUM)
    print_text_file = open(source_file,"a")
    print_text_file.write('url="'+url+'">name="'+name+'"'+'\n')
    Dialog.ok('Added',"Press OK then go back","For changes to take effect")

			
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
		
		
def Menu(name,url,mode,iconimage,fanart,description,trailer,choice,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&trailer="+urllib.quote_plus(trailer)+"&choice="+str(choice)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if not name in movie_favourites_read:
                contextMenu.append(('Add to Index Movie_Favourites','XBMC.RunPlugin(%s?choice=1&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            if not name in tv_favourites_read:
                contextMenu.append(('Add to Index TV_Favorites','XBMC.RunPlugin(%s?choice=2&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            if not name in music_favourites_read:
                contextMenu.append(('Add to Index Music_Favorites','XBMC.RunPlugin(%s?choice=3&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))				
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        

		
def Play(name,url,mode,iconimage,fanart,description,trailer,choice,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&trailer="+urllib.quote_plus(trailer)+"&choice="+str(choice)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if not name in movie_favourites_read:
                contextMenu.append(('Add to Index Movie_Favourites','XBMC.RunPlugin(%s?choice=1&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            if not name in tv_favourites_read:
                contextMenu.append(('Add to Index TV_Favorites','XBMC.RunPlugin(%s?choice=2&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            if not name in music_favourites_read:
                contextMenu.append(('Add to Index Music_Favorites','XBMC.RunPlugin(%s?choice=3&mode=3&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
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
elif mode == 1 : Main_Loop(url)
elif mode == 2 : Source_File()
elif mode == 3 : Write_Favourite(name,url,choice,fav_mode)
elif mode == 4 : Read_Favourite(name,url,choice,fav_mode)
elif mode == 5 : Favourites_menu()
#elif mode == 6 : Search()
elif mode == 7 : Index_List()
elif mode == 10: resolve(url)

		
xbmcplugin.endOfDirectory(int(sys.argv[1]))
