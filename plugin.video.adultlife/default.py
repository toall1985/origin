# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from lib import process
from threading import Thread
addon_id = 'plugin.video.adultlife'
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.adultlife/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.adultlife/'
favourites = ADDON_DATA + 'favourites'
ADDON = xbmcaddon.Addon(id=addon_id)
Adult_Pass = ADDON.getSetting('Adult')
Adult_Default = ADDON.getSetting('Porn_Pass')

if os.path.exists(favourites) == True:
    FAV = open(favourites).read()
else:
    FAV = []

def Main_Menu():
    if Adult_Pass == Adult_Default:
		process.Menu('X Videos','',700,'https://pbs.twimg.com/profile_images/378800000578199366/cf160c1c86c13778a834bbade0c30e38.jpeg',FANART,'','')
		process.Menu('Porn Hub','',708,'http://cdimage.debian.org/mirror/addons.superrepo.org/v7/addons/plugin.video.pornhub/icon.png',FANART,'','')
		process.Menu('X Hamster','',714,'http://www.logospike.com/wp-content/uploads/2016/05/Xhamster_Logo_03.png',FANART,'','')
		process.Menu('Chaturbate','',720,'https://pbs.twimg.com/profile_images/671662441210753024/sE2tHWMB_400x400.png',FANART,'','')
		process.Menu('You Porn','',723,'http://www.ares-portal.com/wp-content/uploads/2016/12/plugin.video_.youporngay.png',FANART,'','')
		process.Menu('Red Tube','',730,'http://gosha-portal.pp.ua/1311/pic/redtube.png',FANART,'','')
		process.Menu('Tube 8','',738,'https://a3-images.myspacecdn.com/images03/1/cb9e1e694ca941abaf62f0026d18049f/300x300.jpg',FANART,'','')
		process.Menu('Thumbzilla','',745,'http://static.spark.autodesk.com/2013/02/14__13_53_32/data2cd61048-351b-4b48-bd9c-946e7e076b53Medium2.jpg',FANART,'','')
		process.Menu('XTube','',753,'https://pbs.twimg.com/profile_images/732348322044903425/xTK0J4Cz.jpg',FANART,'','')
		process.Menu('Eporner','',760,'http://kenny2u.org/wp-content/uploads/2016/09/icon-1.png',FANART,'','')
		process.Menu('YouJizz','',771,'https://pbs.twimg.com/profile_images/3332003625/23c080fbec17cfb45ca3fd40ec06afe1.png',FANART,'','')
		process.Menu('Spank Wire','',772,'http://kenny2u.org/wp-content/uploads/2016/09/icon-43.png',FANART,'','')
		process.Menu('4k','',758,'https://pbs.twimg.com/profile_images/700315084980035588/fZZO6Pf-.jpg',FANART,'','')
		process.Menu('VR','http://www.xvideos.com/?k=vr',701,'https://pbs.twimg.com/profile_images/741907565689217024/DByQczLO.jpg',FANART,'','')
	
def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
		
				
		
# ===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------

def addFavorite(name, url, mode, iconimage, fanart, description, extra):
    favList = []
    xbmc.log(extra)
    try:
        name = name.encode('utf-8', 'ignore')
    except:
        pass
    if os.path.exists(favourites) == False:
        favList.append((name, url, mode, iconimage, fanart, description, extra))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        a = open(favourites).read()
        data = json.loads(a)
        data.append((name, url, mode, iconimage, fanart, description, extra))
        b = open(favourites, "w")
        b.write(json.dumps(data))
        b.close()


def getFavourites():
    if not os.path.exists(favourites):
        favList = []
        favList.append(('REPLACE_THIS_NAME Favourites Section', '', '', '', '', '', ''))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        items = json.loads(open(favourites).read())
        for i in items:
            name = i[0]
            url = i[1]
            try:
			    iconimage = i[3]
            except:
                iconimage = ''
            try:
                fanart = i[4]
            except:
                fanart = ''
            try:
                description = i[5]
            except:
                description = ''
            try:
                extra = i[6]
            except:
                extra = ''

            if i[2] == 20:
                Play(name, url, i[2], iconimage, fanart, description, extra, 'fav')
            else:
                Menu(name, url, i[2], iconimage, fanart, description, extra, 'fav')


