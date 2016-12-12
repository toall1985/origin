# -*- coding: utf-8 -*-
'''The code on this section was taken from the original addons great work by whoever coded this masterpiece
This section was kindly donated by the dev of the Pyramid,tigens world,maverick,oblivion,supremacy addons, give them a follow on twitter or fb to say thanks 
for these amazing sections all issues with errors in this addon Sanctuary should be reported to @Origin_Ent but streams not working taken to original 
author/playlister'''


import urllib
import urllib2
import datetime
import re
import os
import base64
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
import xbmc, sys, base64
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
try:
    import json
except:
    import simplejson as json
import SimpleDownloader as downloader
import time
import requests
addon_id = 'plugin.video.sanctuary'
ADDON = xbmcaddon.Addon(id=addon_id)
Adult_Pass = ADDON.getSetting('Adult')

resolve_url=['180upload.com', 'allmyvideos.net','gorillavid.in', 'bestreams.net', 'clicknupload.com', 'cloudzilla.to', 'movshare.net', 'novamov.com', 'nowvideo.sx', 'videoweed.es', 'daclips.in', 'datemule.com', 'fastvideo.in', 'faststream.in', 'filehoot.com', 'filenuke.com', 'sharesix.com', 'docs.google.com', 'plus.google.com', 'picasaweb.google.com', 'gorillavid.com', 'gorillavid.in', 'grifthost.com', 'hugefiles.net', 'ipithos.to', 'ishared.eu', 'kingfiles.net', 'mail.ru', 'my.mail.ru', 'videoapi.my.mail.ru', 'mightyupload.com', 'mooshare.biz', 'movdivx.com', 'movpod.net', 'movpod.in', 'movreel.com', 'mrfile.me', 'uptostream.com', 'nosvideo.com', 'openload.co', 'played.to', 'bitshare.com', 'filefactory.com', 'k2s.cc', 'oboom.com', 'rapidgator.net', 'uploaded.net', 'primeshare.tv', 'bitshare.com', 'filefactory.com', 'k2s.cc', 'oboom.com', 'rapidgator.net', 'uploaded.net', 'sharerepo.com', 'stagevu.com', 'streamcloud.eu', 'streamin.to', 'thefile.me', 'thevideo.me', 'tusfiles.net', 'uploadc.com', 'zalaa.com', 'uploadrocket.net', 'uptobox.com', 'v-vids.com', 'veehd.com', 'vidbull.com', 'videomega.tv', 'vidplay.net', 'vidspot.net', 'vidto.me', 'vidzi.tv', 'vimeo.com', 'vk.com', 'vodlocker.com', 'xfileload.com', 'xvidstage.com', 'zettahost.tv']
g_ignoreSetResolved=['plugin.video.dramasonline','plugin.video.f4mTester','plugin.video.shahidmbcnet','plugin.video.SportsDevil','plugin.stream.vaughnlive.tv','plugin.video.ZemTV-shani']

class NoRedirection(urllib2.HTTPErrorProcessor):
   def http_response(self, request, response):
       return response
   https_response = http_response
       
addon = xbmcaddon.Addon('plugin.video.sanctuary')
addon_version = addon.getAddonInfo('version')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/Sanctuary/'
favorites = ADDON_DATA + 'favourites'
history = os.path.join(profile, 'history')

REV = os.path.join(profile, 'list_revision')
icon = os.path.join(home, 'icon.png')
FANART = os.path.join(home, 'fanart.jpg')
source_file = os.path.join(profile, 'source_file')
functions_dir = profile

downloader = downloader.SimpleDownloader()
debug = addon.getSetting('debug')
if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
else: FAV = []
if os.path.exists(source_file)==True:
    SOURCES = open(source_file).read()
else: SOURCES = []

def addon_log(string):
    if debug == 'true':
        pass


def makeRequest(url, headers=None):
        try:
            if headers is None:
                headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
            req = urllib2.Request(url,None,headers)
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
            return data
        except urllib2.URLError, e:
            addon_log('URL: '+url)
            if hasattr(e, 'code'):
                addon_log('We failed with error code - %s.' % e.code)
                xbmc.executebuiltin("XBMC.Notification(Sanctuary ,We failed with error code - "+str(e.code)+",10000,"+icon+")")
            elif hasattr(e, 'reason'):
                addon_log('We failed to reach a server.')
                addon_log('Reason: %s' %e.reason)
                xbmc.executebuiltin("XBMC.Notification(Sanctuary ,We failed to reach a server. - "+str(e.reason)+",10000,"+icon+")")

				
