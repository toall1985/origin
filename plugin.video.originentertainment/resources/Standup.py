import sys
import urlparse
import yt
import time
import urllib,urllib2,re,base64,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import base64
import urlresolver
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
from resources import streams
from resources import lists
from resources import utube

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
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART 		=  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
net = Net()

def Stand_Up():

	addList('Stand Up',BASE+'standuplist'+CAT,400,ART + 'icon.png')
	addVID('','Billy Connolly','2kuspt3Cglo',9,'icon.png',ART + 'background.png','','')
	addVID('','Dara O Briain','39LK1A1YGPc',9,'icon.png',ART + 'background.png','','')
	addVID('','Dave Gorman','Zdq9p2cBITU',9,'icon.png',ART + 'background.png','','')
	addVID('','Frankie Boyle','PR1hrP6YBR4',9,'icon.png',ART + 'background.png','','')
	addVID('','Lee Evans','8JHWGMVTLwQ',9,'icon.png','',ART + 'background.png','')
	addDir('Jeff Dunham','',24,ART + 'icon.png',ART + 'background.png','')
	addVID('','Micheal Mcintyre','W1Aa503qr-E',9,'icon.png',ART + 'background.png','','')
	addVID('','Mrs Browns Boys','nmGf1k0nfwo',9,'icon.png',ART + 'background.png','','')
	addVID('','Sean Lock','iBcnfgM43VM',9,'icon.png',ART + 'background.png','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Jeff_Dunham():

	addVID('','Spark of insanity','UDBYXC8EUsg',9,'icon.png',ART + 'background.png','','')
	addVID('','Unhinged','I6whmmHRYO8',9,'icon.png',ART + 'background.png','','')
	addVID('','Achmed saves america','OV0Gd0ClBg',9,'icon.png',ART + 'background.png','','')
	addVID('','Very Special Christmas Special','-5ASk6u2ik4',9,'icon.png',ART + 'background.png','','')
	addVID('','All over the map','5POeSnPslv0',9,'icon.png',ART + 'background.png','','')
	addVID('','Controlled Chaos','CcJAFTB6omQ',9,'icon.png',ART + 'background.png','','')
	addList('2015 Unhinged in Hollywood',BASE+'jeffdunham'+CAT,400,ART + 'icon.png')

	
	xbmcplugin.endOfDirectory(addon_handle)

def addList(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
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
