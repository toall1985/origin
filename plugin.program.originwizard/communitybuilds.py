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
import extras
import shutil
import urllib2,urllib
import re
import extract
import time
import CheckPath
import downloader
import zipfile
import ntpath

ARTPATH      =  'http://URLHERE.COM' + os.sep
ADDON        =  xbmcaddon.Addon(id='plugin.program.originwizard')
AddonID      =  'plugin.program.originwizard'
AddonTitle   =  "[COLOR=blue]Origin Wizard[/COLOR]"
zip          =  ADDON.getSetting('zip')
localcopy    =  ADDON.getSetting('localcopy')
privatebuilds=  ADDON.getSetting('private')
reseller     =  ADDON.getSetting('reseller')
resellername =  ADDON.getSetting('resellername')
resellerid   =  ADDON.getSetting('resellerid')
mastercopy   =  ADDON.getSetting('mastercopy')
trcheck      =  ADDON.getSetting('trcheck')
dialog       =  xbmcgui.Dialog()
dp           =  xbmcgui.DialogProgress()
HOME         =  xbmc.translatePath('special://home/')
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata/',''))
MEDIA        =  xbmc.translatePath(os.path.join('special://home/media/',''))
AUTOEXEC     =  xbmc.translatePath(os.path.join(USERDATA,'autoexec.py'))
AUTOEXECBAK  =  xbmc.translatePath(os.path.join(USERDATA,'autoexec_bak.py'))
ADDON_DATA   =  xbmc.translatePath(os.path.join(USERDATA,'addon_data'))
PLAYLISTS    =  xbmc.translatePath(os.path.join(USERDATA,'playlists'))
DATABASE     =  xbmc.translatePath(os.path.join(USERDATA,'Database'))
ADDONS       =  xbmc.translatePath(os.path.join('special://home','addons',''))
CBADDONPATH  =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'default.py'))
GENESIS 	 =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.genesis/favourites.db'))
GUISETTINGS  =  os.path.join(USERDATA,'guisettings.xml')
GUI          =  xbmc.translatePath(os.path.join(USERDATA,'guisettings.xml'))
GUIFIX       =  xbmc.translatePath(os.path.join(USERDATA,'guifix.xml'))
INSTALL      =  xbmc.translatePath(os.path.join(USERDATA,'install.xml'))
IVUE 		 =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.ivueguide/master.db'))
FAVS         =  xbmc.translatePath(os.path.join(USERDATA + 'favourites.xml'))
SOURCE       =  xbmc.translatePath(os.path.join(USERDATA,'sources.xml'))
ADVANCED     =  xbmc.translatePath(os.path.join(USERDATA,'advancedsettings.xml'))
PROFILES     =  xbmc.translatePath(os.path.join(USERDATA,'profiles.xml'))
RSS          =  xbmc.translatePath(os.path.join(USERDATA,'RssFeeds.xml'))
KEYMAPS      =  xbmc.translatePath(os.path.join(USERDATA,'keymaps','keyboard.xml'))
USB          =  xbmc.translatePath(os.path.join(zip))
CBPATH       =  xbmc.translatePath(os.path.join(USB,'Community Builds',''))
startuppath  =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'startup.xml'))
tempfile     =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'temp.xml'))
idfile       =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'id.xml'))
idfiletemp   =  xbmc.translatePath(os.path.join(ADDON_DATA,AddonID,'idtemp.xml'))
skin         =  xbmc.getSkinDir()
username     =  ADDON.getSetting('username')
password     =  ADDON.getSetting('password')
login        =  ADDON.getSetting('login')
userdatafolder = xbmc.translatePath(os.path.join(ADDON_DATA,AddonID))
GUINEW       =  xbmc.translatePath(os.path.join(userdatafolder,'guinew.xml'))
guitemp      =  xbmc.translatePath(os.path.join(userdatafolder,'guitemp',''))
tempdbpath   =  xbmc.translatePath(os.path.join(USB,'Database'))
urlbase      =  'None'

