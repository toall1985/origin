import urllib, urllib2, re, Google,base64
import urllib,urllib2, re, os, sys, HTMLParser, control
from bs4 import BeautifulSoup
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

addon_id='plugin.video.originentertainment'
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
Dialog = xbmcgui.Dialog()
addon_handle = int(sys.argv[1])
Decode = base64.decodestring
BASE2=base64.decodestring('aHR0cDovL2RsLmZpbG0ybW92aWUuaW5mby9zZXJpYWwv')
BASE3=base64.decodestring('aHR0cDovL3dhdGNoLXNpbXBzb25zLmNvbS9kb3dubG9hZHMv')
BASE4=base64.decodestring('aHR0cDovL2dheml6b3ZhLm5ldC9wdWIvU2VyaWFscy9QZXBwYSUyMFBpZy9QZXBwYSUyMFBpZyUyMC0lMjBDb21wbGV0ZSUyMFNlcmllcyUyMDEsJTIwMiwlMjAzLCUyMDQv')
BASE5=base64.decodestring('aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi8=')
BASE6=base64.decodestring('aHR0cDovL2dheml6b3ZhLm5ldC9wdWIvU2VyaWFscy9PdGhlclRvb25zL1Rhei1NYW5pYS8=')
BASE7=base64.decodestring('aHR0cDovL2ljaGkxMzQubmV0MTYubmV0L0lQVFYv')
CAT = base64.decodestring('LnBocA==')
BASE = base64.decodestring('aHR0cDovL2JhY2syYmFzaWNzLngxMGhvc3QuY29tL2JhY2syYmFzaWNzL3Rlc3Qv')
Base_Pand = (Decode('aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi8='))

def Search_Addon_Menu():
#	addDir('Search IMDB','',106,ART + 'search.png',ART + 'background.png','')
	addDir('Search Pandoras Films','',176,ART + 'search.png',ART + 'background.png','')
	addDir('Search Pandoras TV','',177,ART + 'search.png',ART + 'background.png','')
	addDir('Search Films','',178,ART + 'search.png',ART + 'background.png','')

	
def Search_Pandoras_Films():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    filenames = ['mova', 'movb', 'movc', 'movd', 'move', 'movf', 'movg', 'movh', 'movi', 'movj', 'movk', 'movl', 'movm', 'movn', 'movo', 'movp', 'movq', 'movr', 'movs', 'movt', 'movu', 'movv', 'movw', 'movx', 'movy', 'movz']

    for file_Name in filenames:
        search_URL = Base_Pand + file_Name + CAT
        HTML = OPEN_URL(search_URL)
        match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /></a><br><b>(.+?)</b>').findall(HTML)
        for url,iconimage,desc,name in match:
            if Search_Name in name.lower():
                addDir3(name,url,401,iconimage,'',desc)
				
                setView('tvshows', 'Media Info 3')			

