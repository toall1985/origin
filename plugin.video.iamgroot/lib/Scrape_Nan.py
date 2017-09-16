import xbmc,xbmcgui,xbmcplugin,sys
import process
import re
dp =  xbmcgui.DialogProgress()


def return_links(populator):
    fin_list = []
    hd_list = ['s']
    mid_list = ['s']
    sd_list = ['s']
    for scraper_links in populator():
		if scraper_links != None:
			for link in scraper_links:
				if dp.iscanceled():
					return
				fin_list.extend(scraper_links)
				dp.update(int(2*len(fin_list)),'Cancelling will display results so far but cache incomplete list',"Results : ("+str(int(len(hd_list)-1))+ "/"+str(int(len(mid_list)-1))+ "/"+str(int(len(sd_list)-1))+')')	
				if link["quality"]=='SD': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
				elif link["quality"]=='CAM': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
				elif link["quality"]=='360': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
				elif link["quality"]=='480': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
				elif link["quality"]=='560': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
				elif link["quality"]=='720': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
				elif link["quality"]=='1080': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
				elif link["quality"]=='HD': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
				elif link["quality"]=='DVD': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
				else: name = str(link["source"]) + " - " + str(link["scraper"]) + " (" + str(link["quality"]) + ")";sd_list.append('1')
				if dp.iscanceled():
					return

				try:
					process.PLAY(name,str(link['url']),20,'','','','')
					xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE);
				except:
					pass

def scrape_episode(title,show_year,year,season,episode,imdb):
    year = year.replace('(','').replace(')','').replace(' ','').replace('I','')
    show_year = show_year.replace('(','').replace(')','').replace(' ','')
    year = re.sub("[^0123456789\.]","",year)
    show_year = re.sub("[^0123456789\.]","",show_year)
    from nanscrapers import scrape_episode
    progress = []
    item = []
    dp.create('Initiating Scrapers')
    try:
        populator = scrape_episode(title, show_year, year, season, episode,imdb,'')
    except:
        return
    return_links(populator)



def scrape_movie(name,year,imdb):
    dp.create('Initiating Scrapers')
    year = year.replace('(','').replace(')','').replace(' ','').replace('I','')
    year = re.sub("[^0123456789\.]","",year)
    xbmc.log('clean_year:'+year,xbmc.LOGNOTICE)
    xbmc.log('IMDB:'+imdb,xbmc.LOGNOTICE)
    from nanscrapers import scrape_movie
    try:
        populator = scrape_movie(name, year, imdb)
    except:
        return
    return_links(populator)
