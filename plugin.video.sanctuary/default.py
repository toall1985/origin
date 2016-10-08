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
import xbmcplugin, xbmc, xbmcaddon
from lib import comedy, process, Big_Kids, Football_Repeat, Movies, multitv, Kodible, radio_gaga, xxx_vids, Pandora, apprentice, ninja
from lib.pyramid import pyramid
from lib.freeview import freeview
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
addon_id = 'plugin.video.sanctuary'
ADDON = xbmcaddon.Addon(id=addon_id)
FANART = ADDON_PATH + 'fanart.jpg'
Adult_Pass = ADDON.getSetting('Adult')
ORIGIN_ICON = 'http://herovision.x10host.com/freeview/origin.png'
ORIGIN_FANART = 'http://herovision.x10host.com/freeview/origin.jpg'
APPRENTICE_ICON = 'http://herovision.x10host.com/freeview/apprentice.png'
PANDORA_ICON = 'https://s32.postimg.org/ov9s6ipf9/icon.png'
RAIDER_ICON = 'http://herovision.x10host.com/freeview/pyramid.png'
FREEVIEW_ICON = 'http://herovision.x10host.com/freeview/freeview.png'
NINJA_ICON = 'http://herovision.x10host.com/freeview/ninja2.png'

def Main_Menu():
    process.Menu('Origin','',4,ORIGIN_ICON,FANART,'','')
    process.Menu('The Apprentice','',1300,APPRENTICE_ICON,FANART,'','')
    process.Menu('Pandora\'s Box','',900,PANDORA_ICON,FANART,'','')
    process.Menu('Raider','',1100,RAIDER_ICON,FANART,'','')
    process.Menu('FreeView - [COLORred]VPN required if you are outside UK[/COLOR]','',1200,FREEVIEW_ICON,FANART,'','')
    if Adult_Pass == 'forefingeroffury':
        process.Menu('Just For Men','',1400,NINJA_ICON,FANART,'','')
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
    process.Menu('Favourites [COLORred]Some teething issues will be fixed in updates[/COLOR]','',10,'http://herovision.x10host.com/freeview/favs.png',FANART,'','')
    process.setView('movies', 'MAIN')	

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
    process.Menu('Audiobooks','',600,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('World Radio','',500,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Music section to be added soon','',2,ORIGIN_ICON,ORIGIN_FANART,'','')
		

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
	
if mode == None: Main_Menu();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
#elif mode == 1 : 
elif mode == 2 : Music();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
#elif mode == 3 : 
elif mode == 4 : Origin_Main()
elif mode == 10: process.getFavourites();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 100: comedy.Comedy_Main();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 200: Movies.Movie_Main();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 300: multitv.multiv_Main_Menu();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 400: Football_Repeat.footy_Main_Menu();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 500: radio_gaga.Radio_Country();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 600: Kodible.Kodible_Main_Menu();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 700: xxx_vids.X_vid_Menu();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 800: Big_Kids.Big_Kids_Main_Menu();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 900: Pandora.Pandora_Main();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1100: pyramid.SKindex()
elif mode == 1200: freeview.CATEGORIES();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1300: apprentice.apprentice_Main();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1400: ninja.CATEGORIES();    xbmcplugin.endOfDirectory(int(sys.argv[1]))
xbmcplugin.endOfDirectory(int(sys.argv[1]))
