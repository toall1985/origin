import xbmc,xbmcgui,xbmcplugin,sys,xbmcaddon
import process
import re
dp =  xbmcgui.DialogProgress()
ADDON = xbmcaddon.Addon(id='plugin.video.iamgroot')
Hosts = []
if ADDON.getSetting('vidzi')=='true':Hosts.append('vidzi')
if ADDON.getSetting('thevideo')=='true':Hosts.append('thevideo')
if ADDON.getSetting('gvid')=='true':Hosts.append('gvideo')
if ADDON.getSetting('direct')=='true':Hosts.append('direct')
if ADDON.getSetting('low_return')=='None':
	low_qual = '0'
else:
	low_qual = int(ADDON.getSetting('low_return'))
if ADDON.getSetting('high_return')=='None':
	high_qual = '1080'
else:
	high_qual = int(ADDON.getSetting('high_return'))



def return_links(populator):
    result = 0
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
				qual_return = str(link["quality"]).lower().replace('0p','0')
				if qual_return=='sd': qual_check = '240';name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
				elif qual_return=='cam': qual_check = '120'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
				elif qual_return=='360': qual_check = '360'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
				elif qual_return=='480': qual_check = '480'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
				elif qual_return=='560': qual_check = '560'; name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
				elif qual_return=='720': qual_check = '720'; name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
				elif qual_return=='1080': qual_check = '1080'; name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
				elif qual_return=='hd': qual_check = '1080'; name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
				elif qual_return=='dvd': qual_check = '1080'; name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
				elif qual_return=='blueray': qual_check = '1080'; name = ' '+link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
				else: qual_check='240';name = str(link["source"]) + " - " + str(link["scraper"]) + " (" + str(link["quality"]) + ")";sd_list.append('1')
				if dp.iscanceled():
					return
				if int(high_qual)>=int(qual_check)>=int(low_qual):
					process.PLAY(' '+name,str(link['url']),20,'','','','')
					result+=1
				else:
					for host in Hosts:
						if str(host) in str(link["source"].lower().replace(' ','')):
							process.PLAY(name,str(link['url']),20,'','','','')
							result+=1
						else:
							pass
				if result == 0:
					process.PLAY('No streams found for required resolution','',100,'','','','')
					process.PLAY('Try lowering in settings','',100,'','','','')
					process.PLAY('#####################','',100,'','','','')
					process.PLAY('Open Settings Menu','',100,'','','','')
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE);

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
        populator = scrape_episode(title, show_year, year, season, episode,imdb,'', timeout=60000)
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
        populator = scrape_movie(name, year, imdb, timeout=60000)
    except:
        return
    return_links(populator)


'''import sys

import nanscrapers
import originresolver
import xbmc
import xbmcgui
import xbmcaddon
import process

debug = False

def scrape_movie(name,year,imdb):

    year = year.replace('(','').replace(')','')
    if debug == True:
        xbmc.log('groot scrape_movie | Name = '+name+' ; Year = '+year,xbmc.LOGNOTICE)
    if name is not "" and year is not "":
        def sort_function(item):
            quality = item[1][0]["quality"]
            if quality.lower() == "bluray": quality = "HDa"
            if quality.lower() == "dvd": quality = "HDb"
            if quality == "1080": quality = "HDc"
            if quality.lower() == "hd": quality = "HDd"
            if quality == "720": quality = "HDe"
            if quality == "560": quality = "HDf"
            if quality == "480": quality = "SDa"
            if quality == "360": quality = "SDb"
            if quality == "SD": quality = "SDc"

            return quality


        link = nanscrapers.scrape_movie_with_dialog(name, year, imdb, timeout=600, sort_function=sort_function)
        if link is False:
            xbmcgui.Dialog().ok("Movie not found", "No Links Found for " + name + " (" + year + ")")
        else:
            if link:
                url = link['url']
                originresolver.originresolver(name,url)

def scrape_episode(name,show_year,year,season,episode,imdb):

    process.watched_shows(name,show_year,year,season,episode,imdb)

    if name is not "" and season is not "" and episode is not "":
        def sort_function(item):
            quality = item[1][0]["quality"]
            if quality.lower() == "bluray": quality = "HDa"
            if quality.lower() == "dvd": quality = "HDb"
            if quality == "1080": quality = "HDc"
            if quality.lower() == "hd": quality = "HDd"
            if quality == "720": quality = "HDe"
            if quality == "560": quality = "HDf"
            if quality == "480": quality = "SDa"
            if quality == "360": quality = "SDb"
            if quality == "SD": quality = "SDc"

            return quality
        link = nanscrapers.scrape_episode_with_dialog(name, show_year, year, season, episode, imdb, None, timeout=600, sort_function=sort_function)
        if link is False:
            xbmcgui.Dialog().ok("TV Show not found", "No Links Found for " + name + " (" + year + ")" + " - S" + season
                                + "E" + episode)
        else:
            if link:
                url = link['url']
                originresolver.originresolver(name,url)'''
