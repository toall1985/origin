'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

import sys
import urllib2,re,os,base64,xbmc,xbmcplugin,xbmcaddon,xbmcgui,urlparse,urllib
import urlresolver,yt
try:
    import json
except:
    import simplejson as json
from threading import Thread

Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
CAT=Decode('LnBocA==')
BASE = 'http://www.couchtripper.com/forum2/page.php?page=3'
addon_id='plugin.video.getupstandup'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Get Up - Stand Up"
VERSION = "1.0.1"
dp = xbmcgui.DialogProgress()
ADDON = xbmcaddon.Addon(id=addon_id)
debug = ADDON.getSetting('debug')
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/'+PATH+'/'
favourites = ADDON_DATA + 'favourites'
if not os.path.exists(ADDON_DATA):
    os.makedirs(ADDON_DATA)
if os.path.exists(favourites)==True:
    FAV = open(favourites).read()
else: FAV = []
Sources = ['daclips','filehoot','allmyvideos','vidspot','vodlocker','vidto']		



ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
IMAGES 		=  ART + 'icon.png'
Main 		= 'http://www.watchseries.ac'

def Main_Menu():

    Menu('Stand Up','',6,IMAGES,FANART,'','')
    Menu('Tv Shows','http://herovision.x10host.com/GetUpStandUp/TV_Shows.php',4,IMAGES,FANART,'','')
    Menu('Movies','http://herovision.x10host.com/GetUpStandUp/Movies.php',4,IMAGES,FANART,'','')
    Menu('Favourites','',103,IMAGES,FANART,'','')
	
def Stand_up_Menu():
    Menu('Youtube Playlists','http://herovision.x10host.com/GetUpStandUp/yt_standup_playlist.php',4,IMAGES,FANART,'','')
    Menu('Couch Tripper','',1,IMAGES,FANART,'','')
	
def Regex(url):
    HTML = OPEN_URL(url)
    match = re.compile('<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"').findall(HTML)
    for name,url,mode,image,fanart,desc in match:
        if image == 'IMAGES':
            image = IMAGES
        if fanart == 'FANART':
            fanart = FANART
        if '.php' in url:
            Menu(name,url,4,image,fanart,desc,'')
        if mode == 'single':
            Play(name,url,9,image,fanart,desc,'')
        elif mode == 'playlist':
            Menu(name,url,7,image,fanart,desc,'')
        elif mode == 'watchseries':
            Menu(name,url,100,image,fanart,desc,name)
        elif mode == 'normal':
            Play(name,url,5,image,fanart,desc,'')
            
    	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);		
	
	
def grab_youtube_playlist(url):

    HTML = OPEN_URL(url)
    block_set = re.compile('<tr class="pl-video yt-uix-tile(.+?)</tr>',re.DOTALL).findall(HTML)
    for block in block_set:
        image = re.compile('data-thumb="(.+?)"').findall(str(block))
        for image in image:
            image = image
        name = re.compile('data-title="(.+?)"').findall(str(block))
        for name in name:
            if 'elete' in name:
                pass
            elif 'rivate Vid' in name:
                pass
            else:
    			name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
        duration = re.compile('<div class="timestamp"><span aria-label=".+?">(.+?)</span>').findall(str(block))
        for duration in duration:
            duration = duration
        url = re.compile('data-video-ids="(.+?)"').findall(str(block))
        for url in url:
            url = url
        Play('[COLORred]'+str(duration)+'[/COLOR] : '+str(name),str(url),9,str(image),FANART,'','' )


#    image = ''
#    HTML = OPEN_URL(url)
#    block_set = re.compile('<li class="yt-uix-scroller-scroll-unit "(.+?)</li>',re.DOTALL).findall(HTML)
#    for block in block_set:
#        name = re.compile('data-video-title="(.+?)"').findall(str(block))
#        for name in name:
#            name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
#        url = re.compile('<a href="/w(.+?)&').findall(str(block))
#       for url in url:
#            url = (url).replace('atch?v=','')
#        image = re.compile('data-thumbnail-url="(.+?)"').findall(str(block))
#        for image in image:
#            image = image
#        if 'elete' in name:
#            pass
#        if 'rivate ' in name:
#            pass        
#        else:
#            Play(name,url,9,image,FANART,'','')

