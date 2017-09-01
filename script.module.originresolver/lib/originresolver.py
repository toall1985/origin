import os
import re
import sys
import xbmc
import xbmcgui

def originresolver(name,url):
	try:
		if not url.startswith('http:'):
			if not url.startswith('https'):
				url = 'http:'+url
		xbmc.log('STARTING O RESOLVER:'+url,xbmc.LOGNOTICE)
		Dialog = xbmcgui.Dialog()
		path = os.path.dirname(os.path.abspath(__file__))
		s = os.path.join(path,'sources')
		for Root,Dir,File in os.walk(s):
			for f in File:
				if str(f.replace('.py','')) in url:
					info = open(os.path.join(s,f)).read()
					domain = re.findall("domain.+?'(.+?)'",str(info))[0]
					xbmc.log('domain:'+domain,xbmc.LOGNOTICE)
					if domain in url:
						xbmc.log('domain:'+domain,xbmc.LOGNOTICE)
						directory = s
						module_name = f
						module_name = os.path.splitext(module_name)[0]
						path = list(sys.path)
						sys.path.insert(0, directory)
						try:
							sources = __import__(module_name).resolve(url)
						finally:
							sys.path[:] = path # restore
						if sources == None:
							xbmcgui.Dialog().notification("Origin Resolvers", "Can\'t resolve stream link")
							sys.exit()
						elif len(sources)==1:
							for link in sources:
								xbmc.Player().play(link["url"], xbmcgui.ListItem(name))
						elif len(sources)==0:
							xbmcgui.Dialog().notification("Origin Resolvers", "Can\'t resolve stream link")
							sys.exit()
						else:
							choice = Dialog.select('Select Playlink',[link["quality"] for link in sources])
							if choice != -1:
								playlink = sources[choice]['url']
								isFolder=False
								xbmc.Player().play(playlink, xbmcgui.ListItem(name))
				else:
					xbmcgui.Dialog().notification("Origin Resolvers", "Can\'t resolve stream link")
				
	except:
		xbmcgui.Dialog().notification("Origin Resolvers", "Can\'t resolve stream link")