#---------------------------------------------------------------------------------------------------
#Main addDirectory function - xbmcplugin.addDirectoryItem()
def Add_Directory_Item(handle, url, listitem, isFolder):
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder)
#---------------------------------------------------------------------------------------------------
#Add a standard directory for the builds. Essentially the same as above but grabs unique artwork from previous call
def Add_Build_Dir(name,url,mode,iconimage,fanart,video,description,skins,guisettingslink):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&video="+urllib.quote_plus(video)+"&description="+urllib.quote_plus(description)+"&skins="+urllib.quote_plus(skins)+"&guisettingslink="+urllib.quote_plus(guisettingslink)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        liz.setProperty( "Build.Video", video )
        if (mode==None) or (mode=='restore_option') or (mode=='backup_option') or (mode=='cb_root_menu') or (mode=='genres') or (mode=='grab_builds') or (mode=='community_menu') or (mode=='instructions') or (mode=='countries')or (url==None) or (len(url)<1):
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
#---------------------------------------------------------------------------------------------------
#Add a directory for the description, this requires multiple string to be called from previous menu
def Add_Desc_Dir(name,url,mode,iconimage,fanart,buildname,author,version,description,updated,skins,videoaddons,audioaddons,programaddons,pictureaddons,sources,adult):
        iconimage = ARTPATH + iconimage
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&author="+urllib.quote_plus(author)+"&description="+urllib.quote_plus(description)+"&version="+urllib.quote_plus(version)+"&buildname="+urllib.quote_plus(buildname)+"&updated="+urllib.quote_plus(updated)+"&skins="+urllib.quote_plus(skins)+"&videoaddons="+urllib.quote_plus(videoaddons)+"&audioaddons="+urllib.quote_plus(audioaddons)+"&buildname="+urllib.quote_plus(buildname)+"&programaddons="+urllib.quote_plus(programaddons)+"&pictureaddons="+urllib.quote_plus(pictureaddons)+"&sources="+urllib.quote_plus(sources)+"&adult="+urllib.quote_plus(adult)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        liz.setProperty( "Build.Video", video )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
#---------------------------------------------------------------------------------------------------
#Zip up tree
def Archive_Tree(sourcefile, destfile, message_header, message1, message2, message3, exclude_dirs, exclude_files):
    zipobj = zipfile.ZipFile(destfile , 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(sourcefile)
    for_progress = []
    ITEM =[]
    dp.create(message_header, message1, message2, message3)
    for base, dirs, files in os.walk(sourcefile):
        for file in files:
            ITEM.append(file)
    N_ITEM =len(ITEM)
    for base, dirs, files in os.walk(sourcefile):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        files[:] = [f for f in files if f not in exclude_files]
        for file in files:
            for_progress.append(file) 
            progress = len(for_progress) / float(N_ITEM) * 100  
            dp.update(int(progress),"Backing Up",'[COLOR yellow]%s[/COLOR]'%file, 'Please Wait')
            fn = os.path.join(base, file)
            if not 'temp' in dirs:
                if not 'plugin.program.originwizard' in dirs:
                   import time
                   FORCE= '01/01/1980'
                   FILE_DATE=time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(fn)))
                   if FILE_DATE > FORCE:
                       zipobj.write(fn, fn[rootlen:])  
    zipobj.close()
    dp.close()
#---------------------------------------------------------------------------------------------------
#Zip up tree
def Archive_File(sourcefile, destfile):
    zipobj = zipfile.ZipFile(destfile , 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(sourcefile)
    for_progress = []
    ITEM =[]
    dp.create("[COLOR=white]Origin[/COLOR]","Archiving...",'', 'Please Wait')
    for base, dirs, files in os.walk(sourcefile):
        for file in files:
            ITEM.append(file)
    N_ITEM =len(ITEM)
    for base, dirs, files in os.walk(sourcefile):
        for file in files:
            for_progress.append(file) 
            progress = len(for_progress) / float(N_ITEM) * 100  
            dp.update(int(progress),"Backing Up",'[COLOR yellow]%s[/COLOR]'%file, 'Please Wait')
            fn = os.path.join(base, file)
            if not 'temp' in dirs:
                if not 'plugin.program.originwizard' in dirs:
                   import time
                   FORCE= '01/01/1980'
                   FILE_DATE=time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(fn)))
                   if FILE_DATE > FORCE:
                       zipobj.write(fn, fn[rootlen:])  
    zipobj.close()
    dp.close()
