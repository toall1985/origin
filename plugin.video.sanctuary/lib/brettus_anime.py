import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,shutil,urlresolver, process
addon_id        = 'plugin.video.sanctuary'
addon           = xbmcaddon.Addon(id=addon_id)
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
baseurl         = 'http://brettusbuilds.com/Anime%20/anime%20index.xml'

def GetList():
        link=process.OPEN_URL(baseurl)
        match= re.compile('<link>(.+?)</link><thumbnail>(.+?)</thumbnail><title>(.+?)</title>').findall(link)
        for url,iconimage,name in match:
                if not 'http' in iconimage:iconimage=icon
                process.Menu(name,url,1801,iconimage,fanart,'','')

def GetContent(url,iconimage):
        link=process.OPEN_URL(url)
        match= re.compile('<link>(.+?)</link><thumbnail>(.+?)</thumbnail><title>(.+?)</title>').findall(link)
        for url,iconimage,name in match:
                if not 'http' in iconimage:iconimage=icon
                if '/brettusbuilds.com/' in url:
                    process.Menu(name,url,1801,iconimage,fanart,'','')
                else:process.Play(name,url,1802,iconimage,fanart,'','')

def PLAYLINK(url,iconimage):
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setPath(stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                                     

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
              

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
 
print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)
 
if mode==1800: GetList()
elif mode==1801:GetContent(url,iconimage)
elif mode==1802:PLAYLINK(url,iconimage)

