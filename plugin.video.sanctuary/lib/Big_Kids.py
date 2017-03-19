import urllib2,re,os,xbmc,xbmcplugin,xbmcaddon,xbmcgui,urlparse,urllib,sys,base64, process, random

addon_handle = int(sys.argv[1])
Decode = base64.decodestring
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
BASE = Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=')
Dialog = xbmcgui.Dialog()

def Big_Kids_Main_Menu():

    process.Menu('Cartoons','',801,ICON,FANART,'','')
    process.Menu('Cartoons and Movies','',806,ICON,FANART,'','')
    process.Menu('Search Cartoons','',802,ICON,FANART,'','')
    process.Menu('24/7','',812,ICON,FANART,'','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

def Random_Lists():
    process.Menu('24/7 Search Cartoon','',818,ICON,FANART,'','')	
    process.Random_play('24/7 Random Cartoon',813,url=BASE,image=ICON,isFolder=False)
    process.Menu('24/7 Select Cartoon','',817,ICON,FANART,'','')
    process.Random_play('20 Random Movies',814,url='http://www.animetoon.org/movies',image=ICON,isFolder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	
	
def Search_247():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    HTML = process.OPEN_URL(BASE)
    match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(HTML)
    for url2,name in match:
        if Search_Name.replace(' ','').replace('\'','').replace('-','').lower() in name.replace(' ','').replace('\'','').replace('-','').lower():
			process.Random_play(name,816,url=url2,isFolder=False)
    HTML2 = process.OPEN_URL('https://www.watchcartoononline.io/cartoon-list')
    match = re.compile('<li><a href="(.+?)" title=".+?">(.+?)</a>').findall(HTML2)
    for url, name in match:
        if Search_Name.replace(' ','').replace('\'','').replace('-','').lower() in name.replace(' ','').replace('\'','').replace('-','').lower():
			process.Random_play(name,816,url=url,isFolder=False)

def Random_Cartoon(url):
    Playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    Playlist.clear()
    Counter = []
    full_count = []
    Prog_Name = [] 
    html=process.OPEN_URL(url) 
    match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(html) 
    for url,name in match: 
        full_count.append([url,name]) 
        if len(full_count) == len(match): 
            for item in full_count: 
                get_random=random.randint(1,len(full_count)) 
                try: 
                    url_to_add = full_count[int(get_random)] 
                except: 
                    pass 
                if url_to_add[1] not in Prog_Name:
                    Prog_Name.append(url_to_add[1]) 
                    if int(len(Counter)) < 1:
                        Counter.append(url_to_add[1][0])
                        Random_Play_Cartoon(url_to_add[0],url_to_add[1])
                    else:
                        pass
                else:
                    pass
        else:
            pass
			
def twenty47_select():
    html=process.OPEN_URL(BASE)
    match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(html)
    for url,name in match:
		process.Random_play(name,816,url=url,image=ICON,isFolder=False)
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
		
def Random_Movie(url):
	Playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	Playlist.clear()
	Full_List = []
	Count = []
	Name = []
	HTML = process.OPEN_URL(url)
	match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(HTML)
	for url2,name in match:
		Full_List.append([url2,name])
		if len(Full_List)==len(match):
			for item in Full_List:
				random_movie=random.randint(1,len(Full_List))
				try:
					next_url = Full_List[int(random_movie)]
				except:
					pass
				if len(Count)<=20:
					if next_url[1] not in Name:
						HTML2 = process.OPEN_URL(next_url[0])
						match3 = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(HTML2) 
						for Playlink_url,Ep_name in match3: 
							HTML4 = process.OPEN_URL(Playlink_url)
							match4 = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(HTML4)
							for ignore,link in match4:
								if 'panda' in link:
									HTML5 = process.OPEN_URL(link)
									match5 = re.compile("url: '(.+?)'").findall(HTML5)
									for finally_got_there_phew in match5:
										if 'http' in finally_got_there_phew:
											liz = xbmcgui.ListItem(next_url[1], iconImage=ICON, thumbnailImage=ICON)
											liz.setInfo( type="Video", infoLabels={"Title": next_url[1]})
											liz.setProperty("IsPlayable","true")
											Playlist.add(finally_got_there_phew, liz)
											xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
									
			
		
	
def Random_Play_Cartoon(url,name):
    url = url;name = name
    Playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    Playlist.clear()
    episode_full_count = []
    Ep_Name_List = []
    html2 = process.OPEN_URL(url) 
    match2 = re.compile('<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />').findall(html2) 
    for img in match2: 
        IMAGE = img 
    match3 = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(html2) 
    for Playlink_url,Ep_name in match3: 
        episode_full_count.append([Playlink_url,Ep_name]) 
        if len(episode_full_count)==len(match3):
            for item in episode_full_count:
                get_random_ep=random.randint(1,len(episode_full_count))
                try:									
                    next_url_to_use=episode_full_count[int(get_random_ep)]
                    if next_url_to_use[1] not in Ep_Name_List:
                        Ep_Name_List.append(next_url_to_use[1])
                        html3 = process.OPEN_URL(next_url_to_use[0])
                        match4 = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html3)
                        for ignore,final_playlink_get in match4:
                            if 'panda' in final_playlink_get:
                                html4 = process.OPEN_URL(final_playlink_get)
                                match5 = re.compile("url: '(.+?)'").findall(html4)
                                for finally_got_there_phew in match5:
                                    if 'http' in finally_got_there_phew:
                                        liz = xbmcgui.ListItem(next_url_to_use[1], iconImage=IMAGE, thumbnailImage=IMAGE)
                                        liz.setInfo( type="Video", infoLabels={"Title": next_url_to_use[1]})
                                        liz.setProperty("IsPlayable","true")
                                        Playlist.add(finally_got_there_phew, liz)
                                        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                                    else:
                                        pass
                            else:
                                pass
                    else:
                        pass
                except:
                    pass
        else:
            pass
                    
	
def watch_cartoon_menu():
    process.Menu('Cartoons','https://www.watchcartoononline.io/cartoon-list',807,ICON,FANART,'','')
    process.Menu('Movies','https://www.watchcartoononline.io/movie-list',809,ICON,FANART,'','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

def watch_cartoon_grab_episode(url):
	html = process.OPEN_URL(url)
	match = re.compile('<li><a href="(.+?)" title=".+?">(.+?)</a>').findall(html)
	for url, name in match:
		name = name.replace('&#8217;','\'').replace('&#8216;','\'').replace('&#038;','&').replace('&#8211;','-')
		if '<' in name:
			pass
		else:
			process.Menu(name,url,810,ICON,FANART,'','')
			
def watch_cartoon_grab_episode_second(url):
	html = process.OPEN_URL(url)
	match = re.compile('<li><a href="(.+?)" rel="bookmark" title=".+?" class="sonra">(.+?)</a>').findall(html)
	for url, name in match:
		name = name.replace('&#8217;','\'').replace('&#8216;','\'').replace('&#038;','&').replace('&#8211;','-')
		if '<' in name:
			pass
		else:
			process.Play(name,url,808,ICON,FANART,'','')
			
def watch_cartoon_grab_movies(url):
	html = process.OPEN_URL(url)
	match = re.compile('<li><a href="(.+?)" title=".+?">(.+?)</a>').findall(html)
	for url, name in match:
		name = name.replace('&#8217;','\'').replace('&#8216;','\'').replace('&#038;','&').replace('&#8211;','-')
		if '<' in name:
			pass
		else:
			process.Play(name,url,808,ICON,FANART,'','')
			
def watch_cartoon_final(url):
	url = url.replace('www','m')
	html = process.OPEN_URL(url)
	playlink = re.compile('<source src="(.+?)"').findall(html)
	for play in playlink:
		Resolve(play)

	
def Search_cartoons():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    HTML = process.OPEN_URL(BASE)
    match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(HTML)
    for url,name in match:
        if Search_Name.replace(' ','').replace('\'','').replace('-','').lower() in name.replace(' ','').replace('\'','').replace('-','').lower():
            process.Menu('Source 1 - '+name,url,3,ICON,FANART,'','')
    HTML2 = process.OPEN_URL('https://www.watchcartoononline.io/cartoon-list')
    match = re.compile('<li><a href="(.+?)" title=".+?">(.+?)</a>').findall(HTML2)
    for url, name in match:
        if Search_Name.replace(' ','').replace('\'','').replace('-','').lower() in name.replace(' ','').replace('\'','').replace('-','').lower():
			process.Menu(name,url,810,ICON,FANART,'','')

def Search_movies():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    HTML = process.OPEN_URL('https://www.watchcartoononline.io/movie-list')
    match = re.compile('<li><a href="(.+?)" title=".+?">(.+?)</a>').findall(HTML)
    for url, name in match:
        name = name.replace('&#8217;','\'').replace('&#8216;','\'').replace('&#038;','&').replace('&#8211;','-')
        if '<' in name:
            pass
        else:
            if Search_Name.replace(' ','').replace('\'','').replace('-','').lower() in name.replace(' ','').replace('\'','').replace('-','').lower():
				process.Play(name,url,808,ICON,FANART,'','')
	
	
def TESTCATS():
    html=process.OPEN_URL(BASE)
    match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(html)
    for url,name in match:
		process.Menu(name,url,803,ICON,FANART,'','')
    
def LISTS(url):
    html=process.OPEN_URL(url)
    match2 = re.compile('<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />').findall(html)
    for img in match2:
        IMAGE = img
    match = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
		process.Menu(name,url,804,IMAGE,FANART,'','')
    match3 = re.compile('<li><a href="(.+?)">Next</a></li>').findall(html)
    for url in match3:
		process.Menu('NEXT PAGE',url,803,IMAGE,FANART,'','')

def LISTS2(url,IMAGE):
    sources = []
    html=process.OPEN_URL(url)
    match = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html)
    for name,url2 in match:
        if 'panda' in url2:
            HTML = process.OPEN_URL(url2)
            match2 = re.compile("url: '(.+?)'").findall(HTML)
            for url3 in match2:
                if 'http' in url3:
					sources.append({'source': 'playpanda', 'quality': 'SD', 'url': url3})
        elif 'easy' in url2:
            HTML2 = process.OPEN_URL(url2)
            match3 = re.compile("url: '(.+?)'").findall(HTML2)
            for url3 in match3:
                if 'http' in url3:
					sources.append({'source': 'easyvideo', 'quality': 'SD', 'url': url3})
        elif 'zoo' in url2:
            HTML3 = process.OPEN_URL(url2)
            match4 = re.compile("url: '(.+?)'").findall(HTML3)
            for url3 in match4:
                if 'http' in url3:
					sources.append({'source': 'videozoo', 'quality': 'SD', 'url': url3})
    if len(sources)>=3:
    	choice = Dialog.select('Select Playlink',
	                                [link["source"] + " - " + " (" + link["quality"] + ")"
	                                for link in sources])
        if choice != -1:
            url = sources[choice]['url']
            isFolder=False
            xbmc.Player().play(url)

def LISTS3(url):
    html=process.OPEN_URL(url)
    match = re.compile("url: '(.+?)',").findall(html)
    for url in match:
        process.Resolve(url)
