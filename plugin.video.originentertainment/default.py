import sys, os
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import yt

addon_id='plugin.video.originentertainment'


base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Origin Entertainment"
VERSION = "1.0.1"
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART 		= os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def Home_Menu():
	# This add a list item yeah its name of label then url if its a link then mode then icon image then fanart image and dont know about last one lol description i think
	addDir('Movies','',2,'','','')
	addDir('Comedy','',3,'','','')
#	addDir('Home Three','','test2','','','')
#	addDir('Home Four','','test2','','','')
#	addDir('Home Five','','test2','','','')
#	addDir('Home Six','','test2','','','')
#	addDir('Home Seven','','test2','','','')
#	addDir('Home Eight','','test2','','','')
#	addDir('Home Nine','','test2','','','')
#	addDir('Home Ten','','test2','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)

def Third_Menu():
	addVID('','Beauty and the beast','VBVqtr9yYFU',9,'icon.png','','','')
	addVID('','Bedtime Stories','TPW2haPRsIs',9,'icon.png','','','')
	addVID('','Bruce Almighty','81KO8AYwnqY',9,'icon.png','','','')
	addVID('','Crank','bCGfQKA-w_c',9,'icon.png','','','')
	addVID('','Cowboys and Aliens','ovEC9uucMdc',9,'icon.png','','','')
	addVID('','Flash Gordon','cX2prhbupro',9,'icon.png','','','')
	addVID('','Just go with it','qMmnM_p_UWU',9,'icon.png','','','')
	addVID('','Legally Blonde','KgTmGFiRaWI',9,'icon.png','','','')
	addVID('','Law Abiding Citizen','ZiGJWAkxyTA',9,'icon.png','','','')
	addVID('','Planes','5-JP00Asyj8',9,'icon.png','','','')
	addVID('','Peabody and Sherman','CnqYG-ErVw',9,'icon.png','','','')
	addVID('','R.E.D','8uYpHmOcuf8',9,'icon.png','','','')
	addVID('','Robin Hood 2010','v6AJyDPfzlY',9,'icon.png','','','')
	addVID('','Rush Hour','WwOx_7gCP9U',9,'icon.png','','','')
	addVID('','Rush Hour 2','pPI4gYCEbnA',9,'icon.png','','','')
	addVID('','Richie Rich','kcIktGgrRmQ',9,'icon.png','','','')
	addVID('','S.W.A.T','Gl1r10HpZZM',9,'icon.png','','','')
	addVID('','The 40 year old virgin','TXvDbsh-pwk',9,'icon.png','','','')
	addVID('','The A Team','AsFJY1LvTLE',9,'icon.png','','','')
	addVID('','Tombstone','ggd-74FG6ac',9,'icon.png','','','')
	addVID('','The Bourne Identity','tvi3shzDaPQ',9,'icon.png','','','')
	addVID('','The Bourne Ultimatum','7MyZSUMN6Mc',9,'icon.png','','','')
	addVID('','The Bourne Legacy','oRrifHAhVjc',9,'icon.png','','','')
	addVID('','The Little Rascals','5L1ODF8iPWY',9,'icon.png','','','')
	addVID('','The Maze Runner','V3sIffYlBtg',9,'icon.png','','','')
	addVID('','Waterboy','dkj2aI9xdTw','9','icon.png','')
	addVID('','Wall-E','9Zp10_vBqEM',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)

def Comedy():

	addDir('Stand Up','',100,'','','')
	addDir('Tv Shows','',101,'','','')
#	addVID('','Sean Lock','iBcnfgM43VM',9,'icon.png','','','')
#	addVID('','Lee Evans','8JHWGMVTLwQ',9,'icon.png','','','')
#	addVID('','Micheal Mcintyre','W1Aa503qr-E',9,'icon.png','','','')
#	addVID('','Mrs Browns Boys','nmGf1k0nfwo',9,'icon.png','','','')
#	addVID('','Billy Connolly','2kuspt3Cglo',9,'icon.png','','','')
#	addVID('','Dara O Briain','39LK1A1YGPc',9,'icon.png','','','')
#	addVID('','Cats','UIrEM_9qvZU',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
	
