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

import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys
import urllib, urllib2, re, glob
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

Decode       =   base64.decodestring
addon_handle = int(sys.argv[1])
ARTPATH      =  'special://home/resources/art/' + os.sep
ADDON        =  xbmcaddon.Addon(id='plugin.program.originwizard')
AddonID      =  'plugin.program.originwizard'
AddonTitle   =  "Origin Wizard"
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,AddonID,'resources','art')+os.sep
zip          =  ADDON.getSetting('zip')
localcopy    =  ADDON.getSetting('localcopy')
privatebuilds=  ADDON.getSetting('private')
reseller     =  ADDON.getSetting('reseller')
resellername =  ADDON.getSetting('resellername')
resellerid   =  ADDON.getSetting('resellerid')
mastercopy   =  ADDON.getSetting('mastercopy')
username     =  ADDON.getSetting('username')
password     =  ADDON.getSetting('password')
login        =  ADDON.getSetting('login')
trcheck      =  ADDON.getSetting('trcheck')
dialog       =  xbmcgui.Dialog()
dp           =  xbmcgui.DialogProgress()
HOME         =  xbmc.translatePath('special://home/')
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
MEDIA        =  xbmc.translatePath(os.path.join('special://home/media',''))
AUTOEXEC     =  xbmc.translatePath(os.path.join(USERDATA,'autoexec.py'))
AUTOEXECBAK  =  xbmc.translatePath(os.path.join(USERDATA,'autoexec_bak.py'))
ADDON_DATA   =  xbmc.translatePath(os.path.join(USERDATA,'addon_data'))
PLAYLISTS    =  xbmc.translatePath(os.path.join(USERDATA,'playlists'))
DATABASE     =  xbmc.translatePath(os.path.join(USERDATA,'Database'))
THUMBNAILS   =  xbmc.translatePath(os.path.join(USERDATA,'Thumbnails'))
ADDONS       =  xbmc.translatePath(os.path.join('special://home','addons',''))
CBADDONPATH  =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'default.py'))
FANART       =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'fanart.jpg'))
GENESIS 	 =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.genesis/favourites.db'))
GUISETTINGS  =  os.path.join(USERDATA,'guisettings.xml')
GUI          =  xbmc.translatePath(os.path.join(USERDATA,'guisettings.xml'))
GUIFIX       =  xbmc.translatePath(os.path.join(USERDATA,'guifix.xml'))
INSTALL      =  xbmc.translatePath(os.path.join(USERDATA,'install.xml'))
IVUE 		 =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.ivueguide/master.db'))
FAVS         =  xbmc.translatePath(os.path.join(USERDATA,'favourites.xml'))
SOURCE       =  xbmc.translatePath(os.path.join(USERDATA,'sources.xml'))
ADVANCED     =  xbmc.translatePath(os.path.join(USERDATA,'advancedsettings.xml'))
PROFILES     =  xbmc.translatePath(os.path.join(USERDATA,'profiles.xml'))
RSS          =  xbmc.translatePath(os.path.join(USERDATA,'RssFeeds.xml'))
KEYMAPS      =  xbmc.translatePath(os.path.join(USERDATA,'keymaps','keyboard.xml'))
USB          =  xbmc.translatePath(os.path.join(zip))
CBPATH       =  xbmc.translatePath(os.path.join(USB,'Community Builds',''))
cookiepath   =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'cookiejar'))
startuppath  =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'startup.xml'))
tempfile     =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'temp.xml'))
idfile       =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'id.xml'))
idfiletemp   =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'idtemp.xml'))
notifyart    =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'resources/'))
toolbox 	 =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'resources/toolbox.xml'))
skin         =  xbmc.getSkinDir()
userdatafolder = xbmc.translatePath(os.path.join(ADDON_DATA,AddonID))
GUINEW       =  xbmc.translatePath(os.path.join(userdatafolder,'guinew.xml'))
guitemp      =  xbmc.translatePath(os.path.join(userdatafolder,'guitemp',''))
tempdbpath   =  xbmc.translatePath(os.path.join(USB,'Database'))
TEXT_FILE_PATH = xbmc.translatePath(os.path.join('special://home/addons/plugin.program.originwizard/Generated/TEST/resources/'))
WIPE_ADDON 	 =  xbmc.translatePath(os.path.join('special://home/addons/plugin.program.originwizard'))
urlbase      =  'None'
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
base='http://rh-project.info/'
VERSION = "2.0.3"
PATH = "originwizard" 

#-----------------------------------------------------------------------------------------------------------------
#Addon removal menu
def Addon_Removal_Menu():
    for file in glob.glob(os.path.join(ADDONS,'*')):
        name=str(file).replace(ADDONS,'[COLOR=red]REMOVE [/COLOR]').replace('plugin.','[COLOR=dodgerblue](PLUGIN) [/COLOR]').replace('audio.','').replace('video.','').replace('skin.','[COLOR=yellow](SKIN) [/COLOR]').replace('repository.','[COLOR=orange](REPOSITORY) [/COLOR]').replace('script.','[COLOR=cyan](SCRIPT) [/COLOR]').replace('metadata.','[COLOR=gold](METADATA) [/COLOR]').replace('service.','[COLOR=pink](SERVICE) [/COLOR]').replace('weather.','[COLOR=green](WEATHER) [/COLOR]').replace('module.','[COLOR=gold](MODULE) [/COLOR]')
        iconimage=(os.path.join(file,'icon.png'))
        fanart=(os.path.join(file,'fanart.jpg'))
        extras.addDir('',name,file,'remove_addons',iconimage,fanart,'','')
#-----------------------------------------------------------------------------------------------------------------
#Function to open addon settings
def Addon_Settings():
    ADDON.openSettings(sys.argv[0])
#---------------------------------------------------------------------------------------------------
#Addon Maintenance Section
def Addon_Fixes():
    extras.addDir('folder','Completely remove an add-on (inc. passwords)','plugin','addon_removal_menu', 'Remove_Addon.png','','','')
    extras.addDir('','Hide my add-on passwords','none','hide_passwords', 'Hide_Passwords.png','','','')
    extras.addDir('','Unhide my add-on passwords','none','unhide_passwords', 'Unhide_Passwords.png','','','')
    extras.addDir('','Update My Add-ons (Force Refresh)', 'none', 'update', 'Update_Addons.png','','','')
    extras.addDir('','Wipe All Add-on Settings (addon_data)','url','remove_addon_data','Delete_Addon_Data.png','','','')
	
#-----------------------------------------------------------------------------------------------------------------
#Backup/Restore root menu
def Backup_Restore():
    extras.addDir('folder','Backup My Content','none','backup_option','Backup.png','','','')
    extras.addDir('folder','Restore My Content','none','restore_option','Restore.png','','','')
