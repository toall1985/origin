# -*- coding: utf-8 -*-

'''
    Sanctuary Add-on
    Copyright (C) 2016 Origin

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
	
    This addon could not of became what it is without the help and generosity of everyone involved.
    Not all of the coding is my original work but i have tried my best to utilise and learn from others.
    If i have used code that you wrote i can only apologise for not thanking you personally and ensure you no offence was meant.
    Just sometimes i find it best not to rewrite what works well, mostly to a higher standard that my current understanding
'''
import xbmcplugin, xbmc, xbmcaddon, urllib, xbmcgui, traceback, requests, re
from lib import process
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
addon_id = 'plugin.video.sanctuary'
ADDON = xbmcaddon.Addon(id=addon_id)
FANART = ADDON_PATH + 'fanart.jpg'
Adult_Pass = ADDON.getSetting('Adult')
base_icons = 'http://herovision.x10host.com/freeview/'
ORIGIN_ICON = base_icons + 'origin.png'
ORIGIN_FANART = base_icons + 'origin.jpg'
APPRENTICE_ICON = base_icons + 'apprentice.png'
PANDORA_ICON = 'https://s32.postimg.org/ov9s6ipf9/icon.png'
RAIDER_ICON = base_icons + 'pyramid.png'
FREEVIEW_ICON = base_icons + 'freeview.png'
NINJA_ICON = base_icons + 'ninja2.png'
MAVERICK_ICON = base_icons + 'maverick.png'
BRETTUS_ICON = base_icons + 'brettus_anime.png'
OBLIVION_ICON = base_icons + 'oblivion.png'
TIGEN_ICON = base_icons + 'Tigen.png'
COLD_ICON = base_icons + 'Cold.png'
BAMF_ICON = base_icons + 'BAMF.png'
FREEDOM_ICON = base_icons + 'freedom.png'
RENEGADES_ICON = base_icons + 'renegades.png'
QUICK_ICON = base_icons + 'quick.png'
RAY_ICON = base_icons + 'raysraver.png'
SILENT_ICON = base_icons + 'silent.png'
REAPER_ICON = base_icons + 'reaper.png'
DOJO_ICON = base_icons + 'dojo.png'
ULTRA_ICON = base_icons + 'Ultra.png'

def Main_Menu():
    if ADDON.getSetting('Origin')=='true':
        process.Menu('Origin','',4,ORIGIN_ICON,FANART,'','')
    if ADDON.getSetting('Pandoras_Box')=='true':
        process.Menu('Pandora\'s Box','',900,PANDORA_ICON,FANART,'','')
    if ADDON.getSetting('Pyramid')=='true':
        process.Menu('Pyramid','',1100,RAIDER_ICON,FANART,'','')
    if ADDON.getSetting('Maverick')=='true':
        process.Menu('Maverick TV','',1128,MAVERICK_ICON,FANART,'','')
    if ADDON.getSetting('Freeview')=='true':
        process.Menu('FreeView - [COLORred]VPN required if you are outside UK[/COLOR]','',1200,FREEVIEW_ICON,FANART,'','')
    if ADDON.getSetting('Brettus_Anime')=='true':
        process.Menu('Brettus Anime','',1600,BRETTUS_ICON,FANART,'','')
    if ADDON.getSetting('Oblivion')=='true':
        process.Menu('Oblivion IPTV','',1129,OBLIVION_ICON,FANART,'','')
    if ADDON.getSetting("Tigen's_World")=='true':
        process.Menu('Tigen\'s World','',1143,TIGEN_ICON,FANART,'','')
    if ADDON.getSetting('Cold_As_Ice')=='true':
        process.Menu('Cold As Ice','',1800,COLD_ICON,FANART,'','')
    if ADDON.getSetting('Supremacy')=='true':
        process.Menu('Supremacy','',1131,'http://www.stephen-builds.co.uk/wizard/fanart.jpg',FANART,'','')
    if ADDON.getSetting('Freedom')=='true':
        process.Menu('Freedom IPTV','',1900,FREEDOM_ICON,FANART,'','')
    if ADDON.getSetting('Renegades')=='true':
        process.Menu('Renegades Darts','',2150,RENEGADES_ICON,FANART,'','')
    if ADDON.getSetting('Just_For_Him')=='true':
        process.Menu('Just For Him','',1400,NINJA_ICON,FANART,'','')
    if ADDON.getSetting('BAMF')=='true':
        process.Menu('BAMF IPTV','',1132,BAMF_ICON,FANART,'','')
    if ADDON.getSetting('Quicksilver')=='true':
        process.Menu('Quicksilver Music','',1133,QUICK_ICON,'','','')
    if ADDON.getSetting('Rays_Ravers')=='true':
        process.Menu('Rays Ravers','',2250,RAY_ICON,'','','')
    if ADDON.getSetting('Silent_Hunter')=='true':
        process.Menu('Silent Hunter','',1134,SILENT_ICON,'','','')
    if ADDON.getSetting('Dojo')=='true':
        process.Menu('Dojo Streams','http://herovision.x10host.com/dojo/main.php',2300,DOJO_ICON,'','','')
    if ADDON.getSetting('Reaper')=='true':
        process.Menu('Reaper','https://leto.feralhosting.com/grimw01f/tr/mainmenu.php',2301,REAPER_ICON,'','','')
    if ADDON.getSetting('Ultra')=='true':
        process.Menu('Ultra IPTV','',1145,ULTRA_ICON,'','','')
    if ADDON.getSetting('TV_Guide')=='true':
        process.Menu('TV Guide','',2200,ICON,FANART,'','')
    if ADDON.getSetting("Today's_Football")=='true':
        process.Menu('Today\'s Football','',1750,ICON,FANART,'','')
    if ADDON.getSetting('Latest_Episodes')=='true':
        process.Menu('Latest Episodes','',3,ICON,FANART,'','')
    if ADDON.getSetting('Recent_Movies')=='true':
        process.Menu('Recent Movies','',5,ICON,FANART,'','')
    if ADDON.getSetting('Favourites')=='true':
        process.Menu('Favourites','',10,base_icons + 'favs.png',FANART,'','')
    if ADDON.getSetting('Search')=='true':
        process.Menu('Search','',1500,base_icons + 'search.png',FANART,'','')
    process.setView('movies', 'MAIN')
	
