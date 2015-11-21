import urllib, urllib2, re, xbmc, xbmcgui, xbmcplugin, xbmcaddon, os, sys
from bs4 import BeautifulSoup


BaseUrl = 'http://entertainmentlists.x10host.com/Lists/?'

AddonID = 'plugin.video.DKTV'
ADDON = xbmcaddon.Addon(id=AddonID)
localizedString = ADDON.getLocalizedString
ART = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID + '/resources/images/'))
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
		addDir(category,BaseUrl+'mode=LiveTV&list='+category,46,ART+icon,ART+'fanart.jpg','')
	
	setView('livetv', 'TV-Guide')

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
		addDir(category,BaseUrl+'mode=Live Sports&list='+category,46,ART+icon,ART+'fanart.jpg','')
	
	setView('livetv', 'TV-Guide')

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
		addDir(category,BaseUrl+'mode=Movies&list='+category,46,ART+icon,ART+'fanart.jpg','')
	
	setView('livetv', 'TV-Guide')

def Category(name, url):
	ChannelURL = url
	OpenURL = urllib2.urlopen(url)
	soup = BeautifulSoup(OpenURL)
	OpenURL.close()
	GetCategory = soup.find_all('div', {'class': name})
	
	for item in GetCategory:
		GetItem = item.find_all('div', {'class': 'Online'})
		for item in GetItem:
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
			if len(DataList)>=5:
					info = DataList[4]
			else:
				info = 'Sorry this description is currently unavailable'
		          
			
			if len(UrlList) == 1:
				urllink = UrlList[0]
				AddTestDir(title,urllink,3,icon,description=info,isFolder=False, background=fanart)

			elif len(UrlList) > 1:
				AddTestDir(title,ChannelURL,45,icon,description=info,isFolder=True, background=fanart)
			
			
			
	
		setView('livetv', 'TV-Guide')


		
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
                AddTestDir('Link 1: '+title,urllink1,3,icon,description=info,isFolder=False, background=fanart)
                AddTestDir('Link 2: '+title,urllink2,3,icon,description=info,isFolder=False, background=fanart)
                

            elif len(UrlList) == 3:
                urllink1 = UrlList[0]
                urllink2 = UrlList[1]
                urllink3 = UrlList[2]
                AddTestDir('Link 1: '+title,urllink1,3,icon,description=info,isFolder=False, background=fanart)
                AddTestDir('Link 2: '+title,urllink2,3,icon,description=info,isFolder=False, background=fanart)
                AddTestDir('Link 3: '+title,urllink3,3,icon,description=info,isFolder=False, background=fanart)
                
            
        
        
        
        else:
            pass

	
	
	setView('livetv', 'TV-Guide')
	
def addDir(name,url,mode,iconimage,fanart,description):
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

def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)		
	
def AddTestDir(name, url, mode, iconimage, description="", isFolder=True, background=None):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)

	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
	if background:
		liz.setProperty('fanart_image', background)
	if mode == 1 or mode == 2:
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10008).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=22)'.format(sys.argv[0], urllib.quote_plus(url)))])
	elif mode == 3:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
	elif mode == 32:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10010).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
		
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)
	