#---------------------------------------------------------------------------------------------------
#Create backup menu
def Backup_Option():
    extras.addDir('','[COLOR=yellow]Full Backup[/COLOR]','url','community_backup','Backup.png','','','Back Up Your Full System')
    extras.addDir('','Backup Just Your Addons','addons','restore_zip','Backup.png','','','Back Up Your Addons')
    extras.addDir('','Backup Just Your Addon UserData','addon_data','restore_zip','Backup.png','','','Back Up Your Addon Userdata')
    extras.addDir('','Backup Guisettings.xml',GUI,'restore_backup','Backup.png','','','Back Up Your guisettings.xml')
    if os.path.exists(IVUE):
        extras.addDir('','Backup Ivue Config',IVUE,'restore_backup','Backup.png','','','Back Up Your master.db')	    
    if os.path.exists(GENESIS):
        extras.addDir('','Backup Genesis Favourites',GENESIS,'restore_backup','Backup.png','','','Back Up Your Favourites.db')	    
    if os.path.exists(FAVS):
        extras.addDir('','Backup Favourites.xml',FAVS,'restore_backup','Backup.png','','','Back Up Your favourites.xml')
    if os.path.exists(SOURCE):
        extras.addDir('','Backup Source.xml',SOURCE,'restore_backup','Backup.png','','','Back Up Your sources.xml')
    if os.path.exists(ADVANCED):
        extras.addDir('','Backup Advancedsettings.xml',ADVANCED,'restore_backup','Backup.png','','','Back Up Your advancedsettings.xml')
    if os.path.exists(KEYMAPS):
        extras.addDir('','Backup Advancedsettings.xml',KEYMAPS,'restore_backup','Backup.png','','','Back Up Your keyboard.xml')
    if os.path.exists(RSS):
        extras.addDir('','Backup RssFeeds.xml',RSS,'restore_backup','Backup.png','','','Back Up Your RssFeeds.xml')
#---------------------------------------------------------------------------------------------------
#Function to restore a zip file 
def Check_Download_Path():
    path = xbmc.translatePath(os.path.join(zip,'testCBFolder'))
    if not os.path.exists(zip):
        dialog.ok('[COLOR=white]Origin[/COLOR]','The download location you have stored does not exist .\nPlease update the addon settings and try again.','','')        
        ADDON.openSettings(sys.argv[0])
#---------------------------------------------------------------------------------------------------
#Create restore menu
def Check_Local_Install():
    localfile = open(idfile, mode='r')
    content = file.read(localfile)
    file.close(localfile)
    localbuildmatch = re.compile('name="(.+?)"').findall(content)
    localbuildcheck  = localbuildmatch[0] if (len(localbuildmatch) > 0) else ''
    if localbuildcheck == "Incomplete":
        choice = xbmcgui.Dialog().yesno("Finish Restore Process", 'If you\'re certain the correct skin has now been set click OK', 'to finish the install process, once complete XBMC/Kodi will', ' then close. Do you want to finish the install process?', yeslabel='Yes',nolabel='No')
        if choice == 1:
            Finish_Local_Restore()
        elif choice ==0:
            return
#---------------------------------------------------------------------------------------------------
#Check whether or not the guisettings fix has been done, loops on a timer.
def Check_GUI_Temp(url):
    time.sleep(120)
    if os.path.exists(guitemp):
        choice = xbmcgui.Dialog().yesno('Run step 2 of install', 'You still haven\'t completed step 2 of the', 'install. Would you like to complete it now?', '', nolabel='No, not yet',yeslabel='Yes, complete setup')
        if choice == 0:
            Check_GUI_Temp(url)
        elif choice == 1:
            try: xbmc.executebuiltin("PlayerControl(Stop)")       
            except: pass
            xbmc.executebuiltin("ActivateWindow(appearancesettings)")
            GUI_Merge(url)