def Stand_up():
    HTML = OPEN_URL(BASE)
    Block = re.compile('<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>',re.DOTALL).findall(HTML)
    for img, comic, c in Block:
	find_URL = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(c)
        for url, name in find_URL:
            if 'tube' in url:
                pass
            elif 'stage' in url:
				Play(comic + '   -   ' + name,(url).replace('" target="_blank',''),3,'http://couchtripper.com/'+img,FANART,'','')
            elif 'vee' in url:
                pass
			    

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def Youtube_StandUP_grab():
    pass
	
###########################Watch series Grab##########################################

def Grab_Season(iconimage,url,extra):
    image = ' '
    description = ' '
    fanart = ' '
    season = ' '
    OPEN = OPEN_URL(url)
    image = re.compile('<img src="(.+?)">').findall(OPEN)
    for image in image:
        image = image
    background = re.compile('style="background-image: url\((.+?)\)">').findall(OPEN)
    for fanart in background:
        fanart = fanart	
    match = re.compile('itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>',re.DOTALL).findall(OPEN)
    for url,season in match:
        season = 'S'+(season).replace('  ','').replace('\n','').replace('    ','').replace('	','')
        url = Main + url
        Menu((season).replace('  ',''),url,101,image,fanart,description,'')
        setView('Movies', 'INFO')
	
def Grab_Episode(url,name,fanart,extra,iconimage):
    main_name = extra 
    season = name
    OPEN = OPEN_URL(url)
    image = iconimage
    match = re.compile('<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>',re.DOTALL).findall(OPEN)
    for url,name,date in match:
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        url = Main+url
        date = date
        full_name = name+' - [COLORred]'+date+'[/COLOR]'
        Menu(full_name,url,102,image,fanart,'Aired : '+date,full_name)

def Get_Sources(name,URL,iconimage,fanart):
    HTML = OPEN_URL(URL)
    match = re.compile('<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n',re.DOTALL).findall(HTML)
    for url,name in match:
        for item in Sources:
            if item in url:
                URL = 'http://www.watchseries.ac/link/' + url
                Play(name,URL,106,IMAGES,FANART,'','')
    if len(match)<=0:
        Menu('[COLORred]NO STREAMS AVAILABLE[/COLOR]','','','','','','')
		
		
def Get_site_link(url,name):
    season_name = name
    HTML = OPEN_URL(url)
    match = re.compile('<iframe style=.+?" src="(.+?)"').findall(HTML)
    match2 = re.compile('<IFRAME SRC="(.+?)"').findall(HTML)
    match3 = re.compile('<IFRAME style=".+?" SRC="(.+?)"').findall(HTML)
    for url in match:
        main(url,season_name)
    for url in match2:
        main(url,season_name)
    for url in match3:
        main(url,season_name)

def main(url,season_name):
    if 'daclips.in' in url:
        daclips(url,season_name)
    elif 'filehoot.com' in url:
        filehoot(url,season_name)
    elif 'allmyvideos.net' in url:
        allmyvid(url,season_name)
    elif 'vidspot.net' in url:
        vidspot(url,season_name)
    elif 'vodlocker' in url:
        vodlocker(url,season_name)	
    elif 'vidto' in url:
        vidto(url,season_name)	


def vidto(url,season_name):
    HTML = OPEN_URL(url)
    match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"',re.DOTALL).findall(HTML)
    for Link,name in match:
        Printer(Link,season_name)

												
def allmyvid(url,season_name):
    HTML = OPEN_URL(url)
    match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"',re.DOTALL).findall(HTML)
    for Link,name in match:
        Printer(Link,season_name)

def vidspot(url,season_name):
    HTML = OPEN_URL(url)
    match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"').findall(HTML)
    for Link,name in match:
        Printer(Link,season_name)

def vodlocker(url,season_name):
    HTML = OPEN_URL(url)
    match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
    for Link in match:
        Printer(Link,season_name)

def daclips(url,season_name):
    HTML = OPEN_URL(url)
    match = re.compile('{ file: "(.+?)", type:"video" }').findall(HTML)
    for Link in match:
        Printer(Link,season_name)

def filehoot(url,season_name):
    HTML = OPEN_URL(url)
    match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
    for Link in match:
        Printer(Link,season_name)

def Printer(Link,season_name):
    if 'http:/' in Link:
        Resolve(Link)
###########################################Watch series end###########################################			
	
def Play_Stage(url):
    HTML = OPEN_URL(url)
    playlink = re.compile("url\[.+?\] = '(.+?)';").findall(HTML)
    for url in playlink:
        Resolve((url).replace('[','').replace(']','').replace('\'',''))

