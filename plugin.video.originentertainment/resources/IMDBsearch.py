import urllib, urllib2, re, Google
import urllib,urllib2, re, os, sys, HTMLParser, control
from bs4 import BeautifulSoup
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
Dialog = xbmcgui.Dialog()
addon_handle = int(sys.argv[1])


def class IMDB:
	def Get_imdb_movie_search():
		Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
		SEARCH_NAME = Search_Name
		Search_Title = Search_Name.lower()
		search_URL = 'http://www.imdb.com/find?ref_=nv_sr_fn&q=' + (Search_Name).replace(' ','+') + '&s=all'
		HTML = OPEN_URL(search_URL)
		match = re.compile('<td class=".+?"> <a href="(.+?)" ><img src="(.+?)" /></a> </td> <td class="result_text"> <a href=".+?" >(.+?)</a>.+?</td>',re.DOTALL).findall(HTML)
		for url,img,name in match:
			addDir3(name,'http://www.imdb.com' + url,107,(img).replace('UX32_CR0,0,32,44','UY1200_CR89,0,800,1200').replace('UY44_CR0,0,32,44','UY1200_CR126,0,800,1200').replace('UY44_CR11,0,32,44','UY1200_CR435,0,800,1200'),'','')
		
		   
	def Get_movie(SEARCH_NAME,url,iconimage):
		HTML = OPEN_URL(url)
		SEARCH_NAME2 = SEARCH_NAME
		match = re.compile(' <link rel=\'image_src\' href="(.+?)">.+?<meta property=\'og:title\' content="(.+?)" />.+?<meta name="description" content="(.+?)" />',re.DOTALL).findall(HTML)
		for img,name,desc in match:
			addDir3(name,'',111,img,'',desc)
			
		setView('tvshows', 'Media Info 3')
		else:
			match2 = re.compile('<a href="/title/(.+?)/episodes.+?season=(.+?)"\n>(.+?)</a>').findall(HTML)
			for chn,url,name in match2:
				addDir3('Season - ' + name,'http://www.imdb.com/title/' + chn + '/episodes?season=' + url,108,img,'','')
			
				xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
			
				setView('tvshows', 'List')

		
				
	def Get_imdb_TV_Episode(SEARCH_NAME2,url):
		SEARCH_NAME3 = SEARCH_NAME2
		HTML = OPEN_URL(url)
		match = re.compile('<img width.+?class=".+?" alt=".+?" src="(.+?)">\n<div>(.+?)</div>.+?itemprop="name">(.+?)</a>.+?itemprop="description">\n(.+?)</div>',re.DOTALL).findall(HTML)
		for img,ep,name,desc in match:
			EP = ep
			addDir3(ep + '  :  ' + name,'',111,img,'',desc)
			Final_Name = (SEARCH_NAME3).replace(' ','+') + '+' + EP
		   
			
		
		setView('tvshows', 'Media Info 3')

	# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Alluc Part Begins >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	def find_Alluc_Link(Final_Name):
		search_URL_Cleaned = 'http://www.alluc.ee/stream/' + (Final_Name).replace(' ','+').replace(',','%2C').replace(' : ','%3A') + 'host%3Aallmyvideos.net'
		HTML = OPEN_URL(search_URL_Cleaned)
		print '>>>>>>>>SEARCH URL CLEANED>>>>>>>>' + search_URL_Cleaned +'<<<<<<<<<<<<<SEARCH URL CLEANED<<<<<<<<<<<<<<<'
		match = re.compile('<div class="title"><!--<h2>--><a href="(.+?)"   title=".+?" >(.+?)</a>',re.DOTALL).findall(HTML)
		for url,name in match:
			addDir4(name,'http://alluc.ee' + url,91,'')#wlist search result
			print '>>>>>>>>>>>>>>>>' + url +'<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
	#http://www.alluc.ee/stream/s1%2C+ep1+%3A+the+one+where+monica+gets+a+roommate+host%3Aallmyvideos.net		
	# need that episode to be included in the search mate to bring back

	# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.. Alluc part ends >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>	
	
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
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
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
