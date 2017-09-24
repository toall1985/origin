# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from lib import process
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.plugin.video.iamgroot/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.iamgroot/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
    FAV = open(favourites).read()
else:
    FAV = []

def Main_Menu():
	process.Menu('TV Shows','',300,'','','','')
	process.Menu('Movies','',200,'','','','')
	process.Menu('Comedy','http://www.imdb.com/user/ur80459712/watchlist',13,'','','','')
	process.Menu('Origin\'s Entertainment','',14,'','','','')
	process.Menu('Favourites','',10,'','','','')
	process.setView('movies', 'INFO')
	
def Origin_picks():
	process.Menu('Origin\'s TV','http://www.imdb.com/list/ls020814698/',16,'','','','')
	process.Menu('Origin\'s Movies','http://www.imdb.com/list/ls020814225/',15,'','','','')
	
def get_list_movie(url):
	html = requests.get(url).content
	block = re.findall('<div class="list_item(.+?)<div class="clear"',html,re.DOTALL)
	for blocky in block:
		url = re.findall('href="(.+?)"',str(blocky))[0]
		image = re.findall('img src="(.+?)"',str(blocky))[0]
		name = re.findall('<div class="info">.+?href=.+?>(.+?)</a>',str(blocky),re.DOTALL)[0]
		year = re.findall('<span class="year_type">(.+?)</span>',str(blocky))[0]
		desc,length = re.findall('"item_description">(.+?)<span>(.+?)</span>',str(blocky))[0]
		process.PLAY(name+' '+year,'Movies',1501,image,'',length+' '+desc,'>'+name+'>'+year+'>')
	
def get_list_tv(url):
	html = requests.get(url).content
	block = re.findall('<div class="list_item(.+?)<div class="clear"',html,re.DOTALL)
	for blocky in block:
		url = re.findall('href="(.+?)"',str(blocky))[0]
		image = re.findall('img src="(.+?)"',str(blocky))[0]
		name = re.findall('<div class="info">.+?href=.+?>(.+?)</a>',str(blocky),re.DOTALL)[0]
		year = re.findall('<span class="year_type">(.+?)</span>',str(blocky))[0]
		desc,length = re.findall('"item_description">(.+?)<span>(.+?)</span>',str(blocky))[0]
		year = re.sub("[^()0123456789\.]","",year)
		process.Menu(name+' '+year,'http://imdb.com'+url,305,image,'',desc,name.encode('utf-8')+year.encode('utf-8'))
	
def comedy(url):
	html = requests.get(url).content
	match = re.compile('{"primary".+?"href":"(.+?)".+?"year":\["(.+?)".+?"title":"(.+?)".+?"plot":(.+?)".+?"poster":.+?"url":"(.+?)".+?"numberOfEpisodes":(.+?),').findall(html)
	for url,year,name,desc,image,eps in match:
		desc = desc.replace('"','').replace('&#39;','\'').replace('&quot;','"')
		try:
			extra_name = re.findall('(.+?):',str(name))[0]
		except:
			extra_name = name
		if eps == 'null':
			process.PLAY(name + ' (' + year+')','Movies',1501,image,'',desc,'>'+extra_name+'>'+year+'>')
		else:
			process.PLAY(name + ' (' + year+')','http://imdb.com'+url,305,image,'',desc,name+'('+year+')')

def TV_Calender_Day(url):
	from datetime import datetime
	today = datetime.now().strftime("%d")
	this_month = datetime.now().strftime("%m")
	this_year = datetime.now().strftime("%y")
	todays_number = (int(this_year)*100)+(int(this_month)*31)+(int(today))
	HTML = process.OPEN_URL(url)
	match = re.compile('<span class="dayofmonth">.+?<span class=".+?">(.+?)</span>(.+?)</span>(.+?)</div>',re.DOTALL).findall(HTML)
	for Day_Month,Date,Block in match:
		Date = Date.replace('\n','').replace('  ','').replace('	','')
		Day_Month = Day_Month.replace('\n','').replace('  ','').replace('	','')
		Final_Name = Day_Month.replace(',',' '+Date+' ')
		split_month = Day_Month+'>'
		Month_split = re.compile(', (.+?)>').findall(str(split_month))
		for item in Month_split:
			month_one = item.replace('January','1').replace('February','2').replace('March','3').replace('April','4').replace('May','5').replace('June','6')
			month = month_one.replace('July','7').replace('August','8').replace('September','9').replace('October','10').replace('November','11').replace('December','12')
		show_day = Date.replace('st','').replace('th','').replace('nd','').replace('rd','')
		shows_number = (int(this_year)*100)+(int(month)*31)+(int(show_day))
		if shows_number>= todays_number:
			process.Menu('[COLORred]*'+'[COLORwhite]'+Final_Name+'[/COLOR]','',7,'','','',Block)
		else:
			process.Menu('[COLORgreen]*'+'[COLORwhite]'+Final_Name+'[/COLOR]','',7,'','','',Block)

