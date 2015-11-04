import sys
import urlparse
import yt
import time
import urllib,urllib2,re,base64,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import base64
import urlresolver
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net

addon_id='plugin.video.originentertainment'
CAT = base64.decodestring('LnBocA==')
BASE = base64.decodestring('aHR0cDovL2JhY2syYmFzaWNzLngxMGhvc3QuY29tL2JhY2syYmFzaWNzL3Rlc3Qv')
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Origin Entertainment"
VERSION = "1.0.1"
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART 		=  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
net = Net()

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def Home_Menu():
	addDir('Movies','',10,ART + 'icon.png',ART + 'background.png','')
	addDir('TV Shows','',11,ART + 'icon.png',ART + 'background.png','')
	addDir('Stand Up','',12,ART + 'icon.png',ART + 'background.png','')
	addDir('TEST AREA','',13,ART + 'icon.png',ART + 'background.png','')

	xbmcplugin.endOfDirectory(addon_handle)

def Films():   

	addList('Action',BASE+'actionfilm'+CAT,400,ART + 'icon.png')
	addList('Animation',BASE+'animationfilm'+CAT,400,ART + 'icon.png')
#	addList('Biography',BASE+'biographyfilm'+CAT,400,ART + 'icon.png')
	addList('Comedy',BASE+'comedyfilm'+CAT,400,ART + 'icon.png')
#	addList('Crime',BASE+'crimefilm'+CAT,400,ART + 'icon.png')
#	addList('Family',BASE+'familyfilm'+CAT,400,ART + 'icon.png')
#	addList('Fantasy',BASE+'fantasyfilm'+CAT,400,ART + 'icon.png')
	addList('History/Factual',BASE+'historyfilm'+CAT,400,ART + 'icon.png')
	addList('Horror',BASE+'horrorfilm'+CAT,400,ART + 'icon.png')
	addList('Kids',BASE+'kidsfilm'+CAT,400,ART + 'icon.png')
#	addList('Music',BASE+'musicfilm'+CAT,400,ART + 'icon.png')
#	addList('Romance',BASE+'romancefilm'+CAT,400,ART + 'icon.png')
#	addList('Scifi',BASE+'scififilm'+CAT,400,ART + 'icon.png')
	
	xbmcplugin.endOfDirectory(addon_handle)

def TV_Shows():
	
#	addList('Recent Episodes',BASE+'recentepisodes'+CAT,400,ART + 'icon.png')
#	addDir('Animated','',14,ART + 'icon.png',ART + 'background.png','')
	addDir('Action','',15,ART + 'icon.png',ART + 'background.png','')
	addDir('Childrens','',16,ART + 'icon.png',ART + 'background.png','')
	addDir('Comedy','',17,ART + 'icon.png',ART + 'background.png','')
	addDir('Drama','',18,ART + 'icon.png',ART + 'background.png','')
#	addDir('Entertainment','',19,ART + 'icon.png',ART + 'background.png','')
	addDir('Fantasy','',20,ART + 'icon.png',ART + 'background.png','')
#	addDir('Music','',21,ART + 'icon.png',ART + 'background.png','')
	addDir('Scifi','',22,ART + 'icon.png',ART + 'background.png','')
