def scrape_episode(name,season,episode):
	import nanscrapers, process, xbmcgui
	progress = []
	item = []
	dp =  xbmcgui.DialogProgress()
	links_scraper = nanscrapers.scrape_episode(name, '', '', season.replace('Season',''), episode.replace('pisode',''), '', None)
	if links_scraper is False:
		pass
	else:
		scraped_links = []
		for scraper_links in links_scraper():
			item.append(scraper_links)
		items = len(item)
		for scraper_links in links_scraper():
			if scraper_links is not None:
				progress.append(scraper_links)
				dp_add = len(progress) / float(items) * 100
				dp.create('Checking for stream')
				dp.update(int(dp_add),'Checking sources',"Checking Nan Scrapers",'Please Wait')				
				scraped_links.extend(scraper_links)
		for link in scraped_links:
			process.Play('Direct Link - '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")",link["url"],'','','','','')

def scrape_movie(name,year):
	import nanscrapers, process, xbmcgui
	progress = []
	item = []
	dp =  xbmcgui.DialogProgress()
	links_scraper = nanscrapers.scrape_movie(name, year, '', timeout=60)
	if links_scraper is False:
		pass
	else:
		scraped_links = []
		for scraper_links in links_scraper():
			item.append(scraper_links)
		items = len(item)
		for scraper_links in links_scraper():
			if scraper_links is not None:
				progress.append(scraper_links)
				dp_add = len(progress) / float(items) * 100
				dp.create('Checking for stream')
				dp.update(int(dp_add),'Checking sources',"Checking Nan Scrapers",'Please Wait')				
				scraped_links.extend(scraper_links)
		for link in scraped_links:
			process.Play('Direct Link - '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")",link["url"],'','','','','')

