import urllib, urllib2, re, cookielib ,sys, xbmc, xbmcgui, xbmcplugin, xbmcaddon, os
from urllib2 import urlopen
from cookielib import CookieJar
import base64


ADDON_ID = 'plugin.video.originentertainment'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL =base64.decodestring('aHR0cDovL3dhdGNoLXNpbXBzb25zLmNvbS9kb3dubG9hZHMv')
cookieJar = CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
urlOpener.addheaders = [('User-Agent', 'Mozilla/5.0')]
localizedString = ADDON.getLocalizedString

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

                if '.mkv' in link or '.mp3' in link or '.mp4' in link or '.avi' in link:
                    AddTVSHOWDir(name, url+link, 404, '', '', isFolder=False)
					
                else:
					AddTVSHOWDir(name, url+link, 402, '', '', isFolder=True)
                    

                

    except Exception, e:
                print str(e)        

