import json
import os
import sys
import urllib
import urllib2
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.iamgroot/')
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.iamgroot/'
if not os.path.exists(ADDON_DATA):
    os.makedirs(ADDON_DATA)
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
Dialog = xbmcgui.Dialog()
addon_id = 'plugin.video.iamgroot'
ADDON = xbmcaddon.Addon(id=addon_id)
PATH = 'I Am Groot'
VERSION = '0.0.1'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
    FAV = open(favourites).read()
else:
    FAV = []
watched = ADDON_DATA + 'watched'
if os.path.exists(watched) == True:
    WATCHED = open(watched).read()
else:
    WATCHED = []
imdbFile = ADDON_DATA + 'imdb'
if os.path.exists(imdbFile) == True:
    IMDB = open(imdbFile).read()
else:
    IMDB = []
dp = xbmcgui.DialogProgress()
addon_handle = int(sys.argv[1])
List = []
temp_file = ADDON_PATH + 'Temp.txt'
debug = ADDON.getSetting('debug')


def Menu(name, url, mode, iconimage, fanart, description, extra, showcontext=True, allinfo={},folder=True):
    if iconimage == '':
        iconimage = ICON
    elif iconimage == ' ':
        iconimage = ICON
    if fanart == '':
        fanart = FANART
    elif fanart == ' ':
        fanart = FANART
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&fanart=" + urllib.quote_plus(
        fanart) + "&description=" + urllib.quote_plus(description) + "&extra=" + urllib.quote_plus(extra)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    liz.setProperty("Fanart_Image", fanart)
    if 'imdb' in url:
        if 'title' in url:
            if not name in IMDB:
                imdb_log(name,url,iconimage)
    if showcontext:
        contextMenu = []
        if showcontext == 'fav':
            contextMenu.append(('Remove from I am groot Favorites', 'XBMC.RunPlugin(%s?mode=12&name=%s)'
                                % (sys.argv[0], urllib.quote_plus(name))))
        if not name in FAV:
            contextMenu.append(('Add to I am groot Favorites',
                                'XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                                % (sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url),
                                   urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
        if showcontext == 'watched':
            contextMenu.append(('Remove from I am groot Watched List', 'XBMC.RunPlugin(%s?mode=17&name=%s)'
                                % (sys.argv[0], urllib.quote_plus(name))))
        liz.addContextMenuItems(contextMenu)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=folder)
    return ok
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def PLAY(name, url, mode, iconimage, fanart, description, extra, showcontext=True, allinfo={}):
    url = url.replace('http:https:','http:')
    if url.startswith('//'):
        url = 'http:'+url
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&fanart=" + urllib.quote_plus(
        fanart) + "&description=" + urllib.quote_plus(description) + "&extra=" + urllib.quote_plus(extra)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage=" ", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    liz.setProperty("Fanart_Image", fanart)
    if showcontext:
        contextMenu = []
        if showcontext == 'fav':
            contextMenu.append(('Remove from I am groot Favorites', 'XBMC.RunPlugin(%s?mode=17&name=%s)'
                                % (sys.argv[0], urllib.quote_plus(name))))
        if not name in FAV:
            contextMenu.append(('Add to I am groot Favorites',
                                'XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                                % (sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url),
                                   urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
        if showcontext == 'watched':
            contextMenu.append(('Remove from I am groot Watched List', 'XBMC.RunPlugin(%s?mode=12&name=%s)'
                                % (sys.argv[0], urllib.quote_plus(name))))
        contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=1)' % sys.argv[0]))
        liz.addContextMenuItems(contextMenu)
    if '.mp4' in url or '.mkv' in url or 'm3u8' in url or '=m22' in url or '=m18' in url or '=m37' in url:
        if 'openload' in url:
            url2=u
        elif 'embed' in url:
            url2=u
        elif '.html' in url:
            url2=u
        else:
            url2 = url
    else:
        url2 = u
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url2, listitem=liz, isFolder=False)
    return ok
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def queueItem():
    return xbmc.executebuiltin('Action(Queue)')
	
