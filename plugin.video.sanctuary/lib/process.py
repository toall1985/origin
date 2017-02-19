import json
import os
import sys
import urllib
import urllib2
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.sanctuary/'
if not os.path.exists(ADDON_DATA):
    os.makedirs(ADDON_DATA)
    file_fav = ADDON_DATA + 'favourites'
    file_open = open(file_fav,'w+')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
Dialog = xbmcgui.Dialog()
addon_id = 'plugin.video.sanctuary'
ADDON = xbmcaddon.Addon(id=addon_id)
PATH = 'Sanctuary'
VERSION = '0.0.1'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
    FAV = open(favourites).read()
else:
    FAV = []
dp = xbmcgui.DialogProgress()
addon_handle = int(sys.argv[1])
List = []
temp_file = ADDON_PATH + 'Temp.txt'
debug = ADDON.getSetting('debug')


def Menu(name, url, mode, iconimage, fanart, description, extra, showcontext=True, allinfo={}):
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
    if showcontext:
        contextMenu = []
        if showcontext == 'fav':
            contextMenu.append(('Remove from Sanctuary Favorites', 'XBMC.RunPlugin(%s?mode=12&name=%s)'
                                % (sys.argv[0], urllib.quote_plus(name))))
        if not name in FAV:
            contextMenu.append(('Add to Sanctuary Favorites',
                                'XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                                % (sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url),
                                   urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
        liz.addContextMenuItems(contextMenu)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def Play(name, url, mode, iconimage, fanart, description, extra, showcontext=True, allinfo={}):
    if iconimage == '':
        iconimage = ICON
    if fanart == '':
        fanart = FANART
    if not 'http' in url:
        PLAY(name, url, mode, iconimage, fanart, description, extra)
    elif 'watchseries' in url:
        PLAY(name, url, mode, iconimage, fanart, description, extra)
    elif 'm3u' in url:
        PLAY(name, url, mode, iconimage, fanart, description, extra)
    else:
        from pyramid import pyramid
        pyramid.addLink(url, name, iconimage, fanart, description, '', '', True, '', '', 1, '')


def PLAY(name, url, mode, iconimage, fanart, description, extra, showcontext=True, allinfo={}):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&fanart=" + urllib.quote_plus(
        fanart) + "&description=" + urllib.quote_plus(description)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage=" ", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    liz.setProperty("Fanart_Image", fanart)
    if showcontext:
        contextMenu = []
        if showcontext == 'fav':
            contextMenu.append(('Remove from Sanctuary Favorites', 'XBMC.RunPlugin(%s?mode=12&name=%s)'
                                % (sys.argv[0], urllib.quote_plus(name))))
        if not name in FAV:
            contextMenu.append(('Add to Sanctuary Favorites',
                                'XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                                % (sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url),
                                   urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
        contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=1)' % sys.argv[0]))
        liz.addContextMenuItems(contextMenu)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)
    return ok
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def queueItem():
    return xbmc.executebuiltin('Action(Queue)')

# =======================================Credit to Spoyser for this, was in funnier moments and using to implement playlists, will rewrite when i better understand it ======

def Random_play(name, mode, url='', image=None, isFolder=True, page=1, keyword=None, infoLabels=None, contextMenu=None):
    if not image:
        image = ICON
    u  = sys.argv[0] 
    u += '?mode='  + str(mode)
    u += '&title=' + urllib.quote_plus(name)
    u += '&image=' + urllib.quote_plus(image)
    u += '&page='  + str(page)
    if url != '':     
        u += '&url='   + urllib.quote_plus(url) 
    if keyword:
        u += '&keyword=' + urllib.quote_plus(keyword) 
    liz = xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
    if contextMenu:
        liz.addContextMenuItems(contextMenu)
    if infoLabels:
        liz.setInfo(type="Video", infoLabels=infoLabels)
    if not isFolder:
        liz.setProperty("IsPlayable","true")
    liz.setProperty('Fanart_Image', FANART)     
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)


# ===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------

def addon_log(string):
    if debug == 'true':
        xbmc.log("[addon.live.Sanctuary-%s]: %s" % (addon_version, string))


def addFavorite(name, url, iconimage, fanart, mode, playlist=None, regexs=None):
    favList = []
    try:
        # seems that after
        name = name.encode('utf-8', 'ignore')
    except:
        pass
    if os.path.exists(favourites) == False:
        addon_log('Making Favorites File')
        favList.append((name, url, iconimage, fanart, mode, playlist, regexs))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        addon_log('Appending Favorites')
        a = open(favourites).read()
        data = json.loads(a)
        data.append((name, url, iconimage, fanart, mode))
        b = open(favourites, "w")
        b.write(json.dumps(data))
        b.close()


def getFavourites():
    if os.path.exists(favourites) == False:
        favList = []
        addon_log('Making Favorites File')
        favList.append(('Sanctuary Favourites Section', '', '', '', '', '', ''))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        items = json.loads(open(favourites).read())
        total = len(items)
        for i in items:
            name = i[0]
            url = i[1]
            iconimage = i[2]
            try:
                fanart = i[3]
            except:
                fanart = ''
            try:
                playlist = i[5]
            except:
                playlist = None
            try:
                regexs = i[6]
            except:
                regexs = None

            if i[4] == 906:
                Play(name, url, '', iconimage, fanart, '', '', 'fav')
            else:
                Menu(name, url, i[4], iconimage, fanart, '', '', 'fav')


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

def Straight_Resolve(name,url):
	xbmc.Player().play(url, xbmcgui.ListItem(name))

def Resolve(url):
    Big_Resolve('',url)


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


def resolve_playercore(url):
	Big_Resolve('',url)

def Big_Resolve(name,url):
	import urlresolver
	try:
		resolved_url = urlresolver.resolve(url)
		xbmc.Player().play(resolved_url, xbmcgui.ListItem(name))
	except:
		xbmc.Player().play(url, xbmcgui.ListItem(name))
	xbmcplugin.endOfDirectory(int(sys.argv[1]))


