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


def Films():   

	addList('Action',BASE+'actionfilm'+CAT,400,ART + 'icon.png')
	addList('Animation',BASE+'animationfilm'+CAT,400,ART + 'icon.png')
	addList('Biography/Factual',BASE+'biographyfilm'+CAT,400,ART + 'icon.png')
	addList('Christmas',BASE+'christmasfilm'+CAT,400,ART + 'icon.png')
	addList('Comedy',BASE+'comedyfilm'+CAT,400,ART + 'icon.png')
#	addList('Crime',BASE+'crimefilm'+CAT,400,ART + 'icon.png')
	addList('Drama',BASE+'dramafilm'+CAT,400,ART + 'icon.png')
	addList('Family',BASE+'familyfilm'+CAT,400,ART + 'icon.png')
	addList('Fantasy',BASE+'fantasyfilm'+CAT,400,ART + 'icon.png')
	addList('History',BASE+'historyfilm'+CAT,400,ART + 'icon.png')
	addList('Horror',BASE+'horrorfilm'+CAT,400,ART + 'icon.png')
#	addList('Music',BASE+'musicfilm'+CAT,400,ART + 'icon.png')
	addList('Romance',BASE+'romancefilm'+CAT,400,ART + 'icon.png')
	addList('Scifi',BASE+'scififilm'+CAT,400,ART + 'icon.png')
	
	xbmcplugin.endOfDirectory(addon_handle)

	
def addList(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
