import sys, base64
import urllib,re,os,xbmcplugin
import process

Decode = base64.decodestring
addon_handle = int(sys.argv[1])
List = []


def Radio_Country():  
    html=process.OPEN_URL(Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw=='))
    match = re.compile('<tr>.+?<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(html)
    for url,name in match:
        if name not in List:
    	    process.Menu((name).replace('email me','').replace('External services',''),Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1LyVz')%url,501,'','','','')
            List.append(name)
	
def Radio(url):
    process.Menu('Please allow loading to finish before pressing back','','','','','','')
    process.Menu('To save potentially crashing kodi','','','','','','')
    html=process.OPEN_URL(url)
    match = re.compile('<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">',re.DOTALL).findall(html)
    for name,url in match:
		process.Play(name,url,502,'','','','')

			
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);


			
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

if mode   == 500   : Radio_Country()
elif mode == 501   : Radio(url)
elif mode == 502   : process.Resolve(url)