def DOJO_MAIN(url):
    OPEN = process.OPEN_URL(url)
    Regex = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(OPEN)
    for url,icon,desc,fanart,name in Regex:
        if 'php' in url:
            process.Menu(name,url,2300,icon,fanart,desc,'')
        else:
            process.Play(name,url,906,icon,fanart,desc,'')

    process.setView('tvshows', 'Media Info 3')			
		
def Reaper_Loop(url):
    OPEN = process.OPEN_URL(url)
    Regex = re.compile('<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>').findall(OPEN)
    for name,url,icon,fanart,desc in Regex:
        if 'Favourites' in name:
            pass
        elif 'Search' in name:
            pass
        elif 'php' in url:
            process.Menu(name,url,2301,icon,fanart,desc,'')
        else:
            process.Play(name,url,906,icon,fanart,desc,'')


def Latest_Episodes():
    process.Menu('Pandora Latest Episodes','http://genietvcunts.co.uk/PansBox/ORIGINS/recenttv.php',426,ICON,FANART,'','')
    process.Menu('Origin Latest Episodes','http://www.watchseriesgo.to/latest',301,ICON,FANART,'','')
    process.Menu('TV Schedule','http://www.tvmaze.com/calendar',6,ICON,FANART,'','')

def Recent_Movies():
    process.Menu('Pandora Recent Movies','http://genietvcunts.co.uk/PansBox/ORIGINS/recentmovies.php',426,ICON,FANART,'','')
    process.Menu('Pyramid Recent Movies','http://tombraiderbuilds.co.uk/addon/New%20Releaes/newreleases.txt',1101,ICON,FANART,'','')
    process.Menu('Maverick Recent Movies','http://164.132.106.213/data/movies/2016.xml',1101,ICON,FANART,'','')
    process.Menu('Supremacy Recent Movies','https://simplekore.com/wp-content/uploads/file-manager/steboy11/New%20Releases/New%20Releases.txt',1101,ICON,FANART,'','')


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
		process.Menu(prog+' - Season '+ep.replace('x',' Episode '),'',8,'','','',prog)

def send_to_search(name,extra):
	dp =  xbmcgui.DialogProgress()
	dp.create('Checking for stream')
	from lib import search, Scrape_Nan
	Search_name = extra.lower().replace(' ','')
	name_splitter = name + '<>'
	name_split = re.compile('(.+?) - Season(.+?) Episode(.+?)<>').findall(str(name_splitter))
	for name,season,episode in name_split:
		title = name
		season = season
		episode = episode
	year = ''
	Scrape_Nan.scrape_episode(title,year,'',season,episode)
	search.TV(Search_name)

def send_to_movie_search(name,extra):
	from lib import Scrape_Nan
	if '(' in name:
		name_minus_year = re.compile('(.+?) \(').findall(str(name))
		for item in name:
			name = item
	dp =  xbmcgui.DialogProgress()
	dp.create('Checking for stream')
	year = extra.replace('/)','').replace('/(','')
	Scrape_Nan.scrape_movie(name,year)




