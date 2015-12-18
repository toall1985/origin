import re, sys, os, xbmc, xbmcaddon, xbmcplugin, xbmcgui, urllib, urllib2
from resources.modules import modules, yt
from resources.modules.parsers import parser

ADDON_ID = 'plugin.video.entertainmentlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))

#********** Test Text Files YouTube**********
LEntertainment = 'LiVE/LIVETV.m3u'
LMovies = 'LiVE/LIVEMOVIES.m3u'
LKids = 'LiVE/LIVEKIDS.m3u'
LSports = 'LiVE/LIVESPORTS.m3u'

def AllLiveTV(url):
	parser.Category('Entertainment', url)
	parser.Category('Kids', url)
	parser.Category('Music', url)
	parser.Category('Movies', url)
	parser.Category('Sports', url)
	parser.Category('News', url)
	parser.Category('Radio', url)
	parser.Category('Other', url)
	
	modules.setView('livetv', 'TV-Guide')

def KidsLiveTV(url):
	parser.Category('Kids', url)
	modules.AUTO_VIEW('504')

def LiveEntertainment():
	url = BaseURL + LEntertainment
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def LiveMovies():
	url = BaseURL + LMovies
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def LiveKids():
	url = BaseURL + LKids
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def LiveSport():
	url = BaseURL + LSports
	modules.TestMenuDIR(url)
	modules.AUTO_VIEW('518')

def Music():
	url = 'http://community-links.googlecode.com/svn/trunk/MrCuddlesTVLinks.xml'
	modules.TestMenuDIR(url)
	modules.addDir('MTV TEST','',2,ART+'UKTop100.png',FANART,'')
	modules.AUTO_VIEW('500')

def Adult_Live():
	modules.addDir('Adult Live TEST','',2,ART+'UKTop100.png',FANART,'')
	modules.AUTO_VIEW('500')
	
	
	