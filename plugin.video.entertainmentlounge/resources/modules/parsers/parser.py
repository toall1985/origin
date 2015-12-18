import urllib2, re, base64, xbmc, xbmcgui, xbmcplugin, xbmcaddon

from resources.modules import modules
from bs4 import BeautifulSoup
from datetime import datetime


Decode = base64.decodestring
ART = Decode('aHR0cDovL2NoYW1lbGVvbi54MTBob3N0LmNvbS90ZXN0L0VMaWNvbnMv')
BaseUrl = Decode('aHR0cDovL2VudGVydGFpbm1lbnRsaXN0cy54MTBob3N0LmNvbS9MaXN0cy8/')


#-------------------------------------------------------------------------------------
def TVCategories(url):
	
    OpenURL = urllib2.urlopen(BaseUrl+url)
    soup = BeautifulSoup(OpenURL)
    OpenURL.close()

    GetCategories = soup.find_all('div', {'id': 'CategorySection'})    
    for category in GetCategories:

        CatData = []

        GetCategoryTitle = category.find_all('title', {'class': 'Category'})
        for title in GetCategoryTitle:
            title = re.findall(r'<title class="Category">(.*?)</title>',str(title))
            for Title in title:
                CatData.append(Title)


        Icon = category.find_all('a', {'class': 'CategoryIcon'})
        for icon in Icon:
            icon = re.findall(r'<a class="CategoryIcon">(.*?)</a>',str(icon))
            for Icon in icon:
                CatData.append(Icon)
				
		Fanart = category.find_all('a', {'class': 'CategoryFanart'})
		for fanart in Fanart:
			fanart = re.findall(r'<a class="CategoryFanart">(.*?)</a>',str(fanart))
			for Fanart in fanart:
				CatData.append(Fanart)
		
		category = CatData[0]
		icon = CatData[1]
		fanart = CatData[2]
		modules.addDir(category,BaseUrl+Decode('bW9kZT1MaXZlVFYmbGlzdD0=')+category,34,ART+icon,ART+fanart,'')
	
	modules.setView('livetv', 'TV-Guide')

def LiveSportCategories(url):
	
    OpenURL = urllib2.urlopen(BaseUrl+url)
    soup = BeautifulSoup(OpenURL)
    OpenURL.close()

    GetCategories = soup.find_all('div', {'id': 'CategorySection'})    
    for category in GetCategories:

        CatData = []

        GetCategoryTitle = category.find_all('title', {'class': 'Category'})
        for title in GetCategoryTitle:
            title = re.findall(r'<title class="Category">(.*?)</title>',str(title))
            for Title in title:
                CatData.append(Title)


        Icon = category.find_all('a', {'class': 'CategoryIcon'})
        for icon in Icon:
            icon = re.findall(r'<a class="CategoryIcon">(.*?)</a>',str(icon))
            for Icon in icon:
                CatData.append(Icon)
				
		Fanart = category.find_all('a', {'class': 'CategoryFanart'})
		for fanart in Fanart:
			fanart = re.findall(r'<a class="CategoryFanart">(.*?)</a>',str(fanart))
			for Fanart in fanart:
				CatData.append(Fanart)
		
		category = CatData[0]
		icon = CatData[1]
		fanart = CatData[2]
		modules.addDir(category,BaseUrl+'mode=Live Sports&list='+category,34,ART+icon,ART+fanart,'')
	
	modules.setView('livetv', 'TV-Guide')

def MovieCategories(url):
	
    OpenURL = urllib2.urlopen(BaseUrl+url)
    soup = BeautifulSoup(OpenURL)
    OpenURL.close()

    GetCategories = soup.find_all('div', {'id': 'CategorySection'})    
    for category in GetCategories:

        CatData = []

        GetCategoryTitle = category.find_all('title', {'class': 'Category'})
        for title in GetCategoryTitle:
            title = re.findall(r'<title class="Category">(.*?)</title>',str(title))
            for Title in title:
                CatData.append(Title)


        Icon = category.find_all('a', {'class': 'CategoryIcon'})
        for icon in Icon:
            icon = re.findall(r'<a class="CategoryIcon">(.*?)</a>',str(icon))
            for Icon in icon:
                CatData.append(Icon)
				
		Fanart = category.find_all('a', {'class': 'CategoryFanart'})
		for fanart in Fanart:
			fanart = re.findall(r'<a class="CategoryFanart">(.*?)</a>',str(fanart))
			for Fanart in fanart:
				CatData.append(Fanart)
		
		category = CatData[0]
		icon = CatData[1]
		fanart = CatData[2]
		modules.addDir(category,BaseUrl+'mode=Movies&list='+category,34,ART+icon,ART+fanart,'')
	
	modules.setView('livetv', 'TV-Guide')