#---------------------------------------------------------------------------------------------------
#Create a community (universal) backup - this renames paths to special:// and removes unwanted folders
def Community_Backup():
    guisuccess=1
    Check_Download_Path()
    fullbackuppath = xbmc.translatePath(os.path.join(USB,'Community Builds','My Builds',''))
    myfullbackup = xbmc.translatePath(os.path.join(USB,'Community Builds','My Builds','my_full_backup.zip'))
    myfullbackupGUI = xbmc.translatePath(os.path.join(USB,'Community Builds','My Builds','my_full_backup_GUI_Settings.zip'))
    if not os.path.exists(fullbackuppath):
        os.makedirs(fullbackuppath)
    vq = extras.Get_Keyboard( heading="Enter a name for this backup" )
    if ( not vq ): return False, 0
    title = urllib.quote_plus(vq)
    backup_zip = xbmc.translatePath(os.path.join(fullbackuppath,title+'.zip'))
    exclude_dirs_full =  ['plugin.program.originwizard']
    exclude_files_full = ["xbmc.log","xbmc.old.log","kodi.log","kodi.old.log",'.DS_Store','.setup_complete','XBMCHelper.conf']
    exclude_dirs =  ['plugin.program.originwizard', 'plugin.repository.shadowcrew','cache', 'system', 'Thumbnails', "peripheral_data",'library','keymaps']
    exclude_files = ["xbmc.log","xbmc.old.log","kodi.log","kodi.old.log","Textures13.db",'.DS_Store','.setup_complete','XBMCHelper.conf', 'advancedsettings.xml']
    message_header = "Creating full backup of existing build"
    message_header2 = "Creating Community Build"
    message1 = "Archiving..."
    message2 = ""
    message3 = "Please Wait"
    if mastercopy=='true':
        Archive_Tree(HOME, myfullbackup, message_header, message1, message2, message3, exclude_dirs_full, exclude_files_full)
    choice = xbmcgui.Dialog().yesno("Do you want to include your addon_data folder?", 'This contains ALL addon settings including passwords.', 'If you\'re intending on sharing this with others we stongly', 'recommend against this unless all data has been manually removed.', yeslabel='Yes',nolabel='No')
    if choice == 0:
        DeleteAddonData()
    elif choice == 1:
        pass
    Fix_Special(HOME)
    Delete_Packages()
    Archive_Tree(HOME, backup_zip, message_header2, message1, message2, message3, exclude_dirs, exclude_files)  
    time.sleep(1)
    GUIname = xbmc.translatePath(os.path.join(fullbackuppath, title+'_guisettings.zip'))
    zf = zipfile.ZipFile(GUIname, mode='w')
    try:
        zf.write(GUI, 'guisettings.xml', zipfile.ZIP_DEFLATED) #Copy guisettings.xml
    except: guisuccess=0
    try:
        zf.write(xbmc.translatePath(os.path.join(HOME,'userdata','profiles.xml')), 'profiles.xml', zipfile.ZIP_DEFLATED) #Copy profiles.xml
    except: pass
    zf.close()
    if mastercopy=='true':
        zfgui = zipfile.ZipFile(myfullbackupGUI, mode='w')
        try:
            zfgui.write(GUI, 'guisettings.xml', zipfile.ZIP_DEFLATED) #Copy guisettings.xml
        except: guisuccess=0

        try:
            zfgui.write(xbmc.translatePath(os.path.join(HOME,'userdata','profiles.xml')), 'profiles.xml', zipfile.ZIP_DEFLATED) #Copy profiles.xml
        except: pass
        zfgui.close()
    if guisuccess == 0:
        dialog.ok("FAILED!", 'The guisettings.xml file could not be found on your', 'system, please reboot and try again.', '')
    else:
        dialog.ok("SUCCESS!", 'You Are Now Backed Up. If you\'d like to share this build with', 'the community please post details on the forum at', '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]')
        dialog.ok("Build Locations", 'Full Backup (only used to restore on this device): [COLOR=yellow]'+myfullbackup, '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]'+backup_zip+'[/COLOR]')
#---------------------------------------------------------------------------------------------------
#Function to delete the userdata/addon_data folder
def DeleteAddonData():
    print '############################################################       DELETING USERDATA             ###############################################################'
    addon_data_path = xbmc.translatePath(os.path.join('special://home/userdata/addon_data', ''))
    for root, dirs, files in os.walk(addon_data_path):
        file_count = 0
        file_count += len(files)
    # Count files and give option to delete
        if file_count >= 0:
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))        
#---------------------------------------------------------------------------------------------------
#Delete Packages Folder
def Delete_Packages():
    print '############################################################       DELETING PACKAGES             ###############################################################'
    packages_cache_path = xbmc.translatePath(os.path.join('special://home/addons/packages', ''))
    for root, dirs, files in os.walk(packages_cache_path):
        file_count = 0
        file_count += len(files)
    # Count files and give option to delete
        if file_count > 0:
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
#---------------------------------------------------------------------------------------------------
#Convert physical paths to special paths
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
#---------------------------------------------------------------------------------------------------
#Installs special art for premium.
def Install_Art(path):
    background_art = xbmc.translatePath(os.path.join(USERDATA,'background_art',''))
    if not os.path.exists(background_art):
        os.makedirs(background_art)
    try:
        dp.create("Installing Artwork","Downloading artwork pack",'', 'Please Wait')
        artpack=os.path.join(USB, resellername+'_artpack.zip')
        downloader.download(path, artpack, dp)
        time.sleep(1)
