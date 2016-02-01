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
oo = 'special://home/resources/art/' + os . sep
i1iII1IiiIiI1 = xbmcaddon . Addon ( id = 'plugin.program.originwizard' )
iIiiiI1IiI1I1 = 'plugin.program.originwizard'
o0OoOoOO00 = "Origin Wizard"
I11i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
O0O = os . path . join ( I11i , iIiiiI1IiI1I1 , 'resources' , 'art' ) + os . sep
zip = i1iII1IiiIiI1 . getSetting ( 'zip' )
Oo = i1iII1IiiIiI1 . getSetting ( 'localcopy' )
I1ii11iIi11i = i1iII1IiiIiI1 . getSetting ( 'private' )
I1IiI = i1iII1IiiIiI1 . getSetting ( 'reseller' )
o0OOO = i1iII1IiiIiI1 . getSetting ( 'resellername' )
iIiiiI = i1iII1IiiIiI1 . getSetting ( 'resellerid' )
Iii1ii1II11i = i1iII1IiiIiI1 . getSetting ( 'mastercopy' )
iI111iI = i1iII1IiiIiI1 . getSetting ( 'username' )
IiII = i1iII1IiiIiI1 . getSetting ( 'password' )
iI1Ii11111iIi = i1iII1IiiIiI1 . getSetting ( 'login' )
i1i1II = i1iII1IiiIiI1 . getSetting ( 'trcheck' )
O0oo0OO0 = xbmcgui . Dialog ( )
I1i1iiI1 = xbmcgui . DialogProgress ( )
iiIIIII1i1iI = xbmc . translatePath ( 'special://home/' )
o0oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
oo00 = xbmc . translatePath ( os . path . join ( 'special://home/media' , '' ) )
o00 = xbmc . translatePath ( os . path . join ( o0oO0 , 'autoexec.py' ) )
Oo0oO0ooo = xbmc . translatePath ( os . path . join ( o0oO0 , 'autoexec_bak.py' ) )
o0oOoO00o = xbmc . translatePath ( os . path . join ( o0oO0 , 'addon_data' ) )
i1 = xbmc . translatePath ( os . path . join ( o0oO0 , 'playlists' ) )
oOOoo00O0O = xbmc . translatePath ( os . path . join ( o0oO0 , 'Database' ) )
i1111 = xbmc . translatePath ( os . path . join ( o0oO0 , 'Thumbnails' ) )
I11i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
i11 = xbmc . translatePath ( os . path . join ( I11i , iIiiiI1IiI1I1 , 'default.py' ) )
I11 = xbmc . translatePath ( os . path . join ( I11i , iIiiiI1IiI1I1 , 'fanart.jpg' ) )
Oo0o0000o0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.genesis/favourites.db' ) )
oOo0oooo00o = os . path . join ( o0oO0 , 'guisettings.xml' )
oO0o0o0ooO0oO = xbmc . translatePath ( os . path . join ( o0oO0 , 'guisettings.xml' ) )
oo0o0O00 = xbmc . translatePath ( os . path . join ( o0oO0 , 'guifix.xml' ) )
oO = xbmc . translatePath ( os . path . join ( o0oO0 , 'install.xml' ) )
i1iiIIiiI111 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
oooOOOOO = xbmc . translatePath ( os . path . join ( o0oO0 , 'favourites.xml' ) )
i1iiIII111ii = xbmc . translatePath ( os . path . join ( o0oO0 , 'sources.xml' ) )
i1iIIi1 = xbmc . translatePath ( os . path . join ( o0oO0 , 'advancedsettings.xml' ) )
ii11iIi1I = xbmc . translatePath ( os . path . join ( o0oO0 , 'profiles.xml' ) )
iI111I11I1I1 = xbmc . translatePath ( os . path . join ( o0oO0 , 'RssFeeds.xml' ) )
OOooO0OOoo = xbmc . translatePath ( os . path . join ( o0oO0 , 'keymaps' , 'keyboard.xml' ) )
iIii1 = xbmc . translatePath ( os . path . join ( zip ) )
oOOoO0 = xbmc . translatePath ( os . path . join ( iIii1 , 'Community Builds' , '' ) )
O0OoO000O0OO = xbmc . translatePath ( os . path . join ( o0oOoO00o , iIiiiI1IiI1I1 , 'cookiejar' ) )
iiI1IiI = xbmc . translatePath ( os . path . join ( o0oOoO00o , iIiiiI1IiI1I1 , 'startup.xml' ) )
II = xbmc . translatePath ( os . path . join ( o0oOoO00o , iIiiiI1IiI1I1 , 'temp.xml' ) )
ooOoOoo0O = xbmc . translatePath ( os . path . join ( o0oOoO00o , iIiiiI1IiI1I1 , 'id.xml' ) )
OooO0 = xbmc . translatePath ( os . path . join ( o0oOoO00o , iIiiiI1IiI1I1 , 'idtemp.xml' ) )
II11iiii1Ii = xbmc . translatePath ( os . path . join ( I11i , iIiiiI1IiI1I1 , 'resources/' ) )
OO0o = xbmc . getSkinDir ( )
Ooo = xbmc . translatePath ( os . path . join ( o0oOoO00o , iIiiiI1IiI1I1 ) )
O0o0Oo = xbmc . translatePath ( os . path . join ( Ooo , 'guinew.xml' ) )
Oo00OOOOO = xbmc . translatePath ( os . path . join ( Ooo , 'guitemp' , '' ) )
O0OO00o0OO = xbmc . translatePath ( os . path . join ( iIii1 , 'Database' ) )
I11i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.program.originwizard/Generated/TEST/resources/text_file/' ) )
iIi1ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.program.originwizard' ) )
o0 = 'None'
I11II1i = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
IIIII = 'http://rh-project.info/'
ooooooO0oo = "2.0.3"
IIiiiiiiIi1I1 = "originwizard"
if 13 - 13: OOoo0O0 + Ii + I1I - II11iII % oOoo % iIii11I
if 69 - 69: OOOO00ooo0Ooo % OOooOooo % O00oo0OO0oOOO * i1i1i11IIi . o0OOOoO0 / OO0O
if 70 - 70: OoOO
def IIi1I1Ii11iI ( ) :
 for file in glob . glob ( os . path . join ( I11i , '*' ) ) :
  I11i1I1I = str ( file ) . replace ( I11i , '[COLOR=red]REMOVE [/COLOR]' ) . replace ( 'plugin.' , '[COLOR=dodgerblue](PLUGIN) [/COLOR]' ) . replace ( 'audio.' , '' ) . replace ( 'video.' , '' ) . replace ( 'skin.' , '[COLOR=yellow](SKIN) [/COLOR]' ) . replace ( 'repository.' , '[COLOR=orange](REPOSITORY) [/COLOR]' ) . replace ( 'script.' , '[COLOR=cyan](SCRIPT) [/COLOR]' ) . replace ( 'metadata.' , '[COLOR=gold](METADATA) [/COLOR]' ) . replace ( 'service.' , '[COLOR=pink](SERVICE) [/COLOR]' ) . replace ( 'weather.' , '[COLOR=green](WEATHER) [/COLOR]' ) . replace ( 'module.' , '[COLOR=gold](MODULE) [/COLOR]' )
  oO0Oo = ( os . path . join ( file , 'icon.png' ) )
  oOOoo0Oo = ( os . path . join ( file , 'fanart.jpg' ) )
  extras . addDir ( '' , I11i1I1I , file , 'remove_addons' , oO0Oo , oOOoo0Oo , '' , '' )
  if 78 - 78: OOO00OoOO00
  if 45 - 45: ooO0O0O00 + I1I * i1i1i11IIi / o0OOOoO0
def oOOOoO0O00o0 ( ) :
 i1iII1IiiIiI1 . openSettings ( sys . argv [ 0 ] )
 if 30 - 30: iIii11I . o0OOOoO0 - OoooooooOO
 if 8 - 8: i1IIi - iIii1I11I1II1 * OOoo0O0 + i11iIiiIii / OOO00OoOO00 % O00oo0OO0oOOO
