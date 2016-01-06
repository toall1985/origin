import sys
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver
addon_id='plugin.video.originentertainment'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])


def Soap_TV():

    addDir3('Coronation Street','',98,'')   
    addDir3('Eastenders','',96,'')
    addDir3('Emmerdale','',97,'')
    addDir3('Hollyoaks','',95,'')
    addDir3('Im a Celebrity','',101,'')



    
def Hollyoaks():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Holly' in name:
            img = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
            if 'huge' in url:
			    addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),425,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE_IGNORE_THE);

def Eastenders():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'East' in name:
            img = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
            if 'huge' in url:
    			addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),425,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def Emmerdale():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Emmer' in name:
            img = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
            if 'huge' in url:
                addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),425,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def CoronationStreet():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Coro' in name:
            img = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
            if 'huge' in url:
    			addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),425,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def ImACeleb():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)" target="_blank">(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Celeb' in name:
            img = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
            if 'huge' in url:
    			addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),425,img)
            else:
                pass


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

def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def SOAPPLAYER(name,url):
        if urlresolver.HostedMediaFile(url).valid_url():
                stream_url = urlresolver.HostedMediaFile(url).resolve()
        else:
                link = open_url(url)
                url=re.compile('src="(.+?)"></iframe>').findall(link)[0]
                url=url.split('?autoplay')[0]
                link = open_url(url)
                streamurl = re.compile('mp4","url":"(.+?)"').findall(link)[-1]
                stream_url=streamurl.replace('\\/','/')
        liz = xbmcgui.ListItem(name)
        liz.setPath(stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

#ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)