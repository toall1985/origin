import sys
import urlparse
import yt
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver
addon_id='plugin.video.originentertainment'

Decode = base64.decodestring
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))


def DOC1():
    html=OPEN_URL(Decode('aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw=='))
    match = re.compile('<a href="(.+?)" >(.+?)</a></li><li>').findall(html)
    for url,name in match:
                addDir3(name,url,103,ART+'tv.png')
def DOC2(url):
    html=OPEN_URL(url)
    match = re.compile('<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"',re.DOTALL).findall(html)
    match2 = re.compile('class="inactive">.+?</a><a href="(.+?)">Next</a></div>',re.DOTALL).findall(html)
    for url,name,img in match:
        addDir3((name).replace('&#039;s',''),url,104,img)                
    for url in match2:
        addDir3('NEXT PAGE',url,103,ART + 'icon.png')

	
def DOC3(url):
    html=OPEN_URL(url)
    match = re.compile('<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />',re.DOTALL).findall(html)
    match2 = re.compile('<div class="video new-video"><iframe width="766" height="431" src="(.+?)"',re.DOTALL).findall(html)
    for name,img,url,disc in match:
        addDir4((name).replace('&#039;s',''),url.replace('https://www.youtube.com/embed/',''),9,img)
    for url in match2:
        DOCLIST((url).replace('//','http://'))

def DOCLIST(url):
    html=OPEN_URL(url)
    match = re.compile('<link rel="canonical" href="(.+?)">  <link rel="stylesheet"').findall(html)
    for url in match:
        addDir4('PLAY',(url).replace('http://www.youtube.com/watch?v=',''),9,ART + 'icon.png')
		
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
		
