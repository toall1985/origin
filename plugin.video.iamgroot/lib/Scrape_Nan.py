import xbmc,xbmcgui,xbmcplugin,sys
import process
dp =  xbmcgui.DialogProgress()


def return_links(populator):
    fin_list = []
    hd_list = ['s']
    mid_list = ['s']
    sd_list = ['s']
    for scraper_links in populator():
        for link in scraper_links:
			if dp.iscanceled():
				return
			if scraper_links != None:
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
				else: name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
				try:
					process.PLAY(name,str(link['url']),20,'','','','')
					xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE);
				except:
					pass

def scrape_episode(title,show_year,year,season,episode,imdb):
    year = year.replace('(','').replace(')','').replace(' ','').replace('I','')
    show_year = show_year.replace('(','').replace(')','').replace(' ','')
    from nanscrapers import scrape_episode
    progress = []
    item = []
    dp.create('Initiating Scrapers')
    populator = scrape_episode(title, show_year, year, season, episode,imdb,'')
    return_links(populator)



def scrape_movie(name,year,imdb):
    dp.create('Initiating Scrapers')
    year = year.replace('(','').replace(')','').replace(' ','').replace('I','')
    from nanscrapers import scrape_movie
    populator = scrape_movie(name, year, imdb)
    return_links(populator)
