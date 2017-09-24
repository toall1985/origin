import sys

import nanscrapers
import originresolver
import xbmc
import xbmcgui
import xbmcaddon

addon_id = 'plugin.video.scrapertest'
ADDON = xbmcaddon.Addon(id=addon_id)

def scrape_movie(name,year,imdb):

    if name is not "" and year is not "":
        def sort_function(item):
            quality = item[1][0]["quality"]
            if quality == "1080": quality = "HDa"
            if quality == "720": quality = "HDb"
            if quality == "560": quality = "HDc"
            if quality == "HD": quality = "HDd"
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

    if name is not "" and year is not "" and season is not "" and episode is not "":
        link = nanscrapers.scrape_episode_with_dialog(name, show_year, year, season, episode, imdb, None)
        if link is False:
            xbmcgui.Dialog().ok("TV Show not found", "No Links Found for " + name + " (" + year + ")" + " - S" + season
                                + "E" + episode)
        else:
            if link:
                url = link['url']
                originresolver.originresolver(name,url)
