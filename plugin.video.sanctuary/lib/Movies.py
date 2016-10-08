import urllib2,re,os,xbmc,xbmcplugin,xbmcaddon,xbmcgui,urlparse,urllib,sys, process

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'

def Movie_Main():
    process.Menu('Links and menus will take a little to load','',200,ICON,FANART,'','')
    process.Menu('Genre','http://www.pubfilm.biz',202,ICON,FANART,'','')
    process.Menu('New Movies','http://www.pubfilm.biz/lastnews',203,ICON,FANART,'','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
def Movie_Genre(url):
    HTML = process.OPEN_URL(url)
    block = re.compile('<ul class="main-menu clearfix">(.+?)</ul>',re.DOTALL).findall(HTML)
    for item in block:
        match = re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(str(item))
        for url, name in match:
            process.Menu(name,'http://www.pubfilm.biz'+url,203,ICON,FANART,'','')

def Pubfilm_Grab(url):
    HTML = process.OPEN_URL(url)
    match = re.compile('<a class="short-img" href="(.+?)" data-label=".+?">.+?<img src="(.+?)" height="317".+?title="(.+?)" />',re.DOTALL).findall(HTML)
    for url,img,name in match:
        image = 'http://www.pubfilm.biz' + img
        Check_Link(name,url,image)
    Next_Page = re.compile('<a href="(.+?)">Next</a></span>').findall(HTML)
    for item in Next_Page:
        process.Menu('Next Page',item,203,ICON,FANART,'','')
	

def Check_Link(name,url,image):
    HTML = process.OPEN_URL(url)
    match = re.compile('<iframe width="660" height="400" scrolling="no" frameborder="0" src="http://mystream.la/external/(.+?)" allowFullScreen></iframe>').findall(HTML)
    for end in match:
        url = 'http://mystream.la/external/'+end
        process.Play(name,url,205,image,FANART,'','')        

def Get_playlink(url):
    HTML = process.OPEN_URL(url)
    match = re.compile('file:"(.+?)",label:"(.+?)"}').findall(HTML)
    for playlink,quality in match:
        process.Resolve(playlink)
		
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
extra=None
fav_mode=None

try:
    fav_mode=int(params["fav_mode"])
except:
    pass
try:
    extra=urllib.unquote_plus(params["extra"])
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

if mode == 200 : Movie_Main()
elif mode == 202 : Movie_Genre(url)
elif mode == 203 : Pubfilm_Grab(url)
elif mode == 204 : Check_Link(name,url,image)
elif mode == 205 : Get_playlink(url)
