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

import xbmc
import xbmcgui
import xbmcaddon
import os

ADDON        =  xbmcaddon.Addon(id='plugin.program.originwizard')
zip          =  ADDON.getSetting('zip')
d            =  xbmcgui.Dialog()

def CheckPath():
    path = xbmc.translatePath(os.path.join(zip,'testCBFolder'))
    print path
    try:
        os.makedirs(path)
        os.removedirs(path)
        d.ok('[COLOR=lime]SUCCESS[/COLOR]', 'Great news, the path you chose is writeable.', 'Some of these builds are rather big, we recommend', 'a minimum of 1GB storage space.')
    except:
        d.ok('[COLOR=red]CANNOT WRITE TO PATH[/COLOR]', 'Kodi cannot write to the path you\'ve chosen. Please click OK', 'in the settings menu to save the path then try again.', 'Some devices give false results, we recommend using a USB stick as the backup path.')

if __name__ == '__main__':
    CheckPath()