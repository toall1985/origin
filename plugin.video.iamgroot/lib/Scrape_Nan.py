import sys

import nanscrapers
import originresolver
import xbmc
import xbmcgui
import xbmcaddon
import process

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

    process.watched_shows(name,show_year,year,season,episode,imdb)

    if name is not "" and season is not "" and episode is not "":
        def sort_function(item):
            quality = item[1][0]["quality"]
            if quality == "DVD": quality = "HDa"
            if quality == "1080": quality = "HDb"
            if quality == "720": quality = "HDc"
            if quality == "560": quality = "HDd"
            if quality == "HD": quality = "HDe"
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
                originresolver.originresolver(name,url)
