import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import urlresolver
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2,urllib, glob
import re
import extract
import downloader
import plugintools
import zipfile
import time
import ntpath
import cookielib
from urllib2 import urlopen
from cookielib import CookieJar
from addon.common.addon import Addon
from addon.common.net import Net
 

###THANK YOU TO THE PEOPLE THAT ORIGINALY WROTE SOME OF THIS CODE "STUART DENTON, PIPCAN, MIKEY1234, WHUFCLEE" TO NAME A FEW, WITHOUT YOU I STILL PROBABLY WOULDNT HAVE A CLUE WHERE TO START###


USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
addon_id = 'plugin.video.GenieTv'
EXCLUDES     = ['plugin.video.GenieTv','script.module.addon.common']
ADDON = xbmcaddon.Addon(id=addon_id)
MEDIA = xbmc.translatePath('special://home/media')
AddonID='plugin.video.GenieTv'
dp =  xbmcgui.DialogProgress()
AddonTitle="[COLORgreen]GenieTv[/COLOR]" 
net = Net()
MyBuild = ADDON.getSetting('Build')
MyLocal = ADDON.getSetting('Local')
U = ADDON.getSetting('User')
dialog = xbmcgui.Dialog()
HOME = xbmc.translatePath('special://home/')
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png',FANART,''))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
VERSION = "1.0.10"
DBPATH = xbmc.translatePath('special://database')
TNPATH = xbmc.translatePath('special://thumbnails');
PATH = "GenieTv"            
BASEURL = "http://architects.x10host.com"
H = 'http://'
localizedString = ADDON.getLocalizedString
cookieJar = CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
urlOpener.addheaders = [('User-Agent', 'Mozilla/5.0')]

def AddTVSHOWDir(name, url, mode, iconimage, description="", isFolder=True, background=None):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)

	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
	if background:
		liz.setProperty('fanart_image', background)
	if mode == 1 or mode == 2:
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10008).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=22)'.format(sys.argv[0], urllib.quote_plus(url)))])
	elif mode == 404:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
	elif mode == 556:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10010).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
		
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def Add_Directory_Item(handle, url, listitem, isFolder):

    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder) 



