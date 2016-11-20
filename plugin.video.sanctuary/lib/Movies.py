# -*- coding: utf-8 -*-
import urllib,re,xbmcgui,xbmcplugin,xbmc,sys,process,requests


def Movie_Main():
    process.Menu('Genre','',202,'','','','')
    process.Menu('IMDB top 250 Films','http://www.imdb.com/chart/top',206,'','','','')
    process.Menu('Search','',207,'','','','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def search_movies():
	Search_title = xbmcgui.Dialog().input('Search', type=xbmcgui.INPUT_ALPHANUM)
	url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+Search_title.replace(' ','+')+'&s=all'
	html = requests.get(url).text
	match = re.compile('<tr class="findResult.+?"> <td class="primary_photo"> <a href=".+?" ><img src="(.+?)" /></a> </td> <td class="result_text"> <a href=".+?" >(.+?)</a>(.+?)</td>').findall(html)
	for image,title,year in match:
		if '<' in year:
			pass
		else:
			if '(TV Series)' in year:
				pass
			else:
				image = image.replace('32,44','174,256').replace('UY67','UY256').replace('UX32','UX175').replace('UY44','UY256')
				process.Menu(title+' '+year,'',9,image,'','',year)
	
def Movie_Genre(url):
	html = requests.get('http://www.imdb.com/genre/').text
	match = re.compile('<h3><a href="(.+?)">(.+?)<span class="normal">').findall(html)
	for url, name in match:
		url = 'http://www.imdb.com/search/title?genres='+name.replace(' ','').lower()+'&title_type=feature&sort=moviemeter,asc'
		process.Menu(name,url,203,'','','','')

def IMDB_Top250(url):
	html = requests.get(url).text
	film = re.compile('<td class="posterColumn">.+?<img src="(.+?)".+?<td class="titleColumn">(.+?)<a.+?title=".+?" >(.+?)</a>.+?<span class="secondaryInfo">(.+?)</span>',re.DOTALL).findall(html)
	for img,no,title,year in film:
		no = no.replace('\n','').replace('	','').replace('  ','')
		try:
			img = img.replace('45,67','174,256').replace('UY67','UY256').replace('UX45','UX175')
			process.Menu(title+' '+year,'',9,img,'','',year)
		except:
			pass
		
def IMDB_Grab(url):
	List = []
	html = requests.get(url).text
	match = re.compile('<div class="lister-item-image float-left">.+?<a href="(.+?)".+?<img alt="(.+?)".+?loadlate="(.+?)".+?<span class="lister-item-year text-muted unbold">(.+?)</span>',re.DOTALL).findall(html)
	for url,name,image,year in match:
		image = image.replace('45,67','174,256').replace('UY67','UY256')
		try:
			if '(2017)' in year:
				pass
			else:
				year = year.replace('(I) ','')
				process.Menu(name+' '+year,url,9,image,'','',year)
		except:
			pass
	next_page = re.compile('<a href="(.+?)"\nclass="lister-page-next next-page" ref-marker=adv_nxt>Next &#187;</a>').findall(html)
	for item in next_page:
		if item not in List:
			process.Menu('Next Page','http://imdb.com/search/title'+item,203,'','','','')
			List.append(item)
			
def Check_Link(name,url,image):
    HTML = process.OPEN_URL(url)
    match = re.compile('<iframe width="660" height="400" scrolling="no" frameborder="0" src="http://mystream.la/external/(.+?)" allowFullScreen></iframe>').findall(HTML)
    for end in match:
        url = 'http://mystream.la/external/'+end
        process.Play(name,url,205,image,FANART,'','')        

def Get_playlink(url):
    HTML = process.OPEN_URL(url)
    match = re.compile('file:"(.+?)",label:"(.+?)"}').findall(HTML)
    for playlink,quality in match:
        process.Resolve(playlink)
		