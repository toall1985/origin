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
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
IiII1IiiIiI1 = 'special://home/resources/art/' + os . sep
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
iIi1ii1I1 = 'None'
o0 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
I11II1i = 'http://rh-project.info/'
IIIII = "2.0.3"
ooooooO0oo = "originwizard"
if 49 - 49: ooo * I1I1i / IIIii1I1 * Ii + oo0O0oOOO00oO
if 61 - 61: iiiiiIIii * o00OO0OOO0 % i1Iii % OOooOooo % O000oo0O
if 66 - 66: OoOo00o / IIIii1II1II % iI1iI1I1i1I + Ii11Ii1I / oo0O0oOOO00oO % II111iiii
def OOO0 ( ) :
 for file in glob . glob ( os . path . join ( O0O , '*' ) ) :
  Oo0O0O0ooO0O = str ( file ) . replace ( O0O , '[COLOR=red]REMOVE [/COLOR]' ) . replace ( 'plugin.' , '[COLOR=dodgerblue](PLUGIN) [/COLOR]' ) . replace ( 'audio.' , '' ) . replace ( 'video.' , '' ) . replace ( 'skin.' , '[COLOR=yellow](SKIN) [/COLOR]' ) . replace ( 'repository.' , '[COLOR=orange](REPOSITORY) [/COLOR]' ) . replace ( 'script.' , '[COLOR=cyan](SCRIPT) [/COLOR]' ) . replace ( 'metadata.' , '[COLOR=gold](METADATA) [/COLOR]' ) . replace ( 'service.' , '[COLOR=pink](SERVICE) [/COLOR]' ) . replace ( 'weather.' , '[COLOR=green](WEATHER) [/COLOR]' ) . replace ( 'module.' , '[COLOR=gold](MODULE) [/COLOR]' )
  IIIIii = ( os . path . join ( file , 'icon.png' ) )
  O0o0 = ( os . path . join ( file , 'fanart.jpg' ) )
  extras . addDir ( '' , Oo0O0O0ooO0O , file , 'remove_addons' , IIIIii , O0o0 , '' , '' )
  if 71 - 71: i1Iii + Ii11Ii1I % i11iIiiIii + iiiiiIIii - IIIii1II1II
  if 88 - 88: Ii - IIIii1I1 % i1Iii
def iI1I111Ii111i ( ) :
 iIiiiI1IiI1I1 . openSettings ( sys . argv [ 0 ] )
 if 7 - 7: Ii11Ii1I * IIIii1I1 % o00OO0OOO0 . IIIii1II1II
 if 45 - 45: i11iIiiIii * II111iiii % iIii1I11I1II1 + iiiiiIIii - O000oo0O
