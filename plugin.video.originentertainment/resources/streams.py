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
                if '.' in name:
                    name = name.replace('.', ' ')

                if '.mkv' in link or '.mp3' in link:
                    mode = 'Mode: Link'
                else:
                    mode = 'Mode: Folder'

                print mode
                print name
                print url+link
                print '\n'

    except Exception, e:
                print str(e)        

