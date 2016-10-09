import re, process, urllib, urllib2, xbmcgui, base64, Football_Repeat, comedy, yt, Pandora, Big_Kids, multitv, sys, xbmcplugin
from threading import Thread
from pyramid import pyramid
Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
addon_handle = int(sys.argv[1])
Base_Pand = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv'))
Pans_files_Movies = ['hey1080p','hey3D','hey','480p','720p','1080p','mova', 'movb', 'movc', 'movd', 'move', 'movf', 'movg', 'movh', 'movi', 'movj', 'movk', 'movl', 'movm', 'movn', 'movo', 'movp', 'movq', 'movr', 'movs', 'movt', 'movu', 'movv', 'movw', 'movx', 'movy', 'movz','720paction','720padventure','720panimation','720pcomedy','720pcrime','720pdocumentary','720pdrama','720pfamily','720pfantasy','720phorror','720pmystery','720promance','720psci-Fi','720psport','720pthriller','720pwestern','1080paction','1080padventure','1080panimation','1080pcomedy','1080pcrime','1080pdocumentary','1080pdrama','1080pfamily','1080pfantasy','1080phorror','1080pmystery','1080promance','1080psci-Fi','1080psport','1080pthriller','1080pwestern','top10action','top10animation','top10biography','top10comedy','top10crime','top10documentary','top10drama','top10family','top10fantasy','top10horror','top10music','top10mystery','top10romance','top10sci-fi','top10sport','top10thriller','top10western']
Pans_files_TV = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Search_Menu():
    process.Menu('TV','',1502,'','','','TV')
    process.Menu('Movies','',1501,'','','','Movies')
    process.Menu('Cartoons','',1503,'','','','cartoon')
    process.Menu('Football','',1504,'','','','Football')
    process.Menu('Audiobooks','',1505,'','','','Football')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def Movies():
    Search = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search.lower()
    if Search_name == '':
        pass
    for file_Name in Pans_files_Movies:
        search_URL = Base_Pand + file_Name + '.php'
        HTML = process.OPEN_URL(search_URL)
        if HTML != 'Opened':
            match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML)
            for url,iconimage,desc,fanart,name in match:
                if Search_name in name.lower():
                    name = '[COLORred]Pandora [/COLOR]' + name
                    process.Play(name,url,906,iconimage,fanart,desc,'')
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
    HTML = process.OPEN_URL('http://tombraiderbuilds.co.uk/addon/')
    match = re.compile('<a href="(.+?)">(.+?)</a>').findall(HTML)
    for url2, name in match:
        if '?C' in url2:
            pass
        else:
            url2 = 'http://tombraiderbuilds.co.uk/addon/' + url2
            second_menu(Search_name, url2)
	
def TV():
    Search = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search.lower()
    if Search_name == '':
        pass
    for file_Name in Pans_files_TV:
        search_URL2 = Base_Pand + file_Name + '.php'
        HTML = process.OPEN_URL(search_URL2)
        if HTML != 'Opened':
            match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(HTML)
            for name,desc,url,img,fanart,mode in match:
                if Search_name in name.lower():
                    name = '[COLORred]Pandora [/COLOR]' + name
                    process.Menu(name,url,mode,img,fanart,desc,'')
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
    Search_url = 'http://www.watchseries.ac/search/' + (Search_name).replace(' ','%20')
    OPEN = process.OPEN_URL(Search_url)
    match3 = re.compile('<div class="block-left-home-inside col-sm-9 col-xs-12" title=".+?">.+?<a href="(.+?)" title=.+?<img src="(.+?)" alt=.+?<b>(.+?)</b></a><br>(.+?)<br>',re.DOTALL).findall(OPEN)
    for url,img,name,desc in match3:
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        url3 = 'http://www.watchseries.ac' + url
        image = 'http://www.watchseries.ac' + img
        description = (desc).replace('<b>','').replace('</b>','').replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"').replace('Description: ','').replace('  ','')
        name = '[COLORred]Origin [/COLOR]' + name
        process.Menu(name,url3,305,image,fanart,description,name)		
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
def Cartoons():
    Search = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search.lower()
    HTML2 = process.OPEN_URL(Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24='))
    match2 = re.compile('<td><a href="(.+?)">(.+)</a></td>').findall(HTML2)
    for url,name in match2:
        if Search_name in name.lower():
            name = '[COLORred]Origin [/COLOR]' + name
            process.Menu(name,url,803,'','','','')
	
def Football():
    Search = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search.lower()
    url = Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS8/cz0=')+(Search_name).replace(' ','+')
    origin_url = Decode('aHR0cDovL3d3dy5mb290YmFsbG9yZ2luLmNvbS8/cz0=')+(Search_name).replace(' ','+')
    Football_Repeat.Origin_Highlights(origin_url)
    Football_Repeat.Get_the_rows(url,'')
	
def audiobooks():			
    Search = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search.lower()
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
	

def second_menu(Search_name, url2):
    HTML = process.OPEN_URL(url2)
    match = re.compile('<a href="(.+?)">(.+?)</a>').findall(HTML)
    for url3, name in match:
        if 'txt' in url3:
            url4 = url2 + url3
            third_menu(Search_name, url4)
           
def third_menu(Search_name, url4):
    HTML = process.OPEN_URL(url4)
    match = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>',re.DOTALL).findall(HTML)
    for name,url,img in match:
        if '<title>' in name:
            pass
        else:
            if Search_name.lower() in name.lower():
                name = '[COLORred]Raiders [/COLOR]' + name
                pyramid.addLink(url, name,img,'','','','','',None,'',1)
	
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
					
if mode == 900 : Pandora.Pandora_Main()
elif mode == 901 : Pandora.Pandoras_Box()
elif mode == 423 : Pandora.open_Menu(url)
elif mode == 426 : Pandora.Pandora_Menu(url)
elif mode == 903 : Pandora.Search_Menu()
elif mode == 904 : Pandora.Search_Pandoras_Films()
elif mode == 905 : Pandora.Search_Pandoras_TV()
elif mode == 906 : process.Big_Resolve(url)
elif mode == 104 : comedy.Regex(url)
elif mode == 105 : process.Resolve(url)
elif mode == 107 : comedy.grab_youtube_playlist(url)
elif mode == 109 : yt.PlayVideo(url)
elif mode == 112 : comedy.Grab_Season(iconimage,url)
elif mode == 803 : Big_Kids.LISTS(url)
elif mode == 305 : multitv.Grab_Season(url,extra)
elif mode == 1501: Movies()
elif mode == 1502: TV()
elif mode == 1503: Cartoons()
elif mode == 1504: Football()
elif mode == 1505: audiobooks()