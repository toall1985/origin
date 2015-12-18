import urllib, urllib2
from bs4 import BeautifulStoneSoup, BeautifulSoup
from resources.modules import modules



def GetDIRS():
	BaseURL = urllib2.urlopen('http://watch-simpsons.com/downloads/', timeout=500)
	Soup = BeautifulSoup(BaseURL)
	
	GetUL = Soup.find_all('ul')

	for item in GetUL:
		GetLI = Soup.find_all('li')

		for item in GetLI:
			GetANCHOR = Soup.find_all('a')

		for link in GetANCHOR:
			URLStart = 'http://watch-simpsons.com/downloads/'
			DirURL = link.get("href")
			Title = link.text
			
			#BuildFinalURLVARS = {'base': URLStart, 'dir': DirURL}
			#BuildFinalURL = urllib.urlencode(BuildFinalURLVARS)
			#FURL =  print(BuildFinalURL)
			
			modules.addDir(Title,URLStart +str(DirURL),32,'','','')

def GetLINKS(url):
	GETurl = url
	DIRurl = urllib2.urlopen(GETurl)

	Soup2 = BeautifulSoup(DIRurl)

	GetUL = Soup2.find_all('ul')

	for item in GetUL:
		GetLI = Soup2.find_all('li')

		for item in GetLI:
			GetANCHOR = Soup2.find_all('a')

		for link in GetANCHOR:
			LINKurl = link.get("href")
			modules.AddTestDir(LINKurl,GETurl +str(LINKurl),28,'','',isFolder=False)

    