#---------------------------------------------------------------------------------------------------
#Main category list
def Categories():
	sign = 0
	maintenance  =  ADDON.getSetting('maintenance')
	mainmenu  =  ADDON.getSetting('mainmenu')
	guisettings  =  ADDON.getSetting('guisettings')
	adultbuilds  =  ADDON.getSetting('adultbuilds')
	if mainmenu == 'true':
		extras.addDir('folder','Origin Builds','none', 'buildmenu', 'Build_Menu.png','','','')
		extras.addDir('folder','Fast Update','none', 'fastupdatemenu', 'Adult_Menu.png','','','')
	if guisettings == 'true':
		extras.addDir('folder','Gui Settings XML','none', 'guisettings', 'Gui_Menu.png','','','')
	if maintenance == 'true':
		extras.addDir('folder','Maintenance','none', 'tools', 'Tools.png','','','')
	
#---------------------------------------------------------------------------------------------------
#Function to clear all known cache files
def Clear_Cache():
    choice = xbmcgui.Dialog().yesno('Clear All Known Cache?', 'This will clear all known cache files and can help', 'if you\'re encountering kick-outs during playback.','as well as other random issues. There is no harm in using this.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        cache.Wipe_Cache()
        Remove_Textures()
#---------------------------------------------------------------------------------------------------
#Get params and clean up into string or integer
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
#---------------------------------------------------------------------------------------------------
#Function to clear the addon_data
def Remove_Addon_Data():
    choice = xbmcgui.Dialog().yesno('Delete Addon_Data Folder?', 'This will free up space by deleting your addon_data', 'folder. This contains all addon related settings', 'including username and password info.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        extras.Delete_Userdata()
        dialog.ok("Addon_Data Removed", '', 'Your addon_data folder has now been removed.','')
#---------------------------------------------------------------------------------------------------
#Function to clear the packages folder
def Remove_Crash_Logs():
    choice = xbmcgui.Dialog().yesno('Remove All Crash Logs?', 'There is absolutely no harm in doing this, these are', 'log files generated when Kodi crashes and are','only used for debugging purposes.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        extras.Delete_Logs()
        dialog.ok("Crash Logs Removed", '', 'Your crash log files have now been removed.','')
#---------------------------------------------------------------------------------------------------
#Function to clear the packages folder
def Remove_Packages():
    choice = xbmcgui.Dialog().yesno('Delete Packages Folder?', 'This will free up space by deleting the zip install', 'files of your addons. The only downside is you\'ll no', 'longer be able to rollback to older versions.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        extras.Delete_Packages()
        dialog.ok("Packages Removed", '', 'Your zip install files have now been removed.','')
#---------------------------------------------------------------------------------------------------
#Function to clear the packages folder
def Remove_Textures():
    choice = xbmcgui.Dialog().yesno('Clear Cached Images?', 'This will clear your textures13.db file and remove', 'your Thumbnails folder. These will automatically be', 'repopulated after a restart.', nolabel='Cancel',yeslabel='Delete')
    if choice == 1:
        cache.Remove_Textures()
        extras.Destroy_Path(THUMBNAILS)
        choice = xbmcgui.Dialog().yesno('Quit Kodi Now?', 'Cache has been successfully deleted.', 'You must now restart Kodi, would you like to quit now?','', nolabel='I\'ll restart later',yeslabel='Yes, quit')
        if choice == 1:
            killxbmc()
#---------------------------------------------------------------------------------------------------
#Maintenance section
def Tools():
    extras.addDir('folder','[COLOR white]Addon Installer[/COLOR]', 'none', 'Addons_Menu', '','','','')
    extras.addDir('wizard','[COLOR red]Wizard Generator[/COLOR]', 'none', 'Merlin', ARTPATH + 'icon.png',ARTPATH + 'fanart.jpg','','')
    extras.addDir('folder','Add-on Maintenance/Fixes', 'none', 'addonfixes', '','','','')
    extras.addDir('folder','Backup/Restore My Content','none','backup_restore','','','','')
    extras.addDir('folder','Clean/Wipe Options', 'none', 'wipetools', '','','','')
    extras.addDir('','Check XBMC/Kodi Version', 'none', 'xbmcversion', '','','','')
    extras.addDir('','Convert Physical Paths To Special',HOME,'fix_special','','','','')
    extras.addDir('','Force Close Kodi','url','kill_xbmc','','','','')
#-----------------------------------------------------------------------------------------------------------------
#Merlin
def Merlin():
    extras.addDir('wizard2','[COLOR red]How To Guide[/COLOR]', 'none', 'How_To',ARTPATH + 'icon.png',ARTPATH + 'fanart.jpg','','')
    extras.addDir('wizard2','[COLOR blue]Generate your personalised wizard[/COLOR]', 'none', 'Text_Gen',ARTPATH + 'icon.png',ARTPATH + 'fanart.jpg','','')

#------------------------------------------------------------
#How To Guide For Wizard Generator

def How_To():
    TextBoxes('How To guide For Wizard Creation','1: First you will need to create a build and host somewhere online that it can be accessed, aswell as an image for thumbnail and background\n\n\n2:Run Wizard Generator, it will ask you to set backup path if its not been set, try to keep local on the device\n\n\n3:Fill in the relevant fields, then let others enjoy your build. for FREE\n\n\n4:[COLOR red] Take time to thank devs for there hard work, maybe donate (not to me i dont accept as i dont have costs, but to those who do need it) and just appreciate the work that goes in to bring you FREE stuff, maybe visit some streaming sites suffer some ads to keep them going once a week aswell, help people to help you basically[/COLOR]')


def TextBoxes(heading,announce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    isFolder=True
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(announce); text=f.read()
      except: text=announce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()
	
#--------------------------------------------------------------------------------------------------------------------------
#Function to clear the addon_data
def Wipe_Kodi():
    mybackuppath = xbmc.translatePath(os.path.join(USB,'Community Builds','My Builds'))
    choice = xbmcgui.Dialog().yesno("ABSOLUTELY CERTAIN?!!!", 'Are you absolutely certain you want to wipe?', '', 'All addons and settings will be completely wiped!', yeslabel='Yes',nolabel='No')
    if choice == 1:
        if skin!= "skin.confluence":
            dialog.ok('[COLOR=white]Origin[/COLOR]','Please switch to the default Confluence skin','before performing a wipe.','')
            xbmc.executebuiltin("ActivateWindow(appearancesettings)")
            return
        else:
            choice = xbmcgui.Dialog().yesno("VERY IMPORTANT", 'This will completely wipe your install.', 'Would you like to create a backup before proceeding?', '', yeslabel='No', nolabel='Yes')
            if choice == 0:
                if not os.path.exists(mybackuppath):
                    os.makedirs(mybackuppath)
                vq = extras.Get_Keyboard( heading="Enter a name for this backup" )
                if ( not vq ): return False, 0
                title = urllib.quote_plus(vq)
                backup_zip = xbmc.translatePath(os.path.join(mybackuppath,title+'.zip'))
                exclude_dirs_full =  ['plugin.program.originwizard']
                exclude_files_full = ["xbmc.log","xbmc.old.log","kodi.log","kodi.old.log",'.DS_Store','.setup_complete','XBMCHelper.conf']
                message_header = "Creating full backup of existing build"
                message1 = "Archiving..."
                message2 = ""
                message3 = "Please Wait"
                communitybuilds.Archive_Tree(HOME, backup_zip, message_header, message1, message2, message3, exclude_dirs_full, exclude_files_full)
            choice = xbmcgui.Dialog().yesno("Remove Origin Wizard?", 'Do you also want to remove the Origin Wizard', 'add-on and have a complete fresh start or would you', 'prefer to keep this on your system?', yeslabel='Remove',nolabel='Keep')
            if choice == 0:
                cache.Remove_Textures()
                trpath = xbmc.translatePath(os.path.join(ADDONS,AddonID,''))
                trtemp = xbmc.translatePath(os.path.join(HOME,'..','originwizard.zip'))
                communitybuilds.Archive_File(trpath, trtemp)
                deppath = xbmc.translatePath(os.path.join(ADDONS,'script.module.addon.common',''))
                deptemp = xbmc.translatePath(os.path.join(HOME,'..','originwizarddep.zip'))
                communitybuilds.Archive_File(deppath, deptemp)
                extras.Destroy_Path(HOME)
                if not os.path.exists(trpath):
                    os.makedirs(trpath)
                if not os.path.exists(deppath):
                    os.makedirs(deppath)
                time.sleep(1)
                communitybuilds.Read_Zip(trtemp)
                dp.create("[[COLOR=white]Origin[/COLOR][/B]","Checking ",'', 'Please Wait')
                dp.update(0,"", "Extracting Zip Please Wait")
                extract.all(trtemp,trpath,dp)
                communitybuilds.Read_Zip(deptemp)
                extract.all(deptemp,deppath,dp)
                dp.update(0,"", "Extracting Zip Please Wait")
                dp.close()
                time.sleep(1)
                extras.Kill_XBMC()
            elif choice == 1:
                cache.Remove_Textures()
                extras.Destroy_Path(HOME)
                dp.close()
                extras.Kill_XBMC()
            else: return
#-----------------------------------------------------------------------------------------------------------------    
#Maintenance section
def Wipe_Tools():
    extras.addDir('','Clear Cache','url','clear_cache','Clear_Cache.png','','','')
    extras.addDir('','Clear My Cached Artwork', 'none', 'remove_textures', 'Delete_Cached_Artwork.png','','','')
    extras.addDir('','Delete Addon_Data','url','remove_addon_data','Delete_Addon_Data.png','','','')
    extras.addDir('','Delete Old Builds/Zips From Device','url','remove_build','Delete_Builds.png','','','')
    extras.addDir('','Delete Old Crash Logs','url','remove_crash_logs','Delete_Crash_Logs.png','','','')
    extras.addDir('','Delete Packages Folder','url','remove_packages','Delete_Packages.png','','','')
    extras.addDir('','Wipe My Install (Fresh Start)', 'none', 'wipe_xbmc', 'Fresh_Start.png','','','')
#-----------------------------------------------------------------------------------------------------------------
#Builds Section
def BuildMenu():
    link = open(toolbox).read()
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"',re.DOTALL).findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,'wizard',iconimage,fanart,description)
    AUTO_VIEW('500')
	
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link  
    
def wizard(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("origin wizard","Downloading ",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    dialog = xbmcgui.Dialog()
    dialog.ok("DOWNLOAD COMPLETE", 'To ensure all changes are saved you must now close Kodi', 'to force close Kodi. Click ok,', 'DO NOT use the quit/exit options in Kodi.')
    killxbmc()
	            
def killxbmc():
    choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    if choice == 0:
        return
    elif choice == 1:
        pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass        
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "Your system has been detected as Android, you ", "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Pulling the power cable is the simplest method to force close.")
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.","Your platform could not be detected so just pull the power cable.")    

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'


def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def AUTO_VIEW(content = ''):
    if not content:
        return

    xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view') != 'true':
        return

    if content == 'addons':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting('addon_view'))
    else:
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting('default-view'))		
#-----------------------------------------------------------------------------------------------------------------
#Addon starts here
params=Get_Params()
addon_id=None
audioaddons=None
author=None
buildname=None
data_path=None
description=None
DOB=None
email=None
fanart=None
forum=None
iconimage=None
link=None
local=None
messages=None
mode=None
name=None
posts=None
programaddons=None
provider_name=None
repo_id=None
repo_link=None
skins=None
sources=None
updated=None
unread=None
url=None
version=None
video=None
videoaddons=None
welcometext=None
zip_link=None

try:    addon_id=urllib.unquote_plus(params["addon_id"])
except: pass
try:    adult=urllib.unquote_plus(params["adult"])
except: pass
try:    audioaddons=urllib.unquote_plus(params["audioaddons"])
except: pass
try:    author=urllib.unquote_plus(params["author"])
except: pass
try:    buildname=urllib.unquote_plus(params["buildname"])
except: pass
try:    data_path=urllib.unquote_plus(params["data_path"])
except: pass
try:    description=urllib.unquote_plus(params["description"])
except: pass
try:    DOB=urllib.unquote_plus(params["DOB"])
except: pass
try:    email=urllib.unquote_plus(params["email"])
except: pass
try:    fanart=urllib.unquote_plus(params["fanart"])
except: pass
try:    forum=urllib.unquote_plus(params["forum"])
except: pass
try:    guisettingslink=urllib.unquote_plus(params["guisettingslink"])
except: pass
try:    iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try:    link=urllib.unquote_plus(params["link"])
except: pass
try:    local=urllib.unquote_plus(params["local"])
except: pass
try:    messages=urllib.unquote_plus(params["messages"])
except: pass
try:    mode=str(params["mode"])
except: pass
try:    name=urllib.unquote_plus(params["name"])
except: pass
try:    pictureaddons=urllib.unquote_plus(params["pictureaddons"])
except: pass
try:    posts=urllib.unquote_plus(params["posts"])
except: pass
try:    programaddons=urllib.unquote_plus(params["programaddons"])
except: pass
try:    provider_name=urllib.unquote_plus(params["provider_name"])
except: pass
try:    repo_link=urllib.unquote_plus(params["repo_link"])
except: pass
try:    repo_id=urllib.unquote_plus(params["repo_id"])
except: pass
try:    skins=urllib.unquote_plus(params["skins"])
except: pass
try:    sources=urllib.unquote_plus(params["sources"])
except: pass
try:    updated=urllib.unquote_plus(params["updated"])
except: pass
try:    unread=urllib.unquote_plus(params["unread"])
except: pass
try:    url=urllib.unquote_plus(params["url"])
except: pass
try:    version=urllib.unquote_plus(params["version"])
except: pass
try:    video=urllib.unquote_plus(params["video"])
except: pass
try:    videoaddons=urllib.unquote_plus(params["videoaddons"])
except: pass
try:    zip_link=urllib.unquote_plus(params["zip_link"])
except: pass

print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)

#--------------------------------------------------------------------------------------------------------
#Fast Update


def Fast_Update():
    
    HTML = OPEN_URL('http://back2basicsbuild.co.uk/Fast%20Update/readme.txt')
    match = re.compile('<url="(.+?)"').findall(HTML)
    for url in match:
        if 'addons' in url:
            path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
            dp = xbmcgui.DialogProgress()
            dp.create("Origin","Downloading Content",'', 'Please Wait')
            lib=os.path.join(path, name+'.zip')
            try:
                os.remove(lib)
            except:
                pass
            downloader.download(url, lib, dp)
            addonfolder = xbmc.translatePath(os.path.join('special://home','addons'))
            time.sleep(2)
            dp.update(0,"", "Extracting Zip Please Wait")
            print '======================================='
            print addonfolder
            print '======================================='
            extract.all(lib,addonfolder,dp)
            dialog = xbmcgui.Dialog()
            dialog.ok("Origin", "Press ok to update gui settings","[COLOR yellow]Brought To You By Origin[/COLOR]")
            UPDATEGUI()
			
def UPDATEGUI():

    HTML = OPEN_URL('http://back2basicsbuild.co.uk/Fast%20Update/readme.txt')
    match = re.compile('<url="(.+?)"').findall(HTML)
    for url in match:
        if 'gui' in url:
            path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
            dp = xbmcgui.DialogProgress()
            dp.create("Origin","Downloading Content",'', 'Please Wait')
            lib=os.path.join(path, name+'.zip')
            try:
                os.remove(lib)
            except:
                pass
            downloader.download(url, lib, dp)
            addonfolder = xbmc.translatePath(os.path.join('special://home','userdata'))
            time.sleep(2)
            dp.update(0,"", "Extracting Zip Please Wait")
            print '======================================='
            print addonfolder
            print '======================================='
            extract.all(lib,addonfolder,dp)
            dialog = xbmcgui.Dialog()
            dialog.ok("Origin", "Press ok to remove old addons","[COLOR yellow]Brought To You By Origin[/COLOR]")
            REMOVE()

def REMOVE():
    HTML = OPEN_URL('http://back2basicsbuild.co.uk/Fast%20Update/readme.txt')
    match = re.compile('<name="(.+?)"').findall(HTML)
    for name in match:
        shutil.rmtree(ADDONS + name)
        dialog.ok("Origin", "Press ok to refresh","[COLOR yellow]If changes dont take effect you may need to force close[/COLOR]")
#--------------------------------------------------------------------------------------------------------
#Addon Installer

ADDON        =  xbmcaddon.Addon(id='plugin.program.originwizard')
Dialog 		 = xbmcgui.Dialog()
HOME         =  xbmc.translatePath('special://home/')
USB          =  xbmc.translatePath(os.path.join(zip))
dp           =  xbmcgui.DialogProgress()
base_url 	 = 'https://addons.tvaddons.ag/'

def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def Addons_Menu():
    
    extras.addDir('folder','Catagories', 'none', 'Addon_Cat', '','','','')
    extras.addDir('folder','Search', 'none', 'Search_Addons', '','','','')

def Search_Addons():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name.lower()
    Search_URL = 'https://addons.tvaddons.ag/search/?keyword=' + Search_Title 
    HTML = OPEN_URL(Search_URL)
    match = re.compile('<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>').findall(HTML)
    for url,image,name in match:
        extras.addDirNew(name,url, 'Addon_Extract','https://addons.tvaddons.ag/'+image,FANART,'')    

def Addon_Cat():
    HTML = OPEN_URL(base_url)
    match = re.compile('<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>').findall(HTML)
    for url,img,name in match:
        if 'Repositories' in name:
            pass
        elif 'Services' in name:
            pass
        elif 'International' in name:
            pass
        else:
            extras.addDir('folder',name,url, 'Addon','https://addons.tvaddons.ag/'+img,'','','')

def Repo(url):
    HTML = OPEN_URL(url)
    match = re.compile('<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" width="100%" alt=".+?" class="pic" /></span><strong>(.+?)</strong></a></li>').findall(HTML)
    for url,img,name in match:
        extras.addDir('',name,url,'Addon','https://addons.tvaddons.ag/'+img,'','','')


def Addon(url):
    HTML = OPEN_URL(url)
    Next = re.compile('<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>').findall(HTML)
    for url in Next:
        extras.addDirNewFolder('NEXT PAGE','https://addons.tvaddons.ag' + url, 'Addon',ART + 'Next.png','','')
    match = re.compile('<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>').findall(HTML)
    for url,img,name in match:
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>' + 'https://addons.tvaddons.ag/'+img +'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
        if 'Please' in name:
            pass
        else:
            extras.addDirNew(name,url, 'Addon_Extract','https://addons.tvaddons.ag/'+img,FANART,'')


def Addon_Extract(url,name):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="(.+?)"').findall(HTML)
    for url in match:
        if 'plugin' in url:
            print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
            path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
            dp = xbmcgui.DialogProgress()
            dp.create("Origin","Downloading Content",'', 'Please Wait')
            lib=os.path.join(path, name+'.zip')
            try:
                os.remove(lib)
            except:
                pass
            downloader.download(url, lib, dp)
            addonfolder = xbmc.translatePath(os.path.join('special://home','addons'))
            time.sleep(2)
            dp.update(0,"", "Extracting Zip Please Wait")
            print '======================================='
            print addonfolder
            print '======================================='
            extract.all(lib,addonfolder,dp)
            dialog = xbmcgui.Dialog()
            dialog.ok("Origin", "Press ok to finish install","[COLOR yellow]Brought To You By Origin[/COLOR]")
            UPDATEREPO()

def UPDATEREPO():
    xbmc.executebuiltin( 'UpdateLocalAddons' )
    xbmc.executebuiltin( 'UpdateAddonRepos' )
    dialog = xbmcgui.Dialog()
    dialog.ok("Origin", '','                                 REFRESH SUCCESSFUL :)', "                          [COLOR gold]Brought To You By Origin[/COLOR]")
    return

#------------------------------------------------------------------------------------
#Wizard Generator

ADDON        =  xbmcaddon.Addon(id='plugin.program.originwizard')
zip =  ADDON.getSetting('zip')
Addons_path = xbmc.translatePath(os.path.join('special://home/addons/plugin.program.originwizard/Generated/'))
Generated = 'TEST'
Folders_path = Addons_path + Generated
Dialog = xbmcgui.Dialog()
HOME         =  xbmc.translatePath('special://home/')
USB          =  xbmc.translatePath(os.path.join(zip))
dp           =  xbmcgui.DialogProgress()

def Check_Download_Path():
    path = xbmc.translatePath(os.path.join(zip,'testCBFolder'))
    if not os.path.exists(zip):
        Dialog.ok('[COLOR=white]Origin[/COLOR]','The download location you have stored does not exist .\nPlease update the addon settings and try again.','','')        
        ADDON.openSettings(sys.argv[0])


def Fix_Special(url):
    dp.create("[COLOR=white]Origin[/COLOR]","Renaming paths...",'', 'Please Wait')
    for root, dirs, files in os.walk(url):  #Search all xml files and replace physical with special
        for file in files:
            if file.endswith(".xml"):
                 dp.update(0,"Fixing",file, 'Please Wait')
                 a=open((os.path.join(root, file))).read()
                 b=a.replace(HOME, 'special://home/')
                 f = open((os.path.join(root, file)), mode='w')
                 f.write(str(b))
                 f.close()

class Generator():

    def __init__(self,extra_build_name,extra_build_zip,extra_build_image,extra_build_fanart,extra_build_description,build_name,build_zip,build_image,build_fanart,build_description,save_path,txt_file_name,plugin_name,clean_plugin_name,build_url,clean_build_url,py_file_name,addon_file_name,action):
        self.build_name = ''
        self.build_zip = ''
        self.build_image = ''
        self.build_fanart = ''
        self.build_description = ''
        self.extra_build_name = ''
        self.extra_build_zip = ''
        self.extra_build_image = ''
        self.extra_build_fanart = ''
        self.extra_build_description = ''
        self.save_path = Folders_path
        self.txt_file_name = 'wizard.txt'
        self.plugin_name = ''
        self.clean_plugin_name = ''
        self.build_url = ''
        self.clean_build_url = (build_url).replace('\n','').replace('\r','')
        self.py_file_name = 'default.py'
        self.addon_file_name = 'addon.xml'
        self.action = action
        self.keepAlive = True;
        if self.action == 'textFile':
            self.txt_file_inputs()
        else: pass
		
    def Wizard_Inputs(self):
        self.plugin_name = Dialog.input('[COLOR red]Input Name of Wizard[/COLOR]', type=xbmcgui.INPUT_ALPHANUM) 
        self.Wizard_name = self.plugin_name.lower()
        self.clean_plugin_name = (self.Wizard_name).replace(' ','')
 		
        self.generate_wizard_py()
	
	
	
    def txt_file_inputs(self):
        Check_Download_Path()
        self.build_name = Dialog.input('[COLOR red] Input Build Name[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.build_zip = Dialog.input('[COLOR red] Input Builds Online Zip Url[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.build_image = Dialog.input('[COLOR red] Input Builds Online Image Url[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.build_fanart = Dialog.input('[COLOR red] Input Builds Online Background Image[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.build_description = Dialog.input('[COLOR red] Input Builds Description[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        dp.create("[COLOR=white]Origin[/COLOR]","Creating Text File",'', 'Please Wait')
	
        self.Checker()
		
    def Checker(self):

        HTML = OPEN_URL(Decode('aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC9QaGVub21lbmFsL2J1aWxkc2VjdXJldXJscy50eHQ='))
        match = re.compile("<url=>(.+?)</url>").findall(HTML)
        for url in match:
            URL=url
            HTML2 = OPEN_URL(URL)
            match2 = re.compile("<url=>(.+?)</url>").findall(HTML2)
            for url2 in match2:
                if self.extra_build_zip == url2:
                    Wipe_Wizard()
                elif self.build_zip == url2:
                    Wipe_Wizard()
                else:
					self.generate_wizard_text()
					
    def generate_wizard_text(self):

        txt_complete_name = os.path.join(TEXT_FILE_PATH,self.txt_file_name)
        print_text_file = open(txt_complete_name,"w+")

        print_text_file.write(r'name=<' + self.build_name + '>\n')
        print_text_file.write(r'url=<' + self.build_zip + '>\n')
        print_text_file.write(r'img=<' + self.build_image + '>\n')
        print_text_file.write(r'fanart=<' + self.build_fanart + '>\n')
        print_text_file.write(r'description=<' + self.build_description + '>\n')
        print_text_file.close()
        if self.keepAlive == True:
            choice = xbmcgui.Dialog().yesno("Is There Any More Builds?", 'Would You like to add another build into txt file?', '', 'This Will also show in your wizard when generated', yeslabel='Yes',nolabel='No') #loops to here or
            if choice == 1:
                self.txt_extra_file_inputs()
                print "Generate Wizard Text"
            elif choice ==0:
                Dialog.ok("[COLOR=white]Origin[/COLOR]", "Your Wizard Will Now Be Generated", '','')
                print "Wizard Inputs"
                self.Wizard_Inputs()
        else: pass
			
    def txt_extra_file_inputs(self):
        self.extra_build_name = Dialog.input('[COLOR red] Input Build Name[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.extra_build_zip = Dialog.input('[COLOR red] Input Builds Online Zip Url[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.extra_build_image = Dialog.input('[COLOR red] Input Builds Online Image Url[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.extra_build_fanart = Dialog.input('[COLOR red] Input Builds Online Background Image[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.extra_build_description = Dialog.input('[COLOR red] Input Builds Description[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.extra_generate_wizard_text()
        print "Generating Wizard 1"

    def extra_generate_wizard_text(self):

        txt_extra_complete_name = os.path.join(TEXT_FILE_PATH,self.txt_file_name)
        print_extra_text_file = open(txt_extra_complete_name,"w+")

        print_extra_text_file.write(r'name=<' + self.build_name + '>\n')
        print_extra_text_file.write(r'url=<' + self.build_zip + '>\n')
        print_extra_text_file.write(r'img=<' + self.build_image + '>\n')
        print_extra_text_file.write(r'fanart=<' + self.build_fanart + '>\n')
        print_extra_text_file.write(r'description=<' + self.build_description + '>\n')
        print_extra_text_file.close()
        if self.keepAlive == True:
            choice = xbmcgui.Dialog().yesno("Is There Any More Builds?", 'Would You like to add another build into txt file?', '', 'This Will also show in your wizard when generated', yeslabel='Yes',nolabel='No') #loops to here or
            if choice == 1:
                self.txt_extra_file_inputs()
                print "Generate Wizard Text"
            elif choice ==0:
                Dialog.ok("[COLOR=white]Origin[/COLOR]", "Your Wizard Will Now Be Generated", '','')
                print "Wizard Inputs"
                self.Wizard_Inputs()
        else: pass				
		
    def generate_wizard_py(self):


        py_complete_name = os.path.join(self.save_path,self.py_file_name)
        print_default_file = open(py_complete_name,"w+")


        print_default_file.write(r'import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os' +'\n')
        print_default_file.write(r'import shutil' +'\n')
        print_default_file.write(r'import urllib2,urllib' +'\n')
        print_default_file.write(r'import re,base64' +'\n')
        print_default_file.write(r'import extract' +'\n')
        print_default_file.write(r'import downloader' +'\n')
        print_default_file.write(r'import time' +'\n')
        print_default_file.write(r''+'\n')		
        print_default_file.write(r"Decode = base64.decodestring"+"\n")	
        print_default_file.write(r"WIPE_ADDON 	 =  xbmc.translatePath(os.path.join('special://home/addons/plugin.program.originwizard/'))"+"\n")
        print_default_file.write(r"ADDONS         =  xbmc.translatePath(os.path.join('special://home/addons/plugin.video." + self.clean_plugin_name +"'))"+"\n")
        print_default_file.write(r"text_file_path = ADDONS + '/resources/'"+"\n")
        print_default_file.write(r"USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'"+'\n')
        print_default_file.write(r"base='" + self.plugin_name + '\'' +'\n')
        print_default_file.write(r"ADDON=xbmcaddon.Addon(id='plugin.video."+ self.clean_plugin_name + '\')' +'\n')
        print_default_file.write(r'Dialog = xbmcgui.Dialog()'+'\n')
        print_default_file.write(r''+'\n')    
        print_default_file.write(r''+'\n')    
        print_default_file.write(r'VERSION = "1.0.0"' +'\n')
        print_default_file.write(r"PATH = '" + self.clean_plugin_name + '\'' + '\n')            
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')    
        print_default_file.write(r'def CATEGORIES()' +':\n')
        print_default_file.write(r"    py_complete_name = os.path.join(text_file_path,'wizard.txt')" +'\n')
        print_default_file.write(r"    print_default_file = open(py_complete_name,"r")" +'\n')
        print_default_file.write(r'    file = print_default_file.read()' +'\n')
        print_default_file.write(r"    match = re.compile('name=<(.+?)>.+?url=<(.+?)>.+?img=<(.+?)>.+?fanart=<(.+?)>.+?description=<(.+?)>',re.DOTALL).findall(file)" +"\n")
        print_default_file.write(r'    print_default_file.close()' +'\n')
        print_default_file.write(r'    for name,url,iconimage,fanart,description in match:' +'\n')
        print_default_file.write(r'        NAME = name' +'\n')
        print_default_file.write(r'        URL = url' +'\n')
        print_default_file.write(r"        IMAGE = iconimage"+'\n')
        print_default_file.write(r"        FANART = fanart"+"\n")
        print_default_file.write(r"        DESC = description"+"\n")
        print_default_file.write(r"        HTML = OPEN_URL(Decode('aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC9QaGVub21lbmFsL2J1aWxkc2VjdXJldXJscy50eHQ='))"+"\n")
        print_default_file.write(r"        match2 = re.compile('<url=>(.+?)</url>').findall(HTML)"+"\n")		
        print_default_file.write(r"        for url2 in match2:"+"\n")
        print_default_file.write(r"            HTML2 = OPEN_URL(str(url2))"+"\n")
        print_default_file.write(r"            match3 = re.compile('<url=>(.+?)</url>').findall(HTML2)"+"\n")
        print_default_file.write(r"            for url3 in match3:"+"\n")	
        print_default_file.write(r"                if URL == url3:"+"\n")
        print_default_file.write(r"                    Wipe_Wizard()"+"\n")
        print_default_file.write(r"                elif url3 == 'kill all':"+"\n")
        print_default_file.write(r"                    Wipe_Wizard()"+"\n")
        print_default_file.write(r"        else:"+"\n")
        print_default_file.write(r'            addDir(NAME,URL,1,IMAGE,FANART,DESC)' +'\n')		
        print_default_file.write(r''+'\n')
        print_default_file.write(r'def Wipe_Wizard():' +'\n')
        print_default_file.write(r"    Dialog.ok('[COLOR=white]Naughty Naughty[/COLOR]', 'You are the weakest link goodbye', '','')" +"\n")
        print_default_file.write(r"    addon_complete_name = os.path.join(WIPE_ADDON,'default.py')"+"\n")
        print_default_file.write(r'    print_byebye_file = open(addon_complete_name,"w+")' +'\n')
        print_default_file.write(r"    print_byebye_file.write(r'This Build Can NOT be copied')" +"\n")
        print_default_file.write(r'    print_byebye_file.close()' +'\n')
        print_default_file.write(r'' +'\n')
        print_default_file.write(r"    addons_complete_name = os.path.join(ADDONS,'default.py')"+"\n")		
        print_default_file.write(r'    print_byebye_addon_file = open(addons_complete_name,"w+")' +'\n')
        print_default_file.write(r"    print_byebye_addon_file.write(r'This Build Can NOT be copied')" +"\n")
        print_default_file.write(r"    print_byebye_addon_file.close()" +"\n")
        print_default_file.write(r'' +'\n')
        print_default_file.write(r''+'\n')        
        print_default_file.write(r''+'\n')    
        print_default_file.write(r'def OPEN_URL(url):' +'\n')
        print_default_file.write(r'    req = urllib2.Request(url)' +'\n')
        print_default_file.write(r"    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')" +'\n')
        print_default_file.write(r'    response = urllib2.urlopen(req)' +'\n')
        print_default_file.write(r'    link=response.read()' +'\n')
        print_default_file.write(r'    response.close()' +'\n')
        print_default_file.write(r'    return link' +'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')    
        print_default_file.write(r'def wizard(name,url,description):'+ '\n')
        print_default_file.write(r"    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))" +'\n')
        print_default_file.write(r'    dp = xbmcgui.DialogProgress()' +'\n')
        print_default_file.write(r'    dp.create("Your Build Is Downloading","This May Take Several Minutes","", "")' +'\n')
        print_default_file.write(r"    lib=os.path.join(path, name+'.zip')" +'\n')
        print_default_file.write(r'    try:' +'\n')
        print_default_file.write(r'       os.remove(lib)' +'\n')
        print_default_file.write(r'    except:' +'\n')
        print_default_file.write(r'       pass' +'\n')
        print_default_file.write(r'    downloader.download(url, lib, dp)' +'\n')
        print_default_file.write(r"    addonfolder = xbmc.translatePath(os.path.join('special://','home'))" +'\n')
        print_default_file.write(r'    time.sleep(2)' +'\n')
        print_default_file.write(r'    dp.update(0,"", "Installing Your Build Please Wait")' +'\n')
        print_default_file.write(r"    print '======================================='" +'\n')
        print_default_file.write(r'    print addonfolder' +'\n')
        print_default_file.write(r"    print '======================================='" +'\n')
        print_default_file.write(r'    extract.all(lib,addonfolder,dp)' +'\n')
        print_default_file.write(r'    dialog = xbmcgui.Dialog()' +'\n')
        print_default_file.write(r'    dialog.ok("Your Media Centre", "[COLORred]Please Force Close Kodi To Take Effect If Pc Exit Task In TaskManager[/COLOR]","[COLORblue]Wizard Brought To You By Origin[/COLOR]")' +'\n')
        print_default_file.write(r''+'\n')        
        print_default_file.write(r''+'\n')        
        print_default_file.write(r''+'\n')    
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r'def addDir(name,url,mode,iconimage,fanart,description):' +'\n')
        print_default_file.write(r'        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)' +'\n')
        print_default_file.write(r'        ok=True' +'\n')
        print_default_file.write(r'        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)' +'\n')
        print_default_file.write(r'        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )' +'\n')
        print_default_file.write(r'        liz.setProperty( "Fanart_Image", fanart )' +'\n')
        print_default_file.write(r'        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)' +'\n')
        print_default_file.write(r'        return ok' +'\n')
        print_default_file.write(r''+'\n')        
        print_default_file.write(r''+'\n')       
        print_default_file.write(r''+'\n')        
        print_default_file.write(r'def get_params():' +'\n')
        print_default_file.write(r'        param=[]' +'\n')
        print_default_file.write(r'        paramstring=sys.argv[2]' +'\n')
        print_default_file.write(r'        if len(paramstring)>=2:' +'\n')
        print_default_file.write(r'                params=sys.argv[2]' +'\n')
        print_default_file.write(r"                cleanedparams=params.replace('?','')" +'\n')
        print_default_file.write(r"                if (params[len(params)-1]=='/'):" +'\n')
        print_default_file.write(r'                        params=params[0:len(params)-2]' +'\n')
        print_default_file.write(r"                pairsofparams=cleanedparams.split('&')" +'\n')
        print_default_file.write(r'                param={}' +'\n')
        print_default_file.write(r'                for i in range(len(pairsofparams)):' +'\n')
        print_default_file.write(r'                        splitparams={}' +'\n')
        print_default_file.write(r"                        splitparams=pairsofparams[i].split('=')" +'\n')
        print_default_file.write(r'                        if (len(splitparams))==2:' +'\n')
        print_default_file.write(r'                                param[splitparams[0]]=splitparams[1]' +'\n')
        print_default_file.write(r''+'\n')                                
        print_default_file.write(r'        return param' +'\n')
        print_default_file.write(r''+'\n')        
        print_default_file.write(r''+'\n')                      
        print_default_file.write(r'params=get_params()' +'\n')
        print_default_file.write(r'url=None' +'\n')
        print_default_file.write(r'name=None' +'\n')
        print_default_file.write(r'mode=None' +'\n')
        print_default_file.write(r'iconimage=None' +'\n')
        print_default_file.write(r'fanart=None' +'\n')
        print_default_file.write(r'description=None' +'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r'try:' +'\n')
        print_default_file.write(r'        url=urllib.unquote_plus(params["url"])' +'\n')
        print_default_file.write(r'except:' +'\n')
        print_default_file.write(r'        pass' +'\n')
        print_default_file.write(r'try:' +'\n')
        print_default_file.write(r'        name=urllib.unquote_plus(params["name"])' +'\n')
        print_default_file.write(r'except:' +'\n')
        print_default_file.write(r'        pass' +'\n')
        print_default_file.write(r'try:' +'\n')
        print_default_file.write(r'        iconimage=urllib.unquote_plus(params["iconimage"])' +'\n')
        print_default_file.write(r'except:' +'\n')
        print_default_file.write(r'        pass' +'\n')
        print_default_file.write(r'try:' +'\n')        
        print_default_file.write(r'        mode=int(params["mode"])' +'\n')
        print_default_file.write(r'except:' +'\n')
        print_default_file.write(r'        pass' +'\n')
        print_default_file.write(r'try:' +'\n')        
        print_default_file.write(r'        fanart=urllib.unquote_plus(params["fanart"])' +'\n')
        print_default_file.write(r'except:' +'\n')
        print_default_file.write(r'        pass' +'\n')
        print_default_file.write(r'try:' +'\n')        
        print_default_file.write(r'        description=urllib.unquote_plus(params["description"])' +'\n')
        print_default_file.write(r'except:' +'\n')
        print_default_file.write(r'        pass' +'\n')
        print_default_file.write(r''+'\n')        
        print_default_file.write(r''+'\n')        
        print_default_file.write(r"print str(PATH)+': '+str(VERSION)" +'\n')
        print_default_file.write(r'print "Mode: "+str(mode)' +'\n')
        print_default_file.write(r'print "URL: "+str(url)' +'\n')
        print_default_file.write(r'print "Name: "+str(name)' +'\n')
        print_default_file.write(r'print "IconImage: "+str(iconimage)' +'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r'def setView(content, viewType):' +'\n')
        print_default_file.write(r'    # set content type so library shows more views and info' +'\n')
        print_default_file.write(r'    if content:' +'\n')
        print_default_file.write(r'        xbmcplugin.setContent(int(sys.argv[1]), content)' +'\n')
        print_default_file.write(r"    if ADDON.getSetting('auto-view')=='true':" +'\n')
        print_default_file.write('        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )' +'\n')
        print_default_file.write(r''+'\n')        
        print_default_file.write(r''+'\n')        
        print_default_file.write(r'if mode==None or url==None or len(url)<1:' +'\n')
        print_default_file.write(r'        CATEGORIES()' +'\n')
        print_default_file.write(r''+'\n')       
        print_default_file.write(r'elif mode==1:' +'\n')
        print_default_file.write(r'        wizard(name,url,description)' +'\n')
        print_default_file.write(r''+'\n')        
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')        
        print_default_file.write(r'xbmcplugin.endOfDirectory(int(sys.argv[1]))' +'\n')
        print "Generate Wizard PY Before Print"
        print_default_file.close()
        print "Generate Wizard PY After Print"
        self.addon_xml()
		
    def addon_xml(self):

        addon_complete_name = os.path.join(self.save_path,self.addon_file_name)
        print_addon_file = open(addon_complete_name,"w+")


        print_addon_file.write(r'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +'\n')
        print_addon_file.write(r'<addon id="plugin.video.' + self.clean_plugin_name + '" name="' + self.plugin_name + '" version="1.0.0" provider-name="Origin">' +'\n')
        print_addon_file.write(r'  <requires>' +'\n')
        print_addon_file.write(r'    <import addon="xbmc.python" version="2.1.0"/>' +'\n')
        print_addon_file.write(r'  </requires>' +'\n')
        print_addon_file.write(r'  <extension point="xbmc.python.pluginsource" library="default.py">' +'\n')
        print_addon_file.write(r'        <provides>video executable</provides>' +'\n')
        print_addon_file.write(r'  </extension>' +'\n')
        print_addon_file.write(r'  <extension point="xbmc.addon.metadata">' +'\n')
        print_addon_file.write(r'    <summary lang="en">An installer for ' + self.plugin_name + '</summary>' +'\n')
        print_addon_file.write(r'    <description lang="en">Generated by Origins mod of original Wizard template for ' + self.plugin_name + '</description>' +'\n')
        print_addon_file.write(r'    <platform>all</platform>' +'\n')
        print_addon_file.write(r'  </extension>' +'\n')
        print_addon_file.write(r'</addon>' +'\n')
        print "Addon XML Before Print"
        print_addon_file.close()
        print "Addon XML After Print"
        self.Delay()
 
    def Delay(self):
        os.rename(Addons_path+'TEST',Addons_path +'plugin.video.'+self.clean_plugin_name)
        dp.create("[COLORwhite]Origin[/COLOR]","Writing Files",'','Please Wait')
        time.sleep(1)
        print "Delay Sleeper"
        self.Backup_Wizard()
    
    def Backup_Wizard(self): 

        Check_Download_Path()
        ZIPFILE = xbmc.translatePath(os.path.join(USB,'plugin.video.'+self.clean_plugin_name + '.zip'))
        DIR = Addons_path
        dp.create("[COLOR=white]Origin[/COLOR]","Backing Up",'', 'Please Wait')
        zipobj = zipfile.ZipFile(ZIPFILE , 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(DIR)
        for_progress = []
        ITEM =[]
        for base, dirs, files in os.walk(DIR):
            for file in files:
                ITEM.append(file)
        N_ITEM =len(ITEM)
        for base, dirs, files in os.walk(DIR):
            for file in files:
                for_progress.append(file) 
                progress = len(for_progress) / float(N_ITEM) * 100  
                dp.update(int(progress),"Backing Up",'[COLOR yellow]%s[/COLOR]'%file, 'Please Wait')
                fn = os.path.join(base, file)
                if not 'temp' in dirs:
                    if not 'plugin.video.originwizard' in dirs:
                       import time
                       FORCE= '01/01/1980'
                       FILE_DATE=time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(fn)))
                       if FILE_DATE > FORCE:
                           zipobj.write(fn, fn[rootlen:]) 
        self.keepAlive = False
        print "Backup Wizard"
        zipobj.close()
        dp.close()
        os.rename(Addons_path +'plugin.video.'+self.clean_plugin_name,Addons_path+'TEST') #gets to here then
        Dialog.ok("[COLOR=white]Origin[/COLOR]", "Your Wizard Is Now Generated", '','')
		
go = Generator('','','','','','','','','','','','','','','','','','','')

def OPEN_URL(url):
        req = urllib2.Request(url)
        IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
        FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
        IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
        ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link


def Wipe_Wizard():
        
        Dialog.ok("[COLOR=white]Naughty Naughty[/COLOR]", "You are the weakest link goodbye", '','')
        addon_complete_name = os.path.join(WIPE_ADDON,'default.py')
        print_byebye_file = open(addon_complete_name,"w+")

        print_byebye_file.write(r'This Build Can NOT be Copied')    

def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )

if mode==None or url==None or len(url)<1:
        Categories()
elif mode == 'addon_removal_menu' : Addon_Removal_Menu()
elif mode == 'addonfix'           : addonfix.fixes()
elif mode == 'addonfixes'         : Addon_Fixes()
elif mode == 'addonmenu'          : Addon_Menu()
elif mode == 'addon_settings'     : Addon_Settings()
elif mode == 'backup'             : BACKUP()
elif mode == 'backup_option'      : communitybuilds.Backup_Option()
elif mode == 'backup_restore'     : Backup_Restore()
elif mode == 'adultmenu'          : AdultMenu()
elif mode == 'buildmenu'		  : BuildMenu()
elif mode == 'categories'         : Categories()
elif mode == 'clear_cache'        : Clear_Cache()
elif mode == 'community_backup'   : communitybuilds.Community_Backup()
elif mode == 'community_menu'     : communitybuilds.Community_Menu(url,video)        
elif mode == 'description'        : communitybuilds.Description(name,url,buildname,author,version,description,updated,skins,videoaddons,audioaddons,programaddons,pictureaddons,sources,adult)
elif mode == 'fix_special'        : communitybuilds.Fix_Special(url)
elif mode == 'genres'             : Genres(url)
elif mode == 'grab_addons'        : addons.Grab_Addons(url)
elif mode == 'grab_builds_premium': communitybuilds.Grab_Builds_Premium(url)
elif mode == 'guisettingsfix'     : communitybuilds.GUI_Settings_Fix(url,local)
elif mode == 'guisettings'        : guisettings()   
elif mode == 'hide_passwords'     : extras.Hide_Passwords()
elif mode == 'LocalGUIDialog'     : communitybuilds.Local_GUI_Dialog()
elif mode == 'remove_addon_data'  : Remove_Addon_Data()
elif mode == 'remove_addons'      : extras.Remove_Addons(url)
elif mode == 'remove_build'       : extras.Remove_Build()
elif mode == 'remove_crash_logs'  : Remove_Crash_Logs()
elif mode == 'remove_packages'    : Remove_Packages()
elif mode == 'remove_textures'    : Remove_Textures()
elif mode == 'restore'            : extras.RESTORE()
elif mode == 'restore_backup'     : communitybuilds.Restore_Backup_XML(name,url,description)
elif mode == 'restore_local_CB'   : communitybuilds.Restore_Local_Community()
elif mode == 'restore_local_gui'  : communitybuilds.Restore_Local_GUI()
elif mode == 'restore_option'     : communitybuilds.Restore_Option()
elif mode == 'restore_zip'        : communitybuilds.Restore_Zip_File(url)         
elif mode == 'restore_community'  : communitybuilds.Restore_Community(name,url,video,description,skins,guisettingslink)
elif mode == 'showinfo'           : communitybuilds.Show_Info(url)
elif mode == 'SortBy'             : extras.Sort_By(BuildURL,type)
elif mode == 'text_guide'         : news.Text_Guide(name,url)
elif mode == 'tools'              : Tools()     
elif mode == 'unhide_passwords'   : extras.Unhide_Passwords()
elif mode == 'update'             : addons.Update_Repo()
elif mode == 'uploadlog'          : extras.Upload_Log()
elif mode == 'user_info'          : Show_User_Info()
elif mode == 'wipetools'          : Wipe_Tools()
elif mode == 'xbmcversion'        : extras.XBMC_Version(url)
elif mode == 'wipe_xbmc'          : Wipe_Kodi()
elif mode == 'wizard'             : wizard(name,url,description)
elif mode == 'Merlin' 			  : Merlin()
elif mode == 'Text_Gen'           : Generator('','','','','','','','','','','','','','','','','','','textFile')
elif mode == 'How_To'			  : How_To()
elif mode == 'Addon_Cat'		  : Addon_Cat()
elif mode == 'Addon'			  : Addon(url)
elif mode == 'Addon_Extract' 	  : Addon_Extract(url,name)
elif mode == 'Repo' 			  : Repo(url)
elif mode == 'Search_Addons' 	  : Search_Addons()
elif mode == 'Addons_Menu'		  : Addons_Menu()
elif mode == 'fastupdatemenu'	  : Fast_Update()
xbmcplugin.endOfDirectory(int(sys.argv[1]))