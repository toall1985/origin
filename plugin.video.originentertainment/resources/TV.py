import sys
import urlparse
import yt
import time
import urllib,urllib2,re,base64,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import base64
import urlresolver
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
from resources import streams
from resources import lists
from resources import utube

Decode = base64.decodestring
BASE2= lists.BASE2
BASE3= lists.BASE3
BASE4= lists.BASE4
BASE5= lists.BASE5
BASE6= lists.BASE6
BASE7= lists.BASE7
CAT=lists.CAT
BASE = lists.BASE
addon_id='plugin.video.originentertainment'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Origin Entertainment"
VERSION = "1.0.1"
ADDON = xbmcaddon.Addon(id=addon_id)
GetTVPassword = ADDON.getSetting('Password')
TVURL = Decode('http://seedurgreed.x10host.com/origin/TV/index.php?mode=TV&password=')
TVFinalURL = TVURL + GetTVPassword
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART 		=  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
net = Net()


def TV_Shows():
	
	addList('Recent Episodes',BASE+'recentepisodes'+CAT,400,ART + 'icon.png')
	addDir('Animated','',14,ART + 'icon.png',ART + 'background.jpg','')
	addDir('Action','',15,ART + 'icon.png',ART + 'background.jpg','')
	addDir('Childrens','',16,ART + 'icon.png',ART + 'background.jpg','')
	addDir('Comedy','',17,ART + 'icon.png',ART + 'background.jpg','')
	addDir('Drama','',18,ART + 'icon.png',ART + 'background.jpg','')
#	addDir('Entertainment','',19,ART + 'icon.png',ART + 'background.jpg','')
	addDir('Fantasy','',20,ART + 'icon.png',ART + 'background.jpg','')
#	addDir('Music','',21,ART + 'icon.png',ART + 'background.jpg','')
	addDir('Scifi','',22,ART + 'icon.png',ART + 'background.jpg','')
#	addDir('Soaps','',23,ART + 'icon.png',ART + 'background.jpg','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	

def Childrens_TV():
	addList('Bing',BASE+'bing'+CAT,400,'http://goo.gl/IHk8Ya')
	addList('Peppa Pig',BASE4,402,'http://ia.media-imdb.com/images/M/MV5BMTgzMTAwNDczMF5BMl5BanBnXkFtZTgwNzUzMzU0MTE@._V1_UY1200_CR135,0,630,1200_AL_.jpg')
	addList('Tazmania',BASE6,402,'http://ia.media-imdb.com/images/M/MV5BMTUyMTY5MDE0N15BMl5BanBnXkFtZTcwMDEwMDEzMQ@@._V1_UY1200_CR8,0,630,1200_AL_.jpg')
	addVID('','Minnie Mouse Bowtique','xNbjhNmNUGA',9,'Icon.jpg',ART + 'background.jpg','','')
	addVID('','Mickey Mouse Clubhouse','vn6xsuAokPg',9,'Icon.jpg',ART + 'background.jpg','','')
	addVID('','Mickey Mouse goofy and donald duck cartoons','blIHV79HplU',9,'Icon.jpg',ART + 'background.jpg','','')
	addVID('','Mickeys Once Upon A Christmas','X_ULfylsMzY',9,'Icon.jpg',ART + 'background.jpg','','')
	addVID('','Pluto Meets Cute Little Critters','3BkNDE5GI0g',9,'Icon.jpg',ART + 'background.jpg','','')
	addVID('','Walt Disney Classic Cartoons','s0IGJUTQQus',9,'Icon.jpg',ART + 'background.jpg','','')
	addVID('','Winter Cartoon Classics','vJw5IPX-mLI',9,'Icon.jpg',ART + 'background.jpg','','')
	

	xbmcplugin.endOfDirectory(addon_handle)
	
