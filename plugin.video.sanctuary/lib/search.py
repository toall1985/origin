import re, process, urllib, urllib2, xbmc, xbmcgui, base64, sys, xbmcplugin

freeview_py = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/lib/freeview/freeview.py')
Dialog = xbmcgui.Dialog()
dp =  xbmcgui.DialogProgress()
Decode = base64.decodestring
addon_handle = int(sys.argv[1])
Base_Pand = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv'))
Pans_files_Movies = ['hey1080p','hey3D','hey','480p','720p','1080p','mova', 'movb', 'movc', 'movd', 'move', 'movf', 'movg', 'movh', 'movi', 'movj', 'movk', 'movl', 'movm', 'movn', 'movo', 'movp', 'movq', 'movr', 'movs', 'movt', 'movu', 'movv', 'movw', 'movx', 'movy', 'movz','720paction','720padventure','720panimation','720pcomedy','720pcrime','720pdocumentary','720pdrama','720pfamily','720pfantasy','720phorror','720pmystery','720promance','720psci-Fi','720psport','720pthriller','720pwestern','1080paction','1080padventure','1080panimation','1080pcomedy','1080pcrime','1080pdocumentary','1080pdrama','1080pfamily','1080pfantasy','1080phorror','1080pmystery','1080promance','1080psci-Fi','1080psport','1080pthriller','1080pwestern','top10action','top10animation','top10biography','top10comedy','top10crime','top10documentary','top10drama','top10family','top10fantasy','top10horror','top10music','top10mystery','top10romance','top10sci-fi','top10sport','top10thriller','top10western','seasonmoviecollection','4Kmovies']
Pans_files_TV = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Search_Menu():
    process.Menu('TV','TV',1501,'','','','')
    process.Menu('Movies','Movies',1501,'','','','')
    process.Menu('Live TV','Live TV',1501,'','','','')
    process.Menu('Cartoons','cartoon',1501,'','','','')
    process.Menu('Football Team','Football',1501,'','','','')
    process.Menu('Audiobooks','Music',1501,'','','','')

    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Search_Input(url):
    Dialog = xbmcgui.Dialog()
    Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search_title.lower()
    if Search_name == '':
        pass
    else:
        if url == 'TV':
            TV(Search_name)
        elif url == 'Movies':
            Movies(Search_name)
        elif url == 'cartoon':
            Cartoons(Search_name)
        elif url == 'Football':
            Football(Search_name)
        elif url == 'Live TV':
            Live_TV(Search_name)
        elif url == 'Music':
            Music(Search_name)
        else:
            process.Menu('NOT WORKING - '+extra,'','','','','','')
		
def Movies(Search_name):
    dp.create('Checking for streams')
    dp.update(20,'',"Checking Pandoras Box",'Please Wait')
    Pans_Search_Movies(Search_name)
    dp.update(40,'',"Checking Apprentice",'Please Wait')
    Apprentice_Search(Search_name,'http://herovision.x10host.com/search/searchmov.php')
    dp.update(60,'',"Checking Raider",'Please Wait')
#    Raider_Loop(Search_name,'http://tombraiderbuilds.co.uk/addon/mainmovies/mainmovies.txt')
    dp.update(80,'',"Checking Joker",'Please Wait')
    Raider_Loop(Search_name,'http://jokerswizard.esy.es/joker/data/quality/quality.txt')
    dp.update(100,'',"Finished checking",'Please Wait')
    dp.close()
	
def TV(Search_name):
    dp.create('Checking for streams')
    dp.update(25,'',"Checking Pandoras Box",'Please Wait')
    Pans_Search_TV(Search_name) 
    dp.update(50,'',"Checking Apprentice",'Please Wait')
    Apprentice_Search(Search_name,'http://herovision.x10host.com/search/searchtv.php')
    dp.update(75,'',"Checking Origin",'Please Wait')
    Search_WatchSeries(Search_name)
    dp.update(100,'',"Finished checking",'Please Wait')
    dp.close()

def Search_GetUpStandUp(Search_name):
    filename = ['Movies','yt_standup_playlist','TV_Shows']
    for file_name in filename:
        Search_Url = 'http://herovision.x10host.com/GetUpStandUp/'+file_name+'.php'
        HTML = process.OPEN_URL(Search_Url)
        match = re.compile('<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"').findall(HTML)
        for name,url,mode,image,fanart,desc in match:
            if Search_name in name.lower():
                name = '[COLORred]Origin [/COLOR]' + name
                if image == 'IMAGES':
                    image = ''
                if fanart == 'FANART':
                    fanart = ''
                if '.php' in url:
                    process.Menu(name,url,104,image,fanart,desc,'')
                if mode == 'single':
                    process.Play(name,url,109,image,fanart,desc,'')
                elif mode == 'playlist':
                    process.Menu(name,url,107,image,fanart,desc,'')
                elif mode == 'watchseries':
                    process.Menu(name,url,112,image,fanart,desc,name)
                elif mode == 'normal':
                    process.Play(name,url,105,image,fanart,desc,'')