def Search_Pandoras_TV():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    filenames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for file_Name in filenames:
        search_URL = Base_Pand + file_Name + CAT
        HTML = OPEN_URL(search_URL)
        match = re.compile('<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(HTML)
        for name,url,img,fanart,mode in match:
            if Search_Name in name.lower():
                addList(name,url,mode,img)
				
                setView('tvshows', 'Media Info 3')			

def Search_Films_Lists():
  
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) 
    Search_Title = Search_Name.lower()
    url = (Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDE1Lw=='))
    url2 = (Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDE0Lw=='))
    url3 = (Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDEzLw=='))
    url4 = (Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDEyLw=='))
	
    HTML = OPEN_URL(url)
    HTML2 = OPEN_URL(url2)
    HTML3 = OPEN_URL(url3)
    HTML4 = OPEN_URL(url4)	
    match = re.compile('<td valign="top"><img src=".+?" alt=".+?"></td><td><a href="(.+?)">(.+?)</a></td>').findall(HTML)
    match2 = re.compile('<td valign="top"><img src=".+?" alt=".+?"></td><td><a href="(.+?)">(.+?)</a></td>').findall(HTML2)
    match3 = re.compile('<td valign="top"><img src=".+?" alt=".+?"></td><td><a href="(.+?)">(.+?)</a></td>').findall(HTML3)
    match4 = re.compile('<td valign="top"><img src=".+?" alt=".+?"></td><td><a href="(.+?)">(.+?)</a></td>').findall(HTML4)
    for url,name in match:
        if Search_Name in name.lower():
            addDir4((name).replace('..&gt;',''),'http://dl.filmiha.com/Movies/2015/' + url,404,'')
				
            setView('tvshows', 'Media Info 3')			
    for url,name in match2:
        if Search_Name in name.lower():
            addDir4((name).replace('..&gt;',''),'http://dl.filmiha.com/Movies/2015/' + url,404,'')
				
            setView('tvshows', 'Media Info 3')			
    for url,name in match3:
        if Search_Name in name.lower():
            addDir4((name).replace('..&gt;',''),'http://dl.filmiha.com/Movies/2015/' + url,404,'')
				
            setView('tvshows', 'Media Info 3')			
    for url,name in match4:
        if Search_Name in name.lower():
            addDir4((name).replace('..&gt;',''),'http://dl.filmiha.com/Movies/2015/' + url,404,'')
				
            setView('tvshows', 'Media Info 3')			

    movie_filenames = ['actionfilm', 'animationfilm', 'biographyfilm', 'christmasfilm', 'classicfilm', 'comedyfilm', 'crimefilm', 'dramafilm', 'familyfilm', 'fantasyfilm', 'historyfilm', 'horrorfilm', 'kidsfilm', 'latestfilms', 'musicfilm', 'romancefilm', 'scififilm' ]

			
    for file_Name2 in movie_filenames:
        search_URL2 = BASE + file_Name2 + CAT
        HTML5 = OPEN_URL(search_URL2)
        print search_URL2
        match5=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(HTML5)
        for url,iconimage,name in match5:
            if Search_Name in name.lower():
                addDir3(name,url,401,iconimage,'','')
				
                setView('tvshows', 'Media Info 3')			

def Search_TV_Lists():
	
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) 
    Search_Title = Search_Name.lower()
    url = (Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDE1Lw=='))
    url2 = (Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDE0Lw=='))
    url3 = (Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDEzLw=='))
    url4 = (Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDEyLw=='))
	
    HTML = OPEN_URL(url)
    HTML2 = OPEN_URL(url2)
    HTML3 = OPEN_URL(url3)
    HTML4 = OPEN_URL(url4)	
    match = re.compile('<td valign="top"><img src=".+?" alt=".+?"></td><td><a href="(.+?)">(.+?)</a></td>').findall(HTML)
    match2 = re.compile('<td valign="top"><img src=".+?" alt=".+?"></td><td><a href="(.+?)">(.+?)</a></td>').findall(HTML2)
    match3 = re.compile('<td valign="top"><img src=".+?" alt=".+?"></td><td><a href="(.+?)">(.+?)</a></td>').findall(HTML3)
    match4 = re.compile('<td valign="top"><img src=".+?" alt=".+?"></td><td><a href="(.+?)">(.+?)</a></td>').findall(HTML4)
    for url,name in match:
        if Search_Name in name.lower():
            addDir4((name).replace('..&gt;',''),'http://dl.filmiha.com/Movies/2015/' + url,404,'')
				
            setView('tvshows', 'Media Info 3')			
    for url,name in match2:
        if Search_Name in name.lower():
            addDir4((name).replace('..&gt;',''),'http://dl.filmiha.com/Movies/2015/' + url,404,'')
				
            setView('tvshows', 'Media Info 3')			
    for url,name in match3:
        if Search_Name in name.lower():
            addDir4((name).replace('..&gt;',''),'http://dl.filmiha.com/Movies/2015/' + url,404,'')
				
            setView('tvshows', 'Media Info 3')			
    for url,name in match4:
        if Search_Name in name.lower():
            addDir4((name).replace('..&gt;',''),'http://dl.filmiha.com/Movies/2015/' + url,404,'')
				
            setView('tvshows', 'Media Info 3')			

    tv_filenames = []

			
    for file_Name2 in tv_filenames:
        search_URL2 = BASE + file_Name2 + CAT
        HTML5 = OPEN_URL(search_URL2)
        print search_URL2
        match5=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(HTML5)
        for url,iconimage,name in match5:
            if Search_Name in name.lower():
                addDir3(name,url,401,iconimage,'','')
				
                setView('tvshows', 'Media Info 3')			


	
def addList(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def auto_View(Vmode = ''):
	xbmc.executebuiltin("Container.SetViewMode(" + Vmode +")")

def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)
		
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def addDir3(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==19 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

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

def Resolve(name, url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass

def addDir4(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

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