def iIIIi1 ( ) :
 extras . addDir ( 'folder' , 'Completely remove an add-on (inc. passwords)' , 'plugin' , 'addon_removal_menu' , 'Remove_Addon.png' , '' , '' , '' )
 extras . addDir ( '' , 'Hide my add-on passwords' , 'none' , 'hide_passwords' , 'Hide_Passwords.png' , '' , '' , '' )
 extras . addDir ( '' , 'Unhide my add-on passwords' , 'none' , 'unhide_passwords' , 'Unhide_Passwords.png' , '' , '' , '' )
 extras . addDir ( '' , 'Update My Add-ons (Force Refresh)' , 'none' , 'update' , 'Update_Addons.png' , '' , '' , '' )
 extras . addDir ( '' , 'Wipe All Add-on Settings (addon_data)' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 if 20 - 20: i1IIi + OOOO00ooo0Ooo - ooO0O0O00
 if 30 - 30: OOoo0O0 - O00oo0OO0oOOO - i11iIiiIii % oOoo - OOoo0O0 * o0OOOoO0
 if 61 - 61: OOooOooo - i1i1i11IIi % O00oo0OO0oOOO
def OOoOO0oo0ooO ( ) :
 extras . addDir ( 'folder' , 'Backup My Content' , 'none' , 'backup_option' , 'Backup.png' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Restore My Content' , 'none' , 'restore_option' , 'Restore.png' , '' , '' , '' )
 if 98 - 98: OO0O * OO0O / OO0O + i1i1i11IIi
 if 34 - 34: ooO0O0O00
def I1111I1iII11 ( ) :
 Oooo0O0oo00oO = 0
 IIi1i = i1iII1IiiIiI1 . getSetting ( 'maintenance' )
 I1I1iIiII1 = i1iII1IiiIiI1 . getSetting ( 'mainmenu' )
 i11i1I1 = i1iII1IiiIiI1 . getSetting ( 'guisettings' )
 ii1I = i1iII1IiiIiI1 . getSetting ( 'adultbuilds' )
 if I1I1iIiII1 == 'true' :
  extras . addDir ( 'folder' , 'Origin Builds' , 'none' , 'buildmenu' , 'Build_Menu.png' , '' , '' , '' )
 if ii1I == 'true' :
  extras . addDir ( 'folder' , 'Adult Builds' , 'none' , 'adultmenu' , 'Adult_Menu.png' , '' , '' , '' )
 if i11i1I1 == 'true' :
  extras . addDir ( 'folder' , 'Gui Settings XML' , 'none' , 'guisettings' , 'Gui_Menu.png' , '' , '' , '' )
 if IIi1i == 'true' :
  extras . addDir ( 'folder' , 'Maintenance' , 'none' , 'tools' , 'Tools.png' , '' , '' , '' )
  if 67 - 67: i11iIiiIii - i1IIi % OOOO00ooo0Ooo . O0
  if 77 - 77: OoOO / Ii
  if 15 - 15: OoOO . iIii1I11I1II1 . OoooooooOO / i11iIiiIii - o0OOOoO0 . i1IIi
def i1O0OoO0o ( ) :
 OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( 'Clear All Known Cache?' , 'This will clear all known cache files and can help' , 'if you\'re encountering kick-outs during playback.' , 'as well as other random issues. There is no harm in using this.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0oOO0O == 1 :
  cache . Wipe_Cache ( )
  oOiIi1IIIi1 ( )
  if 86 - 86: i1i1i11IIi % oOoo / Ii / oOoo
  if 42 - 42: II11iII
def o0o ( ) :
 o00OooOO000 = [ ]
 OOoOoo = sys . argv [ 2 ]
 if len ( OOoOoo ) >= 2 :
  oO0000OOo00 = sys . argv [ 2 ]
  iiIi1IIiIi = oO0000OOo00 . replace ( '?' , '' )
  if ( oO0000OOo00 [ len ( oO0000OOo00 ) - 1 ] == '/' ) :
   oO0000OOo00 = oO0000OOo00 [ 0 : len ( oO0000OOo00 ) - 2 ]
  oOO00Oo = iiIi1IIiIi . split ( '&' )
  o00OooOO000 = { }
  for i1iIIIi1i in range ( len ( oOO00Oo ) ) :
   iI1iIIiiii = { }
   iI1iIIiiii = oOO00Oo [ i1iIIIi1i ] . split ( '=' )
   if ( len ( iI1iIIiiii ) ) == 2 :
    o00OooOO000 [ iI1iIIiiii [ 0 ] ] = iI1iIIiiii [ 1 ]
    if 26 - 26: i1i1i11IIi . OoooooooOO
 return o00OooOO000
 if 39 - 39: OO0O - O0 % i11iIiiIii * OOO00OoOO00 . OoOO
 if 58 - 58: II11iII % i11iIiiIii . OO0O / OOooOooo
def O0o ( ) :
 OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( 'Delete Addon_Data Folder?' , 'This will free up space by deleting your addon_data' , 'folder. This contains all addon related settings' , 'including username and password info.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0oOO0O == 1 :
  extras . Delete_Userdata ( )
  O0oo0OO0 . ok ( "Addon_Data Removed" , '' , 'Your addon_data folder has now been removed.' , '' )
  if 59 - 59: Ii + Ii + iIii11I / iIii1I11I1II1
  if 51 - 51: i1i1i11IIi + OO0O % iIii1I11I1II1 / OOooOooo / O00oo0OO0oOOO % OoooooooOO
def o0O0OOO0Ooo ( ) :
 OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( 'Remove All Crash Logs?' , 'There is absolutely no harm in doing this, these are' , 'log files generated when Kodi crashes and are' , 'only used for debugging purposes.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0oOO0O == 1 :
  extras . Delete_Logs ( )
  O0oo0OO0 . ok ( "Crash Logs Removed" , '' , 'Your crash log files have now been removed.' , '' )
  if 45 - 45: O0 / iIii11I
  if 32 - 32: OO0O . OoOO . OoOO
def OO00O0O ( ) :
 OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( 'Delete Packages Folder?' , 'This will free up space by deleting the zip install' , 'files of your addons. The only downside is you\'ll no' , 'longer be able to rollback to older versions.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0oOO0O == 1 :
  extras . Delete_Packages ( )
  O0oo0OO0 . ok ( "Packages Removed" , '' , 'Your zip install files have now been removed.' , '' )
  if 33 - 33: O0 . OoOO . Ii
  if 72 - 72: i1IIi / II11iII + OoooooooOO - I1I
def oOiIi1IIIi1 ( ) :
 OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( 'Clear Cached Images?' , 'This will clear your textures13.db file and remove' , 'your Thumbnails folder. These will automatically be' , 'repopulated after a restart.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if OO0oOO0O == 1 :
  cache . Remove_Textures ( )
  extras . Destroy_Path ( i1111 )
  OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( 'Quit Kodi Now?' , 'Cache has been successfully deleted.' , 'You must now restart Kodi, would you like to quit now?' , '' , nolabel = 'I\'ll restart later' , yeslabel = 'Yes, quit' )
  if OO0oOO0O == 1 :
   iI1Iii ( )
   if 68 - 68: O00oo0OO0oOOO % OOO00OoOO00
   if 88 - 88: iIii1I11I1II1 - ooO0O0O00 + O00oo0OO0oOOO
def IiI111111IIII ( ) :
 extras . addDir ( 'folder' , '[COLOR white]Addon Installer[/COLOR]' , 'none' , 'Addons_Menu' , '' , '' , '' , '' )
 extras . addDir ( 'wizard' , '[COLOR red]Wizard Generator[/COLOR]' , 'none' , 'Merlin' , oo + 'icon.png' , oo + 'fanart.jpg' , '' , '' )
 extras . addDir ( 'folder' , 'Add-on Maintenance/Fixes' , 'none' , 'addonfixes' , '' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Backup/Restore My Content' , 'none' , 'backup_restore' , '' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Clean/Wipe Options' , 'none' , 'wipetools' , '' , '' , '' , '' )
 extras . addDir ( '' , 'Check XBMC/Kodi Version' , 'none' , 'xbmcversion' , '' , '' , '' , '' )
 extras . addDir ( '' , 'Convert Physical Paths To Special' , iiIIIII1i1iI , 'fix_special' , '' , '' , '' , '' )
 extras . addDir ( '' , 'Force Close Kodi' , 'url' , 'kill_xbmc' , '' , '' , '' , '' )
 if 37 - 37: OOO00OoOO00 / oOoo
 if 23 - 23: O0
def o00oO0oOo00 ( ) :
 extras . addDir ( 'wizard2' , '[COLOR red]How To Guide[/COLOR]' , 'none' , 'How_To' , oo + 'icon.png' , oo + 'fanart.jpg' , '' , '' )
 extras . addDir ( 'wizard2' , '[COLOR blue]Generate your personalised wizard[/COLOR]' , 'none' , 'Text_Gen' , oo + 'icon.png' , oo + 'fanart.jpg' , '' , '' )
 if 81 - 81: II11iII
 if 42 - 42: II11iII / i1i1i11IIi / iIii11I + OO0O / oOoo
 if 84 - 84: ooO0O0O00 * OOoo0O0 + I1I
 if 53 - 53: OO0O % OOoo0O0 . OoOO - iIii1I11I1II1 - OoOO * OOoo0O0
def ooO0oOOooOo0 ( ) :
 i1I1ii11i1Iii ( 'How To guide For Wizard Creation' , '1: First you will need to create a build and host somewhere online that it can be accessed\n\n\n2: Then you can run the Generate Txt File which will be what your wizard talks to in order to collect information about your build(s)\n\n\n3: Once Generated Host this file online somewhere so can be accessed by wizard\n\n\n4: Run the wizard generator and fill in relevant fields\n\n\n5: Get your zip and host online that will become your url that can be put into source in kodi\n\n\n6: Enjoy and do not forget to thank the devs, maybe donate to help them help you and visit some streaming sites suffer some ads to help keep them going aswell\n\n\n[COLORred]If you wish to add another build into your wizard simply duplicate the information in the .txt file thats generated then edit the information. May look at adding a funtion so you can add more builds easily in future[/COLOR]' )
 if 26 - 26: i1i1i11IIi - iIii1I11I1II1 - Ii / II11iII . oOoo % iIii1I11I1II1
 if 91 - 91: iIii11I . iIii1I11I1II1 / OOooOooo + i1IIi
def i1I1ii11i1Iii ( heading , announce ) :
 class I1i ( ) :
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
   try : OOOOO0oo0O0O0 = open ( announce ) ; oOoO0O0o0Oooo = OOOOO0oo0O0O0 . read ( )
   except : oOoO0O0o0Oooo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oOoO0O0o0Oooo ) )
   return
 I1i ( )
 if 5 - 5: ooO0O0O00 - OOoo0O0 - OoooooooOO % o0OOOoO0 + Ii * iIii1I11I1II1
 if 37 - 37: OoOO % ooO0O0O00 + oOoo + iIii11I * i1i1i11IIi % O0
 if 61 - 61: Ii - O00oo0OO0oOOO . OOooOooo / O00oo0OO0oOOO + I1I
def I1i11i ( ) :
 o00oO0oo0OO = xbmc . translatePath ( os . path . join ( iIii1 , 'Community Builds' , 'My Builds' ) )
 OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( "ABSOLUTELY CERTAIN?!!!" , 'Are you absolutely certain you want to wipe?' , '' , 'All addons and settings will be completely wiped!' , yeslabel = 'Yes' , nolabel = 'No' )
 if OO0oOO0O == 1 :
  if OO0o != "skin.confluence" :
   O0oo0OO0 . ok ( '[COLOR=white]Origin[/COLOR]' , 'Please switch to the default Confluence skin' , 'before performing a wipe.' , '' )
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
   return
  else :
   OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( "VERY IMPORTANT" , 'This will completely wipe your install.' , 'Would you like to create a backup before proceeding?' , '' , yeslabel = 'No' , nolabel = 'Yes' )
   if OO0oOO0O == 0 :
    if not os . path . exists ( o00oO0oo0OO ) :
     os . makedirs ( o00oO0oo0OO )
    O0O0OOOOoo = extras . Get_Keyboard ( heading = "Enter a name for this backup" )
    if ( not O0O0OOOOoo ) : return False , 0
    oOooO0 = urllib . quote_plus ( O0O0OOOOoo )
    Ii1I1Ii = xbmc . translatePath ( os . path . join ( o00oO0oo0OO , oOooO0 + '.zip' ) )
    OOoO0 = [ 'plugin.program.originwizard' ]
    OO0Oooo0oOO0O = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
    o00O0 = "Creating full backup of existing build"
    oOO0O00Oo0O0o = "Archiving..."
    ii1 = ""
    I1iIIiiIIi1i = "Please Wait"
    communitybuilds . Archive_Tree ( iiIIIII1i1iI , Ii1I1Ii , o00O0 , oOO0O00Oo0O0o , ii1 , I1iIIiiIIi1i , OOoO0 , OO0Oooo0oOO0O )
   OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( "Remove Origin Wizard?" , 'Do you also want to remove the Origin Wizard' , 'add-on and have a complete fresh start or would you' , 'prefer to keep this on your system?' , yeslabel = 'Remove' , nolabel = 'Keep' )
   if OO0oOO0O == 0 :
    cache . Remove_Textures ( )
    O0O0ooOOO = xbmc . translatePath ( os . path . join ( I11i , iIiiiI1IiI1I1 , '' ) )
    oOOo0O00o = xbmc . translatePath ( os . path . join ( iiIIIII1i1iI , '..' , 'originwizard.zip' ) )
    communitybuilds . Archive_File ( O0O0ooOOO , oOOo0O00o )
    iIiIi11 = xbmc . translatePath ( os . path . join ( I11i , 'script.module.addon.common' , '' ) )
    OOO = xbmc . translatePath ( os . path . join ( iiIIIII1i1iI , '..' , 'originwizarddep.zip' ) )
    communitybuilds . Archive_File ( iIiIi11 , OOO )
    extras . Destroy_Path ( iiIIIII1i1iI )
    if not os . path . exists ( O0O0ooOOO ) :
     os . makedirs ( O0O0ooOOO )
    if not os . path . exists ( iIiIi11 ) :
     os . makedirs ( iIiIi11 )
    time . sleep ( 1 )
    communitybuilds . Read_Zip ( oOOo0O00o )
    I1i1iiI1 . create ( "[[COLOR=white]Origin[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
    I1i1iiI1 . update ( 0 , "" , "Extracting Zip Please Wait" )
    extract . all ( oOOo0O00o , O0O0ooOOO , I1i1iiI1 )
    communitybuilds . Read_Zip ( OOO )
    extract . all ( OOO , iIiIi11 , I1i1iiI1 )
    I1i1iiI1 . update ( 0 , "" , "Extracting Zip Please Wait" )
    I1i1iiI1 . close ( )
    time . sleep ( 1 )
    extras . Kill_XBMC ( )
   elif OO0oOO0O == 1 :
    cache . Remove_Textures ( )
    extras . Destroy_Path ( iiIIIII1i1iI )
    I1i1iiI1 . close ( )
    extras . Kill_XBMC ( )
   else : return
   if 32 - 32: i1IIi / OOoo0O0 . I1I
   if 62 - 62: OoooooooOO * Ii
def oOOOoo0O0oO ( ) :
 extras . addDir ( '' , 'Clear Cache' , 'url' , 'clear_cache' , 'Clear_Cache.png' , '' , '' , '' )
 extras . addDir ( '' , 'Clear My Cached Artwork' , 'none' , 'remove_textures' , 'Delete_Cached_Artwork.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Addon_Data' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Old Builds/Zips From Device' , 'url' , 'remove_build' , 'Delete_Builds.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Old Crash Logs' , 'url' , 'remove_crash_logs' , 'Delete_Crash_Logs.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Packages Folder' , 'url' , 'remove_packages' , 'Delete_Packages.png' , '' , '' , '' )
 extras . addDir ( '' , 'Wipe My Install (Fresh Start)' , 'none' , 'wipe_xbmc' , 'Fresh_Start.png' , '' , '' , '' )
 if 6 - 6: O00oo0OO0oOOO * iIii11I + OO0O
 if 44 - 44: o0OOOoO0 % II11iII + OoooooooOO - O0 - o0OOOoO0 - OOoo0O0
def O0Oo0oOOoooOOOOo ( ) :
 o0oO0O0o0O00O = OoO000O0Oo ( 'http://back2basicsbuild.co.uk/wizard/toolbox.xml' ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0o0oooo0O0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0oO0O0o0O00O )
 for I11i1I1I , OooooOOoo0 , oO0Oo , oOOoo0Oo , i1I1IiiIi1i in Oo0o0oooo0O0 :
  iiI11ii1I1 ( I11i1I1I , OooooOOoo0 , 'wizard' , oO0Oo , oOOoo0Oo , i1I1IiiIi1i )
 Ooo0OOoOoO0 ( '500' )
 if 70 - 70: OOooOooo
def OoO000O0Oo ( url ) :
 oOOoO0o0oO = urllib2 . Request ( url )
 oOOoO0o0oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0Oo0oO0oOO00 = urllib2 . urlopen ( oOOoO0o0oO )
 o0oO0O0o0O00O = o0Oo0oO0oOO00 . read ( )
 o0Oo0oO0oOO00 . close ( )
 return o0oO0O0o0O00O
 if 92 - 92: OoooooooOO * OOO00OoOO00
def o0000oO ( name , url , description ) :
 I1II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 I1i1iiI1 = xbmcgui . DialogProgress ( )
 I1i1iiI1 . create ( "origin wizard" , "Downloading " , '' , 'Please Wait' )
 oooO = os . path . join ( I1II1 , name + '.zip' )
 try :
  os . remove ( oooO )
 except :
  pass
 downloader . download ( url , oooO , I1i1iiI1 )
 i1I1i111Ii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 I1i1iiI1 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I1i111Ii
 print '======================================='
 extract . all ( oooO , i1I1i111Ii , I1i1iiI1 )
 O0oo0OO0 = xbmcgui . Dialog ( )
 O0oo0OO0 . ok ( "DOWNLOAD COMPLETE" , 'To ensure all changes are saved you must now close Kodi' , 'to force close Kodi. Click ok,' , 'DO NOT use the quit/exit options in Kodi.' )
 iI1Iii ( )
 if 67 - 67: Ii . i1IIi
def iI1Iii ( ) :
 OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OO0oOO0O == 0 :
  return
 elif OO0oOO0O == 1 :
  pass
 i1i1iI1iiiI = Ooo0oOooo0 ( )
 print "Platform: " + str ( i1i1iI1iiiI )
 if i1i1iI1iiiI == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  O0oo0OO0 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1i1iI1iiiI == 'linux' :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  O0oo0OO0 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1i1iI1iiiI == 'android' :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  O0oo0OO0 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
 elif i1i1iI1iiiI == 'windows' :
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
  O0oo0OO0 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  O0oo0OO0 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
  if 61 - 61: oOoo - O00oo0OO0oOOO - i1IIi
def Ooo0oOooo0 ( ) :
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
  if 25 - 25: O0 * i1i1i11IIi + OOOO00ooo0Ooo . iIii11I . iIii11I
  if 58 - 58: Ii
def iiI11ii1I1 ( name , url , mode , iconimage , fanart , description ) :
 oOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoO00O0 = True
 OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OO . setProperty ( "Fanart_Image" , fanart )
 oOoO00O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoO , listitem = OO , isFolder = False )
 return oOoO00O0
 if 7 - 7: O0 * i11iIiiIii * o0OOOoO0 + ooO0O0O00 % II11iII - ooO0O0O00
def Ooo0OOoOoO0 ( content = '' ) :
 if not content :
  return
  if 39 - 39: I1I * O00oo0OO0oOOO % O00oo0OO0oOOO - OoooooooOO + iIii11I - i1i1i11IIi
 xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if i1iII1IiiIiI1 . getSetting ( 'auto-view' ) != 'true' :
  return
  if 23 - 23: i11iIiiIii
 if content == 'addons' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % i1iII1IiiIiI1 . getSetting ( 'addon_view' ) )
 else :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % i1iII1IiiIiI1 . getSetting ( 'default-view' ) )
  if 30 - 30: iIii11I - i1IIi % OOoo0O0 + i1i1i11IIi * iIii1I11I1II1
  if 81 - 81: OoOO % i1IIi . iIii1I11I1II1
oO0000OOo00 = o0o ( )
Ii1Iii1iIi = None
OO0oo = None
Iii1 = None
OOO0000oO = None
iI1i111I1Ii = None
i1I1IiiIi1i = None
i11i1ii1I = None
o0OO0o0o00o = None
oOOoo0Oo = None
oOo0 = None
oO0Oo = None
o0oO0O0o0O00O = None
OOOoOO = None
I11IIIi = None
iIIiiI1II1i11 = None
I11i1I1I = None
o0o0 = None
IIii1111 = None
I1iI = None
IIIIiIiIi1 = None
I11iiiiI1i = None
iI1i11 = None
OoOOoooOO0O = None
ooo00Ooo = None
Oo0o0O00 = None
OooooOOoo0 = None
ii1I1i11 = None
OOo0O0oo0OO0O = None
OO0 = None
o0O = None
ooo = None
if 36 - 36: OoooooooOO . II11iII
try : Ii1Iii1iIi = urllib . unquote_plus ( oO0000OOo00 [ "addon_id" ] )
except : pass
try : oOIIiIi = urllib . unquote_plus ( oO0000OOo00 [ "adult" ] )
except : pass
try : OO0oo = urllib . unquote_plus ( oO0000OOo00 [ "audioaddons" ] )
except : pass
try : Iii1 = urllib . unquote_plus ( oO0000OOo00 [ "author" ] )
except : pass
try : OOO0000oO = urllib . unquote_plus ( oO0000OOo00 [ "buildname" ] )
except : pass
try : iI1i111I1Ii = urllib . unquote_plus ( oO0000OOo00 [ "data_path" ] )
except : pass
try : i1I1IiiIi1i = urllib . unquote_plus ( oO0000OOo00 [ "description" ] )
except : pass
try : i11i1ii1I = urllib . unquote_plus ( oO0000OOo00 [ "DOB" ] )
except : pass
try : o0OO0o0o00o = urllib . unquote_plus ( oO0000OOo00 [ "email" ] )
except : pass
try : oOOoo0Oo = urllib . unquote_plus ( oO0000OOo00 [ "fanart" ] )
except : pass
try : oOo0 = urllib . unquote_plus ( oO0000OOo00 [ "forum" ] )
except : pass
try : OOoOooOoOOOoo = urllib . unquote_plus ( oO0000OOo00 [ "guisettingslink" ] )
except : pass
try : oO0Oo = urllib . unquote_plus ( oO0000OOo00 [ "iconimage" ] )
except : pass
try : o0oO0O0o0O00O = urllib . unquote_plus ( oO0000OOo00 [ "link" ] )
except : pass
try : OOOoOO = urllib . unquote_plus ( oO0000OOo00 [ "local" ] )
except : pass
try : I11IIIi = urllib . unquote_plus ( oO0000OOo00 [ "messages" ] )
except : pass
try : iIIiiI1II1i11 = str ( oO0000OOo00 [ "mode" ] )
except : pass
try : I11i1I1I = urllib . unquote_plus ( oO0000OOo00 [ "name" ] )
except : pass
try : Iiii1iI1i = urllib . unquote_plus ( oO0000OOo00 [ "pictureaddons" ] )
except : pass
try : o0o0 = urllib . unquote_plus ( oO0000OOo00 [ "posts" ] )
except : pass
try : IIii1111 = urllib . unquote_plus ( oO0000OOo00 [ "programaddons" ] )
except : pass
try : I1iI = urllib . unquote_plus ( oO0000OOo00 [ "provider_name" ] )
except : pass
try : I11iiiiI1i = urllib . unquote_plus ( oO0000OOo00 [ "repo_link" ] )
except : pass
try : IIIIiIiIi1 = urllib . unquote_plus ( oO0000OOo00 [ "repo_id" ] )
except : pass
try : iI1i11 = urllib . unquote_plus ( oO0000OOo00 [ "skins" ] )
except : pass
try : OoOOoooOO0O = urllib . unquote_plus ( oO0000OOo00 [ "sources" ] )
except : pass
try : ooo00Ooo = urllib . unquote_plus ( oO0000OOo00 [ "updated" ] )
except : pass
try : Oo0o0O00 = urllib . unquote_plus ( oO0000OOo00 [ "unread" ] )
except : pass
try : OooooOOoo0 = urllib . unquote_plus ( oO0000OOo00 [ "url" ] )
except : pass
try : ii1I1i11 = urllib . unquote_plus ( oO0000OOo00 [ "version" ] )
except : pass
try : OOo0O0oo0OO0O = urllib . unquote_plus ( oO0000OOo00 [ "video" ] )
except : pass
try : OO0 = urllib . unquote_plus ( oO0000OOo00 [ "videoaddons" ] )
except : pass
try : ooo = urllib . unquote_plus ( oO0000OOo00 [ "zip_link" ] )
except : pass
if 34 - 34: ooO0O0O00 * Ii . i1IIi * ooO0O0O00 / ooO0O0O00
print str ( IIiiiiiiIi1I1 ) + ': ' + str ( ooooooO0oo )
print "Mode: " + str ( iIIiiI1II1i11 )
print "URL: " + str ( OooooOOoo0 )
print "Name: " + str ( I11i1I1I )
print "IconImage: " + str ( oO0Oo )
if 30 - 30: OOOO00ooo0Ooo + I1I / I1I % OOOO00ooo0Ooo . OOOO00ooo0Ooo
if 55 - 55: ooO0O0O00 - i1i1i11IIi + OOoo0O0 + OO0O % o0OOOoO0
if 41 - 41: i1IIi - i1i1i11IIi - o0OOOoO0
if 8 - 8: II11iII + OOO00OoOO00 - iIii11I % I1I % iIii11I * OOooOooo
i1iII1IiiIiI1 = xbmcaddon . Addon ( id = 'plugin.program.originwizard' )
IIIi11I11 = xbmcgui . Dialog ( )
iiIIIII1i1iI = xbmc . translatePath ( 'special://home/' )
iIii1 = xbmc . translatePath ( os . path . join ( zip ) )
I1i1iiI1 = xbmcgui . DialogProgress ( )
iIIII = 'https://addons.tvaddons.ag/'
if 45 - 45: OOOO00ooo0Ooo % Ii - i11iIiiIii
def OoO000O0Oo ( url ) :
 oOOoO0o0oO = urllib2 . Request ( url )
 oOOoO0o0oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0Oo0oO0oOO00 = urllib2 . urlopen ( oOOoO0o0oO )
 o0oO0O0o0O00O = o0Oo0oO0oOO00 . read ( )
 o0Oo0oO0oOO00 . close ( )
 return o0oO0O0o0O00O
 if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * Ii
def iII1ii1 ( ) :
 if 12 - 12: O00oo0OO0oOOO - ooO0O0O00 . OoooooooOO / OOOO00ooo0Ooo . i1IIi * II11iII
 extras . addDir ( 'folder' , 'Catagories' , 'none' , 'Addon_Cat' , '' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Search' , 'none' , 'Search_Addons' , '' , '' , '' , '' )
 if 19 - 19: i11iIiiIii + OoooooooOO - I1I - i1i1i11IIi
def Iii1iiIi1II ( ) :
 OO0O00oOo = IIIi11I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1II = OO0O00oOo . lower ( )
 iI1I = 'https://addons.tvaddons.ag/search/?keyword=' + ii1II
 OooOoOo = OoO000O0Oo ( iI1I )
 Oo0o0oooo0O0 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OooOoOo )
 for OooooOOoo0 , III1I1Iii1iiI , I11i1I1I in Oo0o0oooo0O0 :
  extras . addDirNew ( I11i1I1I , OooooOOoo0 , 'Addon_Extract' , 'https://addons.tvaddons.ag/' + III1I1Iii1iiI , I11 , '' )
  if 17 - 17: o0OOOoO0 % iIii1I11I1II1 - iIii1I11I1II1
def O0o0O0 ( ) :
 OooOoOo = OoO000O0Oo ( iIIII )
 Oo0o0oooo0O0 = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OooOoOo )
 for OooooOOoo0 , Ii1II1I11i1 , I11i1I1I in Oo0o0oooo0O0 :
  if 'Repositories' in I11i1I1I :
   pass
  elif 'Services' in I11i1I1I :
   pass
  elif 'International' in I11i1I1I :
   pass
  else :
   extras . addDir ( 'folder' , I11i1I1I , OooooOOoo0 , 'Addon' , 'https://addons.tvaddons.ag/' + Ii1II1I11i1 , '' , '' , '' )
   if 59 - 59: OOooOooo % iIii1I11I1II1 . i1IIi
def iiIi1i ( url ) :
 OooOoOo = OoO000O0Oo ( url )
 Oo0o0oooo0O0 = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" width="100%" alt=".+?" class="pic" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OooOoOo )
 for url , Ii1II1I11i1 , I11i1I1I in Oo0o0oooo0O0 :
  extras . addDir ( '' , I11i1I1I , url , 'Addon' , 'https://addons.tvaddons.ag/' + Ii1II1I11i1 , '' , '' , '' )
  if 27 - 27: O00oo0OO0oOOO * ooO0O0O00 . OOO00OoOO00 % OoOO * OoOO . i1IIi
  if 72 - 72: O00oo0OO0oOOO % OOOO00ooo0Ooo + II11iII / OOooOooo + OoOO
def I1I1i ( url ) :
 OooOoOo = OoO000O0Oo ( url )
 I1IIIiIiIi = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( OooOoOo )
 for url in I1IIIiIiIi :
  extras . addDirNewFolder ( 'NEXT PAGE' , 'https://addons.tvaddons.ag' + url , 'Addon' , O0O + 'Next.png' , '' , '' )
 Oo0o0oooo0O0 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OooOoOo )
 for url , Ii1II1I11i1 , I11i1I1I in Oo0o0oooo0O0 :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>' + 'https://addons.tvaddons.ag/' + Ii1II1I11i1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
  if 'Please' in I11i1I1I :
   pass
  else :
   extras . addDirNew ( I11i1I1I , url , 'Addon_Extract' , 'https://addons.tvaddons.ag/' + Ii1II1I11i1 , I11 , '' )
   if 27 - 27: OOOO00ooo0Ooo + oOoo - O00oo0OO0oOOO + O0 . o0OOOoO0
   if 46 - 46: OoOO
def ii1iIi1iIiI1i ( url , name ) :
 OooOoOo = OoO000O0Oo ( url )
 Oo0o0oooo0O0 = re . compile ( '<a href="(.+?)"' ) . findall ( OooOoOo )
 for url in Oo0o0oooo0O0 :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   I1II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   I1i1iiI1 = xbmcgui . DialogProgress ( )
   I1i1iiI1 . create ( "Origin" , "Downloading Content" , '' , 'Please Wait' )
   oooO = os . path . join ( I1II1 , name + '.zip' )
   try :
    os . remove ( oooO )
   except :
    pass
   downloader . download ( url , oooO , I1i1iiI1 )
   i1I1i111Ii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   I1i1iiI1 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print i1I1i111Ii
   print '======================================='
   extract . all ( oooO , i1I1i111Ii , I1i1iiI1 )
   O0oo0OO0 = xbmcgui . Dialog ( )
   O0oo0OO0 . ok ( "Origin" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Origin[/COLOR]" )
   if 40 - 40: i1IIi % O00oo0OO0oOOO
   if 71 - 71: oOoo
   if 14 - 14: i11iIiiIii % O00oo0OO0oOOO
   if 82 - 82: iIii1I11I1II1 + I1I . iIii1I11I1II1 % OoOO / o0OOOoO0 . o0OOOoO0
i1iII1IiiIiI1 = xbmcaddon . Addon ( id = 'plugin.program.originwizard' )
zip = i1iII1IiiIiI1 . getSetting ( 'zip' )
IIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.program.originwizard/Generated/' ) )
oOoO00oo0O = 'TEST'
IiiiI = IIi + oOoO00oo0O
IIIi11I11 = xbmcgui . Dialog ( )
iiIIIII1i1iI = xbmc . translatePath ( 'special://home/' )
iIii1 = xbmc . translatePath ( os . path . join ( zip ) )
I1i1iiI1 = xbmcgui . DialogProgress ( )
if 61 - 61: O00oo0OO0oOOO % O00oo0OO0oOOO * iIii11I / iIii11I
def o0oOO ( ) :
 I1II1 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  IIIi11I11 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  i1iII1IiiIiI1 . openSettings ( sys . argv [ 0 ] )
  if 53 - 53: OOO00OoOO00 * OoOO . I1I - o0OOOoO0 % o0OOOoO0 * i11iIiiIii
  if 7 - 7: O0 . o0OOOoO0
def OO0oOOoo ( url ) :
 I1i1iiI1 . create ( "[COLOR=white]Origin[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for oOOO00o000o , iIi11i1 , oO00oo0o00o0o in os . walk ( url ) :
  for file in oO00oo0o00o0o :
   if file . endswith ( ".xml" ) :
    I1i1iiI1 . update ( 0 , "Fixing" , file , 'Please Wait' )
    IiIIIIIi = open ( ( os . path . join ( oOOO00o000o , file ) ) ) . read ( )
    IiIi1iIIi1 = IiIIIIIi . replace ( iiIIIII1i1iI , 'special://home/' )
    OOOOO0oo0O0O0 = open ( ( os . path . join ( oOOO00o000o , file ) ) , mode = 'w' )
    OOOOO0oo0O0O0 . write ( str ( IiIi1iIIi1 ) )
    OOOOO0oo0O0O0 . close ( )
    if 86 - 86: i1i1i11IIi * Ii + i1i1i11IIi + OOoo0O0
class i1i111iI ( ) :
 if 29 - 29: OOOO00ooo0Ooo / i1IIi . Ii - oOoo - oOoo - o0OOOoO0
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
  self . save_path = IiiiI
  self . txt_file_name = 'wizard.txt'
  self . plugin_name = ''
  self . clean_plugin_name = ''
  self . build_url = ''
  self . clean_build_url = ( build_url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  self . py_file_name = 'default.py'
  self . addon_file_name = 'addon.xml'
  self . action = action
  if self . action == 'newWizard' :
   self . Wizard_Inputs ( )
  elif self . action == 'textFile' :
   self . txt_file_inputs ( )
  else : pass
  if 20 - 20: i1IIi % II11iII . Ii / OoOO * i11iIiiIii * O00oo0OO0oOOO
 def Wizard_Inputs ( self ) :
  o0oOO ( )
  self . plugin_name = IIIi11I11 . input ( '[COLOR red]Input Name of Wizard[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . Wizard_name = self . plugin_name . lower ( )
  self . clean_plugin_name = ( self . Wizard_name ) . replace ( ' ' , '' )
  if 85 - 85: iIii11I . oOoo / ooO0O0O00 . O0 % OOO00OoOO00
  self . generate_wizard_py ( )
  if 90 - 90: I1I % O0 * iIii1I11I1II1 . OO0O
  if 8 - 8: ooO0O0O00 + OOoo0O0 / OO0O / i1i1i11IIi
  if 74 - 74: O0 / i1IIi
 def txt_file_inputs ( self ) :
  o0oOO ( )
  self . build_name = IIIi11I11 . input ( '[COLOR red] Input Build Name[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_zip = IIIi11I11 . input ( '[COLOR red] Input Builds Online Zip Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_image = IIIi11I11 . input ( '[COLOR red] Input Builds Online Image Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_fanart = IIIi11I11 . input ( '[COLOR red] Input Builds Online Background Image[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_description = IIIi11I11 . input ( '[COLOR red] Input Builds Description[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  if 78 - 78: OoooooooOO . II11iII + ooO0O0O00 - i1IIi
  self . Checker ( )
  if 31 - 31: OoooooooOO . O00oo0OO0oOOO
 def Checker ( self ) :
  if 83 - 83: OO0O . O0 / I1I / O00oo0OO0oOOO - OOoo0O0
  OooOoOo = OoO000O0Oo ( o0OO00 ( 'aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC9QaGVub21lbmFsL2J1aWxkc2VjdXJldXJscy50eHQ=' ) )
  Oo0o0oooo0O0 = re . compile ( "<url=>(.+?)</url>" ) . findall ( OooOoOo )
  for OooooOOoo0 in Oo0o0oooo0O0 :
   oO0oO0 = OooooOOoo0
   i1i1IIIIi1i = OoO000O0Oo ( oO0oO0 )
   Ii11iiI = re . compile ( "<url=>(.+?)</url>" ) . findall ( i1i1IIIIi1i )
   for IIi1iiii1iI in Ii11iiI :
    if self . extra_build_zip == IIi1iiii1iI :
     iIiiii ( )
    elif self . build_zip == IIi1iiii1iI :
     iIiiii ( )
    else :
     self . generate_wizard_text ( )
     if 89 - 89: OO0O - ooO0O0O00 % I1I % iIii11I
 def generate_wizard_text ( self ) :
  if 49 - 49: I1I - Ii / OoOO / O0 % iIii11I * o0OOOoO0
  OOo = os . path . join ( I11i1 , self . txt_file_name )
  O0II11iI111i1 = open ( OOo , "w+" )
  if 95 - 95: OoooooooOO - OoOO * Ii + oOoo
  O0II11iI111i1 . write ( r'name=<' + self . build_name + '>\n' )
  O0II11iI111i1 . write ( r'url=<' + self . build_zip + '>\n' )
  O0II11iI111i1 . write ( r'img=<' + self . build_image + '>\n' )
  O0II11iI111i1 . write ( r'fanart=<' + self . build_fanart + '>\n' )
  O0II11iI111i1 . write ( r'description=<' + self . build_description + '>\n' )
  O0II11iI111i1 . close ( )
  OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( "Is There Any More Builds?" , 'Would You like to add another build into txt file?' , '' , 'This Will also show in your wizard when generated' , yeslabel = 'Yes' , nolabel = 'No' )
  if OO0oOO0O == 1 :
   self . txt_extra_file_inputs ( )
  elif OO0oOO0O == 0 :
   IIIi11I11 . ok ( "[COLOR=white]Origin[/COLOR]" , "Your Wizard Will Now Be Generated" , '' , '' )
   self . Wizard_Inputs ( )
   if 10 - 10: iIii11I / i11iIiiIii
 def txt_extra_file_inputs ( self ) :
  o0oOO ( )
  self . extra_build_name = IIIi11I11 . input ( '[COLOR red] Input Build Name[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_zip = IIIi11I11 . input ( '[COLOR red] Input Builds Online Zip Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_image = IIIi11I11 . input ( '[COLOR red] Input Builds Online Image Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_fanart = IIIi11I11 . input ( '[COLOR red] Input Builds Online Background Image[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_description = IIIi11I11 . input ( '[COLOR red] Input Builds Description[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  if choice == 1 :
   self . txt_extra_file_inputs ( )
  elif choice == 0 :
   IIIi11I11 . ok ( "[COLOR=white]Origin[/COLOR]" , "Your Wizard Will Now Be Generated" , '' , '' )
   if 92 - 92: i1i1i11IIi . OOO00OoOO00
  self . extra_generate_wizard_text ( )
  if 85 - 85: OOOO00ooo0Ooo . OOO00OoOO00
 def extra_generate_wizard_text ( self ) :
  if 78 - 78: ooO0O0O00 * OOO00OoOO00 + iIii1I11I1II1 + iIii1I11I1II1 / OOO00OoOO00 . o0OOOoO0
  O000 = os . path . join ( I11i1 , self . txt_file_name )
  ooo0o000O = open ( O000 , "a" )
  if 100 - 100: OOooOooo . ooO0O0O00 * OOOO00ooo0Ooo / iIii1I11I1II1 * i1IIi % ooO0O0O00
  ooo0o000O . write ( r'name=<' + self . extra_build_name + '>\n' )
  ooo0o000O . write ( r'url=<' + self . extra_build_zip + '>\n' )
  ooo0o000O . write ( r'img=<' + self . extra_build_image + '>\n' )
  ooo0o000O . write ( r'fanart=<' + self . extra_build_fanart + '>\n' )
  ooo0o000O . write ( r'description=<' + self . extra_build_description + '>\n' )
  ooo0o000O . close ( )
  OO0oOO0O = xbmcgui . Dialog ( ) . yesno ( "Is There Any More Builds?" , 'Would You like to add another build into txt file?' , '' , 'This Will also show in your wizard when generated' , yeslabel = 'Yes' , nolabel = 'No' )
  if OO0oOO0O == 1 :
   self . txt_extra_file_inputs ( )
  elif OO0oOO0O == 0 :
   IIIi11I11 . ok ( "[COLOR=white]Origin[/COLOR]" , "Your Wizard Will Now Be Generated" , '' , '' )
   self . Wizard_Inputs ( )
   if 17 - 17: i1i1i11IIi . OoOO - OOoo0O0 + O0 / iIii1I11I1II1 / i11iIiiIii
 def generate_wizard_py ( self ) :
  if 39 - 39: OoOO * I1I + iIii1I11I1II1 - OoOO + O00oo0OO0oOOO
  if 69 - 69: O0
  o0ooO = os . path . join ( self . save_path , self . py_file_name )
  OoOOOo0o0ooo = open ( o0ooO , "w+" )
  if 19 - 19: i1i1i11IIi % OOoo0O0 / i11iIiiIii / OO0O - OoooooooOO
  if 37 - 37: O00oo0OO0oOOO / OoooooooOO - i11iIiiIii
  OoOOOo0o0ooo . write ( r'import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os' + '\n' )
  OoOOOo0o0ooo . write ( r'import shutil' + '\n' )
  OoOOOo0o0ooo . write ( r'import urllib2,urllib' + '\n' )
  OoOOOo0o0ooo . write ( r'import re,base64' + '\n' )
  OoOOOo0o0ooo . write ( r'import extract' + '\n' )
  OoOOOo0o0ooo . write ( r'import downloader' + '\n' )
  OoOOOo0o0ooo . write ( r'import time' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r"Decode = base64.decodestring" + "\n" )
  OoOOOo0o0ooo . write ( r"WIPE_ADDON 	 =  xbmc.translatePath(os.path.join('special://home/addons/plugin.program.originwizard/'))" + "\n" )
  OoOOOo0o0ooo . write ( r"ADDONS         =  xbmc.translatePath(os.path.join('special://home/addons/plugin.video." + self . clean_plugin_name + "'))" + "\n" )
  OoOOOo0o0ooo . write ( r"text_file_path = ADDONS + '/resources/text_file/'" + "\n" )
  OoOOOo0o0ooo . write ( r"USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'" + '\n' )
  OoOOOo0o0ooo . write ( r"base='" + self . plugin_name + '\'' + '\n' )
  OoOOOo0o0ooo . write ( r"ADDON=xbmcaddon.Addon(id='plugin.video." + self . clean_plugin_name + '\')' + '\n' )
  OoOOOo0o0ooo . write ( r'Dialog = xbmcgui.Dialog()' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'VERSION = "1.0.0"' + '\n' )
  OoOOOo0o0ooo . write ( r"PATH = '" + self . clean_plugin_name + '\'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'def CATEGORIES()' + ':\n' )
  OoOOOo0o0ooo . write ( r"    py_complete_name = os.path.join(text_file_path,'wizard.txt')" + '\n' )
  OoOOOo0o0ooo . write ( r"    print_default_file = open(py_complete_name," r")" + '\n' )
  OoOOOo0o0ooo . write ( r'    file = print_default_file.read()' + '\n' )
  OoOOOo0o0ooo . write ( r"    match = re.compile('name=<(.+?)>.+?url=<(.+?)>.+?img=<(.+?)>.+?fanart=<(.+?)>.+?description=<(.+?)>',re.DOTALL).findall(file)" + "\n" )
  OoOOOo0o0ooo . write ( r'    print_default_file.close()' + '\n' )
  OoOOOo0o0ooo . write ( r'    for name,url,iconimage,fanart,description in match:' + '\n' )
  OoOOOo0o0ooo . write ( r'        NAME = name' + '\n' )
  OoOOOo0o0ooo . write ( r'        URL = url' + '\n' )
  OoOOOo0o0ooo . write ( r"        IMAGE = iconimage" + '\n' )
  OoOOOo0o0ooo . write ( r"        FANART = fanart" + "\n" )
  OoOOOo0o0ooo . write ( r"        DESC = description" + "\n" )
  OoOOOo0o0ooo . write ( r"        HTML = OPEN_URL(Decode('aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC9QaGVub21lbmFsL2J1aWxkc2VjdXJldXJscy50eHQ='))" + "\n" )
  OoOOOo0o0ooo . write ( r"        match2 = re.compile('<url=>(.+?)</url>').findall(HTML)" + "\n" )
  OoOOOo0o0ooo . write ( r"        for url2 in match2:" + "\n" )
  OoOOOo0o0ooo . write ( r"            HTML2 = OPEN_URL(str(url2))" + "\n" )
  OoOOOo0o0ooo . write ( r"            match3 = re.compile('<url=>(.+?)</url>').findall(HTML2)" + "\n" )
  OoOOOo0o0ooo . write ( r"            for url3 in match3:" + "\n" )
  OoOOOo0o0ooo . write ( r"                if URL == url3:" + "\n" )
  OoOOOo0o0ooo . write ( r"                    Wipe_Wizard()" + "\n" )
  OoOOOo0o0ooo . write ( r"                elif url3 == 'kill all':" + "\n" )
  OoOOOo0o0ooo . write ( r"                    Wipe_Wizard()" + "\n" )
  OoOOOo0o0ooo . write ( r"        else:" + "\n" )
  OoOOOo0o0ooo . write ( r'            addDir(NAME,URL,1,IMAGE,FANART,DESC)' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'def Wipe_Wizard():' + '\n' )
  OoOOOo0o0ooo . write ( r"    Dialog.ok('[COLOR=white]Naughty Naughty[/COLOR]', 'You are the weakest link goodbye', '','')" + "\n" )
  OoOOOo0o0ooo . write ( r"    addon_complete_name = os.path.join(WIPE_ADDON,'default.py')" + "\n" )
  OoOOOo0o0ooo . write ( r'    print_byebye_file = open(addon_complete_name,"w+")' + '\n' )
  OoOOOo0o0ooo . write ( r"    print_byebye_file.write(r'This Build Can NOT be copied')" + "\n" )
  OoOOOo0o0ooo . write ( r'    print_byebye_file.close()' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r"    addons_complete_name = os.path.join(ADDONS,'default.py')" + "\n" )
  OoOOOo0o0ooo . write ( r'    print_byebye_addon_file = open(addons_complete_name,"w+")' + '\n' )
  OoOOOo0o0ooo . write ( r"    print_byebye_addon_file.write(r'This Build Can NOT be copied')" + "\n" )
  OoOOOo0o0ooo . write ( r"    print_byebye_addon_file.close()" + "\n" )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'def OPEN_URL(url):' + '\n' )
  OoOOOo0o0ooo . write ( r'    req = urllib2.Request(url)' + '\n' )
  OoOOOo0o0ooo . write ( r"    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')" + '\n' )
  OoOOOo0o0ooo . write ( r'    response = urllib2.urlopen(req)' + '\n' )
  OoOOOo0o0ooo . write ( r'    link=response.read()' + '\n' )
  OoOOOo0o0ooo . write ( r'    response.close()' + '\n' )
  OoOOOo0o0ooo . write ( r'    return link' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'def wizard(name,url,description):' + '\n' )
  OoOOOo0o0ooo . write ( r"    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))" + '\n' )
  OoOOOo0o0ooo . write ( r'    dp = xbmcgui.DialogProgress()' + '\n' )
  OoOOOo0o0ooo . write ( r'    dp.create("Your Build Is Downloading","This May Take Several Minutes","", "")' + '\n' )
  OoOOOo0o0ooo . write ( r"    lib=os.path.join(path, name+'.zip')" + '\n' )
  OoOOOo0o0ooo . write ( r'    try:' + '\n' )
  OoOOOo0o0ooo . write ( r'       os.remove(lib)' + '\n' )
  OoOOOo0o0ooo . write ( r'    except:' + '\n' )
  OoOOOo0o0ooo . write ( r'       pass' + '\n' )
  OoOOOo0o0ooo . write ( r'    downloader.download(url, lib, dp)' + '\n' )
  OoOOOo0o0ooo . write ( r"    addonfolder = xbmc.translatePath(os.path.join('special://','home'))" + '\n' )
  OoOOOo0o0ooo . write ( r'    time.sleep(2)' + '\n' )
  OoOOOo0o0ooo . write ( r'    dp.update(0,"", "Installing Your Build Please Wait")' + '\n' )
  OoOOOo0o0ooo . write ( r"    print '======================================='" + '\n' )
  OoOOOo0o0ooo . write ( r'    print addonfolder' + '\n' )
  OoOOOo0o0ooo . write ( r"    print '======================================='" + '\n' )
  OoOOOo0o0ooo . write ( r'    extract.all(lib,addonfolder,dp)' + '\n' )
  OoOOOo0o0ooo . write ( r'    dialog = xbmcgui.Dialog()' + '\n' )
  OoOOOo0o0ooo . write ( r'    dialog.ok("Your Media Centre", "[COLORred]Please Force Close Kodi To Take Effect If Pc Exit Task In TaskManager[/COLOR]","[COLORblue]Wizard Brought To You By Origin[/COLOR]")' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'def addDir(name,url,mode,iconimage,fanart,description):' + '\n' )
  OoOOOo0o0ooo . write ( r'        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)' + '\n' )
  OoOOOo0o0ooo . write ( r'        ok=True' + '\n' )
  OoOOOo0o0ooo . write ( r'        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)' + '\n' )
  OoOOOo0o0ooo . write ( r'        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )' + '\n' )
  OoOOOo0o0ooo . write ( r'        liz.setProperty( "Fanart_Image", fanart )' + '\n' )
  OoOOOo0o0ooo . write ( r'        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)' + '\n' )
  OoOOOo0o0ooo . write ( r'        return ok' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'def get_params():' + '\n' )
  OoOOOo0o0ooo . write ( r'        param=[]' + '\n' )
  OoOOOo0o0ooo . write ( r'        paramstring=sys.argv[2]' + '\n' )
  OoOOOo0o0ooo . write ( r'        if len(paramstring)>=2:' + '\n' )
  OoOOOo0o0ooo . write ( r'                params=sys.argv[2]' + '\n' )
  OoOOOo0o0ooo . write ( r"                cleanedparams=params.replace('?','')" + '\n' )
  OoOOOo0o0ooo . write ( r"                if (params[len(params)-1]=='/'):" + '\n' )
  OoOOOo0o0ooo . write ( r'                        params=params[0:len(params)-2]' + '\n' )
  OoOOOo0o0ooo . write ( r"                pairsofparams=cleanedparams.split('&')" + '\n' )
  OoOOOo0o0ooo . write ( r'                param={}' + '\n' )
  OoOOOo0o0ooo . write ( r'                for i in range(len(pairsofparams)):' + '\n' )
  OoOOOo0o0ooo . write ( r'                        splitparams={}' + '\n' )
  OoOOOo0o0ooo . write ( r"                        splitparams=pairsofparams[i].split('=')" + '\n' )
  OoOOOo0o0ooo . write ( r'                        if (len(splitparams))==2:' + '\n' )
  OoOOOo0o0ooo . write ( r'                                param[splitparams[0]]=splitparams[1]' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'        return param' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'params=get_params()' + '\n' )
  OoOOOo0o0ooo . write ( r'url=None' + '\n' )
  OoOOOo0o0ooo . write ( r'name=None' + '\n' )
  OoOOOo0o0ooo . write ( r'mode=None' + '\n' )
  OoOOOo0o0ooo . write ( r'iconimage=None' + '\n' )
  OoOOOo0o0ooo . write ( r'fanart=None' + '\n' )
  OoOOOo0o0ooo . write ( r'description=None' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'try:' + '\n' )
  OoOOOo0o0ooo . write ( r'        url=urllib.unquote_plus(params["url"])' + '\n' )
  OoOOOo0o0ooo . write ( r'except:' + '\n' )
  OoOOOo0o0ooo . write ( r'        pass' + '\n' )
  OoOOOo0o0ooo . write ( r'try:' + '\n' )
  OoOOOo0o0ooo . write ( r'        name=urllib.unquote_plus(params["name"])' + '\n' )
  OoOOOo0o0ooo . write ( r'except:' + '\n' )
  OoOOOo0o0ooo . write ( r'        pass' + '\n' )
  OoOOOo0o0ooo . write ( r'try:' + '\n' )
  OoOOOo0o0ooo . write ( r'        iconimage=urllib.unquote_plus(params["iconimage"])' + '\n' )
  OoOOOo0o0ooo . write ( r'except:' + '\n' )
  OoOOOo0o0ooo . write ( r'        pass' + '\n' )
  OoOOOo0o0ooo . write ( r'try:' + '\n' )
  OoOOOo0o0ooo . write ( r'        mode=int(params["mode"])' + '\n' )
  OoOOOo0o0ooo . write ( r'except:' + '\n' )
  OoOOOo0o0ooo . write ( r'        pass' + '\n' )
  OoOOOo0o0ooo . write ( r'try:' + '\n' )
  OoOOOo0o0ooo . write ( r'        fanart=urllib.unquote_plus(params["fanart"])' + '\n' )
  OoOOOo0o0ooo . write ( r'except:' + '\n' )
  OoOOOo0o0ooo . write ( r'        pass' + '\n' )
  OoOOOo0o0ooo . write ( r'try:' + '\n' )
  OoOOOo0o0ooo . write ( r'        description=urllib.unquote_plus(params["description"])' + '\n' )
  OoOOOo0o0ooo . write ( r'except:' + '\n' )
  OoOOOo0o0ooo . write ( r'        pass' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r"print str(PATH)+': '+str(VERSION)" + '\n' )
  OoOOOo0o0ooo . write ( r'print "Mode: "+str(mode)' + '\n' )
  OoOOOo0o0ooo . write ( r'print "URL: "+str(url)' + '\n' )
  OoOOOo0o0ooo . write ( r'print "Name: "+str(name)' + '\n' )
  OoOOOo0o0ooo . write ( r'print "IconImage: "+str(iconimage)' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'def setView(content, viewType):' + '\n' )
  OoOOOo0o0ooo . write ( r'    # set content type so library shows more views and info' + '\n' )
  OoOOOo0o0ooo . write ( r'    if content:' + '\n' )
  OoOOOo0o0ooo . write ( r'        xbmcplugin.setContent(int(sys.argv[1]), content)' + '\n' )
  OoOOOo0o0ooo . write ( r"    if ADDON.getSetting('auto-view')=='true':" + '\n' )
  OoOOOo0o0ooo . write ( '        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'if mode==None or url==None or len(url)<1:' + '\n' )
  OoOOOo0o0ooo . write ( r'        CATEGORIES()' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'elif mode==1:' + '\n' )
  OoOOOo0o0ooo . write ( r'        wizard(name,url,description)' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'' + '\n' )
  OoOOOo0o0ooo . write ( r'xbmcplugin.endOfDirectory(int(sys.argv[1]))' + '\n' )
  if 18 - 18: OO0O . Ii
  OoOOOo0o0ooo . close ( )
  if 40 - 40: O0 - OoooooooOO - OoOO
  self . addon_xml ( )
  if 37 - 37: oOoo / OOoo0O0 / O0
 def addon_xml ( self ) :
  if 76 - 76: Ii . ooO0O0O00 - OOOO00ooo0Ooo - OO0O * II11iII
  O0Oo00O = os . path . join ( self . save_path , self . addon_file_name )
  OOo0o000oO = open ( O0Oo00O , "w+" )
  if 99 - 99: OOooOooo * OOoo0O0 * OOO00OoOO00
  if 92 - 92: I1I
  OOo0o000oO . write ( r'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + '\n' )
  OOo0o000oO . write ( r'<addon id="plugin.video.' + self . clean_plugin_name + '" name="' + self . plugin_name + '" version="1.0.0" provider-name="Origin">' + '\n' )
  OOo0o000oO . write ( r'  <requires>' + '\n' )
  OOo0o000oO . write ( r'    <import addon="xbmc.python" version="2.1.0"/>' + '\n' )
  OOo0o000oO . write ( r'  </requires>' + '\n' )
  OOo0o000oO . write ( r'  <extension point="xbmc.python.pluginsource" library="default.py">' + '\n' )
  OOo0o000oO . write ( r'        <provides>video executable</provides>' + '\n' )
  OOo0o000oO . write ( r'  </extension>' + '\n' )
  OOo0o000oO . write ( r'  <extension point="xbmc.addon.metadata">' + '\n' )
  OOo0o000oO . write ( r'    <summary lang="en">An installer for ' + self . plugin_name + '</summary>' + '\n' )
  OOo0o000oO . write ( r'    <description lang="en">Generated by Origins mod of original Wizard template for ' + self . plugin_name + '</description>' + '\n' )
  OOo0o000oO . write ( r'    <platform>all</platform>' + '\n' )
  OOo0o000oO . write ( r'  </extension>' + '\n' )
  OOo0o000oO . write ( r'</addon>' + '\n' )
  if 40 - 40: oOoo / OoOO
  OOo0o000oO . close ( )
  self . Delay ( )
  if 79 - 79: II11iII - iIii1I11I1II1 + o0OOOoO0 - OOO00OoOO00
 def Delay ( self ) :
  os . rename ( IIi + 'TEST' , IIi + 'plugin.video.' + self . clean_plugin_name )
  I1i1iiI1 . create ( "[COLORwhite]Origin[/COLOR]" , "Writing Files" , '' , 'Please Wait' )
  time . sleep ( 1 )
  self . Backup_Wizard ( )
  if 93 - 93: OOoo0O0 . Ii - I1I + oOoo
 def Backup_Wizard ( self ) :
  if 61 - 61: OOoo0O0
  o0oOO ( )
  Ii1ii111i1 = xbmc . translatePath ( os . path . join ( iIii1 , 'plugin.video.' + self . clean_plugin_name + '.zip' ) )
  i1i1i1I = IIi
  I1i1iiI1 . create ( "[COLOR=white]Origin[/COLOR]" , "Backing Up" , '' , 'Please Wait' )
  oOoo000 = zipfile . ZipFile ( Ii1ii111i1 , 'w' , zipfile . ZIP_DEFLATED )
  OooOo00o = len ( i1i1i1I )
  IiI11i1IIiiI = [ ]
  oOOo000oOoO0 = [ ]
  for IIIII , iIi11i1 , oO00oo0o00o0o in os . walk ( i1i1i1I ) :
   for file in oO00oo0o00o0o :
    oOOo000oOoO0 . append ( file )
  OoOo00o0OO = len ( oOOo000oOoO0 )
  for IIIII , iIi11i1 , oO00oo0o00o0o in os . walk ( i1i1i1I ) :
   for file in oO00oo0o00o0o :
    IiI11i1IIiiI . append ( file )
    ii1IIIIiI11 = len ( IiI11i1IIiiI ) / float ( OoOo00o0OO ) * 100
    I1i1iiI1 . update ( int ( ii1IIIIiI11 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    iI1IIIii = os . path . join ( IIIII , file )
    if not 'temp' in iIi11i1 :
     if not 'plugin.video.originwizard' in iIi11i1 :
      import time
      I1i11ii11 = '01/01/1980'
      OO00O0oOO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iI1IIIii ) ) )
      if OO00O0oOO > I1i11ii11 :
       oOoo000 . write ( iI1IIIii , iI1IIIii [ OooOo00o : ] )
  oOoo000 . close ( )
  I1i1iiI1 . close ( )
  os . rename ( IIi + 'plugin.video.' + self . clean_plugin_name , IIi + 'TEST' )
  IIIi11I11 . ok ( "[COLOR=white]Origin[/COLOR]" , "Your wizard is now created" , '' , '' )
  if 4 - 4: OoooooooOO - i1IIi % o0OOOoO0 - O00oo0OO0oOOO * iIii11I
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . OO0O / OoooooooOO % Ii % O0
I1iii = i1i111iI ( '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
if 86 - 86: OOOO00ooo0Ooo * O0 * OoOO
def OoO000O0Oo ( url ) :
 oOOoO0o0oO = urllib2 . Request ( url )
 Ooo0oo = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
 IIi11IIiIii1 = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
 I1iIII1 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
 iIii = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
 oOOoO0o0oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0Oo0oO0oOO00 = urllib2 . urlopen ( oOOoO0o0oO )
 o0oO0O0o0O00O = o0Oo0oO0oOO00 . read ( )
 o0Oo0oO0oOO00 . close ( )
 return o0oO0O0o0O00O
 if 84 - 84: OOooOooo % i1IIi
 if 70 - 70: I1I . OoooooooOO - OO0O
def iIiiii ( ) :
 if 30 - 30: OOOO00ooo0Ooo % Ii
 IIIi11I11 . ok ( "[COLOR=white]Naughty Naughty[/COLOR]" , "You are the weakest link goodbye" , '' , '' )
 O0Oo00O = os . path . join ( iIi1ii1I1 , 'default.py' )
 O0Oo00 = open ( O0Oo00O , "w+" )
 if 41 - 41: iIii1I11I1II1 % i1i1i11IIi
 O0Oo00 . write ( r'This Build Can NOT be Copied' )
 if 59 - 59: O00oo0OO0oOOO + i11iIiiIii
def oo0OOo0O ( content , viewType ) :
 if 39 - 39: OoooooooOO + OOooOooo % O00oo0OO0oOOO / O00oo0OO0oOOO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if i1iII1IiiIiI1 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % i1iII1IiiIiI1 . getSetting ( viewType ) )
  if 27 - 27: OO0O . i1i1i11IIi . iIii1I11I1II1 . iIii1I11I1II1
if iIIiiI1II1i11 == None or OooooOOoo0 == None or len ( OooooOOoo0 ) < 1 :
 I1111I1iII11 ( )
elif iIIiiI1II1i11 == 'addon_removal_menu' : IIi1I1Ii11iI ( )
elif iIIiiI1II1i11 == 'addonfix' : addonfix . fixes ( )
elif iIIiiI1II1i11 == 'addonfixes' : iIIIi1 ( )
elif iIIiiI1II1i11 == 'addonmenu' : Addon_Menu ( )
elif iIIiiI1II1i11 == 'addon_settings' : oOOOoO0O00o0 ( )
elif iIIiiI1II1i11 == 'backup' : BACKUP ( )
elif iIIiiI1II1i11 == 'backup_option' : communitybuilds . Backup_Option ( )
elif iIIiiI1II1i11 == 'backup_restore' : OOoOO0oo0ooO ( )
elif iIIiiI1II1i11 == 'adultmenu' : AdultMenu ( )
elif iIIiiI1II1i11 == 'buildmenu' : O0Oo0oOOoooOOOOo ( )
elif iIIiiI1II1i11 == 'categories' : I1111I1iII11 ( )
elif iIIiiI1II1i11 == 'clear_cache' : i1O0OoO0o ( )
elif iIIiiI1II1i11 == 'community_backup' : communitybuilds . Community_Backup ( )
elif iIIiiI1II1i11 == 'community_menu' : communitybuilds . Community_Menu ( OooooOOoo0 , OOo0O0oo0OO0O )
elif iIIiiI1II1i11 == 'description' : communitybuilds . Description ( I11i1I1I , OooooOOoo0 , OOO0000oO , Iii1 , ii1I1i11 , i1I1IiiIi1i , ooo00Ooo , iI1i11 , OO0 , OO0oo , IIii1111 , Iiii1iI1i , OoOOoooOO0O , oOIIiIi )
elif iIIiiI1II1i11 == 'fix_special' : communitybuilds . Fix_Special ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'genres' : Genres ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'grab_addons' : addons . Grab_Addons ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'grab_builds_premium' : communitybuilds . Grab_Builds_Premium ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'guisettingsfix' : communitybuilds . GUI_Settings_Fix ( OooooOOoo0 , OOOoOO )
elif iIIiiI1II1i11 == 'guisettings' : guisettings ( )
elif iIIiiI1II1i11 == 'hide_passwords' : extras . Hide_Passwords ( )
elif iIIiiI1II1i11 == 'LocalGUIDialog' : communitybuilds . Local_GUI_Dialog ( )
elif iIIiiI1II1i11 == 'remove_addon_data' : O0o ( )
elif iIIiiI1II1i11 == 'remove_addons' : extras . Remove_Addons ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'remove_build' : extras . Remove_Build ( )
elif iIIiiI1II1i11 == 'remove_crash_logs' : o0O0OOO0Ooo ( )
elif iIIiiI1II1i11 == 'remove_packages' : OO00O0O ( )
elif iIIiiI1II1i11 == 'remove_textures' : oOiIi1IIIi1 ( )
elif iIIiiI1II1i11 == 'restore' : extras . RESTORE ( )
elif iIIiiI1II1i11 == 'restore_backup' : communitybuilds . Restore_Backup_XML ( I11i1I1I , OooooOOoo0 , i1I1IiiIi1i )
elif iIIiiI1II1i11 == 'restore_local_CB' : communitybuilds . Restore_Local_Community ( )
elif iIIiiI1II1i11 == 'restore_local_gui' : communitybuilds . Restore_Local_GUI ( )
elif iIIiiI1II1i11 == 'restore_option' : communitybuilds . Restore_Option ( )
elif iIIiiI1II1i11 == 'restore_zip' : communitybuilds . Restore_Zip_File ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'restore_community' : communitybuilds . Restore_Community ( I11i1I1I , OooooOOoo0 , OOo0O0oo0OO0O , i1I1IiiIi1i , iI1i11 , OOoOooOoOOOoo )
elif iIIiiI1II1i11 == 'showinfo' : communitybuilds . Show_Info ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'SortBy' : extras . Sort_By ( BuildURL , type )
elif iIIiiI1II1i11 == 'text_guide' : news . Text_Guide ( I11i1I1I , OooooOOoo0 )
elif iIIiiI1II1i11 == 'tools' : IiI111111IIII ( )
elif iIIiiI1II1i11 == 'unhide_passwords' : extras . Unhide_Passwords ( )
elif iIIiiI1II1i11 == 'update' : addons . Update_Repo ( )
elif iIIiiI1II1i11 == 'uploadlog' : extras . Upload_Log ( )
elif iIIiiI1II1i11 == 'user_info' : Show_User_Info ( )
elif iIIiiI1II1i11 == 'wipetools' : oOOOoo0O0oO ( )
elif iIIiiI1II1i11 == 'xbmcversion' : extras . XBMC_Version ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'wipe_xbmc' : I1i11i ( )
elif iIIiiI1II1i11 == 'wizard' : o0000oO ( I11i1I1I , OooooOOoo0 , i1I1IiiIi1i )
elif iIIiiI1II1i11 == 'Merlin' : o00oO0oOo00 ( )
elif iIIiiI1II1i11 == 'Text_Gen' : i1i111iI ( '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , 'textFile' )
elif iIIiiI1II1i11 == 'Wizard_Gen' : i1i111iI ( '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , 'newWizard' )
elif iIIiiI1II1i11 == 'How_To' : ooO0oOOooOo0 ( )
elif iIIiiI1II1i11 == 'Addon_Cat' : O0o0O0 ( )
elif iIIiiI1II1i11 == 'Addon' : I1I1i ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'Addon_Extract' : ii1iIi1iIiI1i ( OooooOOoo0 , I11i1I1I )
elif iIIiiI1II1i11 == 'Repo' : iiIi1i ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'Search_Addons' : Iii1iiIi1II ( )
elif iIIiiI1II1i11 == 'Addons_Menu' : iII1ii1 ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