def ParseURL(url): 
    response = urlOpener.open(url).read()
        
    try:
        Titles = re.findall(r'<a .*?>(.*?)</a>',response)
        Links = re.findall(r'<a.*?href="(.*?)">',response)
            
        for link in Links:
            if '.gif' in link:
                pass
            if '.srt' in link:
                pass
            elif '..' in link:
                pass
            elif '.txt' in link:
                pass
            elif '.nfo' in link:
                pass
            elif '.jpg' in link:
                pass
            elif '1-Irani/' in link:
                pass
            elif 'index.php' in link:
                pass
            elif '.png' in link:
                pass
            elif '?C=M&O=D' in link:
                pass
            elif '?C=M&O=A' in link:
                pass
            elif '?C=N&O=D' in link:
                pass
            elif '?C=N&O=A' in link:
                pass
            elif '?C=S&O=A' in link:
                pass
            elif '?C=S&O=D' in link:
                pass
            elif '?C=N;O=D' in link:
                pass
            elif '?C=M;O=A' in link:
                pass
            elif '?C=S;O=A' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif 'Torrent' in link:
                pass
            elif 'exe' in link:
                pass
            elif 'public' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif 'pub' in link:
                pass
            elif 'install' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif '.m3u' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif 'mpeg' in link:
                pass
            elif '.doc' in link:
                pass
            elif '.html' in link:
                pass
            else:
                name = link
                if 'txt' in name:
                    pass
                if '_ir' in name:
                    name = name.replace ('_ir', '')
                if '%20%5b%5bWwW.Max-Movie.In%5d%5d' in name:
                    name = name.replace ('%20%5b%5bWwW.Max-Movie.In%5d%5d', '')
                if 'download' in name:
                    name = name.replace ('download', '')
                if '[' in name:
                    name = name.replace ('[', '')
                if ']' in name:
                    name = name.replace (']', '')
                if 'Ir' in name:
                    name = name.replace ('Ir', '')
                if 'Downloado' in name:
                    name = name.replace ('Downloado', '')
                if 'Nightsdl' in name:
                    name = name.replace ('Nightsdl', '')
                if 'farvardin' in name:
                    name = name.replace ('farvardin', 'LIST 1')
                if 'khordad' in name:
                    name = name.replace ('khordad', 'LIST 2')
                if 'Max-Movie.In' in name:
                    name = name.replace ('Max-Movie.In', '')
                if 'ordibehesht' in name:
                    name = name.replace ('ordibehesht', 'LIST 3')
                if 'flv' in name:
                    name = name.replace ('flv', '')
                if 'FazMusic' in name:
                    name = name.replace ('FazMusic', '')
                if 'parsfilm' in name:
                    name = name.replace ('parsfilm', '')
                if 'YIFY' in name:
                    name = name.replace ('YIFY', '')
                if 'bruce v' in name:
                    name = name.replace ('bruce v', 'bruce willis')
                if '.avi' in name:
                    name = name.replace ('.avi', '')
                if 'ParsFilm' in name:
                    name = name.replace ('ParsFilm', '')
                if 'INTERNAL' in name:
                    name = name.replace ('INTERNAL', '')
                if 'rmvb' in name:
                    name = name.replace ('rmvb', '')
                if 'HDTV' in name:
                    name = name.replace ('HDTV', '')
                if 'XviD-LOL' in name:
                    name = name.replace ('XviD-LOL', '')
                if 'x264-LOL' in name:
                    name = name.replace ('x264-LOL', '')
                if 'X264-DIMENSION' in name:
                    name = name.replace ('X264-DIMENSION', '')
                if 'Farsimovie' in name:
                    name = name.replace ('Farsimovie', '')
                if 'mp4' in name:
                    name = name.replace ('mp4', '')
                if 'mkv' in name:
                    name = name.replace ('mkv', '')
                if '%20' in name:
                    name = name.replace ('%20', ' ')
                if '%5bVTV%5d' in name:
                    name = name.replace ('%5bVTV%5d', ' ')
                if 'DeeJayAhmed' in name:
                    name = name.replace ('DeeJayAhmed', '')
                if '-' in name:
                    name = name.replace ('-', '')
                if '1Ch' in name:
                    name = name.replace ('1Ch', '')
                if 'BluRay' in name:
                    name = name.replace ('BluRay', '')
                if 'ReEnc' in name:
                    name = name.replace ('ReEnc', '')
                if '/' in name:
                    name = name.replace('/', ' ')
                if 'Movie_ORG' in name:
                    name = name.replace('Movie_ORG', ' ')
                if 'Film2' in name:
                    name = name.replace('Film2', ' ')
                if 'Movie_INFO' in name:
                    name = name.replace('Movie_INFO', ' ')
                if 'x265' in name:
                    name = name.replace('x265', ' ')
                if 'HEVC' in name:
                    name = name.replace('HEVC', ' ')
                if 'net' in name:
                    name = name.replace('net', ' ')
                if '5B' in name:
                    name = name.replace('5B', ' ')
                if 'Movie' in name:
                    name = name.replace('Movie', ' ')
                if 'halfOU' in name:
                    name = name.replace('halfOU', ' ')
                if 'FardaDownload' in name:
                    name = name.replace('FardaDownload', ' ')
                if 'SpicyHunt' in name:
                    name = name.replace('SpicyHunt', ' ')
                if 'Com' in name:
                    name = name.replace('Com', ' ')
                if 'ClearSound' in name:
                    name = name.replace('ClearSound', ' ')
                if 'Farsi' in name:
                    name = name.replace('Farsi', ' ')
                if '_' in name:
                    name = name.replace('_', ' ')
                if '5D' in name:
                    name = name.replace('5D', ' ')
                if 'Ash61' in name:
                    name = name.replace('Ash61', ' ')
                if 'ash61' in name:
                    name = name.replace('ash61', ' ')
                if '28' in name:
                    name = name.replace('28', ' ')
                if '29' in name:
                    name = name.replace('29', ' ')
                if '&amp;' in name:
                    name = name.replace('&amp;', ' ')
                if '%5b2007%5d' in name:
                    name = name.replace('%5b2007%5d', ' ')
                if '%5b2006%5d%5b' in name:
                    name = name.replace('%5b2006%5d%5b', ' ')
                if 'MovIran' in name:
                    name = name.replace('MovIran', ' ')
                if 'filmuha' in name:
                    name = name.replace('filmuha', ' ')
                if 'Ozlem' in name:
                    name = name.replace('Ozlem', ' ')
                if 'nItRo' in name:
                    name = name.replace('nItRo', ' ')
                if 'COM' in name:
                    name = name.replace('COM', ' ')
                if 'AACETRG' in name:
                    name = name.replace('AACETRG', ' ')
                if 'Filmgir' in name:
                    name = name.replace('Filmgir', ' ')
                if 'ShAaNiG' in name:
                    name = name.replace('ShAaNiG', ' ')
                if 'FILMIHA' in name:
                    name = name.replace('FILMIHA', ' ')
                if 'DL' in name:
                    name = name.replace('DL', ' ')
                if 'Ganool' in name:
                    name = name.replace('Ganool', ' ')
                if '%5b' in name:
                    name = name.replace('%5b', ' ')
                if '%5d' in name:
                    name = name.replace('%5d', ' ')
                if 'x264' in name:
                    name = name.replace('x264', ' ')
                if 'CHD' in name:
                    name = name.replace('CHD', ' ')
                if 'sample' in name:
                    name = name.replace('sample', ' ')
                if 'DVDSCR' in name:
                    name = name.replace('DVDSCR', ' ')
                if 'DVDRip' in name:
                    name = name.replace('DVDRip', ' ')
                if '%d0' in name:
                    name = name.replace('%d0', ' ')
                if '%92' in name:
                    name = name.replace('%92', ' ')
                if '%b3' in name:
                    name = name.replace('%b3', ' ')
                if '%d1' in name:
                    name = name.replace('%d1', ' ')
                if '%be' in name:
                    name = name.replace('%be', ' ')
                if '%81' in name:
                    name = name.replace('%81', ' ')
                if '%82' in name:
                    name = name.replace('%82', ' ')
                if '%8f' in name:
                    name = name.replace('%8f', ' ')
                if '%94' in name:
                    name = name.replace('%94', ' ')
                if '%83' in name:
                    name = name.replace('%83', ' ')
                if '%85' in name:
                    name = name.replace('%85', ' ')
                if '%93' in name:
                    name = name.replace('%93', ' ')
                if '%80' in name:
                    name = name.replace('%80', ' ')
                if '%b4' in name:
                    name = name.replace('%b4', ' ')
                if '%bd' in name:
                    name = name.replace('%bd', ' ')
                if '%b0' in name:
                    name = name.replace('%b0', ' ')
                if '%9e' in name:
                    name = name.replace('%9e', ' ')
                if '%8b' in name:
                    name = name.replace('%8b', ' ')
                if '%84' in name:
                    name = name.replace('%84', ' ')
                if '%b8' in name:
                    name = name.replace('%b8', ' ')
                if '%bb' in name:
                    name = name.replace('%bb', ' ')
                if '%86' in name:
                    name = name.replace('%86', ' ')
                if '%8c' in name:
                    name = name.replace('%8c', ' ')
                if '%b9' in name:
                    name = name.replace('%b9', ' ')
                if '%ba' in name:
                    name = name.replace('%ba', ' ')
                if '%9a' in name:
                    name = name.replace('%9a', ' ')
                if '%9d' in name:
                    name = name.replace('%9d', ' ')
                if '.' in name:
                    name = name.replace('.', ' ')
                if 'mp3' in name:
                    name = name.replace('mp3', ' ')
                if '(' in name:
                    name = name.replace('(', ' ')
                if ')' in name:
                    name = name.replace(')', ' ')
                if 'DivX' in name:
                    name = name.replace('DivX', ' ')
                if 'Filmiha' in name:
                    name = name.replace('Filmiha', ' ')
                if 'com' in name:
                    name = name.replace('com', ' ')
                if 'filmiha' in name:
                    name = name.replace('filmiha', ' ')
                if 'XViD' in name:
                    name = name.replace('XViD', ' ')
                if 'WEB' in name:
                    name = name.replace('WEB', ' ')
                if 'AC3MAJESTIC' in name:
                    name = name.replace('AC3MAJESTIC', ' ')
                if 'anoXmous_' in name:
                    name = name.replace('anoXmous', ' ')
                if 'juggs' in name:
                    name = name.replace('juggs', ' ')
                if 'GECKOS' in name:
                    name = name.replace('GECKOS', ' ')
                if 'AMIABLE' in name:
                    name = name.replace('AMIABLE', ' ')
                if 'tuvideo' in name:
                    name = name.replace('tuvideo', ' ')
                if 'matiasmx' in name:
                    name = name.replace('matiasmx', ' ')
                if 'farsimovie' in name:
                    name = name.replace('farsimovie', ' ')
                if 'info' in name:
                    name = name.replace('info', ' ')
                if 'REMUX' in name:
                    name = name.replace('REMUX', ' ')
                if 'DTSHD' in name:
                    name = name.replace('DTSHD', ' ')
                if 'MA' in name:
                    name = name.replace('MA', ' ')
                if '1PublicHD' in name:
                    name = name.replace('1PublicHD', ' ')
                if 'AC3EVE' in name:
                    name = name.replace('AC3EVE', ' ')
                if 'LTRG' in name:
                    name = name.replace('LTRG', ' ')
                if 'FarsiMovie' in name:
                    name = name.replace('FarsiMovie', ' ')
                if 'Net' in name:
                    name = name.replace('Net', ' ')
                if '%' in name:
                    name = name.replace('%', ' ')
                if 'png' in name:
                    name = name.replace('png', ' ')
                if 'wmv' in name:
                    name = name.replace('wmv', ' ')

                if '.mkv' in link or '.m4B' in link or '.m4v' in link or '.mp3' in link or '.mp4' in link or '.avi' in link or '.flv' in link or '.mpeg' in link or '.3gp' in link or '.divx' in link or '.strm' in link:
                    AddTVSHOWDir('[COLORgreen]'+name+'[/COLOR]', url+link, 222, ART+'VOD.png', 'GenieTv does not host or distribute any of the content displayed by this addon. GenieTV does not have any affiliation with the content provider.', isFolder=False)
					
                else:
					AddTVSHOWDir(name, url+link, 1006, ART+'VOD.png', '', isFolder=True)
                    

                

    except Exception, e:
                print str(e)        


