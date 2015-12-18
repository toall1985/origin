import requests, urllib, urllib2
from bs4 import BeautifulSoup
from resources.modules import modules

#opener = urllib2.build_opener()
#opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = "http://genvideos.org/most_viewed"
ourUrl = requests.get(url)
GenVidBaseUrl = "http://genvideos.org"

global soup
soup = BeautifulSoup(ourUrl.content)
def ScrapData():
	GetBody = soup.find_all('div', {'class': 'video_container b_10 box'})

	for item in GetBody:
		VidCells = soup.find_all('div', {'class': 'cell'})

		for item in VidCells:
			Get_Video_Content = soup.find_all('div', {'class': 'thumb'})

		for item in Get_Video_Content:
			Get_Raw_Data = soup.find_all('a')

		for link in Get_Raw_Data:
			Title = link.get("title")
			Video_Url = link.get('href')
			if Title != None:

				modules.AddTestDir(Title,GenVidBaseUrl + Video_Url,28,'','',isFolder=False)
			
	modules.AUTO_VIEW('518')