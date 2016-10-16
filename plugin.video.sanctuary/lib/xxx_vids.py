# -*- coding: utf-8 -*-
import urllib2, urllib, xbmcgui, xbmcplugin, xbmcaddon, xbmc, re, sys, os, process
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary')
ICON = ADDON_PATH + '/icon.png'
FANART = ADDON_PATH + '/fanart.jpg'
Dialog = xbmcgui.Dialog()
List = []

def X_vid_Menu():
    process.Menu('Best Videos','http://www.xvideos.com/best',501,ICON,FANART,'','')
    process.Menu('Genres','http://www.xvideos.com',502,ICON,FANART,'','')
    process.Menu('Recently Uploaded','http://xvideos.com',501,ICON,FANART,'','')
    process.Menu('Tags','http://www.xvideos.com/tags',505,ICON,FANART,'','')
    process.Menu('Search','',504,ICON,FANART,'','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

	
def Xtags(url):
    HTML = process.OPEN_URL(url)
    match = re.compile('<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>').findall(HTML)
    for url,name,no in match:
        if '<span' in name:
            pass
        else:
            process.Menu(name + ' - No of Videos : ' + (no).replace('>',''),'http://www.xvideos.com'+url,501,ICON,FANART,'','')
    next_button = re.compile('<li><a class=".+?".+?href="(.+?)">Next</a></li>').findall(HTML)
    for url in next_button:
        if 'Next' not in List:
            process.Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,505,ICON,FANART,'','')
            List.append('Next')
    
def XPornstars(url):
    HTML = process.OPEN_URL(url)
    match = re.compile(':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n',re.DOTALL).findall(HTML)
    for img,url,name,count in match:
        process.Menu(name+'--'+count,'http://www.xvideos.com'+url+'#_tabVideos,videos-best',501,(img).replace('http:\/\/','http://'),FANART,'','')        
    next_button = re.compile('href="([^"]*)">Next</a></li>').findall(HTML)
    for url in next_button:
        if 'Next' not in List:
            process.Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,505,ICON,FANART,'','')
            List.append('Next')
		
	  
def XNew_Videos(url):
    HTML = process.OPEN_URL(url)
    match = re.compile('<div class="thumb-inside">.+?<img src="(.+?)" id=".+?<p><a href="(.+?)" title="(.+?)">.+?<span class="bg"><strong>(.+?)</strong> - (.+?) %',re.DOTALL).findall(HTML)
    for img,url,name,length,rating in match:
        process.Play((name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"').replace('  ','') + ' - Porn Quality : ' + rating + '% - ' + length,'http://www.xvideos.com'+url,506,img,FANART,rating + '% - ' + length,'')	
    next_button2 = re.compile('<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>').findall(HTML)
    for url in next_button2:
        if 'Next' not in List:
            process.Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,505,ICON,FANART,'','')
            List.append('Next')
    
def XGenres(url):
    HTML = process.OPEN_URL(url)
    block = re.compile('<div class="main-categories">(.+?)</div>',re.DOTALL).findall(HTML)
    match = re.compile('<li><a href="(.+?)" class="btn btn-default">(.+?)</a>').findall(str(block))
    for url,name in match:
        if '<span' in name:
            pass
        else:
    		process.Menu(name,'http://www.xvideos.com'+url,501,ICON,FANART,'','')
    next_button = re.compile('<li><a class=".+?".+?href="(.+?)">Next</a></li>').findall(HTML)
    for url in next_button:
        if 'Next' not in List:
            process.Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,505,ICON,FANART,'','')
            List.append('Next')

		
def XSearch_X():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean = (Search_Name).replace(' ','+').replace('&','&')
    Search_Title = Search_Clean.lower()
    Search_URL = 'http://www.xvideos.com/?k=' + Search_Title
    print Search_URL + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
    HTML = process.OPEN_URL(Search_URL)
    match = re.compile('<div class=".+?"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?) %.+?</span>',re.DOTALL).findall(HTML)
    for img,url,name,length,rating in match:
        process.Play((name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"').replace('  ','') + ' - Porn Quality : ' + rating + '% - ' + length,'http://www.xvideos.com'+url,506,img,FANART,rating + '% - ' + length,'')	
    next_button2 = re.compile('<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>').findall(HTML)
    for url in next_button2:
        if 'Next' not in List:
            process.Menu('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,505,ICON,FANART,'','')
            List.append('Next')

def XPlayLink(url):
    HTML = process.OPEN_URL(url)
    match = re.compile("setVideoHLS.+?'(.+?)'").findall(HTML)
    for url in match:
        process.Resolve(url)
			
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
fanart=None
description=None
fav_mode=None


try:
    fav_mode=int(params["fav_mode"])
except:
    pass

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
        
        
		
if mode   == 500: X_vid_Menu()
elif mode == 501: XNew_Videos(url)
elif mode == 502: XGenres(url)
elif mode == 503: XPornstars(url)
elif mode == 504: XSearch_X()
elif mode == 505: Xtags(url)
elif mode == 506: XPlayLink(url)
