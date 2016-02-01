#
#      Copyright (C) 2015 Lee Randall (whufclee)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys
import shutil
import extras
import urllib2,urllib
import re
import extract
import downloader
import time

base         =  'http://URLHERE.COM'
ADDON        =  xbmcaddon.Addon(id='plugin.program.originwizard')
VERSION      =  "0.0.3"
PATH         =  "originwizard"

#-----------------------------------------------------------------------------------------------------------------
def Get_Params():
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
#-----------------------------------------------------------------------------------------------------------------
def Popular():
    link = extras.Open_URL('http://totalxbmc.tv/totalrevolution/Addon_Packs/addonpacks.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        extras.addDir('folder2',name,url,'popularwizard',iconimage,fanart,description)
#-----------------------------------------------------------------------------------------------------------------
def Popular_Wizard(name,url,description):
    choice = xbmcgui.Dialog().yesno(name, 'This will install the '+name, '', 'Are you sure you want to continue?', nolabel='Cancel',yeslabel='Accept')
    if choice == 0:
        return
    elif choice == 1:
        import downloader
        path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
        addonfolder = xbmc.translatePath(os.path.join('special://','home'))
        dp = xbmcgui.DialogProgress()
        dp.create("Addon Packs","Downloading "+name +" addon pack.",'', 'Please Wait')
        lib=os.path.join(path, name+'.zip')
        try:
            os.remove(lib)
        except:
            pass
            downloader.download(url, lib, dp)
            time.sleep(3)
            dp.update(0,"", "Extracting Zip Please Wait")
            xbmc.executebuiltin("XBMC.Extract(%s,%s)" %(lib,addonfolder))
            dialog = xbmcgui.Dialog()
            dialog.ok("Total Installer", "All Done. Your addons will now go through the update process, it may take a minute or two until the addons are working.")
            xbmc.executebuiltin( 'UpdateLocalAddons' )
            xbmc.executebuiltin( 'UpdateAddonRepos' )
#            xbmc.executebuiltin("LoadProfile(Master user)")
#-----------------------------------------------------------------------------------------------------------------

params=Get_Params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None

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
        mode=str(params["mode"])
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
                
if mode=='popularwizard': Popular_Wizard(name,url,description)