def SKindex():
    addon_log("SKindex")
    addDir('[B][COLOR gold]THE PYRAMID SEARCH[/B][/COLOR]','http://tombraiderbuilds.co.uk/addon/mainmovies/mainmovies.txt',1141,'http://previews.123rf.com/images/markinv/markinv1212/markinv121200020/17010740-All-seeing-eye-Stock-Vector-horus-eye-egyptian.jpg' ,  FANART,'','','','')
    getData('http://tombraiderbuilds.co.uk/addon/home.txt','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SKindex_Joker():
    addDir('[B][COLOR lime]Maverick Movie Search[/B][/COLOR]','http://jokerswizard.esy.es/joker/data/quality/quality.txt',1141,'http://previews.123rf.com/images/markinv/markinv1212/markinv121200020/17010740-All-seeing-eye-Stock-Vector-horus-eye-egyptian.jpg' ,  FANART,'','','','')
    getData('http://164.132.106.213/data/home/home.txt','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SKindex_Oblivion():
    getData(base64.decodestring('aHR0cDovL29ibGl2aW9uYnVpbGRzLmNvbS9GcmVlLnhtbA=='),'')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SKindex_TigensWorld():
    addDir('Search Tigens World Movies','MULTILINK-TIGEN',1141,'http://herovision.x10host.com/freeview/Tigen.png' ,  FANART,'','','','')
    getData('http://www.kodeeresurrection.com/TigensWorldtxt/home.txt','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
def SKindex_Supremacy():
    getData('https://simplekore.com/wp-content/uploads/file-manager/steboy11/home.txt','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SKindex_BAMF():
    getData('http://genietvcunts.co.uk/bamffff/BAMF.xml','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SKindex_Quicksilver():
    getData('http://quicksilver-music.com/addoncore/Texts/home.txt','')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SKindex_Silent():
    getData(base64.decodestring('aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvL2pkaC9ob21lLnR4dA=='),'')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SKindex_Ultra():
    getData(base64.decodestring('aHR0cDovL3VsdHJhdHYubmV0MTYubmV0L2lwdHZzZXJ2ZXIvcG9ydGFsLnhtbA=='),'')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def SKindex_Fido():
    getData(base64.decodestring('aHR0cHM6Ly9nb28uZ2wvOEtRSWQ4'),'')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
def Search_input(url):
    Dialog = xbmcgui.Dialog()
    Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search_title.lower()
    if Search_name == '':
        pass
    else:
        Search_loop(Search_name,url)    
	
def Search_loop(Search_name,url):
    if 'MULTILINK' in url:
        if 'TIGEN' in url:
            TigenList = ['http://kodeeresurrection.com/TigensWorldtxt/Movies/Txts/TigensMoviesSub.txt','http://kodeeresurrection.com/LILYSPORTStxts/MovieRack/txts/NUMBER%20TITLES.txt',
	        'http://kodeeresurrection.com/LILYSPORTStxts/MovieRack/txts/A-F.txt','http://kodeeresurrection.com/LILYSPORTStxts/MovieRack/txts/G-L.txt','http://kodeeresurrection.com/LILYSPORTStxts/MovieRack/txts/M-R.txt',
	        'http://kodeeresurrection.com/LILYSPORTStxts/MovieRack/txts/S-Z.txt','http://kodeeresurrection.com/LILYSPORTStxts/boxsetssub.txt']
            List = TigenList
        for item in List:
            if 'boxset' in item:
                HTML = Open_Url(item)
                match = re.compile('<name>(.+?)</name>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>.+?<fanart>(.+?)</fanart>',re.DOTALL).findall(HTML)
                for name,image,url,fanart in match:
                    if (Search_name).replace(' ','').lower() in (name).replace(' ','').lower():
                        addDir(name,url,1101,image,fanart,'','','','')
            else:
				HTML = Open_Url(item)
				if HTML != 'Failed':
					match = re.compile('<channel>.+?<name>(.+?)</name>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>.+?<fanart>(.+?)</fanart>.+?</channel>',re.DOTALL).findall(HTML)
					for name,image,url,fanart in match:
						if 'http:' in url:
							Search_loop(Search_name,url)
					match2 = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>',re.DOTALL).findall(HTML)
					for name,url,image,fanart in match2:
						if 'http:' in url:
							if (Search_name).replace(' ','').lower() in (name).replace(' ','').lower():
								addLink(url, name,image,fanart,'','','','',None,'',1)	

    else:			
		HTML = Open_Url(url)
		if HTML != 'Failed':
			match = re.compile('<channel>.+?<name>(.+?)</name>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>.+?<fanart>(.+?)</fanart>.+?</channel>',re.DOTALL).findall(HTML)
			for name,image,url,fanart in match:
				if not 'http:' in url:
					pass
				else:
					Search_loop(Search_name,url)
			match2 = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>',re.DOTALL).findall(HTML)
			for name,url,image,fanart in match2:
				if 'http:' in url:
					if (Search_name).replace(' ','').lower() in (name).replace(' ','').lower():
						addLink(url,name,image,fanart,'','','','',None,'',1)	
	
def Open_Url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = ''
    link = ''
    try: 
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    except: pass
    if link != '':
        return link
    else:
        link = 'Opened'
        return link
	
				

	
def getSources():
        if os.path.exists(favorites) == True:
            addDir('Favorites','url',1104,os.path.join(home, 'resources', 'favorite.png'),FANART,'','','','')
        if addon.getSetting("browse_xml_database") == "true":
            addDir('XML Database','http://xbmcplus.xb.funpic.de/www-data/filesystem/',1115,icon,FANART,'','','','')
        if addon.getSetting("browse_community") == "true":
            addDir('Community Files','community_files',1116,icon,FANART,'','','','')
        if os.path.exists(history) == True:
            addDir('Search History','history',1125,os.path.join(home, 'resources', 'favorite.png'),FANART,'','','','')
        if addon.getSetting("searchyt") == "true":
            addDir('Search:Youtube','youtube',1125,icon,FANART,'','','','')
        if addon.getSetting("searchDM") == "true":
            addDir('Search:dailymotion','dmotion',1125,icon,FANART,'','','','')
        if addon.getSetting("PulsarM") == "true":
            addDir('Pulsar:IMDB','IMDBidplay',1127,icon,FANART,'','','','')            
        if os.path.exists(source_file)==True:
            sources = json.loads(open(source_file,"r").read())
            #print 'sources',sources
            if len(sources) > 1:
                for i in sources:
                    ## for pre 1.0.8 sources
                    if isinstance(i, list):
                        addDir(i[0].encode('utf-8'),i[1].encode('utf-8'),1101,icon,FANART,'','','','','source')
                    else:
                        thumb = icon
                        fanart = FANART
                        desc = ''
                        date = ''
                        credits = ''
                        genre = ''
                        if i.has_key('thumbnail'):
                            thumb = i['thumbnail']
                        if i.has_key('fanart'):
                            fanart = i['fanart']
                        if i.has_key('description'):
                            desc = i['description']
                        if i.has_key('date'):
                            date = i['date']
                        if i.has_key('genre'):
                            genre = i['genre']
                        if i.has_key('credits'):
                            credits = i['credits']
                        addDir(i['title'].encode('utf-8'),i['url'].encode('utf-8'),1101,thumb,fanart,desc,genre,date,credits,'source')

            else:
                if len(sources) == 1:
                    if isinstance(sources[0], list):
                        getData(sources[0][1].encode('utf-8'),FANART)
                    else:
                        getData(sources[0]['url'], sources[0]['fanart'])

def re_me(data, re_patten):
    match = ''
    m = re.search(re_patten, data)
    if m != None:
        match = m.group(1)
    else:
        match = ''
    return match

def addSource(url=None):
        if url is None:
            if not addon.getSetting("new_file_source") == "":
               source_url = addon.getSetting('new_file_source').decode('utf-8')
            elif not addon.getSetting("new_url_source") == "":
               source_url = addon.getSetting('new_url_source').decode('utf-8')
        else:
            source_url = url
        if source_url == '' or source_url is None:
            return
        addon_log('Adding New Source: '+source_url.encode('utf-8'))

        media_info = None
        #print 'source_url',source_url
        data = getSoup(source_url)
        print 'source_url',source_url
        if isinstance(data,BeautifulSOAP):
            if data.find('channels_info'):
                media_info = data.channels_info
            elif data.find('items_info'):
                media_info = data.items_info
        if media_info:
            source_media = {}
            source_media['url'] = source_url
            try: source_media['title'] = media_info.title.string
            except: pass
            try: source_media['thumbnail'] = media_info.thumbnail.string
            except: pass
            try: source_media['fanart'] = media_info.fanart.string
            except: pass
            try: source_media['genre'] = media_info.genre.string
            except: pass
            try: source_media['description'] = media_info.description.string
            except: pass
            try: source_media['date'] = media_info.date.string
            except: pass
            try: source_media['credits'] = media_info.credits.string
            except: pass
        else:
            if '/' in source_url:
                nameStr = source_url.split('/')[-1].split('.')[0]
            if '\\' in source_url:
                nameStr = source_url.split('\\')[-1].split('.')[0]
            if '%' in nameStr:
                nameStr = urllib.unquote_plus(nameStr)
            keyboard = xbmc.Keyboard(nameStr,'Displayed Name, Rename?')
            keyboard.doModal()
            if (keyboard.isConfirmed() == False):
                return
            newStr = keyboard.getText()
            if len(newStr) == 0:
                return
            source_media = {}
            source_media['title'] = newStr
            source_media['url'] = source_url
            source_media['fanart'] = fanart

        if os.path.exists(source_file)==False:
            source_list = []
            source_list.append(source_media)
            b = open(source_file,"w")
            b.write(json.dumps(source_list))
            b.close()
        else:
            sources = json.loads(open(source_file,"r").read())
            sources.append(source_media)
            b = open(source_file,"w")
            b.write(json.dumps(sources))
            b.close()
        addon.setSetting('new_url_source', "")
        addon.setSetting('new_file_source', "")
        xbmc.executebuiltin("XBMC.Notification(ThePyramid,New source added.,5000,"+icon+")")
        if not url is None:
            if 'xbmcplus.xb.funpic.de' in url:
                xbmc.executebuiltin("XBMC.Container.Update(%s?mode=1114,replace)" %sys.argv[0])
            elif 'community-links' in url:
                xbmc.executebuiltin("XBMC.Container.Update(%s?mode=1110,replace)" %sys.argv[0])
        else: addon.openSettings()


def rmSource(name):
        sources = json.loads(open(source_file,"r").read())
        for index in range(len(sources)):
            if isinstance(sources[index], list):
                if sources[index][0] == name:
                    del sources[index]
                    b = open(source_file,"w")
                    b.write(json.dumps(sources))
                    b.close()
                    break
            else:
                if sources[index]['title'] == name:
                    del sources[index]
                    b = open(source_file,"w")
                    b.write(json.dumps(sources))
                    b.close()
                    break
        xbmc.executebuiltin("XBMC.Container.Refresh")



def get_xml_database(url, browse=False):
        if url is None:
            url = 'http://xbmcplus.xb.funpic.de/www-data/filesystem/'
        soup = BeautifulSoup(makeRequest(url), convertEntities=BeautifulSoup.HTML_ENTITIES)
        for i in soup('a'):
            href = i['href']
            if not href.startswith('?'):
                name = i.string
                if name not in ['Parent Directory', 'recycle_bin/']:
                    if href.endswith('/'):
                        if browse:
                            addDir(name,url+href,1115,icon,fanart,'','','')
                        else:
                            addDir(name,url+href,1114,icon,fanart,'','','')
                    elif href.endswith('.xml'):
                        if browse:
                            addDir(name,url+href,1101,icon,fanart,'','','','','download')
                        else:
                            if os.path.exists(source_file)==True:
                                if name in SOURCES:
                                    addDir(name+' (in use)',url+href,1111,icon,fanart,'','','','','download')
                                else:
                                    addDir(name,url+href,1111,icon,fanart,'','','','','download')
                            else:
                                addDir(name,url+href,1111,icon,fanart,'','','','','download')


def getCommunitySources(browse=False):
        url = 'http://community-links.googlecode.com/svn/trunk/'
        soup = BeautifulSoup(makeRequest(url), convertEntities=BeautifulSoup.HTML_ENTITIES)
        files = soup('ul')[0]('li')[1:]
        for i in files:
            name = i('a')[0]['href']
            if browse:
                addDir(name,url+name,1101,icon,fanart,'','','','','download')
            else:
                addDir(name,url+name,1111,icon,fanart,'','','','','download')


def getSoup(url,data=None):
        print 'getsoup',url,data
        if url.startswith('http://') or url.startswith('https://'):
            data = makeRequest(url)
            if re.search("#EXTM3U",data) or 'm3u' in url: 
                print 'found m3u data',data
                return data
                
        elif data == None:
            if xbmcvfs.exists(url):
                if url.startswith("smb://") or url.startswith("nfs://"):
                    copy = xbmcvfs.copy(url, os.path.join(profile, 'temp', 'sorce_temp.txt'))
                    if copy:
                        data = open(os.path.join(profile, 'temp', 'sorce_temp.txt'), "r").read()
                        xbmcvfs.delete(os.path.join(profile, 'temp', 'sorce_temp.txt'))
                    else:
                        addon_log("failed to copy from smb:")
                else:
                    data = open(url, 'r').read()
                    if re.match("#EXTM3U",data)or 'm3u' in url: 
                        print 'found m3u data',data
                        return data
            else:
                addon_log("Soup Data not found!")
                return
        return BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)


def getData(url,fanart):
    SetViewLayout = "List"
     
    soup = getSoup(url)
    if isinstance(soup,BeautifulSOAP):
        if len(soup('layoutype')) > 0:
            SetViewLayout = "Thumbnail"		    

        if len(soup('channels')) > 0:
            channels = soup('channel')
            for channel in channels:
                linkedUrl=''
                lcount=0
                try:
                    linkedUrl =  channel('externallink')[0].string
                    lcount=len(channel('externallink'))
                except: pass
                if lcount>1: linkedUrl=''

                name = channel('name')[0].string
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    thumbnail = ''

                try:
                    if not channel('fanart'):
                        if addon.getSetting('use_thumb') == "true":
                            fanArt = thumbnail
                        else:
                            fanArt = fanart
                    else:
                        fanArt = channel('fanart')[0].string
                    if fanArt == None:
                        raise
                except:
                    fanArt = fanart

                try:
                    desc = channel('info')[0].string
                    if desc == None:
                        raise
                except:
                    desc = ''

                try:
                    genre = channel('genre')[0].string
                    if genre == None:
                        raise
                except:
                    genre = ''

                try:
                    date = channel('date')[0].string
                    if date == None:
                        raise
                except:
                    date = ''

                try:
                    credits = channel('credits')[0].string
                    if credits == None:
                        raise
                except:
                    credits = ''

                try:
                    if linkedUrl=='':
                        if Adult_Pass == 'forefingeroffury':
                            addDir(url,url.encode('utf-8'),1102,thumbnail,fanArt,desc,genre,date,credits,True)
                        else:
                            if 'xxx' in name.lower():
                                pass
                            elif 'adult' in name.lower():
                                pass
                            elif 'porn' in name.lower():
                                pass
                            else:
                                addDir(url,url.encode('utf-8'),1102,thumbnail,fanArt,desc,genre,date,credits,True)
                    else:
                        if Adult_Pass == 'forefingeroffury':
                            addDir(name.encode('utf-8'),linkedUrl.encode('utf-8'),1101,thumbnail,fanArt,desc,genre,date,None,'source')
                        else:
                            if 'xxx' in name.lower():
                                pass
                            elif 'adult' in name.lower():
                                pass
                            elif 'porn' in name.lower():
                                pass
                            else:
                                addDir(name.encode('utf-8'),linkedUrl.encode('utf-8'),1101,thumbnail,fanArt,desc,genre,date,None,'source')
                except:
                    addon_log('There was a problem adding directory from getData(): '+name.encode('utf-8', 'ignore'))
        else:
            getItems(soup('item'),fanart)
    else:
        parse_m3u(soup)

    if SetViewLayout == "Thumbnail":
       SetViewThumbnail()

	
	
# borrow from https://github.com/enen92/P2P-Streams-XBMC/blob/master/plugin.video.p2p-streams/resources/core/livestreams.py
# This will not go through the getItems functions ( means you must have ready to play url, no regex)
def parse_m3u(data):
    content = data.rstrip()
    match = re.compile(r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)').findall(content)
    total = len(match)
    print 'total m3u links',total
    for other,channel_name,stream_url in match:
        if '{PQ},' in stream_url:
            Decrypt_Link(other,channel_name,stream_url,total)
        else:
            if 'tvg-logo' in other:
                thumbnail = re_me(other,'tvg-logo=[\'"](.*?)[\'"]')
                if thumbnail:
                    if thumbnail.startswith('http'):
                        thumbnail = thumbnail
                
                    elif not addon.getSetting('logo-folderPath') == "":
                        logo_url = addon.getSetting('logo-folderPath')
                        thumbnail = logo_url + thumbnail

                    else:
                        thumbnail = thumbnail
            else:
                thumbnail = ''
            if 'type' in other:
                mode_type = re_me(other,'type=[\'"](.*?)[\'"]')
                if mode_type == 'yt-dl':
                    stream_url = stream_url +"&mode=1118"
                elif mode_type == 'regex':
                    url = stream_url.split('&regexs=')
                    regexs = parse_regex(getSoup('',data=url[1]))
                    addLink(url[0], channel_name,thumbnail,'','','','','',None,regexs,total)
                    continue
            addLink(stream_url, channel_name,thumbnail,'','','','','',None,'',total)
		
    xbmc.executebuiltin("Container.SetViewMode(50)")
	

def Decrypt_Link(other,channel_name,stream_url,total):
 ii = ( stream_url ) . replace ( '{IX},' , 'http' ) . replace ( '{UD},' , '.com' )
 oOOo = ( ii ) . replace ( '{LM},' , 'a' ) . replace ( '{XG},' , 'b' ) . replace ( '{JP},' , 'c' ) . replace ( '{WE},' , 'd' ) . replace ( '{PL},' , 'e' ) . replace ( '{JT},' , 'f' )
 O0 = ( oOOo ) . replace ( '{XX},' , 'g' ) . replace ( '{HA},' , 'h' ) . replace ( '{YT},' , 'i' ) . replace ( '{PF},' , 'j' ) . replace ( '{HW},' , 'k' ) . replace ( '{RT},' , 'l' )
 o0O = ( O0 ) . replace ( '{SF},' , 'm' ) . replace ( '{IF},' , 'n' ) . replace ( '{PW},' , 'o' ) . replace ( '{GF},' , 'p' ) . replace ( '{DD},' , 'q' ) . replace ( '{UO},' , 'r' )
 iI11I1II1I1I = ( o0O ) . replace ( '{LE},' , 's' ) . replace ( '{WP},' , 't' ) . replace ( '{ZY},' , 'u' ) . replace ( '{UE},' , 'v' ) . replace ( '{PE},' , 'w' ) . replace ( '{JE},' , 'x' )
 if 'tvg-logo' in other :
  oooo = re_me ( other , 'tvg-logo=[\'"](.*?)[\'"]' )
  if oooo :
   if oooo . startswith ( 'http' ) :
    oooo = oooo
    if 11 - 11: ii1I - ooO0OO000o
   elif not addon . getSetting ( 'logo-folderPath' ) == "" :
    ii11i = addon . getSetting ( 'logo-folderPath' )
    oooo = ii11i + oooo
   else :
    oooo = oooo
 else :
  oooo = ''
 oOooOoO0Oo0O = ( iI11I1II1I1I ) . replace ( '{TH},' , 'y' ) . replace ( '{LK},' , 'z' ) . replace ( '{UN},' , '.' ) . replace ( '{IG},' , '(' ) . replace ( '{LO},' , ')' ) . replace ( '{LP},' , '/' )
 iI1 = ( oOooOoO0Oo0O ) . replace ( '{ZH},' , '1' ) . replace ( '{PP},' , '2' ) . replace ( '{AM},' , '3' ) . replace ( '{TA},' , '4' ) . replace ( '{DP},' , '5' ) . replace ( '{JS},' , '6' )
 i1I11i = ( iI1 ) . replace ( '{JJ},' , '7' ) . replace ( '{MM},' , '8' ) . replace ( '{FQ},' , '9' ) . replace ( '{HH},' , '0' ) . replace ( '{PQ},' , ':' ) . replace ( '{SC},' , '%' )
 OoOoOO00 = ( i1I11i ) . replace ( '{UJ},' , '-' ) . replace ( '{XD},' , '_' ) . replace ( 'HAVE_A_NICE_DAY_NOW' , 'TV' )
 if 'type' in other :
  stream_url = OoOoOO00
  I11i = re_me ( other , 'type=[\'"](.*?)[\'"]' )
  if I11i == 'yt-dl' :
   stream_url = stream_url + "&mode=1118"
  elif I11i == 'regex' :
   O0O = stream_url . split ( '&regexs=' )
   Oo = parse_regex ( getSoup ( '' , data = O0O [ 1 ] ) )
   if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI
   addLink ( O0O [ 0 ] , channel_name , oooo , '' , '' , '' , '' , '' , None , Oo , total )
 stream_url = OoOoOO00
 addLink ( stream_url , channel_name , oooo , '' , '' , '' , '' , '' , None , '' , total ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
	
def getChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('channel', attrs={'name' : name.decode('utf-8')})
        items = channel_list('item')
        try:
            fanArt = channel_list('fanart')[0].string
            if fanArt == None:
                raise
        except:
            fanArt = fanart
        for channel in channel_list('subchannel'):
            name = channel('name')[0].string
            try:
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''
            try:
                if not channel('fanart'):
                    if addon.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                else:
                    fanArt = channel('fanart')[0].string
                if fanArt == None:
                    raise
            except:
                pass
            try:
                desc = channel('info')[0].string
                if desc == None:
                    raise
            except:
                desc = ''

            try:
                genre = channel('genre')[0].string
                if genre == None:
                    raise
            except:
                genre = ''

            try:
                date = channel('date')[0].string
                if date == None:
                    raise
            except:
                date = ''

            try:
                credits = channel('credits')[0].string
                if credits == None:
                    raise
            except:
                credits = ''

            try:
				if Adult_Pass == 'forefingeroffury':
					addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),1103,thumbnail,fanArt,desc,genre,credits,date)
				else:
					if 'xxx' in name.lower():
					    pass
					elif 'adult' in name.lower():
					    pass
					elif 'porn' in name.lower():
					    pass
					else:
					    addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),1103,thumbnail,fanArt,desc,genre,credits,date)
            except:
                addon_log('There was a problem adding directory - '+name.encode('utf-8', 'ignore'))
        getItems(items,fanArt)


def getSubChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('subchannel', attrs={'name' : name.decode('utf-8')})
        items = channel_list('subitem')
        getItems(items,fanart)

#hakamac
def GetSublinks(name,url,iconimage,fanart):
    List=[]; ListU=[]; c=0
    all_videos = regex_get_all(url, 'sublink:', '#')
    for a in all_videos:
        if 'LISTSOURCE:' in a:
            vurl = regex_from_to(a, 'LISTSOURCE:', '::')
            linename = regex_from_to(a, 'LISTNAME:', '::')
        else:
            vurl = a.replace('sublink:','').replace('#','')
            linename = name
        if len(vurl) > 10:
            c=c+1; List.append(linename); ListU.append(vurl)
 
    if c==1:
        try:
            #print 'play 1   Name:' + name + '   url:' + ListU[0] + '     ' + str(c)
            liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=ListU[0],listitem=liz)
            xbmc.Player().play(urlsolver(ListU[0]), liz)
        except:
            pass
    else:
         dialog=xbmcgui.Dialog()
         rNo=dialog.select('Select A Source', List)
         if rNo>=0:
             rName=name
             rURL=str(ListU[rNo])
             #print 'Sublinks   Name:' + name + '   url:' + rURL
             try:
                 xbmc.Player().play(urlsolver(rURL), xbmcgui.ListItem(rName))
             except:
                 xbmc.Player().play(rURL, xbmcgui.ListItem(rName))
	
