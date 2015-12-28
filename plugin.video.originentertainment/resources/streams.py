import urllib, urllib2, re, cookielib ,sys, xbmc, xbmcgui, xbmcplugin, xbmcaddon, os
from urllib2 import urlopen
from cookielib import CookieJar
import base64
import sys
import urlparse
import yt
import time
import urllib,urllib2,re,base64,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import urlresolver
from t0mm0.common.net import Net

addon_id='plugin.video.originentertainment'
ADDON_ID = 'plugin.video.originentertainment'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL =base64.decodestring('aHR0cDovL3dhdGNoLXNpbXBzb25zLmNvbS9kb3dubG9hZHMv')
cookieJar = CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
urlOpener.addheaders = [('User-Agent', 'Mozilla/5.0')]
localizedString = ADDON.getLocalizedString
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Origin Entertainment"
VERSION = "1.0.1"
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART 		=  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
net = Net()

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
            elif '..' in link:
                pass
            elif '.txt' in link:
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
            elif '?C=D;O=A' in link:
                pass
            elif 'mpeg' in link:
                pass
            elif 'dubleh' in link:
                pass
            elif 'Ablah' in link:
                pass
            elif 'Armaghan' in link:
                pass
            elif 'Bible' in link:
                pass
            elif 'Hashieh' in link:
                pass
            elif 'Das' in link:
                pass
            elif 'Enghelabe' in link:
                pass
            elif 'Eshgh' in link:
                pass
            elif 'Galbe' in link:
                pass
            elif 'Gallipoli' in link:
                pass
            elif 'Kolah' in link:
                pass
            elif 'Madar' in link:
                pass
            elif 'Paay' in link:
                pass
            elif 'Poldark' in link:
                pass
            elif 'Sakh' in link:
                pass
            elif 'Shabhaye' in link:
                pass
            elif 'Shahriar' in link:
                pass
            elif 'Shokhi' in link:
                pass
            elif 'Shirin' in link:
                pass
            elif 'Umbre' in link:
                pass
            elif 'Vaziat' in link:
                pass
            elif 'Veep' in link:
                pass
            elif 'poorang' in link:
                pass
            elif 'shaam' in link:
                pass
            elif 'Nenok' in link:
                pass
            elif 'Raja' in link:
                pass
            elif 'BAJRANGI' in link:
                pass
            elif 'BHAAG' in link:
                pass
            elif 'Baahubali' in link:
                pass
            elif 'Bayou' in link:
                pass
            elif 'Badlapur' in link:
                pass
            elif 'Bajrangi' in link:
                pass
            elif 'Bakshy' in link:
                pass
            elif 'Dhadakne' in link:
                pass
            elif 'Haisha' in link:
                pass
            elif 'Drishyam' in link:
                pass
            elif 'Gabbar' in link:
                pass
            elif 'Gopala' in link:
                pass
            elif 'Hamari' in link:
                pass
            elif 'Hawaizaada' in link:
                pass
            elif 'Heneral' in link:
                pass
            elif 'Batti' in link:
                pass
            elif 'Kisko' in link:
                pass
            elif 'Ecume' in link:
                pass
            elif 'Luokkakokous' in link:
                pass
            elif 'Manijhi' in link:
                pass
            elif 'Masaan' in link:
                pass
            elif 'Masala' in link:
                pass
            elif 'Heneral' in link:
                pass
            elif 'Hindi' in link:
                pass
            elif 'Premam' in link:
                pass
            elif 'Pyaar' in link:
                pass
            elif 'Rammstein' in link:
                pass
            elif 'Sardaar' in link:
                pass
            elif 'Shamitabh' in link:
                pass
            elif 'filmiha' in link:
                pass
            elif 'Nayanthara' in link:
                pass
            elif 'Vaalu' in link:
                pass
            elif 'Damascus' in link:
                pass
            elif 'Playlist 1' in link:
                pass
            elif 'Playlist 2' in link:
                pass
            elif 'Playlist 4' in link:
                pass
            else:
                name = link
                if 'txt' in name:
                    pass
                if 'HDTV' in name:
                    name = name.replace ('HDTV', '')
                if 'XviD-LOL' in name:
                    name = name.replace ('XviD-LOL', '')
                if 'x264-LOL' in name:
                    name = name.replace ('x264-LOL', '')
                if 'X264-DIMENSION' in name:
                    name = name.replace ('X264-DIMENSION', '')
                if '720p' in name:
                    name = name.replace ('720p', '')
                if 'avi' in name:
                    name = name.replace ('avi', '')
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
                if 'Film2Movie_ORG' in name:
                    name = name.replace('Film2Movie_ORG', ' ')
                if 'Film2Movie_INFO' in name:
                    name = name.replace('Film2Movie_INFO', ' ')
                if 'x265' in name:
                    name = name.replace('x265', ' ')
                if 'HEVC' in name:
                    name = name.replace('HEVC', ' ')
                if '&amp;' in name:
                    name = name.replace('&amp;', ' ')
                if '%5b2007%5d' in name:
                    name = name.replace('%5b2007%5d', ' ')
                if '%5b2006%5d%5b' in name:
                    name = name.replace('%5b2006%5d%5b', ' ')
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
                if '2012' in name:
                    name = name.replace('2012', ' ')
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
                if 'FarsiMovie' in name:
                    name = name.replace('FarsiMovie', ' ')
                if 'Net' in name:
                    name = name.replace('Net', ' ')
                if '2BG' in name:
                    name = name.replace('2BG', ' ')
                if '24_' in name:
                    name = name.replace('24_', ' ')
                if '%5BFarsimovie%5D' in name:
                    name = name.replace('%5BFarsimovie%5D', ' ')
                if '_ORG' in name:
                    name = name.replace('_ORG', ' ')
                if 'info' in name:
                    name = name.replace('info', ' ')
                if 'ShAaNiG' in name:
                    name = name.replace('ShAaNiG', ' ')
                if 'Ganool' in name:
                    name = name.replace('Ganool', ' ')
                if 'fILMIHA' in name:
                    name = name.replace('fILMIHA', ' ')
                if 'COM' in name:
                    name = name.replace('COM', ' ')
                if 'FILMIHA' in name:
                    name = name.replace('FILMIHA', ' ')
                if 'YIFY' in name:
                    name = name.replace('YIFY', ' ')
                if 'WEBDL' in name:
                    name = name.replace('WEBDL', ' ')
                if 'WEBrip' in name:
                    name = name.replace('WEBrip', ' ')
                if 'AACETRG' in name:
                    name = name.replace('AACETRG', ' ')
                if 'Filmgir' in name:
                    name = name.replace('Filmgir', ' ')
                if 'DesiSCR' in name:
                    name = name.replace('DesiSCR', ' ')
                if 'Rip' in name:
                    name = name.replace('Rip', ' ')
                if 'DVDRip' in name:
                    name = name.replace('DVDRip', ' ')
                if 'XviD' in name:
                    name = name.replace('XviD', ' ')
                if 'MP3' in name:
                    name = name.replace('MP3', ' ')
                if 'HDrip' in name:
                    name = name.replace('HDrip', ' ')
                if 'mSD' in name:
                    name = name.replace('mSD', ' ')
                if 'TinyMoviez' in name:
                    name = name.replace('TinyMoviez', ' ')
                if 'Copy' in name:
                    name = name.replace('Copy', ' ')
                if 'DVDrip' in name:
                    name = name.replace('DVDrip', ' ')
                if 'AACETRG' in name:
                    name = name.replace('AACETRG', ' ')
                if 'AC3EVO' in name:
                    name = name.replace('AC3EVO', ' ')
                if 'X264' in name:
                    name = name.replace('X264', ' ')
                if 'AC3ETRG' in name:
                    name = name.replace('AC3ETRG', ' ')
                if 'uNkNoWn' in name:
                    name = name.replace('uNkNoWn', ' ')
                if 'Xvid' in name:
                    name = name.replace('Xvid', ' ')
                if 'UnKnOwN' in name:
                    name = name.replace('UnKnOwN', ' ')
                if 'net%5D' in name:
                    name = name.replace('net%5D', ' ')
                if '%5B' in name:
                    name = name.replace('%5B', ' ')
                if 'HiveCM8' in name:
                    name = name.replace('HiveCM8', ' ')
                if 'HDTS' in name:
                    name = name.replace('HDTS', ' ')
                if 'XVID' in name:
                    name = name.replace('XVID', ' ')
                if '%7b2015%7d' in name:
                    name = name.replace('%7b2015%7d', ' ')
                if 'AC3MRG' in name:
                    name = name.replace('AC3MRG', ' ')
                if 'filmuha' in name:
                    name = name.replace('filmuha', ' ')
                if 'Familha' in name:
                    name = name.replace('Familha', ' ')
                if 'www' in name:
                    name = name.replace('www', ' ')
                if 'torentz' in name:
                    name = name.replace('torentz', ' ')
                if '3xforum' in name:
                    name = name.replace('3xforum', ' ')
                if '%7b2009%7d' in name:
                    name = name.replace('%7b2009%7d', ' ')
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
                if 'Filmia' in name:
                    name = name.replace('Filmia', ' ')
                if '98Music' in name:
                    name = name.replace('98Music', ' ')
                if 'DL' in name:
                    name = name.replace('DL', ' ')
                if 'Bluray' in name:
                    name = name.replace('Bluray', ' ')
                if 'Web' in name:
                    name = name.replace('Web', ' ')

                if '.mkv' in link or '.mp3' in link or '.mp4' in link or '.avi' in link or '.flv' in link or '.divx' in link:
                    AddTVSHOWDir(name, url+link, 404,ART + 'icon.png', 'The author neither hosts or stores any content, the author has no affiliation with content hosts', isFolder=False)
					
                else:
					AddTVSHOWDir(name, url+link, 402, '', '', isFolder=True)
                    

                

    except Exception, e:
                print str(e)        