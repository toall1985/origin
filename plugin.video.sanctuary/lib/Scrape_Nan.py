def scrape_episode(name,season,episode):
	import process, xbmcgui
	from nanscrapers import scrape_episode
	progress = []
	item = []
	dp =  xbmcgui.DialogProgress()
	dp.create('Initiating Scrapers')
	links_scraper = scrape_episode(name, '', '', season.replace('Season',''), episode.replace('pisode',''), '', None)
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
				dp.update(int(dp_add),'Checking sources',"Checking Nan Scrapers",'Please Wait')				
				scraped_links.extend(scraper_links)
		for link in scraped_links:
			process.Play(link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")",link["url"],906,'','','','')

def scrape_movie(name,year):
	import process, xbmcgui,re
	from nanscrapers import scrape_movie
	if '(' in name:
		year_remover = re.compile('\((.+?)\)').findall(str(name))
		for item in year_remover:
			name = name.replace(item,'').replace('(','').replace(')','')
	year = year.replace('(','').replace(')','').replace(' ','')
	if name is not "" and year is not "":
		progress = []
		item = []
		dp =  xbmcgui.DialogProgress()
		dp.create('Initiating Scrapers')
		links_scraper = scrape_movie(name, year, '', timeout=600)
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
				process.Play(link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")",link["url"],906,'','','','')

