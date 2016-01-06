import sys
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver
from resources import downloader, extract
addon_id='plugin.video.originentertainment'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])


def Get_Group():
    HTML = OPEN_URL('https://seo-michael.co.uk')
    match2 = re.compile('<nav id="nav">(.+?)</nav>',re.DOTALL).findall(HTML)
    match = re.compile('<li class="nav-.+?" role="presentation"><a href="(.+?)">(.+?)</a></li>').findall(str(match2))
    for url,name in match:
	    addDir3(name,url,187,'')

def Get_Page(url):
    HTML = OPEN_URL(url)
    match = re.compile('<h2 class="post-title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+?<div class="post-excerpt">(.+?)</div>',re.DOTALL).findall(HTML)
    for url,name,desc in match:
        addDirPand2(name,'https://seo-michael.co.uk' + url,188,'','',desc)
    match2 = re.compile('<link rel="next" href="(.+?)" />').findall(HTML)
    for url in match2:
        addDir3('NEXT PAGE',url,187,'')

        setView('tvshows', 'Media Info 3')			
		
#(name,url,mode,iconimage,fanart,description)
        
def Get_Info(url):
    HTML = OPEN_URL(url)
    match4 = re.compile('<p>(.+?)<a href="(.+?)"><strong>(.+?)</strong></a>').findall(HTML)
    for name,url,name2 in match4:
        addDir3(name + ' ' + name2,'https://seo-michael.co.uk' + url,188,'')
    match3 = re.compile('<li>(.+?)<a href="(.+?)" rel="nofollow" target="_blank"><strong>(.+?)</strong></a>(.+?)</li>').findall(HTML)
    for name1,url,name2,name3 in match3:
        addDir4('[COLORred]PRESS HERE TO INSTALL ADDON[/COLOR]',url,190,'')
        name = name1
    else:
		match = re.compile('<p>(.+?)</p>').findall(HTML)
		for name in match:
			if 'img' in name:
				pass
			elif 'href' in name:
				pass
			elif 'strong' in name:
				pass
			else:
				addDir3(name,'','','')
		match3 = re.compile('<a href="(.+?)"><strong>(.+?)</strong></a>').findall(str(match))
		for url,name in match3:
			addDir3(name,'https://seo-michael.co.uk' + url,188,'')
		match2 = re.compile('<li>(.+?)<strong>(.+?)</strong></li>\n</ul>\n\n<p><img src="(.+?)" alt="" /></p>').findall(HTML)
		for name1,name2,img in match2:
			addDir3((name1).replace('</strong>','').replace('<strong>','').replace('&#47;','').replace('&amp;','')+ (name2).replace('</strong>','').replace('<strong>','').replace('&#47;','').replace('&amp;',''),'','',img)

def Get_Download_File(url):
    HTML = OPEN_URL(url)
    print 'THIS IS URL========' + url
    url2 = (url).replace('file.html','')
    print 'THIS IS URL2========' + url2
    match = re.compile('var n = (.+?) +').findall(HTML)	
    for var in match:
        print 'THIS IS VAR========' + var
        A = int(var)
        B = 1
        varchange = (A + B)
        print varchange		
        matchname = re.compile('<title>(.+?)</title>').findall(HTML)
        for name in matchname:
			url = url2 + (str(varchange)) + '/' + (name).replace('Zippyshare.com - ','')
			urlfull = 'http://www31.zippyshare.com/d/N3GHU1hH/668382/plugin.video.SportsDevil-2016-01-02.zip'
			print 'THIS IS URLFULL ======== ' + urlfull
			print 'THIS IS NAME ======== ' + (name).replace('Zippyshare.com - ','')
			Install_Addon(urlfull,(name).replace('Zippyshare.com - ',''))
			print 'THIS IS URL FULL AFTER ======== ' + urlfull
	
	
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
		
		
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def addDirPand2(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)

def Install_Addon(url,name):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("ADDON INSTALLING","Downloading Content",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://home','addons'))
    time.sleep(2)
    dp.update(0,"", "Installing addon - Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    UPDATEREPO()		