#	addDir('Soaps','',23,ART + 'icon.png',ART + 'background.png','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Stand_Up():

	addVID('','Billy Connolly','2kuspt3Cglo',9,'icon.png',ART + 'background.png','','')
	addVID('','Dara O Briain','39LK1A1YGPc',9,'icon.png',ART + 'background.png','','')
	addVID('','Frankie Boyle','PR1hrP6YBR4',9,'icon.png',ART + 'background.png','','')
	addVID('','Lee Evans','8JHWGMVTLwQ',9,'icon.png','',ART + 'background.png','')
	addDir('Jeff Dunham','',24,ART + 'icon.png',ART + 'background.png','')
	addVID('','Micheal Mcintyre','W1Aa503qr-E',9,'icon.png',ART + 'background.png','','')
	addVID('','Mrs Browns Boys','nmGf1k0nfwo',9,'icon.png',ART + 'background.png','','')
	addVID('','Sean Lock','iBcnfgM43VM',9,'icon.png',ART + 'background.png','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Jeff_Dunham():

	addVID('','Spark of insanity','UDBYXC8EUsg',9,'icon.png',ART + 'background.png','','')
	addVID('','Unhinged','I6whmmHRYO8',9,'icon.png',ART + 'background.png','','')
	addVID('','Achmed saves america','OV0Gd0ClBg',9,'icon.png',ART + 'background.png','','')
	addVID('','Very Special Christmas Special','-5ASk6u2ik4',9,'icon.png',ART + 'background.png','','')
	addVID('','All over the map','5POeSnPslv0',9,'icon.png',ART + 'background.png','','')
	addVID('','Controlled Chaos','CcJAFTB6omQ',9,'icon.png',ART + 'background.png','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Test():

	
	xbmcplugin.endOfDirectory(addon_handle)
		
def Childrens_TV():

	addList('Bing',BASE+'bing'+CAT,400,'http://goo.gl/IHk8Ya')
	addVID('','Minnie Mouse Bowtique','xNbjhNmNUGA',9,'Icon.jpg',ART + 'background.png','','')
	addVID('','Mickey Mouse Clubhouse','vn6xsuAokPg',9,'Icon.jpg',ART + 'background.png','','')
	addVID('','Mickey Mouse goofy and donald duck cartoons','blIHV79HplU',9,'Icon.jpg',ART + 'background.png','','')
	addVID('','Mickeys Once Upon A Christmas','X_ULfylsMzY',9,'Icon.jpg',ART + 'background.png','','')
	addVID('','Pluto Meets Cute Little Critters','3BkNDE5GI0g',9,'Icon.jpg',ART + 'background.png','','')
	addVID('','Walt Disney Classic Cartoons','s0IGJUTQQus',9,'Icon.jpg',ART + 'background.png','','')
	addVID('','Winter Cartoon Classics','vJw5IPX-mLI',9,'Icon.jpg',ART + 'background.png','','')
	

	xbmcplugin.endOfDirectory(addon_handle)
	
def Comedy_TV():
	
	addDir('Mock The Week','',28,ART + 'mock.png',ART + 'background.png','')
	addDir('The Inbetweeners','',29,ART + 'inbetween.png',ART + 'background.png','')
	addDir('The Last Man On Earth','',32,'http://ia.media-imdb.com/images/M/MV5BMTQ3NTEzODcyNl5BMl5BanBnXkFtZTgwNjY1NzU2NDE@._V1_SY317_CR2,0,214,317_AL_.jpg',ART + 'background.png','')
	addDir('Would I Lie To You','',30,ART + 'wouldi.jpg',ART + 'background.png','')

	xbmcplugin.endOfDirectory(addon_handle)
	
def The_Last_Man_On_Earth():
	
	addList('Series 1',BASE+'lastmanonearthseries1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ3NTEzODcyNl5BMl5BanBnXkFtZTgwNjY1NzU2NDE@._V1_SY317_CR2,0,214,317_AL_.jpg')
	addList('Series 2',BASE+'lastmanonearthseries2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ3NTEzODcyNl5BMl5BanBnXkFtZTgwNjY1NzU2NDE@._V1_SY317_CR2,0,214,317_AL_.jpg')
	
def Inbetweeners():

	addVID('','Series 1 Episode 1','e1_qe2Y9cYE',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 2','yh7kTxF-xUU',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 3','WdMIksVRI2o',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 4','kqHRsHp1DKk',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 5','JftuhfsVkQ4',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 6','rIv02RHqF7Q',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 1','qsyhn98YhQE',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 2','l5Ghi_mmzF8',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 3','Fduc924tmx8',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 4','reaRXLh9BqQ',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 5','ol7vl4BftWU',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 6','fBDF9YXYYg0',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 1','CC-YbIKquDM',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 3	Episode 2','Twj7poTUibs',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 3','utvj7FyBtRI',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 4','HwVMRcOyhWA',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 5','mCZd3Uz7lbo',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 6','_pngx_MTZgs',9,'inbetween.png',ART + 'background.png','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def WouldILieToYou():
	
	addVID('','Series 1 Episode 1','ql3yoGIBlOw',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 1 Episode 2','d4QYhPWCC4M',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 1 Episode 3','x1aSCd2T13o',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 1 Episode 4','tEYiXt-gw-g',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 1 Episode 5','n4O2BqU4Gug',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 1 Episode 6','Svljl0kN2HE',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 1','E8DlNckBUFQ',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 3','UjeLRqCA53Q',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 4','gslBhWkBAlk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 5','4vSoZTZ2Oqs',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 6','VnYU4zQaE1c',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 7','aHcPRcWMB1c',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 8','Y4RQe_4yeSo',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 9','2grbT9fe7Pk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 3 Episode 1','UCPIBQDI0QM',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 3 Episode 2','hhSNKJ_lcNU',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 3 Episode 3','QbthTZVmNYk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 3 Episode 4','DJRLZV4Ec44',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 3 Episode 5','ZrnEJ5g4CLU',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 3 Episode 6','VSSCH5LcafA',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 3 Episode 7','K9h744kQGTM',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 3 Episode 8','4guAsXvaYfE',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 1 Part 1','7AYOdlw5Gg4',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 1 Part 2','Nj66dXc93U0',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 1 Part 3','Af5tAj0w2Ig',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 2 Part 1','ZtLI7s4GvnI',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 2 Part 2','8at1JnjYn58',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 3 Part 1','nkCdzNDP8CY',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 3 Part 2','mkcL-pW0MYk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 4','X9LG_kwG9uQ',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 5 Part 1','8oe8NUESnpA',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 5 Part 2','Ipb8dXlJqO4',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 6 Part 1','fWWJWsjclaQ',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 6 Part 2','YoegsEq9se0',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 7 Part 1','hS8BsP3sRf4',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 7 Part 2','OfRZO8-H-Sg',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 8 Part 1','loPuU_k3FT0',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 8 Part 2','NY3AyfzPJ1s',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 9 Part 1','HpM8HbO6KVQ',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 4 Episode 9 Part 2','7aahLFGgU4s',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 1','paKvWxTNl_w',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 2 Part 1','Z788yKSQPYE',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 2 Part 2','vAAUg3cp-Gc',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 3','xXnyKLgp3eg',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 4','gZ0LejGn0RI',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 5','3Iv2foOhh3g',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 6','L2dK_5Zg5Rg',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 7','LPs5nlYYQck',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 8','NHiEffV3Ixw',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 5 Episode 9','uEblflQB8GE',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 6 Episode 1','goi-_qyD7UU',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 6 Episode 2','txoRmRLHD-E',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 6 Episode 3','FvHR_5rI8NY',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 6 Episode 4','XOOe7-3jptw',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 6 Episode 5','9OL-NBu1S4M',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 6 Episode 6','1NFSwyz7Vqk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 6 Episode 7','JGSs-r3MTjU',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 6 Episode 8','m5YR12v8bMA',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 6 Episode 9','vgwUFePSlXI',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 7 Episode 1','SG1B36dxeJ0',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 7 Episode 2','7fWdlSdE9Fo',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 7 Episode 3','K_dUfIegnis',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 7 Episode 4','4er8rBrelyw',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 7 Episode 5','vbsNrE6Oocs',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 7 Episode 6','jflRZk9V_qY',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 7 Episode 7','4iznh63xL44',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Series 7 Episode 8','ZcP6V7hBRfs',9,'wouldi.jpg',ART + 'background.png','','')

		
	xbmcplugin.endOfDirectory(addon_handle)
	
def Mock_the_week():

	addVID('','Series 1 Episode 1','cQ0nx_OQa2A',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 2','M1NWfTh1C08',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 3','UupD9ps50aY',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 4','_KkoFa0IOXM',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 5','J7q_NyPB6Gc',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 1 Episode 6','evOnwzQYbhg',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 1','xCbZgLzq9k4',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 2','A6VKesdHI5c',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 3','pmkcBUtGyeY',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 5','5c3WeNzDO9w',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 6','toTke-pSKs',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 2 Episode 7','g-AwJFYmHoQ',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 1','fkE1s0wfmW0',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 2','6Ol7WcJlcDo',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 3','XXLotk-Ba80',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 4','eUxBAtawXfI',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 5','ovqxz4Rern4',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 3 Episode 6','CuJkZPESvwQ',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 1','KrY38wXPVYk',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 2','h9CUeiRwPVI',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 3','8kNquJdmqeM',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 4','AU4J63yifiA',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 5','vIq46nzKyGQ',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 6','KwRjGLG3IFo',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 7','FkKY9W10TYw',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 8','coL-Lvlrw9M',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 9','QwiTYfzQK1s',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 10','xDDhVNwO2aE',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 11','BaqdsavmksY',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 5 Episode 12','qEw0YCfNO74',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 1','75UqWFcBMPM',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 2','n5-vDCuaej0',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 3','wrKwUhIiNjc',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 4','dFT6TKz7KH0',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 5','WKyusa-fzO8',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 6','fQhhO_fkmUI',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 7','L0bJcaRsKHw',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 8','y07qKlYrSP8',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 9','MAdcaQb9reg',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 10','j0cUIh8diq0',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 11','ech5uIrI9e0',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 6 Episode 12','KltcEj-EMQY',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 1','xmG1kk8fUTc',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 2','E21zgdeXIs0',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 3','T6kPMKIq2mY',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 4','rCyuL3-PZ08',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 5','Uua8_aj73MU',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 6','XxPVBH1MYrU',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 7','21_5bC0d9Bk',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 8','LgD7_O1CeuI',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 9','pL6AkJvcZ8Y',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 10','FIOsd22eIW8',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 11','s3uxOnPJRVI',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 7 Episode 12','IpuFzS_0T0M',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 8 Episode 1','G-KwANeNMhc',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 8 Episode 2','olcTSdKMx-0',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 8 Episode 3','a5sH6X25CCs',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 8 Episode 4','c987j7XQ1_s',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 8 Episode 5','ldW25L3eIac',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 8 Episode 6','WZMJtq69MkA',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 1','CafIUOxcXMU',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 2','5VTwM7w4nac',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 4','ryQg-H-07KI',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 5','CrpCRDYD-PQ',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 6','z6IATgpcBdM',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 7','K_OQ5h_HoE4',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 8','J6IYnZbKd4o',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 9','qwG9Mr1vaB8',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 10','szvxK68bIXk',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 11','2h2eC2WfR3E',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 9 Episode 12','4F07lXvkp1M',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 1','ldbpxCbHh9w',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 2','tjBlwuWmzxM',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 4','yzZMtFt68Ck',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 5','0ZAPvNpbIdY',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 7','Rlv8J-9yV_8',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 8','uFbKUqOuhjg',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 9','XVNLk84mrvM',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 10','U0hB3Hagdnk',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 11','jrRzKV8wA48',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 10 Episode 12','q8lhK3tBpOs',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 1','iXvV0beQH20',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 2','P8tajImp7N8',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 3','QTmExC-SpDw',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 4','nzm3og9Vlu0',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 5','apHL_8ATG6g',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 6','sPSP6lK8nI0',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 8','-XpYdrHya1k',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 9','UUzhVqVFukY',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 11','Kef4X25zSRY',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 12','HasUHM-x3eo',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 11 Episode 13','6DbS1VB8HGo',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 1','zECxFkGNxkk',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 2','JUKfaubUmnY',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 3','TCvmtAsggMI',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 4','VL4ajGla344',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 5','rDQTzFloalE',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 6','Ghj7SmJnCz8',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 8','TJZOYntCnwA',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 9','jTsFD407hIE',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 10','YktFqujwQas',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 11','wjM4p1ahz-Y',9,'mock.png',ART + 'background.png','','')
	addVID('','Series 12 Episode 13','kiXTed_g_PQ',9,'mock.png',ART + 'background.png','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Drama_TV():

	addDir('Fargo','',33,'http://ia.media-imdb.com/images/M/MV5BNDEzOTYzMDkzN15BMl5BanBnXkFtZTgwODkzNTAyNjE@._V1_SY317_CR4,0,214,317_AL_.jpg',ART + 'background.png','')
	addList('Quantico',BASE+'quantico'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTg2NjU1NTkyMl5BMl5BanBnXkFtZTgwMzk5Mjg5NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addDir('The Knick','',34,'http://ia.media-imdb.com/images/M/MV5BMTQ5NzcyNDc5MV5BMl5BanBnXkFtZTgwMDMyOTY5NjE@._V1_SX214_AL_.jpg',ART + 'background.png','')
	addList('The Last Kingdom',BASE+'thelastkingdom'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjE1MzYzNjk3OF5BMl5BanBnXkFtZTgwMzk0MzYwNzE@._V1_SX214_AL_.jpg')

	xbmcplugin.endOfDirectory(addon_handle)
	
def The_Knick():

	addList('Season 1',BASE+'the-knick'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ5NzcyNDc5MV5BMl5BanBnXkFtZTgwMDMyOTY5NjE@._V1_SX214_AL_.jpg')
	addList('Season 2',BASE+'the-knickseason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ5NzcyNDc5MV5BMl5BanBnXkFtZTgwMDMyOTY5NjE@._V1_SX214_AL_.jpg')
	
def Fargo():

	addList('Series 1',BASE+'fargo'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BNDEzOTYzMDkzN15BMl5BanBnXkFtZTgwODkzNTAyNjE@._V1_SY317_CR4,0,214,317_AL_.jpg')
	addList('Series 2',BASE+'fargoseries2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BNDEzOTYzMDkzN15BMl5BanBnXkFtZTgwODkzNTAyNjE@._V1_SY317_CR4,0,214,317_AL_.jpg')
	
def Entertainment_TV():

	xbmcplugin.endOfDirectory(addon_handle)
	
def Music_TV():

	xbmcplugin.endOfDirectory(addon_handle)
	
def Action_TV():

	addDir('Arrow','',26,ART + 'arrow.png',ART + 'background.png','')
	addList('Blindspot',BASE+'blindspot'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTczMTMyMzM2M15BMl5BanBnXkFtZTgwNzM1NDA2NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addDir('Flash','',27,ART + 'flash.jpg',ART + 'background.png','')
	addDir('Gotham','',27,'http://ia.media-imdb.com/images/M/MV5BMTQ1ODk3NDczNF5BMl5BanBnXkFtZTgwODE5MDQ4NjE@._V1_SY317_CR0,0,214,317_AL_.jpg',ART + 'background.png','')
	addDir('Sons Of Anarchy','',27,ART + 'flash.jpg',ART + 'background.png','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Gotham():
	
	addList('Season 1',BASE+'gotham.php'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ1ODk3NDczNF5BMl5BanBnXkFtZTgwODE5MDQ4NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addList('Season 2',BASE+'gothamseason2.php'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ1ODk3NDczNF5BMl5BanBnXkFtZTgwODE5MDQ4NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	
def Sons_Of_Anarchy()
	
	addList('Season 1',BASE+'SonsOfAnarchySeason1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTEyODg2NzkwMDBeQTJeQWpwZ15BbWU4MDQwODI3MzIx._V1_SX214_AL_.jpg')
	addList('Season 2',BASE+'SonsOfAnarchySeason2'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTEyODg2NzkwMDBeQTJeQWpwZ15BbWU4MDQwODI3MzIx._V1_SX214_AL_.jpg')
	addList('Season 3',BASE+'SonsOfAnarchySeason3'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTEyODg2NzkwMDBeQTJeQWpwZ15BbWU4MDQwODI3MzIx._V1_SX214_AL_.jpg')
	
def Arrow():

	addVID('','Series 4 Episode 1','uIS78BLxodE',9,'arrow.png',ART + 'background.png','','')
	addVID('','Series 4 Episode 2','xuu-hJP8K3g',9,'arrow.png',ART + 'background.png','','')
	addVID('','Series 4 Episode 3','9UFEqovbPxA',9,'arrow.png',ART + 'background.png','','')
	

	xbmcplugin.endOfDirectory(addon_handle)

def Flash():

	addList('Season 1',BASE+'theflashseries1'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BNjAwNzkxNzAwNF5BMl5BanBnXkFtZTgwODg2NTc2NjE@._V1_SY317_CR19,0,214,317_AL_.jpg')
	addDir('Season 2','',31,'http://ia.media-imdb.com/images/M/MV5BNjAwNzkxNzAwNF5BMl5BanBnXkFtZTgwODg2NTc2NjE@._V1_SY317_CR19,0,214,317_AL_.jpg',ART + 'background.png','')
	
def Flash_Series2():
	
	addVID('','Series 2 Episode 1','-srjHKXgfnw',9,'flash.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 2','Qf6Wvbk0Vug',9,'flash.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 3','MVugMhH7EOQ',9,'flash.jpg',ART + 'background.png','','')
	addVID('','Series 2 Episode 4','VCzthVJu7d0',9,'flash.jpg',ART + 'background.png','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def Fantasy_TV():

	addList('Heroes Reborn',BASE+'heroesreborn'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMjI0NTE5NDIxOV5BMl5BanBnXkFtZTgwMDQ3ODM2NjE@._V1_SY317_CR0,0,214,317_AL_.jpg')
	addList('Limitless',BASE+'limitless'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTA4ODE4NjA5ODleQTJeQWpwZ15BbWU4MDUxMTQ0NTYx._V1_SX214_AL_.jpg')
	addList('Supergirl',BASE+'supergirl'+CAT,400,'')
	addList('The Walking Dead',BASE+'thewalkingdead'+CAT,400,'http://ia.media-imdb.com/images/M/MV5BMTQ3NzQ2Mzk1OF5BMl5BanBnXkFtZTgwNTAzNjI5NjE@._V1_SX214_AL_.jpg')

	xbmcplugin.endOfDirectory(addon_handle)
	
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
	
	
def Animated_TV():

	xbmcplugin.endOfDirectory(addon_handle)
	
def Scifi_TV():

	addDir('Dr Who','',25,'http://ia.media-imdb.com/images/M/MV5BMjI2MTc4MjMzMV5BMl5BanBnXkFtZTgwNDIyNzkwMjE@._V1_UY1200_CR88,0,630,1200_AL_.jpg','background.png','')

	xbmcplugin.endOfDirectory(addon_handle)
	
def Soap_TV():

	xbmcplugin.endOfDirectory(addon_handle)
	
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

def OPEN_URL(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link

def Live(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a.href="(.+?)".target="_blank"><img.src="(.+?)".style="max-width:200px;"./></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,name in match:
                addList2('%s'%(name).replace('Origin Entertainment','Origin Entertainment').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),401,'%s'%(iconimage))
def Resolve(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('LOADING','Opening %s Now'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve() 
    if dp.iscanceled(): 
        print "[COLORred]STREAM CANCELLED[/COLOR]" # need to get this part working    
        dialog = xbmcgui.Dialog()
        if dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
	         return
    else:
        try: play.play(url)
        except: pass
        try: ADDON.resolve_url(url) 
        except: pass 
        dp.close()
		
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 
	  
def addList(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addList2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:	
                params=sys.argv[2] 
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}	
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
		
params=get_params()
url=None
name=None
iconimage=None
mode=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

if mode == None		: Home_Menu()
elif mode == 9		: yt.PlayVideo(url)
elif mode == 10		: Films()
elif mode == 11		: TV_Shows()
elif mode == 12 	: Stand_Up()
elif mode == 13		: Test()
elif mode == 14		: Animated_TV()
elif mode == 15		: Action_TV()
elif mode == 16		: Childrens_TV()
elif mode == 17		: Comedy_TV()
elif mode == 18		: Drama_TV()
elif mode == 19		: Entertainment_TV()
elif mode == 20		: Fantasy_TV()
elif mode == 21		: Music_TV()
elif mode == 22		: Scifi_TV()
elif mode == 23		: Soap_TV()
elif mode == 24		: Jeff_Dunham()
elif mode == 25		: DrWho()
elif mode == 26		: Arrow()
elif mode == 27		: Flash()
elif mode == 28		: Mock_the_week()
elif mode == 29		: Inbetweeners()
elif mode == 30		: WouldILieToYou()
elif mode == 31		: Flash_Series2()
elif mode == 32 	: The_Last_Man_On_Earth()
elif mode == 33 	: Fargo()
elif mode == 34		: The_Knick()
elif mode == 35 	: Gotham()
elif mode == 36 	: Sons_Of_Anarchy()

elif mode == 401	: Resolve(url)
elif mode == 400 	: Live(url)
	
xbmcplugin.endOfDirectory(int(sys.argv[1]))