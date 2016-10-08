'''
These addons are only possible because websites are open and allow us to view them for free.

These addons are also only possible due to the numerous hours the kodi developers and addon developers put in to ensure that
you, the user can have as much content as you need.

However, it is incredibly clear that numerous cunts exist in the community and like nothing than to rip of the code of us,
the hard working developers. You are known, we are watching.

This section was kindly donated by the dev of the addon - oneil, give him a follow on twitter to say thanks for this amazing section - @oneilxm_uk'''



import sys, os, xbmc, xbmcgui, xbmcplugin, xbmcaddon, urllib, urllib2, cookielib, re

settings = xbmcaddon.Addon(id='plugin.video.sanctuary')
cookiejar = cookielib.LWPCookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(cookie_handler)
addon_id = 'plugin.video.sanctuary'
selfAddon = xbmcaddon.Addon(id=addon_id)
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

def CATEGORIES():
    link = openURL('http://www.perfectgirls.net/')
    match = re.compile('<a href="/category/([0-9][0-9])/(.*)">(.*)</a>').findall(link)
    addDir('[COLOR red]Latest[/COLOR]', 'http://www.perfectgirls.net/', 1401, icon, 1)
    addDir('---', '', 1401, '', 1)
    for page_id, channame, name in match:
        addDir(name,
               ('http://www.perfectgirls.net/category/' + page_id + '/' + channame),
               1401, icon, 1)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def VIDEOLIST(url):
    link = openURL(url)
    match = re.compile('-->\n<a href="/([0-9]+)/(.*)" title="(.*)">').findall(link)
    for v_id, videourl, name, in match:
        addLink(name,'http://www.perfectgirls.net/' + v_id + '/' + videourl,1402,icon)


def PLAYVIDEO(url):
    link = openURL(url)
    match = re.compile('get\("(.*)", function').findall(link)
    for configurl in match:
        link = openURL('http://www.perfectgirls.net/' + configurl)
        match2 = re.compile('http://(.*)').findall(link)
        match3 = ['http://' + str(match2[0])]
        if match2:
            xbmc.Player().play(match3[-1])


def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params)-1] == '/'):
            params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param


def addLink(name, url, mode, iconimage):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode)\
        + "&name=" + urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="icon.png",
                           thumbnailImage=iconimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u,
                                     listitem=liz, isFolder=False)
    return ok


def addDir(name, url, mode, iconimage, page):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) +\
        "&name=" + urllib.quote_plus(name) + "&page=" + str(page)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="icon.png",
                           thumbnailImage=iconimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u,
                                     listitem=liz, isFolder=True)
    return ok


def openURL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    return link


params = get_params()
url = None
name = None
mode = None
page = 1

try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass
try:
    page = int(params["page"])
except:
    pass

if mode == 1400:
    CATEGORIES()

elif mode == 1401:
    VIDEOLIST(url)

elif mode == 1402:
    PLAYVIDEO(url)