def Search_WatchSeries(Search_name):
    Search_url = 'http://www.watchseriesgo.to/search/' + (Search_name).replace(' ','%20')
    OPEN = process.OPEN_URL(Search_url)
    match3 = re.compile('<div class="block-left-home-inside col-sm-9 col-xs-12" title=".+?">.+?<a href="(.+?)" title=.+?<img src="(.+?)" alt=.+?<b>(.+?)</b></a><br>(.+?)<br>',re.DOTALL).findall(OPEN)
    for url,img,name,desc in match3:
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        url3 = 'http://www.watchseriesgo.to/' + url
        image = 'http://www.watchseriesgo.to/' + img
        fanart=''
        description = (desc).replace('<b>','').replace('</b>','').replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"').replace('Description: ','').replace('  ','')
        name = '[COLORred]Origin [/COLOR]' + name
        process.Menu(name,url3,305,image,fanart,description,name)		
	
	
def Apprentice_Search(Search_name,url):	
    HTML_app = process.OPEN_URL(url)
    if HTML_app != 'Opened':
        match_app = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML_app)
        for url,img,desc,fanart,name in match_app:
            if Search_name in name.lower():
				name = '[COLORwhitesmoke]Apprentice[/COLOR] '+name
				if 'php' in url:
					process.Menu(name,url,1303,img,fanart,desc,'')
				elif 'playlist' in url:
					process.Menu(name,url,10002,img,fanart,desc,'')
				elif 'watchseries' in url:
					process.Menu(name,url,112,img,fanart,desc,'')
				elif not 'http' in url:
					process.Play(name,url,10003,img,fanart,desc,'')
				else:
					process.Play(name,url,1307,img,fanart,desc,'')
				
def Pans_Search_Movies(Search_name):
    for file_Name in Pans_files_Movies:
        search_URL = Base_Pand + file_Name + '.php'
        HTML = process.OPEN_URL(search_URL)
        if HTML != 'Opened':
            match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML)
            for url,iconimage,desc,fanart,name in match:
                if Search_name in name.lower():
                    name = '[COLOR darkgoldenrod]Pandora [/COLOR]' + name
                    process.Play(name,url,906,iconimage,fanart,desc,'')

def Pans_Search_TV (Search_name):
    for file_Name in Pans_files_TV:
        search_URL2 = Base_Pand + file_Name + '.php'
        HTML = process.OPEN_URL(search_URL2)
        if HTML != 'Opened':
            match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(HTML)
            for name,desc,url,img,fanart,mode in match:
                if Search_name in name.lower():
                    name = '[COLOR darkgoldenrod]Pandora [/COLOR]' + name
                    process.Menu(name,url,mode,img,fanart,desc,'')
					
	
