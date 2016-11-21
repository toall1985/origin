def scrape_episode(name,season,episode):
	import process, xbmcgui, sys, xbmcplugin
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
			if link["quality"]=='SD': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='CAM': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='360': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='480': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='560': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='720': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='1080': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='HD': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			process.Play(name,link["url"],906,'','','','')
			xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE);

def scrape_movie(name,year):
	import process, xbmcgui,re, xbmcplugin, sys
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
				if link["quality"]=='SD': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
				elif link["quality"]=='CAM': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
				elif link["quality"]=='360': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
				elif link["quality"]=='480': name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
				elif link["quality"]=='560': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
				elif link["quality"]=='720': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
				elif link["quality"]=='1080': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
				elif link["quality"]=='HD': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
				process.Play(name,link["url"],906,'','','','')
				xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE);