def Menu(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Get Up Stand Up Favorites','XBMC.RunPlugin(%s?mode=105&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Get Up Stand Up Favorites','XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

		
def Play(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Get Up Stand Up Favorites','XBMC.RunPlugin(%s?mode=105&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Get Up Stand Up Favorites','XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def RESOLVE(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    url = (url).strip()
    try: play.play(url).strip()
    except: pass

		
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True
		
		
#===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------

def addon_log(string):
    if debug == 'true':
        xbmc.log("[addon.live.GenieTV-%s]: %s" %(addon_version, string))

def addFavorite(name,url,iconimage,fanart,mode,playlist=None,regexs=None):
        favList = []
        try:
            # seems that after
            name = name.encode('utf-8', 'ignore')
        except:
            pass
        if os.path.exists(favourites)==False:
            addon_log('Making Favorites File')
            favList.append((name,url,iconimage,fanart,mode,playlist,regexs))
            a = open(favourites, "w")
            a.write(json.dumps(favList))
            a.close()
        else:
            addon_log('Appending Favorites')
            a = open(favourites).read()
            data = json.loads(a)
            data.append((name,url,iconimage,fanart,mode))
            b = open(favourites, "w")
            b.write(json.dumps(data))
            b.close()
		

def getFavorites():
        if os.path.exists(favourites)==False:
            favList = []
            addon_log('Making Favorites File')
            favList.append(('Get Up Stand Up Favourites Section','','','','','',''))
            a = open(favourites, "w")
            a.write(json.dumps(favList))
            a.close()        
        else:
			items = json.loads(open(favourites).read())
			total = len(items)
			for i in items:
				name = i[0]
				url = i[1]
				iconimage = i[2]
				try:
					fanArt = i[3]
					if fanArt == None:
						raise
				except:
					if ADDON.getSetting('use_thumb') == "true":
						fanArt = iconimage
					else:
						fanArt = fanart
				try: playlist = i[5]
				except: playlist = None
				try: regexs = i[6]
				except: regexs = None

				if i[4] == 0:
					Menu(name,url,'',iconimage,fanart,'','','fav')
				else:
					Menu(name,url,i[4],iconimage,fanart,'','','fav')

def rmFavorite(name):
        data = json.loads(open(favourites).read())
        for index in range(len(data)):
            if data[index][0]==name:
                del data[index]
                b = open(favourites, "w")
                b.write(json.dumps(data))
                b.close()
                break
        xbmc.executebuiltin("XBMC.Container.Refresh")
		
############################## FAVOURITES END ###############################
		
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
        
def Resolve(url): 
    play=xbmc.Player()
    import urlresolver
    try: play.play(url)
    except: pass

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = ''
    link = ''
    try: 
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    except: pass
    if link != '':
        return link
    else:
        link = 'Opened'
        return link

def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)


if mode == None     : Main_Menu()
elif mode == 1 		: Stand_up()
elif mode == 2    	: Search()
elif mode == 3 		: Play_Stage(url)
elif mode == 4 		: Regex(url)
elif mode == 5    	: Resolve(url)
elif mode == 6 		: Stand_up_Menu()

elif mode == 7 		: grab_youtube_playlist(url)
elif mode == 9 	 	: yt.PlayVideo(url)


elif mode == 100 	: Grab_Season(iconimage,url,extra)
elif mode == 101 	: Grab_Episode(url,name,fanart,extra,iconimage)
elif mode == 102	: Get_Sources(name,url,iconimage,fanart)
elif mode == 106 	: Get_site_link(url,name)
elif mode==103:
    addon_log("getFavorites")
    getFavorites()
elif mode==104:
    addon_log("addFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name,url,iconimage,fanart,fav_mode)
elif mode==105:
    addon_log("rmFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

#def Search():
#    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
#    Search_Title = Search_Name.lower()
#    HTML = OPEN_URL(BASE)
#    Block = re.compile('<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>',re.DOTALL).findall(HTML)
#    for img, comic, c in Block:
#        for Search_Name in comic:
#            find_URL = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(c)
#            for url, name in find_URL:
#                if 'tube' in url:
#                    pass
#                elif 'stage' in url:
#                    Play(comic + '   -   ' + name,(url).replace('" target="_blank',''),3,'http://couchtripper.com/'+img,FANART,'')
#                elif 'vee' in url:
#			        pass
