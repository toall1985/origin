import os
import re
import sys
import xbmc
import xbmcgui
import xbmcplugin
playlist = ['.mp4','.mkv','.m3u8','=m22','=m18','=m37']

def originresolver(name,url):
	try:
		xbmc.log('STARTING O RESOLVER:'+url,xbmc.LOGNOTICE)
		xbmcgui.Dialog().notification("Origin Resolvers", "Starting Resolvers")
		if not url.startswith('http'):
			url = 'http:'+url
		if '.mp4' in url or '.mkv' in url or 'm3u8' in url or '=m22' in url or '=m18' in url or '=m37' in url:
			if 'openload' in url:
				resolve(name,url)
			elif 'embed' in url:
				resolve(name,url)
			elif '.html' in url:
				resolve(name,url)
			else:
				xbmc.Player().play(url, xbmcgui.ListItem(name))
		elif 'youtube' in url:
			try:
				url = re.findall('v=(.+?)>',str(url+'>'))[0]
			except:
				url = url
			xbmc.log('STARTING O RESOLVER YOUTUBE:'+url,xbmc.LOGNOTICE)
			from sources.resources import yt
			yt.PlayVideo(url)
		else:
			resolve(name,url)
			xbmc.log('STARTING O RESOLVER:'+url,xbmc.LOGNOTICE)
			
	except Exception as e:
		xbmc.log(repr(e),xbmc.LOGNOTICE)
		xbmcgui.Dialog().notification("Origin Resolvers", "Can\'t resolve stream link c")

def resolve(name,url):
	run = False
	Dialog = xbmcgui.Dialog()
	path = os.path.dirname(os.path.abspath(__file__))
	s = os.path.join(path,'sources')
	file_to_run = ''
	for Root,Dir,File in os.walk(s):
		for f in File:
			if str(f.replace('.py','')) in url:
				info = open(os.path.join(s,f)).read()
				domain_list = re.findall("domain.+?\[(.+?)\]",str(info))[0]
				domains = re.findall("'(.+?)'",str(domain_list))
				for domain in domains:
					xbmcgui.Dialog().notification("Origin Resolvers", str(domain))
					if domain in url:
						file_to_run = f
						run = True
	if run == True:
		directory = s
		module_name = file_to_run
		module_name = os.path.splitext(module_name)[0]
		xbmcgui.Dialog().notification("Origin Resolvers", str(module_name))
		path = list(sys.path)
		sys.path.insert(0, directory)
		try:
			sources = __import__(module_name).resolve(url)
		finally:
			sys.path[:] = path # restore
		if sources == None:
			xbmcgui.Dialog().notification("Origin Resolvers", "Can\'t resolve stream link b")
			sys.exit()
		elif len(sources)==1:
			for link in sources:
				xbmc.Player().play(link["url"], xbmcgui.ListItem(name))
		elif len(sources)==0:
			xbmcgui.Dialog().notification("Origin Resolvers", "Can\'t resolve stream link a")
			sys.exit()
		else:
			choice = Dialog.select('Select Playlink',[link["quality"] for link in sources])
			if choice != -1:
				playlink = sources[choice]['url']
				isFolder=False
				xbmc.Player().play(playlink, xbmcgui.ListItem(name))
	else:
		xbmcgui.Dialog().notification("Origin Resolvers", "Can\'t resolve stream link *")
	