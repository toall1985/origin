import urllib, urllib2, re, Google
import urllib,urllib2, re, os, sys, HTMLParser, control
from bs4 import BeautifulSoup
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
Dialog = xbmcgui.Dialog()
addon_handle = int(sys.argv[1])
addon_id='plugin.video.originentertainment'
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep


def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link


def Get_m3u_links():
    HTML = OPEN_URL('http://bratu-marian.ro/iptv/')
    match = re.compile('<article class=(.+?)</article>',re.DOTALL).findall(HTML)
    match2 = re.compile('class="image-link">.+?<img width.+?src="(.+?)" class="image.+?<time datetime=".+?" itemprop="datePublished">(.+?)</time>.+?<h2 itemprop="name"><a href="(.+?)" title=".+?" itemprop="url">(.+?)</a></h2>').findall(str(match))
    for img,date,url,name in match2:
        addDir3(date + '   -   ' + (name).replace('&#038;',' & ').replace('_',' '),url,110,img)
    match3 = re.compile('<a class="next page-numbers" href="(.+?)"><span class="visuallyhidden">Next</span>').findall(HTML)
    for url in match3:
        addDir3('NEXT',url,112,'')
        print '>>>>>>>>>>>>' + url
		
def next_page(url):
    HTML = OPEN_URL(url)
    match = re.compile('<article class=(.+?)</article>',re.DOTALL).findall(HTML)
    match2 = re.compile('class="image-link">.+?<img width.+?src="(.+?)" class="image.+?<time datetime=".+?" itemprop="datePublished">(.+?)</time>.+?<h2 itemprop="name"><a href="(.+?)" title=".+?" itemprop="url">(.+?)</a></h2>').findall(str(match))
    for img,date,url,name in match2:
        addDir3((date + '   -   ' + name).replace('&#038;',' & ').replace('_',' '),url,110,img)
    match3 = re.compile('<a class="next page-numbers" href="(.+?)"><span class="visuallyhidden">Next</span>').findall(HTML)
    for url in match3:
        addDir3('NEXT',url,112,'')
        print '>>>>>>>>>>>>' + url
		
def Get_m3u_playlinks(url):
    HTML = OPEN_URL(url)
    match = re.compile('#EXTINF:.+?,(.+?)<br />\n(.+?)<br />').findall(HTML)
    match2 = re.compile('<p>(.+?)<br />\n(.+?)</p>').findall(HTML)
    for name,url in match:
		addDir4((name).replace('&#038;',' & ').replace('_',' '),url,401,ART + 'scraper.png')
    for name,url in match2:
		addDir4((name).replace('&#038;',' & ').replace('_',' '),url,401,ART + 'scraper.png')
		
		
		
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


