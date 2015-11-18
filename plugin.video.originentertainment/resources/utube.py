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


addon_id='plugin.video.originentertainment'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Origin Entertainment"
VERSION = "1.0.1"
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART 		=  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
net = Net()

def Add_Directory_Item(handle, url, listitem, isFolder):

    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder) 

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


def Mock_the_week():

	addVID('','Season 1 Episode 1','cQ0nx_OQa2A',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 2','M1NWfTh1C08',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 3','UupD9ps50aY',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 4','_KkoFa0IOXM',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 5','J7q_NyPB6Gc',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 6','evOnwzQYbhg',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 1','xCbZgLzq9k4',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 2','A6VKesdHI5c',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 3','pmkcBUtGyeY',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 5','5c3WeNzDO9w',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 6','toTke-pSKs',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 7','g-AwJFYmHoQ',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 1','fkE1s0wfmW0',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 2','6Ol7WcJlcDo',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 3','XXLotk-Ba80',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 4','eUxBAtawXfI',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 5','ovqxz4Rern4',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 6','CuJkZPESvwQ',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 1','KrY38wXPVYk',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 2','h9CUeiRwPVI',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 3','8kNquJdmqeM',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 4','AU4J63yifiA',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 5','vIq46nzKyGQ',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 6','KwRjGLG3IFo',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 7','FkKY9W10TYw',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 8','coL-Lvlrw9M',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 9','QwiTYfzQK1s',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 10','xDDhVNwO2aE',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 11','BaqdsavmksY',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 5 Episode 12','qEw0YCfNO74',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 1','75UqWFcBMPM',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 2','n5-vDCuaej0',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 3','wrKwUhIiNjc',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 4','dFT6TKz7KH0',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 5','WKyusa-fzO8',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 6','fQhhO_fkmUI',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 7','L0bJcaRsKHw',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 8','y07qKlYrSP8',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 9','MAdcaQb9reg',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 10','j0cUIh8diq0',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 11','ech5uIrI9e0',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 6 Episode 12','KltcEj-EMQY',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 1','xmG1kk8fUTc',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 2','E21zgdeXIs0',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 3','T6kPMKIq2mY',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 4','rCyuL3-PZ08',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 5','Uua8_aj73MU',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 6','XxPVBH1MYrU',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 7','21_5bC0d9Bk',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 8','LgD7_O1CeuI',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 9','pL6AkJvcZ8Y',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 10','FIOsd22eIW8',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 11','s3uxOnPJRVI',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 7 Episode 12','IpuFzS_0T0M',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 8 Episode 1','G-KwANeNMhc',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 8 Episode 2','olcTSdKMx-0',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 8 Episode 3','a5sH6X25CCs',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 8 Episode 4','c987j7XQ1_s',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 8 Episode 5','ldW25L3eIac',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 8 Episode 6','WZMJtq69MkA',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 1','CafIUOxcXMU',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 2','5VTwM7w4nac',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 4','ryQg-H-07KI',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 5','CrpCRDYD-PQ',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 6','z6IATgpcBdM',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 7','K_OQ5h_HoE4',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 8','J6IYnZbKd4o',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 9','qwG9Mr1vaB8',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 10','szvxK68bIXk',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 11','2h2eC2WfR3E',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 9 Episode 12','4F07lXvkp1M',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 1','ldbpxCbHh9w',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 2','tjBlwuWmzxM',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 4','yzZMtFt68Ck',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 5','0ZAPvNpbIdY',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 7','Rlv8J-9yV_8',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 8','uFbKUqOuhjg',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 9','XVNLk84mrvM',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 10','U0hB3Hagdnk',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 11','jrRzKV8wA48',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 10 Episode 12','q8lhK3tBpOs',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 1','iXvV0beQH20',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 2','P8tajImp7N8',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 3','QTmExC-SpDw',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 4','nzm3og9Vlu0',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 5','apHL_8ATG6g',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 6','sPSP6lK8nI0',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 8','-XpYdrHya1k',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 9','UUzhVqVFukY',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 11','Kef4X25zSRY',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 12','HasUHM-x3eo',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 11 Episode 13','6DbS1VB8HGo',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 1','zECxFkGNxkk',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 2','JUKfaubUmnY',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 3','TCvmtAsggMI',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 4','VL4ajGla344',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 5','rDQTzFloalE',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 6','Ghj7SmJnCz8',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 8','TJZOYntCnwA',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 9','jTsFD407hIE',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 10','YktFqujwQas',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 11','wjM4p1ahz-Y',9,'mock.png',ART + 'background.png','','')
	addVID('','Season 12 Episode 13','kiXTed_g_PQ',9,'mock.png',ART + 'background.png','','')
	
	xbmcplugin.endOfDirectory(addon_handle)

def WouldILieToYou():
	
	addVID('','Season 1 Episode 1','ql3yoGIBlOw',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 1 Episode 2','d4QYhPWCC4M',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 1 Episode 3','x1aSCd2T13o',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 1 Episode 4','tEYiXt-gw-g',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 1 Episode 5','n4O2BqU4Gug',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 1 Episode 6','Svljl0kN2HE',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 2 Episode 1','E8DlNckBUFQ',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 2 Episode 3','UjeLRqCA53Q',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 2 Episode 4','gslBhWkBAlk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 2 Episode 5','4vSoZTZ2Oqs',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 2 Episode 6','VnYU4zQaE1c',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 2 Episode 7','aHcPRcWMB1c',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 2 Episode 8','Y4RQe_4yeSo',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 2 Episode 9','2grbT9fe7Pk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 3 Episode 1','UCPIBQDI0QM',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 3 Episode 2','hhSNKJ_lcNU',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 3 Episode 3','QbthTZVmNYk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 3 Episode 4','DJRLZV4Ec44',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 3 Episode 5','ZrnEJ5g4CLU',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 3 Episode 6','VSSCH5LcafA',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 3 Episode 7','K9h744kQGTM',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 3 Episode 8','4guAsXvaYfE',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 1 Part 1','7AYOdlw5Gg4',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 1 Part 2','Nj66dXc93U0',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 1 Part 3','Af5tAj0w2Ig',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 2 Part 1','ZtLI7s4GvnI',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 2 Part 2','8at1JnjYn58',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 3 Part 1','nkCdzNDP8CY',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 3 Part 2','mkcL-pW0MYk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 4','X9LG_kwG9uQ',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 5 Part 1','8oe8NUESnpA',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 5 Part 2','Ipb8dXlJqO4',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 6 Part 1','fWWJWsjclaQ',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 6 Part 2','YoegsEq9se0',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 7 Part 1','hS8BsP3sRf4',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 7 Part 2','OfRZO8-H-Sg',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 8 Part 1','loPuU_k3FT0',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 8 Part 2','NY3AyfzPJ1s',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 9 Part 1','HpM8HbO6KVQ',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 4 Episode 9 Part 2','7aahLFGgU4s',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 1','paKvWxTNl_w',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 2 Part 1','Z788yKSQPYE',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 2 Part 2','vAAUg3cp-Gc',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 3','xXnyKLgp3eg',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 4','gZ0LejGn0RI',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 5','3Iv2foOhh3g',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 6','L2dK_5Zg5Rg',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 7','LPs5nlYYQck',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 8','NHiEffV3Ixw',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 5 Episode 9','uEblflQB8GE',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 6 Episode 1','goi-_qyD7UU',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 6 Episode 2','txoRmRLHD-E',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 6 Episode 3','FvHR_5rI8NY',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 6 Episode 4','XOOe7-3jptw',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 6 Episode 5','9OL-NBu1S4M',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 6 Episode 6','1NFSwyz7Vqk',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 6 Episode 7','JGSs-r3MTjU',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 6 Episode 8','m5YR12v8bMA',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 6 Episode 9','vgwUFePSlXI',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 7 Episode 1','SG1B36dxeJ0',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 7 Episode 2','7fWdlSdE9Fo',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 7 Episode 3','K_dUfIegnis',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 7 Episode 4','4er8rBrelyw',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 7 Episode 5','vbsNrE6Oocs',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 7 Episode 6','jflRZk9V_qY',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 7 Episode 7','4iznh63xL44',9,'wouldi.jpg',ART + 'background.png','','')
	addVID('','Season 7 Episode 8','ZcP6V7hBRfs',9,'wouldi.jpg',ART + 'background.png','','')

		
	xbmcplugin.endOfDirectory(addon_handle)

def Inbetweeners():

	addVID('','Season 1 Episode 1','e1_qe2Y9cYE',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 2','yh7kTxF-xUU',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 3','WdMIksVRI2o',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 4','kqHRsHp1DKk',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 5','JftuhfsVkQ4',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 1 Episode 6','rIv02RHqF7Q',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 1','qsyhn98YhQE',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 2','l5Ghi_mmzF8',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 3','Fduc924tmx8',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 4','reaRXLh9BqQ',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 5','ol7vl4BftWU',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 2 Episode 6','fBDF9YXYYg0',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 1','CC-YbIKquDM',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 3	Episode 2','Twj7poTUibs',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 3','utvj7FyBtRI',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 4','HwVMRcOyhWA',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 5','mCZd3Uz7lbo',9,'inbetween.png',ART + 'background.png','','')
	addVID('','Season 3 Episode 6','_pngx_MTZgs',9,'inbetween.png',ART + 'background.png','','')
	
	xbmcplugin.endOfDirectory(addon_handle)