def Cartoons(Search_name):
    HTML2 = process.OPEN_URL(Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24='))
    match2 = re.compile('<td><a href="(.+?)">(.+)</a></td>').findall(HTML2)
    for url,name in match2:
        if Search_name in name.lower():
            name = '[COLORred]Origin [/COLOR]' + name
            process.Menu(name,url,803,'','','','')
	
def Football(Search_name):
    url = Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS8/cz0=')+(Search_name).replace(' ','+')
    origin_url = Decode('aHR0cDovL3d3dy5mb290YmFsbG9yZ2luLmNvbS8/cz0=')+(Search_name).replace(' ','+')
    Football_Repeat.Origin_Highlights(origin_url)
    Football_Repeat.Get_the_rows(url,'')
	
def Music(Search_name):			
    HTML4 = process.OPEN_URL(Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ=='))
    match4 = re.compile('<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>',re.DOTALL).findall(HTML4)
    for url,name in match4:
        if Search_name in name.lower():			
            name = '[COLORred]Origin [/COLOR]' + (name).replace('\n',' ').replace('	','')
            if '</a>' in name:
                pass
            elif '(' in name:
                process.Menu((name).replace('&nbsp;','').replace('  ','').replace('+','').replace('.mp3',''),Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=') + url,605,'','','','')
            else:
                process.Play((name).replace('&nbsp;','').replace('  ','').replace('+','').replace('.mp3',''),Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=') + url,604,'','','','')
    HTML5 = process.OPEN_URL('https://www.youtube.com/user/audiobooksfree/playlists')
    block = re.compile('<ul class="yt-lockup-meta-info">(.+?)<div class="yt-lockup-meta">',re.DOTALL).findall(HTML5)
    for item in block:
        name = re.compile('dir="ltr" title="(.+?)"').findall(str(item))
        for name in name:
            name = (name).replace('	','').replace('&#39;','\'')
        url = re.compile('<a href="(.+?)" class="yt-pl-thumb-link yt-uix-sessionlink').findall(str(item))
        for url in url:
            url = 'https://www.youtube.com'+url
        image = re.compile('data-thumb="(.+?)"').findall(str(item))
        for image in image:
            image = image
        if Search_name in name.lower():
            name = '[COLORred]Origin [/COLOR]' + str(name)		
            process.Menu(name,str(url),10001,str(image),'','','')   
				
def Live_TV(Search_name):
    dp.create('Checking for streams')
    Oblivion_list = ['FreeSports.m3u','FreeKids.m3u','FreeMovies.m3u','FreeUK.m3u','FreeUS.m3u']
    Joker_live_list = ['http://jokerswizard.esy.es/joker/data/sports/sports.txt','http://jokerstv.no-ip.org/data/livetv/worldtv.xml','http://jokerstv.no-ip.org/data/livetv/news.xml',
	'http://jokerstv.no-ip.org/data/livetv/iptv.xml']
    Raider_live_list = ['http://tombraiderbuilds.co.uk/addon/skysportslive/skysportslive.txt','http://tombraiderbuilds.co.uk/addon/beinsportslive/beinsportslive.txt',
	'http://tombraiderbuilds.co.uk/addon/sportschannels/sportschannels.txt','http://tombraiderbuilds.co.uk/addon/btsportslive/btsportslive.txt']
    HTML = open(freeview_py).read()
    block = re.compile('def CATEGORIES(.+?)#4Music',re.DOTALL).findall(HTML)
    match = re.compile("addLink\('(.+?)','(.+?)',(.+?),(.+?)\)").findall(str(block))
    dp.update(0,'',"Checking Freeview",'Please Wait')
    for name,url,mode,img in match:
    	if Search_name in name.lower():
            from freeview.freeview import addLink
            addLink('[COLORred]Freeview [/COLOR]'+name,url,mode,img)
    dp.update(25,'',"Checking Oblivion",'Please Wait')
    for item in Oblivion_list:
        from pyramid._EditOblivion import MainBase as OblivionMain
        Raider_Live_Loop(Search_name,(OblivionMain).replace('Free.xml',item))
    dp.update(50,'',"Checking Joker",'Please Wait')
    for item in Joker_live_list:
        Raider_Live_Loop(Search_name,item)
#    dp.update(75,'',"Checking Raider",'Please Wait')
#    for item in Raider_live_list:
#        Raider_Live_Loop(Search_name,item)
    dp.update(100,'',"Finished checking",'Please Wait')
    dp.close()


def Raider_Live_Loop(Search_name,url):
    if 'joker' in url:
        ADD_NAME = '[COLORgreen]Joker[/COLOR]'
    if 'raider' in url:
        ADD_NAME = '[COLORblue]Raider[/COLOR]'
    if 'oblivion' in url:
        ADD_NAME = '[COLORlightblue]Oblivion[/COLOR]'
    HTML = process.OPEN_URL(url)
    loop = re.compile('<name>.+?</name>.+?<thumbnail>.+?</thumbnail>.+?<externallink>(.+?)</externallink>.+?<fanart>.+?</fanart>',re.DOTALL).findall(HTML)
    for url in loop:
        Raider_Live_Loop(Search_name,url)
    match = re.compile('<title>(.+?)</title>.+?<sportsdevil>(.+?)</sportsdevil>.+?<thumbnail>(.+?)</thumbnail>',re.DOTALL).findall(HTML)
    for name,url,img in match: 
    	if Search_name in name.lower():
            from pyramid.pyramid import addLink
            url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +url
            addLink(url, ADD_NAME + ' ' +name,img,'','','','','',None,'',1)
    match2 = re.compile(r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)').findall(HTML)
    for ignore,name,url in match2:
    	if Search_name in name.lower():
            if 'http' in url:
                from pyramid.pyramid import addLink
                addLink(url,ADD_NAME + ' ' +name,'','','','','','',None,'',1)


def Raider_Loop(Search_name,url):
    if 'joker' in url:
        ADD_NAME = '[COLORgreen]Joker[/COLOR]'
    if 'raider' in url:
        ADD_NAME = '[COLORblue]Raider[/COLOR]'
    HTML = process.OPEN_URL(url)
    if HTML != 'Failed':
        match = re.compile('<channel>.+?<name>(.+?)</name>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>.+?<fanart>(.+?)</fanart>.+?</channel>',re.DOTALL).findall(HTML)
        for name,image,url,fanart in match:
            if not 'http:' in url:
                pass
            else:
                Raider_Loop(Search_name,url)
        match2 = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>',re.DOTALL).findall(HTML)
        for name,url,image,fanart in match2:
            if 'http:' in url:
                if Search_name.lower() in name.lower():
                    from pyramid.pyramid import addLink
                    addLink(url, ADD_NAME + ' ' +name,image,fanart,'','','','',None,'',1)
                            