def Origin_Main():
    process.Menu('Movies','',200,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('TV Shows','',300,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Comedy','',100,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Sports Replays','',2100,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Cartoons','',800,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Music','',2,ORIGIN_ICON,ORIGIN_FANART,'','')
    if Adult_Pass == 'forefingeroffury':
        process.Menu('Porn','',700,ORIGIN_ICON,ORIGIN_FANART,'','')

def Music():
    process.Menu('Now thats what i call music','',1700,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Misc A-Z','http://herovision.x10host.com/Music/',2000,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Audiobooks','',600,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('World Radio','',500,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Music Search','',1503,'','','','')


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
extra=None
fanart=None
fav_mode=None
regexs=None
playlist=None

try:
    regexs=params["regexs"]
except:
    pass

try:
    fav_mode=int(params["fav_mode"])
except:
    pass
try:
    extra=urllib.unquote_plus(params["extra"])
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
    playitem=urllib.unquote_plus(params["playitem"])
except:
    pass
try:
    playlist=eval(urllib.unquote_plus(params["playlist"]).replace('||',','))
except:
    pass
try:
    regexs=params["regexs"]
except:
    pass


if mode == None: Main_Menu()
elif mode == 1 : process.queueItem()
elif mode == 2 : Music()
elif mode == 3 : Latest_Episodes()
elif mode == 4 : Origin_Main()
elif mode == 5 : Recent_Movies()
elif mode == 6 : TV_Calender_Day(url)
elif mode == 7 : TV_Calender_Prog(extra)
elif mode == 8 : send_to_search(name,extra)
elif mode == 9 : from lib import Scrape_Nan;Scrape_Nan.scrape_movie(name,extra)
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
    process.addFavorite(name,url,iconimage,fanart,fav_mode)
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
elif mode == 15: from lib import Scrape_Nan;Scrape_Nan.scrape_episode(extra)
elif mode == 20: pass
elif mode == 100: from lib import comedy;comedy.Comedy_Main()
elif mode == 101: from lib import comedy;comedy.Stand_up()
elif mode == 102: from lib import comedy;comedy.Search()
elif mode == 103: from lib import comedy;comedy.Play_Stage(url)
elif mode == 104: from lib import comedy;comedy.Regex(url)
elif mode == 105: process.Resolve(url)
elif mode == 106: from lib import comedy;comedy.Stand_up_Menu()
elif mode == 107: from lib import comedy;comedy.grab_youtube_playlist(url)
elif mode == 108: from lib import comedy;comedy.Search()
elif mode == 109: from lib import yt;yt.PlayVideo(url)
elif mode == 110: from lib import comedy;comedy.Movies_Menu()
elif mode == 111: from lib import comedy;comedy.Pubfilm_Comedy_Grab(url)
elif mode == 112: from lib import comedy;comedy.Grab_Season(iconimage,url)
elif mode == 113: from lib import comedy;comedy.Grab_Episode(url,name,fanart,iconimage)
elif mode == 114: from lib import comedy;comedy.Get_Sources(name,url,iconimage,fanart)
elif mode == 115: from lib import comedy;comedy.Get_site_link(url,name)
elif mode == 116: from lib import comedy;comedy.final(url)
elif mode == 200: from lib import Movies;Movies.Movie_Main()
elif mode == 202 : from lib import Movies;Movies.Movie_Genre(url)
elif mode == 203 : from lib import Movies;Movies.IMDB_Grab(url)
elif mode == 204 : from lib import Movies;Movies.Check_Link(name,url,image)
elif mode == 205 : from lib import Movies;Movies.Get_playlink(url)
elif mode == 206 : from lib import Movies;Movies.IMDB_Top250(url)
elif mode == 207 : from lib import Movies;Movies.search_movies()
elif mode == 208 : from lib import Movies;Movies.movie_channels()
elif mode == 209 : from lib import Movies;Movies.split_for_search(extra)
elif mode == 300 : from lib import multitv;multitv.multiv_Main_Menu()
elif mode == 301 : from lib import multitv;multitv.IMDB_TOP_100_EPS(url)
elif mode == 302 : from lib import multitv;multitv.Popular(url)
elif mode == 303 : from lib import multitv;multitv.Genres()
elif mode == 304 : from lib import multitv;multitv.Genres_Page(url)
elif mode == 305 : from lib import multitv;multitv.IMDB_Get_Season_info(url,iconimage,extra)
elif mode == 306 : from lib import multitv;multitv.IMDB_Get_Episode_info(url,extra)
elif mode == 307 : from lib import multitv;multitv.SPLIT(extra)
elif mode == 308 : from lib import multitv;multitv.Search_TV()
elif mode == 400: from lib import Football_Repeat;Football_Repeat.footy_Main_Menu()
elif mode == 401: from lib import Football_Repeat;Football_Repeat.get_All_Rows(url,iconimage)
elif mode == 402: from lib import Football_Repeat;Football_Repeat.get_PLAYlink(url)
elif mode == 403: from lib import Football_Repeat;Football_Repeat.Football_Highlights()
elif mode == 404: from lib import Football_Repeat;Football_Repeat.FootballFixturesDay()
elif mode == 405: from lib import Football_Repeat;Football_Repeat.FootballFixturesGame(url,iconimage)
elif mode == 406: from lib import Football_Repeat;Football_Repeat.Prem_Table(url)
elif mode == 407: from lib import Football_Repeat;Football_Repeat.get_Multi_Links(url,iconimage)
elif mode == 408: from lib import Football_Repeat;Football_Repeat.Get_the_rows(url,iconimage)
elif mode == 409: from lib import Football_Repeat;Football_Repeat.League_Tables(url)
elif mode == 410: from lib import Football_Repeat;Football_Repeat.Search()
elif mode == 411: from lib import Football_Repeat;Football_Repeat.Prem_Table2(url)
elif mode == 412: from lib import Football_Repeat;Football_Repeat.champ_league(url)
elif mode == 413: from lib import Football_Repeat;Football_Repeat.footytube(url)
elif mode == 414: from lib import Football_Repeat;Football_Repeat.footytube_leagues(name)
elif mode == 415: from lib import Football_Repeat;Football_Repeat.footytube_teams(url)
elif mode == 416: from lib import Football_Repeat;Football_Repeat.footytube_videos(url)
elif mode == 417: from lib import Football_Repeat;Football_Repeat.footytube_frame(name,url)
elif mode == 418: from lib import Football_Repeat;Football_Repeat.get_origin_playlink(url,iconimage,FANART)
elif mode == 419: from lib import Football_Repeat;Football_Repeat.Resolve(url)
elif mode == 420: from lib import Football_Repeat;Football_Repeat.FootballFixturesSingle(description);Football_Repeat.window.doModal();del Football_Repeat.window
elif mode == 421: from lib import Football_Repeat;Football_Repeat.METALLIQ()
elif mode == 500: from lib import radio_gaga;radio_gaga.Radio_Country()
elif mode == 501: from lib import radio_gaga;radio_gaga.Radio(url)
elif mode == 502: process.Resolve(url)
elif mode == 600: from lib import Kodible;Kodible.Kodible_Main_Menu()
elif mode == 602: process.Resolve(url)
elif mode == 603: from lib import Kodible;Kodible.Kids_Audio()
elif mode == 604: from lib import Kodible;Kodible.Kids_Play(url)
elif mode == 605: from lib import Kodible;Kodible.Kids_Play_Multi(url)
elif mode == 606: from lib import Kodible;Kodible.Kids_Menu()
elif mode == 607: from lib import Kodible;Kodible.Kids_AZ()
elif mode == 608: from lib import Kodible;Kodible.Kids_AZ_Audio(url)
elif mode == 614: from lib import Kodible;Kodible.Search_Kids()
elif mode == 700: from lib import xxx_vids;xxx_vids.X_vid_Menu()
elif mode == 701: from lib import xxx_vids;xxx_vids.XNew_Videos(url)
elif mode == 702: from lib import xxx_vids;xxx_vids.XGenres(url)
elif mode == 703: from lib import xxx_vids;xxx_vids.XPornstars(url)
elif mode == 704: from lib import xxx_vids;xxx_vids.XSearch_X()
elif mode == 705: from lib import xxx_vids;xxx_vids.Xtags(url)
elif mode == 706: from lib import xxx_vids;xxx_vids.XPlayLink(url)
elif mode == 800: from lib import Big_Kids;Big_Kids.Big_Kids_Main_Menu()
elif mode == 801: from lib import Big_Kids;Big_Kids.TESTCATS()
elif mode == 802: from lib import Big_Kids;Big_Kids.Search()
elif mode == 803: from lib import Big_Kids;Big_Kids.LISTS(url)
elif mode == 804: from lib import Big_Kids;Big_Kids.LISTS2(url,iconimage)
elif mode == 805: process.Resolve(url)
elif mode == 806: from lib import Big_Kids;Big_Kids.Classics1()
elif mode == 807: from lib import Big_Kids;Big_Kids.Classics2(url)
elif mode == 808: from lib import Big_Kids;Big_Kids.Classics3(url)
elif mode == 900: from lib import Pandora;Pandora.Pandora_Main()
elif mode == 901: from lib import Pandora;Pandora.Pandoras_Box()
elif mode == 423: from lib import Pandora;Pandora.open_Menu(url)
elif mode == 426: from lib import Pandora;Pandora.Pandora_Menu(url)
elif mode == 903: from lib import Pandora;Pandora.Search_Menu()
elif mode == 904: from lib import Pandora;Pandora.Search_Pandoras_Films()
elif mode == 905: from lib import Pandora;Pandora.Search_Pandoras_TV()
elif mode == 906: process.Big_Resolve(name,url)
elif mode == 907: from lib import Pandora;Pandora.Pans_Resolve(name,url)
elif mode == 1100: from lib.pyramid import pyramid;pyramid.SKindex()
elif mode == 1128: from lib.pyramid import pyramid;pyramid.SKindex_Joker()
elif mode == 1129: from lib.pyramid import pyramid;pyramid.SKindex_Oblivion()
elif mode == 1131: from lib.pyramid import pyramid;pyramid.SKindex_Supremacy()
elif mode == 1132: from lib.pyramid import pyramid;pyramid.SKindex_BAMF()
elif mode == 1133: from lib.pyramid import pyramid;pyramid.SKindex_Quicksilver()
elif mode == 1134: from lib.pyramid import pyramid;pyramid.SKindex_Silent()
elif mode == 1101:from lib.pyramid import pyramid;pyramid.getData(url,fanart);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1102:from lib.pyramid import pyramid;pyramid.getChannelItems(name,url,fanart);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1103:from lib.pyramid import pyramid;pyramid.getSubChannelItems(name,url,fanart);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1104:from lib.pyramid import pyramid;pyramid.getFavorites();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1105:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    from lib.pyramid import pyramid;pyramid.addFavorite(name,url,iconimage,fanart,fav_mode)
elif mode==1106:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    from lib.pyramid import pyramid;pyramid.rmFavorite(name)
elif mode==1107:from lib.pyramid import pyramid;pyramid.addSource(url)
elif mode==1108:from lib.pyramid import pyramid;pyramid.rmSource(name)
elif mode==1109:from lib.pyramid import pyramid;pyramid.download_file(name, url)
elif mode==1110:from lib.pyramid import pyramid;pyramid.getCommunitySources()
elif mode==1111:from lib.pyramid import pyramid;pyramid.addSource(url)
elif mode==1112:
	import urlresolver
	try:
		resolved_url = urlresolver.resolve(url)
		xbmc.Player().play(resolved_url, xbmcgui.ListItem(name))
	except:
		try:
			xbmc.Player().play(url, xbmcgui.ListItem(name))
		except:
			xbmcgui.Dialog().notification("Sanctuary", "unplayable stream")
			sys.exit()
#    if not url.startswith("plugin://plugin") or not any(x in url for x in pyramid.g_ignoreSetResolved):#not url.startswith("plugin://plugin.video.f4mTester") :
 #       item = xbmcgui.ListItem(path=url)
  #      xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
   # else:
    #    print 'Not setting setResolvedUrl'
     #   xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
elif mode==1113:from lib.pyramid import pyramid;pyramid.play_playlist(name, playlist)
elif mode==1114:from lib.pyramid import pyramid;pyramid.get_xml_database(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1115:from lib.pyramid import pyramid;pyramid.get_xml_database(url, True);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1116:from lib.pyramid import pyramid;pyramid.getCommunitySources(True);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1117:
    url,setresolved = getRegexParsed(regexs, url)
    if url:
        from lib.pyramid import pyramid;pyramid.playsetresolved(url,name,iconimage,setresolved)
    else:
        xbmc.executebuiltin("XBMC.Notification(ThePyramid ,Failed to extract regex. - "+"this"+",4000,"+icon+")")
elif mode==1118:
    try:
        from lib.pyramid import youtubedl
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000,"")")
    stream_url=youtubedl.single_YD(url)
    from lib.pyramid import pyramid;pyramid.playsetresolved(stream_url,name,iconimage)
elif mode==1119:from lib.pyramid import pyramid;pyramid.playsetresolved (pyramid.urlsolver(url),name,iconimage,True)
elif mode==1121:from lib.pyramid import pyramid;pyramid.ytdl_download('',name,'video')
elif mode==1123:from lib.pyramid import pyramid;pyramid.ytdl_download(url,name,'video')
elif mode==1124:from lib.pyramid import pyramid;pyramid.ytdl_download(url,name,'audio')
elif mode==1125:from lib.pyramid import pyramid;pyramid.search(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1126:
    name = name.split(':')
    from lib.pyramid import pyramid;pyramid.search(url,search_term=name[1])
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1127:
    from lib.pyramid import pyramid;pyramid.pulsarIMDB=search(url)
    xbmc.Player().play(pulsarIMDB)
elif mode == 1130:from lib.pyramid import pyramid;pyramid.GetSublinks(name,url,iconimage,fanart)
elif mode == 1140:from lib.pyramid import pyramid;pyramid.SearchChannels();pyramid.SetViewThumbnail();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1141: from lib.pyramid import pyramid;pyramid.Search_input(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1142: from lib.pyramid import pyramid;pyramid.RESOLVE(url)
elif mode == 1143: from lib.pyramid import pyramid;pyramid.SKindex_TigensWorld()
elif mode == 1144: from lib.pyramid import pyramid;pyramid.queueItem()
elif mode == 1145: from lib.pyramid import pyramid;pyramid.SKindex_Ultra()
elif mode == 1153: from lib.pyramid import pyramid;pyramid.pluginquerybyJSON(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1200: from lib.freeview import freeview;freeview.CATEGORIES()
elif mode == 1201: from lib.freeview import freeview;freeview.play(url)
elif mode == 1202: from lib.freeview import freeview;freeview.tvplayer(url)
elif mode == 1400 : from lib import ninja;ninja.CATEGORIES()
elif mode == 1401 : from lib import ninja;ninja.VIDEOLIST(url)
elif mode == 1402 : from lib import ninja;ninja.PLAYVIDEO(url)
elif mode == 1500 : from lib import search;search.Search_Menu()
elif mode == 1501 : from lib import search;search.Search_Input(url)
elif mode == 1502 : from lib import search;search.MUSIC(Search_name,url)
elif mode == 1503 : from lib import search;search.Music_Search()
elif mode == 1600 : from lib import brettus_anime;brettus_anime.GetList()
elif mode == 1601 : from lib import brettus_anime;brettus_anime.GetContent(url,iconimage)
elif mode == 1602 : from lib import brettus_anime;brettus_anime.PLAYLINK(url,iconimage)
elif mode == 1700 : from lib import Now_thats_what_i_call_music;Now_thats_what_i_call_music.Now_Thats_What_I_Call_Music()
elif mode == 1701 : from lib import Now_thats_what_i_call_music;Now_thats_what_i_call_music.Now_Loop(url,iconimage,fanart)
elif mode == 1702 : from lib import Now_thats_what_i_call_music;Now_thats_what_i_call_music.Now_Playlinks(url,iconimage,fanart)
elif mode == 1750 : from lib import todays_football;todays_football.Todays_Football_Menu()
elif mode == 1751 : from lib import todays_football;todays_football.Todays_Football()
elif mode == 1752 : from lib import todays_football;todays_football.Search_Channels_Mainstream(url)
elif mode == 1753 : from lib import todays_football;todays_football.Live_On_Sat()
elif mode == 1800 : from lib import cold_as_ice;cold_as_ice.Cold_Menu()
elif mode == 1801 : from lib import cold_as_ice;cold_as_ice.GetContent(url,iconimage)
elif mode == 1802 : from lib import cold_as_ice;cold_as_ice.PLAYLINK(name,url,iconimage)
elif mode == 1900 : from lib.freedom import freedom;freedom.getSources();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1901:
    from lib.freedom import freedom
    data=None
    if regexs:
        data=freedom.getRegexParsed(regexs, url)
        url=''
    freedom.getData(url,fanart,data)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==1902:
    from lib.freedom import freedom
    freedom.getChannelItems(name,url,fanart)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==1903:
    from lib.freedom import freedom
    freedom.getSubChannelItems(name,url,fanart)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==1904:
    from lib.freedom import freedom
    freedom.getFavorites()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==1905:
    from lib.freedom import freedom
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    freedom.addFavorite(name,url,iconimage,fanart,fav_mode)

elif mode==1906:
    from lib.freedom import freedom
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    freedom.rmFavorite(name)

elif mode==1907:
    from lib.freedom import freedom
    freedom.SportsDevil()
    freedom.Dutch()

elif mode==1908:
    from lib.freedom import freedom
    freedom.rmSource(name)

elif mode==1909:
    from lib.freedom import freedom
    freedom.download_file(name, url)

elif mode==1910:
    from lib.freedom import freedom
    freedom.getCommunitySources()

elif mode==1911:
    from lib.freedom import freedom
    freedom.addSource(url)

elif mode==1912:
    from lib.freedom import freedom
    if not url.startswith("plugin://plugin") or not any(x in url for x in freedom.g_ignoreSetResolved):#not url.startswith("plugin://plugin.video.f4mTester") :
        setres=True
        if '$$LSDirect$$' in url:
            url=url.replace('$$LSDirect$$','')
            setres=False
        item = xbmcgui.ListItem(path=url)
        if not setres:
            xbmc.Player().play(url)
        else:
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    else:
        xbmc.executebuiltin('XBMC.RunPlugin('+url+')')

elif mode==1913:
    from lib.freedom import freedom
    freedom.play_playlist(name, playlist)

elif mode==1914:
    from lib.freedom import freedom
    freedom.get_xml_database(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==1915:
    from lib.freedom import freedom
    freedom.get_xml_database(url, True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==1916:
    from lib.freedom import freedom
    freedom.getCommunitySources(url,browse=True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

playitem=''
if not playitem =='':
    s=getSoup('',data=playitem)
    name,url,regexs=getItems(s,None,dontLink=True)
    mode=1990

elif mode==1917 or mode==1990:
    from lib.freedom import freedom

    data=None
    if regexs and 'listrepeat' in urllib.unquote_plus(regexs):
        listrepeat,ret,m,regexs =freedom.getRegexParsed(regexs, url)
        d=''
        regexname=m['name']
        existing_list=regexs.pop(regexname)
        url=''
        import copy
        ln=''
        rnumber=0
        for obj in ret:
            try:
                rnumber+=1
                newcopy=copy.deepcopy(regexs)
                listrepeatT=listrepeat
                i=0
                for i in range(len(obj)):
                    if len(newcopy)>0:
                        for the_keyO, the_valueO in newcopy.iteritems():
                            if the_valueO is not None:
                                for the_key, the_value in the_valueO.iteritems():
                                    if the_value is not None:
                                        if type(the_value) is dict:
                                            for the_keyl, the_valuel in the_value.iteritems():
                                                if the_valuel is not None:
                                                    val=None
                                                    if isinstance(obj,tuple):
                                                        try:
                                                           val= obj[i].decode('utf-8')
                                                        except:
                                                            val= obj[i]
                                                    else:
                                                        try:
                                                            val= obj.decode('utf-8')
                                                        except:
                                                            val= obj

                                                    if '[' + regexname+'.param'+str(i+1) + '][DE]' in the_valuel:
                                                        the_valuel=the_valuel.replace('[' + regexname+'.param'+str(i+1) + '][DE]', unescape(val))
                                                    the_value[the_keyl]=the_valuel.replace('[' + regexname+'.param'+str(i+1) + ']', val)
                                                    #print 'first sec',the_value[the_keyl]

                                        else:
                                            val=None
                                            if isinstance(obj,tuple):
                                                try:
                                                     val=obj[i].decode('utf-8')
                                                except:
                                                    val=obj[i]
                                            else:
                                                try:
                                                    val= obj.decode('utf-8')
                                                except:
                                                    val= obj
                                            if '[' + regexname+'.param'+str(i+1) + '][DE]' in the_value:
                                                #print 'found DE',the_value.replace('[' + regexname+'.param'+str(i+1) + '][DE]', unescape(val))
                                                the_value=the_value.replace('[' + regexname+'.param'+str(i+1) + '][DE]', unescape(val))

                                            the_valueO[the_key]=the_value.replace('[' + regexname+'.param'+str(i+1) + ']', val)
                                            #print 'second sec val',the_valueO[the_key]

                    val=None
                    if isinstance(obj,tuple):
                        try:
                            val=obj[i].decode('utf-8')
                        except:
                            val=obj[i]
                    else:
                        try:
                            val=obj.decode('utf-8')
                        except:
                            val=obj
                    if '[' + regexname+'.param'+str(i+1) + '][DE]' in listrepeatT:
                        listrepeatT=listrepeatT.replace('[' + regexname+'.param'+str(i+1) + '][DE]',val)
                    listrepeatT=listrepeatT.replace('[' + regexname+'.param'+str(i+1) + ']',escape(val))
                listrepeatT=listrepeatT.replace('[' + regexname+'.param'+str(0) + ']',str(rnumber))

                regex_xml=''
                if len(newcopy)>0:
                    regex_xml=d2x(newcopy,'lsproroot')
                    regex_xml=regex_xml.split('<lsproroot>')[1].split('</lsproroot')[0]

                try:
                    ln+='\n<item>%s\n%s</item>'%(listrepeatT,regex_xml)
                except: ln+='\n<item>%s\n%s</item>'%(listrepeatT.encode("utf-8"),regex_xml)
            except: traceback.print_exc(file=sys.stdout)
        freedom.getData('','',ln)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
    else:
        url,setresolved = freedom.getRegexParsed(regexs, url)
        if url:
            if '$PLAYERPROXY$=' in url:
                url,proxy=url.split('$PLAYERPROXY$=')
                print 'proxy',proxy
                proxyuser = None
                proxypass = None
                if len(proxy) > 0 and '@' in proxy:
                    proxy = proxy.split(':')
                    proxyuser = proxy[0]
                    proxypass = proxy[1].split('@')[0]
                    proxyip = proxy[1].split('@')[1]
                    port = proxy[2]
                else:
                    proxyip,port=proxy.split(':')

                freedom.playmediawithproxy(url,name,iconimage,proxyip,port, proxyuser,proxypass) #jairox
            else:
                freedom.playsetresolved(url,name,iconimage,setresolved)
        else:
            xbmc.executebuiltin("XBMC.Notification(FREEDOM IPTV,Failed to extract regex. - "+"this"+",4000,"+icon+")")

elif mode==1918:
    from lib.freedom import freedom
    try:
        import youtubedl
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(FREEDOM IPTV,Please [COLOR yellow]install Youtube-dl[/COLOR] module ,10000,"")")
    stream_url=youtubedl.single_YD(url)
    freedom.playsetresolved(stream_url,name,iconimage)

elif mode==1919:
    from lib.freedom import freedom
    freedom.playsetresolved (urlsolver(url),name,iconimage,True)

elif mode==1921:
    from lib.freedom import freedom
    freedom.ytdl_download('',name,'video')

elif mode==1923:
    from lib.freedom import freedom
    freedom.ytdl_download(url,name,'video')

elif mode==1924:
    from lib.freedom import freedom
    freedom.ytdl_download(url,name,'audio')

elif mode==1925:
    from lib.freedom import freedom
    freedom._search(url,name)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==1955:
    from lib.freedom import freedom
    parentalblockedpin =addon.getSetting('parentalblockedpin')
    keyboard = xbmc.Keyboard('','Enter Pin')
    keyboard.doModal()
    if not (keyboard.isConfirmed() == False):
        newStr = keyboard.getText()
        if newStr==parentalblockedpin:
            addon.setSetting('parentalblocked', "false")
            xbmc.executebuiltin("XBMC.Notification(FREEDOM IPTV,Parental Block Disabled,5000,"+icon+")")
        else:
            xbmc.executebuiltin("XBMC.Notification(FREEDOM IPTV,Wrong Pin??,5000,"+icon+")")
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==1956:
    from lib.freedom import freedom
    addon.setSetting('parentalblocked', "true")
    xbmc.executebuiltin("XBMC.Notification(FREEDOM IPTV,Parental block enabled,5000,"+icon+")")
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==1953:
    from lib.freedom import freedom
    freedompluginquerybyJSON(url)
    #xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 2000 : from lib import index_regex;index_regex.Main_Loop(url)
elif mode == 2100 : from lib import Sports_Replays;Sports_Replays.Sports_Repeats()
elif mode == 2101 : from lib import Sports_Replays;Sports_Replays.Motor_Replays(url)
elif mode == 2102 : from lib import Sports_Replays;Sports_Replays.motor_name(url)
elif mode == 2103 : from lib import Sports_Replays;Sports_Replays.motor_race(extra)
elif mode == 2104 : from lib import Sports_Replays;Sports_Replays.motor_single(extra)
elif mode == 2105 : from lib import Sports_Replays;Sports_Replays.F1_Replays(url)
elif mode == 2106 : from lib import Sports_Replays;Sports_Replays.F1_page(url)
elif mode == 2107 : from lib import Sports_Replays;Sports_Replays.F1_items(url,iconimage)
elif mode == 2108 : from lib import Sports_Replays;Sports_Replays.F1_Playlink(url)
elif mode == 2150 : from lib import renegades;renegades.run()
elif mode == 2151 : import plugintools;plugintools.add_item(mode,name,url,iconimage,fanart)
elif mode == 2200 : from lib import tv_guide;tv_guide.TV_GUIDE_MENU()
elif mode == 2201 : from lib import tv_guide;tv_guide.whatsoncat()
elif mode == 2202 : from lib import tv_guide;tv_guide.whatson(url)
elif mode == 2203 : from lib import tv_guide;tv_guide.search_split(extra)
elif mode == 2204 : from lib import tv_guide;tv_guide.TV_GUIDE_CO_UK_CATS()
elif mode == 2205 : from lib import tv_guide;tv_guide.tvguide_co_uk(url)
elif mode == 2206 : from lib import tv_guide;tv_guide.WhatsOnCOUK(url,extra)
elif mode == 2207 : from lib import tv_guide;tv_guide.Select_Type()
elif mode == 2250 : from lib import raysravers;raysravers.LISTS(url)
elif mode == 2251 : from lib import raysravers;raysravers.LISTS2(url)
elif mode == 2252 : from lib import raysravers;raysravers.SEARCHLISTS()
elif mode == 2300 : DOJO_MAIN(url)
elif mode == 2301 : Reaper_Loop(url)
elif mode == 10000: from lib import youtube_regex;youtube_regex.Youtube_Grab_Playlist_Page(url)
elif mode == 10001: from lib import youtube_regex;youtube_regex.Youtube_Playlist_Grab(url)
elif mode == 10002: from lib import youtube_regex;youtube_regex.Youtube_Playlist_Grab_Duration(url)
elif mode == 10003: from lib import yt;yt.PlayVideo(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