def Date_Time(check_Route):
	
	now = datetime.now()
	
	if check_Route == 'Time':
		hour = str(now.hour)
		return hour
		#minute = now.minute
	
	elif check_Route == 'Date':
			Date = str(now.month) + '/' + str(now.day) + '/' + str(now.year)
			return Date
	else:
		pass
		
Guide_URL = 'http://www.tvguide.co.uk/?catcolor=&systemid=5&thistime=' + str(Date_Time('Time')) + '&thisday=' + str(Date_Time('Date')) + '&gridspan=03:00&view=0&gw=1877'
dp = xbmcgui.DialogProgress()

def Category(name, url):
	ChannelURL = url
	OpenURL = urllib2.urlopen(url)
	soup = BeautifulSoup(OpenURL)
	OpenURL.close()
	GetCategory = soup.find_all('div', {'class': name})
	
	loaded_Channels = 0
	progress_Marker = 0
	
	
	
	WBLN_Message = 'Wont Be Long Now'
	dp.create('Loading Channels','','',WBLN_Message)
	
	for item in GetCategory:
		GetItem = item.find_all('div', {'class': 'Online'})
		item_Count = len(GetItem)
		calc_Progress = 100 / item_Count
		
		for item in GetItem:
			Channels_Loaded = 'Loaded ' + str(loaded_Channels) + ' of ' + str(item_Count) + ' Channels'
			dp.update(int(progress_Marker),Channels_Loaded)
			
			print 'Progress Marker:  ' + str(progress_Marker)
			print 'Progress Marker INT:  ' + str(progress_Marker)
			print loaded_Channels

			DataList = []
			UrlList = []
			
			GetTitle = item.find_all('title', {'class': 'Name'})
			for title in GetTitle:
				title = re.findall(r'<title class="Name">(.*?)</title>',str(title))
				for Title in title:
					DataList.append(Title)
			
			
			GetUrl = item.find_all('a', {'class': 'Link1'})
			for link in GetUrl:
				link1 = re.findall(r'<a class="Link1">(.*?)</a>',str(link))
				for Link1 in link1:
					UrlList.append(Link1)
			
			
			try:
				GetUrl = item.find_all('a', {'class': 'Link2'})
				for link2 in GetUrl:
					url = re.findall(r'<a class="Link2">(.*?)</a>',str(link2))
					for Link2 in url:
						UrlList.append(Link2)
			except:
				pass
			
			
			try:
				GetUrl = item.find_all('a', {'class': 'Link3'})
				for link3 in GetUrl:
					url = re.findall(r'<a class="Link3">(.*?)</a>',str(link3))
					for Link3 in url:
						UrlList.append(Link3)
			except:
				pass

			GetMode = item.find_all('title', {'class': 'Mode'})
			for mode in GetMode:
				mode = re.findall(r'<title class="Mode">(.*?)</title>',str(mode))
				for Mode in mode:
					DataList.append(Mode)
					
			GetIcon = item.find_all('a', {'class': 'Icon'})
			for icon in GetIcon:
				icon = re.findall(r'<a class="Icon">(.*?)</a>',str(icon))
				for Icon in icon:
					DataList.append(Icon)
			
			GetFanart = item.find_all('a', {'class': 'Fanart'})
			for fanart in GetFanart:
				fanart = re.findall(r'<a class="Fanart">(.*?)</a>',str(fanart))
				for Fanart in fanart:
					DataList.append(Fanart)
			
			GetDesc = item.find_all('p', {'class': 'Description'})
			for Desc in GetDesc:
				Description = re.findall(r'<p class="Description">(.*?)</p>',str(Desc))
				for description in Description:
					DataList.append(description)
			
			title = DataList[0]
			#url = DataList[1]
			mode = int(DataList[1])
			icon = DataList[2]
			fanart = DataList[3]
			
			html=OPEN_URL(Guide_URL)
			match = re.compile('<div class="div-epg-channel-name">(.+?)</div>.+?<a qt-title="(.+?)"',re.DOTALL).findall(html)
			info = 'No Data Currently Available'
			for name, whatson in match:
				if 'HD' in name:
					name = name.replace ('HD', '')
				if 'hd' in name:
					name = name.replace ('hd', '')
				if '//' in name:
					name = name.replace ('//', ' ')
				
				channel = str(title)
				
				if channel in name:
					info = whatson
				else:
					pass

			if len(UrlList) == 1:
				urllink = UrlList[0]
				modules.AddTestDir(title,urllink,mode,icon,description=info,isFolder=False, background=fanart)				

			elif len(UrlList) > 1:
				modules.AddTestDir(title,ChannelURL,36,icon,description=info,isFolder=True, background=fanart)
			
			progress_Marker = progress_Marker + calc_Progress
			loaded_Channels = loaded_Channels + 1
	
		#progress_Marker = 0
		dp.close()
		modules.setView('tvshows', 'Media info 3')
	


