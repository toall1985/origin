'''
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

'''

import sys
import urlparse
import yt
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup, BeautifulSOAP
try:
    import json
except:
    import simplejson as json
import time
import requests
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
from resources import streams,lists,utube,TV,Standup,Films,premierleague,Google,client,CNF_Studio_Indexer,Alluc_Indexer,FootballReplays,SoapsCatchup,documentary
from resources import M3Uscrape, search_addon, SEO_INFO
from resources.lib.parsers import TVParser
from datetime import datetime

Decode = base64.decodestring
BASE2= lists.BASE2
BASE3= lists.BASE3
BASE4= lists.BASE4
BASE5= lists.BASE5
BASE6= lists.BASE6
BASE7= lists.BASE7
CAT=lists.CAT
BASE = lists.BASE
addon_id='plugin.video.originentertainment'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Origin Entertainment"
VERSION = "1.0.1"
IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'

ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
net = Net()
HD_URLS = []
SD_URLS = []
Play_URLS = []
ADDON = xbmcaddon.Addon(id=addon_id)
GetAdultPassword = ADDON.getSetting('Password')
AdultURL = Decode('aHR0cDovL2JhY2syYmFzaWNzLngxMGhvc3QuY29tL0FkdWx0L2luZGV4LnBocD9tb2RlPVh4WCZwYXNzd29yZD0=')
AdultFinalURL = AdultURL + GetAdultPassword
TOKEN_URL = Decode('aHR0cDovL2lkYS5vbXJvZXAubmwvbnBvcGxheWVyL2kuanM=')
Article_Cache = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + addon_id + 'Article_Dump.txt'))


addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), addon_id)
if not os.path.exists(addon_data_dir):
        os.makedirs(addon_data_dir)

tmpListFile = os.path.join(addon_data_dir, 'tempList.txt')

#def ChangeLog():
#    TextBoxes('Change Log, Future Plans and General Info', ' [CR] ---------------------------------------------------------------------------------------------------------- [CR]Going to look at adding TV guide to new live tv streams [CR] ---------------------------------------------------------------------------------------------------------- [CR]Hoping to get search function in soon to make things easier to find [CR] ---------------------------------------------------------------------------------------------------------- [CR]Am thinking of making a second release of the addon once my knowledge grows to tidy things up a bit [CR] ---------------------------------------------------------------------------------------------------------- [CR]11/12/15 Fixed Scraper, still need to work on some streams not playing [CR] ---------------------------------------------------------------------------------------------------------- [CR]Massive thanks and respect to Chris for all his help lately helping me push forwards [CR] ---------------------------------------------------------------------------------------------------------- [CR]Also to Jay, Damian and Sponge head for being here from the start and of course Team H20 [CR] ---------------------------------------------------------------------------------------------------------- [CR]Will look at adding a music section once search function in and working properly [CR] ---------------------------------------------------------------------------------------------------------- [CR]Fixes Needed - Scraper streams not working. Newspaper Article and Prem League table windows not working on android  ')



def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def Home_Menu():

#    addDir4('Change Log','',1000,ART+'ChangeLog.png')
    addList('24/7 Shows',BASE+'24-7'+CAT,400,ART + '24shows.png')
    addDir('Lists','',53,ART + 'lists.png',ART + 'background.png','')
    addDir('Live TV','',41,ART + 'livetv.png',ART + 'background.png','')
    addDir('M3U8 Lists','',54,ART + 'm3u8.png',ART + 'background.png','')
    addDir('Movies','',10,ART + 'movies.png',ART + 'background.png','')
    addDir('News','',72,ART + 'News2.png',ART + 'background.png','')
    addDir('Pandoras Box','',55,ART + 'pandorasbox.png',ART + 'background.png','')
    addDir('Radio','',63,ART + 'radio.png',ART + 'background.png','')	
    addDir('Scraper','',76,ART + 'scraper.png',ART + 'background.png','')	
    addDir('Search','',175,ART + 'search.png',ART + 'background.png','')
    addDir('Seo Guides','',186,ART + 'icon.png', ART + 'background.png','')
    addDir('Sports','',64,ART + 'sports.png',ART + 'background.png','')
    addDir('Stand Up','',12,ART + 'comedy.png',ART + 'background.png','') 
    addDir('Test Area','',52,ART + 'testarea.png',ART + 'background.png','')
    addDir('TV Guide','',69,ART + 'tvguide.png',ART + 'background.png','')
    addDir('TV Shows','',11,ART + 'tv.png',ART + 'background.png','')	
    addList('World Cams',BASE+'worldcams'+CAT,400,ART + 'worldcams.png')
    if GetAdultPassword == Decode('Zm9yZGZpZXN0YQ=='):
        addList('Adult Movies',AdultFinalURL,400,ART + 'icon.png')
	
	
