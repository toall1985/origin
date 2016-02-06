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
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , sys
import urllib , urllib2 , re , glob
import shutil
import extras
import extract
import addonfix
import addons
import communitybuilds
import CheckPath
import cache
import time
import downloader
import plugintools
import zipfile
import ntpath
import base64
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = base64 . decodestring
oo = int ( sys . argv [ 1 ] )
i1iII1IiiIiI1 = 'special://home/resources/art/' + os . sep
iIiiiI1IiI1I1 = xbmcaddon . Addon ( id = 'plugin.program.originwizard' )
o0OoOoOO00 = 'plugin.program.originwizard'
I11i = "Origin Wizard"
O0O = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
Oo = os . path . join ( O0O , o0OoOoOO00 , 'resources' , 'art' ) + os . sep
zip = iIiiiI1IiI1I1 . getSetting ( 'zip' )
I1ii11iIi11i = iIiiiI1IiI1I1 . getSetting ( 'localcopy' )
I1IiI = iIiiiI1IiI1I1 . getSetting ( 'private' )
o0OOO = iIiiiI1IiI1I1 . getSetting ( 'reseller' )
iIiiiI = iIiiiI1IiI1I1 . getSetting ( 'resellername' )
Iii1ii1II11i = iIiiiI1IiI1I1 . getSetting ( 'resellerid' )
iI111iI = iIiiiI1IiI1I1 . getSetting ( 'mastercopy' )
IiII = iIiiiI1IiI1I1 . getSetting ( 'username' )
iI1Ii11111iIi = iIiiiI1IiI1I1 . getSetting ( 'password' )
i1i1II = iIiiiI1IiI1I1 . getSetting ( 'login' )
O0oo0OO0 = iIiiiI1IiI1I1 . getSetting ( 'trcheck' )
I1i1iiI1 = xbmcgui . Dialog ( )
iiIIIII1i1iI = xbmcgui . DialogProgress ( )
o0oO0 = xbmc . translatePath ( 'special://home/' )
oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
o00 = xbmc . translatePath ( os . path . join ( 'special://home/media' , '' ) )
Oo0oO0ooo = xbmc . translatePath ( os . path . join ( oo00 , 'autoexec.py' ) )
o0oOoO00o = xbmc . translatePath ( os . path . join ( oo00 , 'autoexec_bak.py' ) )
i1 = xbmc . translatePath ( os . path . join ( oo00 , 'addon_data' ) )
oOOoo00O0O = xbmc . translatePath ( os . path . join ( oo00 , 'playlists' ) )
i1111 = xbmc . translatePath ( os . path . join ( oo00 , 'Database' ) )
i11 = xbmc . translatePath ( os . path . join ( oo00 , 'Thumbnails' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
I11 = xbmc . translatePath ( os . path . join ( O0O , o0OoOoOO00 , 'default.py' ) )
Oo0o0000o0o0 = xbmc . translatePath ( os . path . join ( O0O , o0OoOoOO00 , 'fanart.jpg' ) )
oOo0oooo00o = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.genesis/favourites.db' ) )
oO0o0o0ooO0oO = os . path . join ( oo00 , 'guisettings.xml' )
oo0o0O00 = xbmc . translatePath ( os . path . join ( oo00 , 'guisettings.xml' ) )
oO = xbmc . translatePath ( os . path . join ( oo00 , 'guifix.xml' ) )
i1iiIIiiI111 = xbmc . translatePath ( os . path . join ( oo00 , 'install.xml' ) )
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
i1iiIII111ii = xbmc . translatePath ( os . path . join ( oo00 , 'favourites.xml' ) )
i1iIIi1 = xbmc . translatePath ( os . path . join ( oo00 , 'sources.xml' ) )
ii11iIi1I = xbmc . translatePath ( os . path . join ( oo00 , 'advancedsettings.xml' ) )
iI111I11I1I1 = xbmc . translatePath ( os . path . join ( oo00 , 'profiles.xml' ) )
OOooO0OOoo = xbmc . translatePath ( os . path . join ( oo00 , 'RssFeeds.xml' ) )
iIii1 = xbmc . translatePath ( os . path . join ( oo00 , 'keymaps' , 'keyboard.xml' ) )
oOOoO0 = xbmc . translatePath ( os . path . join ( zip ) )
O0OoO000O0OO = xbmc . translatePath ( os . path . join ( oOOoO0 , 'Community Builds' , '' ) )
iiI1IiI = xbmc . translatePath ( os . path . join ( i1 , o0OoOoOO00 , 'cookiejar' ) )
II = xbmc . translatePath ( os . path . join ( i1 , o0OoOoOO00 , 'startup.xml' ) )
ooOoOoo0O = xbmc . translatePath ( os . path . join ( i1 , o0OoOoOO00 , 'temp.xml' ) )
OooO0 = xbmc . translatePath ( os . path . join ( i1 , o0OoOoOO00 , 'id.xml' ) )
II11iiii1Ii = xbmc . translatePath ( os . path . join ( i1 , o0OoOoOO00 , 'idtemp.xml' ) )
OO0o = xbmc . translatePath ( os . path . join ( O0O , o0OoOoOO00 , 'resources/' ) )
Ooo = xbmc . getSkinDir ( )
O0o0Oo = xbmc . translatePath ( os . path . join ( i1 , o0OoOoOO00 ) )
Oo00OOOOO = xbmc . translatePath ( os . path . join ( O0o0Oo , 'guinew.xml' ) )
O0OO00o0OO = xbmc . translatePath ( os . path . join ( O0o0Oo , 'guitemp' , '' ) )
I11i1 = xbmc . translatePath ( os . path . join ( oOOoO0 , 'Database' ) )
iIi1ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.program.originwizard/Generated/TEST/resources/' ) )
o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.program.originwizard' ) )
I11II1i = 'None'
IIIII = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
ooooooO0oo = 'http://rh-project.info/'
IIiiiiiiIi1I1 = "2.0.3"
I1IIIii = "originwizard"
if 95 - 95: iiiIi1i1I % II11iII % OoOo
if 18 - 18: iii11I111
if 63 - 63: I11iii1Ii * OOOooOooo00O0 . o0IiIIIiIi11i1 * IIIii1II1II
def i1I1iI ( ) :
 for file in glob . glob ( os . path . join ( O0O , '*' ) ) :
  oo0OooOOo0 = str ( file ) . replace ( O0O , '[COLOR=red]REMOVE [/COLOR]' ) . replace ( 'plugin.' , '[COLOR=dodgerblue](PLUGIN) [/COLOR]' ) . replace ( 'audio.' , '' ) . replace ( 'video.' , '' ) . replace ( 'skin.' , '[COLOR=yellow](SKIN) [/COLOR]' ) . replace ( 'repository.' , '[COLOR=orange](REPOSITORY) [/COLOR]' ) . replace ( 'script.' , '[COLOR=cyan](SCRIPT) [/COLOR]' ) . replace ( 'metadata.' , '[COLOR=gold](METADATA) [/COLOR]' ) . replace ( 'service.' , '[COLOR=pink](SERVICE) [/COLOR]' ) . replace ( 'weather.' , '[COLOR=green](WEATHER) [/COLOR]' ) . replace ( 'module.' , '[COLOR=gold](MODULE) [/COLOR]' )
  o0O = ( os . path . join ( file , 'icon.png' ) )
  O00oO = ( os . path . join ( file , 'fanart.jpg' ) )
  extras . addDir ( '' , oo0OooOOo0 , file , 'remove_addons' , o0O , O00oO , '' , '' )
  if 39 - 39: O0O0O - i1IiIIIII % Ii1i111I / OoOO00O - IIiI1I - O00Oo000ooO0
  if 100 - 100: II11i1iIiII1 + O0 / IIIii1II1II * O00Oo000ooO0 / iIii1I11I1II1
def ii111 ( ) :
 iIiiiI1IiI1I1 . openSettings ( sys . argv [ 0 ] )
 if 16 - 16: o0IiIIIiIi11i1 + iii11I111 - iiiIi1i1I
 if 85 - 85: I11iii1Ii + i1IIi
def Oo0OoO00oOO0o ( ) :
 extras . addDir ( 'folder' , 'Completely remove an add-on (inc. passwords)' , 'plugin' , 'addon_removal_menu' , 'Remove_Addon.png' , '' , '' , '' )
 extras . addDir ( '' , 'Hide my add-on passwords' , 'none' , 'hide_passwords' , 'Hide_Passwords.png' , '' , '' , '' )
 extras . addDir ( '' , 'Unhide my add-on passwords' , 'none' , 'unhide_passwords' , 'Unhide_Passwords.png' , '' , '' , '' )
 extras . addDir ( '' , 'Update My Add-ons (Force Refresh)' , 'none' , 'update' , 'Update_Addons.png' , '' , '' , '' )
 extras . addDir ( '' , 'Wipe All Add-on Settings (addon_data)' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 if 80 - 80: IIIii1II1II + O0O0O - O0O0O % OoOO00O
 if 63 - 63: II11iII - o0IiIIIiIi11i1 + O0 % i1IiIIIII / iIii1I11I1II1 / OOOooOooo00O0
 if 98 - 98: OoOO00O * OoOO00O / OoOO00O + i1IiIIIII
def ii111111I1iII ( ) :
 extras . addDir ( 'folder' , 'Backup My Content' , 'none' , 'backup_option' , 'Backup.png' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Restore My Content' , 'none' , 'restore_option' , 'Restore.png' , '' , '' , '' )
 if 68 - 68: OoOO00O - iIii1I11I1II1 * i11iIiiIii / o0IiIIIiIi11i1 * O00Oo000ooO0
 if 23 - 23: OoOO00O
def oo0oOo ( ) :
 o000O0o = 0
 iI1iII1 = iIiiiI1IiI1I1 . getSetting ( 'maintenance' )
 oO0OOoo0OO = iIiiiI1IiI1I1 . getSetting ( 'mainmenu' )
 O0ii1ii1ii = iIiiiI1IiI1I1 . getSetting ( 'guisettings' )
 oooooOoo0ooo = iIiiiI1IiI1I1 . getSetting ( 'adultbuilds' )
 if oO0OOoo0OO == 'true' :
  extras . addDir ( 'folder' , 'Origin Builds' , 'none' , 'buildmenu' , 'Build_Menu.png' , '' , '' , '' )
  extras . addDir ( 'folder' , 'Fast Update' , 'none' , 'fastupdatemenu' , 'Adult_Menu.png' , '' , '' , '' )
 if O0ii1ii1ii == 'true' :
  extras . addDir ( 'folder' , 'Gui Settings XML' , 'none' , 'guisettings' , 'Gui_Menu.png' , '' , '' , '' )
 if iI1iII1 == 'true' :
  extras . addDir ( 'folder' , 'Maintenance' , 'none' , 'tools' , 'Tools.png' , '' , '' , '' )
  if 6 - 6: i1IiIIIII - Ii1i111I + iIii1I11I1II1 - O00Oo000ooO0 - i11iIiiIii
  if 79 - 79: I11iii1Ii - O0 * iii11I111 + I11iii1Ii % O0 * O0
  if 61 - 61: iiiIi1i1I
def O0OOO ( ) :
 II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( 'Clear All Known Cache?' , 'This will clear all known cache files and can help' , 'if you\'re encountering kick-outs during playback.' , 'as well as other random issues. There is no harm in using this.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if II11iIiIIIiI == 1 :
  cache . Wipe_Cache ( )
  o0o ( )
  if 84 - 84: O0
  if 74 - 74: o0IiIIIiIi11i1 - II11iII - OoOo . Ii1i111I - IIiI1I
def OOOoOoo0O ( ) :
 O000OOo00oo = [ ]
 oo0OOo = sys . argv [ 2 ]
 if len ( oo0OOo ) >= 2 :
  ooOOO00Ooo = sys . argv [ 2 ]
  IiIIIi1iIi = ooOOO00Ooo . replace ( '?' , '' )
  if ( ooOOO00Ooo [ len ( ooOOO00Ooo ) - 1 ] == '/' ) :
   ooOOO00Ooo = ooOOO00Ooo [ 0 : len ( ooOOO00Ooo ) - 2 ]
  ooOOoooooo = IiIIIi1iIi . split ( '&' )
  O000OOo00oo = { }
  for II1I in range ( len ( ooOOoooooo ) ) :
   O0i1II1Iiii1I11 = { }
   O0i1II1Iiii1I11 = ooOOoooooo [ II1I ] . split ( '=' )
   if ( len ( O0i1II1Iiii1I11 ) ) == 2 :
    O000OOo00oo [ O0i1II1Iiii1I11 [ 0 ] ] = O0i1II1Iiii1I11 [ 1 ]
    if 9 - 9: o0IiIIIiIi11i1 / OoOo - II11iII / OoooooooOO / iIii1I11I1II1 - OOOooOooo00O0
 return O000OOo00oo
 if 91 - 91: OoOO00O % i1IIi % iIii1I11I1II1
 if 20 - 20: O0O0O % Ii1i111I / Ii1i111I + Ii1i111I
def III1IiiI ( ) :
 II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( 'Delete Addon_Data Folder?' , 'This will free up space by deleting your addon_data' , 'folder. This contains all addon related settings' , 'including username and password info.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if II11iIiIIIiI == 1 :
  extras . Delete_Userdata ( )
  I1i1iiI1 . ok ( "Addon_Data Removed" , '' , 'Your addon_data folder has now been removed.' , '' )
  if 31 - 31: OOOooOooo00O0 . II11iII
  if 46 - 46: OoOO00O
def IIIII11I1IiI ( ) :
 II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( 'Remove All Crash Logs?' , 'There is absolutely no harm in doing this, these are' , 'log files generated when Kodi crashes and are' , 'only used for debugging purposes.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if II11iIiIIIiI == 1 :
  extras . Delete_Logs ( )
  I1i1iiI1 . ok ( "Crash Logs Removed" , '' , 'Your crash log files have now been removed.' , '' )
  if 16 - 16: iIii1I11I1II1
  if 90 - 90: OOOooOooo00O0 % i1IIi / iii11I111
def IIi ( ) :
 II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( 'Delete Packages Folder?' , 'This will free up space by deleting the zip install' , 'files of your addons. The only downside is you\'ll no' , 'longer be able to rollback to older versions.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if II11iIiIIIiI == 1 :
  extras . Delete_Packages ( )
  I1i1iiI1 . ok ( "Packages Removed" , '' , 'Your zip install files have now been removed.' , '' )
  if 41 - 41: Ii1i111I - O0 - O0
  if 68 - 68: O0O0O % O00Oo000ooO0
def o0o ( ) :
 II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( 'Clear Cached Images?' , 'This will clear your textures13.db file and remove' , 'your Thumbnails folder. These will automatically be' , 'repopulated after a restart.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if II11iIiIIIiI == 1 :
  cache . Remove_Textures ( )
  extras . Destroy_Path ( i11 )
  II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( 'Quit Kodi Now?' , 'Cache has been successfully deleted.' , 'You must now restart Kodi, would you like to quit now?' , '' , nolabel = 'I\'ll restart later' , yeslabel = 'Yes, quit' )
  if II11iIiIIIiI == 1 :
   ooO00OO0 ( )
   if 31 - 31: OoOO00O % OoOO00O % i1IiIIIII
   if 69 - 69: iii11I111 - OoOo + i1IIi / O00Oo000ooO0
def ii1 ( ) :
 extras . addDir ( 'folder' , '[COLOR white]Addon Installer[/COLOR]' , 'none' , 'Addons_Menu' , '' , '' , '' , '' )
 extras . addDir ( 'wizard' , '[COLOR red]Wizard Generator[/COLOR]' , 'none' , 'Merlin' , i1iII1IiiIiI1 + 'icon.png' , i1iII1IiiIiI1 + 'fanart.jpg' , '' , '' )
 extras . addDir ( 'folder' , 'Add-on Maintenance/Fixes' , 'none' , 'addonfixes' , '' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Backup/Restore My Content' , 'none' , 'backup_restore' , '' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Clean/Wipe Options' , 'none' , 'wipetools' , '' , '' , '' , '' )
 extras . addDir ( '' , 'Check XBMC/Kodi Version' , 'none' , 'xbmcversion' , '' , '' , '' , '' )
 extras . addDir ( '' , 'Convert Physical Paths To Special' , o0oO0 , 'fix_special' , '' , '' , '' , '' )
 extras . addDir ( '' , 'Force Close Kodi' , 'url' , 'kill_xbmc' , '' , '' , '' , '' )
 if 11 - 11: IIiI1I * II11iII . iIii1I11I1II1 % OoooooooOO + OoOO00O
 if 78 - 78: iii11I111 . O0O0O + iii11I111 / i1IiIIIII / iii11I111
def oO0O00OoOO0 ( ) :
 extras . addDir ( 'wizard2' , '[COLOR red]How To Guide[/COLOR]' , 'none' , 'How_To' , i1iII1IiiIiI1 + 'icon.png' , i1iII1IiiIiI1 + 'fanart.jpg' , '' , '' )
 extras . addDir ( 'wizard2' , '[COLOR blue]Generate your personalised wizard[/COLOR]' , 'none' , 'Text_Gen' , i1iII1IiiIiI1 + 'icon.png' , i1iII1IiiIiI1 + 'fanart.jpg' , '' , '' )
 if 82 - 82: iiiIi1i1I . IIiI1I - iIii1I11I1II1 - IIiI1I * iiiIi1i1I
 if 77 - 77: iIii1I11I1II1 * iii11I111
 if 95 - 95: II11iII + i11iIiiIii
 if 6 - 6: II11i1iIiII1 / i11iIiiIii + OoOO00O * IIIii1II1II
def o00o0 ( ) :
 ii ( 'How To guide For Wizard Creation' , '1: First you will need to create a build and host somewhere online that it can be accessed, aswell as an image for thumbnail and background\n\n\n2:Run Wizard Generator, it will ask you to set backup path if its not been set, try to keep local on the device\n\n\n3:Fill in the relevant fields, then let others enjoy your build. for FREE\n\n\n4:[COLOR red] Take time to thank devs for there hard work, maybe donate (not to me i dont accept as i dont have costs, but to those who do need it) and just appreciate the work that goes in to bring you FREE stuff, maybe visit some streaming sites suffer some ads to keep them going once a week aswell, help people to help you basically[/COLOR]' )
 if 84 - 84: OOOooOooo00O0 % iiiIi1i1I . i11iIiiIii / iii11I111
 if 80 - 80: O00Oo000ooO0 . i11iIiiIii - OOOooOooo00O0
def ii ( heading , announce ) :
 class iIiIIi1 ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  isFolder = True
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : I1IIII1i = open ( announce ) ; I1I11i = I1IIII1i . read ( )
   except : I1I11i = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1I11i ) )
   return
 iIiIIi1 ( )
 if 5 - 5: OoooooooOO % I11iii1Ii % IIIii1II1II % OoOO00O
 if 7 - 7: iiiIi1i1I + OoooooooOO . O00Oo000ooO0 . II11i1iIiII1 - OOOooOooo00O0
 if 26 - 26: OoOo / IIiI1I % iIii1I11I1II1 / IIiI1I + i1IiIIIII
def oOO0O00oO0Ooo ( ) :
 oO0Oo0O0o = xbmc . translatePath ( os . path . join ( oOOoO0 , 'Community Builds' , 'My Builds' ) )
 II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( "ABSOLUTELY CERTAIN?!!!" , 'Are you absolutely certain you want to wipe?' , '' , 'All addons and settings will be completely wiped!' , yeslabel = 'Yes' , nolabel = 'No' )
 if II11iIiIIIiI == 1 :
  if Ooo != "skin.confluence" :
   I1i1iiI1 . ok ( '[COLOR=white]Origin[/COLOR]' , 'Please switch to the default Confluence skin' , 'before performing a wipe.' , '' )
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
   return
  else :
   II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( "VERY IMPORTANT" , 'This will completely wipe your install.' , 'Would you like to create a backup before proceeding?' , '' , yeslabel = 'No' , nolabel = 'Yes' )
   if II11iIiIIIiI == 0 :
    if not os . path . exists ( oO0Oo0O0o ) :
     os . makedirs ( oO0Oo0O0o )
    OO = extras . Get_Keyboard ( heading = "Enter a name for this backup" )
    if ( not OO ) : return False , 0
    I1iI1ii1II = urllib . quote_plus ( OO )
    O0O0OOOOoo = xbmc . translatePath ( os . path . join ( oO0Oo0O0o , I1iI1ii1II + '.zip' ) )
    oOooO0 = [ 'plugin.program.originwizard' ]
    Ii1I1Ii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
    OOoO0 = "Creating full backup of existing build"
    OO0Oooo0oOO0O = "Archiving..."
    o00O0 = ""
    oOO0O00Oo0O0o = "Please Wait"
    communitybuilds . Archive_Tree ( o0oO0 , O0O0OOOOoo , OOoO0 , OO0Oooo0oOO0O , o00O0 , oOO0O00Oo0O0o , oOooO0 , Ii1I1Ii )
   II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( "Remove Origin Wizard?" , 'Do you also want to remove the Origin Wizard' , 'add-on and have a complete fresh start or would you' , 'prefer to keep this on your system?' , yeslabel = 'Remove' , nolabel = 'Keep' )
   if II11iIiIIIiI == 0 :
    cache . Remove_Textures ( )
    ii1I1iIIiiIIi1i = xbmc . translatePath ( os . path . join ( O0O , o0OoOoOO00 , '' ) )
    O0O0ooOOO = xbmc . translatePath ( os . path . join ( o0oO0 , '..' , 'originwizard.zip' ) )
    communitybuilds . Archive_File ( ii1I1iIIiiIIi1i , O0O0ooOOO )
    oOOo0O00o = xbmc . translatePath ( os . path . join ( O0O , 'script.module.addon.common' , '' ) )
    iIiIi11 = xbmc . translatePath ( os . path . join ( o0oO0 , '..' , 'originwizarddep.zip' ) )
    communitybuilds . Archive_File ( oOOo0O00o , iIiIi11 )
    extras . Destroy_Path ( o0oO0 )
    if not os . path . exists ( ii1I1iIIiiIIi1i ) :
     os . makedirs ( ii1I1iIIiiIIi1i )
    if not os . path . exists ( oOOo0O00o ) :
     os . makedirs ( oOOo0O00o )
    time . sleep ( 1 )
    communitybuilds . Read_Zip ( O0O0ooOOO )
    iiIIIII1i1iI . create ( "[[COLOR=white]Origin[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
    iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
    extract . all ( O0O0ooOOO , ii1I1iIIiiIIi1i , iiIIIII1i1iI )
    communitybuilds . Read_Zip ( iIiIi11 )
    extract . all ( iIiIi11 , oOOo0O00o , iiIIIII1i1iI )
    iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
    iiIIIII1i1iI . close ( )
    time . sleep ( 1 )
    extras . Kill_XBMC ( )
   elif II11iIiIIIiI == 1 :
    cache . Remove_Textures ( )
    extras . Destroy_Path ( o0oO0 )
    iiIIIII1i1iI . close ( )
    extras . Kill_XBMC ( )
   else : return
   if 87 - 87: OoOo . II11iII - iiiIi1i1I + O0 / OoOo / IIIii1II1II
   if 25 - 25: II11iII . II11iII - I11iii1Ii % I11iii1Ii - i11iIiiIii / O00Oo000ooO0
def OOoO ( ) :
 extras . addDir ( '' , 'Clear Cache' , 'url' , 'clear_cache' , 'Clear_Cache.png' , '' , '' , '' )
 extras . addDir ( '' , 'Clear My Cached Artwork' , 'none' , 'remove_textures' , 'Delete_Cached_Artwork.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Addon_Data' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Old Builds/Zips From Device' , 'url' , 'remove_build' , 'Delete_Builds.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Old Crash Logs' , 'url' , 'remove_crash_logs' , 'Delete_Crash_Logs.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Packages Folder' , 'url' , 'remove_packages' , 'Delete_Packages.png' , '' , '' , '' )
 extras . addDir ( '' , 'Wipe My Install (Fresh Start)' , 'none' , 'wipe_xbmc' , 'Fresh_Start.png' , '' , '' , '' )
 if 89 - 89: OOOooOooo00O0 + iii11I111 * i1IiIIIII * Ii1i111I
 if 37 - 37: OoooooooOO - O0 - OOOooOooo00O0
def o0o0O0O00oOOo ( ) :
 iIIIiIi = OO0O0 ( 'http://back2basicsbuild.co.uk/wizard/toolbox.xml' ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11I11 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iIIIiIi )
 for oo0OooOOo0 , o000O0O , o0O , O00oO , I1i1i1iii in I11I11 :
  I1111i ( oo0OooOOo0 , o000O0O , 'wizard' , o0O , O00oO , I1i1i1iii )
 iIIii ( '500' )
 if 92 - 92: Ii1i111I + IIIii1II1II % O0O0O
def OO0O0 ( url ) :
 oOo0 = urllib2 . Request ( url )
 oOo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1iI = urllib2 . urlopen ( oOo0 )
 iIIIiIi = i1iI . read ( )
 i1iI . close ( )
 return iIIIiIi
 if 94 - 94: iIii1I11I1II1 / OoOo % OoOO00O * OoOO00O * iiiIi1i1I
def IIiIiI ( name , url , description ) :
 OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iiIIIII1i1iI = xbmcgui . DialogProgress ( )
 iiIIIII1i1iI . create ( "origin wizard" , "Downloading " , '' , 'Please Wait' )
 IIiI1i1i = os . path . join ( OOO , name + '.zip' )
 try :
  os . remove ( IIiI1i1i )
 except :
  pass
 downloader . download ( url , IIiI1i1i , iiIIIII1i1iI )
 O00Oo0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print O00Oo0
 print '======================================='
 extract . all ( IIiI1i1i , O00Oo0 , iiIIIII1i1iI )
 I1i1iiI1 = xbmcgui . Dialog ( )
 I1i1iiI1 . ok ( "DOWNLOAD COMPLETE" , 'To ensure all changes are saved you must now close Kodi' , 'to force close Kodi. Click ok,' , 'DO NOT use the quit/exit options in Kodi.' )
 ooO00OO0 ( )
 if 33 - 33: O0 * OOOooOooo00O0 - O00Oo000ooO0 % O00Oo000ooO0
def ooO00OO0 ( ) :
 II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if II11iIiIIIiI == 0 :
  return
 elif II11iIiIIIiI == 1 :
  pass
 I11I = I11iIi1i1II11 ( )
 print "Platform: " + str ( I11I )
 if I11I == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  I1i1iiI1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I11I == 'linux' :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  I1i1iiI1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I11I == 'android' :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  I1i1iiI1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
 elif I11I == 'windows' :
  print "############   try windows force close  #################"
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill XBMC.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill Kodi.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im Kodi.exe /f' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im XBMC.exe /f' )
  except : pass
  I1i1iiI1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  I1i1iiI1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
  if 47 - 47: OoooooooOO . I11iii1Ii
def I11iIi1i1II11 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) :
  return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) :
  return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) :
  return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) :
  return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) :
  return 'ios'
  if 26 - 26: Ii1i111I % o0IiIIIiIi11i1
  if 76 - 76: IIiI1I * OoOO00O
def I1111i ( name , url , mode , iconimage , fanart , description ) :
 ooooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0oooOO00 = True
 iiIiii1IIIII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIiii1IIIII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIiii1IIIII . setProperty ( "Fanart_Image" , fanart )
 o0oooOO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooooooo00o , listitem = iiIiii1IIIII , isFolder = False )
 return o0oooOO00
 if 67 - 67: Ii1i111I / IIiI1I
def iIIii ( content = '' ) :
 if not content :
  return
  if 9 - 9: O0 % O0 - OOOooOooo00O0
 xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if iIiiiI1IiI1I1 . getSetting ( 'auto-view' ) != 'true' :
  return
  if 51 - 51: II11iII . iIii1I11I1II1 - o0IiIIIiIi11i1 / O0
 if content == 'addons' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % iIiiiI1IiI1I1 . getSetting ( 'addon_view' ) )
 else :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % iIiiiI1IiI1I1 . getSetting ( 'default-view' ) )
  if 52 - 52: OOOooOooo00O0 + O0 + OoOO00O + OoOo % OoOO00O
  if 75 - 75: II11iII . II11i1iIiII1 . O0 * O00Oo000ooO0