def Stand_up():

	addDir('Billy Connolly','',206,'','','')
	addDir('Frankie Boyle','',201,'','','')
	addDir('Jeff Dunham','',205,'','','')
	addDir('Lee Evans','',203,'','','')
	addDir('Micheal Mcintyre','',204,'','','')
	addDir('Sean Lock','',202,'','','')

	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Tv_shows():

	addDir('Mrs Browns Boys','',301,'','','')
	addDir('Russell Howards Good News','',300,'','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Russell_howard_good_news():

	addVID('','Series 4 Episode 1','iXMTuenopsQ',9,'icon.png','','','')
	addVID('','Series 4 Episode 3','ztg_E7WJhp8',9,'icon.png','','','')
	addVID('','Series 4 Episode 4','S_WIfJL2EXQ',9,'icon.png','','','')
	addVID('','Series 4 Episode 6','93dVLvMrXq8',9,'icon.png','','','')
	addVID('','Series 6 Episode 2','ri74H1RjZaI',9,'icon.png','','','')
	addVID('','Series 6 Episode 3','LRclkw38HRE',9,'icon.png','','','')
	addVID('','Series 6 Episode 4','euGEauS6Kk0',9,'icon.png','','','')
	addVID('','Series 6 Episode 5','1CR-iBap3gY',9,'icon.png','','','')
	addVID('','Series 6 Episode 6','mbWAZHj5enc',9,'icon.png','','','')
	addVID('','Series 7 Episode 2','em45lXWhH4U',9,'icon.png','','','')
	addVID('','Series 7 Episode 6','ZvasN4BUPCc',9,'icon.png','','','')
	addVID('','Series 7 Episode 7','0Y81TdTmVps',9,'icon.png','','','')
	addVID('','Series 7 Episode 8','QlfSyWuJ97A',9,'icon.png','','','')
	addVID('','Series 7 Episode 10','EG11HvNcGyg',9,'icon.png','','','')
	addVID('','Series 8 Episode 1','S_WIfJL2EXQ',9,'icon.png','','','')
	addVID('','Series 8 Episode 2','R1VQxxyiS8c',9,'icon.png','','','')
	addVID('','Series 8 Episode 4','MJ0hqGe1RZ4',9,'icon.png','','','')
	addVID('','Series 8 Episode 5','3mZn0Hi1qwM',9,'icon.png','','','')
	addVID('','Series 8 Episode 6','s-Vf2A96zok',9,'icon.png','','','')
	addVID('','Series 8 Episode 7','6lujoodyWuw',9,'icon.png','','','')
	addVID('','Series 8 Episode 8','t7mJjO7n2c0',9,'icon.png','','','')
	addVID('','Series 9 Episode 1','a5OKA5SZJK4',9,'icon.png','','','')
	addVID('','Series 9 Episode 8','5-y9NvcRHpY',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)

def Frankie_Boyle():

	addVID('','Frankie Boyle','PR1hrP6YBR4',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)

def Sean_Lock():

	addVID('','Sean Lock','iBcnfgM43VM',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)

def Lee_Evans():

	addVID('','Lee Evans','8JHWGMVTLwQ',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)

def Micheal_Mcintyre():

	addVID('','Micheal Mcintyre','W1Aa503qr-E',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Jeff_Dunham():

	addVID('','Spark of insanity','UDBYXC8EUsg',9,'icon.png','','','')
	addVID('','Unhinged','I6whmmHRYO8',9,'icon.png','','','')
	addVID('','Achmed saves america','OV0Gd0ClBg',9,'icon.png','','','')
	addVID('','Very Special Christmas Special','-5ASk6u2ik4',9,'icon.png','','','')
	addVID('','All over the map','5POeSnPslv0',9,'icon.png','','','')
	addVID('','Controlled Chaos','CcJAFTB6omQ',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)

def Mrs_Browns_Boys():

	addVID('','Mrs Browns Boys','nmGf1k0nfwo',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Billy_Connoly():

	addVID('','Billy Connolly','2kuspt3Cglo',9,'icon.png','','','')
	
	xbmcplugin.endOfDirectory(addon_handle)

def Dara_Obriain():

	addVID('','Dara O Briain','39LK1A1YGPc',9,'icon.png','','','')
	
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
mode=None
iconimage=None
fanart=None
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

if mode == None		: Home_Menu()
elif mode == 2		: Third_Menu()
elif mode == 3		: Comedy()
elif mode == 100	: Stand_up()
elif mode == 101 	: Tv_shows()
elif mode == 201 	: Frankie_Boyle()
elif mode == 202 	: Sean_Lock()
elif mode == 203 	: Lee_Evans()
elif mode == 204 	: Micheal_Mcintyre()
elif mode == 205 	: Jeff_Dunham()
elif mode == 206 	: Billy_Connoly()
elif mode == 207 	: Dara_Obriain()
elif mode == 300 	: Russell_howard_good_news()
elif mode == 301 	: Mrs_Browns_Boys()
elif mode == 9		: yt.PlayVideo(url)