def imdb_log(name,url,iconimage):
    imdbList = []
    try:
        # seems that after
        name = name.encode('utf-8', 'ignore')
    except:
        pass
    if os.path.exists(imdbFile) == False:
        imdbList.append((name,url,iconimage))
        a = open(imdbFile, "w")
        a.write(json.dumps(imdbList))
        a.close()
    else:
        a = open(imdbFile).read()
        data = json.loads(a)
        data.append((name,url,iconimage))
        b = open(imdbFile, "w")
        b.write(json.dumps(data))
        b.close()


def watched_shows(name,show_year,year,season,episode,imdb_url):
	if episode[0] == '0':
		episode = episode[1:]
	if season[0] == '0':
		season = season[1:]
	watchedList = []
	run = False

	try:
		# seems that after
		name = name.encode('utf-8', 'ignore')
	except:
		pass
	if os.path.exists(watched) == False:
		watchedList.append((name,show_year,year,season,episode,imdb_url))
		a = open(watched, "w")
		a.write(json.dumps(watchedList))
		a.close()
	file_open = json.loads(open(watched).read())
	for item in file_open:
		item_season = item[3]
		item_episode = item[4]
		item_name = item[0]
		if item_name == name:
			if item_season >= season:
				if item_episode < episode:
					run = True
		else:
			run = True
	if run == True:
		data = json.loads(open(watched).read())
		for index in range(len(data)):
			try:
				if data[index][0] == name:
					del data[index]
					b = open(watched, "w")
					b.write(json.dumps(data))
					b.close()
			except:
				pass
		a = open(watched).read()
		data = json.loads(a)
		data.append((name,show_year,year,season,episode,imdb_url))
		b = open(watched, "w")
		b.write(json.dumps(data))
		b.close()

def rmWatched(name):
    data = json.loads(open(watched).read())
    for index in range(len(data)):
        if data[index][0] == name:
            del data[index]
            b = open(watched, "w")
            b.write(json.dumps(data))
            b.close()
            break
    xbmc.executebuiltin("XBMC.Container.Refresh")

# ===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------

def addon_log(string):
    if debug == 'true':
        xbmc.log("[addon.live.Sanctuary-%s]: %s" % (addon_version, string))


def addFavorite(name, url, mode, iconimage, fanart, desc, extra):
    favList = []
    try:
        # seems that after
        name = name.encode('utf-8', 'ignore')
    except:
        pass
    if os.path.exists(favourites) == False:
        addon_log('Making Favorites File')
        favList.append((name, url, mode, iconimage, fanart, desc, extra))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        addon_log('Appending Favorites')
        a = open(favourites).read()
        data = json.loads(a)
        data.append((name, url, mode, iconimage, fanart, desc, extra))
        b = open(favourites, "w")
        b.write(json.dumps(data))
        b.close()


def getFavourites():
    if os.path.exists(favourites) == False:
        favList = []
        addon_log('Making Favorites File')
        favList.append(('I am Groot Favourites Section', '', '', '', '', '', ''))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        items = json.loads(open(favourites).read())
        for i in items:
            name = i[0]
            url = i[1]
            mode = i[2]
            iconimage = i[3]
            fanart = i[4]
            desc = i[5]
            extra = i[6]
            if i[4] == 906:
                Play(name, url, mode, iconimage, fanart, '', '', 'fav')
            else:
                Menu(name, url, mode, iconimage, fanart, '', '', 'fav')


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


############################## FAVOURITES END ###############################


def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = ''
    link = ''
    try:
        response = urllib2.urlopen(req)
        link = response.read()
        response.close()
    except:
        pass
    if link != '':
        return link
    else:
        link = 'Opened'
        return link


def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view') == 'true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType))



def Big_Resolve(name,url):
	import originresolver
	originresolver.originresolver(name,url)
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


