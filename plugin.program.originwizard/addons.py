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

import urllib, urllib2, re, xbmcplugin, xbmcgui, xbmc, xbmcaddon, os, sys, time, xbmcvfs
import extract
import extras
import shutil
import subprocess
import datetime
import extract
import downloader
import popularpacks
from addon.common.addon import Addon

ADDON_ID   = 'plugin.program.originwizard'
BASEURL    = 'http://addons.totalxbmc.com/'
ADDON      =  xbmcaddon.Addon(id=ADDON_ID)
HOME       =  ADDON.getAddonInfo('path')
dialog     =  xbmcgui.Dialog()
dp         =  xbmcgui.DialogProgress()
USERDATA   =  xbmc.translatePath(os.path.join('special://home/userdata',''))
ADDON_DATA =  xbmc.translatePath(os.path.join(USERDATA,'addon_data'))
ADDONS     =  xbmc.translatePath(os.path.join('special://home','addons'))
ytlink     = 'http://gdata.youtube.com/feeds/api/users/"+YT_ID+"/playlists?start-index=1&max-results=25'
addonfolder      = xbmc.translatePath(os.path.join('special://','home/addons'))
packages         = xbmc.translatePath(os.path.join('special://home/addons','packages'))
username     =  ADDON.getSetting('username')
password     =  ADDON.getSetting('password')


def Update_Repo():
    xbmc.executebuiltin( 'UpdateLocalAddons' )
    xbmc.executebuiltin( 'UpdateAddonRepos' )    
    xbmcgui.Dialog().ok('Force Refresh Started Successfully', 'Depending on the speed of your device it could take a few minutes for the update to take effect.','','[COLOR=blue]For all your XBMC/Kodi support visit[/COLOR] [COLOR=blue][B]http://rh-project.info[/COLOR][/B]')
    return
#-----------------------------------------------------------------------------------------------------------------