def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link


		
def ChannelLinks(name, url):
    
    OpenURL = urllib2.urlopen(url)
    soup = BeautifulSoup(OpenURL)
    OpenURL.close()

    GetChannel = soup.find_all('div', {'class': 'Online'})    
    for channel in GetChannel:
        
        DataList = []
        UrlList = []
        start = False
        GetTitle = channel.find_all('title', {'class': 'Name'})
        for title in GetTitle:
            CheckTitle = re.findall(r'<title class="Name">(.*?)</title>',str(title))
            for checktitle in CheckTitle:      
                if checktitle == name:
                    start = True
                else:
                    pass

        if start == True:
            for title in GetTitle:
                title = re.findall(r'<title class="Name">(.*?)</title>',str(title))
                for Title in title:
                    DataList.append(Title)
            
            
            GetUrl = channel.find_all('a', {'class': 'Link1'})
            for link in GetUrl:
                link1 = re.findall(r'<a class="Link1">(.*?)</a>',str(link))
                for Link1 in link1:
                    UrlList.append(Link1)
            
            
            try:
                GetUrl = channel.find_all('a', {'class': 'Link2'})
                for link2 in GetUrl:
                    url = re.findall(r'<a class="Link2">(.*?)</a>',str(link2))
                    for Link2 in url:
                        UrlList.append(Link2)
            except:
                pass
            
            
            try:
                GetUrl = channel.find_all('a', {'class': 'Link3'})
                for link3 in GetUrl:
                    url = re.findall(r'<a class="Link3">(.*?)</a>',str(link3))
                    for Link3 in url:
                        UrlList.append(Link3)
            except:
                pass

            GetMode = channel.find_all('title', {'class': 'Mode'})
            for mode in GetMode:
                mode = re.findall(r'<title class="Mode">(.*?)</title>',str(mode))
                for Mode in mode:
                    DataList.append(Mode)
                    
            GetIcon = channel.find_all('a', {'class': 'Icon'})
            for icon in GetIcon:
                icon = re.findall(r'<a class="Icon">(.*?)</a>',str(icon))
                for Icon in icon:
                    DataList.append(Icon)
            
            GetFanart = channel.find_all('a', {'class': 'Fanart'})
            for fanart in GetFanart:
                fanart = re.findall(r'<a class="Fanart">(.*?)</a>',str(fanart))
                for Fanart in fanart:
                    DataList.append(Fanart)
            
            GetDesc = channel.find_all('p', {'class': 'Description'})
            for Desc in GetDesc:
                Description = re.findall(r'<p class="Description">(.*?)</p>',str(Desc))
                for description in Description:
                    DataList.append(description)
        
            title = DataList[0]
            mode = int(DataList[1])
            icon = DataList[2]
            fanart = DataList[3]
            if len(DataList)>=5:
                    info = DataList[4]
            else:
                info = 'Sorry this description is currently unavailable'
        
        
            if len(UrlList) == 2:
                urllink1 = UrlList[0]
                urllink2 = UrlList[1]
                modules.AddTestDir('Link 1: '+title,urllink1,mode,icon,description=info,isFolder=False, background=fanart)
                modules.AddTestDir('Link 2: '+title,urllink2,mode,icon,description=info,isFolder=False, background=fanart)
                

            elif len(UrlList) == 3:
                urllink1 = UrlList[0]
                urllink2 = UrlList[1]
                urllink3 = UrlList[2]
                modules.AddTestDir('Link 1: '+title,urllink1,mode,icon,description=info,isFolder=False, background=fanart)
                modules.AddTestDir('Link 2: '+title,urllink2,mode,icon,description=info,isFolder=False, background=fanart)
                modules.AddTestDir('Link 3: '+title,urllink3,mode,icon,description=info,isFolder=False, background=fanart)

        
        else:
            pass

	
	
	modules.setView('livetv', 'TV-Guide')
	
	
	
	
	