def TV_Calender_Prog(extra):
	match = re.compile('<span class="show">.+?<a href=".+?">(.+?)</a>:.+?</span>.+?<a href=".+?" title=".+?">(.+?)</a>',re.DOTALL).findall(str(extra))
	for prog, ep in match:
		process.PLAY(prog+' - Season '+ep.replace('x',' Episode '),'',8,'','','',prog)

def send_to_search(name,extra):
	title,season,episode = re.findall('<(.+?)- Season (.+?) Episode (.+?)>','<'+str(name)+'>')[0]
	if 'COLOR' in name:
		name = re.compile('- (.+?)>').findall(str(name)+'>')
		for name in name:
			name = name
	dp =  xbmcgui.DialogProgress()
	dp.create('Checking for stream')
	from lib import Scrape_Nan
	Scrape_Nan.scrape_episode(title,'','',season,episode,'')
	
def movie_search(extra):
	xbmc.log(extra,xbmc.LOGNOTICE)
	title,year = re.findall('>(.+?)>(.+?)>',str(extra))[0]
	xbmc.log(title,xbmc.LOGNOTICE)
	xbmc.log(year,xbmc.LOGNOTICE)
	from lib import Scrape_Nan
	Scrape_Nan.scrape_movie(title,year,'')
	
	
	
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
elif mode == 1 : process.queueItem()
elif mode == 2 : Search()
elif mode == 6 : TV_Calender_Day(url)
elif mode == 7 : TV_Calender_Prog(extra)
elif mode == 8 : send_to_search(name,extra)
elif mode == 10: from lib import process;process.getFavourites()
elif mode==11:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    process.addFavorite(name, url, fav_mode, iconimage, fanart, description, extra)
elif mode==12:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    process.rmFavorite(name)
elif mode == 13: comedy(url)
elif mode == 14: Origin_picks()
elif mode == 15: get_list_movie(url)
elif mode == 16: get_list_tv(url)
elif mode == 20: from lib import process;process.Big_Resolve(name,url)
elif mode == 200 : from lib import Movies;Movies.Movie_Main(url)
elif mode == 202 : from lib import Movies;Movies.Movie_Genre(url)
elif mode == 203 : from lib import Movies;Movies.IMDB_Grab(url)
elif mode == 204 : from lib import Movies;Movies.Check_Link(name,url,image)
elif mode == 205 : from lib import Movies;Movies.Get_playlink(url)
elif mode == 206 : from lib import Movies;Movies.IMDB_Top250(url)
elif mode == 207 : from lib import Movies;Movies.search_movies()
elif mode == 208 : from lib import Movies;Movies.movie_channels()
elif mode == 300 : from lib import multitv;multitv.multiv_Main_Menu(url)
elif mode == 301 : from lib import multitv;multitv.IMDB_TOP_100_EPS(url)
elif mode == 302 : from lib import multitv;multitv.Popular(url)
elif mode == 303 : from lib import multitv;multitv.Genres()
elif mode == 304 : from lib import multitv;multitv.Genres_Page(url)
elif mode == 305 : from lib import multitv;multitv.IMDB_Get_Season_info(url,iconimage,extra)
elif mode == 306 : from lib import multitv;multitv.IMDB_Get_Episode_info(url,extra)
elif mode == 307 : from lib import multitv;multitv.SPLIT(extra)
elif mode == 308 : from lib import multitv;multitv.Search_TV()
elif mode == 1501: movie_search(extra)
xbmcplugin.endOfDirectory(int(sys.argv[1]))