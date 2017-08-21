import os
import re
import sys
import xbmc
import xbmcgui

def originresolver(name,url):
    xbmc.log('STARTING O RESOLVER',xbmc.LOGNOTICE)
    Dialog = xbmcgui.Dialog()
    path = os.path.dirname(os.path.abspath(__file__))
    s = os.path.join(path,'sources')
    for Root,Dir,File in os.walk(s):
        for f in File:
            if str(f.replace('.py','')) in url:
                info = open(os.path.join(s,f)).read()
                domain = re.findall("domain.+?'(.+?)'",str(info))[0]
                if domain in url:
                    directory = s
                    module_name = f
                    module_name = os.path.splitext(module_name)[0]
                    path = list(sys.path)
                    sys.path.insert(0, directory)
                    try:
                        sources = __import__(module_name).resolve(url)
                    finally:
                        sys.path[:] = path # restore
                    if len(sources)==1:
                        for link in sources:
                            xbmc.Player().play(link["url"], xbmcgui.ListItem(name))
                    else:
                        choice = Dialog.select('Select Playlink',[link["quality"] for link in sources])
                        if choice != -1:
                            playlink = sources[choice]['url']
                            isFolder=False
                            xbmc.Player().play(playlink, xbmcgui.ListItem(name))