ooOOO00Ooo = OOOoOoo0O ( )
i11II1I11I1 = None
OOoOO0ooo = None
II1iIi11 = None
I11iiii = None
O0i1iI = None
I1i1i1iii = None
IiI1iiiIii = None
I1III1111iIi = None
O00oO = None
I1i111I = None
o0O = None
iIIIiIi = None
OooOo0oo0O0o00O = None
I1i11 = None
IiIi1I1 = None
oo0OooOOo0 = None
IiIIi1 = None
IIIIiii1IIii = None
II1i11I = None
ii1I1IIii11 = None
O0o0oO = None
IIIIiIiIi1 = None
I11iiiiI1i = None
iI1i11 = None
OoOOoooOO0O = None
o000O0O = None
ooo00Ooo = None
Oo0o0O00 = None
ii1I1i11 = None
OOo0O0oo0OO0O = None
OO0 = None
if 72 - 72: OoooooooOO
try : i11II1I11I1 = urllib . unquote_plus ( ooOOO00Ooo [ "addon_id" ] )
except : pass
try : OooooOoooO = urllib . unquote_plus ( ooOOO00Ooo [ "adult" ] )
except : pass
try : OOoOO0ooo = urllib . unquote_plus ( ooOOO00Ooo [ "audioaddons" ] )
except : pass
try : II1iIi11 = urllib . unquote_plus ( ooOOO00Ooo [ "author" ] )
except : pass
try : I11iiii = urllib . unquote_plus ( ooOOO00Ooo [ "buildname" ] )
except : pass
try : O0i1iI = urllib . unquote_plus ( ooOOO00Ooo [ "data_path" ] )
except : pass
try : I1i1i1iii = urllib . unquote_plus ( ooOOO00Ooo [ "description" ] )
except : pass
try : IiI1iiiIii = urllib . unquote_plus ( ooOOO00Ooo [ "DOB" ] )
except : pass
try : I1III1111iIi = urllib . unquote_plus ( ooOOO00Ooo [ "email" ] )
except : pass
try : O00oO = urllib . unquote_plus ( ooOOO00Ooo [ "fanart" ] )
except : pass
try : I1i111I = urllib . unquote_plus ( ooOOO00Ooo [ "forum" ] )
except : pass
try : oOIIiIi = urllib . unquote_plus ( ooOOO00Ooo [ "guisettingslink" ] )
except : pass
try : o0O = urllib . unquote_plus ( ooOOO00Ooo [ "iconimage" ] )
except : pass
try : iIIIiIi = urllib . unquote_plus ( ooOOO00Ooo [ "link" ] )
except : pass
try : OooOo0oo0O0o00O = urllib . unquote_plus ( ooOOO00Ooo [ "local" ] )
except : pass
try : I1i11 = urllib . unquote_plus ( ooOOO00Ooo [ "messages" ] )
except : pass
try : IiIi1I1 = str ( ooOOO00Ooo [ "mode" ] )
except : pass
try : oo0OooOOo0 = urllib . unquote_plus ( ooOOO00Ooo [ "name" ] )
except : pass
try : OOoOooOoOOOoo = urllib . unquote_plus ( ooOOO00Ooo [ "pictureaddons" ] )
except : pass
try : IiIIi1 = urllib . unquote_plus ( ooOOO00Ooo [ "posts" ] )
except : pass
try : IIIIiii1IIii = urllib . unquote_plus ( ooOOO00Ooo [ "programaddons" ] )
except : pass
try : II1i11I = urllib . unquote_plus ( ooOOO00Ooo [ "provider_name" ] )
except : pass
try : O0o0oO = urllib . unquote_plus ( ooOOO00Ooo [ "repo_link" ] )
except : pass
try : ii1I1IIii11 = urllib . unquote_plus ( ooOOO00Ooo [ "repo_id" ] )
except : pass
try : IIIIiIiIi1 = urllib . unquote_plus ( ooOOO00Ooo [ "skins" ] )
except : pass
try : I11iiiiI1i = urllib . unquote_plus ( ooOOO00Ooo [ "sources" ] )
except : pass
try : iI1i11 = urllib . unquote_plus ( ooOOO00Ooo [ "updated" ] )
except : pass
try : OoOOoooOO0O = urllib . unquote_plus ( ooOOO00Ooo [ "unread" ] )
except : pass
try : o000O0O = urllib . unquote_plus ( ooOOO00Ooo [ "url" ] )
except : pass
try : ooo00Ooo = urllib . unquote_plus ( ooOOO00Ooo [ "version" ] )
except : pass
try : Oo0o0O00 = urllib . unquote_plus ( ooOOO00Ooo [ "video" ] )
except : pass
try : ii1I1i11 = urllib . unquote_plus ( ooOOO00Ooo [ "videoaddons" ] )
except : pass
try : OO0 = urllib . unquote_plus ( ooOOO00Ooo [ "zip_link" ] )
except : pass
if 25 - 25: OoooooooOO - II11iII . II11iII * IIIii1II1II
print str ( I1IIIii ) + ': ' + str ( IIiiiiiiIi1I1 )
print "Mode: " + str ( IiIi1I1 )
print "URL: " + str ( o000O0O )
print "Name: " + str ( oo0OooOOo0 )
print "IconImage: " + str ( o0O )
if 81 - 81: OoOO00O + IIiI1I
if 98 - 98: II11iII
if 95 - 95: II11i1iIiII1 / II11i1iIiII1
if 30 - 30: o0IiIIIiIi11i1 + OoOo / OoOo % o0IiIIIiIi11i1 . o0IiIIIiIi11i1
if 55 - 55: II11i1iIiII1 - i1IiIIIII + iiiIi1i1I + OoOO00O % Ii1i111I
def iiI11i1II ( ) :
 if 51 - 51: OOOooOooo00O0 % OoOo % OOOooOooo00O0 * O0 - O0O0O % OoOo
 o0O00OooOOOOO = OO0O0 ( 'http://back2basicsbuild.co.uk/Fast%20Update/readme.txt' )
 I11I11 = re . compile ( '<url="(.+?)"' ) . findall ( o0O00OooOOOOO )
 for o000O0O in I11I11 :
  if 'addons' in o000O0O :
   OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   iiIIIII1i1iI = xbmcgui . DialogProgress ( )
   iiIIIII1i1iI . create ( "Origin" , "Downloading Content" , '' , 'Please Wait' )
   IIiI1i1i = os . path . join ( OOO , oo0OooOOo0 + '.zip' )
   try :
    os . remove ( IIiI1i1i )
   except :
    pass
   downloader . download ( o000O0O , IIiI1i1i , iiIIIII1i1iI )
   O00Oo0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print O00Oo0
   print '======================================='
   extract . all ( IIiI1i1i , O00Oo0 , iiIIIII1i1iI )
   I1i1iiI1 = xbmcgui . Dialog ( )
   I1i1iiI1 . ok ( "Origin" , "Press ok to update gui settings" , "[COLOR yellow]Brought To You By Origin[/COLOR]" )
   IIIiiI1i1 ( )
   if 15 - 15: i1IIi + I11iii1Ii
