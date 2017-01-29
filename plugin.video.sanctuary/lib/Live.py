import process, re, requests, threading, xbmc, xbmcgui, os

Stream_file = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.sanctuary/streams.txt')
Addon_data = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.sanctuary/')
def Live_Menu():
    process.Menu('By Country','',20,'','','','')
    process.Menu('M3u8 Lists','',23,'','','','')


def Live_Main():
	HTML = requests.get('http://www.shadow-net.org').text
	match = re.compile('<li class=""><a href="(.+?)">(.+?)</a>').findall(HTML)
	for url, name in match:
		name = name.replace('&amp;','&')
		if 'p2p' in name.lower():
			pass
		else:
			process.Menu(name,url,21,'','','','')
		
def Get_Channel(url):
	List = []
	HTML = requests.get(url).text
	block = re.compile('<div class="Block CategoryContent Moveable Panel"(.+?)<br class="Clear" />',re.DOTALL).findall(HTML)
	for item in block:
		match = re.compile('<div class="ProductImage">.+?<a href="(.+?)".+?img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(str(item.encode('utf-8')))
		for url,image,name in match:
			process.PLAY(name,url,22,image,'','','')
	next = re.compile('<div class="FloatRight"><a href="(.+?)">.+?</a>').findall(HTML)
	for url in next:
		if 'skippy' not in List:
			process.Menu('Next Page',url,21,'','','','')
			List.append('skippy')
			
def Get_Playlink(name,url):
	playlink = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
	HTML = requests.get(url).text
	m3u8 = re.compile('<source src="(.+?)"').findall(HTML)
	for item in m3u8:
		playlink = item
	process.Big_Resolve(name,playlink)
	
def Ultra():
	headers = {"User-Agent": "Mozilla/5.0"}
	process.Menu('[COLORwhite]Search All Lists[/COLOR]','',25,'','','','')
	process.Menu('________________________________________________________','',25,'','','','')
	process.Menu('[COLORwhite]Check for response off streams[/COLOR]','',26,'','','','')
	process.Menu('[COLORred]AVERAGE RUN TIME FOR ABOVE IS 30 MINUTES!!!![/COLOR]','',23,'','','','')
	process.Menu('[COLORred]This will check every single stream for a response[/COLOR]','',23,'','','','')
	process.Menu('[COLORred]It will take a while but should only need doing every couple of days[/COLOR]','',23,'','','','')
	process.Menu('[COLORred]It\'s not a guarantee they will work and be perfect just that they exist[/COLOR]','',23,'','','','')
	process.Menu('________________________________________________________','',25,'','','','')
	process.Menu('[COLORwhite]Search pre-checked list of streams - run above first!!![/COLOR]','',27,'','','','')
	process.Menu('________________________________________________________','',25,'','','','')
	process.Menu('[COLORred]Streams are not checked manually so may be hit or miss!!!![/COLOR]','',23,'','','','')
	process.Menu('[COLORred]But enjoy what does work, don\'t enjoy what doesn\'t ;-)[/COLOR]','',23,'','','','')
	process.Menu('________________________________________________________','',25,'','','','')
	HTML = requests.get('http://www.iptvultra.com/',headers=headers).text
	match = re.compile('<span class="link"><a href="(.+?)">(.+?)</a>').findall(HTML)
	for url, name in match:
		process.Menu(name,url,24,'','','','')
		
def Get_Ultra_Channel(url):
	headers = {"User-Agent": "Mozilla/5.0"}
	HTML = requests.get(url,headers=headers).text
	match = re.compile('".+?[@](.+?)[@].+?[@].+?[@](.+?)"').findall(HTML)
	for name,url in match:
		name = name.replace('[','').replace(']','')
		if name[0] == ' ':
			name = name[1:]
		if name[-1] == ' ':
			name = name[:-1]
		url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url='+url.replace('[','').replace(']','')+';name=Sanctuary'
		process.Play(name,url,906,'','','','')


		
def Search_Ultra():
	Dialog = xbmcgui.Dialog()
	Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
	Search_name = Search_title.lower()
	search_next(Search_name)
	
def search_next(name):
	Search_name = name
	headers = {"User-Agent": "Mozilla/5.0"}
	progress = []
	item = []
	result = []
	dp =  xbmcgui.DialogProgress()
	Dialog = xbmcgui.Dialog()
	HTML = requests.get('http://www.iptvultra.com/',headers=headers).text
	match = re.compile('<span class="link"><a href="(.+?)">(.+?)</a>').findall(HTML)
	for url, name in match:
		item.append(url[0])
		items = len(item)
	for url, name in match:
		progress.append(url[0])
		dp_add = len(progress) / float(items) * 100
		dp.create('Checking for stream')
		dp.update(int(dp_add),'Checking list '+str(len(progress))+'/'+str(len(match)),str(len(result))+' Results')
		if dp.iscanceled():
			return
		HTML2 = requests.get(url,headers=headers).text
		match2 = re.compile('".+?[@](.+?)[@].+?[@].+?[@](.+?)"').findall(HTML2)
		for name,url2 in match2:
			name = name.replace('[','').replace(']','')
			if name[0] == ' ':
				name = name[1:]
			if name[-1] == ' ':
				name = name[:-1]
			playlink = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url='+url2.replace('[','').replace(']','')+';name=Sanctuary'
			if (Search_name).replace(' ','') in (name).replace(' ','').lower():
				result.append(url[0])
				try:
					process.Play(name,playlink,906,'','','','')
				except:
					pass
				
def Check_For_200_Response():
	headers = {"User-Agent": "Mozilla/5.0"}
	progress = []
	item = []
	result = []
	dp =  xbmcgui.DialogProgress()
	HTML = requests.get('http://www.iptvultra.com/',headers=headers).text
	match = re.compile('<span class="link"><a href="(.+?)">(.+?)</a>').findall(HTML)
	for url, name in match:
		item.append(url[0])
		items = len(item)
	for url, name in match:
		progress.append(url[0])
		dp_add = len(progress) / float(items) * 100
		dp.create('Checking for stream')
		dp.update(int(dp_add),'Checking list '+str(len(progress))+'/'+str(len(match)),str(len(result))+' Results')
		if dp.iscanceled():
			return
		HTML2 = requests.get(url,headers=headers).text
		match2 = re.compile('".+?[@](.+?)[@].+?[@].+?[@](.+?)"').findall(HTML2)
		for name,url2 in match2:
			name = name.replace('[','').replace(']','')
			if name[0] == ' ':
				name = name[1:]
			if name[-1] == ' ':
				name = name[:-1]
			try:
				final_url = url2.replace(']','').replace(']','')
				try:
					r = requests.head(final_url,timeout=0.05)
				except:
					pass
				if '200' in str(r.status_code):
					result.append(url[0])
					playlink = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url='+final_url+';name=Sanctuary'
					if not os.path.exists(Addon_data):
						os.makedirs(Addon_data)
					if not os.path.exists(Stream_file):
						print_text_file = open(Stream_file,"w")
						print_text_file.write('<NAME=>'+name+'</NAME><URL=>'+playlink+'</URL>\n')
					else:
						print_text_file = open(Stream_file,"a")
						print_text_file.write('<NAME=>'+name+'</NAME><URL=>'+playlink+'</URL>\n')
			except:
				pass
				
def search_checked():
	Dialog = xbmcgui.Dialog()
	if not os.path.exists(Addon_data):
		os.makedirs(Addon_data)
	if not os.path.exists(Stream_file):
		Dialog.ok('You need to run \'Check for response off streams\' first','Please run above and then come back')
	else:
		progress = []
		item = []
		result = []
		dp =  xbmcgui.DialogProgress()
		Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
		Search_name = Search_title.lower()
		HTML = open(Stream_file).read()
		match = re.compile('<NAME=>(.+?)</NAME><URL=>(.+?)</URL>').findall(HTML)
		for name, url in match:
			item.append(url[0])
			items = len(item)
		for name, url in match:
			progress.append(url[0])
			dp_add = len(progress) / float(items) * 100
			dp.create('Checking for stream')
			dp.update(int(dp_add),'Checking list '+str(len(progress))+'/'+str(len(match)),str(len(result))+' Results')
			if dp.iscanceled():
				return
			if (Search_name).replace(' ','') in (name).replace(' ','').lower():
				result.append(url[0])
				process.Play(name,url,906,'','','','')