#        Read_Zip(artpack)
        dp.create("[COLOR=white]Origin[/COLOR]","Checking ",'', 'Please Wait')
        dp.update(0,"", "Extracting Zip Please Wait")
        extract.all(artpack,background_art,dp)
    except: pass
#---------------------------------------------------------------------------------------------------
# Dialog to warn users about local guisettings fix.
def Local_GUI_Dialog():
    dialog.ok("Restore local guisettings fix", "You should [COLOR=red]ONLY[/COLOR] use this option if the guisettings fix", "is failing to download via the addon. Installing via this","method means you do not receive notifications of updates")
    Restore_Local_GUI()
#---------------------------------------------------------------------------------------------------
#Read a zip file and extract the relevant data
def Read_Zip(url):
    z = zipfile.ZipFile(url, "r")
    for filename in z.namelist():
        if 'guisettings.xml' in filename:
            a = z.read(filename)
            r='<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>'% skin
            match=re.compile(r).findall(a)
            for type,string,setting in match:
                setting=setting.replace('&quot;','') .replace('&amp;','&') 
                xbmc.executebuiltin("Skin.Set%s(%s,%s)"%(type.title(),string,setting))
        if 'favourites.xml' in filename:
            a = z.read(filename)
            f = open(FAVS, mode='w')
            f.write(a)
            f.close()
        if 'sources.xml' in filename:
            a = z.read(filename)
            f = open(SOURCE, mode='w')
            f.write(a)
            f.close()
        if 'advancedsettings.xml' in filename:
            a = z.read(filename)
            f = open(ADVANCED, mode='w')
            f.write(a)
            f.close()
        if 'RssFeeds.xml' in filename:
            a = z.read(filename)
            f = open(RSS, mode='w')
            f.write(a)
            f.close()
        if 'keyboard.xml' in filename:
            a = z.read(filename)
            f = open(KEYMAPS, mode='w')
            f.write(a)
            f.close()                              
