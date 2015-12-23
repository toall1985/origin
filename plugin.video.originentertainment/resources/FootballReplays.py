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
from resources import streams,lists,utube,TV,Standup,Films,premierleague,Google,client,CNF_Studio_Indexer,Alluc_Indexer
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


#_________________________________________________________________________________________________________________________________________________________

# Get All Rows
def Replay_Menu():
    addDir3('Premier League','http://www.fullmatchesandshows.com/premier-league/',94,ART+'ChangeLog.png')
    addDir3('La Liga','http://www.fullmatchesandshows.com/la-liga/',94,ART+'ChangeLog.png')
    addDir3('Bundesliga','http://www.fullmatchesandshows.com/bundesliga/',94,ART+'ChangeLog.png')
    addDir3('Champions League','http://www.fullmatchesandshows.com/champions-league/',94,ART+'ChangeLog.png')
    addDir3('Serie A','http://www.fullmatchesandshows.com/category/serie-a/',94,ART+'ChangeLog.png')
    addDir3('Ligue 1','http://www.fullmatchesandshows.com/category/ligue-1/',94,ART+'ChangeLog.png')
    addDir3('Copa America 2015','http://www.fullmatchesandshows.com/copa-america-2015/',94,ART+'ChangeLog.png')
    addDir3('CONCACAF','http://www.fullmatchesandshows.com/category/concacaf/',94,ART+'ChangeLog.png')
    addDir3('Women World Cup','http://www.fullmatchesandshows.com/category/women-world-cup/',94,ART+'ChangeLog.png')


		
def get_All_Rows(url):
	request_HTML = open_URL(url)
	get_Rows = re.compile('<div class="td-block-row">(.*?)</div><!--./row-fluid-->',re.DOTALL).findall(request_HTML)
	for row in get_Rows:
		for_Each_Row(row)

# Get Each Video From The Row

def for_Each_Row(row):
	Get_Row_Item = re.compile('<div class="td-block-span4">(.+?)<!-- ./td-block-span4 -->',re.DOTALL).findall(row)
	for row_Item in Get_Row_Item:
		get_Each_Item_Data(row_Item)

# For Each Video In Row Get Link & Title

def get_Each_Item_Data(row_Item):
	get_item_Data = re.findall(r'<a href="(.+?)" rel="bookmark" title="(.+?)">',str(row_Item))
	item_Data = []
	link = ''
	for link, title in get_item_Data:
		item_Data.append(title)
		link = link
	
	get_Each_Item_Image(item_Data, row_Item, link)

# For Each Video In Row Get Image

def get_Each_Item_Image(item_Data, row_Item, link):
	get_Item_Image = re.compile('<img width=".+?" height=".+?" itemprop=".+?" class="entry-thumb" src="(.+?)" alt=".+?" title=".+?"/>',re.DOTALL).findall(row_Item)
	for image in get_Item_Image:
		item_Data.append(image)
	
	get_Each_Item_PLink(item_Data, link)

# For Each Video In Row Get Play Link
	
def get_Each_Item_PLink(item_Data, link):
	get_HTML = open_URL(link)
	get_Play_Link = re.compile('<script data-config="(.+?)" data-css=".+?" data-height=".+?" data-width=".+?" src=".+?" type="text/javascript"></script>',re.DOTALL).findall(get_HTML)
	for pLink in get_Play_Link:
		item_Data.append(pLink)
		
	clean_And_Build_Item(item_Data)

# For Each Video In Row Clean And Build Item

def clean_And_Build_Item(item_Data):
	Name = item_Data[0]
	Image = item_Data[1]
	Play_Link = item_Data[2]
	
	#Name = Name.decode("utf-8")
	#Name = Name.encode("ascii")
	Name = Name.replace('&#8211;', '-').replace('&#038;', '&')
	Play_Link = Play_Link.replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
	print '~~~~~~~~~~~~~~~~~~~~'
	print Name
	print Image
	print Play_Link
	print '~~~~~~~~~~~~~~~~~~~~'
	addDir4(Name,'http:'+Play_Link,401,Image)
#_________________________________________________________________________________________________________________________________________________________

def open_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
	


# NOTES

#item_Data[0] = Title
#item_Data[1] = Image
#item_Data[2] = Play Link

def addDir4(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
