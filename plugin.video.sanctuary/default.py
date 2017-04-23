# -*- coding: utf-8 -*-

'''
    Sanctuary Add-on
    Copyright (C) 2016 Origin

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
	
    Just don't be a nob about it....

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
import xbmcplugin, xbmc, xbmcaddon, urllib, xbmcgui, traceback, requests, re, os, base64
from lib import process
import os, shutil, xbmcgui
addon_id = 'plugin.video.sanctuary'
Dialog = xbmcgui.Dialog()
addons = xbmc.translatePath('special://home/addons/')
ADDON = xbmcaddon.Addon(id=addon_id)
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
ADDON = xbmcaddon.Addon(id=addon_id)
FANART = ADDON_PATH + 'fanart.jpg'
Adult_Pass = ADDON.getSetting('Adult')
Adult_Default = ADDON.getSetting('Porn_Pass')
base_icons = 'http://herovision.x10host.com/freeview/'
ORIGIN_ICON = base_icons + 'origin.png'
ORIGIN_FANART = base_icons + 'origin.jpg'
PANDORA_ICON = 'https://s32.postimg.org/ov9s6ipf9/icon.png'
RAIDER_ICON = base_icons + 'pyramid.png'
FREEVIEW_ICON = base_icons + 'freeview.png'
NINJA_ICON = base_icons + 'ninja2.png'
BRETTUS_ICON = base_icons + 'brettus_anime.png'
OBLIVION_ICON = base_icons + 'oblivion.png'
TIGEN_ICON = base_icons + 'Tigen.png'
COLD_ICON = base_icons + 'Cold.png'
BAMF_ICON = base_icons + 'BAMF.png'
RENEGADES_ICON = base_icons + 'renegades.png'
QUICK_ICON = base_icons + 'quick.png'
RAY_ICON = base_icons + 'raysraver.png'
SILENT_ICON = base_icons + 'silent.png'
REAPER_ICON = base_icons + 'reaper.png'
DOJO_ICON = base_icons + 'dojo.png'
ULTRA_ICON = base_icons + 'Ultra.png'
FIDO_ICON = base_icons + 'fido.png'
MIDNIGHT_IMAGE = base_icons + 'midnight2.png'
INTRO_VID = base_icons + 'Intro.mp4'
INTRO_VID_TEMP = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/DELETE_ME')

ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
addon_id='plugin.video.sanctuary'
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




def Main_Menu():
    if not os.path.exists(INTRO_VID_TEMP):
        if ADDON.getSetting('Intro_Vid')=='true':
            xbmc.Player().play(INTRO_VID, xbmcgui.ListItem('You have been updated'))
            os.makedirs(INTRO_VID_TEMP)
    process.Menu('Big Bag \'O\' Tricks','',13,'',FANART,'','')
    url = 'https%3a%2f%2fredirector.googlevideo.com%2fvideoplayback%3fid%3d5592f895cd80a652%26itag%3d18%26source%3dwebdrive%26requiressl%3dyes%26ttl%3dtransient%26mm%3d30%26mn%3dsn-5hne6nlk%26ms%3dnxu%26mv%3du%26pl%3d32%26sc%3dyes%26ei%3dr4T6WJeRLpTtqgXN052oDw%26mime%3dvideo%2fmp4%26lmt%3d1490764756253437%26mt%3d1492812909%26ip%3d2a02%3a5060%3ac170%3a517%3a%3a3%26ipbits%3d0%26expire%3d1492827375%26sparams%3dip%2cipbits%2cexpire%2cid%2citag%2csource%2crequiressl%2cttl%2cmm%2cmn%2cms%2cmv%2cpl%2csc%2cei%2cmime%2clmt%26signature%3d25A9649A78AAF27979C72AF81B99063B771EC958.B8692E78BFF44E282E96783C7CA27FD3C10EED14%26key%3dck2%26app%3dexplorer'
    url = url.replace('%3a',':').replace('%2f','/')
    process.Play('TESTies',url,906,'','','','')
    if ADDON.getSetting('View_Type')=='Classic':
        classic_list()
    elif ADDON.getSetting('View_Type')=='IMDB':
        IMDB_list()
    elif ADDON.getSetting('View_Type')=='TV Shows':
		TV_Men()
    elif ADDON.getSetting('View_Type')=='Movies':
		Movie_Men()
    elif ADDON.getSetting('View_Type')=='Sport':
		sports()
    elif ADDON.getSetting('View_Type')=='Music':
		Music_Men()
    elif ADDON.getSetting('View_Type')=='Kids':
		Kids_Men()
    elif ADDON.getSetting('View_Type')=='24/7':
		twenty47()
    elif ADDON.getSetting('View_Type')=='Docs':
		docs()
    elif ADDON.getSetting('View_Type')=='Live':
		Live_Men()
    elif ADDON.getSetting('View_Type')=='Adult':
		Adult()
    elif ADDON.getSetting('View_Type')=='Menu':
		process.Menu('24/7','',38,'',FANART,'','')
		process.Menu('Documentaries','',39,'',FANART,'','')
		process.Menu('Kids','',33,'',FANART,'','')
		process.Menu('Live TV','',32,'',FANART,'','')
		process.Menu('Movies','',30,'',FANART,'','')
		process.Menu('Music','',34,'',FANART,'','')
		process.Menu('Sports','',40,'',FANART,'','')
		process.Menu('TV Shows','',31,'',FANART,'','')
		if Adult_Pass == Adult_Default:
			process.Menu('Adult','',37,'',FANART,'','')
		process.Menu('Add-on\'s','',35,'',FANART,'','')
		process.setView('movies', 'INFO')

def IMDB_list():
	process.Menu('TV Shows','',300,'','','','')
	process.Menu('Movies','',200,'','','','')
	process.Menu('Favourites','',10,'','','','')
	process.setView('movies', 'INFO')
		
def twenty47():
	from lib.pyramid import pyramid
	process.Menu('Origin 24/7 Cartoons','',812,ORIGIN_ICON,FANART,'','')
	pyramid.not_so_anon('Fido 24/7','[QT][LW][PD][QZ][WI][PD][AL][DE][SS][MW][FU][XU][WX][UR][YY][YZ][PD][LS][LS][XU][QZ][YO][BU][PD][OI][MW][UP][YZ][LW][YO][LS][XU][WX][PD][LS][LS][XU][QZ][YZ][XX][XW]-[XB][RJ][KW][PD][QZ][QZ][MW][JJ][UP][YZ][XX][XW][XB][RJ][KW][PD][QZ][QZ][MW][JJ][UP]Hope you enjoy the view',FIDO_ICON,FANART,'','','')
	process.Menu('Pyramid 24/7','http://tombraiderbuilds.co.uk/addon/tvseries/247shows/247shows.txt',1101,RAIDER_ICON,'','','')
	process.Menu('Supremacy 24/7','http://stephen-builds.uk/supremacy/24-7/24-7.txt',1101,'http://www.stephen-builds.co.uk/wizard/icon.png','','','')
	process.Random_play('Raiz TV - Play 10 Random Cartoons',1154,url='http://raiztv.co.uk/RaysRavers/list2/raiztv/kids/kidsrandom.txt',image=RAY_ICON,isFolder=False)
	
def docs():
	process.Menu('Raiz Documentaries','http://raiztv.co.uk/RaysRavers/list2/raiztv/doc/doc.txt',1101,RAY_ICON,'','','')
	process.Menu('Pyramid Documentaries','http://tombraiderbuilds.co.uk/addon/documentaries/documentaries.txt',1101,RAY_ICON,'','','')
	
def sports():
	process.Menu('Renegades Darts','',2150,RENEGADES_ICON,FANART,'','')
	process.Menu('DELIVERANCE','',1139,'https://3.bp.blogspot.com/-mRS8HrApaaY/WOI17mTddmI/AAAAAAAAXBo/CaxwCX7o47QZxaV6W1Qeff39ZyQjYuI5wCLcB/s1600/Deliverance%2BKodi%2B17%2B1.png',FANART,'','')
	process.Menu('BAMF Live Sports','http://genietvcunts.co.uk/bamffff/livesports.xml',1101,ORIGIN_ICON,FANART,'','')
	process.Menu('Origin Football Replays','',400,ORIGIN_ICON,FANART,'','')
	process.Menu('Today\'s Football','',1750,ICON,FANART,'','')
		
def Adult():
	process.Menu('Just For Him','',1400,NINJA_ICON,FANART,'','')
	process.Menu('Fido','http://fantazyrepo.uk/addonimages/fido.addon/Livetv/adult.xml',1101,FIDO_ICON,'','','')
	process.Menu('X Videos','',700,'https://pbs.twimg.com/profile_images/378800000578199366/cf160c1c86c13778a834bbade0c30e38.jpeg',FANART,'','')
	process.Menu('Porn Hub','',708,'http://cdimage.debian.org/mirror/addons.superrepo.org/v7/addons/plugin.video.pornhub/icon.png',FANART,'','')
	process.Menu('X Hamster','',714,'http://www.logospike.com/wp-content/uploads/2016/05/Xhamster_Logo_03.png',FANART,'','')
	process.Menu('Chaturbate','',720,'https://pbs.twimg.com/profile_images/671662441210753024/sE2tHWMB_400x400.png',FANART,'','')
	process.Menu('You Porn','',723,'http://www.ares-portal.com/wp-content/uploads/2016/12/plugin.video_.youporngay.png',FANART,'','')
	process.Menu('Red Tube','',730,'http://gosha-portal.pp.ua/1311/pic/redtube.png',FANART,'','')
	process.Menu('Tube 8','',738,'https://a3-images.myspacecdn.com/images03/1/cb9e1e694ca941abaf62f0026d18049f/300x300.jpg',FANART,'','')
	process.Menu('Thumbzilla','',745,'http://static.spark.autodesk.com/2013/02/14__13_53_32/data2cd61048-351b-4b48-bd9c-946e7e076b53Medium2.jpg',FANART,'','')
	process.Menu('XTube','',753,'https://pbs.twimg.com/profile_images/732348322044903425/xTK0J4Cz.jpg',FANART,'','')
	process.Menu('Eporner','',760,'http://kenny2u.org/wp-content/uploads/2016/09/icon-1.png',FANART,'','')
	process.Menu('YouJizz','',771,'https://pbs.twimg.com/profile_images/3332003625/23c080fbec17cfb45ca3fd40ec06afe1.png',FANART,'','')
	process.Menu('Spank Wire','',772,'http://kenny2u.org/wp-content/uploads/2016/09/icon-43.png',FANART,'','')
	process.Menu('4k','',758,'https://pbs.twimg.com/profile_images/700315084980035588/fZZO6Pf-.jpg',FANART,'','')
	process.Menu('VR','http://www.xvideos.com/?k=vr',701,'https://pbs.twimg.com/profile_images/741907565689217024/DByQczLO.jpg',FANART,'','')


def Movie_Men():
	process.Menu('Search','Movies',1501,'','','','')
	process.Menu('Recent Movies','',5,ICON,FANART,'','')
	process.Menu('4k','4k',36,'','','','')
	process.Menu('3D','3D',36,'','','','')
	process.Menu('1080p','1080p',36,'','','','')
	process.Menu('Other - Linked to add-on\'s menu as most have movies','Other',36,'','','','')

def Movie_Def(url):
	if url == '4k':
		from lib.pyramid import pyramid
		process.Menu('Silent Hunter 4k','http://silenthunter.srve.io/main/4k.xml',1101,SILENT_ICON,FANART,'','','')
		process.Menu('Pandora 4k','http://genietvcunts.co.uk/PansBox/ORIGINS/4Kmovies.php',426,PANDORA_ICON,'','','')
		process.Menu('Pyramid 4k','http://tombraiderbuilds.co.uk/addon/movies/uhd/uhd.txt',1101,RAIDER_ICON,'','','')
	elif url == '3D':
		process.Menu('Pandora 3D','http://genietvcunts.co.uk/PansBox/ORIGINS/hey3D.php',426,PANDORA_ICON,'','','')
		process.Menu('Pyramid 3D','http://tombraiderbuilds.co.uk/addon/movies/3d/3d.txt',1101,RAIDER_ICON,'','','')
	elif url == '1080p':
		process.Menu('Pandora 1080p','http://genietvcunts.co.uk/PansBox/ORIGINS/hey1080p.php',426,PANDORA_ICON,'','','')
	elif url == 'Other':
		classic_list()


def TV_Men():
	process.Menu('Search','TV',1501,'','','','')
	process.Menu('Latest Episodes','',3,ICON,FANART,'','')
	from lib.pyramid import pyramid
	process.Menu('Pandora\'s TV','http://genietvcunts.co.uk/PansBox/ORIGINS/tvcats.php',423,PANDORA_ICON,'','','')
	process.Menu('Cerberus TV','http://roguemedia.x10.mx/cerberus/add-on/tvmenu.php',2301,REAPER_ICON,'','','')
	pyramid.not_so_anon('Pyramid TV','[QT][WI][XU][BU][ID][SS][PD][YO][LS][MW][SS][ID][UR][YO][JJ][LS][UP][WX][RJ][XU][WX][UR][YY][YZ][PD][LS][LS][XU][QZ][YZ][WI][FA][UP][MW][SS][YO][MW][UP][YZ][WI][FA][AL][XU][QZ][MW][BU][PD][YO][QZ]Have a nice day now',RAIDER_ICON,FANART,'','','')
	process.Menu('Tigen\'s TV','http://kodeeresurrection.com/TigensWorldtxt/TvShows/Txts/OnDemandSub.txt',1101,TIGEN_ICON,'','','')
	process.Menu('Raiz TV','http://raiztv.co.uk/RaysRavers/list2/raiztv/tv/tv.txt',1101,RAY_ICON,'','','')
	process.Menu('Dojo TV','http://herovision.x10host.com/dojo/tvshows/tvshows.php',2300,DOJO_ICON,'','','')
	process.Menu('BAMF\'s Classics','http://genietvcunts.co.uk/bamffff/bamfoldtv.xml',1101,BAMF_ICON,FANART,'','')

def Live_Men():
	process.Menu('Search','Live TV',1501,'','','','')
	process.Menu('TV Guide','',2200,ICON,FANART,'','')
	from lib.pyramid import pyramid
	process.Menu('Oblivion IPTV','',1129,OBLIVION_ICON,FANART,'','')
	process.Menu('BAMF IPTV','http://genietvcunts.co.uk/bamffff/BAMF.xml',1101,BAMF_ICON,FANART,'','')
	pyramid.not_so_anon('Pyramid Live','[QT][WI][XU][BU][ID][SS][PD][YO][LS][MW][SS][ID][UR][YO][JJ][LS][UP][WX][RJ][XU][WX][UR][YY][YZ][PD][LS][LS][XU][QZ][YZ][UR][YY][MW][QZ][WI][MW][SS][WI][PD][YO][QZ][BU][MW][QZ][WI][YZ][UR][YY][MW][QZ][WI][MW][SS][WI][PD][YO][QZ][BU][MW][QZ][WI]Have a nice day now',RAIDER_ICON,FANART,'','','')
	process.Menu('Ultra Live',base64.decodestring('aHR0cDovL3VsdHJhdHYubmV0MTYubmV0L2lwdHZzZXJ2ZXIvcG9ydGFsLnhtbA=='),1101,ULTRA_ICON,'','','')
	pyramid.not_so_anon('Fido Live','[QT][LW][PD][QZ][WI][PD][AL][DE][SS][MW][FU][XU][WX][UR][YY][YZ][PD][LS][LS][XU][QZ][YO][BU][PD][OI][MW][UP][YZ][LW][YO][LS][XU][WX][PD][LS][LS][XU][QZ][YZ]L[YO][FA][MW][WI][FA][YZ][JJ][YO][FA][MW][WI][FA]Hope you enjoy the view',FIDO_ICON,FANART,'','','')
	process.Menu('FreeView - [COLORred]VPN required if you are outside UK[/COLOR]','',1200,FREEVIEW_ICON,FANART,'','')
	process.Menu('Lily Sports Live','http://kodeeresurrection.com/LILYSPORTStxts/home.txt',1101,'http://kodeeresurrection.com/LILYSPORTS/plugin.video.LILYSPORTS/icon.png','','','')
	process.Menu('Supremacy Live','http://stephen-builds.uk/supremacy/LiveTV/live.txt',1101,'http://www.stephen-builds.co.uk/wizard/icon.png','','','')

def Kids_Men():
	process.Menu('Search','cartoon',1501,'','','','')
	from lib.pyramid import pyramid
	process.Menu('Tigen\'s World','',1143,TIGEN_ICON,FANART,'','')
	process.Menu('Raiz Kids','http://raiztv.co.uk/RaysRavers/list2/raiztv/kids/kidsmain.txt',1101,RAY_ICON,'','','')
	process.Menu('Origin Kids','',800,ORIGIN_ICON,ORIGIN_FANART,'','')
	process.Menu('Oblivion Kids','http://pastebin.com/raw/Y8X1vCaV',1101,OBLIVION_ICON,'','','')
	pyramid.not_so_anon('Pyramid Kids','[QT][WI][XU][BU][ID][SS][PD][YO][LS][MW][SS][ID][UR][YO][JJ][LS][UP][WX][RJ][XU][WX][UR][YY][YZ][PD][LS][LS][XU][QZ][YZ][YY][YO][LS][UP][RJ][KW][PD][QZ][QZ][MW][JJ][UP][YZ][YY][YO][LS][UP][RJ][KW][PD][QZ][QZ][MW][JJ][UP]Have a nice day now',RAIDER_ICON,FANART,'','','')
	process.Menu('BAMF\'s Kids','http://genietvcunts.co.uk/bamffff/lfk.xml',1101,BAMF_ICON,'','','')
	process.Menu('Supremacy Kids Live','http://stephen-builds.uk/supremacy/Kids%20Tv/Kids%20Tv.txt',1101,'http://www.stephen-builds.co.uk/wizard/icon.png','','','')
	process.Menu('Brettus Anime','',1600,BRETTUS_ICON,FANART,'','')

	

def Music_Men():
	process.Menu('Search','',1503,'','','','')
	from lib.pyramid import pyramid
	process.Menu('Quicksilver Music','',1133,QUICK_ICON,'','','')
	process.Menu('Rays Ravers','',1147,RAY_ICON,'','','')
	pyramid.not_so_anon('Fido Live Music','[QT][LW][PD][QZ][WI][PD][AL][DE][SS][MW][FU][XU][WX][UR][YY][YZ][PD][LS][LS][XU][QZ][YO][BU][PD][OI][MW][UP][YZ][LW][YO][LS][XU][WX][PD][LS][LS][XU][QZ][YZ]M[UR][UP][YO][RJ][YZ]M[UR][UP][YO][RJ]Hope you enjoy the view',FIDO_ICON,FANART,'','','')
	process.Menu('Tigen\'s World','',1143,TIGEN_ICON,FANART,'','')
	pyramid.not_so_anon('Pyramid\'s Music','[QT][WI][XU][BU][ID][SS][PD][YO][LS][MW][SS][ID][UR][YO][JJ][LS][UP][WX][RJ][XU][WX][UR][YY][YZ][PD][LS][LS][XU][QZ][YZ][BU][UR][UP][YO][RJ][YZ][BU][UR][UP][YO][RJ]Have a nice day now',RAIDER_ICON,FANART,'','','')
	process.Menu('Pandora\'s Music','http://genietvcunts.co.uk/PansBox/ORIGINS/seasonmusic.php',423,PANDORA_ICON,'','','')
	process.Menu('BAMF\'s Music','http://genietvcunts.co.uk/bamffff/bamfsmusic.xml',1101,BAMF_ICON,'','','')

def classic_list():
		if ADDON.getSetting('Origin')=='true':
			process.Menu('Origin','',4,ORIGIN_ICON,FANART,'','')
		if ADDON.getSetting('Pandoras_Box')=='true':
			process.Menu('Pandora\'s Box','',900,PANDORA_ICON,FANART,'','')
		if ADDON.getSetting('Pyramid')=='true':
			process.Menu('Pyramid','',1100,RAIDER_ICON,FANART,'','')
		if ADDON.getSetting('Freeview')=='true':
			process.Menu('FreeView - [COLORred]VPN required if you are outside UK[/COLOR]','',1200,FREEVIEW_ICON,FANART,'','')
		if ADDON.getSetting('Brettus_Anime')=='true':
			process.Menu('Brettus Anime','',1600,BRETTUS_ICON,FANART,'','')
		if ADDON.getSetting('Oblivion')=='true':
			process.Menu('Oblivion IPTV','',1129,OBLIVION_ICON,FANART,'','')
		if ADDON.getSetting("Tigen's_World")=='true':
			process.Menu('Tigen\'s World','',1143,TIGEN_ICON,FANART,'','')
		if ADDON.getSetting('Supremacy')=='true':
			process.Menu('Supremacy','',1131,'http://www.stephen-builds.co.uk/wizard/icon.png',FANART,'','')
		if ADDON.getSetting('Renegades')=='true':
			process.Menu('Renegades Darts','',2150,RENEGADES_ICON,FANART,'','')
		if ADDON.getSetting('Just_For_Him')=='true':
			process.Menu('Just For Him','',1400,NINJA_ICON,FANART,'','')
		if ADDON.getSetting('BAMF')=='true':
			process.Menu('BAMF IPTV','',1132,BAMF_ICON,FANART,'','')
		if ADDON.getSetting('Quicksilver')=='true':
			process.Menu('Quicksilver Music','',1133,QUICK_ICON,'','','')
		if ADDON.getSetting('Rays_Ravers')=='true':
			process.Menu('Rays Ravers','',1147,RAY_ICON,'','','')
		if ADDON.getSetting('Silent_Hunter')=='true':
			process.Menu('Silent Hunter','',1134,SILENT_ICON,'','','')
		if ADDON.getSetting('Dojo')=='true':
			process.Menu('Dojo Streams','http://herovision.x10host.com/dojo/main.php',2300,DOJO_ICON,'','','')
		if ADDON.getSetting('Cerberus')=='true':
			process.Menu('Cerberus','http://roguemedia.x10.mx/cerberus/add-on/mainmenu.php',2301,REAPER_ICON,'','','')
		if ADDON.getSetting('Ultra')=='true':
			process.Menu('Ultra IPTV','',1145,ULTRA_ICON,'','','')
		if ADDON.getSetting('Fido')=='true':
			process.Menu('Fido','',1146,FIDO_ICON,'','','')
		if ADDON.getSetting('Midnight')=='true':
			process.Menu('Midnight Society','',1156,MIDNIGHT_IMAGE,FANART,'','')
		if ADDON.getSetting('Deliverance')=='true':
			process.Menu('DELIVERANCE','',1139,'https://3.bp.blogspot.com/-mRS8HrApaaY/WOI17mTddmI/AAAAAAAAXBo/CaxwCX7o47QZxaV6W1Qeff39ZyQjYuI5wCLcB/s1600/Deliverance%2BKodi%2B17%2B1.png',FANART,'','')
		process.setView('movies', 'MAIN')
		

def bagotricks():
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
    process.Menu('TV Schedule','http://www.tvmaze.com/calendar',6,ICON,FANART,'','')

def Recent_Movies():
    process.Menu('Pandora Recent Movies','http://genietvcunts.co.uk/PansBox/ORIGINS/recentmovies.php',426,PANDORA_ICON,FANART,'','')
    process.Menu('Pyramid Recent Movies','http://tombraiderbuilds.co.uk/addon/movies/New%20Releaes/newreleases.txt',1101,RAIDER_ICON,FANART,'','')
    process.Menu('Supremacy Recent Movies','https://simplekore.com/wp-content/uploads/file-manager/steboy11/New%20Releases/New%20Releases.txt',1101,'http://www.stephen-builds.co.uk/wizard/icon.png',FANART,'','')


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
	if 'COLOR' in name:
		name = re.compile('- (.+?)>').findall(str(name)+'>')
		for name in name:
			name = name
	dp =  xbmcgui.DialogProgress()
	dp.create('Checking for stream')
	from lib import search
	search.TV(name)





def Origin_Main():
    process.Menu('Movies','',200,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('TV Shows','',300,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Sports Replays','',2100,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('Cartoons','',800,ORIGIN_ICON,ORIGIN_FANART,'','')
    process.Menu('AudioBooks','',600,ORIGIN_ICON,ORIGIN_FANART,'','')
    if Adult_Pass == Adult_Default:
        process.Menu('Porn','',707,ORIGIN_ICON,ORIGIN_FANART,'','')

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
elif mode == 13: bagotricks()
elif mode == 19: from lib import Live;Live.Live_Menu()
elif mode == 20: from lib import Live;Live.Live_Main()
elif mode == 21: from lib import Live;Live.Get_Channel(url)
elif mode == 22: from lib import Live;Live.Get_Playlink(name,url)
elif mode == 23: from lib import Live;Live.Ultra()
elif mode == 24: from lib import Live;Live.Get_Ultra_Channel(url)
elif mode == 25: from lib import Live;Live.Search_Ultra()
elif mode == 26: from lib import Live;Live.Check_For_200_Response()
elif mode == 27: from lib import Live;Live.search_checked()
elif mode == 30: Movie_Men()
elif mode == 31: TV_Men()
elif mode == 32: Live_Men()
elif mode == 33: Kids_Men()
elif mode == 34: Music_Men()
elif mode == 35: classic_list()
elif mode == 36: Movie_Def(url)
elif mode == 37: Adult()
elif mode == 38: twenty47()
elif mode == 39: docs()
elif mode == 40: sports()
elif mode == 41: process.check_for_episode()
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
elif mode == 200: from lib import Movies;Movies.Movie_Main(url)
elif mode == 202 : from lib import Movies;Movies.Movie_Genre(url)
elif mode == 203 : from lib import Movies;Movies.IMDB_Grab(url)
elif mode == 204 : from lib import Movies;Movies.Check_Link(name,url,image)
elif mode == 205 : from lib import Movies;Movies.Get_playlink(url)
elif mode == 206 : from lib import Movies;Movies.IMDB_Top250(url)
elif mode == 207 : from lib import Movies;Movies.search_movies()
elif mode == 208 : from lib import Movies;Movies.movie_channels()
elif mode == 209 : from lib import Movies;Movies.split_for_search(extra)
elif mode == 300 : from lib import multitv;multitv.multiv_Main_Menu(url)
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
elif mode == 402: from lib import Football_Repeat;Football_Repeat.get_PLAYlink(name,url)
elif mode == 403: from lib import Football_Repeat;Football_Repeat.Football_Highlights()
elif mode == 404: from lib import Football_Repeat;Football_Repeat.FootballFixturesDay()
elif mode == 405: from lib import Football_Repeat;Football_Repeat.FootballFixturesGame(url,iconimage)
elif mode == 406: from lib import Football_Repeat;Football_Repeat.Prem_Table(url,extra)
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
elif mode == 420: from lib import Football_Repeat;Football_Repeat.FootballFixturesSingle(description);
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
elif mode == 707: from lib import xxx_vids;xxx_vids.Porn_Menu()
elif mode == 708: from lib import xxx_vids;xxx_vids.Porn_Hub()
elif mode == 709: from lib import xxx_vids;xxx_vids.get_video_item(url)
elif mode == 710: from lib import xxx_vids;xxx_vids.get_cat_item(url)
elif mode == 711: from lib import xxx_vids;xxx_vids.get_pornhub_playlinks(url)
elif mode == 712: from lib import xxx_vids;xxx_vids.get_pornstar(url)
elif mode == 713: from lib import xxx_vids;xxx_vids.search_pornhub()
elif mode == 714: from lib import xxx_vids;xxx_vids.XHamster()
elif mode == 715: from lib import xxx_vids;xxx_vids.hamster_cats(url)
elif mode == 716: from lib import xxx_vids;xxx_vids.get_hamster_vid(url)
elif mode == 717: from lib import xxx_vids;xxx_vids.chaturbate_tags(url)
elif mode == 718: from lib import xxx_vids;xxx_vids.hamster_cats_split(name,url)
elif mode == 719: from lib import xxx_vids;xxx_vids.get_hamster_playlinks(url)
elif mode == 720: from lib import xxx_vids;xxx_vids.chaturbate()
elif mode == 721: from lib import xxx_vids;xxx_vids.chaturbate_videos(url)
elif mode == 722: from lib import xxx_vids;xxx_vids.chaturbate_playlink(url)
elif mode == 723: from lib import xxx_vids;xxx_vids.YouPorn()
elif mode == 724: from lib import xxx_vids;xxx_vids.youporn_new_video(url)
elif mode == 725: from lib import xxx_vids;xxx_vids.youporn_video(url)
elif mode == 726: from lib import xxx_vids;xxx_vids.youporn_collections(url)
elif mode == 727: from lib import xxx_vids;xxx_vids.youporn_categories(url)
elif mode == 728: from lib import xxx_vids;xxx_vids.youporn_playlink(url)
elif mode == 729: from lib import xxx_vids;xxx_vids.search_youporn(url)
elif mode == 730: from lib import xxx_vids;xxx_vids.redtube()
elif mode == 731: from lib import xxx_vids;xxx_vids.redtube_video(url)
elif mode == 732: from lib import xxx_vids;xxx_vids.redtube_playlink(url)
elif mode == 733: from lib import xxx_vids;xxx_vids.redtube_channels(url)
elif mode == 734: from lib import xxx_vids;xxx_vids.redtube_pornstars(url)
elif mode == 735: from lib import xxx_vids;xxx_vids.redtube_collections(url)
elif mode == 736: from lib import xxx_vids;xxx_vids.redtube_cats(url)
elif mode == 737: from lib import xxx_vids;xxx_vids.redtube_search(url)
elif mode == 738: from lib import xxx_vids;xxx_vids.tube8()
elif mode == 739: from lib import xxx_vids;xxx_vids.tube8_videos(url)
elif mode == 740: from lib import xxx_vids;xxx_vids.tube8_playlink(url)
elif mode == 741: from lib import xxx_vids;xxx_vids.tube8_cats(url)
elif mode == 742: from lib import xxx_vids;xxx_vids.tube8_tags(url)
elif mode == 743: from lib import xxx_vids;xxx_vids.tube8_search()
elif mode == 744: from lib import xxx_vids;xxx_vids.tube8_letters(name,url)
elif mode == 745: from lib import xxx_vids;xxx_vids.thumbzilla()
elif mode == 746: from lib import xxx_vids;xxx_vids.thumbzilla_videos(url)
elif mode == 747: from lib import xxx_vids;xxx_vids.thumbzilla_tags(url)
elif mode == 748: from lib import xxx_vids;xxx_vids.thumbzilla_pornstars(url)
elif mode == 749: from lib import xxx_vids;xxx_vids.thumbzilla_cats(url)
elif mode == 750: from lib import xxx_vids;xxx_vids.thumbzilla_search()
elif mode == 751: from lib import xxx_vids;xxx_vids.thumbzilla_tags_letters(name,url)
elif mode == 752: from lib import xxx_vids;xxx_vids.thumbzilla_playlink(url)
elif mode == 753: from lib import xxx_vids;xxx_vids.xtube()
elif mode == 754: from lib import xxx_vids;xxx_vids.xtube_videos(url)
elif mode == 755: from lib import xxx_vids;xxx_vids.xtube_cats(url)
elif mode == 756: from lib import xxx_vids;xxx_vids.xtube_search(url)
elif mode == 757: from lib import xxx_vids;xxx_vids.xtube_playlink(url)
elif mode == 758: from lib import xxx_vids;xxx_vids.fourK()
elif mode == 759: from lib import xxx_vids;xxx_vids.eporner_playlink(url)
elif mode == 760: from lib import xxx_vids;xxx_vids.eporner()
elif mode == 761: from lib import xxx_vids;xxx_vids.eporner_video(url)
elif mode == 762: from lib import xxx_vids;xxx_vids.eporner_pornstar(url)
elif mode == 763: from lib import xxx_vids;xxx_vids.eporner_cats(url)
elif mode == 764: from lib import xxx_vids;xxx_vids.eporner_search()
elif mode == 765: from lib import xxx_vids;xxx_vids.youjizz_videos(url)
elif mode == 766: from lib import xxx_vids;xxx_vids.youjizz_tags(url)
elif mode == 767: from lib import xxx_vids;xxx_vids.youjizz_pornstars(url)
elif mode == 768: from lib import xxx_vids;xxx_vids.youjizz_search()
elif mode == 769: from lib import xxx_vids;xxx_vids.youjizz_playlink(url)
elif mode == 770: from lib import xxx_vids;xxx_vids.youjizz_tags_letters(name,url)
elif mode == 771: from lib import xxx_vids;xxx_vids.youjizz()
elif mode == 772: from lib import xxx_vids;xxx_vids.spank_wire()
elif mode == 773: from lib import xxx_vids;xxx_vids.spank_cats(url)
elif mode == 774: from lib import xxx_vids;xxx_vids.spank_tags(url)
elif mode == 775: from lib import xxx_vids;xxx_vids.spank_videos(url)
elif mode == 776: from lib import xxx_vids;xxx_vids.spank_search()
elif mode == 777: from lib import xxx_vids;xxx_vids.spank_playlink(url)
elif mode == 778: from lib import xxx_vids;xxx_vids.spank_tags_letter(name,url)
elif mode == 800: from lib import Big_Kids;Big_Kids.Big_Kids_Main_Menu()
elif mode == 801: from lib import Big_Kids;Big_Kids.TESTCATS()
elif mode == 802: from lib import Big_Kids;Big_Kids.Search_cartoons()
elif mode == 803: from lib import Big_Kids;Big_Kids.LISTS(url)
elif mode == 804: from lib import Big_Kids;Big_Kids.LISTS2(url,iconimage)
elif mode == 805: process.Resolve(url)
elif mode == 806: from lib import Big_Kids;Big_Kids.watch_cartoon_menu()
elif mode == 807: from lib import Big_Kids;Big_Kids.watch_cartoon_grab_episode(url)
elif mode == 808: from lib import Big_Kids;Big_Kids.watch_cartoon_final(url)
elif mode == 809: from lib import Big_Kids;Big_Kids.watch_cartoon_grab_movies(url)
elif mode == 810: from lib import Big_Kids;Big_Kids.watch_cartoon_grab_episode_second(url)
elif mode == 811: from lib import Big_Kids;Big_Kids.Search_movies()
elif mode == 812: from lib import Big_Kids;Big_Kids.Random_Lists()
elif mode == 813: from lib import Big_Kids;Big_Kids.Random_Cartoon(url)
elif mode == 814: from lib import Big_Kids;Big_Kids.Random_Movie(url)
elif mode == 816: from lib import Big_Kids;Big_Kids.Random_Play_Cartoon(url,name)
elif mode == 817: from lib import Big_Kids;Big_Kids.twenty47_select()
elif mode == 818: from lib import Big_Kids;Big_Kids.Search_247()
elif mode == 900: from lib import Pandora;Pandora.Pandora_Main()
elif mode == 901: from lib import Pandora;Pandora.Pandoras_Box(url)
elif mode == 902: from lib import Pandora;Pandora.open_normal(name,url,iconimage,fanart,description)
elif mode == 423: from lib import Pandora;Pandora.open_Menu(url)
elif mode == 426: from lib import Pandora;Pandora.Pandora_Menu(url)
elif mode == 903: from lib import Pandora;Pandora.Search_Menu()
elif mode == 904: from lib import Pandora;Pandora.Search_Pandoras_Films()
elif mode == 905: from lib import Pandora;Pandora.Search_Pandoras_TV()
elif mode == 906: process.Big_Resolve(name,url)
elif mode == 907: from lib import Pandora;Pandora.Pans_Resolve(name,url)
elif mode == 1100: from lib.pyramid import pyramid;pyramid.SKindex();xbmcplugin.endOfDirectory(int(sys.argv[1]))
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
    if 'google' in url:
        import urlresolver
        resolved = urlresolver.resolve(url)
        item = xbmcgui.ListItem(path=resolved)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    elif not url.startswith("plugin://plugin") or not any(x in url for x in pyramid.g_ignoreSetResolved):#not url.startswith("plugin://plugin.video.f4mTester") :
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
elif mode == 1128: from lib.pyramid import pyramid;pyramid.SKindex_Joker();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1129: from lib.pyramid import pyramid;pyramid.SKindex_Oblivion();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1130: from lib.pyramid import pyramid;pyramid.GetSublinks(name,url,iconimage,fanart)
elif mode == 1131: from lib.pyramid import pyramid;pyramid.SKindex_Supremacy();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1132: from lib.pyramid import pyramid;pyramid.SKindex_BAMF();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1133: from lib.pyramid import pyramid;pyramid.SKindex_Quicksilver();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1134: from lib.pyramid import pyramid;pyramid.SKindex_Silent();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1135: from lib.pyramid import pyramid;pyramid.WizHDMenu(url,iconimage,fanart);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1136: from lib.pyramid import pyramid;pyramid.Wiz_Get_url(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1137: from lib.pyramid import pyramid;pyramid.scrape();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1138: from lib.pyramid import pyramid;pyramid.scrape_link(name,url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1139: from lib.pyramid import pyramid;pyramid.SKindex_deliverance();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1140: from lib.pyramid import pyramid;pyramid.SearchChannels();pyramid.SetViewThumbnail();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1141: from lib.pyramid import pyramid;pyramid.Search_input(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1142: from lib.pyramid import pyramid;pyramid.RESOLVE(url)
elif mode == 1143: from lib.pyramid import pyramid;pyramid.SKindex_TigensWorld();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1144: from lib.pyramid import pyramid;pyramid.queueItem();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1145: from lib.pyramid import pyramid;pyramid.SKindex_Ultra();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1146: from lib.pyramid import pyramid;pyramid.SKindex_Fido();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1147: from lib.pyramid import pyramid;pyramid.SKindex_Rays();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1153: from lib.pyramid import pyramid;pyramid.pluginquerybyJSON(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1154: from lib.pyramid import pyramid;pyramid.get_random(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1156: from lib.pyramid import pyramid;pyramid.SKindex_Midnight();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1200: from lib.freeview import freeview;freeview.CATEGORIES()
elif mode == 1201: from lib.freeview import freeview;freeview.play(url)
elif mode == 1202: from lib.freeview import freeview;freeview.tvplayer(url)
elif mode == 1400 : from lib import ninja;ninja.CATEGORIES()
elif mode == 1401 : from lib import ninja;ninja.VIDEOLIST(url)
elif mode == 1402 : from lib import ninja;ninja.PLAYVIDEO(url)
elif mode == 1500 : from lib import search;search.Search_Menu()
elif mode == 1501 : from lib import search;search.Search_Input(name,url,extra)
elif mode == 1502 : from lib import search;search.MUSIC(Search_name,url)
elif mode == 1503 : from lib import search;search.Music_Search()
elif mode == 1504 : from lib import search;search.Clear_Search(url)
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
elif mode == 2100 : from lib import Sports_Replays;Sports_Replays.Sports_Repeats()
elif mode == 2101 : from lib import Sports_Replays;Sports_Replays.Motor_Replays(url)
elif mode == 2102 : from lib import Sports_Replays;Sports_Replays.motor_name(url)
elif mode == 2103 : from lib import Sports_Replays;Sports_Replays.motor_race(extra)
elif mode == 2104 : from lib import Sports_Replays;Sports_Replays.motor_single(name,extra)
elif mode == 2105 : from lib import Sports_Replays;Sports_Replays.F1_Replays(url)
elif mode == 2106 : from lib import Sports_Replays;Sports_Replays.F1_page(url)
elif mode == 2107 : from lib import Sports_Replays;Sports_Replays.F1_items(url,iconimage)
elif mode == 2108 : from lib import Sports_Replays;Sports_Replays.F1_Playlink(url)
elif mode == 2150 : from lib import renegades;renegades.run()
#elif mode == 2151 : import plugintools;plugintools.add_item(mode,name,url,iconimage,fanart)
elif mode == 2200 : from lib import tv_guide;tv_guide.TV_GUIDE_MENU()
elif mode == 2201 : from lib import tv_guide;tv_guide.whatsoncat()
elif mode == 2202 : from lib import tv_guide;tv_guide.whatson(url)
elif mode == 2203 : from lib import tv_guide;tv_guide.search_split(extra)
elif mode == 2204 : from lib import tv_guide;tv_guide.TV_GUIDE_CO_UK_CATS()
elif mode == 2205 : from lib import tv_guide;tv_guide.tvguide_co_uk(url)
elif mode == 2206 : from lib import tv_guide;tv_guide.WhatsOnCOUK(url,extra)
elif mode == 2207 : from lib import tv_guide;tv_guide.Select_Type()
elif mode == 2300 : DOJO_MAIN(url)
elif mode == 2301 : Reaper_Loop(url)
elif mode == 2350 : google_index_search()
elif mode == 10000: from lib import youtube_regex;youtube_regex.Youtube_Grab_Playlist_Page(url)
elif mode == 10001: from lib import youtube_regex;youtube_regex.Youtube_Playlist_Grab(url)
elif mode == 10002: from lib import youtube_regex;youtube_regex.Youtube_Playlist_Grab_Duration(url)
elif mode == 10003: from lib import yt;yt.PlayVideo(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
