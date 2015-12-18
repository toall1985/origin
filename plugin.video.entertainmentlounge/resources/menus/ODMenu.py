import re, sys, os, xbmc, xbmcaddon, xbmcplugin, xbmcgui, urllib, urllib2
from resources.modules import modules, yt
from resources.modules.parsers import parser

ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))

#********** Test Text Files YouTube**********
TwentyFS = 'ONDeMaND/TWENTYFOURSEVEN.m3u'
NrlYTGames = 'ONDeMaND/NRLGAMESYT.m3u'
YTMatchOfTheDay = 'ONDeMaND/YTMatchOfTheDay.m3u'
WSimpsons = 'ONDeMaND/WSimpsons.m3u'

def TV_SHOWS():
	modules.addDir('Watch Simpsons','',32,ART+'Music.png',FANART,'')
	modules.AUTO_VIEW('518')

def watchSimp():
	url = BaseURL + WSimpsons
	modules.TestMenuDIR2(url)
	modules.AUTO_VIEW('518')

def TwentyFour_Seven():
	url = BaseURL + TwentyFS
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def NRL_YT_RP():
	url = BaseURL + NrlYTGames
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def YT_Match_Of_The_Day():
	url = BaseURL + YTMatchOfTheDay
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def ALLMOVIES_OD(url):
	parser.Category('Cinema', url)
	parser.Category('Kids', url)
	parser.Category('Christmas', url)

def KidsMOVIES_OD(url):
	parser.Category('Kids', url)
	

def MOVIES_OD():
	try:
		modules.addDir('All Movies','http://entertainmentlists.x10host.com/Lists/?mode=Movies&list=GetGenres',39,ART+'LiveTv.png',FANART,'')
	except:
		pass
	
	try:
		parser.MovieCategories('mode=Movies&list=GetGenres')
	except:
		pass
	modules.AUTO_VIEW('500')

def Adult_OD():
	modules.addDir('Adult OD Test','',2,ART+'MoviesOD.png',FANART,'')
	modules.AUTO_VIEW('500')