def IIIiiI1i1 ( ) :
 if 48 - 48: II11iII % OoOO00O / iIii1I11I1II1
 o0O00OooOOOOO = OO0O0 ( 'http://back2basicsbuild.co.uk/Fast%20Update/readme.txt' )
 I11I11 = re . compile ( '<url="(.+?)"' ) . findall ( o0O00OooOOOOO )
 for o000O0O in I11I11 :
  if 'gui' in o000O0O :
   OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   iiIIIII1i1iI = xbmcgui . DialogProgress ( )
   iiIIIII1i1iI . create ( "Origin" , "Downloading Content" , '' , 'Please Wait' )
   IIiI1i1i = os . path . join ( OOO , oo0OooOOo0 + '.zip' )
   try :
    os . remove ( IIiI1i1i )
   except :
    pass
   downloader . download ( o000O0O , IIiI1i1i , iiIIIII1i1iI )
   O00Oo0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'userdata' ) )
   time . sleep ( 2 )
   iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print O00Oo0
   print '======================================='
   extract . all ( IIiI1i1i , O00Oo0 , iiIIIII1i1iI )
   I1i1iiI1 = xbmcgui . Dialog ( )
   I1i1iiI1 . ok ( "Origin" , "Press ok to remove old addons" , "[COLOR yellow]Brought To You By Origin[/COLOR]" )
   Oo0oooO0oO ( )
   if 19 - 19: i11iIiiIii + OoooooooOO - OoOo - i1IiIIIII
