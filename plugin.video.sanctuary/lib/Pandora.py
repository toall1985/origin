'''This section was kindly donated by the dev of the addon, join his fb group to say thanks for this amazing section - https://www.facebook.com/groups/120495048374613/'''


import re, xbmcplugin, xbmcgui, process, base64, sys, urllib

addon_handle = int(sys.argv[1])
Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
CAT=Decode('LnBocA==')
Base_Pand = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv'))

def Pandora_Main():
    
    process.Menu('[COLOR darkgoldenrod][I]Open Pandora\'s Box[/I][/COLOR]','',901,'https://s32.postimg.org/ov9s6ipf9/icon.png','','','')
    process.Menu('[COLOR darkgoldenrod][I]Search[/I][/COLOR]','',903,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png','','','')

    xbmcplugin.setContent(addon_handle, 'movies')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))		
def Search_Menu():
	process.Menu('[COLOR darkgoldenrod][I]Search Pandoras Films[/I][/COLOR]','',904,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png','','','')
	process.Menu('[COLOR darkgoldenrod][I]Search Pandoras TV[/I][/COLOR]','',905,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png','','','')

	xbmcplugin.setContent(addon_handle, 'movies')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

	
def Pandoras_Box():

    html=process.OPEN_URL(Base_Pand +Decode('c3BvbmdlbWFpbi5waHA='))
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
            process.Menu(name,url,mode,img,fanart,desc,'')

    xbmcplugin.setContent(addon_handle, 'movies')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
			
			
def Pandora_Menu(url):
        
        link = process.OPEN_URL(url)
        match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,desc,background,name in match:
            process.PLAY(name,url,906,iconimage,background,desc,'')
            xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Search_Pandoras_Films():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name.lower()
    filenames = ['hey1080p','hey3D','hey','480p','720p','1080p','mova', 'movb', 'movc', 'movd', 'move', 'movf', 'movg', 'movh', 'movi', 'movj', 'movk', 'movl', 'movm', 'movn', 'movo', 'movp', 'movq', 'movr', 'movs', 'movt', 'movu', 'movv', 'movw', 'movx', 'movy', 'movz','720paction','720padventure','720panimation','720pcomedy','720pcrime','720pdocumentary','720pdrama','720pfamily','720pfantasy','720phorror','720pmystery','720promance','720psci-Fi','720psport','720pthriller','720pwestern','1080paction','1080padventure','1080panimation','1080pcomedy','1080pcrime','1080pdocumentary','1080pdrama','1080pfamily','1080pfantasy','1080phorror','1080pmystery','1080promance','1080psci-Fi','1080psport','1080pthriller','1080pwestern','top10action','top10animation','top10biography','top10comedy','top10crime','top10documentary','top10drama','top10family','top10fantasy','top10horror','top10music','top10mystery','top10romance','top10sci-fi','top10sport','top10thriller','top10western']
    for file_Name in filenames:
        search_URL = Base_Pand + file_Name + CAT
        HTML = process.OPEN_URL(search_URL)
        if HTML != 'Opened':
            match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML)
            for url,iconimage,desc,fanart,name in match:
                if Search_Name in name.lower():
                    process.PLAY(name,url,906,iconimage,fanart,desc,'Pans')
					
                    xbmcplugin.setContent(addon_handle, 'movies')
                    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
				
				
def Search_Pandoras_TV():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name.lower()
    filenames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for file_Name in filenames:
        search_URL2 = Base_Pand + file_Name + CAT
        HTML = process.OPEN_URL(search_URL2)
        if HTML != 'Opened':
            match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(HTML)
            for name,desc,url,img,fanart,mode in match:
                if Search_Name in name.lower():
                    process.Menu(name,url,mode,img,fanart,desc,'')
					
                    xbmcplugin.setContent(addon_handle, 'movies')
                    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

			
def open_Menu(url):

    html=process.OPEN_URL(url)
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
        process.Menu(name,url,mode,img,fanart,desc,'')

        xbmcplugin.setContent(addon_handle, 'movies')
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
    xbmcplugin.endOfDirectory(int(sys.argv[1]))