def iIi1iIiii111 ( ) :
 extras . addDir ( 'folder' , 'Completely remove an add-on (inc. passwords)' , 'plugin' , 'addon_removal_menu' , 'Remove_Addon.png' , '' , '' , '' )
 extras . addDir ( '' , 'Hide my add-on passwords' , 'none' , 'hide_passwords' , 'Hide_Passwords.png' , '' , '' , '' )
 extras . addDir ( '' , 'Unhide my add-on passwords' , 'none' , 'unhide_passwords' , 'Unhide_Passwords.png' , '' , '' , '' )
 extras . addDir ( '' , 'Update My Add-ons (Force Refresh)' , 'none' , 'update' , 'Update_Addons.png' , '' , '' , '' )
 extras . addDir ( '' , 'Wipe All Add-on Settings (addon_data)' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 if 16 - 16: iiiiiIIii + IIIii1I1 - II111iiii
 if 85 - 85: Ii + i1IIi
 if 58 - 58: II111iiii * i1Iii * iiiiiIIii / i1Iii
def oO0o0OOOO ( ) :
 extras . addDir ( 'folder' , 'Backup My Content' , 'none' , 'backup_option' , 'Backup.png' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Restore My Content' , 'none' , 'restore_option' , 'Restore.png' , '' , '' , '' )
 if 68 - 68: OoOo00o - iI1iI1I1i1I - ooo - iiiiiIIii + OOooOooo
 if 10 - 10: OoooooooOO % iIii1I11I1II1
def O00o0O00 ( ) :
 ii111111I1iII = 0
 O00ooo0O0 = iIiiiI1IiI1I1 . getSetting ( 'maintenance' )
 i1iIi1iIi1i = iIiiiI1IiI1I1 . getSetting ( 'mainmenu' )
 I1I1iIiII1 = iIiiiI1IiI1I1 . getSetting ( 'guisettings' )
 i11i1I1 = iIiiiI1IiI1I1 . getSetting ( 'adultbuilds' )
 if i1iIi1iIi1i == 'true' :
  extras . addDir ( 'folder' , 'Origin Builds' , 'none' , 'buildmenu' , 'Build_Menu.png' , '' , '' , '' )
 if i11i1I1 == 'true' :
  extras . addDir ( 'folder' , 'Adult Builds' , 'none' , 'adultmenu' , 'Adult_Menu.png' , '' , '' , '' )
 if I1I1iIiII1 == 'true' :
  extras . addDir ( 'folder' , 'Gui Settings XML' , 'none' , 'guisettings' , 'Gui_Menu.png' , '' , '' , '' )
 if O00ooo0O0 == 'true' :
  extras . addDir ( 'folder' , 'Maintenance' , 'none' , 'tools' , 'Tools.png' , '' , '' , '' )
  if 36 - 36: iIii1I11I1II1 / Ii * i1Iii
  if 65 - 65: O000oo0O . iIii1I11I1II1 / O0 - O000oo0O
  if 21 - 21: ooo * iIii1I11I1II1
def oooooOoo0ooo ( ) :
 I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( 'Clear All Known Cache?' , 'This will clear all known cache files and can help' , 'if you\'re encountering kick-outs during playback.' , 'as well as other random issues. There is no harm in using this.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if I1I1IiI1 == 1 :
  cache . Wipe_Cache ( )
  III1iII1I1ii ( )
  if 61 - 61: II111iiii
  if 64 - 64: Ii11Ii1I / Ii - O0 - OOooOooo
def O0oOoOOOoOO ( ) :
 ii1ii11IIIiiI = [ ]
 O00OOOoOoo0O = sys . argv [ 2 ]
 if len ( O00OOOoOoo0O ) >= 2 :
  O000OOo00oo = sys . argv [ 2 ]
  oo0OOo = O000OOo00oo . replace ( '?' , '' )
  if ( O000OOo00oo [ len ( O000OOo00oo ) - 1 ] == '/' ) :
   O000OOo00oo = O000OOo00oo [ 0 : len ( O000OOo00oo ) - 2 ]
  ooOOO00Ooo = oo0OOo . split ( '&' )
  ii1ii11IIIiiI = { }
  for IiIIIi1iIi in range ( len ( ooOOO00Ooo ) ) :
   ooOOoooooo = { }
   ooOOoooooo = ooOOO00Ooo [ IiIIIi1iIi ] . split ( '=' )
   if ( len ( ooOOoooooo ) ) == 2 :
    ii1ii11IIIiiI [ ooOOoooooo [ 0 ] ] = ooOOoooooo [ 1 ]
    if 1 - 1: I1I1i / oo0O0oOOO00oO % OoOo00o * IIIii1II1II . i11iIiiIii
 return ii1ii11IIIiiI
 if 2 - 2: iiiiiIIii * OOooOooo - iIii1I11I1II1 + ooo . o00OO0OOO0 % OoOo00o
 if 92 - 92: OoOo00o
def IIiIiiIi ( ) :
 I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( 'Delete Addon_Data Folder?' , 'This will free up space by deleting your addon_data' , 'folder. This contains all addon related settings' , 'including username and password info.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if I1I1IiI1 == 1 :
  extras . Delete_Userdata ( )
  I1i1iiI1 . ok ( "Addon_Data Removed" , '' , 'Your addon_data folder has now been removed.' , '' )
  if 51 - 51: OOooOooo + OoOo00o % iIii1I11I1II1 / o00OO0OOO0 / i1Iii % OoooooooOO
  if 78 - 78: O000oo0O % iI1iI1I1i1I + iiiiiIIii
def OOooOoooOoOo ( ) :
 I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( 'Remove All Crash Logs?' , 'There is absolutely no harm in doing this, these are' , 'log files generated when Kodi crashes and are' , 'only used for debugging purposes.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if I1I1IiI1 == 1 :
  extras . Delete_Logs ( )
  I1i1iiI1 . ok ( "Crash Logs Removed" , '' , 'Your crash log files have now been removed.' , '' )
  if 84 - 84: IIIii1II1II
  if 86 - 86: Ii - O000oo0O - IIIii1I1 * OoOo00o
def oooo0O0 ( ) :
 I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( 'Delete Packages Folder?' , 'This will free up space by deleting the zip install' , 'files of your addons. The only downside is you\'ll no' , 'longer be able to rollback to older versions.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if I1I1IiI1 == 1 :
  extras . Delete_Packages ( )
  I1i1iiI1 . ok ( "Packages Removed" , '' , 'Your zip install files have now been removed.' , '' )
  if 51 - 51: IIIii1I1 / IIIii1I1
  if 53 - 53: I1I1i
def III1iII1I1ii ( ) :
 I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( 'Clear Cached Images?' , 'This will clear your textures13.db file and remove' , 'your Thumbnails folder. These will automatically be' , 'repopulated after a restart.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if I1I1IiI1 == 1 :
  cache . Remove_Textures ( )
  extras . Destroy_Path ( i11 )
  I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( 'Quit Kodi Now?' , 'Cache has been successfully deleted.' , 'You must now restart Kodi, would you like to quit now?' , '' , nolabel = 'I\'ll restart later' , yeslabel = 'Yes, quit' )
  if I1I1IiI1 == 1 :
   iI1Iii ( )
   if 68 - 68: i1Iii % iI1iI1I1i1I
   if 88 - 88: iIii1I11I1II1 - Ii11Ii1I + i1Iii
def IiI111111IIII ( ) :
 extras . addDir ( 'folder' , '[COLOR white]Addon Installer[/COLOR]' , 'none' , 'Addons_Menu' , '' , '' , '' , '' )
 extras . addDir ( 'wizard' , '[COLOR red]Wizard Generator[/COLOR]' , 'none' , 'Merlin' , IiII1IiiIiI1 + 'icon.png' , IiII1IiiIiI1 + 'fanart.jpg' , '' , '' )
 extras . addDir ( 'folder' , 'Add-on Maintenance/Fixes' , 'none' , 'addonfixes' , '' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Backup/Restore My Content' , 'none' , 'backup_restore' , '' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Clean/Wipe Options' , 'none' , 'wipetools' , '' , '' , '' , '' )
 extras . addDir ( '' , 'Check XBMC/Kodi Version' , 'none' , 'xbmcversion' , '' , '' , '' , '' )
 extras . addDir ( '' , 'Convert Physical Paths To Special' , o0oO0 , 'fix_special' , '' , '' , '' , '' )
 extras . addDir ( '' , 'Force Close Kodi' , 'url' , 'kill_xbmc' , '' , '' , '' , '' )
 if 37 - 37: iI1iI1I1i1I / Ii
 if 23 - 23: O0
def o00oO0oOo00 ( ) :
 extras . addDir ( 'wizard2' , '[COLOR red]How To Guide[/COLOR]' , 'none' , 'How_To' , IiII1IiiIiI1 + 'icon.png' , IiII1IiiIiI1 + 'fanart.jpg' , '' , '' )
 extras . addDir ( 'wizard2' , '[COLOR white]Generate Txt File to Host online[/COLOR]' , 'none' , 'Text_Gen' , IiII1IiiIiI1 + 'icon.png' , IiII1IiiIiI1 + 'fanart.jpg' , '' , '' )
 extras . addDir ( 'wizard2' , '[COLOR blue]Generate your personalised wizard[/COLOR]' , 'none' , 'Wizard_Gen' , IiII1IiiIiI1 + 'icon.png' , IiII1IiiIiI1 + 'fanart.jpg' , '' , '' )
 if 81 - 81: IIIii1I1
 if 42 - 42: IIIii1I1 / OOooOooo / oo0O0oOOO00oO + OoOo00o / Ii
 if 84 - 84: Ii11Ii1I * II111iiii + I1I1i
 if 53 - 53: OoOo00o % II111iiii . IIIii1II1II - iIii1I11I1II1 - IIIii1II1II * II111iiii
def ooO0oOOooOo0 ( ) :
 i1I1ii11i1Iii ( 'How To guide For Wizard Creation' , '1: First you will need to create a build and host somewhere online that it can be accessed\n\n\n2: Then you can run the Generate Txt File which will be what your wizard talks to in order to collect information about your build(s)\n\n\n3: Once Generated Host this file online somewhere so can be accessed by wizard\n\n\n4: Run the wizard generator and fill in relevant fields\n\n\n5: Get your zip and host online that will become your url that can be put into source in kodi\n\n\n6: Enjoy and do not forget to thank the devs, maybe donate to help them help you and visit some streaming sites suffer some ads to help keep them going aswell\n\n\n[COLORred]If you wish to add another build into your wizard simply duplicate the information in the .txt file thats generated then edit the information. May look at adding a funtion so you can add more builds easily in future[/COLOR]' )
 if 26 - 26: OOooOooo - iIii1I11I1II1 - ooo / IIIii1I1 . Ii % iIii1I11I1II1
 if 91 - 91: oo0O0oOOO00oO . iIii1I11I1II1 / o00OO0OOO0 + i1IIi
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
 if 5 - 5: Ii11Ii1I - II111iiii - OoooooooOO % O000oo0O + ooo * iIii1I11I1II1
 if 37 - 37: IIIii1II1II % Ii11Ii1I + Ii + oo0O0oOOO00oO * OOooOooo % O0
 if 61 - 61: ooo - i1Iii . o00OO0OOO0 / i1Iii + I1I1i
def I1i11i ( ) :
 o00oO0oo0OO = xbmc . translatePath ( os . path . join ( oOOoO0 , 'Community Builds' , 'My Builds' ) )
 I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( "ABSOLUTELY CERTAIN?!!!" , 'Are you absolutely certain you want to wipe?' , '' , 'All addons and settings will be completely wiped!' , yeslabel = 'Yes' , nolabel = 'No' )
 if I1I1IiI1 == 1 :
  if Ooo != "skin.confluence" :
   I1i1iiI1 . ok ( '[COLOR=white]Origin[/COLOR]' , 'Please switch to the default Confluence skin' , 'before performing a wipe.' , '' )
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
   return
  else :
   I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( "VERY IMPORTANT" , 'This will completely wipe your install.' , 'Would you like to create a backup before proceeding?' , '' , yeslabel = 'No' , nolabel = 'Yes' )
   if I1I1IiI1 == 0 :
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
    communitybuilds . Archive_Tree ( o0oO0 , Ii1I1Ii , o00O0 , oOO0O00Oo0O0o , ii1 , I1iIIiiIIi1i , OOoO0 , OO0Oooo0oOO0O )
   I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( "Remove Origin Wizard?" , 'Do you also want to remove the Origin Wizard' , 'add-on and have a complete fresh start or would you' , 'prefer to keep this on your system?' , yeslabel = 'Remove' , nolabel = 'Keep' )
   if I1I1IiI1 == 0 :
    cache . Remove_Textures ( )
    O0O0ooOOO = xbmc . translatePath ( os . path . join ( O0O , o0OoOoOO00 , '' ) )
    oOOo0O00o = xbmc . translatePath ( os . path . join ( o0oO0 , '..' , 'originwizard.zip' ) )
    communitybuilds . Archive_File ( O0O0ooOOO , oOOo0O00o )
    iIiIi11 = xbmc . translatePath ( os . path . join ( O0O , 'script.module.addon.common' , '' ) )
    OOO = xbmc . translatePath ( os . path . join ( o0oO0 , '..' , 'originwizarddep.zip' ) )
    communitybuilds . Archive_File ( iIiIi11 , OOO )
    extras . Destroy_Path ( o0oO0 )
    if not os . path . exists ( O0O0ooOOO ) :
     os . makedirs ( O0O0ooOOO )
    if not os . path . exists ( iIiIi11 ) :
     os . makedirs ( iIiIi11 )
    time . sleep ( 1 )
    communitybuilds . Read_Zip ( oOOo0O00o )
    iiIIIII1i1iI . create ( "[[COLOR=white]Origin[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
    iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
    extract . all ( oOOo0O00o , O0O0ooOOO , iiIIIII1i1iI )
    communitybuilds . Read_Zip ( OOO )
    extract . all ( OOO , iIiIi11 , iiIIIII1i1iI )
    iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
    iiIIIII1i1iI . close ( )
    time . sleep ( 1 )
    extras . Kill_XBMC ( )
   elif I1I1IiI1 == 1 :
    cache . Remove_Textures ( )
    extras . Destroy_Path ( o0oO0 )
    iiIIIII1i1iI . close ( )
    extras . Kill_XBMC ( )
   else : return
   if 32 - 32: i1IIi / II111iiii . I1I1i
   if 62 - 62: OoooooooOO * ooo
def oOOOoo0O0oO ( ) :
 extras . addDir ( '' , 'Clear Cache' , 'url' , 'clear_cache' , 'Clear_Cache.png' , '' , '' , '' )
 extras . addDir ( '' , 'Clear My Cached Artwork' , 'none' , 'remove_textures' , 'Delete_Cached_Artwork.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Addon_Data' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Old Builds/Zips From Device' , 'url' , 'remove_build' , 'Delete_Builds.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Old Crash Logs' , 'url' , 'remove_crash_logs' , 'Delete_Crash_Logs.png' , '' , '' , '' )
 extras . addDir ( '' , 'Delete Packages Folder' , 'url' , 'remove_packages' , 'Delete_Packages.png' , '' , '' , '' )
 extras . addDir ( '' , 'Wipe My Install (Fresh Start)' , 'none' , 'wipe_xbmc' , 'Fresh_Start.png' , '' , '' , '' )
 if 6 - 6: i1Iii * oo0O0oOOO00oO + OoOo00o
 if 44 - 44: O000oo0O % IIIii1I1 + OoooooooOO - O0 - O000oo0O - II111iiii
def O0Oo0oOOoooOOOOo ( ) :
 o0oO0O0o0O00O = OoO000O0Oo ( 'http://back2basicsbuild.co.uk/wizard/toolbox.xml' ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo0o0oooo0O0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0oO0O0o0O00O )
 for Oo0O0O0ooO0O , OooooOOoo0 , IIIIii , O0o0 , i1I1IiiIi1i in Oo0o0oooo0O0 :
  iiI11ii1I1 ( Oo0O0O0ooO0O , OooooOOoo0 , 'wizard' , IIIIii , O0o0 , i1I1IiiIi1i )
 Ooo0OOoOoO0 ( '500' )
 if 70 - 70: o00OO0OOO0
def OoO000O0Oo ( url ) :
 oOOoO0o0oO = urllib2 . Request ( url )
 oOOoO0o0oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0Oo0oO0oOO00 = urllib2 . urlopen ( oOOoO0o0oO )
 o0oO0O0o0O00O = o0Oo0oO0oOO00 . read ( )
 o0Oo0oO0oOO00 . close ( )
 return o0oO0O0o0O00O
 if 92 - 92: OoooooooOO * iI1iI1I1i1I
def o0000oO ( name , url , description ) :
 I1II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iiIIIII1i1iI = xbmcgui . DialogProgress ( )
 iiIIIII1i1iI . create ( "origin wizard" , "Downloading " , '' , 'Please Wait' )
 oooO = os . path . join ( I1II1 , name + '.zip' )
 try :
  os . remove ( oooO )
 except :
  pass
 downloader . download ( url , oooO , iiIIIII1i1iI )
 i1I1i111Ii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I1i111Ii
 print '======================================='
 extract . all ( oooO , i1I1i111Ii , iiIIIII1i1iI )
 I1i1iiI1 = xbmcgui . Dialog ( )
 I1i1iiI1 . ok ( "DOWNLOAD COMPLETE" , 'To ensure all changes are saved you must now close Kodi' , 'to force close Kodi. Click ok,' , 'DO NOT use the quit/exit options in Kodi.' )
 iI1Iii ( )
 if 67 - 67: ooo . i1IIi
def iI1Iii ( ) :
 I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if I1I1IiI1 == 0 :
  return
 elif I1I1IiI1 == 1 :
  pass
 i1i1iI1iiiI = Ooo0oOooo0 ( )
 print "Platform: " + str ( i1i1iI1iiiI )
 if i1i1iI1iiiI == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  I1i1iiI1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
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
  I1i1iiI1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
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
  I1i1iiI1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
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
  if 61 - 61: Ii - i1Iii - i1IIi
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
  if 25 - 25: O0 * OOooOooo + iiiiiIIii . oo0O0oOOO00oO . oo0O0oOOO00oO
  if 58 - 58: ooo
def iiI11ii1I1 ( name , url , mode , iconimage , fanart , description ) :
 oOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoO00O0 = True
 OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OO . setProperty ( "Fanart_Image" , fanart )
 oOoO00O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoO , listitem = OO , isFolder = False )
 return oOoO00O0
 if 7 - 7: O0 * i11iIiiIii * O000oo0O + Ii11Ii1I % IIIii1I1 - Ii11Ii1I
def Ooo0OOoOoO0 ( content = '' ) :
 if not content :
  return
  if 39 - 39: I1I1i * i1Iii % i1Iii - OoooooooOO + oo0O0oOOO00oO - OOooOooo
 xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if iIiiiI1IiI1I1 . getSetting ( 'auto-view' ) != 'true' :
  return
  if 23 - 23: i11iIiiIii
 if content == 'addons' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % iIiiiI1IiI1I1 . getSetting ( 'addon_view' ) )
 else :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % iIiiiI1IiI1I1 . getSetting ( 'default-view' ) )
  if 30 - 30: oo0O0oOOO00oO - i1IIi % II111iiii + OOooOooo * iIii1I11I1II1
  if 81 - 81: IIIii1II1II % i1IIi . iIii1I11I1II1
O000OOo00oo = O0oOoOOOoOO ( )
Ii1Iii1iIi = None
OO0oo = None
Iii1 = None
OOO0000oO = None
iI1i111I1Ii = None
i1I1IiiIi1i = None
i11i1ii1I = None
o0OO0o0o00o = None
O0o0 = None
oOo0 = None
IIIIii = None
o0oO0O0o0O00O = None
OOOoOO = None
I11IIIi = None
iIIiiI1II1i11 = None
Oo0O0O0ooO0O = None
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
oooiiI = None
if 56 - 56: I1I1i . iiiiiIIii . ooo
try : Ii1Iii1iIi = urllib . unquote_plus ( O000OOo00oo [ "addon_id" ] )
except : pass
try : ii111I = urllib . unquote_plus ( O000OOo00oo [ "adult" ] )
except : pass
try : OO0oo = urllib . unquote_plus ( O000OOo00oo [ "audioaddons" ] )
except : pass
try : Iii1 = urllib . unquote_plus ( O000OOo00oo [ "author" ] )
except : pass
try : OOO0000oO = urllib . unquote_plus ( O000OOo00oo [ "buildname" ] )
except : pass
try : iI1i111I1Ii = urllib . unquote_plus ( O000OOo00oo [ "data_path" ] )
except : pass
try : i1I1IiiIi1i = urllib . unquote_plus ( O000OOo00oo [ "description" ] )
except : pass
try : i11i1ii1I = urllib . unquote_plus ( O000OOo00oo [ "DOB" ] )
except : pass
try : o0OO0o0o00o = urllib . unquote_plus ( O000OOo00oo [ "email" ] )
except : pass
try : O0o0 = urllib . unquote_plus ( O000OOo00oo [ "fanart" ] )
except : pass
try : oOo0 = urllib . unquote_plus ( O000OOo00oo [ "forum" ] )
except : pass
try : iiI = urllib . unquote_plus ( O000OOo00oo [ "guisettingslink" ] )
except : pass
try : IIIIii = urllib . unquote_plus ( O000OOo00oo [ "iconimage" ] )
except : pass
try : o0oO0O0o0O00O = urllib . unquote_plus ( O000OOo00oo [ "link" ] )
except : pass
try : OOOoOO = urllib . unquote_plus ( O000OOo00oo [ "local" ] )
except : pass
try : I11IIIi = urllib . unquote_plus ( O000OOo00oo [ "messages" ] )
except : pass
try : iIIiiI1II1i11 = str ( O000OOo00oo [ "mode" ] )
except : pass
try : Oo0O0O0ooO0O = urllib . unquote_plus ( O000OOo00oo [ "name" ] )
except : pass
try : iIiiiII = urllib . unquote_plus ( O000OOo00oo [ "pictureaddons" ] )
except : pass
try : o0o0 = urllib . unquote_plus ( O000OOo00oo [ "posts" ] )
except : pass
try : IIii1111 = urllib . unquote_plus ( O000OOo00oo [ "programaddons" ] )
except : pass
try : I1iI = urllib . unquote_plus ( O000OOo00oo [ "provider_name" ] )
except : pass
try : I11iiiiI1i = urllib . unquote_plus ( O000OOo00oo [ "repo_link" ] )
except : pass
try : IIIIiIiIi1 = urllib . unquote_plus ( O000OOo00oo [ "repo_id" ] )
except : pass
try : iI1i11 = urllib . unquote_plus ( O000OOo00oo [ "skins" ] )
except : pass
try : OoOOoooOO0O = urllib . unquote_plus ( O000OOo00oo [ "sources" ] )
except : pass
try : ooo00Ooo = urllib . unquote_plus ( O000OOo00oo [ "updated" ] )
except : pass
try : Oo0o0O00 = urllib . unquote_plus ( O000OOo00oo [ "unread" ] )
except : pass
try : OooooOOoo0 = urllib . unquote_plus ( O000OOo00oo [ "url" ] )
except : pass
try : ii1I1i11 = urllib . unquote_plus ( O000OOo00oo [ "version" ] )
except : pass
try : OOo0O0oo0OO0O = urllib . unquote_plus ( O000OOo00oo [ "video" ] )
except : pass
try : OO0 = urllib . unquote_plus ( O000OOo00oo [ "videoaddons" ] )
except : pass
try : oooiiI = urllib . unquote_plus ( O000OOo00oo [ "zip_link" ] )
except : pass
if 20 - 20: ooo
print str ( ooooooO0oo ) + ': ' + str ( IIIII )
print "Mode: " + str ( iIIiiI1II1i11 )
print "URL: " + str ( OooooOOoo0 )
print "Name: " + str ( Oo0O0O0ooO0O )
print "IconImage: " + str ( IIIIii )
if 95 - 95: OoOo00o - ooo
if 34 - 34: Ii11Ii1I * ooo . i1IIi * Ii11Ii1I / Ii11Ii1I
if 30 - 30: iiiiiIIii + I1I1i / I1I1i % iiiiiIIii . iiiiiIIii
if 55 - 55: Ii11Ii1I - OOooOooo + II111iiii + OoOo00o % O000oo0O
iIiiiI1IiI1I1 = xbmcaddon . Addon ( id = 'plugin.program.originwizard' )
iiI11i1II = xbmcgui . Dialog ( )
o0oO0 = xbmc . translatePath ( 'special://home/' )
oOOoO0 = xbmc . translatePath ( os . path . join ( zip ) )
iiIIIII1i1iI = xbmcgui . DialogProgress ( )
OO0O0OOo0O = 'https://addons.tvaddons.ag/'
if 36 - 36: Ii11Ii1I . I1I1i % Ii11Ii1I % IIIii1I1
def OoO000O0Oo ( url ) :
 oOOoO0o0oO = urllib2 . Request ( url )
 oOOoO0o0oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0Oo0oO0oOO00 = urllib2 . urlopen ( oOOoO0o0oO )
 o0oO0O0o0O00O = o0Oo0oO0oOO00 . read ( )
 o0Oo0oO0oOO00 . close ( )
 return o0oO0O0o0O00O
 if 2 - 2: oo0O0oOOO00oO - iiiiiIIii
def o0OOOo ( ) :
 if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * ooo
 extras . addDir ( 'folder' , 'Catagories' , 'none' , 'Addon_Cat' , '' , '' , '' , '' )
 extras . addDir ( 'folder' , 'Search' , 'none' , 'Search_Addons' , '' , '' , '' , '' )
 if 46 - 46: Ii + IIIii1I1
def o0o0O ( ) :
 ooooO0oOoOOoO = iiI11i1II . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11iIiIi = ooooO0oOoOOoO . lower ( )
 OOOOO0O00 = 'https://addons.tvaddons.ag/search/?keyword=' + I1i11iIiIi
 Iii = OoO000O0Oo ( OOOOO0O00 )
 Oo0o0oooo0O0 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( Iii )
 for OooooOOoo0 , iIIiIiI1I1 , Oo0O0O0ooO0O in Oo0o0oooo0O0 :
  extras . addDirNew ( Oo0O0O0ooO0O , OooooOOoo0 , 'Addon_Extract' , 'https://addons.tvaddons.ag/' + iIIiIiI1I1 , Oo0o0000o0o0 , '' )
  if 56 - 56: ooo . O0 + I1I1i
def i1II1I1Iii1 ( ) :
 Iii = OoO000O0Oo ( OO0O0OOo0O )
 Oo0o0oooo0O0 = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( Iii )
 for OooooOOoo0 , iiI11Iii , Oo0O0O0ooO0O in Oo0o0oooo0O0 :
  if 'Repositories' in Oo0O0O0ooO0O :
   pass
  elif 'Services' in Oo0O0O0ooO0O :
   pass
  elif 'International' in Oo0O0O0ooO0O :
   pass
  else :
   extras . addDir ( 'folder' , Oo0O0O0ooO0O , OooooOOoo0 , 'Addon' , 'https://addons.tvaddons.ag/' + iiI11Iii , '' , '' , '' )
   if 78 - 78: OoOo00o + OOooOooo . Ii11Ii1I - OoOo00o . O000oo0O
def II1I11i ( url ) :
 Iii = OoO000O0Oo ( url )
 Oo0o0oooo0O0 = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" width="100%" alt=".+?" class="pic" /></span><strong>(.+?)</strong></a></li>' ) . findall ( Iii )
 for url , iiI11Iii , Oo0O0O0ooO0O in Oo0o0oooo0O0 :
  extras . addDir ( '' , Oo0O0O0ooO0O , url , 'Addon' , 'https://addons.tvaddons.ag/' + iiI11Iii , '' , '' , '' )
  if 82 - 82: OOooOooo + OoooooooOO - i1IIi . i1IIi
  if 6 - 6: oo0O0oOOO00oO / OOooOooo / II111iiii
def I1i11111i1i11 ( url ) :
 Iii = OoO000O0Oo ( url )
 OOoOOO0 = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( Iii )
 for url in OOoOOO0 :
  extras . addDirNewFolder ( 'NEXT PAGE' , 'https://addons.tvaddons.ag' + url , 'Addon' , Oo + 'Next.png' , '' , '' )
 Oo0o0oooo0O0 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( Iii )
 for url , iiI11Iii , Oo0O0O0ooO0O in Oo0o0oooo0O0 :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>' + 'https://addons.tvaddons.ag/' + iiI11Iii + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
  if 'Please' in Oo0O0O0ooO0O :
   pass
  else :
   extras . addDirNew ( Oo0O0O0ooO0O , url , 'Addon_Extract' , 'https://addons.tvaddons.ag/' + iiI11Iii , Oo0o0000o0o0 , '' )
   if 10 - 10: iI1iI1I1i1I / Ii11Ii1I + i11iIiiIii / O000oo0O
   if 74 - 74: i1Iii + O0 + i1IIi - i1IIi + II111iiii
def oOOO0oo0 ( url , name ) :
 Iii = OoO000O0Oo ( url )
 Oo0o0oooo0O0 = re . compile ( '<a href="(.+?)"' ) . findall ( Iii )
 for url in Oo0o0oooo0O0 :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   I1II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   iiIIIII1i1iI = xbmcgui . DialogProgress ( )
   iiIIIII1i1iI . create ( "Origin" , "Downloading Content" , '' , 'Please Wait' )
   oooO = os . path . join ( I1II1 , name + '.zip' )
   try :
    os . remove ( oooO )
   except :
    pass
   downloader . download ( url , oooO , iiIIIII1i1iI )
   i1I1i111Ii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   iiIIIII1i1iI . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print i1I1i111Ii
   print '======================================='
   extract . all ( oooO , i1I1i111Ii , iiIIIII1i1iI )
   I1i1iiI1 = xbmcgui . Dialog ( )
   I1i1iiI1 . ok ( "Origin" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Origin[/COLOR]" )
   if 46 - 46: IIIii1II1II
   if 45 - 45: Ii11Ii1I
   if 21 - 21: o00OO0OOO0 . iI1iI1I1i1I . i1Iii / I1I1i / iI1iI1I1i1I
   if 17 - 17: i1Iii / i1Iii / OOooOooo
iIiiiI1IiI1I1 = xbmcaddon . Addon ( id = 'plugin.program.originwizard' )
zip = iIiiiI1IiI1I1 . getSetting ( 'zip' )
ii1I1IiiI1ii1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.program.originwizard/Generated/' ) )
O0o = 'TEST'
oO0OoO00o = ii1I1IiiI1ii1i + O0o
iiI11i1II = xbmcgui . Dialog ( )
o0oO0 = xbmc . translatePath ( 'special://home/' )
oOOoO0 = xbmc . translatePath ( os . path . join ( zip ) )
iiIIIII1i1iI = xbmcgui . DialogProgress ( )
if 11 - 11: I1I1i - ooo * II111iiii . iiiiiIIii . o00OO0OOO0
def O0OoOO0oo0 ( ) :
 I1II1 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iiI11i1II . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  iIiiiI1IiI1I1 . openSettings ( sys . argv [ 0 ] )
  if 96 - 96: Ii . oo0O0oOOO00oO - Ii11Ii1I
  if 99 - 99: IIIii1II1II . I1I1i - O000oo0O % O000oo0O * O0 . II111iiii
def iIIII1iIIii ( url ) :
 iiIIIII1i1iI . create ( "[COLOR=white]Origin[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for oOOO00o000o , iIi11i1 , oO00oo0o00o0o in os . walk ( url ) :
  for file in oO00oo0o00o0o :
   if file . endswith ( ".xml" ) :
    iiIIIII1i1iI . update ( 0 , "Fixing" , file , 'Please Wait' )
    IiIIIIIi = open ( ( os . path . join ( oOOO00o000o , file ) ) ) . read ( )
    IiIi1iIIi1 = IiIIIIIi . replace ( o0oO0 , 'special://home/' )
    OOOOO0oo0O0O0 = open ( ( os . path . join ( oOOO00o000o , file ) ) , mode = 'w' )
    OOOOO0oo0O0O0 . write ( str ( IiIi1iIIi1 ) )
    OOOOO0oo0O0O0 . close ( )
    if 86 - 86: OOooOooo * ooo + OOooOooo + II111iiii
class i1i111iI ( ) :
 if 29 - 29: iiiiiIIii / i1IIi . ooo - Ii - Ii - O000oo0O
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
  self . save_path = oO0OoO00o
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
  if 20 - 20: i1IIi % IIIii1I1 . ooo / IIIii1II1II * i11iIiiIii * i1Iii
  if 85 - 85: oo0O0oOOO00oO . Ii / Ii11Ii1I . O0 % iI1iI1I1i1I
 def Wizard_Inputs ( self ) :
  O0OoOO0oo0 ( )
  self . plugin_name = iiI11i1II . input ( '[COLOR red]Input Name of Wizard[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . Wizard_name = self . plugin_name . lower ( )
  self . clean_plugin_name = ( self . Wizard_name ) . replace ( ' ' , '' )
  self . build_url = iiI11i1II . input ( '[COLOR red]Input Online Txt File full URL - include http:[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  if 90 - 90: I1I1i % O0 * iIii1I11I1II1 . OoOo00o
  self . generate_wizard_py ( self )
  if 8 - 8: Ii11Ii1I + II111iiii / OoOo00o / OOooOooo
  if 74 - 74: O0 / i1IIi
  if 78 - 78: OoooooooOO . IIIii1I1 + Ii11Ii1I - i1IIi
 def txt_file_inputs ( self ) :
  O0OoOO0oo0 ( )
  self . build_name = iiI11i1II . input ( '[COLOR red] Input Build Name[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_zip = iiI11i1II . input ( '[COLOR red] Input Builds Online Zip Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_image = iiI11i1II . input ( '[COLOR red] Input Builds Online Image Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_fanart = iiI11i1II . input ( '[COLOR red] Input Builds Online Background Image[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . build_description = iiI11i1II . input ( '[COLOR red] Input Builds Description[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  if 31 - 31: OoooooooOO . i1Iii
  self . generate_wizard_text ( )
  if 83 - 83: OoOo00o . O0 / I1I1i / i1Iii - II111iiii
 def generate_wizard_text ( self ) :
  if 100 - 100: IIIii1I1
  II1i = os . path . join ( zip , self . txt_file_name )
  Ii1IIIIi1ii1I = open ( II1i , "w+" )
  if 13 - 13: ooo % Ii . iiiiiIIii / I1I1i % i1Iii . OoooooooOO
  Ii1IIIIi1ii1I . write ( r'name=<' + self . build_name + '>\n' )
  Ii1IIIIi1ii1I . write ( r'url=<' + self . build_zip + '>\n' )
  Ii1IIIIi1ii1I . write ( r'img=<' + self . build_image + '>\n' )
  Ii1IIIIi1ii1I . write ( r'fanart=<' + self . build_fanart + '>\n' )
  Ii1IIIIi1ii1I . write ( r'description=<' + self . build_description + '>\n' )
  Ii1IIIIi1ii1I . close ( )
  I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( "Is There Any More Builds?" , 'Would You like to add another build into txt file?' , '' , 'This Will also show in your wizard when generated' , yeslabel = 'Yes' , nolabel = 'No' )
  if I1I1IiI1 == 1 :
   self . txt_extra_file_inputs ( )
  elif I1I1IiI1 == 0 :
   iiI11i1II . ok ( "[COLOR=white]Origin[/COLOR]" , "Your Text File is now Created" , '' , '' )
   if 22 - 22: IIIii1II1II / i11iIiiIii
 def txt_extra_file_inputs ( self ) :
  O0OoOO0oo0 ( )
  self . extra_build_name = iiI11i1II . input ( '[COLOR red] Input Build Name[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_zip = iiI11i1II . input ( '[COLOR red] Input Builds Online Zip Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_image = iiI11i1II . input ( '[COLOR red] Input Builds Online Image Url[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_fanart = iiI11i1II . input ( '[COLOR red] Input Builds Online Background Image[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  self . extra_build_description = iiI11i1II . input ( '[COLOR red] Input Builds Description[/COLOR]' , type = xbmcgui . INPUT_ALPHANUM )
  if 62 - 62: IIIii1I1 / iiiiiIIii
  self . extra_generate_wizard_text ( )
  if 7 - 7: OoooooooOO . IIIii1II1II
 def extra_generate_wizard_text ( self ) :
  if 53 - 53: O000oo0O % O000oo0O * oo0O0oOOO00oO + Ii
  Oooo00 = os . path . join ( zip , self . txt_file_name )
  I111iIi1 = open ( Oooo00 , "a" )
  if 92 - 92: Ii11Ii1I
  I111iIi1 . write ( r'name=<' + self . extra_build_name + '>\n' )
  I111iIi1 . write ( r'url=<' + self . extra_build_zip + '>\n' )
  I111iIi1 . write ( r'img=<' + self . extra_build_image + '>\n' )
  I111iIi1 . write ( r'fanart=<' + self . extra_build_fanart + '>\n' )
  I111iIi1 . write ( r'description=<' + self . extra_build_description + '>\n' )
  I111iIi1 . close ( )
  I1I1IiI1 = xbmcgui . Dialog ( ) . yesno ( "Is There Any More Builds?" , 'Would You like to add another build into txt file?' , '' , 'This Will also show in your wizard when generated' , yeslabel = 'Yes' , nolabel = 'No' )
  if I1I1IiI1 == 1 :
   self . txt_extra_file_inputs ( )
  elif I1I1IiI1 == 0 :
   iiI11i1II . ok ( "[COLOR=white]Origin[/COLOR]" , "Your Text File is now Created" , '' , '' )
   if 22 - 22: I1I1i % OoOo00o * iiiiiIIii / i1Iii % i11iIiiIii * OOooOooo
   if 95 - 95: OoooooooOO - IIIii1II1II * ooo + Ii
 def generate_wizard_py ( self , name ) :
  if 10 - 10: oo0O0oOOO00oO / i11iIiiIii
  if 92 - 92: OOooOooo . iI1iI1I1i1I
  oOO00O0Ooooo00 = os . path . join ( self . save_path , self . py_file_name )
  O000 = open ( oOO00O0Ooooo00 , "w+" )
  if 79 - 79: OoooooooOO - ooo
  if 69 - 69: OOooOooo
  O000 . write ( r'import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os' + '\n' )
  O000 . write ( r'import shutil' + '\n' )
  O000 . write ( r'import urllib2,urllib' + '\n' )
  O000 . write ( r'import re' + '\n' )
  O000 . write ( r'import extract' + '\n' )
  O000 . write ( r'import downloader' + '\n' )
  O000 . write ( r'import time' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r"USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'" + '\n' )
  O000 . write ( r"base='" + self . plugin_name + '\'' + '\n' )
  O000 . write ( r"ADDON=xbmcaddon.Addon(id='plugin.video." + self . clean_plugin_name + '\')' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'VERSION = "1.0.0"' + '\n' )
  O000 . write ( r"PATH = '" + self . clean_plugin_name + '\'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'def CATEGORIES()' + ':\n' )
  O000 . write ( r"    link = OPEN_URL('" + self . build_url + "')" + '\n' )
  O000 . write ( r"    match = re.compile('name=<(.+?)>.+?rl=<(.+?)>.+?mg=<(.+?)>.+?anart=<(.+?)>.+?escription=<(.+?)>',re.DOTALL).findall(link)" + '\n' )
  O000 . write ( r'    for name,url,iconimage,fanart,description in match:' + '\n' )
  O000 . write ( r'        addDir(name,url,1,iconimage,fanart,description)' + '\n' )
  O000 . write ( r"    setView('movies', 'MAIN'" + ')\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'def OPEN_URL(url):' + '\n' )
  O000 . write ( r'    req = urllib2.Request(url)' + '\n' )
  O000 . write ( r"    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')" + '\n' )
  O000 . write ( r'    response = urllib2.urlopen(req)' + '\n' )
  O000 . write ( r'    link=response.read()' + '\n' )
  O000 . write ( r'    response.close()' + '\n' )
  O000 . write ( r'    return link' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'def wizard(name,url,description):' + '\n' )
  O000 . write ( r"    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))" + '\n' )
  O000 . write ( r'    dp = xbmcgui.DialogProgress()' + '\n' )
  O000 . write ( r'    dp.create("Your Build Is Downloading","This May Take Several Minutes","", "")' + '\n' )
  O000 . write ( r"    lib=os.path.join(path, name+'.zip')" + '\n' )
  O000 . write ( r'    try:' + '\n' )
  O000 . write ( r'       os.remove(lib)' + '\n' )
  O000 . write ( r'    except:' + '\n' )
  O000 . write ( r'       pass' + '\n' )
  O000 . write ( r'    downloader.download(url, lib, dp)' + '\n' )
  O000 . write ( r"    addonfolder = xbmc.translatePath(os.path.join('special://','home'))" + '\n' )
  O000 . write ( r'    time.sleep(2)' + '\n' )
  O000 . write ( r'    dp.update(0,"", "Installing Your Build Please Wait")' + '\n' )
  O000 . write ( r"    print '======================================='" + '\n' )
  O000 . write ( r'    print addonfolder' + '\n' )
  O000 . write ( r"    print '======================================='" + '\n' )
  O000 . write ( r'    extract.all(lib,addonfolder,dp)' + '\n' )
  O000 . write ( r'    dialog = xbmcgui.Dialog()' + '\n' )
  O000 . write ( r'    dialog.ok("Your Media Centre", "[COLORred]Please Force Close Kodi To Take Effect If Pc Exit Task In TaskManager[/COLOR]","[COLORblue]Wizard Brought To You By Origin[/COLOR]")' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'def addDir(name,url,mode,iconimage,fanart,description):' + '\n' )
  O000 . write ( r'        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)' + '\n' )
  O000 . write ( r'        ok=True' + '\n' )
  O000 . write ( r'        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)' + '\n' )
  O000 . write ( r'        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )' + '\n' )
  O000 . write ( r'        liz.setProperty( "Fanart_Image", fanart )' + '\n' )
  O000 . write ( r'        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)' + '\n' )
  O000 . write ( r'        return ok' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'def get_params():' + '\n' )
  O000 . write ( r'        param=[]' + '\n' )
  O000 . write ( r'        paramstring=sys.argv[2]' + '\n' )
  O000 . write ( r'        if len(paramstring)>=2:' + '\n' )
  O000 . write ( r'                params=sys.argv[2]' + '\n' )
  O000 . write ( r"                cleanedparams=params.replace('?','')" + '\n' )
  O000 . write ( r"                if (params[len(params)-1]=='/'):" + '\n' )
  O000 . write ( r'                        params=params[0:len(params)-2]' + '\n' )
  O000 . write ( r"                pairsofparams=cleanedparams.split('&')" + '\n' )
  O000 . write ( r'                param={}' + '\n' )
  O000 . write ( r'                for i in range(len(pairsofparams)):' + '\n' )
  O000 . write ( r'                        splitparams={}' + '\n' )
  O000 . write ( r"                        splitparams=pairsofparams[i].split('=')" + '\n' )
  O000 . write ( r'                        if (len(splitparams))==2:' + '\n' )
  O000 . write ( r'                                param[splitparams[0]]=splitparams[1]' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'        return param' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'params=get_params()' + '\n' )
  O000 . write ( r'url=None' + '\n' )
  O000 . write ( r'name=None' + '\n' )
  O000 . write ( r'mode=None' + '\n' )
  O000 . write ( r'iconimage=None' + '\n' )
  O000 . write ( r'fanart=None' + '\n' )
  O000 . write ( r'description=None' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'try:' + '\n' )
  O000 . write ( r'        url=urllib.unquote_plus(params["url"])' + '\n' )
  O000 . write ( r'except:' + '\n' )
  O000 . write ( r'        pass' + '\n' )
  O000 . write ( r'try:' + '\n' )
  O000 . write ( r'        name=urllib.unquote_plus(params["name"])' + '\n' )
  O000 . write ( r'except:' + '\n' )
  O000 . write ( r'        pass' + '\n' )
  O000 . write ( r'try:' + '\n' )
  O000 . write ( r'        iconimage=urllib.unquote_plus(params["iconimage"])' + '\n' )
  O000 . write ( r'except:' + '\n' )
  O000 . write ( r'        pass' + '\n' )
  O000 . write ( r'try:' + '\n' )
  O000 . write ( r'        mode=int(params["mode"])' + '\n' )
  O000 . write ( r'except:' + '\n' )
  O000 . write ( r'        pass' + '\n' )
  O000 . write ( r'try:' + '\n' )
  O000 . write ( r'        fanart=urllib.unquote_plus(params["fanart"])' + '\n' )
  O000 . write ( r'except:' + '\n' )
  O000 . write ( r'        pass' + '\n' )
  O000 . write ( r'try:' + '\n' )
  O000 . write ( r'        description=urllib.unquote_plus(params["description"])' + '\n' )
  O000 . write ( r'except:' + '\n' )
  O000 . write ( r'        pass' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r"print str(PATH)+': '+str(VERSION)" + '\n' )
  O000 . write ( r'print "Mode: "+str(mode)' + '\n' )
  O000 . write ( r'print "URL: "+str(url)' + '\n' )
  O000 . write ( r'print "Name: "+str(name)' + '\n' )
  O000 . write ( r'print "IconImage: "+str(iconimage)' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'def setView(content, viewType):' + '\n' )
  O000 . write ( r'    # set content type so library shows more views and info' + '\n' )
  O000 . write ( r'    if content:' + '\n' )
  O000 . write ( r'        xbmcplugin.setContent(int(sys.argv[1]), content)' + '\n' )
  O000 . write ( r"    if ADDON.getSetting('auto-view')=='true':" + '\n' )
  O000 . write ( '        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'if mode==None or url==None or len(url)<1:' + '\n' )
  O000 . write ( r'        CATEGORIES()' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'elif mode==1:' + '\n' )
  O000 . write ( r'        wizard(name,url,description)' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'' + '\n' )
  O000 . write ( r'xbmcplugin.endOfDirectory(int(sys.argv[1]))' + '\n' )
  O000 . close ( )
  self . addon_xml ( )
  if 95 - 95: Ii11Ii1I + i11iIiiIii * iI1iI1I1i1I - i1IIi * iI1iI1I1i1I - iIii1I11I1II1
 def addon_xml ( self ) :
  if 75 - 75: OoooooooOO * IIIii1II1II
  I1Iiiiiii = os . path . join ( self . save_path , self . addon_file_name )
  I1IIIiI1I1ii1 = open ( I1Iiiiiii , "w+" )
  if 30 - 30: O0 * OoooooooOO
  if 38 - 38: IIIii1II1II - iiiiiIIii . Ii - iI1iI1I1i1I . OoooooooOO
  I1IIIiI1I1ii1 . write ( r'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'<addon id="plugin.video.' + self . clean_plugin_name + '" name="' + self . plugin_name + '" version="1.0.0" provider-name="Origin">' + '\n' )
  I1IIIiI1I1ii1 . write ( r'  <requires>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'    <import addon="xbmc.python" version="2.1.0"/>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'  </requires>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'  <extension point="xbmc.python.pluginsource" library="default.py">' + '\n' )
  I1IIIiI1I1ii1 . write ( r'        <provides>video executable</provides>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'  </extension>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'  <extension point="xbmc.addon.metadata">' + '\n' )
  I1IIIiI1I1ii1 . write ( r'    <summary lang="en">An installer for ' + self . plugin_name + '</summary>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'    <description lang="en">Generated by Origins mod of original Wizard template for ' + self . plugin_name + '</description>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'    <platform>all</platform>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'  </extension>' + '\n' )
  I1IIIiI1I1ii1 . write ( r'</addon>' + '\n' )
  if 89 - 89: iIii1I11I1II1
  I1IIIiI1I1ii1 . close ( )
  self . Delay ( )
  if 21 - 21: OOooOooo % OOooOooo
 def Delay ( self ) :
  os . rename ( ii1I1IiiI1ii1i + 'TEST' , ii1I1IiiI1ii1i + 'plugin.video.' + self . clean_plugin_name )
  iiIIIII1i1iI . create ( "[COLORwhite]Origin[/COLOR]" , "Writing Files" , '' , 'Please Wait' )
  time . sleep ( 1 )
  self . Backup_Wizard ( )
  if 27 - 27: i11iIiiIii / iiiiiIIii
 def Backup_Wizard ( self ) :
  if 84 - 84: I1I1i
  O0OoOO0oo0 ( )
  iIiiiii1i = xbmc . translatePath ( os . path . join ( oOOoO0 , 'plugin.video.' + self . clean_plugin_name + '.zip' ) )
  iiIi1IIiI = ii1I1IiiI1ii1i
  iiIIIII1i1iI . create ( "[COLOR=white]Origin[/COLOR]" , "Backing Up" , '' , 'Please Wait' )
  i1oO0OO0 = zipfile . ZipFile ( iIiiiii1i , 'w' , zipfile . ZIP_DEFLATED )
  o0O0Oo00 = len ( iiIi1IIiI )
  O0Oo0o000oO = [ ]
  oO0o00oOOooO0 = [ ]
  for I11II1i , iIi11i1 , oO00oo0o00o0o in os . walk ( iiIi1IIiI ) :
   for file in oO00oo0o00o0o :
    oO0o00oOOooO0 . append ( file )
  OOOoO000 = len ( oO0o00oOOooO0 )
  for I11II1i , iIi11i1 , oO00oo0o00o0o in os . walk ( iiIi1IIiI ) :
   for file in oO00oo0o00o0o :
    O0Oo0o000oO . append ( file )
    oOOOO = len ( O0Oo0o000oO ) / float ( OOOoO000 ) * 100
    iiIIIII1i1iI . update ( int ( oOOOO ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    IiIi1ii111i1 = os . path . join ( I11II1i , file )
    if not 'temp' in iIi11i1 :
     if not 'plugin.video.originwizard' in iIi11i1 :
      import time
      i1i1i1I = '01/01/1980'
      oOoo000 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( IiIi1ii111i1 ) ) )
      if oOoo000 > i1i1i1I :
       i1oO0OO0 . write ( IiIi1ii111i1 , IiIi1ii111i1 [ o0O0Oo00 : ] )
  i1oO0OO0 . close ( )
  iiIIIII1i1iI . close ( )
  os . rename ( ii1I1IiiI1ii1i + 'plugin.video.' + self . clean_plugin_name , ii1I1IiiI1ii1i + 'TEST' )
  iiI11i1II . ok ( "[COLOR=white]Origin[/COLOR]" , "Your wizard is now created" , '' , '' )
  if 87 - 87: OoooooooOO - oo0O0oOOO00oO / IIIii1II1II . i11iIiiIii * OoooooooOO
  if 84 - 84: Ii / OOooOooo * OoOo00o / o00OO0OOO0 - i11iIiiIii . I1I1i
oOOo000oOoO0 = i1i111iI ( '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
if 86 - 86: II111iiii % i11iIiiIii + O000oo0O % i11iIiiIii
if 92 - 92: i11iIiiIii - OoOo00o / Ii11Ii1I / o00OO0OOO0
if 43 - 43: II111iiii + i1Iii + OoOo00o
def iI1IIIii ( content , viewType ) :
 if 7 - 7: IIIii1II1II - OOooOooo / II111iiii * O000oo0O . OoOo00o * OoOo00o
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if iIiiiI1IiI1I1 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % iIiiiI1IiI1I1 . getSetting ( viewType ) )
  if 61 - 61: OOooOooo % Ii11Ii1I - IIIii1I1 / I1I1i
if iIIiiI1II1i11 == None or OooooOOoo0 == None or len ( OooooOOoo0 ) < 1 :
 O00o0O00 ( )
elif iIIiiI1II1i11 == 'addon_removal_menu' : OOO0 ( )
elif iIIiiI1II1i11 == 'addonfix' : addonfix . fixes ( )
elif iIIiiI1II1i11 == 'addonfixes' : iIi1iIiii111 ( )
elif iIIiiI1II1i11 == 'addonmenu' : Addon_Menu ( )
elif iIIiiI1II1i11 == 'addon_settings' : iI1I111Ii111i ( )
elif iIIiiI1II1i11 == 'backup' : BACKUP ( )
elif iIIiiI1II1i11 == 'backup_option' : communitybuilds . Backup_Option ( )
elif iIIiiI1II1i11 == 'backup_restore' : oO0o0OOOO ( )
elif iIIiiI1II1i11 == 'adultmenu' : AdultMenu ( )
elif iIIiiI1II1i11 == 'buildmenu' : O0Oo0oOOoooOOOOo ( )
elif iIIiiI1II1i11 == 'categories' : O00o0O00 ( )
elif iIIiiI1II1i11 == 'clear_cache' : oooooOoo0ooo ( )
elif iIIiiI1II1i11 == 'community_backup' : communitybuilds . Community_Backup ( )
elif iIIiiI1II1i11 == 'community_menu' : communitybuilds . Community_Menu ( OooooOOoo0 , OOo0O0oo0OO0O )
elif iIIiiI1II1i11 == 'description' : communitybuilds . Description ( Oo0O0O0ooO0O , OooooOOoo0 , OOO0000oO , Iii1 , ii1I1i11 , i1I1IiiIi1i , ooo00Ooo , iI1i11 , OO0 , OO0oo , IIii1111 , iIiiiII , OoOOoooOO0O , ii111I )
elif iIIiiI1II1i11 == 'fix_special' : communitybuilds . Fix_Special ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'genres' : Genres ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'grab_addons' : addons . Grab_Addons ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'grab_builds_premium' : communitybuilds . Grab_Builds_Premium ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'guisettingsfix' : communitybuilds . GUI_Settings_Fix ( OooooOOoo0 , OOOoOO )
elif iIIiiI1II1i11 == 'guisettings' : guisettings ( )
elif iIIiiI1II1i11 == 'hide_passwords' : extras . Hide_Passwords ( )
elif iIIiiI1II1i11 == 'LocalGUIDialog' : communitybuilds . Local_GUI_Dialog ( )
elif iIIiiI1II1i11 == 'remove_addon_data' : IIiIiiIi ( )
elif iIIiiI1II1i11 == 'remove_addons' : extras . Remove_Addons ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'remove_build' : extras . Remove_Build ( )
elif iIIiiI1II1i11 == 'remove_crash_logs' : OOooOoooOoOo ( )
elif iIIiiI1II1i11 == 'remove_packages' : oooo0O0 ( )
elif iIIiiI1II1i11 == 'remove_textures' : III1iII1I1ii ( )
elif iIIiiI1II1i11 == 'restore' : extras . RESTORE ( )
elif iIIiiI1II1i11 == 'restore_backup' : communitybuilds . Restore_Backup_XML ( Oo0O0O0ooO0O , OooooOOoo0 , i1I1IiiIi1i )
elif iIIiiI1II1i11 == 'restore_local_CB' : communitybuilds . Restore_Local_Community ( )
elif iIIiiI1II1i11 == 'restore_local_gui' : communitybuilds . Restore_Local_GUI ( )
elif iIIiiI1II1i11 == 'restore_option' : communitybuilds . Restore_Option ( )
elif iIIiiI1II1i11 == 'restore_zip' : communitybuilds . Restore_Zip_File ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'restore_community' : communitybuilds . Restore_Community ( Oo0O0O0ooO0O , OooooOOoo0 , OOo0O0oo0OO0O , i1I1IiiIi1i , iI1i11 , iiI )
elif iIIiiI1II1i11 == 'showinfo' : communitybuilds . Show_Info ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'SortBy' : extras . Sort_By ( BuildURL , type )
elif iIIiiI1II1i11 == 'text_guide' : news . Text_Guide ( Oo0O0O0ooO0O , OooooOOoo0 )
elif iIIiiI1II1i11 == 'tools' : IiI111111IIII ( )
elif iIIiiI1II1i11 == 'unhide_passwords' : extras . Unhide_Passwords ( )
elif iIIiiI1II1i11 == 'update' : addons . Update_Repo ( )
elif iIIiiI1II1i11 == 'uploadlog' : extras . Upload_Log ( )
elif iIIiiI1II1i11 == 'user_info' : Show_User_Info ( )
elif iIIiiI1II1i11 == 'wipetools' : oOOOoo0O0oO ( )
elif iIIiiI1II1i11 == 'xbmcversion' : extras . XBMC_Version ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'wipe_xbmc' : I1i11i ( )
elif iIIiiI1II1i11 == 'wizard' : o0000oO ( Oo0O0O0ooO0O , OooooOOoo0 , i1I1IiiIi1i )
elif iIIiiI1II1i11 == 'Merlin' : o00oO0oOo00 ( )
elif iIIiiI1II1i11 == 'Text_Gen' : i1i111iI ( '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , 'textFile' )
elif iIIiiI1II1i11 == 'Wizard_Gen' : i1i111iI ( '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , 'newWizard' )
elif iIIiiI1II1i11 == 'How_To' : ooO0oOOooOo0 ( )
elif iIIiiI1II1i11 == 'Addon_Cat' : i1II1I1Iii1 ( )
elif iIIiiI1II1i11 == 'Addon' : I1i11111i1i11 ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'Addon_Extract' : oOOO0oo0 ( OooooOOoo0 , Oo0O0O0ooO0O )
elif iIIiiI1II1i11 == 'Repo' : II1I11i ( OooooOOoo0 )
elif iIIiiI1II1i11 == 'Search_Addons' : o0o0O ( )
elif iIIiiI1II1i11 == 'Addons_Menu' : o0OOOo ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