#---------------------------------------------------------------------------------------------------
#Function to restore a backup xml file (guisettings, sources, RSS)
def Restore_Backup_XML(name,url,description):
    if 'Backup' in name:
        Check_Download_Path()
        TO_READ   = open(url).read()
        TO_WRITE  = os.path.join(USB,description.split('Your ')[1])
        f = open(TO_WRITE, mode='w')
        f.write(TO_READ)
        f.close() 
    else:
        if 'guisettings.xml' in description:
            a = open(os.path.join(USB,description.split('Your ')[1])).read()
            r='<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>'% skin
            match=re.compile(r).findall(a)
            for type,string,setting in match:
                setting=setting.replace('&quot;','') .replace('&amp;','&') 
                xbmc.executebuiltin("Skin.Set%s(%s,%s)"%(type.title(),string,setting))  
        else:    
            TO_WRITE   = os.path.join(url)
            TO_READ  = open(os.path.join(USB,description.split('Your ')[1])).read()
            f = open(TO_WRITE, mode='w')
            f.write(TO_READ)
            f.close()  
    dialog.ok("[COLOR=white]Origin[/COLOR]", "", 'All Done !','')
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#Function to restore a local copy of a CB file
#### THIS CODE BLOCK SHOULD BE MERGED INTO THE RESTORE_COMMUNITY FUNCTION BUT I RAN OUT OF TIME TO DO IT CLEANLY ###
def Restore_Local_Community():
    exitfunction=0
    choice4=0
    Check_Download_Path()
    filename = xbmcgui.Dialog().browse(1, 'Select the backup file you want to restore', 'files', '.zip', False, False, USB)
    if filename == '':
        return
    if os.path.exists(GUINEW):
        if os.path.exists(GUI):
            os.remove(GUINEW)
        else:
            os.rename(GUINEW,GUI)
    if os.path.exists(GUIFIX):
        os.remove(GUIFIX)
    if not os.path.exists(tempfile): #Function for debugging, creates a file that was created in previous call and subsequently deleted when run
        localfile = open(tempfile, mode='w+')
    if os.path.exists(guitemp):
        os.removedirs(guitemp)
    try: os.rename(GUI,GUINEW) #Rename guisettings.xml to guinew.xml so we can edit without XBMC interfering.
    except:
        dialog.ok("NO GUISETTINGS!",'No guisettings.xml file has been found.', 'Please exit XBMC and try again','')
        return
    choice = xbmcgui.Dialog().yesno(name, 'We highly recommend backing up your existing build before', 'installing any builds.', 'Would you like to perform a backup first?', nolabel='Backup',yeslabel='Install')
    if choice == 0:
        mybackuppath = xbmc.translatePath(os.path.join(USB,'Community Builds','My Builds'))
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
        Archive_Tree(HOME, backup_zip, message_header, message1, message2, message3, exclude_dirs_full, exclude_files_full)
    choice3 = xbmcgui.Dialog().yesno(name, 'Would you like to keep your existing database', 'files or overwrite? Overwriting will wipe any', 'existing music or video library you may have scanned in.', nolabel='Overwrite',yeslabel='Keep Existing')
    if choice3 == 0: pass
    elif choice3 == 1:
        if os.path.exists(tempdbpath):
            shutil.rmtree(tempdbpath)
        try:
            shutil.copytree(DATABASE, tempdbpath, symlinks=False, ignore=shutil.ignore_patterns("Textures13.db","Addons16.db","Addons15.db","saltscache.db-wal","saltscache.db-shm","saltscache.db","onechannelcache.db")) #Create temp folder for databases, give user option to overwrite existing library
        except:
            choice4 = xbmcgui.Dialog().yesno(name, 'There was an error trying to backup some databases.', 'Continuing may wipe your existing library. Do you', 'wish to continue?', nolabel='No, cancel',yeslabel='Yes, overwrite')
            if choice4 == 1: pass
            if choice4 == 0: exitfunction=1;return
        backup_zip = xbmc.translatePath(os.path.join(USB,'Database.zip'))
        Archive_File(tempdbpath,backup_zip)
    if exitfunction == 1:
        return
    else:
        time.sleep(1)
        readfile = open(CBADDONPATH, mode='r')
        default_contents = readfile.read()
        readfile.close()
        Read_Zip(filename)
        dp.create("[COLOR=white]Origin[/COLOR]","Checking ",'', 'Please Wait')
        dp.update(0,"", "Extracting Zip Please Wait")
        extract.all(filename,HOME,dp)
        time.sleep(1)
        clean_title = ntpath.basename(filename)
        writefile = open(idfile, mode='w+')
        writefile.write('id="none"\nname="'+clean_title+' [COLOR=yellow](Partially installed)[/COLOR]"\nversion="none"')
        writefile.close()
        cbdefaultpy = open(CBADDONPATH, mode='w+')
        cbdefaultpy.write(default_contents)
        cbdefaultpy.close()
        try:
            os.rename(GUI,GUIFIX)
        except:
            print"NO GUISETTINGS DOWNLOADED"
        time.sleep(1)
        localfile = open(GUINEW, mode='r') #Read the original skinsettings tags and store in memory ready to replace in guinew.xml
        content = file.read(localfile)
        file.close(localfile)
        skinsettingsorig = re.compile('<skinsettings>[\s\S]*?<\/skinsettings>').findall(content)
        skinorig  = skinsettingsorig[0] if (len(skinsettingsorig) > 0) else ''
        skindefault = re.compile('<skin default[\s\S]*?<\/skin>').findall(content)
        skindefaultorig  = skindefault[0] if (len(skindefault) > 0) else ''
        lookandfeelorig = re.compile('<lookandfeel>[\s\S]*?<\/lookandfeel>').findall(content)
        lookandfeel  = lookandfeelorig[0] if (len(lookandfeelorig) > 0) else ''
        try:
            localfile2 = open(GUIFIX, mode='r')
            content2 = file.read(localfile2)
            file.close(localfile2)
            skinsettingscontent = re.compile('<skinsettings>[\s\S]*?<\/skinsettings>').findall(content2)
            skinsettingstext  = skinsettingscontent[0] if (len(skinsettingscontent) > 0) else ''
            skindefaultcontent = re.compile('<skin default[\s\S]*?<\/skin>').findall(content2)
            skindefaulttext  = skindefaultcontent[0] if (len(skindefaultcontent) > 0) else ''
            lookandfeelcontent = re.compile('<lookandfeel>[\s\S]*?<\/lookandfeel>').findall(content2)
            lookandfeeltext  = lookandfeelcontent[0] if (len(lookandfeelcontent) > 0) else ''
            replacefile = content.replace(skinorig,skinsettingstext).replace(lookandfeel,lookandfeeltext).replace(skindefaultorig,skindefaulttext)
            writefile = open(GUINEW, mode='w+')
            writefile.write(str(replacefile))
            writefile.close()
        except:
            print"NO GUISETTINGS DOWNLOADED"
        if os.path.exists(GUI):
            os.remove(GUI)
        os.rename(GUINEW,GUI)
        try:
            os.remove(GUIFIX)
        except:
            pass
        if choice3 == 1:
            extract.all(backup_zip,DATABASE,dp) #This folder first needs zipping up
            if choice4 !=1:
                shutil.rmtree(tempdbpath)
        os.makedirs(guitemp)
        time.sleep(1)
        xbmc.executebuiltin('UnloadSkin()') 
        time.sleep(1)
        xbmc.executebuiltin('ReloadSkin()')
        time.sleep(1)
        xbmc.executebuiltin("ActivateWindow(appearancesettings)")
        while xbmc.executebuiltin("Window.IsActive(appearancesettings)"):
            xbmc.sleep(500)
        try: xbmc.executebuiltin("LoadProfile(Master user)")
        except: pass
        dialog.ok('[COLOR=white]Origin[/COLOR]','Step 1 complete. Now please change the skin to','the one this build was designed for. Once done come back','to this addon and restore the guisettings_fix.zip')        
        xbmc.executebuiltin("ActivateWindow(appearancesettings)")
