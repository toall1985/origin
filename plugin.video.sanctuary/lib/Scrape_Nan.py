def scrape_episode(title,show_year,year,season,episode):
	import process, xbmcgui, sys, xbmcplugin, xbmc
	from nanscrapers import scrape_episode
	progress = []
	item = []
	dp =  xbmcgui.DialogProgress()
	dp.create('Initiating Scrapers')
	xbmc.log('Title:'+title)
	xbmc.log('Show Year:'+show_year)
	xbmc.log('Episode Year:'+year)
	xbmc.log('Season:'+season)
	xbmc.log('Episode:'+episode)
	links_scraper = scrape_episode(title, show_year, year, season, episode, '', None)
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
			elif link["quality"]=='360': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='480': name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='560': name = '  '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='720': name = '  '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='1080': name = '  '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			elif link["quality"]=='HD': name = '  '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			else: name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
			if 'vidzi' in name: name = ' ' +name
			elif 'vidbull' in name: name = ' ' +name
			elif 'vidto' in name: name = ' ' +name
			if 'openload.co' in name:
				pass
			elif 'thevideo.me' in name:
				pass
			else:
				process.PLAY(name,link["url"],906,'','','','')
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
				else: name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")"
				import urlresolver
				try:
					xbmc.log("resolving " + url)
					resolved_url = urlresolver.resolve(url)
					xbmc.log("resolved")
				except:
					url = link["url"]
					sys.exit()
				if resolved_url:
					url = resolved_url
				process.PLAY(name,url,906,'','','','')
				xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE);