def Search_m3u(data,Searchkey):
    content = data.rstrip()
    match = re.compile(r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)').findall(content)
    total = len(match)
    print 'total m3u links',total
    for other,channel_name,stream_url in match:
        if 'tvg-logo' in other:
            thumbnail = re_me(other,'tvg-logo=[\'"](.*?)[\'"]')
            if thumbnail:
                if thumbnail.startswith('http'):
                    thumbnail = thumbnail
                
                elif not addon.getSetting('logo-folderPath') == "":
                    logo_url = addon.getSetting('logo-folderPath')
                    thumbnail = logo_url + thumbnail

                else:
                    thumbnail = thumbnail
            #else:
            
        else:
            thumbnail = ''
        if 'type' in other:
            mode_type = re_me(other,'type=[\'"](.*?)[\'"]')
            if mode_type == 'yt-dl':
                stream_url = stream_url +"&mode=1118"
            elif mode_type == 'regex':
                url = stream_url.split('&regexs=')
                #print url[0] getSoup(url,data=None)
                regexs = parse_regex(getSoup('',data=url[1]))
                
                addLink(url[0], channel_name,thumbnail,'','','','','',None,regexs,total)
                continue
        addLink(stream_url, channel_name,thumbnail,'','','','','',None,'',total)

	
def regex_get_all(text, start_with, end_with):
    r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
    return r				