#---------------------------------------------------------------------------------------------------
#Function to restore a local copy of guisettings_fix
def Restore_Local_GUI():
    import time
    Check_Download_Path()
    guifilename = xbmcgui.Dialog().browse(1, 'Select the guisettings zip file you want to restore', 'files', '.zip', False, False, USB)
    if guifilename == '':
        return
    else:
        local=1
        GUI_Settings_Fix(guifilename,local)  
#---------------------------------------------------------------------------------------------------
#Create restore menu
def Restore_Option():
    if trcheck == 'true':
        Check_Local_Install()
    extras.addDir('','[COLOR=lime]RESTORE LOCAL BUILD[/COLOR]','url','restore_local_CB','Restore.png','','','Back Up Your Full System')
    extras.addDir('','[COLOR=dodgerblue]Restore Local guisettings file[/COLOR]','url','LocalGUIDialog','Restore.png','','','Back Up Your Full System')
    
    if os.path.exists(os.path.join(USB,'addons.zip')):   
        extras.addDir('','Restore Your Addons','addons','restore_zip','Restore.png','','','Restore Your Addons')

    if os.path.exists(os.path.join(USB,'addon_data.zip')):   
        extras.addDir('','Restore Your Addon UserData','addon_data','restore_zip','Restore.png','','','Restore Your Addon UserData')           

    if os.path.exists(os.path.join(USB,'guisettings.xml')):
        extras.addDir('','Restore Guisettings.xml',GUI,'restore_backup','Restore.png','','','Restore Your guisettings.xml')

    if os.path.exists(os.path.join(USB,'master.db')):
        extras.addDir('','Restore Ivue Config',IVUE,'restore_backup','Restore.png','','','Restore Your master.db')
    
    if os.path.exists(os.path.join(USB,'favourites.xml')):
        extras.addDir('','Restore Favourites.xml',FAVS,'restore_backup','Restore.png','','','Restore Your favourites.xml')
    
    if os.path.exists(os.path.join(USB,'favourites.db')):
        extras.addDir('','Restore Genesis Favourites',GENESIS,'restore_backup','Restore.png','','','Restore Your favourites.db')
        
    if os.path.exists(os.path.join(USB,'sources.xml')):
        extras.addDir('','Restore Source.xml',SOURCE,'restore_backup','Restore.png','','','Restore Your sources.xml')
        
    if os.path.exists(os.path.join(USB,'advancedsettings.xml')):
        extras.addDir('','Restore Advancedsettings.xml',ADVANCED,'restore_backup','Restore.png','','','Restore Your advancedsettings.xml')        

    if os.path.exists(os.path.join(USB,'keyboard.xml')):
        extras.addDir('','Restore Advancedsettings.xml',KEYMAPS,'restore_backup','Restore.png','','','Restore Your keyboard.xml')
        
    if os.path.exists(os.path.join(USB,'RssFeeds.xml')):
        extras.addDir('','Restore RssFeeds.xml',RSS,'resore_backup','Restore.png','','','Restore Your RssFeeds.xml')    
