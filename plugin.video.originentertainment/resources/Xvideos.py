import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver,sys,Google

Dialog = xbmcgui.Dialog()

def X_vid_Menu():
    addDirFolder('Best Videos','http://www.xvideos.com/best',1005,'','','')
    addDirFolder('Channels','http://www.xvideos.com/channels/all',1005,'','','')
    addDirFolder('Genres','http://www.xvideos.com',1006,'','','')
    addDirFolder('Pornstars','http://www.xvideos.com/pornstars',1004,'','','')
    addDirFolder('Profiles','http://www.xvideos.com/profileslist',1004,'','','')
    addDirFolder('Recently Uploaded','http://xvideos.com',1005,'','','')
    addDirFolder('Search','',1007,'','','',)
    addDirFolder('Tags','http://www.xvideos.com/tags',1003,'','','')
	
def tags(url):
    HTML = OPEN_URL(url)
    next_button = re.compile('<li><a class="nP" href="(.+?)">Next</a></li>').findall(HTML)
    for url in next_button:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,1002,'','','')	
    match = re.compile('<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>').findall(HTML)
    for url,name,no in match:
        addDirFolder(name + ' - No of Videos : ' + (no).replace('>',''),'http://www.xvideos.com'+url,1005,'','','')

def Pornstars(url):
    HTML = OPEN_URL(url)
    next_button = re.compile('<li><a class="nP" href="(.+?)">Next</a></li>').findall(HTML)
    for url in next_button:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,1004,'','','')
    match = re.compile('<p class="profileName">.+?<a href="(.+?)">(.+?)</a>.+?<p class="itemsCounts">\n(.+?)\n.+?<img src="(.+?)"',re.DOTALL).findall(HTML)
    for url,name,vids,img in match:
        addDirFolder(name + ' - No of Vids:' + vids,'http://www.xvideos.com'+url+'#_tabVideos,videos-best',1005,img,'','')        
		
	  
def New_Videos(url):
    HTML = OPEN_URL(url)
    block = re.compile('<div class="pagination ">(.+?)</div>',re.DOTALL).findall(HTML)
    next_button = re.compile('<li><a class="nP" href="(.+?)">Next</a></li>').findall(str(block))
    for url in next_button:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,1005,'','','')
    next_button2 = re.compile('<a href="(.*?)" class="no-page">Next</a>').findall(str(block))
    for url in next_button2:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,1005,'','','')
    match = re.compile('<div class="thumb-inside".+?<a href="(.+?)"><img src="(.+?)" id=".+?title=".+?">(.+?)</a>.+?<span class="duration">(.+?)</span>.+?Porn quality:(.+?)\n</span></p></div></div>',re.DOTALL).findall(HTML)
    for url,img,name,length,rating in match:
        addDir(name + ' - Porn Quality : ' + rating + ' - ' + length,'http://www.xvideos.com'+url,1008,img,img,rating + ' - ' + length)	

def Genres(url):
    HTML = OPEN_URL(url)
    block = re.compile('<div class="main-categories">(.+?)</div>',re.DOTALL).findall(HTML)
    next_button = re.compile('<li><a class="nP" href="(.+?)">Next</a></li>').findall(HTML)
    for url in next_button:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,1006,'','','')
    match = re.compile('<li><a href="(.+?)" class="btn btn-default">(.+?)</a>').findall(str(block))
    for url,name in match:
	    addDirFolder(name,'http://www.xvideos.com'+url,1005,'','','')

		
def Search_X():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name.lower()
    Search_URL = 'http://www.xvideos.com/?k=' + Search_Title
    HTML = OPEN_URL(Search_URL)
    block = re.compile('<div class="pagination ">(.+?)</div>',re.DOTALL).findall(HTML)
    next_button = re.compile('<li><a class="nP" href="(.+?)">Next</a></li>').findall(HTML)
    for url in next_button:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,1005,'','','')
    next_button2 = re.compile('<a href="(.*?)" class="no-page">Next</a>').findall(str(block))
    for url in next_button2:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,1005,'','','')
    match = re.compile('<div class="thumb-inside".+?<a href="(.+?)"><img src="(.+?)" id=".+?title=".+?">(.+?)</a>.+?<span class="duration">(.+?)</span>.+?Porn quality:(.+?)\n</span></p></div></div>',re.DOTALL).findall(HTML)
    for url,img,name,length,rating in match:
        addDirFolder(name + ' - Porn Quality : ' + rating + ' - ' + length,'http://www.xvideos.com'+url,1008,img,img,rating + ' - ' + length)	

def PlayLink(url):
    HTML = OPEN_URL(url)
    match = re.compile('flv_url=(.+?)\;').findall(HTML)
    for url in match:
        URL2 = (url).replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('&amp','')
        ResolveTwo(URL2)
		
def ResolveTwo(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

		
def addDir(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDirFolder(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
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
 