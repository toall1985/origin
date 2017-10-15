import xbmc,xbmcgui,xbmcplugin,sys,xbmcaddon
import process
import re
import os
import datetime
import time
import originresolver

dp =  xbmcgui.DialogProgress()
ADDON = xbmcaddon.Addon(id='plugin.video.iamgroot')
Hosts = []
hd_list = ['s']
mid_list = ['s']
sd_list = ['s']
fin_list = []
unsorted_list = []
scraper_list =[]
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


def sort_qual(link):
	qual_return = str(link["quality"]).lower().replace('0p','0').replace(' ','')
	if qual_return=='sd': qual_check = '240';qual_letter='i';name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
	elif qual_return=='240': qual_check = '240';qual_letter='i'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
	elif qual_return=='cam': qual_check = '120';qual_letter='j'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
	elif qual_return=='360': qual_check = '360';qual_letter='h'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
	elif qual_return=='480': qual_check = '480';qual_letter='g'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
	elif qual_return=='560': qual_check = '560';qual_letter='f'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
	elif qual_return=='720': qual_check = '720';qual_letter='e'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
	elif qual_return=='hd': qual_check = '1080';qual_letter='d'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
	elif qual_return=='dvd': qual_check = '1080';qual_letter='c'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
	elif qual_return=='bluray': qual_check = '1080';qual_letter='b'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
	elif qual_return=='1080': qual_check = '1080';qual_letter='a'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
	else: qual_check='240';qual_letter='i';name = str(link["source"]) + " - " + str(link["scraper"]) + " (" + str(link["quality"]) + ")";sd_list.append('1')
	unsorted_list.append({'name':name,'quality':qual_check,'letter':qual_letter,'link':link})
	
def return_links(populator):
	nanscraper_no = []
	nanscraper_folder = xbmc.translatePath('special://home/addons/script.module.nanscrapers/lib/nanscrapers/scraperplugins/')
	for Root,Dir,Files in os.walk(nanscraper_folder):
		for File in Files:
			if File.endswith('.py'):
				if not '__' in File:
					nanscraper_no.append('1')
	result = 0
	for scraper_links in populator():
		scraper_list.append('a')
		if scraper_links != None:
			for link in scraper_links:
				if dp.iscanceled():
					return
				fin_list.extend('a')
				dp.update(100/int(len(nanscraper_no))*int(len(scraper_list)),'Cancelling will display results so far but cache incomplete list',"Results : ("+str(int(len(hd_list)-1))+ "/"+str(int(len(mid_list)-1))+ "/"+str(int(len(sd_list)-1))+')','Scrapers left to run: '+str(int(len(nanscraper_no))-int(len(scraper_list)))+' of '+str(len(nanscraper_no)))
				if dp.iscanceled():
					return
				sort_qual(link)
	if len(unsorted_list)>=2:
		sorted_list = sorted(unsorted_list, key = lambda unsorted_link: unsorted_link['letter'])
	else:
		sorted_list = unsorted_list
	if ADDON.getSetting('autoplay')=='true':
		if xbmc.Player().isPlaying()==True:
			xbmc.Player().stop()
			time.sleep(3)
		dp.close()
		count = 0
		if len(sorted_list)==1:
			try:
				for item in sorted_list:
					qual_check = item['quality']
					name = item['name']
					if int(high_qual)>=int(qual_check)>=int(low_qual):
						playlink = item['link']
						playlink = playlink['url']
						xbmc.Player().play(playlink, xbmcgui.ListItem(item['name']))
						time.sleep(3)
			except:
				time.sleep(3)
				pass
		else:
			while count<len(sorted_list) and xbmc.Player().isPlaying()!=True:
				count+=1
				try:
					item = sorted_list[int(count)]
					playlink = item['link']
					playlink = playlink['url']
					qual_check = item['quality']
					name = item['name']
					if int(high_qual)>=int(qual_check)>=int(low_qual):
						if '.mp4' in playlink or '.mkv' in playlink or 'm3u8' in playlink or '=m22' in playlink or '=m18' in playlink or '=m37' in playlink:
							if not 'openload' in playlink:
								if not 'embed' in playlink:
									if not '.html' in playlink:
										try:
											xbmc.Player().play(playlink, xbmcgui.ListItem(item['name']))
											time.sleep(3)
										except:
											time.sleep(3)
											pass
						else:
							if not 'openload' in playlink:
								try:
									resolved_link = originresolver(name,url,return_link=True)
								except:
									resolved_link = 'None'
								if resolved_link != 'None':
									try:
										xbmc.Player().play(playlink, xbmcgui.ListItem(item['name']))
										time.sleep(3)
									except:
										time.sleep(3)
										pass
				except:
					pass
	else:
		for item in sorted_list:
			qual_check = item['quality']
			name = item['name']
			link = item['link']
			if int(high_qual)>=int(qual_check)>=int(low_qual):
				process.PLAY(' '+name,str(link['url']),20,'','','','')
			else:
				for host in Hosts:
					if int(qual_check)<=int(high_qual):
						if str(host) in str(link["source"].lower().replace(' ','')):
							process.PLAY(name,str(link['url']),20,'','','','')
					else:
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