#---------------------------------------------------------------------------------------------------
#Function to restore a previously backed up zip, this includes full backup, addons or addon_data.zip
def Restore_Zip_File(url):
    Check_Download_Path()
    if 'addons' in url:
        ZIPFILE = xbmc.translatePath(os.path.join(USB,'addons.zip'))
        DIR = ADDONS
        to_backup = ADDONS
        backup_zip = xbmc.translatePath(os.path.join(USB,'addons.zip'))
    else:
        ZIPFILE = xbmc.translatePath(os.path.join(USB,'addon_data.zip'))
        DIR = ADDON_DATA
    if 'Backup' in name:
        Delete_Packages() 
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
                    if not 'plugin.program.originwizard' in dirs:
                       import time
                       FORCE= '01/01/1980'
                       FILE_DATE=time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(fn)))
                       if FILE_DATE > FORCE:
                           zipobj.write(fn, fn[rootlen:]) 
        zipobj.close()
        dp.close()
        dialog.ok("[COLOR=white]Origin[/COLOR]", "You Are Now Backed Up", '','')   
    else:
        dp.create("[COLOR=white]Origin[/COLOR]","Checking ",'', 'Please Wait')
        dp.update(0,"", "Extracting Zip Please Wait")
        extract.all(ZIPFILE,DIR,dp)
        time.sleep(1)
        xbmc.executebuiltin('UpdateLocalAddons ')    
        xbmc.executebuiltin("UpdateAddonRepos")        
        if 'Backup' in name:
            extras.Kill_XBMC()
            dialog.ok("Community Builds - Install Complete", 'To ensure the skin settings are set correctly XBMC will now', 'close. If XBMC doesn\'t close please force close (pull power', 'or force close in your OS - [COLOR=lime]DO NOT exit via Kodi menu[/COLOR])')
        else:
            dialog.ok("[COLOR=white]Origin[/COLOR]", "You Are Now Restored", '','')        
#---------------------------------------------------------------------------------------------------
# Check local file version name and number against db
def Show_Info(url):
    BaseURL='http://totalxbmc.com/totalrevolution/Community_Builds/community_builds.php?id=%s' % (url)
    link = extras.Open_URL(BaseURL).replace('\n','').replace('\r','')
    namematch = re.compile('name="(.+?)"').findall(link)
    authormatch = re.compile('author="(.+?)"').findall(link)
    versionmatch = re.compile('version="(.+?)"').findall(link)
#    updatedmatch = re.compile('updated="(.+?)"').findall(link)
    name  = namematch[0] if (len(namematch) > 0) else ''
    author  = authormatch[0] if (len(authormatch) > 0) else ''
    version  = versionmatch[0] if (len(versionmatch) > 0) else ''
#    updated  = updatedmatch[0] if (len(updatedmatch) > 0) else ''
    dialog.ok(name,'Author: '+author,'Latest Version: '+version,'')
    return
#---------------------------------------------------------------------------------------------------
#Search in description
def Search_Builds(url):
    vq = extras.Get_Keyboard( heading="Search for content" )
    # if blank or the user cancelled the keyboard, return
    if ( not vq ): return False, 0
    # we need to set the title to our query
    title = urllib.quote_plus(vq)
    url += title
    Grab_Builds(url)
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
# Addon starts here
params=Get_Params()
url=None
name=None
buildname=None
updated=None
author=None
version=None
mode=None
iconimage=None
description=None
video=None
link=None
skins=None
videoaddons=None
audioaddons=None
programaddons=None
audioaddons=None
sources=None
local=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        guisettingslink=urllib.unquote_plus(params["guisettingslink"])
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
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        mode=str(params["mode"])
except:
        pass
try:
        link=urllib.unquote_plus(params["link"])
except:
        pass
try:
        skins=urllib.unquote_plus(params["skins"])
except:
        pass
try:
        videoaddons=urllib.unquote_plus(params["videoaddons"])
except:
        pass
try:
        audioaddons=urllib.unquote_plus(params["audioaddons"])
except:
        pass
try:
        programaddons=urllib.unquote_plus(params["programaddons"])
except:
        pass
try:
        pictureaddons=urllib.unquote_plus(params["pictureaddons"])
except:
        pass
try:
        local=urllib.unquote_plus(params["local"])
except:
        pass
try:
        sources=urllib.unquote_plus(params["sources"])
except:
        pass
try:
        adult=urllib.unquote_plus(params["adult"])
except:
        pass
try:
        buildname=urllib.unquote_plus(params["buildname"])
except:
        pass
try:
        updated=urllib.unquote_plus(params["updated"])
except:
        pass
try:
        version=urllib.unquote_plus(params["version"])
except:
        pass
try:
        author=urllib.unquote_plus(params["author"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
try:        
        video=urllib.unquote_plus(params["video"])
except:
        pass