def Comedy_TV(): 
	
	addDir('How I Met Your Mother','',51,'http://ia.media-imdb.com/images/M/MV5BMTA5MzAzNTcyNjZeQTJeQWpwZ15BbWU3MDUyMzE1MTk@._V1_UY1200_CR91,0,630,1200_AL_.jpg',ART + 'background.jpg','')
	addList('Modern Family',BASE+'modernfamilymulit'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTU5MjQ1MTE2Ml5BMl5BanBnXkFtZTgwMDgwMzg5NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addList('The Big Bang Theory',BASE+'bigbangmulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMjI1Mzc4MDUwNl5BMl5BanBnXkFtZTgwMDAzOTIxMjE@._V1_UY1200_CR165,0,630,1200_AL_.jpg')
	addList('Two and a Half Men',BASE+'twohalfmenmulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTcwMDU1MDExNl5BMl5BanBnXkFtZTcwOTAwMjYyOQ@@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addDir('Mock The Week','',28,ART + 'mock.png',ART + 'background.jpg','')
	addDir('New Girl','',39,'http://ia.media-imdb.com/images/M/MV5BMTkyMTcwNTM3OF5BMl5BanBnXkFtZTcwMDI2MjcxOA@@._V1_UY1200_CR107,0,630,1200_AL_.jpg',ART + 'background.jpg','')
	addDir('The Inbetweeners','',29,ART + 'inbetween.png',ART + 'background.jpg','')
	addDir('The Last Man On Earth','',32,'http://ia.media-imdb.com/images/M/MV5BMTQ3NTEzODcyNl5BMl5BanBnXkFtZTgwNjY1NzU2NDE@._V1_SY317_CR2,0,214,317_AL_.jpg',ART + 'background.jpg','')
	addDir('Would I Lie To You','',30,ART + 'wouldi.jpg',ART + 'background.jpg','')

	xbmcplugin.endOfDirectory(addon_handle)
	
def How_I_Met_Your_Mother():
	
	addList('Series 1/3/4/5/7/8',BASE+'Howimetyourmothermulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTA5MzAzNTcyNjZeQTJeQWpwZ15BbWU3MDUyMzE1MTk@._V1_UY1200_CR91,0,630,1200_AL_.jpg')
	addList('Series 2',BASE+'How-I-Met-Your-Mother-Season-2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTkyMTcwNTM3OF5BMl5BanBnXkFtZTcwMDI2MjcxOA@@._V1_UY1200_CR107,0,630,1200_AL_.jpg')
	addList('Series 6',BASE+'Howimetyourmotherseason6.php'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTkyMTcwNTM3OF5BMl5BanBnXkFtZTcwMDI2MjcxOA@@._V1_UY1200_CR107,0,630,1200_AL_.jpg')

	
def New_girl():

	addList('Season 1',BASE+'New-Girl-Season-1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTkyMTcwNTM3OF5BMl5BanBnXkFtZTcwMDI2MjcxOA@@._V1_UY1200_CR107,0,630,1200_AL_.jpg')
	addList('Season 2',BASE+'New-Girl-Season-2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTkyMTcwNTM3OF5BMl5BanBnXkFtZTcwMDI2MjcxOA@@._V1_UY1200_CR107,0,630,1200_AL_.jpg')
	addList('Season 3',BASE+'New-Girl-Season-3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTkyMTcwNTM3OF5BMl5BanBnXkFtZTcwMDI2MjcxOA@@._V1_UY1200_CR107,0,630,1200_AL_.jpg')
	addList('Season 4',BASE+'New-Girl-Season-4'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTkyMTcwNTM3OF5BMl5BanBnXkFtZTcwMDI2MjcxOA@@._V1_UY1200_CR107,0,630,1200_AL_.jpg')

	xbmcplugin.endOfDirectory(addon_handle)
	
def The_Last_Man_On_Earth():
	
	addList('Season 1',BASE+'lastmanonearthseries1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ3NTEzODcyNl5BMl5BanBnXkFtZTgwNjY1NzU2NDE@._V1_SY317_CR2,0,214,317_AL_.jpg')
	addList('Season 2',BASE+'lastmanonearthseries2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ3NTEzODcyNl5BMl5BanBnXkFtZTgwNjY1NzU2NDE@._V1_SY317_CR2,0,214,317_AL_.jpg')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
	
	
	
def Drama_TV():
	
	addList('Ash vs Evil Dead',BASE+'Ash-vs-Evil-Dead'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTQ5OTQ4ODY0NV5BMl5BanBnXkFtZTgwMzQ4MjA2NjE@._V1_SX214_AL_.jpg')
	addDir('Bates Motel','',46,'http://ia.media-imdb.com/images/M/MV5BOTA5MzU0NzQ0M15BMl5BanBnXkFtZTgwNTYxMjA5NDE@._V1_SX214_AL_.jpg',ART + 'background.jpg','')
	addDir('Black List','',47,'http://ia.media-imdb.com/images/M/MV5BMTY3NjQ1OTU3NF5BMl5BanBnXkFtZTgwODcwMDI2NjE@._V1_UY1200_CR91,0,630,1200_AL_.jpg',ART + 'background.jpg','')
	addList('Bones',BASE+'bonesmulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg')
	addDir('Breaking bad','',42,'http://ia.media-imdb.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SY317_CR0,0,214,317_AL_.jpg',ART + 'background.jpg','')
	addDir('Brooklyn Nine Nine','',44,'http://ia.media-imdb.com/images/M/MV5BMTU2NTExOTI0N15BMl5BanBnXkFtZTgwOTkyNTA3NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg',ART + 'background.jpg','')
	addList('Criminal Minds',BASE+'criminalmindsmulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTQyMzExMzAzMl5BMl5BanBnXkFtZTcwMDEzNzk1OQ@@._V1_UY1200_CR93,0,630,1200_AL_.jpg')
	addDir('Dexter','',40,'http://ia.media-imdb.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_SY317_CR9,0,214,317_AL_.jpg',ART + 'background.jpg','')
	addDir('Fargo','',33,'http://ia.media-imdb.com/images/M/MV5BNDEzOTYzMDkzN15BMl5BanBnXkFtZTgwODkzNTAyNjE@._V1_SY317_CR4,0,214,317_AL_.jpg',ART + 'background.jpg','')
	addDir('Homelands','',37,'http://ia.media-imdb.com/images/M/MV5BMTg2MDAzNDIzOV5BMl5BanBnXkFtZTgwNzY3NDM2NjE@._V1_SY317_CR104,0,214,317_AL_.jpg',ART + 'background.jpg','')
	addList('Quantico',BASE+'quantico'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTg2NjU1NTkyMl5BMl5BanBnXkFtZTgwMzk5Mjg5NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addDir('Suits','',49,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg',ART + 'background.jpg','')	
	addDir('The Knick','',34,'http://ia.media-imdb.com/images/M/MV5BMTQ5NzcyNDc5MV5BMl5BanBnXkFtZTgwMDMyOTY5NjE@._V1_SX214_AL_.jpg',ART + 'background.jpg','')
	addList('The Last Kingdom',BASE+'thelastkingdom'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjE1MzYzNjk3OF5BMl5BanBnXkFtZTgwMzk0MzYwNzE@._V1_SX214_AL_.jpg')
	addList('The Mentalist',BASE+'thementallistmulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTQ5OTgzOTczM15BMl5BanBnXkFtZTcwMDM2OTY4MQ@@._V1_UY1200_CR135,0,630,1200_AL_.jpg')
	xbmcplugin.endOfDirectory(addon_handle)
	
def Suits():

	addList('Season 1',BASE+'suitsseason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg')
	addList('Season 2',BASE+'suitsseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg')
	addList('Season 3',BASE+'suitsseason3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg')
	addList('Season 4',BASE+'suitsseason4'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg')
	addList('Season 5',BASE+'suitsseason5'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg')

	
	
def Bates_motel():

	addList('Season 1',BASE+'batesmotelseason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg')
	addList('Season 2',BASE+'batesmotelseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg')
	addList('Season 3',BASE+'batesmotelseason3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk1MjYzOTU2Nl5BMl5BanBnXkFtZTgwMzAxMTg5MTE@._V1_SX214_AL_.jpg')

	
def Black_list():

	addList('Season 1',BASE+'theblacklistseason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTY3NjQ1OTU3NF5BMl5BanBnXkFtZTgwODcwMDI2NjE@._V1_UY1200_CR91,0,630,1200_AL_.jpg')
	addList('Season 2',BASE+'theblacklistseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTY3NjQ1OTU3NF5BMl5BanBnXkFtZTgwODcwMDI2NjE@._V1_UY1200_CR91,0,630,1200_AL_.jpg')
	addList('Season 3',BASE+'theblacklistseason3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTY3NjQ1OTU3NF5BMl5BanBnXkFtZTgwODcwMDI2NjE@._V1_UY1200_CR91,0,630,1200_AL_.jpg')

	
def Brooklyn_Nine_Nine():

	addList('Season 1',BASE+'Brooklyn-Nine-Nine-Season-1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTU2NTExOTI0N15BMl5BanBnXkFtZTgwOTkyNTA3NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addList('Season 2',BASE+'Brooklyn-Nine-Nine-Season-2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTU2NTExOTI0N15BMl5BanBnXkFtZTgwOTkyNTA3NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addList('Season 3',BASE+'Brooklyn-Nine-Nine-Season-3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTU2NTExOTI0N15BMl5BanBnXkFtZTgwOTkyNTA3NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')

	
def Breaking_bad():

	addList('Season 1',BASE+'Breaking-badseason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addList('Season 2',BASE+'Breaking-badseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addList('Season 3',BASE+'Breaking-badseason3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addList('Season 4',BASE+'Breaking-badseason4'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addList('Season 5',BASE+'Breaking-badseason5'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SY317_CR0,0,214,317_AL_.jpg')


def Dexter():

	addList('Season 1',BASE+'dexterseason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_SY317_CR9,0,214,317_AL_.jpg')
	addList('Season 2',BASE+'dexterseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_SY317_CR9,0,214,317_AL_.jpg')
	addList('Season 3',BASE+'dexterseason3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_SY317_CR9,0,214,317_AL_.jpg')
	addList('Season 4',BASE+'dexterseason4'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_SY317_CR9,0,214,317_AL_.jpg')
	addList('Season 5',BASE+'dexterseason5'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_SY317_CR9,0,214,317_AL_.jpg')
	addList('Season 6',BASE+'dexterseason6'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_SY317_CR9,0,214,317_AL_.jpg')
	addList('Season 7',BASE+'dexterseason7'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_SY317_CR9,0,214,317_AL_.jpg')
	addList('Season 8',BASE+'dexterseason8'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTM5MjkwMTI0MV5BMl5BanBnXkFtZTcwODQwMTc0OQ@@._V1_SY317_CR9,0,214,317_AL_.jpg')

	xbmcplugin.endOfDirectory(addon_handle)
	
	
def Homelands():

	addList('Season 1',BASE+'homelandsseason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTg2MDAzNDIzOV5BMl5BanBnXkFtZTgwNzY3NDM2NjE@._V1_SY317_CR104,0,214,317_AL_.jpg')
	addList('Season 2',BASE+'homelandsseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTg2MDAzNDIzOV5BMl5BanBnXkFtZTgwNzY3NDM2NjE@._V1_SY317_CR104,0,214,317_AL_.jpg')
	addList('Season 3',BASE+'homelandsseason3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTg2MDAzNDIzOV5BMl5BanBnXkFtZTgwNzY3NDM2NjE@._V1_SY317_CR104,0,214,317_AL_.jpg')
	addList('Season 4',BASE+'homelandsseason4'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTg2MDAzNDIzOV5BMl5BanBnXkFtZTgwNzY3NDM2NjE@._V1_SY317_CR104,0,214,317_AL_.jpg')
	addList('Season 5',BASE+'homelandsseason5'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTg2MDAzNDIzOV5BMl5BanBnXkFtZTgwNzY3NDM2NjE@._V1_SY317_CR104,0,214,317_AL_.jpg')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
	
def The_Knick():

	addList('Season 1',BASE+'the-knick'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ5NzcyNDc5MV5BMl5BanBnXkFtZTgwMDMyOTY5NjE@._V1_SX214_AL_.jpg')
	addList('Season 2',BASE+'the-knickseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ5NzcyNDc5MV5BMl5BanBnXkFtZTgwMDMyOTY5NjE@._V1_SX214_AL_.jpg')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
	
def Fargo():

	addList('Season 1',BASE+'fargo'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BNDEzOTYzMDkzN15BMl5BanBnXkFtZTgwODkzNTAyNjE@._V1_SY317_CR4,0,214,317_AL_.jpg')
	addList('Season 2',BASE+'fargoseries2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BNDEzOTYzMDkzN15BMl5BanBnXkFtZTgwODkzNTAyNjE@._V1_SY317_CR4,0,214,317_AL_.jpg')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
	
def Entertainment_TV():

	xbmcplugin.endOfDirectory(addon_handle)
	
def Music_TV():

	xbmcplugin.endOfDirectory(addon_handle)
	
def Action_TV():

	addDir('Arrow','',26,'http://ia.media-imdb.com/images/M/MV5BMTg3OTc0NzkyOV5BMl5BanBnXkFtZTgwMDMwMTM3MjE@._V1_UY1200_CR80,0,630,1200_AL_.jpg',ART + 'background.jpg','')
	addList('Blindspot',BASE+'blindspot'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTczMTMyMzM2M15BMl5BanBnXkFtZTgwNzM1NDA2NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addDir('Daredevil','',38,'http://ia.media-imdb.com/images/M/MV5BMTgyMjU0Mzg5Nl5BMl5BanBnXkFtZTgwMTg3MDYyNTE@._V1_SX214_AL_.jpg',ART + 'background.jpg','')
	addDir('Flash','',27,'http://ia.media-imdb.com/images/M/MV5BNjAwNzkxNzAwNF5BMl5BanBnXkFtZTgwODg2NTc2NjE@._V1_SY317_CR19,0,214,317_AL_.jpg',ART + 'background.jpg','')
	addDir('Game of Thrones','',45,'http://ia.media-imdb.com/images/M/MV5BNTgxOTI4NzY2M15BMl5BanBnXkFtZTgwMjY3MTM2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg',ART + 'background.jpg','')
	addDir('Gotham','',35,'http://ia.media-imdb.com/images/M/MV5BMTQ1ODk3NDczNF5BMl5BanBnXkFtZTgwODE5MDQ4NjE@._V1_SY317_CR0,0,214,317_AL_.jpg',ART + 'background.jpg','')
	addDir('Grimm','',43,'http://ia.media-imdb.com/images/M/MV5BMTk2NDMxOTg3Ml5BMl5BanBnXkFtZTgwNTE5MzExNzE@._V1_UY1200_CR135,0,630,1200_AL_.jpg',ART + 'background.jpg','')
	addDir('Legends','',48,'http://ia.media-imdb.com/images/M/MV5BMTQ4Njg0MzYxMF5BMl5BanBnXkFtZTgwMjAzMjk4MTE@._V1_SY317_CR11,0,214,317_AL_.jpg',ART + 'background.jpg','')
	addDir('Sons Of Anarchy','',36,'http://ia.media-imdb.com/images/M/MV5BMTEyODg2NzkwMDBeQTJeQWpwZ15BbWU4MDQwODI3MzIx._V1_SX214_AL_.jpg',ART + 'background.jpg','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Legends():

	addList('Legends',BASE+'legends-season-1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ4Njg0MzYxMF5BMl5BanBnXkFtZTgwMjAzMjk4MTE@._V1_SY317_CR11,0,214,317_AL_.jpg')


def Game_of_thrones():
	
	addList('Season 1',BASE+'Game-of-Thrones-Season-1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BNTgxOTI4NzY2M15BMl5BanBnXkFtZTgwMjY3MTM2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addList('Season 2-3-4',BASE+'gotmulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BNTgxOTI4NzY2M15BMl5BanBnXkFtZTgwMjY3MTM2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addList('Season 5',BASE+'Game-of-Thrones-Season-5'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BNTgxOTI4NzY2M15BMl5BanBnXkFtZTgwMjY3MTM2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')

	
def Grimm():
	
	addList('Season 1',BASE+'Grimm-Season-1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk2NDMxOTg3Ml5BMl5BanBnXkFtZTgwNTE5MzExNzE@._V1_UY1200_CR135,0,630,1200_AL_.jpg')
	addList('Season 2+3',BASE+'grimmmulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTk2NDMxOTg3Ml5BMl5BanBnXkFtZTgwNTE5MzExNzE@._V1_UY1200_CR135,0,630,1200_AL_.jpg')
	addList('Season 4',BASE+'Grimm-Season-4'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk2NDMxOTg3Ml5BMl5BanBnXkFtZTgwNTE5MzExNzE@._V1_UY1200_CR135,0,630,1200_AL_.jpg')
	addList('Season 5',BASE+'Grimm-Season-5'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTk2NDMxOTg3Ml5BMl5BanBnXkFtZTgwNTE5MzExNzE@._V1_UY1200_CR135,0,630,1200_AL_.jpg')

	
def Daredevil():

	addList('Season 1',BASE+'Daredevilseason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTgyMjU0Mzg5Nl5BMl5BanBnXkFtZTgwMTg3MDYyNTE@._V1_SX214_AL_.jpg')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
	
def Gotham():
	
	addList('Season 1',BASE+'gotham'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ1ODk3NDczNF5BMl5BanBnXkFtZTgwODE5MDQ4NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addList('Season 2',BASE+'gothamseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ1ODk3NDczNF5BMl5BanBnXkFtZTgwODE5MDQ4NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
	
def Sons_Of_Anarchy():
	
	addList('Season 1',BASE+'SonsOfAnarchySeason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTEyODg2NzkwMDBeQTJeQWpwZ15BbWU4MDQwODI3MzIx._V1_SX214_AL_.jpg')
	addList('Season 2',BASE+'SonsOfAnarchySeason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTEyODg2NzkwMDBeQTJeQWpwZ15BbWU4MDQwODI3MzIx._V1_SX214_AL_.jpg')
	addList('Season 3',BASE+'SonsOfAnarchySeason3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTEyODg2NzkwMDBeQTJeQWpwZ15BbWU4MDQwODI3MzIx._V1_SX214_AL_.jpg')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
	
def Arrow():

	addList('Season 1-3',BASE+'arrow1-3'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTg3OTc0NzkyOV5BMl5BanBnXkFtZTgwMDMwMTM3MjE@._V1_UY1200_CR80,0,630,1200_AL_.jpg')
	addList('Season 4',BASE+'arrowseason4'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTg3OTc0NzkyOV5BMl5BanBnXkFtZTgwMDMwMTM3MjE@._V1_UY1200_CR80,0,630,1200_AL_.jpg')


def Flash():

	addList('Season 1',BASE+'theflashseries1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BNjAwNzkxNzAwNF5BMl5BanBnXkFtZTgwODg2NTc2NjE@._V1_SY317_CR19,0,214,317_AL_.jpg')
	addList('Season 2',BASE+'theflashseries2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BNjAwNzkxNzAwNF5BMl5BanBnXkFtZTgwODg2NTc2NjE@._V1_SY317_CR19,0,214,317_AL_.jpg')	
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Fantasy_TV():

	addList('Heroes Reborn',BASE+'heroesreborn'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjI0NTE5NDIxOV5BMl5BanBnXkFtZTgwMDQ3ODM2NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addList('Limitless',BASE+'limitless'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTA4ODE4NjA5ODleQTJeQWpwZ15BbWU4MDUxMTQ0NTYx._V1_SX214_AL_.jpg')
	addDir('Once Upon A Time','',50,'http://ia.media-imdb.com/images/M/MV5BMjE0NDgxNDY2NV5BMl5BanBnXkFtZTgwNjU5Mjg5NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg','background.jpg','')
	addList('Supergirl',BASE+'supergirl'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTg5MDI3OTI3M15BMl5BanBnXkFtZTgwNzk0MDI1NjE@._V1_UY1200_CR84,0,630,1200_AL_.jpg')
	addList('The Walking Dead',BASE+'thewalkingdead'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ3NzQ2Mzk1OF5BMl5BanBnXkFtZTgwNTAzNjI5NjE@._V1_SX214_AL_.jpg')

	xbmcplugin.endOfDirectory(addon_handle)
	
def Once_upon_a_time():

	addList('Season 1',BASE+'onceuponatimeseason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjE0NDgxNDY2NV5BMl5BanBnXkFtZTgwNjU5Mjg5NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addList('Season 2',BASE+'onceuponatimeseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjE0NDgxNDY2NV5BMl5BanBnXkFtZTgwNjU5Mjg5NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addList('Season 3',BASE+'onceuponatimeseason3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjE0NDgxNDY2NV5BMl5BanBnXkFtZTgwNjU5Mjg5NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addList('Season 4',BASE+'onceuponatimeseason4'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjE0NDgxNDY2NV5BMl5BanBnXkFtZTgwNjU5Mjg5NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')
	addList('Season 5',BASE+'onceuponatimeseason5'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjE0NDgxNDY2NV5BMl5BanBnXkFtZTgwNjU5Mjg5NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg')

	
def DrWho():
	
	addList('Series 1',BASE+'drwhoseries1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTYwMzE2OTczMV5BMl5BanBnXkFtZTgwOTE0NjAzMTE@._V1_UY1200_CR485,0,630,1200_AL_.jpg')
	addList('Series 2',BASE+'drwhoseries2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTYwMzE2OTczMV5BMl5BanBnXkFtZTgwOTE0NjAzMTE@._V1_UY1200_CR485,0,630,1200_AL_.jpg')
	addList('Series 3',BASE+'drwhoseries3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTYwMzE2OTczMV5BMl5BanBnXkFtZTgwOTE0NjAzMTE@._V1_UY1200_CR485,0,630,1200_AL_.jpg')
	addList('Series 4',BASE+'drwhoseries4'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTYwMzE2OTczMV5BMl5BanBnXkFtZTgwOTE0NjAzMTE@._V1_UY1200_CR485,0,630,1200_AL_.jpg')
	addList('Series 5',BASE+'drwhoseries5'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTYwMzE2OTczMV5BMl5BanBnXkFtZTgwOTE0NjAzMTE@._V1_UY1200_CR485,0,630,1200_AL_.jpg')
	addList('Series 6',BASE+'drwhoseries6'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTYwMzE2OTczMV5BMl5BanBnXkFtZTgwOTE0NjAzMTE@._V1_UY1200_CR485,0,630,1200_AL_.jpg')
	addList('Series 7',BASE+'drwhoseries7'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTYwMzE2OTczMV5BMl5BanBnXkFtZTgwOTE0NjAzMTE@._V1_UY1200_CR485,0,630,1200_AL_.jpg')
	addList('Series 8',BASE+'drwhoseries8'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjI2MTc4MjMzMV5BMl5BanBnXkFtZTgwNDIyNzkwMjE@._V1_UY1200_CR88,0,630,1200_AL_.jpg')
	addList('Series 9',BASE+'drwhoseries9'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjI2MTc4MjMzMV5BMl5BanBnXkFtZTgwNDIyNzkwMjE@._V1_UY1200_CR88,0,630,1200_AL_.jpg')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
	
def Animated_TV():

	addList('Bobs Burgers',BASE+'bobsburgers1-3'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTg2MzI0NTQ3OV5BMl5BanBnXkFtZTgwODMyMzc1MDE@._V1_UY1200_CR93,0,630,1200_AL_.jpg')
	addList('Family Guy',BASE+'familyguymulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTk4MzM0MTU2MV5BMl5BanBnXkFtZTgwMTIwMzg3MjE@._V1_UY1200_CR204,0,630,1200_AL_.jpg')
	addList('South Park',BASE+'southparkmulti'+CAT,403,'http://ia.media-imdb.com/images/M/MV5BMTYwMzUwOTE0NF5BMl5BanBnXkFtZTcwMDUwNTY0NA@@._V1._CR0,0,372,469_UY1200_CR161,0,630,1200_AL_.jpg')


	xbmcplugin.endOfDirectory(addon_handle)
	
def Scifi_TV():

	addDir('Dr Who','',25,'http://ia.media-imdb.com/images/M/MV5BMjI2MTc4MjMzMV5BMl5BanBnXkFtZTgwNDIyNzkwMjE@._V1_UY1200_CR88,0,630,1200_AL_.jpg','background.jpg','')

	xbmcplugin.endOfDirectory(addon_handle)
	
def Soap_TV():

	xbmcplugin.endOfDirectory(addon_handle)

def Live_TV():

	addList('Freeview',BASE+'livetvtest'+CAT,400,ART + 'icon.png')
	addList('Alt Tv List',BASE+'alttv'+CAT,400,ART + 'icon.png')
	addList('Sports',BASE+'livesports'+CAT,400,ART + 'icon.png')
#	addDir('Full List','',86,ART + 'icon.png',ART + 'background.jpg','')
#	addList('World News','',66,ART + 'icon.png')

	if GetTVPassword == Decode('c3VzcGVjdHBhY2thZ2U='):
		addList('Live TV',TVFinalURL,400,ART + 'icon.png')

		
def LiveTVFull():
    html=OPEN_URL(Decode('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz'))
    match = re.compile('"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}',re.DOTALL).findall(html)
    for name,img,url,url2,url3 in match:
        addDir4(name,(url).replace('\\',''),401,img)
    for name,img,url,url2,url3 in match:
        addDir4(name,(url2).replace('\\',''),401,(img).replace('\\',''))
    for name,img,url,url2,url3 in match:
        addDir4(name,(url3).replace('\\',''),401,(img).replace('\\',''))

def WorldNews():

    html=OPEN_URL('http://wwitv.com/news_tv_live/index.html')
    match = re.compile('<tr><td width="100">.(.+?)<BR><a href="..(.+?)">(.+?)</a></td><td>').findall(html)
    for country,url,name in match:
        addDir3(country + ' - ' + name,'http://wwitv.com/%s'%url,67,'')
		
def WorldPlayUrl(url):

    html=OPEN_URL(url)
    match = re.compile('class="embed-responsive-item".+?src="(.+?)" frameborder="0" allowfullscreen></iframe></u><u></u></div></div>',re.DOTALL).findall(html)
    for url in match:
        addDir3('PLAY NEXT',url,68,ART + 'icon.png')
    else:
		html=OPEN_URL(url)
		match = re.compile('embed.+?<a href="(.+?)"',re.DOTALL).findall(html)
		for url in match:
			addDir3('PLAY',url,400,ART + 'icon.png')

		
def WorldPlayVid(url):
    html=OPEN_URL(url)
    match = re.compile('<a href="(.+?)"').findall(html)
    for url in match:
        addDir3('PLAY',url,401,'')


		
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def addDir4(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
	

def addDir(name,url,mode,iconimage,fanart,description): 
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
		liz.setProperty( "Fanart_Image", fanart )
		if mode==5 :
			ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		else:
			ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		
		return ok

def addList(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addVID(type,name,url,mode,iconimage = '',fanart = '',video = '',description = ''):
    if type != 'folder2' and type != 'addon':
        if len(iconimage) > 0:
            iconimage = ART + iconimage
        else:
            iconimage = 'DefaultFolder.png'
    if type == 'addon':
        if len(iconimage) > 0:
            iconimage = iconimage
        else:
            iconimage = 'http://totalxbmc.tv/addons/cache/images/4c79319887e240789ca125f144d989_addon-dummy.png'
    if fanart == '':
        fanart = FANART
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&video="+urllib.quote_plus(video)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
    liz.setProperty( "Fanart_Image", fanart )
    liz.setProperty( "Build.Video", video )
    if (type=='folder') or (type=='folder2') or (type=='tutorial_folder') or (type=='news_folder'):
        ok=Add_Directory_Item(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    else:
        ok=Add_Directory_Item(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def Add_Directory_Item(handle, url, listitem, isFolder):

    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder) 
