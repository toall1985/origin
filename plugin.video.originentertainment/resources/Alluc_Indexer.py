import urllib,urllib2, re, os, sys, HTMLParser, control
from bs4 import BeautifulSoup
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
Dialog = xbmcgui.Dialog()

def Resolve(name, url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass

def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

  
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def addDir4(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def Search_Alluc():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Name = Search_Name.lower()
    #Search_Name = Search_Name.replace(' ', '%22')
    search_URL = 'http://www.alluc.ee/stream/' + (Search_Name).replace (' ','+') + 'host%3Aallmyvideos.net'
    HTML = OPEN_URL(search_URL)
    match = re.compile('<div class="title"><!--<h2>--><a href="(.+?)"   title=".+?" >(.+?)</a>',re.DOTALL).findall(HTML)
    for url,name in match:
	    addDir4(name,'http://alluc.ee' + url,91,'')#wlist search result


def Get_Alluc_Page(url,name):# get first page
    HTML = OPEN_URL(url)
    match = re.compile('<iframe src="(.+?)" frameborder=0 marginwidth=0 marginheight=0 scrolling=no allowfullscreen').findall(HTML)
    for url in match:
		Get_Playlink(url,name)
		
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

def Get_Playlink(url,name): # get play url
    HTML = OPEN_URL(url)
    match = re.compile('"file" : "(.+?)",').findall(HTML)
    for url in match:
        Resolve(name, url)