def Oo0oooO0oO ( ) :
 o0O00OooOOOOO = OO0O0 ( 'http://back2basicsbuild.co.uk/Fast%20Update/readme.txt' )
 I11I11 = re . compile ( '<name="(.+?)"' ) . findall ( o0O00OooOOOOO )
 for oo0OooOOo0 in I11I11 :
  shutil . rmtree ( O0O + oo0OooOOo0 )
  I1i1iiI1 . ok ( "Origin" , "Press ok to refresh" , "[COLOR yellow]If changes dont take effect you may need to force close[/COLOR]" )
  Iii1iiIi1II ( )
  if 60 - 60: II11iII - IIIii1II1II * i1IiIIIII % iiiIi1i1I
  if 62 - 62: iIii1I11I1II1
  if 12 - 12: O0O0O / OOOooOooo00O0
  if 42 - 42: OoOo
iIiiiI1IiI1I1 = xbmcaddon . Addon ( id = 'plugin.program.originwizard' )
II1IIiiIiI = xbmcgui . Dialog ( )
o0oO0 = xbmc . translatePath ( 'special://home/' )
oOOoO0 = xbmc . translatePath ( os . path . join ( zip ) )
iiIIIII1i1iI = xbmcgui . DialogProgress ( )
i1II1I1Iii1 = 'https://addons.tvaddons.ag/'
if 30 - 30: OoooooooOO - I11iii1Ii
def OO0O0 ( url ) :
 oOo0 = urllib2 . Request ( url )
 oOo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1iI = urllib2 . urlopen ( oOo0 )
 iIIIiIi = i1iI . read ( )
 i1iI . close ( )
 return iIIIiIi
 if 75 - 75: iIii1I11I1II1 - Ii1i111I . OoOo % i11iIiiIii % i1IiIIIII
def O00 ( ) :
 if 30 - 30: II11iII + iii11I111 % Ii1i111I * OoOO00O / OoOo - i1IiIIIII
 extras . addDir ( 'folder' , 'Catagories' , 'none' , 'Addon_Cat' , '' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Search' , 'none' , 'Search_Addons' , '' , '' , '' , '' )
 if 64 - 64: iIii1I11I1II1
def iI ( ) :
 I1ii1 = II1IIiiIiI . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O00Oo0o0000OOoO = I1ii1 . lower ( )
 IiIi1I1ii111 = 'https://addons.tvaddons.ag/search/?keyword=' + O00Oo0o0000OOoO
 o0O00OooOOOOO = OO0O0 ( IiIi1I1ii111 )
 I11I11 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o0O00OooOOOOO )
 for o000O0O , IiIiIi , oo0OooOOo0 in I11I11 :
  extras . addDirNew ( oo0OooOOo0 , o000O0O , 'Addon_Extract' , 'https://addons.tvaddons.ag/' + IiIiIi , Oo0o0000o0o0 , '' )
  if 27 - 27: o0IiIIIiIi11i1 + I11iii1Ii - O0O0O + O0 . Ii1i111I