def regex_from_to(text, from_string, to_string, excluding=True):
    if excluding:
	   try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
	   except: r = ''
    else:
       try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
       except: r = ''
    return r

def getItems(items,fanart):
        total = len(items)
        addon_log('Total Items: %s' %total)
        for item in items:
            isXMLSource=False
            isJsonrpc = False
            try:
                name = item('title')[0].string
                if name is None:
                    name = 'unknown?'
            except:
                addon_log('Name Error')
                name = ''


            try:
                if item('epg'):
                    if item.epg_url:
                        addon_log('Get EPG Regex')
                        epg_url = item.epg_url.string
                        epg_regex = item.epg_regex.string
                        epg_name = get_epg(epg_url, epg_regex)
                        if epg_name:
                            name += ' - ' + epg_name
                    elif item('epg')[0].string > 1:
                        name += getepg(item('epg')[0].string)
                else:
                    pass
            except:
                addon_log('EPG Error')
            try:
                url = []
                if len(item('link')) >0:
#                    print 'item link', item('link')
                    for i in item('link'):
                        if not i.string == None:
                            url.append(i.string)
                    
                elif len(item('sportsdevil')) >0:
                    for i in item('sportsdevil'):
                        if not i.string == None:
                            sportsdevil = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +i.string
                            referer = item('referer')[0].string
                            if referer:
                                sportsdevil = sportsdevil + '%26referer=' +referer
                            url.append(sportsdevil)
                elif len(item('p2p')) >0:
                    for i in item('p2p'):
                        if not i.string == None:
                            if 'sop://' in i:
                                sop = 'plugin://plugin.video.p2p-streams/?url='+i.string +'&amp;mode=2&amp;' + 'name='+name 
                                url.append(sop) 
                            else:
                                p2p='plugin://plugin.video.p2p-streams/?url='+i.string +'&amp;mode=1&amp;' + 'name='+name 
                                url.append(p2p)
                elif len(item('vaughn')) >0:
                    for i in item('vaughn'):
                        if not i.string == None:
                            vaughn = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel='+i.string
                            url.append(vaughn)
                elif len(item('ilive')) >0:
                    for i in item('ilive'):
                        if not i.string == None:
                            if not 'http' in i.string:
                                ilive = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/'+i.string+'&amp;link=99&amp;mode=iLivePlay'
                            else:
                                ilive = 'plugin://plugin.video.tbh.ilive/?url='+i.string+'&amp;link=99&amp;mode=iLivePlay'
                elif len(item('yt-dl')) >0:
                    for i in item('yt-dl'):
                        if not i.string == None:
                            ytdl = i.string + '&mode=1118'
                            url.append(ytdl)
                elif len(item('utube')) >0:
                    for i in item('utube'):
                        if not i.string == None:
                            if len(i.string) == 11:
                                utube = 'plugin://plugin.video.youtube/play/?video_id='+ i.string 
                            elif i.string.startswith('PL') and not '&order=' in i.string :
                                utube = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + i.string
                            else:
                                utube = 'plugin://plugin.video.youtube/play/?playlist_id=' + i.string 
                    url.append(utube)
                elif len(item('imdb')) >0:
                    for i in item('imdb'):
                        if not i.string == None:
                            if addon.getSetting('genesisorpulsar') == '0':
                                imdb = 'plugin://plugin.video.genesis/?action=play&imdb='+i.string
                            else:
                                imdb = 'plugin://plugin.video.pulsar/movie/tt'+i.string+'/play'
                            url.append(imdb)                      
                elif len(item('f4m')) >0:
                        for i in item('f4m'):
                            if not i.string == None:
                                if '.f4m' in i.string:
                                    f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(i.string)
                                elif '.m3u8' in i.string:
                                    f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(i.string)+'&amp;streamtype=HLS'
                                    
                                else:
                                    f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(i.string)+'&amp;streamtype=SIMPLE'
                        url.append(f4m)
                elif len(item('ftv')) >0:
                    for i in item('ftv'):
                        if not i.string == None:
                            ftv = 'plugin://plugin.video.F.T.V/?name='+urllib.quote(name) +'&url=' +i.string +'&mode=125&ch_fanart=na'
                        url.append(ftv)                        
                if len(url) < 1:
                    raise
            except:
                addon_log('Error <link> element, Passing:'+name.encode('utf-8', 'ignore'))
                continue
                
            isXMLSource=False

            try:
                isXMLSource = item('externallink')[0].string
            except: pass
            
            if isXMLSource:
                ext_url=[isXMLSource]
                isXMLSource=True
            else:
                isXMLSource=False
            try:
                isJsonrpc = item('jsonrpc')[0].string
            except: pass
            if isJsonrpc:
                ext_url=[isJsonrpc]
                isJsonrpc=True
            else:
                isJsonrpc=False            
            try:
                thumbnail = item('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''
            try:
                if not item('fanart'):
                    if addon.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                    else:
                        fanArt = fanart
                else:
                    fanArt = item('fanart')[0].string
                if fanArt == None:
                    raise
            except:
                fanArt = fanart
            try:
                desc = item('info')[0].string
                if desc == None:
                    raise
            except:
                desc = ''

            try:
                genre = item('genre')[0].string
                if genre == None:
                    raise
            except:
                genre = ''

            try:
                date = item('date')[0].string
                if date == None:
                    raise
            except:
                date = ''

            regexs = None
            if item('regex'):
                try:
                    reg_item = item('regex')
                    regexs = parse_regex(reg_item)
                except:
                    pass            
           
            try:
                if len(url) > 1:
                    
                    alt = 0
                    playlist = []
                    for i in url:
                    	if addon.getSetting('ask_playlist_items') == 'true':
	                        if regexs:
	                            playlist.append(i+'&regexs='+regexs)
	                        elif  any(x in i for x in resolve_url) and  i.startswith('http'):
	                            playlist.append(i+'&mode=1119')                            
                        else:
                            playlist.append(i)
                    if addon.getSetting('add_playlist') == "false":                    
                            for i in url:
                                alt += 1
                                print 'ADDLINK 1'
                                addLink(i,'%s) %s' %(alt, name.encode('utf-8', 'ignore')),thumbnail,fanArt,desc,genre,date,True,playlist,regexs,total)                            
                    else:
                        addLink('', name.encode('utf-8', 'ignore'),thumbnail,fanArt,desc,genre,date,True,playlist,regexs,total)
                else:
                    if isXMLSource:
                        if Adult_Pass == 'forefingeroffury':
                            addDir(name.encode('utf-8'),ext_url[0].encode('utf-8'),1101,thumbnail,FANART,desc,genre,date,None,'source')
                        else:
                            if 'xxx' in name.lower():
                                pass
                            elif 'adult' in name.lower():
                                pass
                            elif 'porn' in name.lower():
                                pass
                            else:
                                addDir(name.encode('utf-8'),ext_url[0].encode('utf-8'),1101,thumbnail,FANART,desc,genre,date,None,'source')
                    elif isJsonrpc:
                        if Adult_Pass == 'forefingeroffury':
                            addDir(name.encode('utf-8'),ext_url[0],1153,thumbnail,fanart,desc,genre,date,None,'source')
                        else:
                            if 'xxx' in name.lower():
                                pass
                            elif 'adult' in name.lower():
                                pass
                            elif 'porn' in name.lower():
                                pass
                            else:
                                addDir(name.encode('utf-8'),ext_url[0],1153,thumbnail,fanart,desc,genre,date,None,'source')
                    elif url[0].find('sublink') > 0:
                        if Adult_Pass == 'forefingeroffury':
                            addDir(name.encode('utf-8'),url[0],1130,thumbnail,fanart,'','','','')
                        else:
                            if 'xxx' in name.lower():
                                pass
                            elif 'adult' in name.lower():
                                pass
                            elif 'porn' in name.lower():
                                pass
                            else:
                                addDir(name.encode('utf-8'),url[0],1130,thumbnail,fanart,'','','','')
                        #addDir(name.encode('utf-8'),url[0],1130,thumbnail,fanart,desc,genre,date,'sublink')
                    else: 
                        if not total:
                            total = 1
                        if not regexs:
                            regexs = ''
                        addLink(url[0],name.encode('utf-8', 'ignore'),thumbnail,FANART,desc,genre,date,True,None,regexs,total)

                    #print 'success'
            except:
                addon_log('There was a problem adding item - '+name.encode('utf-8', 'ignore'))
        print 'FINISH GET ITEMS *****'      
       
def urlsolver(url):
    import urlresolver
    try:
        resolver = urlresolver.resolve(url)
    except:
        resolver = url
    return resolver
	

def addDir(name,url,mode,iconimage,fanart,description,genre,date,credits,showcontext=False):
        
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date, "credits": credits })
        liz.setProperty("Fanart_Image", fanart)
        if showcontext:
            contextMenu = []
            if showcontext == 'source':
                if name in str(SOURCES):
                    contextMenu.append(('Remove from Sources','XBMC.RunPlugin(%s?mode=1108&name=%s)' %(sys.argv[0], urllib.quote_plus(name))))
            elif showcontext == 'download':
                contextMenu.append(('Download','XBMC.RunPlugin(%s?url=%s&mode=1109&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
            elif showcontext == 'fav':
                contextMenu.append(('Remove from Sanctuary Favourites','XBMC.RunPlugin(%s?mode=1106&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
									
            if not name in FAV:
                contextMenu.append(('Add to Sanctuary Favourites','XBMC.RunPlugin(%s?mode=1105&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

        return ok

def pluginquerybyJSON(url):
    json_query = uni('{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":["thumbnail","title","year","dateadded","fanart","rating","season","episode","studio"]},"id":1}') %url

    json_folder_detail = json.loads(sendJSON(json_query))
    for i in json_folder_detail['result']['files'] :
        url = i['file']
        name = removeNonAscii(i['label'])
        thumbnail = removeNonAscii(i['thumbnail'])
        try:
            fanart = removeNonAscii(i['fanart'])
        except Exception:
            fanart = ''
        try:
            date = i['year']
        except Exception:
            date = ''
        try:
            episode = i['episode']
            season = i['season']
            if episode == -1 or season == -1:
                description = ''
            else:
                description = '[COLOR yellow] S' + str(season)+'[/COLOR][COLOR hotpink] E' + str(episode) +'[/COLOR]'
        except Exception:
            description = ''
        try:
            studio = i['studio']
            if studio:
                description += '\n Studio:[COLOR steelblue] ' + studio[0] + '[/COLOR]'
        except Exception:
            studio = ''

        if i['filetype'] == 'file':
            addLink(url,name,thumbnail,fanart,description,'',date,'',None,'',total=len(json_folder_detail['result']['files']))
            #xbmc.executebuiltin("Container.SetViewMode(500)")

        else:
            addDir(name,url,1153,thumbnail,fanart,description,'',date,'')
            #xbmc.executebuiltin("Container.SetViewMode(500)")

def uni(string, encoding = 'utf-8'):
    if isinstance(string, basestring):
        if not isinstance(string, unicode):
            string = unicode(string, encoding, 'ignore')
    return string

def sendJSON( command):
    data = ''
    try:
        data = xbmc.executeJSONRPC(uni(command))
    except UnicodeEncodeError:
        data = xbmc.executeJSONRPC(ascii(command))

    return uni(data)

def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))
	
		
def addLink(url,name,iconimage,fanart,description,genre,date,showcontext,playlist,regexs,total,setCookie=""):
        #print 'url,name',url,name
        contextMenu =[]
        ok = True
        mode = '906'
        u=sys.argv[0]+"?"
        play_list = False
        u += "url="+urllib.quote_plus(url)+"&mode="+mode
        u += "&regexs="+regexs
        u += "&setCookie="+urllib.quote_plus(setCookie)
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date })
        liz.setProperty("Fanart_Image", fanart)
        liz.setProperty('IsPlayable', 'true')
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(
                    ('Remove from Sanctuary Favourites','XBMC.RunPlugin(%s?mode=1106&name=%s)'
                     %(sys.argv[0], urllib.quote_plus(name)))
                     )
            elif not name in FAV:
                fav_params = (
                    '%s?mode=1105&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
                    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart))
                    )
                contextMenu.append(('Add to Sanctuary Favourites','XBMC.RunPlugin(%s)' %fav_params))
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=1)' % sys.argv[0]))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,totalItems=total,isFolder=False)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))