def rmFavorite(name):
    data = json.loads(open(favourites).read())
    for index in range(len(data)):
        if data[index][0] == name:
            del data[index]
            b = open(favourites, "w")
            b.write(json.dumps(data))
            b.close()
            break
    xbmc.executebuiltin("XBMC.Container.Refresh")		

def resolve(name,url): 
	xbmc.Player().play(url, xbmcgui.ListItem(name))
	xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
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
fanart=None
description=None
trailer=None
fav_mode=None
extra=None

try:
    extra=urllib.unquote_plus(params["extra"])
except:
    pass

try:
    fav_mode=int(params["fav_mode"])
except:
    pass

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

#####################################################END PROCESSES##############################################################		
		
if mode == None: Main_Menu()
elif mode == 2 : Search()

elif mode == 10: getFavourites()
elif mode==11:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name, url, fav_mode, iconimage, fanart, description, extra)
elif mode==12:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)
elif mode == 14 : queueItem()	
elif mode == 20: resolve(name,url)
elif mode == 700: from lib import xxx_vids;xxx_vids.X_vid_Menu()
elif mode == 701: from lib import xxx_vids;xxx_vids.XNew_Videos(url)
elif mode == 702: from lib import xxx_vids;xxx_vids.XGenres(url)
elif mode == 703: from lib import xxx_vids;xxx_vids.XPornstars(url)
elif mode == 704: from lib import xxx_vids;xxx_vids.XSearch_X()
elif mode == 705: from lib import xxx_vids;xxx_vids.Xtags(url)
elif mode == 706: from lib import xxx_vids;xxx_vids.XPlayLink(url)
elif mode == 707: from lib import xxx_vids;xxx_vids.Porn_Menu()
elif mode == 708: from lib import xxx_vids;xxx_vids.Porn_Hub()
elif mode == 709: from lib import xxx_vids;xxx_vids.get_video_item(url)
elif mode == 710: from lib import xxx_vids;xxx_vids.get_cat_item(url)
elif mode == 711: from lib import xxx_vids;xxx_vids.get_pornhub_playlinks(url)
elif mode == 712: from lib import xxx_vids;xxx_vids.get_pornstar(url)
elif mode == 713: from lib import xxx_vids;xxx_vids.search_pornhub()
elif mode == 714: from lib import xxx_vids;xxx_vids.XHamster()
elif mode == 715: from lib import xxx_vids;xxx_vids.hamster_cats(url)
elif mode == 716: from lib import xxx_vids;xxx_vids.get_hamster_vid(url)
elif mode == 717: from lib import xxx_vids;xxx_vids.chaturbate_tags(url)
elif mode == 718: from lib import xxx_vids;xxx_vids.hamster_cats_split(name,url)
elif mode == 719: from lib import xxx_vids;xxx_vids.get_hamster_playlinks(url)
elif mode == 720: from lib import xxx_vids;xxx_vids.chaturbate()
elif mode == 721: from lib import xxx_vids;xxx_vids.chaturbate_videos(url)
elif mode == 722: from lib import xxx_vids;xxx_vids.chaturbate_playlink(url)
elif mode == 723: from lib import xxx_vids;xxx_vids.YouPorn()
elif mode == 724: from lib import xxx_vids;xxx_vids.youporn_new_video(url)
elif mode == 725: from lib import xxx_vids;xxx_vids.youporn_video(url)
elif mode == 726: from lib import xxx_vids;xxx_vids.youporn_collections(url)
elif mode == 727: from lib import xxx_vids;xxx_vids.youporn_categories(url)
elif mode == 728: from lib import xxx_vids;xxx_vids.youporn_playlink(url)
elif mode == 729: from lib import xxx_vids;xxx_vids.search_youporn(url)
elif mode == 730: from lib import xxx_vids;xxx_vids.redtube()
elif mode == 731: from lib import xxx_vids;xxx_vids.redtube_video(url)
elif mode == 732: from lib import xxx_vids;xxx_vids.redtube_playlink(url)
elif mode == 733: from lib import xxx_vids;xxx_vids.redtube_channels(url)
elif mode == 734: from lib import xxx_vids;xxx_vids.redtube_pornstars(url)
elif mode == 735: from lib import xxx_vids;xxx_vids.redtube_collections(url)
elif mode == 736: from lib import xxx_vids;xxx_vids.redtube_cats(url)
elif mode == 737: from lib import xxx_vids;xxx_vids.redtube_search(url)
elif mode == 738: from lib import xxx_vids;xxx_vids.tube8()
elif mode == 739: from lib import xxx_vids;xxx_vids.tube8_videos(url)
elif mode == 740: from lib import xxx_vids;xxx_vids.tube8_playlink(url)
elif mode == 741: from lib import xxx_vids;xxx_vids.tube8_cats(url)
elif mode == 742: from lib import xxx_vids;xxx_vids.tube8_tags(url)
elif mode == 743: from lib import xxx_vids;xxx_vids.tube8_search()
elif mode == 744: from lib import xxx_vids;xxx_vids.tube8_letters(name,url)
elif mode == 745: from lib import xxx_vids;xxx_vids.thumbzilla()
elif mode == 746: from lib import xxx_vids;xxx_vids.thumbzilla_videos(url)
elif mode == 747: from lib import xxx_vids;xxx_vids.thumbzilla_tags(url)
elif mode == 748: from lib import xxx_vids;xxx_vids.thumbzilla_pornstars(url)
elif mode == 749: from lib import xxx_vids;xxx_vids.thumbzilla_cats(url)
elif mode == 750: from lib import xxx_vids;xxx_vids.thumbzilla_search()
elif mode == 751: from lib import xxx_vids;xxx_vids.thumbzilla_tags_letters(name,url)
elif mode == 752: from lib import xxx_vids;xxx_vids.thumbzilla_playlink(url)
elif mode == 753: from lib import xxx_vids;xxx_vids.xtube()
elif mode == 754: from lib import xxx_vids;xxx_vids.xtube_videos(url)
elif mode == 755: from lib import xxx_vids;xxx_vids.xtube_cats(url)
elif mode == 756: from lib import xxx_vids;xxx_vids.xtube_search(url)
elif mode == 757: from lib import xxx_vids;xxx_vids.xtube_playlink(url)
elif mode == 758: from lib import xxx_vids;xxx_vids.fourK()
elif mode == 759: from lib import xxx_vids;xxx_vids.eporner_playlink(url)
elif mode == 760: from lib import xxx_vids;xxx_vids.eporner()
elif mode == 761: from lib import xxx_vids;xxx_vids.eporner_video(url)
elif mode == 762: from lib import xxx_vids;xxx_vids.eporner_pornstar(url)
elif mode == 763: from lib import xxx_vids;xxx_vids.eporner_cats(url)
elif mode == 764: from lib import xxx_vids;xxx_vids.eporner_search()
elif mode == 765: from lib import xxx_vids;xxx_vids.youjizz_videos(url)
elif mode == 766: from lib import xxx_vids;xxx_vids.youjizz_tags(url)
elif mode == 767: from lib import xxx_vids;xxx_vids.youjizz_pornstars(url)
elif mode == 768: from lib import xxx_vids;xxx_vids.youjizz_search()
elif mode == 769: from lib import xxx_vids;xxx_vids.youjizz_playlink(url)
elif mode == 770: from lib import xxx_vids;xxx_vids.youjizz_tags_letters(name,url)
elif mode == 771: from lib import xxx_vids;xxx_vids.youjizz()
elif mode == 772: from lib import xxx_vids;xxx_vids.spank_wire()
elif mode == 773: from lib import xxx_vids;xxx_vids.spank_cats(url)
elif mode == 774: from lib import xxx_vids;xxx_vids.spank_tags(url)
elif mode == 775: from lib import xxx_vids;xxx_vids.spank_videos(url)
elif mode == 776: from lib import xxx_vids;xxx_vids.spank_search()
elif mode == 777: from lib import xxx_vids;xxx_vids.spank_playlink(url)
elif mode == 778: from lib import xxx_vids;xxx_vids.spank_tags_letter(name,url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))