def iIi1i1iIi1iI ( ) :
 o0O00OooOOOOO = OO0O0 ( i1II1I1Iii1 )
 I11I11 = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o0O00OooOOOOO )
 for o000O0O , iiIi1iI1iIii , oo0OooOOo0 in I11I11 :
  if 'Repositories' in oo0OooOOo0 :
   pass
  elif 'Services' in oo0OooOOo0 :
   pass
  elif 'International' in oo0OooOOo0 :
   pass
  else :
   extras . addDir ( 'folder' , oo0OooOOo0 , o000O0O , 'Addon' , 'https://addons.tvaddons.ag/' + iiIi1iI1iIii , '' , '' , '' )
   if 68 - 68: O0O0O
def OooO0oo ( url ) :
 o0O00OooOOOOO = OO0O0 ( url )
 I11I11 = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" width="100%" alt=".+?" class="pic" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o0O00OooOOOOO )
 for url , iiIi1iI1iIii , oo0OooOOo0 in I11I11 :
  extras . addDir ( '' , oo0OooOOo0 , url , 'Addon' , 'https://addons.tvaddons.ag/' + iiIi1iI1iIii , '' , '' , '' )
  if 89 - 89: Ii1i111I
  if 76 - 76: II11i1iIiII1
def IIIiI11ii1I ( url ) :
 o0O00OooOOOOO = OO0O0 ( url )
 IiiiI = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( o0O00OooOOOOO )
 for url in IiiiI :
  extras . addDirNewFolder ( 'NEXT PAGE' , 'https://addons.tvaddons.ag' + url , 'Addon' , Oo + 'Next.png' , '' , '' )
 I11I11 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o0O00OooOOOOO )
 for url , iiIi1iI1iIii , oo0OooOOo0 in I11I11 :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>' + 'https://addons.tvaddons.ag/' + iiIi1iI1iIii + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
  if 'Please' in oo0OooOOo0 :
   pass
  else :
   extras . addDirNew ( oo0OooOOo0 , url , 'Addon_Extract' , 'https://addons.tvaddons.ag/' + iiIi1iI1iIii , Oo0o0000o0o0 , '' )
   if 61 - 61: O0O0O % O0O0O * OOOooOooo00O0 / OOOooOooo00O0
   if 75 - 75: IIiI1I . II11i1iIiII1