def addonParseURL(url): 
    response = urlOpener.open(url).read()
        
    try:
        Titles = re.findall(r'<a .*?>(.*?)</a>',response)
        Links = re.findall(r'<a.*?href="(.*?)">',response)
            
        for link in Links:
            if '.gif' in link:
                pass
            if '.srt' in link:
                pass
            elif '..' in link:
                pass
            elif '.txt' in link:
                pass
            elif '.nfo' in link:
                pass
            elif '.jpg' in link:
                pass
            elif '.png' in link:
                pass
            elif '+ currentPath +' in link:
                pass
            elif '+  currentPath +' in link:
                pass
            elif '#' in link:
                pass
            elif '?C=N&O=A' in link:
                pass
            elif '?C=M&O=D' in link:
                pass
            elif '?C=S&O=D' in link:
                pass
            elif '?C=N&O=D' in link:
                pass
            elif '?C=M&O=A' in link:
                pass
            elif '?C=S&O=A' in link:
                pass
            elif '?C=D&O=A' in link:
                pass
            elif 'Torrent' in link:
                pass
            elif 'exe' in link:
                pass
            elif 'public' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif 'pub' in link:
                pass
            elif 'install' in link:
                pass
            elif '?C=D&O=A' in link:
                pass
            elif '?C=D&O=A' in link:
                pass
            elif '.m3u' in link:
                pass
            elif '?C=D&O=A' in link:
                pass
            elif 'mpeg' in link:
                pass
            elif '.doc' in link:
                pass
            elif '.html' in link:
                pass
            else:
                name = link
                if 'txt' in name:
                    pass
                if '/' in name:
                    name = name.replace ('/', '')
                if '_ir' in name:
                    name = name.replace ('_ir', '')

                if '.zip' in link:
                    AddTVSHOWDir(name, url+link, 42, ART+'ADDONS.png', 'GenieTv does not host or distribute any of the content displayed by this addon. GenieTV does not have any affiliation with the content provider.', isFolder=False)
					
                else:
					AddTVSHOWDir(name, url+link, 2030, ART+'ADDONS.png', '', isFolder=True)
                    

                

    except Exception, e:
                print str(e)     
				