def Sports():

    addDir('Football','',57,ART + 'icon.png',ART + 'background.png','')
    addDir('Sports Channels','',86,ART + 'icon.png',ART + 'background.png','')

    
    xbmcplugin.endOfDirectory(addon_handle)

	
def Radiocountry():

    html=OPEN_URL(Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw=='))
    match = re.compile('<tr>.+?<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(html)
    for url,name in match:
			    addList((name).replace('email me','').replace('External services',''),Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1LyVz')%url,62,ART + 'icon.png')

	
def Radio(url):

    html=OPEN_URL(url)
    match = re.compile('<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">',re.DOTALL).findall(html)
    for name,url in match:
		addDir4(name,url,401,ART + 'icon.png')


def Football():
	addList('Fixtures','',58,ART + 'icon.png')
#	addDir4('Premier League Table','',75,ART+'icon.png')
	addDir3('Replays','',93,ART+'icon.png')

############################################################### PANDORAS SECTION ######################################################################################################

	
#elif mode == 423 	: open_Menu(url)
#elif mode == 426 	: Pandora_Menu(url)


	
def Pandoras_Box():

    html=OPEN_URL(Decode('aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA=='))
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
            addDirPand2(name,url,mode,img,fanart,desc)

def Pandora_Menu(url):
        
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,desc,background,name in match:
            addDirPand(name,url,401,iconimage,background,desc)

            setView('tvshows', 'Media Info 3')			
			
            xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

			
def open_Menu(url):

    html=OPEN_URL(url)
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
            addDirPand2(name,url,mode,img,fanart,desc)

    setView('tvshows', 'Media Info 3')			

			
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def addDirPand(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDirPand2(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
	
	
############################################################### PANDORAS SECTION ######################################################################################################	
	
def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)

	
    
def M3u8Lists():

    addList('List 1','',411,ART + 'icon.png')
    addList('List 2','',413,ART + 'icon.png')
    addList('List 3','',414,ART + 'icon.png')
    addList('List 4','',415,ART + 'icon.png')
    addList('List 5','',416,ART + 'icon.png')
#    addDir('Multi Lists',Decode('aHR0cDovL2ljaGkxMzQubmV0MTYubmV0L0lQVFYv'),418,ART + 'icon.png',ART + 'background.png','')

def Test():

    addList('Test Area',BASE+'test'+CAT,400,ART + 'icon.png')
    addList('Sponge Test',BASE5+'badlands'+CAT,400,ART + 'icon.png')
    addList('Dizilab Scraper Test','',410,ART + 'icon.png')
	

    xbmcplugin.endOfDirectory(addon_handle)
    
    
 
    
def addDir(name,url,mode,iconimage,fanart,description): 
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==5 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        
        return ok


def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir4(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
'''       
def Parsem3uURL(url): 
    response = urlOpener.open(url).read()
        
    try:
        Titles = re.findall(r'<a .*?>(.*?)</a>',response)
        Links = re.findall(('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S),response)
'''

def M3UCATS():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u1.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
        addDir4(name,url,401,ART+'icon.png')

def M3UCATS2():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u2.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
       addDir4(name,url,401,ART+'icon.png')

def M3UCATS3():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u3.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
        addDir4(name,url,401,ART+'icon.png')

def M3UCATS4():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u4.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
        addDir4(name,url,401,ART+'icon.png')

def M3UCATS5():
    html=OPEN_URL('http://back2basics.x10host.com/back2basics/test/m3u5.m3u')
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(html)
    for var,name,url in match:
        addDir4(name,url,401,ART+'icon.png')
        
#elif mode == 58 	: FootballFixturesDay()
#elif mode == 59 	: FootballFixturesGame()
#elif mode == 60 	: FootballFixturesChannel()

def FootballFixturesDay():
    html=OPEN_URL(Decode('aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s'))
    match = re.compile('<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"',re.DOTALL).findall(html)
    for url,img,name in match:
        addDir3((name).replace('amp;',''),Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + url,59,Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + img)
		
def FootballFixturesGame(url):
    HTML = OPEN_URL(url)
    block = re.compile('AndClearL.+?><h2.+?head>(.*?)float',re.DOTALL).findall(HTML)
    for block in block:
        day = re.compile('(.*?)</h2>').findall(str(block))
        for Day in day:
            Day = Day
        game = re.compile('comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->',re.DOTALL).findall(str(block))
        for comp,img,time,chan in game:
            channel = re.compile(",CAPTION, '(.+?)&nbsp").findall(chan)
            addDirPand2(Day + ' - ' + comp + ' - ' + time,'',65,Decode('aHR0cDovL2xpdmVvbnNhdC5jb20=') + img,'',(str(channel)))

    setView('tvshows', 'Media Info 3')
		
def Guidemenu():

#    addDir('Interactive','',65,ART + 'tvguide.png',ART + 'background.png','')		
    addDir('Basic','',65,ART + 'tvguide.png',ART + 'background.png','')		
    addDir('Full','',71,ART + 'tvguide.png',ART + 'background.png','')
    addDir('Sky Basic','',70,ART + 'tvguide.png',ART + 'background.png','')
	

def whatsonsky():
    html=OPEN_URL('http://www.locatetv.com/uk/listings/sky')
    match = re.compile('<li>.+?<li class="channel" data-name="(.+?)">.+?<a href="(.+?)">.+?<img src="(.+?)" alt=".+?title="(.+?)" class',re.DOTALL).findall(html)
    for name,url,img,name2 in match:
        addDir3((name + ' - ' + name2).replace('&#039;s','').replace('&amp;', '&'),'http://www.locatetv.com' + url,'',img)
	

def whatsoncat():
    html=OPEN_URL('http://tvguideuk.telegraph.co.uk/')
    match = re.compile('<li class="tabs"><span><a href="(.+?)">(.+?)</a></span></li>').findall(html)
    for url,name in match:
        if 'amp;' in url:
	    url = url.replace ('amp;','')
        addDir3(name,'http://tvguideuk.telegraph.co.uk/' + url,65,'')
		
def Scraper():
    addDir('Site 1 Films','',77,ART + 'scraper.png',ART + 'background.png','')
    addDir('Search Alluc*in testing*','',90,ART + 'scraper.png', ART + 'background.png','')
    addDir('Scraped M3U8 Lists','',109,ART + 'scraper.png', ART + 'background.png','')
    addDir('IMDB Search','',106,ART + 'scraper.png', ART + 'background.png','')
#    addDir('Site 2 TV Shows','',81,ART + 'scraper.png',ART + 'background.png','')


def whatson(url):
    html=OPEN_URL(url)
    match = re.compile('<div class="channel_name">(.+?)<.+?channel_id=(.+?).+?>(.+?)</a>',re.DOTALL).findall(html)
    for name,id,whatson in match:
        addDir3(name + ' - ' + whatson,'',41,'')

def TESTMOVIE():
    html=OPEN_URL('')
    match = re.compile('<td><a href="(.+?)"><img src="(.+?)" width="100" height="100" border="0"><br>(.+?)</a></td>').findall(html)
    for url,img,name in match:
        addDir3(name,'',420,ART+'icon.png')

def Movie2(url):
    html=OPEN_URL(url)
    match = re.compile('',re.DOTALL).findall(html)
    for url,name,img in match:
        addDir3(name,url,421,'http://www.movietubenow.biz%s'%img)

def Movie3(url):
    html=OPEN_URL(url)
    match = re.compile('<iframe width="680" height="430" scrolling="no" frameborder="0" src="(.+?)"',re.DOTALL).findall(html)
    for url in match:
        addDir3(name,url,422,ART + 'icon.png')

def Movie4(url):
    html=OPEN_URL(url)
    match = re.compile('<source src="(.+?)" type="video/mp4"/>').findall(html)
    for url in match:
        addDir3(name,url,401,'')


def TESTCATS():
    html=OPEN_URL('http://www.animetoon.org/cartoon')
    match = re.compile('<td><a href="(.+?)">(.+)</a></td>').findall(html)
    for url,name in match:
        addDir3(name,url,407,ART+'icon.png')

def NewsCat():
    html=OPEN_URL('http://www.mirror.co.uk/')
    match = re.compile('<a href="(.+?)" data-type="section-head_.+?" data-action="section:.+?">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3((name).replace('amp;',''),url,73,ART+'icon.png')
        

def NewsStory(url):
    html=OPEN_URL(url)
    match = re.compile('<figure>.+?<img src="(.+?)" class="aboveHeadline .+?<a href="(.+?)".+?&#xa;(.+?)</a>',re.DOTALL).findall(html)
    for img,url,name in match:
        addDir4((name).replace('amp;','').replace('&#x3a','').replace('&#xa; </a>','').replace('&#xa;','').replace('&quot;','').replace('&#x27;',''),url,74,img)
        print '>>>>>>>>>>' + url        

		
def LISTS(url):
    html=OPEN_URL(url)
    match = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(name,url,408,ART+'icon.png')
        
def LISTS2(url):
    html=OPEN_URL(url)
    match = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html)
    for name,url in match:
        addDir3(name,url,409,ART+'icon.png')
        
def LISTS3(url):
    html=OPEN_URL(url)
    match = re.compile("url: '(.+?)',").findall(html)
    for url in match:
        addDir4('STREAM',url,401,ART+'icon.png')

def cnfTV():
    html=OPEN_URL('http://tvshows.cnfstudio.com/')
    match = re.compile('<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(name,'http://tvshows.cnfstudio.com/genre/' + url,82,ART+'icon.png')
        print '>>>>>>>>>>' + url

def cnfTVCat(url):
    html=OPEN_URL(url)
    match = re.compile('<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>',re.DOTALL).findall(html)
    prev = re.compile("<link rel='prev' href='(.+?)'/>").findall(html)
    next = re.compile("<link rel='next' href='(.+?)'/>").findall(html)
    for img,url,name in match:
        addDir3((name).replace('&#038;','').replace('&#8216;','').replace('&#8217;','').replace('&#8211;',''),url,83,img)
    prev=prev
    for url in prev:
        addDir3('Prev',url,82,'')
    next=next
    for url in next:
        addDir3('Next',url,82,'')

def cnfTVPlay(url):
    html=OPEN_URL(url)
    match = re.compile('<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>',re.DOTALL).findall(html)
    for url,episode,name in match:
        addDir4(('Season') + episode + ('  ') + name,url,100,ART+'icon.png')

def cnfHome():      
    html=OPEN_URL('http://cnfstudio.com/')
    match = re.compile('<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(name,'http://cnfstudio.com/genre/' + url,78,ART+'icon.png')
		
dialog = xbmcgui.Dialog()

def build_dialog(url):
	#Get_Page('',url,'')
	Part_No = 1
	Link_No = 0
	Get_NextURL = OPEN_URL(url)
	NextURL = re.compile('<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>',re.DOTALL).findall(Get_NextURL)
	for url in NextURL:
		#addDir3('DOUBLE LINK',url,424,'')
		try:
			url2 = Google.resolve(url)
		except:
			pass

		find_Links = re.findall(r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}", str(url2))
		for HD, SD in find_Links:
			
			HD_URLS.append(HD)
			SD_URLS.append(SD)
	

		addDir4('HD LINKS','','','')
		for link in HD_URLS:
			addDir4('Part ' + Part_No,HD_URLS[Link_No],100,'')
			Part_No = Part_No + 1
			Link_No = Link_No + 1
		
		Part_No = 0
		Link_No = 0
		addDir4('SD LINKS','','','')
		for link in SD_URLS:
			addDir4('Part ' + Part_No,SD_URLS[Link_No],100,'')
			Part_No = Part_No + 1
			Link_No = Link_No + 1
		
		Part_No = 0
		Link_No = 0

		
def cnfCat(url):
    html=OPEN_URL(url)
    match = re.compile('<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>',re.DOTALL).findall(html)
    prev = re.compile("<link rel='next' href='(.+?)'/>").findall(html)
    for img,url,name in match:
		addDir4((name).replace('&#038;','').replace('&#8216;','').replace('&#8217;','').replace('&#8211;',''),url,169,img)
    prev=prev
    for url in prev:
		addDir3('Next Page',url,79,'')
  



def cnfMovie(url):

    html=OPEN_URL(url)
    match = re.compile('<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>',re.DOTALL).findall(html)
    for url in match:
        link = url + '&fv=&sou='
        link = link.replace('player','watch')
        Play_URL = cnfPlay1(link)
        ResolvePlayURL = cnfPlay1(url)


def cnfPlay1(url):

    html=OPEN_URL(url)
    match = re.compile('<video id=".+?<source src="(.+?)" type="video/mp4">',re.DOTALL).findall(html)
    for url in match:
        Resolve(url)
		
		
def addVID(type,name,url,mode,iconimage = '',fanart = '',video = '',description = ''):
    if type != 'folder2' and type != 'addon':
        if len(iconimage) > 0:
            iconimage = ART + iconimage
        else:
            iconimage = 'DefaultFolder.png'
    if type == 'addon':
        if len(iconimage) > 0:
            iconimage = iconimage
        else:
            iconimage = 'http://totalxbmc.tv/addons/cache/images/4c79319887e240789ca125f144d989_addon-dummy.png'
    if fanart == '':
        fanart = FANART
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&video="+urllib.quote_plus(video)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
    liz.setProperty( "Fanart_Image", fanart )
    liz.setProperty( "Build.Video", video )
    if (type=='folder') or (type=='folder2') or (type=='tutorial_folder') or (type=='news_folder'):
        ok=Add_Directory_Item(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    else:
        ok=Add_Directory_Item(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def Add_Directory_Item(handle, url, listitem, isFolder):

    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder) 


def Get_Page(name, url, img):
    HTML = OPEN_URL(url)
    Page_Link = re.compile('<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>',re.DOTALL).findall(HTML)
    No_PageLinks = len(Page_Link)
    
    
    if No_PageLinks == 1:
        for PageLink in Page_Link:
            PageLink = PageLink.replace('player','watch')
            Resolve_Link = PageLink + '&fv=&sou='
            Resolve_Page = OPEN_URL(Resolve_Link)
            Resolved = re.compile('<source src="(.+?)" type=".+?">',re.DOTALL).findall(Resolve_Page)
            for Link in Resolved:
                isFolder=False
                Resolve(Link)
    
    elif No_PageLinks > 1:
        
        for PageLink in Page_Link:
            Get_NextURL = OPEN_URL(PageLink)
            NextURL = re.compile('<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>',re.DOTALL).findall(Get_NextURL)
            RT_Link = NextURL
            RT_Link = (str(RT_Link)).replace('[\'', '').replace('\']', '');
            print 'Stripped url : ' + RT_Link
            addDir4('DOUBLE LINK',RT_Link,424,'')
			
            for url in NextURL:
					addDir3('DOUBLE LINK',url,424,'')
					try:
						url2 = Google.resolve(url)
					except:
						pass
					try:
						find_Links = re.findall(r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}", str(url2))
						for HD, SD in find_Links:
							
							HD_URLS.append(HD)
							SD_URLS.append(SD)
					except:
						pass
    else:
        pass
	
	
'''
    print '~~~~~~~~~~ ITEM ~~~~~~~~~~'
    print 'HD Links'
    print 'Part 1 ' + HD_URLS[0]
    print 'Part 2 ' + HD_URLS[1]
    print 'SD Links'
    print 'Part 1 ' + SD_URLS[0]
    print 'Part 2 ' + SD_URLS[1]
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\n\n'
'''	
def OPEN_URL(url):
        req = urllib2.Request(url)
        IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
        FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
        IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
        ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def Live(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a.href="(.+?)".target="_blank"><img.src="(.+?)".style="max-width:200px;"./></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,name in match:
            addList3('%s'%(name).replace('Origin Entertainment','Origin Entertainment').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),401,'%s'%(iconimage))

        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
				
				
def Live2(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a.href="(.+?)".target="_blank"><img.src="(.+?)".style="max-width:200px;"./></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,name in match:
            addList2(name,url,402,iconimage)

        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);


def addMenu(url):
    
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
    menulocation=('%s%s'%(BASE,url))
    link = OPEN_URL(url)
    match=re.compile("addDir('','','','','','')").findall(link)

    
                
def Resolve(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('LOADING','Opening %s Now'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve() 
    if dp.iscanceled(): 
        print "[COLORred]STREAM CANCELLED[/COLOR]" # need to get this part working    
        dialog = xbmcgui.Dialog()
        if dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
	         return
    else:
        try: play.play(url)
        except: pass
        try: ADDON.resolve_url(url) 
        except: pass 
        dp.close()

def ResolveTwo(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
		
		
def addSearch():
    searchStr = ''
    keyboard = xbmc.Keyboard(searchStr, 'Search')
    keyboard.doModal()
    if (keyboard.isConfirmed()==False):
      return
    searchStr=keyboard.getText()
    if len(searchStr) == 0:
      return
    else:
      return searchStr
        
def TestPlayUrl(name, url, iconimage=None):
    print '--- Playing "{0}". {1}'.format(name, url)
    listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
    listitem.setInfo(type="Video", infoLabels={ "Title": name })
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
        
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
      
def addList(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addList2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addList3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok


def News_Article(name, url):
    req = OPEN_URL(url)
    soup = BeautifulSoup(req)
    Dump_Article = open(Article_Cache,'w')
    Heading = name

    Article_Body = soup.find_all('div', {'class': 'body'})
    for Article in Article_Body:
        Article_Paragraph = Article.find_all('p')
        for Paragraph in Article_Paragraph:
            Paragraph = Paragraph.text
            Paragraph = Paragraph.encode('utf-8')

            Write_Paragraph = open(Article_Cache,'a')
            Write_Paragraph.write(Paragraph)
            Write_Paragraph.write('\n')

        Get_Article = open(Article_Cache,'r')
        Read_Article = Get_Article.read()
        TextBoxes (Heading,Read_Article)
        Write_Paragraph.close()

def TextBoxes(heading,announce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    isFolder=True
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

        
def collect_token():
    req = urllib2.Request(TOKEN_URL)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()
    token = re.search(r'npoplayer.token = "(.*?)"',page).group(1)
    #xbmc.log("plugin.video.nederland24:: oldtoken: %s" % token)
    # site change, token invalid, needs to be reordered. Thanks to rieter for figuring this out very quickly.
    first = -1
    last = -1
    for i in range(5, len(token) - 5, 1):
	#xbmc.log("plugin.video.nederland24:: %s" % token[i])
        if token[i].isdigit():
            if first < 0:
                first = i
                #xbmc.log("plugin.video.nederland24:: %s" % token[i])
            elif last < 0:
                last = i
                #xbmc.log("plugin.video.nederland24:: %s" % token[i])
                break

    newtoken = list(token)
    if first < 0 or last < 0:
        first = 12
        last = 13
    newtoken[first] = token[last]
    newtoken[last] = token[first]
    newtoken = ''.join(newtoken)
    #xbmc.log("plugin.video.nederland24:: newtoken: %s" % newtoken)
    return newtoken

		
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
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

def resolve2(url):
    try:
        url = url.replace('/embed-', '/')
        url = re.compile('//.+?/([\w]+)').findall(url)[0]
        page = 'http://allmyvideos.net/%s' % url

        result = client.request(page, close=False)

        post = {}
        f = client.parseDOM(result, 'form', attrs = {'action': ''})
        k = client.parseDOM(f, 'input', ret='name', attrs = {'type': 'hidden'})
        for i in k: post.update({i: client.parseDOM(f, 'input', ret='value', attrs = {'name': i})[0]})
        post = urllib.urlencode(post)

        result = client.request(page, post=post)

        url = re.compile('"file" *: *"(http.+?)"').findall(result)[-1]
        url += '&direct=false&ua=false'
        return url
    except:
        return

def MOVIES_TWO():
    addDir3('Top 20 Most Viewed','http://cnfstudio.com',173,ART+'Movies.png')
    addDir3('Box Office','http://cnfstudio.com/category/box-office/',89,ART+'Movies.png')
    addDir3('Genres','http://cnfstudio.com/movies/',164,ART+'Movies.png')
    addDir3('By Year','http://cnfstudio.com',174,ART+'Movies.png')
    addDir3('Search Movies','',171,ART+'Movies.png')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))




if mode == None     : Home_Menu()
elif mode == 9      : yt.PlayVideo(url)
elif mode == 10     : Films.Films()
elif mode == 11     : TV.TV_Shows()
elif mode == 12     : Standup.Stand_Up()
elif mode == 13     : addSearch()
elif mode == 14     : TV.Animated_TV()
elif mode == 15     : TV.Action_TV()
elif mode == 16     : TV.Childrens_TV()
elif mode == 17     : TV.Comedy_TV()
elif mode == 18     : TV.Drama_TV()
elif mode == 19     : TV.Entertainment_TV()
elif mode == 20     : TV.Fantasy_TV()
elif mode == 21     : TV.Music_TV()
elif mode == 22     : TV.Scifi_TV()
elif mode == 23     : SoapsCatchup.Soap_TV()
elif mode == 24     : Standup.Jeff_Dunham()
elif mode == 25     : TV.DrWho()
elif mode == 26     : TV.Arrow()
elif mode == 27     : TV.Flash()
elif mode == 28     : utube.Mock_the_week()
elif mode == 29     : utube.Inbetweeners()
elif mode == 30     : utube.WouldILieToYou()
elif mode == 31     : TV.Flash_Series2()
elif mode == 32     : TV.The_Last_Man_On_Earth()
elif mode == 33     : TV.Fargo()
elif mode == 34     : TV.The_Knick()
elif mode == 35     : TV.Gotham()
elif mode == 36     : TV.Sons_Of_Anarchy()
elif mode == 37     : TV.Homelands()
elif mode == 38     : TV.Daredevil()
elif mode == 39     : TV.New_girl()
elif mode == 40     : TV.Dexter()
elif mode == 41     : TV.Live_TV()
elif mode == 42     : TV.Breaking_bad()
elif mode == 43     : TV.Grimm()
elif mode == 44     : TV.Brooklyn_Nine_Nine()
elif mode == 45     : TV.Game_of_thrones()
elif mode == 46     : TV.Bates_motel()
elif mode == 47     : TV.Black_list()
elif mode == 48     : TV.Legends()
elif mode == 49     : TV.Suits()
elif mode == 50     : TV.Once_upon_a_time()
elif mode == 51     : TV.How_I_Met_Your_Mother()
elif mode == 52     : Test()
elif mode == 53     : lists.Lists()
elif mode == 54     : M3u8Lists()
elif mode == 55     : Pandoras_Box()
elif mode == 56 	: TESTMOVIE()
elif mode == 57 	: Football()
elif mode == 58 	: FootballFixturesDay()
elif mode == 59 	: FootballFixturesGame(url)
elif mode == 60 	: FootballFixturesChannel()
elif mode == 61 	: Sponge_TV()
elif mode == 62 	: Radio(url)
elif mode == 63 	: Radiocountry()
elif mode == 64 	: Sports()
elif mode == 65 	: whatson(url)
elif mode == 66 	: TV.WorldNews()
elif mode == 67 	: TV.WorldPlayUrl(url)
elif mode == 68 	: TV.WorldPlayVid(url)
elif mode == 69 	: Guidemenu()
elif mode == 70		: whatsonsky()
elif mode == 71 	: whatsoncat()
elif mode == 72 	: NewsCat()
elif mode == 73 	: NewsStory(url)
elif mode == 74 	: News_Article(name, url)
elif mode == 75 	: premierleague.Premier_League_Table()
elif mode == 76 	: Scraper()
elif mode == 77 	: MOVIES_TWO()
elif mode == 78 	: cnfCat(url)
elif mode == 79 	: cnfMovie(url)
elif mode == 80		: cnfPlay1(url)
elif mode == 81 	: cnfTV()
elif mode == 82 	: cnfTVCat(url)
elif mode == 83 	: cnfTVPlay(url)
elif mode == 84 	: cnfTVPlay1(url)
elif mode == 85 	: cnfTVPlay2(url)
elif mode == 86 	: TV.List_LiveTVFull(name)
elif mode == 87 	: TV.LiveTVFull(name)
elif mode == 88 	: TV.LiveTVFullCat()
elif mode == 89 	: CNF_Studio_Indexer.Box_Office(url)
elif mode == 90 	: Alluc_Indexer.Search_Alluc()
elif mode == 91 	: Alluc_Indexer.Get_Alluc_Page(url,name)
elif mode == 92		: Alluc_Indexer.Get_Playlink(url,name)
elif mode == 93 	: FootballReplays.Replay_Menu()
elif mode == 94		: FootballReplays.get_All_Rows(url)
elif mode == 95 	: SoapsCatchup.Hollyoaks()
elif mode == 96 	: SoapsCatchup.Eastenders()
elif mode == 97 	: SoapsCatchup.Emmerdale()
elif mode == 98 	: SoapsCatchup.CoronationStreet()
elif mode == 99 	: collect_token()
elif mode == 100 	: Get_Page(name, url, iconimage)
elif mode == 101 	: SoapsCatchup.ImACeleb()
elif mode == 102	: documentary.DOC1()
elif mode == 103    : documentary.DOC2(url)
elif mode == 104    : documentary.DOC3(url)
elif mode == 105 	: documentary.DOCLIST(url)
elif mode == 106 	: IMDBsearch.Get_imdb_movie_search()
elif mode == 107 	: IMDBsearch.Get_movie(name,url,iconimage)
elif mode == 108 	: IMDBsearch.Get_imdb_TV_Episode(name,url)
elif mode == 109 	: M3Uscrape.Get_m3u_links()
elif mode == 110 	: M3Uscrape.Get_m3u_playlinks(url)
elif mode == 111 	: IMDBsearch.find_Alluc_Link(name)
elif mode == 112 	: M3Uscrape.next_page(url)
elif mode == 113 	: search_addon.Get_Episode_2(url)
elif mode == 164	: cnfHome()
elif mode == 165	: CNF_Studio_Indexer.List_Movies(url)
elif mode == 166	: CNF_Studio_Indexer.Get_Movie_Page(url)
elif mode == 167	: LiveTVFull(name)
elif mode == 168	: List_LiveTVFull(name)
elif mode == 169	: CNF_Studio_Indexer.Resolve_CNF_Link(name, url, iconimage)
elif mode == 170	: List_LiveTVCats()
elif mode == 171	: CNF_Studio_Indexer.Search_Movie()
elif mode == 172	: MOVIES_TWO()
elif mode == 173	: CNF_Studio_Indexer.MV_Movies(url)
elif mode == 174	: CNF_Studio_Indexer.Movie_ByYear(url)
elif mode == 175 	: search_addon.Search_Addon_Menu()
elif mode == 176 	: search_addon.Search_Pandoras_Films()
elif mode == 177  	: search_addon.Search_Pandoras_TV()
elif mode == 178 	: search_addon.Search_Films_Lists()
elif mode == 179 	: search_addon.Search_LiveTV()
elif mode == 180 	: search_addon.Search_TV_Lists()
elif mode == 181 	: search_addon.search_test()
elif mode == 182 	: search_addon.Get_Episode(url)
elif mode == 183 	: search_addon.Play_link(url)
elif mode == 184 	: TV.Recent_Episodes_Now()
elif mode == 185 	: TV.Recent_Scraped()
elif mode == 186 	: SEO_INFO.Get_Group()
elif mode == 187 	: SEO_INFO.Get_Page(url)
elif mode == 188 	: SEO_INFO.Get_Info(url)
elif mode == 189 	: SEO_INFO.Install_Addon(url,name)
elif mode == 190 	: SEO_INFO.Get_Download_File(url)
elif mode == 191 	: TV.get_Country()
elif mode == 192  	: TV.get_Channel(url)
elif mode == 193 	: TV.get_Part_1_Link(url)
elif mode == 401    : Resolve(url)
elif mode == 400    : Live(url)
elif mode == 402    : streams.ParseURL(url)
elif mode == 403    : Live2(url)
elif mode == 404    : TestPlayUrl(name, url, iconimage)
elif mode == 405    : lists.TESTCATS2()
elif mode == 406    : TESTCATS()
elif mode == 407    : LISTS(url)
elif mode == 408    : LISTS2(url)
elif mode == 409    : LISTS3(url)
elif mode == 410    : lists.TestDizi()
elif mode == 411    : M3UCATS()
elif mode == 412    : M3UPLAY(url)
elif mode == 413    : M3UCATS2()
elif mode == 414    : M3UCATS3()
elif mode == 415    : M3UCATS4()
elif mode == 416    : M3UCATS5()
elif mode == 417    : Parsem3uURL(url)
elif mode == 418    : TVParser.GetLinks(url)
elif mode == 419 	: TVParser.m3uCategory(url)
elif mode == 420 	: Movie2(url)
elif mode == 421 	: Movie3(url)
elif mode == 422 	: Movie4(url)
elif mode == 423 	: open_Menu(url)
elif mode == 424	: build_dialog(url)
elif mode == 425 	: SoapsCatchup.SOAPPLAYER(name,url)
elif mode == 426 	: Pandora_Menu(url)
elif mode == 427 	: addDirPand(name,url,mode,iconimage,fanart,description)
elif mode == 428 	: streams.ParseURL_search(url)
elif mode == 501 	: ResolveTwo(url)
elif mode == 1000 	: ChangeLog()
elif mode == 1001 	: TV.TESTING()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