def iII111i ( url , name ) :
 o0O00OooOOOOO = OO0O0 ( url )
 I11I11 = re . compile ( '<a href="(.+?)"' ) . findall ( o0O00OooOOOOO )
 for url in I11I11 :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   iiIIIII1i1iI = xbmcgui . DialogProgress ( )
   iiIIIII1i1iI . create ( "Origin" , "Downloading Content" , '' , 'Please Wait' )
   IIiI1i1i = os . path . join ( OOO , name + '.zip' )
   try :
    os . remove ( IIiI1i1i )
   except :
    pass
   downloader . download ( url , IIiI1i1i , iiIIIII1i1iI )
   O00Oo0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print O00Oo0
   print '======================================='
   extract . all ( IIiI1i1i , O00Oo0 , iiIIIII1i1iI )
   I1i1iiI1 = xbmcgui . Dialog ( )
   I1i1iiI1 . ok ( "Origin" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Origin[/COLOR]" )
   Iii1iiIi1II ( )
   if 87 - 87: O0O0O + II11i1iIiII1 % i11iIiiIii % O0
def Iii1iiIi1II ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 I1i1iiI1 = xbmcgui . Dialog ( )
 I1i1iiI1 . ok ( "Origin" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin[/COLOR]" )
 return
 if 27 - 27: O0
 if 79 - 79: OOOooOooo00O0 - i1IiIIIII + OOOooOooo00O0 . IIIii1II1II
 if 28 - 28: i1IIi - OoOO00O
 if 54 - 54: OoOO00O - O0 % O0O0O
iIiiiI1IiI1I1 = xbmcaddon . Addon ( id = 'plugin.program.originwizard' )
zip = iIiiiI1IiI1I1 . getSetting ( 'zip' )
Ooii11i11i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.program.originwizard/Generated/' ) )
Ooo0o00o0o = 'TEST'
IiIIIIIi = Ooii11i11i1 + Ooo0o00o0o
II1IIiiIiI = xbmcgui . Dialog ( )
o0oO0 = xbmc . translatePath ( 'special://home/' )
oOOoO0 = xbmc . translatePath ( os . path . join ( zip ) )
iiIIIII1i1iI = xbmcgui . DialogProgress ( )
if 11 - 11: i1IIi % i11iIiiIii - i1IIi * I11iii1Ii
def i1I11IiI1iiII ( ) :
 OOO = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  II1IIiiIiI . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  iIiiiI1IiI1I1 . openSettings ( sys . argv [ 0 ] )
  if 91 - 91: II11i1iIiII1 % II11i1iIiII1
  if 7 - 7: OoOO00O / o0IiIIIiIi11i1 / i11iIiiIii
def IIIIIo0ooOoO000oO ( url ) :
 iiIIIII1i1iI . create ( "[COLOR=white]Origin[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OOo , i1i11I1I1iii1 , I1iii11 in os . walk ( url ) :
  for file in I1iii11 :
   if file . endswith ( ".xml" ) :
    iiIIIII1i1iI . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooo0O = open ( ( os . path . join ( OOo , file ) ) ) . read ( )
    iII1iii = ooo0O . replace ( o0oO0 , 'special://home/' )
    I1IIII1i = open ( ( os . path . join ( OOo , file ) ) , mode = 'w' )
    I1IIII1i . write ( str ( iII1iii ) )
    I1IIII1i . close ( )
    if 12 - 12: O0O0O
class O0iII1 ( ) :
 if 27 - 27: iii11I111 . i1IiIIIII + I11iii1Ii / iIii1I11I1II1 % OoOO00O . II11i1iIiII1
 def __init__ ( self , extra_build_name , extra_build_zip , extra_build_image , extra_build_fanart , extra_build_description , build_name , build_zip , build_image , build_fanart , build_description , save_path , txt_file_name , plugin_name , clean_plugin_name , build_url , clean_build_url , py_file_name , addon_file_name , action ) :
  self . build_name = ''
  self . build_zip = ''
  self . build_image = ''
  self . build_fanart = ''
  self . build_description = ''
  self . extra_build_name = ''
  self . extra_build_zip = ''
  self . extra_build_image = ''
  self . extra_build_fanart = ''
  self . extra_build_description = ''
  self . save_path = IiIIIIIi
  self . txt_file_name = 'wizard.txt'
  self . plugin_name = ''
  self . clean_plugin_name = ''
  self . build_url = ''
  self . clean_build_url = ( build_url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  self . py_file_name = 'default.py'
  self . addon_file_name = 'addon.xml'
  self . action = action
  self . keepAlive = True ;
  if self . action == 'textFile' :
   self . txt_file_inputs ( )
  else : pass
  if 14 - 14: IIIii1II1II + o0IiIIIiIi11i1 - OoOO00O / O0 . O00Oo000ooO0
 def Wizard_Inputs ( self ) :
  self . plugin_name = II1IIiiIiI . input ( '[COLOR red]Input Name of Wizard[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . Wizard_name = self . plugin_name . lower ( )
  self . clean_plugin_name = ( self . Wizard_name ) . replace ( ' ' , '' )
  if 45 - 45: O00Oo000ooO0
  self . generate_wizard_py ( )
  if 83 - 83: I11iii1Ii . OoooooooOO
  if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IIiI1I / i11iIiiIii
  if 62 - 62: iii11I111 / o0IiIIIiIi11i1
 def txt_file_inputs ( self ) :
  i1I11IiI1iiII ( )
  self . build_name = II1IIiiIiI . input ( '[COLOR red] Input Build Name[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_zip = II1IIiiIiI . input ( '[COLOR red] Input Builds Online Zip Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_image = II1IIiiIiI . input ( '[COLOR red] Input Builds Online Image Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_fanart = II1IIiiIiI . input ( '[COLOR red] Input Builds Online Background Image[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_description = II1IIiiIiI . input ( '[COLOR red] Input Builds Description[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  iiIIIII1i1iI . create ( "[COLOR=white]Origin[/COLOR]" , "Creating Text File" , '' , 'Please Wait' )
  if 7 - 7: OoooooooOO . IIiI1I
  self . Checker ( )
  if 53 - 53: Ii1i111I % Ii1i111I * OOOooOooo00O0 + I11iii1Ii
 def Checker ( self ) :
  if 92 - 92: OoooooooOO + i1IIi / Ii1i111I * O0
  o0O00OooOOOOO = OO0O0 ( o0OO00 ( 'aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC9QaGVub21lbmFsL2J1aWxkc2VjdXJldXJscy50eHQ=' ) )
  I11I11 = re . compile ( "<url=>(.+?)</url>" ) . findall ( o0O00OooOOOOO )
  for o000O0O in I11I11 :
   O00oOo00o0o = o000O0O
   O00oO0 = OO0O0 ( O00oOo00o0o )
   O0Oo00OoOo = re . compile ( "<url=>(.+?)</url>" ) . findall ( O00oO0 )
   for ii1ii111 in O0Oo00OoOo :
    if self . extra_build_zip == ii1ii111 :
     i11111I1I ( )
    elif self . build_zip == ii1ii111 :
     i11111I1I ( )
    else :
     self . generate_wizard_text ( )
     if 11 - 11: OoooooooOO . O00Oo000ooO0
 def generate_wizard_text ( self ) :
  if 80 - 80: OoooooooOO - O0O0O * Ii1i111I * o0IiIIIiIi11i1 / II11iII / O0O0O
  I1I11iI11iI1i = os . path . join ( iIi1ii1I1 , self . txt_file_name )
  oo0o0O0Oooooo = open ( I1I11iI11iI1i , "w+" )
  if 1 - 1: II11i1iIiII1 % I11iii1Ii * OoOo
  oo0o0O0Oooooo . write ( r'name=<' + self . build_name + '>\n' )
  oo0o0O0Oooooo . write ( r'url=<' + self . build_zip + '>\n' )
  oo0o0O0Oooooo . write ( r'img=<' + self . build_image + '>\n' )
  oo0o0O0Oooooo . write ( r'fanart=<' + self . build_fanart + '>\n' )
  oo0o0O0Oooooo . write ( r'description=<' + self . build_description + '>\n' )
  oo0o0O0Oooooo . close ( )
  if self . keepAlive == True :
   II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( "Is There Any More Builds?" , 'Would You like to add another build into txt file?' , '' , 'This Will also show in your wizard when generated' , yeslabel = 'Yes' , nolabel = 'No' )
   if II11iIiIIIiI == 1 :
    self . txt_extra_file_inputs ( )
    print "Generate Wizard Text"
   elif II11iIiIIIiI == 0 :
    II1IIiiIiI . ok ( "[COLOR=white]Origin[/COLOR]" , "Your Wizard Will Now Be Generated" , '' , '' )
    print "Wizard Inputs"
    self . Wizard_Inputs ( )
  else : pass
  if 55 - 55: I11iii1Ii
 def txt_extra_file_inputs ( self ) :
  self . extra_build_name = II1IIiiIiI . input ( '[COLOR red] Input Build Name[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_zip = II1IIiiIiI . input ( '[COLOR red] Input Builds Online Zip Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_image = II1IIiiIiI . input ( '[COLOR red] Input Builds Online Image Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_fanart = II1IIiiIiI . input ( '[COLOR red] Input Builds Online Background Image[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_description = II1IIiiIiI . input ( '[COLOR red] Input Builds Description[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_generate_wizard_text ( )
  print "Generating Wizard 1"
  if 87 - 87: OoooooooOO % OoOO00O . II11iII / II11i1iIiII1
 def extra_generate_wizard_text ( self ) :
  if 8 - 8: i1IiIIIII + OOOooOooo00O0
  oOOo0o0oo = os . path . join ( iIi1ii1I1 , self . txt_file_name )
  i11iiiiI1i = open ( oOOo0o0oo , "w+" )
  if 37 - 37: O0O0O / OoooooooOO - i11iIiiIii
  i11iiiiI1i . write ( r'name=<' + self . build_name + '>\n' )
  i11iiiiI1i . write ( r'url=<' + self . build_zip + '>\n' )
  i11iiiiI1i . write ( r'img=<' + self . build_image + '>\n' )
  i11iiiiI1i . write ( r'fanart=<' + self . build_fanart + '>\n' )
  i11iiiiI1i . write ( r'description=<' + self . build_description + '>\n' )
  i11iiiiI1i . close ( )
  if self . keepAlive == True :
   II11iIiIIIiI = xbmcgui . Dialog ( ) . yesno ( "Is There Any More Builds?" , 'Would You like to add another build into txt file?' , '' , 'This Will also show in your wizard when generated' , yeslabel = 'Yes' , nolabel = 'No' )
   if II11iIiIIIiI == 1 :
    self . txt_extra_file_inputs ( )
    print "Generate Wizard Text"
   elif II11iIiIIIiI == 0 :
    II1IIiiIiI . ok ( "[COLOR=white]Origin[/COLOR]" , "Your Wizard Will Now Be Generated" , '' , '' )
    print "Wizard Inputs"
    self . Wizard_Inputs ( )
  else : pass
  if 18 - 18: OoOO00O . II11iII
 def generate_wizard_py ( self ) :
  if 40 - 40: O0 - OoooooooOO - IIiI1I
  if 37 - 37: I11iii1Ii / iiiIi1i1I / O0
  OOOO00OO0O0 = os . path . join ( self . save_path , self . py_file_name )
  i1I111Ii1i11 = open ( OOOO00OO0O0 , "w+" )
  if 81 - 81: iii11I111
  if 99 - 99: IIIii1II1II * iiiIi1i1I * O00Oo000ooO0
  i1I111Ii1i11 . write ( r'import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os' + '\n' )
  i1I111Ii1i11 . write ( r'import shutil' + '\n' )
  i1I111Ii1i11 . write ( r'import urllib2,urllib' + '\n' )
  i1I111Ii1i11 . write ( r'import re,base64' + '\n' )
  i1I111Ii1i11 . write ( r'import extract' + '\n' )
  i1I111Ii1i11 . write ( r'import downloader' + '\n' )
  i1I111Ii1i11 . write ( r'import time' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r"Decode = base64.decodestring" + "\n" )
  i1I111Ii1i11 . write ( r"WIPE_ADDON 	 =  xbmc.translatePath(os.path.join('special://home/addons/plugin.program.originwizard/'))" + "\n" )
  i1I111Ii1i11 . write ( r"ADDONS         =  xbmc.translatePath(os.path.join('special://home/addons/plugin.video." + self . clean_plugin_name + "'))" + "\n" )
  i1I111Ii1i11 . write ( r"text_file_path = ADDONS + '/resources/'" + "\n" )
  i1I111Ii1i11 . write ( r"USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'" + '\n' )
  i1I111Ii1i11 . write ( r"base='" + self . plugin_name + '\'' + '\n' )
  i1I111Ii1i11 . write ( r"ADDON=xbmcaddon.Addon(id='plugin.video." + self . clean_plugin_name + '\')' + '\n' )
  i1I111Ii1i11 . write ( r'Dialog = xbmcgui.Dialog()' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'VERSION = "1.0.0"' + '\n' )
  i1I111Ii1i11 . write ( r"PATH = '" + self . clean_plugin_name + '\'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'def CATEGORIES()' + ':\n' )
  i1I111Ii1i11 . write ( r"    py_complete_name = os.path.join(text_file_path,'wizard.txt')" + '\n' )
  i1I111Ii1i11 . write ( r"    print_default_file = open(py_complete_name," r")" + '\n' )
  i1I111Ii1i11 . write ( r'    file = print_default_file.read()' + '\n' )
  i1I111Ii1i11 . write ( r"    match = re.compile('name=<(.+?)>.+?url=<(.+?)>.+?img=<(.+?)>.+?fanart=<(.+?)>.+?description=<(.+?)>',re.DOTALL).findall(file)" + "\n" )
  i1I111Ii1i11 . write ( r'    print_default_file.close()' + '\n' )
  i1I111Ii1i11 . write ( r'    for name,url,iconimage,fanart,description in match:' + '\n' )
  i1I111Ii1i11 . write ( r'        NAME = name' + '\n' )
  i1I111Ii1i11 . write ( r'        URL = url' + '\n' )
  i1I111Ii1i11 . write ( r"        IMAGE = iconimage" + '\n' )
  i1I111Ii1i11 . write ( r"        FANART = fanart" + "\n" )
  i1I111Ii1i11 . write ( r"        DESC = description" + "\n" )
  i1I111Ii1i11 . write ( r"        HTML = OPEN_URL(Decode('aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC9QaGVub21lbmFsL2J1aWxkc2VjdXJldXJscy50eHQ='))" + "\n" )
  i1I111Ii1i11 . write ( r"        match2 = re.compile('<url=>(.+?)</url>').findall(HTML)" + "\n" )
  i1I111Ii1i11 . write ( r"        for url2 in match2:" + "\n" )
  i1I111Ii1i11 . write ( r"            HTML2 = OPEN_URL(str(url2))" + "\n" )
  i1I111Ii1i11 . write ( r"            match3 = re.compile('<url=>(.+?)</url>').findall(HTML2)" + "\n" )
  i1I111Ii1i11 . write ( r"            for url3 in match3:" + "\n" )
  i1I111Ii1i11 . write ( r"                if URL == url3:" + "\n" )
  i1I111Ii1i11 . write ( r"                    Wipe_Wizard()" + "\n" )
  i1I111Ii1i11 . write ( r"                elif url3 == 'kill all':" + "\n" )
  i1I111Ii1i11 . write ( r"                    Wipe_Wizard()" + "\n" )
  i1I111Ii1i11 . write ( r"        else:" + "\n" )
  i1I111Ii1i11 . write ( r'            addDir(NAME,URL,1,IMAGE,FANART,DESC)' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'def Wipe_Wizard():' + '\n' )
  i1I111Ii1i11 . write ( r"    Dialog.ok('[COLOR=white]Naughty Naughty[/COLOR]', 'You are the weakest link goodbye', '','')" + "\n" )
  i1I111Ii1i11 . write ( r"    addon_complete_name = os.path.join(WIPE_ADDON,'default.py')" + "\n" )
  i1I111Ii1i11 . write ( r'    print_byebye_file = open(addon_complete_name,"w+")' + '\n' )
  i1I111Ii1i11 . write ( r"    print_byebye_file.write(r'This Build Can NOT be copied')" + "\n" )
  i1I111Ii1i11 . write ( r'    print_byebye_file.close()' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r"    addons_complete_name = os.path.join(ADDONS,'default.py')" + "\n" )
  i1I111Ii1i11 . write ( r'    print_byebye_addon_file = open(addons_complete_name,"w+")' + '\n' )
  i1I111Ii1i11 . write ( r"    print_byebye_addon_file.write(r'This Build Can NOT be copied')" + "\n" )
  i1I111Ii1i11 . write ( r"    print_byebye_addon_file.close()" + "\n" )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'def OPEN_URL(url):' + '\n' )
  i1I111Ii1i11 . write ( r'    req = urllib2.Request(url)' + '\n' )
  i1I111Ii1i11 . write ( r"    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')" + '\n' )
  i1I111Ii1i11 . write ( r'    response = urllib2.urlopen(req)' + '\n' )
  i1I111Ii1i11 . write ( r'    link=response.read()' + '\n' )
  i1I111Ii1i11 . write ( r'    response.close()' + '\n' )
  i1I111Ii1i11 . write ( r'    return link' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'def wizard(name,url,description):' + '\n' )
  i1I111Ii1i11 . write ( r"    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))" + '\n' )
  i1I111Ii1i11 . write ( r'    dp = xbmcgui.DialogProgress()' + '\n' )
  i1I111Ii1i11 . write ( r'    dp.create("Your Build Is Downloading","This May Take Several Minutes","", "")' + '\n' )
  i1I111Ii1i11 . write ( r"    lib=os.path.join(path, name+'.zip')" + '\n' )
  i1I111Ii1i11 . write ( r'    try:' + '\n' )
  i1I111Ii1i11 . write ( r'       os.remove(lib)' + '\n' )
  i1I111Ii1i11 . write ( r'    except:' + '\n' )
  i1I111Ii1i11 . write ( r'       pass' + '\n' )
  i1I111Ii1i11 . write ( r'    downloader.download(url, lib, dp)' + '\n' )
  i1I111Ii1i11 . write ( r"    addonfolder = xbmc.translatePath(os.path.join('special://','home'))" + '\n' )
  i1I111Ii1i11 . write ( r'    time.sleep(2)' + '\n' )
  i1I111Ii1i11 . write ( r'    dp.update(0,"", "Installing Your Build Please Wait")' + '\n' )
  i1I111Ii1i11 . write ( r"    print '======================================='" + '\n' )
  i1I111Ii1i11 . write ( r'    print addonfolder' + '\n' )
  i1I111Ii1i11 . write ( r"    print '======================================='" + '\n' )
  i1I111Ii1i11 . write ( r'    extract.all(lib,addonfolder,dp)' + '\n' )
  i1I111Ii1i11 . write ( r'    dialog = xbmcgui.Dialog()' + '\n' )
  i1I111Ii1i11 . write ( r'    dialog.ok("Your Media Centre", "[COLORred]Please Force Close Kodi To Take Effect If Pc Exit Task In TaskManager[/COLOR]","[COLORblue]Wizard Brought To You By Origin[/COLOR]")' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'def addDir(name,url,mode,iconimage,fanart,description):' + '\n' )
  i1I111Ii1i11 . write ( r'        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)' + '\n' )
  i1I111Ii1i11 . write ( r'        ok=True' + '\n' )
  i1I111Ii1i11 . write ( r'        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)' + '\n' )
  i1I111Ii1i11 . write ( r'        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )' + '\n' )
  i1I111Ii1i11 . write ( r'        liz.setProperty( "Fanart_Image", fanart )' + '\n' )
  i1I111Ii1i11 . write ( r'        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)' + '\n' )
  i1I111Ii1i11 . write ( r'        return ok' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'def get_params():' + '\n' )
  i1I111Ii1i11 . write ( r'        param=[]' + '\n' )
  i1I111Ii1i11 . write ( r'        paramstring=sys.argv[2]' + '\n' )
  i1I111Ii1i11 . write ( r'        if len(paramstring)>=2:' + '\n' )
  i1I111Ii1i11 . write ( r'                params=sys.argv[2]' + '\n' )
  i1I111Ii1i11 . write ( r"                cleanedparams=params.replace('?','')" + '\n' )
  i1I111Ii1i11 . write ( r"                if (params[len(params)-1]=='/'):" + '\n' )
  i1I111Ii1i11 . write ( r'                        params=params[0:len(params)-2]' + '\n' )
  i1I111Ii1i11 . write ( r"                pairsofparams=cleanedparams.split('&')" + '\n' )
  i1I111Ii1i11 . write ( r'                param={}' + '\n' )
  i1I111Ii1i11 . write ( r'                for i in range(len(pairsofparams)):' + '\n' )
  i1I111Ii1i11 . write ( r'                        splitparams={}' + '\n' )
  i1I111Ii1i11 . write ( r"                        splitparams=pairsofparams[i].split('=')" + '\n' )
  i1I111Ii1i11 . write ( r'                        if (len(splitparams))==2:' + '\n' )
  i1I111Ii1i11 . write ( r'                                param[splitparams[0]]=splitparams[1]' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'        return param' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'params=get_params()' + '\n' )
  i1I111Ii1i11 . write ( r'url=None' + '\n' )
  i1I111Ii1i11 . write ( r'name=None' + '\n' )
  i1I111Ii1i11 . write ( r'mode=None' + '\n' )
  i1I111Ii1i11 . write ( r'iconimage=None' + '\n' )
  i1I111Ii1i11 . write ( r'fanart=None' + '\n' )
  i1I111Ii1i11 . write ( r'description=None' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'try:' + '\n' )
  i1I111Ii1i11 . write ( r'        url=urllib.unquote_plus(params["url"])' + '\n' )
  i1I111Ii1i11 . write ( r'except:' + '\n' )
  i1I111Ii1i11 . write ( r'        pass' + '\n' )
  i1I111Ii1i11 . write ( r'try:' + '\n' )
  i1I111Ii1i11 . write ( r'        name=urllib.unquote_plus(params["name"])' + '\n' )
  i1I111Ii1i11 . write ( r'except:' + '\n' )
  i1I111Ii1i11 . write ( r'        pass' + '\n' )
  i1I111Ii1i11 . write ( r'try:' + '\n' )
  i1I111Ii1i11 . write ( r'        iconimage=urllib.unquote_plus(params["iconimage"])' + '\n' )
  i1I111Ii1i11 . write ( r'except:' + '\n' )
  i1I111Ii1i11 . write ( r'        pass' + '\n' )
  i1I111Ii1i11 . write ( r'try:' + '\n' )
  i1I111Ii1i11 . write ( r'        mode=int(params["mode"])' + '\n' )
  i1I111Ii1i11 . write ( r'except:' + '\n' )
  i1I111Ii1i11 . write ( r'        pass' + '\n' )
  i1I111Ii1i11 . write ( r'try:' + '\n' )
  i1I111Ii1i11 . write ( r'        fanart=urllib.unquote_plus(params["fanart"])' + '\n' )
  i1I111Ii1i11 . write ( r'except:' + '\n' )
  i1I111Ii1i11 . write ( r'        pass' + '\n' )
  i1I111Ii1i11 . write ( r'try:' + '\n' )
  i1I111Ii1i11 . write ( r'        description=urllib.unquote_plus(params["description"])' + '\n' )
  i1I111Ii1i11 . write ( r'except:' + '\n' )
  i1I111Ii1i11 . write ( r'        pass' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r"print str(PATH)+': '+str(VERSION)" + '\n' )
  i1I111Ii1i11 . write ( r'print "Mode: "+str(mode)' + '\n' )
  i1I111Ii1i11 . write ( r'print "URL: "+str(url)' + '\n' )
  i1I111Ii1i11 . write ( r'print "Name: "+str(name)' + '\n' )
  i1I111Ii1i11 . write ( r'print "IconImage: "+str(iconimage)' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'def setView(content, viewType):' + '\n' )
  i1I111Ii1i11 . write ( r'    # set content type so library shows more views and info' + '\n' )
  i1I111Ii1i11 . write ( r'    if content:' + '\n' )
  i1I111Ii1i11 . write ( r'        xbmcplugin.setContent(int(sys.argv[1]), content)' + '\n' )
  i1I111Ii1i11 . write ( r"    if ADDON.getSetting('auto-view')=='true':" + '\n' )
  i1I111Ii1i11 . write ( '        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'if mode==None or url==None or len(url)<1:' + '\n' )
  i1I111Ii1i11 . write ( r'        CATEGORIES()' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'elif mode==1:' + '\n' )
  i1I111Ii1i11 . write ( r'        wizard(name,url,description)' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'' + '\n' )
  i1I111Ii1i11 . write ( r'xbmcplugin.endOfDirectory(int(sys.argv[1]))' + '\n' )
  print "Generate Wizard PY Before Print"
  i1I111Ii1i11 . close ( )
  print "Generate Wizard PY After Print"
  self . addon_xml ( )
  if 92 - 92: OoOo
 def addon_xml ( self ) :
  if 40 - 40: I11iii1Ii / IIiI1I
  OOOoO000 = os . path . join ( self . save_path , self . addon_file_name )
  oOOOO = open ( OOOoO000 , "w+" )
  if 49 - 49: iiiIi1i1I . IIIii1II1II . i11iIiiIii % IIiI1I
  if 34 - 34: O00Oo000ooO0 % IIiI1I
  oOOOO . write ( r'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + '\n' )
  oOOOO . write ( r'<addon id="plugin.video.' + self . clean_plugin_name + '" name="' + self . plugin_name + '" version="1.0.0" provider-name="Origin">' + '\n' )
  oOOOO . write ( r'  <requires>' + '\n' )
  oOOOO . write ( r'    <import addon="xbmc.python" version="2.1.0"/>' + '\n' )
  oOOOO . write ( r'  </requires>' + '\n' )
  oOOOO . write ( r'  <extension point="xbmc.python.pluginsource" library="default.py">' + '\n' )
  oOOOO . write ( r'        <provides>video executable</provides>' + '\n' )
  oOOOO . write ( r'  </extension>' + '\n' )
  oOOOO . write ( r'  <extension point="xbmc.addon.metadata">' + '\n' )
  oOOOO . write ( r'    <summary lang="en">An installer for ' + self . plugin_name + '</summary>' + '\n' )
  oOOOO . write ( r'    <description lang="en">Generated by Origins mod of original Wizard template for ' + self . plugin_name + '</description>' + '\n' )
  oOOOO . write ( r'    <platform>all</platform>' + '\n' )
  oOOOO . write ( r'  </extension>' + '\n' )
  oOOOO . write ( r'</addon>' + '\n' )
  print "Addon XML Before Print"
  oOOOO . close ( )
  print "Addon XML After Print"
  self . Delay ( )
  if 3 - 3: iiiIi1i1I / O0O0O + IIiI1I . II11i1iIiII1 . iii11I111
 def Delay ( self ) :
  os . rename ( Ooii11i11i1 + 'TEST' , Ooii11i11i1 + 'plugin.video.' + self . clean_plugin_name )
  iiIIIII1i1iI . create ( "[COLORwhite]Origin[/COLOR]" , "Writing Files" , '' , 'Please Wait' )
  time . sleep ( 1 )
  print "Delay Sleeper"
  self . Backup_Wizard ( )
  if 83 - 83: IIIii1II1II + OoooooooOO
 def Backup_Wizard ( self ) :
  if 22 - 22: Ii1i111I % OoOO00O * OoooooooOO - OOOooOooo00O0 / iIii1I11I1II1
  i1I11IiI1iiII ( )
  OoOO00 = xbmc . translatePath ( os . path . join ( oOOoO0 , 'plugin.video.' + self . clean_plugin_name + '.zip' ) )
  IIiiIIi1 = Ooii11i11i1
  iiIIIII1i1iI . create ( "[COLOR=white]Origin[/COLOR]" , "Backing Up" , '' , 'Please Wait' )
  o00ooO00O = zipfile . ZipFile ( OoOO00 , 'w' , zipfile . ZIP_DEFLATED )
  oo00o0 = len ( IIiiIIi1 )
  OooOOOOoO00OoOO = [ ]
  oOooo0O0o = [ ]
  for ooooooO0oo , i1i11I1I1iii1 , I1iii11 in os . walk ( IIiiIIi1 ) :
   for file in I1iii11 :
    oOooo0O0o . append ( file )
  Oo000 = len ( oOooo0O0o )
  for ooooooO0oo , i1i11I1I1iii1 , I1iii11 in os . walk ( IIiiIIi1 ) :
   for file in I1iii11 :
    OooOOOOoO00OoOO . append ( file )
    O00O0oOOo = len ( OooOOOOoO00OoOO ) / float ( Oo000 ) * 100
    iiIIIII1i1iI . update ( int ( O00O0oOOo ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    O0oO = os . path . join ( ooooooO0oo , file )
    if not 'temp' in i1i11I1I1iii1 :
     if not 'plugin.video.originwizard' in i1i11I1I1iii1 :
      import time
      OO000oooo0 = '01/01/1980'
      oOoO0o0ooo = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( O0oO ) ) )
      if oOoO0o0ooo > OO000oooo0 :
       o00ooO00O . write ( O0oO , O0oO [ oo00o0 : ] )
  self . keepAlive = False
  print "Backup Wizard"
  o00ooO00O . close ( )
  iiIIIII1i1iI . close ( )
  os . rename ( Ooii11i11i1 + 'plugin.video.' + self . clean_plugin_name , Ooii11i11i1 + 'TEST' )
  II1IIiiIiI . ok ( "[COLOR=white]Origin[/COLOR]" , "Your Wizard Is Now Generated" , '' , '' )
  if 86 - 86: o0IiIIIiIi11i1 * O0 * IIiI1I
Ooo0oo = O0iII1 ( '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
if 41 - 41: I11iii1Ii * i1IiIIIII / I11iii1Ii % IIIii1II1II
def OO0O0 ( url ) :
 oOo0 = urllib2 . Request ( url )
 Ii = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
 oO0oOOO0Ooo = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
 i1i1I = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
 IiIIi1iII11I1Ii1 = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
 oOo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1iI = urllib2 . urlopen ( oOo0 )
 iIIIiIi = i1iI . read ( )
 i1iI . close ( )
 return iIIIiIi
 if 92 - 92: i1IiIIIII / i1IiIIIII . o0IiIIIiIi11i1
 if 17 - 17: i11iIiiIii - iiiIi1i1I * OOOooOooo00O0
def i11111I1I ( ) :
 if 5 - 5: O0O0O - O0O0O . OoOo + I11iii1Ii - O0O0O . IIIii1II1II
 II1IIiiIiI . ok ( "[COLOR=white]Naughty Naughty[/COLOR]" , "You are the weakest link goodbye" , '' , '' )
 OOOoO000 = os . path . join ( o0 , 'default.py' )
 IiIi1i1ii = open ( OOOoO000 , "w+" )
 if 11 - 11: iiiIi1i1I / OOOooOooo00O0
 IiIi1i1ii . write ( r'This Build Can NOT be Copied' )
 if 21 - 21: i11iIiiIii / i1IIi + II11iII * O0O0O . O00Oo000ooO0
def OoO ( content , viewType ) :
 if 73 - 73: iiiIi1i1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if iIiiiI1IiI1I1 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % iIiiiI1IiI1I1 . getSetting ( viewType ) )
  if 24 - 24: I11iii1Ii / OoooooooOO . iiiIi1i1I . II11iII % O0 % Ii1i111I
if IiIi1I1 == None or o000O0O == None or len ( o000O0O ) < 1 :
 oo0oOo ( )
elif IiIi1I1 == 'addon_removal_menu' : i1I1iI ( )
elif IiIi1I1 == 'addonfix' : addonfix . fixes ( )
elif IiIi1I1 == 'addonfixes' : Oo0OoO00oOO0o ( )
elif IiIi1I1 == 'addonmenu' : Addon_Menu ( )
elif IiIi1I1 == 'addon_settings' : ii111 ( )
elif IiIi1I1 == 'backup' : BACKUP ( )
elif IiIi1I1 == 'backup_option' : communitybuilds . Backup_Option ( )
elif IiIi1I1 == 'backup_restore' : ii111111I1iII ( )
elif IiIi1I1 == 'adultmenu' : AdultMenu ( )
elif IiIi1I1 == 'buildmenu' : o0o0O0O00oOOo ( )
elif IiIi1I1 == 'categories' : oo0oOo ( )
elif IiIi1I1 == 'clear_cache' : O0OOO ( )
elif IiIi1I1 == 'community_backup' : communitybuilds . Community_Backup ( )
elif IiIi1I1 == 'community_menu' : communitybuilds . Community_Menu ( o000O0O , Oo0o0O00 )
elif IiIi1I1 == 'description' : communitybuilds . Description ( oo0OooOOo0 , o000O0O , I11iiii , II1iIi11 , ooo00Ooo , I1i1i1iii , iI1i11 , IIIIiIiIi1 , ii1I1i11 , OOoOO0ooo , IIIIiii1IIii , OOoOooOoOOOoo , I11iiiiI1i , OooooOoooO )
elif IiIi1I1 == 'fix_special' : communitybuilds . Fix_Special ( o000O0O )
elif IiIi1I1 == 'genres' : Genres ( o000O0O )
elif IiIi1I1 == 'grab_addons' : addons . Grab_Addons ( o000O0O )
elif IiIi1I1 == 'grab_builds_premium' : communitybuilds . Grab_Builds_Premium ( o000O0O )
elif IiIi1I1 == 'guisettingsfix' : communitybuilds . GUI_Settings_Fix ( o000O0O , OooOo0oo0O0o00O )
elif IiIi1I1 == 'guisettings' : guisettings ( )
elif IiIi1I1 == 'hide_passwords' : extras . Hide_Passwords ( )
elif IiIi1I1 == 'LocalGUIDialog' : communitybuilds . Local_GUI_Dialog ( )
elif IiIi1I1 == 'remove_addon_data' : III1IiiI ( )
elif IiIi1I1 == 'remove_addons' : extras . Remove_Addons ( o000O0O )
elif IiIi1I1 == 'remove_build' : extras . Remove_Build ( )
elif IiIi1I1 == 'remove_crash_logs' : IIIII11I1IiI ( )
elif IiIi1I1 == 'remove_packages' : IIi ( )
elif IiIi1I1 == 'remove_textures' : o0o ( )
elif IiIi1I1 == 'restore' : extras . RESTORE ( )
elif IiIi1I1 == 'restore_backup' : communitybuilds . Restore_Backup_XML ( oo0OooOOo0 , o000O0O , I1i1i1iii )
elif IiIi1I1 == 'restore_local_CB' : communitybuilds . Restore_Local_Community ( )
elif IiIi1I1 == 'restore_local_gui' : communitybuilds . Restore_Local_GUI ( )
elif IiIi1I1 == 'restore_option' : communitybuilds . Restore_Option ( )
elif IiIi1I1 == 'restore_zip' : communitybuilds . Restore_Zip_File ( o000O0O )
elif IiIi1I1 == 'restore_community' : communitybuilds . Restore_Community ( oo0OooOOo0 , o000O0O , Oo0o0O00 , I1i1i1iii , IIIIiIiIi1 , oOIIiIi )
elif IiIi1I1 == 'showinfo' : communitybuilds . Show_Info ( o000O0O )
elif IiIi1I1 == 'SortBy' : extras . Sort_By ( BuildURL , type )
elif IiIi1I1 == 'text_guide' : news . Text_Guide ( oo0OooOOo0 , o000O0O )
elif IiIi1I1 == 'tools' : ii1 ( )
elif IiIi1I1 == 'unhide_passwords' : extras . Unhide_Passwords ( )
elif IiIi1I1 == 'update' : addons . Update_Repo ( )
elif IiIi1I1 == 'uploadlog' : extras . Upload_Log ( )
elif IiIi1I1 == 'user_info' : Show_User_Info ( )
elif IiIi1I1 == 'wipetools' : OOoO ( )
elif IiIi1I1 == 'xbmcversion' : extras . XBMC_Version ( o000O0O )
elif IiIi1I1 == 'wipe_xbmc' : oOO0O00oO0Ooo ( )
elif IiIi1I1 == 'wizard' : IIiIiI ( oo0OooOOo0 , o000O0O , I1i1i1iii )
elif IiIi1I1 == 'Merlin' : oO0O00OoOO0 ( )
elif IiIi1I1 == 'Text_Gen' : O0iII1 ( '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , 'textFile' )
elif IiIi1I1 == 'How_To' : o00o0 ( )
elif IiIi1I1 == 'Addon_Cat' : iIi1i1iIi1iI ( )
elif IiIi1I1 == 'Addon' : IIIiI11ii1I ( o000O0O )
elif IiIi1I1 == 'Addon_Extract' : iII111i ( o000O0O , oo0OooOOo0 )
elif IiIi1I1 == 'Repo' : OooO0oo ( o000O0O )
elif IiIi1I1 == 'Search_Addons' : iI ( )
elif IiIi1I1 == 'Addons_Menu' : O00 ( )
elif IiIi1I1 == 'fastupdatemenu' : iiI11i1II ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