def apkParseURL(url): 
    response = urlOpener.open(url).read()
        
    try:
        Titles = re.findall(r'<a .*?>(.*?)</a>',response)
        Links = re.findall(r'<a.*?href="(.*?)">',response)
            
        for link in Links:
            if '.rar' in link:
                pass
            if '.zip' in link:
                pass
            if '.gif' in link:
                pass
            if '.srt' in link:
                pass
            elif '..' in link:
                pass
            elif '.txt' in link:
                pass
            elif '.nfo' in link:
                pass
            elif '.jpg' in link:
                pass
            elif '.png' in link:
                pass
            elif '+ currentPath +' in link:
                pass
            elif '+  currentPath +' in link:
                pass
            elif '#' in link:
                pass
            elif '?C=N&O=A' in link:
                pass
            elif '?C=M&O=D' in link:
                pass
            elif '?C=S&O=D' in link:
                pass
            elif '?C=N&O=D' in link:
                pass
            elif '?C=M&O=A' in link:
                pass
            elif '?C=S&O=A' in link:
                pass
            elif '?C=D&O=A' in link:
                pass
            elif '?C=N;O=A' in link:
                pass
            elif '?C=M;O=D' in link:
                pass
            elif '?C=S;O=D' in link:
                pass
            elif '?C=N;O=D' in link:
                pass
            elif '?C=M;O=A' in link:
                pass
            elif '?C=S;O=A' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif 'Torrent' in link:
                pass
            elif 'exe' in link:
                pass
            elif 'public' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif 'pub' in link:
                pass
            elif 'install' in link:
                pass
            elif '?C=D&O=A' in link:
                pass
            elif '?C=D&O=A' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif '.m3u' in link:
                pass
            elif 'mpeg' in link:
                pass
            elif '.doc' in link:
                pass
            elif '.html' in link:
                pass
            else:
                name = link
                if 'txt' in name:
                    pass
                if '/' in name:
                    name = name.replace ('/', '')
                if '_MeliDL' in name:
                    name = name.replace ('_MeliDL', '')
                if 'Download' in name:
                    name = name.replace ('Download', '')
                if 'com' in name:
                    name = name.replace ('com', '')
                if '.' in name:
                    name = name.replace ('.', ' ')
                if '_' in name:
                    name = name.replace ('_', '')
                if 'Meli' in name:
                    name = name.replace ('Meli', '')
                if 'apk' in name:
                    name = name.replace ('apk', '')
                if 'android' in name:
                    name = name.replace ('android', '')
                if '%20' in name:
                    name = name.replace ('%20', '')
                if '%' in name:
                    name = name.replace ('%', '')
                if 'android' in name:
                    name = name.replace ('android', '')
                if 'rar' in name:
                    name = name.replace ('rar', '')

                if '.apk' in link:
                    AddTVSHOWDir(name+'[COLORgold]APK[/COLOR]', url+link, 19, ART+'APK.png', 'GenieTv does not host or distribute any of the content displayed by this addon. GenieTV does not have any affiliation with the content provider.', isFolder=False)
					
                else:
					AddTVSHOWDir(name, url+link, 2031, ART+'APK.png', '', isFolder=True)
                    

                

    except Exception, e:
                print str(e)     
				
