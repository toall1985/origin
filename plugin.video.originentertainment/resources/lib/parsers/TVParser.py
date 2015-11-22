import requests, urllib, urllib2, time, re, sys, os, HTMLParser, xbmcgui, xbmc, xbmcplugin, xbmcaddon
from bs4 import BeautifulStoneSoup, BeautifulSoup
#from BeautifulSoup import BeautifulSOAP

AddonID = 'plugin.video.originentertainment'
Addon = xbmcaddon.Addon(AddonID)
localizedString = Addon.getLocalizedString

addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), AddonID)
if not os.path.exists(addon_data_dir):
	os.makedirs(addon_data_dir)
tmpListFile = os.path.join(addon_data_dir, 'tempList.txt')


def request(url, close=True, error=False, proxy=None, post=None, headers=None, mobile=False, safe=False, referer=None, cookie=None, output='', timeout='30'):
    try:
        handlers = []
        if not proxy == None:
            handlers += [urllib2.ProxyHandler({'http':'%s' % (proxy)}), urllib2.HTTPHandler]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        if output == 'cookie' or not close == True:
            import cookielib
            cookies = cookielib.LWPCookieJar()
            handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookies)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        try:
            if sys.version_info < (2, 7, 9): raise Exception()
            import ssl; ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            handlers += [urllib2.HTTPSHandler(context=ssl_context)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        except:
            pass

        try: headers.update(headers)
        except: headers = {}
        if 'User-Agent' in headers:
            pass
        elif not mobile == True:
            headers['User-Agent'] = 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
        else:
            headers['User-Agent'] = 'Apple-iPhone/701.341'
        if 'referer' in headers:
            pass
        elif referer == None:
            headers['referer'] = url
        else:
            headers['referer'] = referer
        if not 'Accept-Language' in headers:
            headers['Accept-Language'] = 'en-US'
        if 'cookie' in headers:
            pass
        elif not cookie == None:
            headers['cookie'] = cookie

        request = urllib2.Request(url, data=post, headers=headers)

        try:
            response = urllib2.urlopen(request, timeout=int(timeout))
        except urllib2.HTTPError as response:
            if error == False: return

        if output == 'cookie':
            result = []
            for c in cookies: result.append('%s=%s' % (c.name, c.value))
            result = "; ".join(result)
        elif output == 'response':
            if safe == True:
                result = (str(response), response.read(224 * 1024))
            else:
                result = (str(response), response.read())
        elif output == 'chunk':
            content = int(response.headers['Content-Length'])
            if content < (2048 * 1024): return
            result = response.read(16 * 1024)
        elif output == 'geturl':
            result = response.geturl()
        else:
            if safe == True:
                result = response.read(224 * 1024)
            else:
                result = response.read()
        if close == True:
            response.close()
        
        return result
    except:
        return

def GetEncodeString(str):
	try:
		import chardet
		str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")
	except:
		try:
			str = str.encode("utf-8")
		except:
			pass
	return str

def GetLinks(url):
    baseurl = url
    link = request(baseurl)
    soup = BeautifulSoup(link)
    GetBody = soup.find('body')
    GetUL = GetBody.find('ul')
    GetLI = GetUL.find_all('li')
    M3uData = []
    for li in GetLI:
        link = li.find_all('a')
        for Link in link:
            GetLink = re.findall(r'<a href=(.*?)>.*?</a>',str(Link))
            for url in GetLink:
                url = url.replace ('"', '')
                fullUrl = baseurl + url
                
            GetName = re.findall(r'<a href=.*?>(.*?)</a>',str(Link))
            for name in GetName:
                name = name.replace('.m3u', '')
                name = name.replace('Parent Directory', 'Origins Live TV')

            AddDir(name, fullUrl, 419, '', description="", isFolder=True, background=None)

                
                    

def m3u2list(url):
	if url.find("http") >= 0:
		response = request(url)
	else:
		response = ReadFile(url)
		
	matches=re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(str(response))
	li = []
	for params, display_name, url in matches:
		item_data = {"params": params, "display_name": display_name, "url": url}
		li.append(item_data)

	list = []
	for channel in li:
		item_data = {"display_name": channel["display_name"], "url": channel["url"]}
		matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
		for field, value in matches:
			item_data[field.strip().lower().replace('-', '_')] = value.strip()
		list.append(item_data)
	return list

def AddDir(name, url, mode, iconimage, description="", isFolder=True, background=None):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)

	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
	if background:
		liz.setProperty('fanart_image', background)
	if mode == 1 or mode == 2:
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10008).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=22)'.format(sys.argv[0], urllib.quote_plus(url)))])
	elif mode == 3:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
	elif mode == 32:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10010).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
		
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def m3uCategory(url):	
	tmpList = []
	list = m3u2list(url)

	for channel in list:
		name = GetEncodeString(channel["display_name"])
		AddDir(name ,channel["url"], 401, "", isFolder=False)
		tmpList.append({"url": channel["url"], "image": "", "name": name.decode("utf-8")})


	SaveList(tmpListFile, tmpList)

def SaveList(filname, list):
	try:
		with io.open(filname, 'w', encoding='utf-8') as handle:
			handle.write(unicode(json.dumps(list, indent=4, ensure_ascii=False)))
		success = True
	except Exception as ex:
		print ex
		success = False
		
	return success


