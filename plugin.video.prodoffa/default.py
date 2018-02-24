#!/usr/bin/python
# -*- coding: ascii -*-

import urllib
import xbmcgui
import xbmcplugin
import requests
import re
import xbmc
import os

ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.prodoffa/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
base_url = 'http://prodoffa.co.uk'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}

ignore_list = ['categories','contact','about us']

def Main_Menu():
	Menu('Gadgets','https://www.prodoffa.co.uk/gadgets',1,'https://static1.squarespace.com/static/5a6c885ad7bdce27c69a5ad4/5a7c9b9ce2c483b61c23e54b/5a914dc78165f549b574ae55/1519472417138/Gadgets.jpeg?format=1500w','','','')
	html = requests.get(base_url, headers = headers).content
	match_block = re.findall('<div class="Header-nav-inner">(.+?)</div>',html,re.DOTALL)
	for block in match_block:
		match = re.findall('<a href="(.+?)".+?>(.+?)</a>',str(block))
		for url, name in match:
			url = base_url+url
			if name.lower() not in ignore_list:
				if 'shop by price' in name.lower():
					image = 'https://static1.squarespace.com/static/5a6c885ad7bdce27c69a5ad4/5a7c9b9ce2c483b61c23e54b/5a8023eae2c48393c5ee1866/1518351164730/buying-online_925x.jpg?format=1500w'
				elif 'gadgets' in name.lower():
					image = 'https://static1.squarespace.com/static/5a6c885ad7bdce27c69a5ad4/5a7c9b9ce2c483b61c23e54b/5a914dc78165f549b574ae55/1519472417138/Gadgets.jpeg?format=1500w'
				elif 'special' in name.lower():
					image = 'https://static1.squarespace.com/static/5a6c885ad7bdce27c69a5ad4/5a7c9b9ce2c483b61c23e54b/5a7dab81652dea7a02567881/1519472387698/gift-package-in-hand_925x.jpg?format=1500w'
				elif 'fashion' in name.lower():
					image = 'https://static1.squarespace.com/static/5a6c885ad7bdce27c69a5ad4/5a7c9b9ce2c483b61c23e54b/5a7dab859140b784388a98b5/1519472387689/thin-black-choker-necklace_925x.jpg?format=1500w'
				elif 'arts' in name.lower():
					image = 'https://static1.squarespace.com/static/5a6c885ad7bdce27c69a5ad4/5a7c9b9ce2c483b61c23e54b/5a7dab8353450a1218cc027e/1519472387692/paint-palette-brushes_925x.jpg?format=1000w'
				elif 'household' in name.lower():
					image = 'https://static1.squarespace.com/static/5a6c885ad7bdce27c69a5ad4/5a7c9b9ce2c483b61c23e54b/5a7c9eae9140b7b11645bb43/1519472387698/hands-heart-house_925x.jpg?format=1000w'
				elif 'toys' in name.lower():
					image = 'https://static1.squarespace.com/static/5a6c885ad7bdce27c69a5ad4/5a7c9b9ce2c483b61c23e54b/5a7c9eb18165f5d59b3036d8/1519472387700/box-full-of-childrens-toys_925x.jpg?format=1500w'
				else:
					image = ''
				Menu(name,url,1,image,'','','')
				
def Second_Menu(url):
	name_list = []
	html = requests.get(url, headers = headers).content
	match = re.findall('<div class="slide" data-type="image">.+?href="(.+?)".+?img src="(.+?)"',html,re.DOTALL)
	for url, image in match:
		name = urllib.unquote(url).replace('/','').replace('shop?category=','').title()
		url = base_url+url
		Menu(name,url,2,image,'','','')
		name_list.append(name)
	match2 = re.findall('<div class="intrinsic".+?<a href="(.+?)".+?img src="(.+?)"',html,re.DOTALL)
	for url, image in match2:
		name = urllib.unquote(url).replace('/','').replace('shop?category=','').title()
		if name not in name_list:
			url = base_url+url
			name_list.append(name)
			Menu(name,url,2,image,'','','')
	match3 = re.findall('<div class="image-block-outer-wrapper.+?<a href="(.+?)".+?img src="(.+?)"',html,re.DOTALL)
	for url, image in match3:
		name = urllib.unquote(url).replace('/','').replace('shop?category=','').title()
		if name not in name_list:
			url = base_url+url
			Menu(name,url,2,image,'','','')
		
def final_menu(url):
	if 'category' in url:
		html = requests.get(url, headers = headers).content
		match = re.findall('<div class="ProductList-item.+?<a href="(.+?)".+?img data-src="(.+?)".+?<h1 class="ProductList-title">(.+?)</h1>.+?<div class="product-price">.+?<span class="sqs-money-native">(.+?)</span>',html,re.DOTALL)
		for url, image, name, price in match:
			url = base_url+url
			Play(name, url, 3, image, '', price, '', '')
	else:
		Second_Menu(url)
		
def open_browser(url):
	if xbmc.getCondVisibility('system.platform.android'):
		try: xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","","'+url+'")')
		except: pass
	elif xbmc.getCondVisibility('system.platform.linux'):
		try: os.system('xdg-open '+url)
		except: pass
	elif xbmc.getCondVisibility('system.platform.windows'):
		try: os.system('start '+url)
		except: pass
	elif xbmc.getCondVisibility('system.platform.osx'):
		try: os.system('open '+url)
		except: pass
	elif xbmc.getCondVisibility('system.platform.ios'):
		try: os.system('open '+url)
		except: pass
	else:
		xbmc.log(str(url),xbmc.LOGNOTICE)

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
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
def Play(name, url, mode, iconimage, fanart, description, extra, showcontext=True, allinfo={}):
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
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)
    return ok
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
description=None
extra=None
fanart=None
fav_mode=None
regexs=None
playlist=None

try:
    regexs=params["regexs"]
except:
    pass

try:
    fav_mode=int(params["fav_mode"])
except:
    pass
try:
    extra=urllib.unquote_plus(params["extra"])
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
try:
    playitem=urllib.unquote_plus(params["playitem"])
except:
    pass
try:
    playlist=eval(urllib.unquote_plus(params["playlist"]).replace('||',','))
except:
    pass
try:
    regexs=params["regexs"]
except:
    pass

if mode == None: Main_Menu()
elif mode == 1: Second_Menu(url)
elif mode == 2: final_menu(url)
elif mode == 3: open_browser(url)
	
xbmcplugin.endOfDirectory(int(sys.argv[1]))
