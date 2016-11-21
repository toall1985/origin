# -*- coding: utf-8 -*-

import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, time, process, requests
from threading import Thread

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
addon_handle = int(sys.argv[1])
Main = 'http://www.watchseriesgo.to/'
List = []
IMDB = 'http://www.imdb.com'



def multiv_Main_Menu():
    process.Menu('TV Schedule','http://www.tvmaze.com/calendar',6,ICON,FANART,'','')
    process.Menu('IMDB Top 100 Programs','http://www.imdb.com/chart/tvmeter?ref_=m_nv_ch_tvm',301,ICON,FANART,'','')
    process.Menu('Popular Episodes','http://www.watchseriesgo.to/new',302,ICON,FANART,'','')
#    process.Menu('Genres','',303,ICON,FANART,'','')
    process.Menu('Search','',308,ICON,FANART,'','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	

def IMDB_TOP_100_EPS(url):	
	html = requests.get(url).text
	show = re.compile('<td class="posterColumn">.+?<a href="(.+?)".+?<img src="(.+?)".+?title=".+?" >(.+?)</a>.+?<span class="secondaryInfo">(.+?)</span>',re.DOTALL).findall(html)
	for url,img,title,year in show:
		try:
			url = 'http://www.imdb.com'+url
			img = img.replace('45,67','174,256').replace('UY67','UY256').replace('UX45','UX175')
			process.Menu(title+' '+year,url,305,img,'','',title)
		except:
			pass
		
def IMDB_Get_Season_info(url,image,title):
	html = requests.get(url).text
	match = re.compile('<a href="/title/(.+?)".+?>(.+?)</a>',re.DOTALL).findall(html)
	for rest,name in match:
		if 'season' in rest:
			url = 'http://www.imdb.com/title/'+str(rest).encode('utf-8')
			process.Menu('Season '+name,url,306,image,'','',title)
			xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE)

def IMDB_Get_Episode_info(url,title):
	html = requests.get(url).text
	block = re.compile('<div class="list_item(.+?)itemprop="description">(.+?)</div>',re.DOTALL).findall(html)
	for block_,desc in block:
		name = re.compile('title="(.+?)"').findall(str(block_))
		for item in name:
			name = item
		image = re.compile('src="(.+?)"').findall(str(block_))
		for item in image:
			image = item
		else:
			image = ''
		ep_no = re.compile('<div>S(.+?)</div>').findall(str(block_))
		for item in ep_no:
			ep_no = item
		ep_split = ep_no+'<'
		Split = re.compile('(.+?),(.+?)<').findall(str(ep_split))
		for one,two in Split:
			xbmc.log('split')
			season = one.replace('S','Season ')
			xbmc.log('season')
			episode = two.replace('Ep','Episode ')
		search_split = 'SPLITTER>'+title+'>'+season.replace('Season ','')+'>'+episode.replace(' Episode ','')+'>'
		xbmc.log('search split')
		final_name = episode+' - '+name
		xbmc.log('final name')
		process.Menu(final_name.encode('utf-8'),'',307,image,'',desc.encode('utf-8'),search_split)
		xbmc.log('displaying')
		process.setView('movies', 'I')
		xbmc.log('view set')
		
def SPLIT(extra):
	finish = re.compile('SPLITTER>(.+?)>(.+?)>(.+?)').findall(str(extra))
	for name,season,episode in finish:
		from Scrape_Nan import scrape_episode
		scrape_episode(name,season,episode)

def Search_TV():
	Search_title = xbmcgui.Dialog().input('Search', type=xbmcgui.INPUT_ALPHANUM)
	url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+Search_title.replace(' ','+')+'&s=all'
	html = requests.get(url).text
	match = re.compile('<tr class="findResult.+?"> <td class="primary_photo"> <a href="(.+?)" ><img src="(.+?)" /></a> </td> <td class="result_text"> <a href=".+?" >(.+?)</a>(.+?)</td>').findall(html)
	for url,image,title,year in match:
		if '<' in year:
			pass
		else:
			if '(TV Series)' in year:
				url = 'http://imdb.com'+url
				year = year.replace('(TV Series)','')
				image = image.replace('32,44','174,256').replace('UY67','UY256').replace('UX32','UX175').replace('UY44','UY256')
				process.Menu(title+' '+year,url,305,image,'','',title)
					
def Genres():
	html = requests.get('http://www.imdb.com/genre/').text
	match = re.compile('<h3><a href="(.+?)">(.+?)<span class="normal">').findall(html)
	for url, name in match:
		process.Menu(name,url,304,'','','','')

def Genres_Page(url):
	pass

		
def Popular(url):
    OPEN = process.OPEN_URL(url)
    match = re.compile('<div class="block-left-home-inside-image">.+?<img src="(.+?)".+?<a href="(.+?)".+?<b>(.+?)</b>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>',re.DOTALL).findall(OPEN)
    for img,url,title,Season,desc in match:
        url = Main + url
        title = (title).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        split = re.compile('Season (.+?), Episode (.+?) -').findall(str(Season))
        for season, episode in split:
            search_split = 'SPLITTER>'+title+'>'+season+'>'+episode+'>'
            process.Menu(title+' - '+Season,url,307,img,FANART,desc,search_split)		
    xbmcplugin.endOfDirectory(int(sys.argv[1]))	


