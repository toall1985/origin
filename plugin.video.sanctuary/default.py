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
import xbmcplugin, xbmc, xbmcaddon, urllib, xbmcgui
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

def Main_Menu():
    process.Menu('Origin','',4,ORIGIN_ICON,FANART,'','')
    process.Menu('The Apprentice','',1300,APPRENTICE_ICON,FANART,'','')
    process.Menu('Pandora\'s Box','',900,PANDORA_ICON,FANART,'','')
    process.Menu('Pyramid','',1100,RAIDER_ICON,FANART,'','')
    process.Menu('Maverick TV','',1128,MAVERICK_ICON,FANART,'','')
    process.Menu('FreeView - [COLORred]VPN required if you are outside UK[/COLOR]','',1200,FREEVIEW_ICON,FANART,'','')
    process.Menu('Brettus Anime','',1600,BRETTUS_ICON,FANART,'','')
#    process.Menu('Oblivion IPTV','',1129,OBLIVION_ICON,FANART,'','')
    process.Menu('Tigen\'s World','',1143,TIGEN_ICON,FANART,'','')
    process.Menu('Cold As Ice','',1800,COLD_ICON,FANART,'','')
    process.Menu('Supremacy','',1131,'http://www.stephen-builds.co.uk/wizard/fanart.jpg',FANART,'','')
    if Adult_Pass == 'forefingeroffury':
        process.Menu('Just For Him','',1400,NINJA_ICON,FANART,'','')
    process.Menu('Today\'s Football','',1750,ICON,FANART,'','')
    process.Menu('Latest Episodes','',3,ICON,FANART,'','')
    process.Menu('Recent Movies','',5,ICON,FANART,'','')
    process.Menu('Favourites','',10,base_icons + 'favs.png',FANART,'','')
    process.Menu('Search','',1500,base_icons + 'search.png',FANART,'','')
#    process.Menu('Recent','',20,base_icons + 'search.png',FANART,'','')
    process.setView('movies', 'MAIN')	
	
def Latest_Episodes():
    process.Menu('Pandora Latest Episodes','http://genietvcunts.co.uk/PansBox/ORIGINS/recenttv.php',426,ICON,FANART,'','')
    process.Menu('Origin Latest Episodes','http://www.watchseriesgo.to/latest',301,ICON,FANART,'','')

def Recent_Movies():
    process.Menu('Pandora Recent Movies','http://genietvcunts.co.uk/PansBox/ORIGINS/recentmovies.php',426,ICON,FANART,'','')
    process.Menu('Pyramid Recent Movies','http://tombraiderbuilds.co.uk/addon/New%20Releaes/newreleases.txt',1101,ICON,FANART,'','')
    process.Menu('Maverick Recent Movies','http://164.132.106.213/data/movies/2016.xml',1101,ICON,FANART,'','')
    process.Menu('Supremacy Recent Movies','https://simplekore.com/wp-content/uploads/file-manager/steboy11/New%20Releases/New%20Releases.txt',1101,ICON,FANART,'','')

def Recent():
    process.Menu('Recent Movies','',200,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Recent TV Shows','',300,ORIGIN_ICON,ORIGIN_FANART,'','')

	
def Origin_Main():
    process.Menu('Movies','',200,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('TV Shows','',300,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Comedy','',100,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Football Replays + Highlights','',400,ORIGIN_ICON,ORIGIN_FANART,'','')
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
	
if mode == None: Main_Menu()
elif mode == 1 : process.queueItem()
elif mode == 2 : Music()
elif mode == 3 : Latest_Episodes()
elif mode == 4 : Origin_Main()
elif mode == 5 : Recent_Movies()
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
elif mode == 20: Recent()
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
elif mode == 203 : from lib import Movies;Movies.Pubfilm_Grab(url)
elif mode == 204 : from lib import Movies;Movies.Check_Link(name,url,image)
elif mode == 205 : from lib import Movies;Movies.Get_playlink(url)
elif mode == 300: from lib import multitv;multitv.multiv_Main_Menu()
elif mode == 301 : from lib import multitv;multitv.Latest_Eps(url)
elif mode == 302 : from lib import multitv;multitv.Popular(url)
elif mode == 303 : from lib import multitv;multitv.Genres()
elif mode == 304 : from lib import multitv;multitv.Genres_Page(url)
elif mode == 305 : from lib import multitv;multitv.Grab_Season(url,extra)
elif mode == 306 : from lib import multitv;multitv.Grab_Episode(url,name,fanart,extra,iconimage)
elif mode == 307 : from lib import multitv;multitv.Tv_Schedule(url)
elif mode == 308 : from lib import multitv;multitv.Schedule_Grab(url)
elif mode == 309 : from lib import multitv;multitv.Search()
elif mode == 310: from lib import multitv;multitv.Get_Sources(name,url,iconimage,fanart)
elif mode == 313: from lib import multitv;multitv.Get_site_link(url,name)
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
elif mode == 417: from lib import Football_Repeat;Football_Repeat.footytube_frame(url)
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
elif mode == 906: process.Big_Resolve(url)
elif mode == 1100: from lib.pyramid import pyramid;pyramid.SKindex()
elif mode == 1128: from lib.pyramid import pyramid;pyramid.SKindex_Joker()
elif mode == 1129: from lib.pyramid import pyramid;pyramid.SKindex_Oblivion()	
elif mode == 1131: from lib.pyramid import pyramid;pyramid.SKindex_Supremacy()	
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
    from lib.pyramid import pyramid
    if not url.startswith("plugin://plugin") or not any(x in url for x in pyramid.g_ignoreSetResolved):#not url.startswith("plugin://plugin.video.f4mTester") :
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    else:
        print 'Not setting setResolvedUrl'
        xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
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
elif mode == 1153: from lib.pyramid import pyramid;pyramid.pluginquerybyJSON(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1200: from lib.freeview import freeview;freeview.CATEGORIES()
elif mode == 1201: from lib.freeview import freeview;freeview.play(url)
elif mode == 1202: from lib.freeview import freeview;freeview.tvplayer(url)
elif mode == 1300: from lib import apprentice;apprentice.apprentice_Main();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1301 : from lib import apprentice;apprentice.Mov_Menu();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1302 : from lib import apprentice;apprentice.Tv_Menu();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1303 : from lib import apprentice;apprentice.Second_Menu(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1304 : from lib import apprentice;apprentice.Index_List_Mov();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1305 : from lib import apprentice;apprentice.Main_Loop(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1306 : from lib import apprentice;apprentice.Index_List_Tv();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1307 : from lib import apprentice;apprentice.Magic_Menu();xbmcplugin.endOfDirectory(int(sys.argv[1]))
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
elif mode == 2000 : from lib import index_regex;index_regex.Main_Loop(url)
elif mode == 10000: from lib import youtube_regex;youtube_regex.Youtube_Grab_Playlist_Page(url)
elif mode == 10001: from lib import youtube_regex;youtube_regex.Youtube_Playlist_Grab(url)
elif mode == 10002: from lib import youtube_regex;youtube_regex.Youtube_Playlist_Grab_Duration(url)
elif mode == 10003: from lib import yt;yt.PlayVideo(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
