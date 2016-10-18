import urllib2,re,os,xbmc,xbmcplugin,xbmcaddon,xbmcgui,urlparse,urllib,sys,base64, process

addon_handle = int(sys.argv[1])
Decode = base64.decodestring
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
BASE = Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=')
Dialog = xbmcgui.Dialog()

def Big_Kids_Main_Menu():

    process.Menu('Cartoons','',801,ICON,FANART,'','')
    process.Menu('Search Cartoons','',802,ICON,FANART,'','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
	
def Search():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name.lower()
    HTML = process.OPEN_URL(BASE)
    match = re.compile('<td><a href="(.+?)">(.+)</a></td>').findall(HTML)
    for url,name in match:
        if Search_Name in name.lower():
            process.Menu(name,url,803,ICON,FANART,'','')
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

def TESTCATS():
    html=process.OPEN_URL(BASE)
    match = re.compile('<td><a href="(.+?)">(.+)</a></td>').findall(html)
    for url,name in match:
        process.Menu(name,url,803,ICON,FANART,'','')
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
    
def LISTS(url):
    html=process.OPEN_URL(url)
    match2 = re.compile('<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />').findall(html)
    for img in match2:
        IMAGE = img
    match = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
        process.Play(name,url,804,IMAGE,FANART,'','')
    match3 = re.compile('<li><a href="(.+?)">Next</a></li>').findall(html)
    for url in match3:
	    process.Menu('NEXT PAGE',url,804,IMAGE,FANART,'','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
	

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def LISTS2(url,IMAGE):
    html=process.OPEN_URL(url)
    match = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html)
    for name,url in match:
        print name + '     ' + url
        if 'panda' in url:
            LISTS3(url)
#second available playlink includes 'easy'        

	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);			
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

def LISTS3(url):
    html=process.OPEN_URL(url)
    match = re.compile("url: '(.+?)',").findall(html)
    for url in match:
        process.Big_Resolve(url)	
