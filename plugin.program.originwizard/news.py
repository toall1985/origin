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

ARTPATH      =  'http://totalxbmc.tv/totalrevolution/art/' + os.sep
ADDON        =  xbmcaddon.Addon(id='plugin.program.originwizard')
AddonID      =  'plugin.program.originwizard'
AddonTitle   =  "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]"
zip          =  ADDON.getSetting('zip')
localcopy    =  ADDON.getSetting('localcopy')
privatebuilds=  ADDON.getSetting('private')
reseller     =  ADDON.getSetting('reseller')
resellername =  ADDON.getSetting('resellername')
resellerid   =  ADDON.getSetting('resellerid')
mastercopy   =  ADDON.getSetting('mastercopy')
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
ADDONS       =  xbmc.translatePath(os.path.join('special://home','addons',''))
CBADDONPATH  =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'default.py'))
GUISETTINGS  =  os.path.join(USERDATA,'guisettings.xml')
GUI          =  xbmc.translatePath(os.path.join(USERDATA,'guisettings.xml'))
GUIFIX       =  xbmc.translatePath(os.path.join(USERDATA,'guifix.xml'))
INSTALL      =  xbmc.translatePath(os.path.join(USERDATA,'install.xml'))
FAVS         =  xbmc.translatePath(os.path.join(USERDATA,'favourites.xml'))
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
userdatafolder = xbmc.translatePath(os.path.join(ADDON_DATA,AddonID))
GUINEW       =  xbmc.translatePath(os.path.join(userdatafolder,'guinew.xml'))
guitemp      =  xbmc.translatePath(os.path.join(userdatafolder,'guitemp',''))
tempdbpath   =  xbmc.translatePath(os.path.join(USB,'Database'))
urlbase      =  'None'
FANART       =  xbmc.translatePath(os.path.join(ADDONS,AddonID,'fanart.jpg'))

#---------------------------------------------------------------------------------------------------
#Function to clean HTML into plain text. Not perfect but it's better than raw html code!
def Clean_HTML(data):        
    data = data.replace('</p><p>','[CR][CR]').replace('&ndash;','-').replace('&mdash;','-').replace("\n", " ").replace("\r", " ").replace("&rsquo;", "'").replace("&rdquo;", '"').replace("</a>", " ").replace("&hellip;", '...').replace("&lsquo;", "'").replace("&ldquo;", '"')
    data = " ".join(data.split())   
    p = re.compile(r'< script[^<>]*?>.*?< / script >')
    data = p.sub('', data)
    p = re.compile(r'< style[^<>]*?>.*?< / style >')
    data = p.sub('', data)
    p = re.compile(r'')
    data = p.sub('', data)
    p = re.compile(r'<[^<]*?>')
    data = p.sub('', data)
    data = data.replace('&nbsp;',' ')
    return data
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
#Function to populate the search based on the initial first filter
def Grab_Hardware(url):
    buildsURL = 'http://totalxbmc.com/totalrevolution/HardwarePortal/sortby.php?sortx=Added&orderx=DESC&%s' % (url)
    link = extras.Open_URL(buildsURL).replace('\n','').replace('\r','')
    match=re.compile('name="(.+?)" <br> id="(.+?)" <br> thumb="(.+?)" <br><br>', re.DOTALL).findall(link)
    extras.Sort_By(buildsURL,'hardware')
    for name, id, thumb in match:
        extras.addDir('folder2',name,id,'hardware_final_menu',thumb,'','')
#---------------------------------------------------------------------------------------------------
#Function to populate the news search
def Grab_News(url):
    buildsURL = 'http://totalxbmc.com/totalrevolution/LatestNews/sortby.php?sortx=item_date&orderx=DESC&%s' % (url)
    link = extras.Open_URL(buildsURL).replace('\n','').replace('\r','')
    match=re.compile('name="(.+?)" <br> date="(.+?)" <br> source="(.+?)" <br> id="(.+?)" <br><br>', re.DOTALL).findall(link)
    for name, date, source, id in match:
        if "OpenELEC" in source:
            extras.addDir('',name+'  ('+date+')',id,'news_menu','OpenELEC.png','','')
        if "Official" in source:
            extras.addDir('',name+'  ('+date+')',id,'news_menu','XBMC.png','','')
        if "Raspbmc" in source:
            extras.addDir('',name+'  ('+date+')',id,'news_menu','Raspbmc.png','','')
        if "XBMC4Xbox" in source:
            extras.addDir('',name+'  ('+date+')',id,'news_menu','XBMC4Xbox.png','','')
        if "TotalXBMC" in source:
            extras.addDir('',name+'  ('+date+')',id,'news_menu','TOTALXBMC.png','','')
#---------------------------------------------------------------------------------------------------
#Function to populate the search based on the initial first filter
def Grab_Tutorials(url):
    buildsURL = 'http://totalxbmc.com/totalrevolution/TutorialPortal/sortby.php?sortx=Name&orderx=ASC&%s' % (url)
    link = extras.Open_URL(buildsURL).replace('\n','').replace('\r','')
    match=re.compile('name="(.+?)" <br> about="(.+?)" <br> id="(.+?)" <br><br>', re.DOTALL).findall(link)
    extras.Sort_By(buildsURL,'tutorials')
    for name, about, id in match:
        extras.addDir('folder',name,id,'tutorial_final_menu','TotalXBMC_Guides.png','',about)
#---------------------------------------------------------------------------------------------------
# This creates the final menu showing build details, video and install link
def Hardware_Menu(url):
    BaseURL='http://totalxbmc.com/totalrevolution/HardwarePortal/hardwaredetails.php?id=%s' % (url)
    link = extras.Open_URL(BaseURL).replace('\n','').replace('\r','')
    namematch = re.compile('name="(.+?)"').findall(link)
    manufacturermatch = re.compile('manufacturer="(.+?)"').findall(link)
    videoguide1match = re.compile('video_guide1="(.+?)"').findall(link)
    videoguide2match = re.compile('video_guide2="(.+?)"').findall(link)
    videoguide3match = re.compile('video_guide3="(.+?)"').findall(link)
    videoguide4match = re.compile('video_guide4="(.+?)"').findall(link)
    videoguide5match = re.compile('video_guide5="(.+?)"').findall(link)
    videolabel1match = re.compile('video_label1="(.+?)"').findall(link)
    videolabel2match = re.compile('video_label2="(.+?)"').findall(link)
    videolabel3match = re.compile('video_label3="(.+?)"').findall(link)
    videolabel4match = re.compile('video_label4="(.+?)"').findall(link)
    videolabel5match = re.compile('video_label5="(.+?)"').findall(link)
    shopmatch = re.compile('shops="(.+?)"').findall(link)
    descmatch = re.compile('description="(.+?)"').findall(link)
    screenshot1match = re.compile('screenshot1="(.+?)"').findall(link)
    screenshot2match = re.compile('screenshot2="(.+?)"').findall(link)
    screenshot3match = re.compile('screenshot3="(.+?)"').findall(link)
    screenshot4match = re.compile('screenshot4="(.+?)"').findall(link)
    screenshot5match = re.compile('screenshot5="(.+?)"').findall(link)
    screenshot6match = re.compile('screenshot6="(.+?)"').findall(link)
    screenshot7match = re.compile('screenshot7="(.+?)"').findall(link)
    screenshot8match = re.compile('screenshot8="(.+?)"').findall(link)
    screenshot9match = re.compile('screenshot9="(.+?)"').findall(link)
    screenshot10match = re.compile('screenshot10="(.+?)"').findall(link)
    screenshot11match = re.compile('screenshot11="(.+?)"').findall(link)
    screenshot12match = re.compile('screenshot12="(.+?)"').findall(link)
    screenshot13match = re.compile('screenshot13="(.+?)"').findall(link)
    screenshot14match = re.compile('screenshot14="(.+?)"').findall(link)
    addedmatch = re.compile('added="(.+?)"').findall(link)
    platformmatch = re.compile('platform="(.+?)"').findall(link)
    chipsetmatch = re.compile('chipset="(.+?)"').findall(link)
    guidematch = re.compile('official_guide="(.+?)"').findall(link)
    previewmatch = re.compile('official_preview="(.+?)"').findall(link)
    thumbmatch = re.compile('thumbnail="(.+?)"').findall(link)
    stockmatch = re.compile('stock_rom="(.+?)"').findall(link)
    cpumatch = re.compile('CPU="(.+?)"').findall(link)
    gpumatch = re.compile('GPU="(.+?)"').findall(link)
    rammatch = re.compile('RAM="(.+?)"').findall(link)
    flashmatch = re.compile('flash="(.+?)"').findall(link)
    wifimatch = re.compile('wifi="(.+?)"').findall(link)
    bluetoothmatch = re.compile('bluetooth="(.+?)"').findall(link)
    lanmatch = re.compile('LAN="(.+?)"').findall(link)
    xbmcmatch = re.compile('xbmc_version="(.+?)"').findall(link)
    prosmatch = re.compile('pros="(.+?)"').findall(link)
    consmatch = re.compile('cons="(.+?)"').findall(link)
    librarymatch = re.compile('library_scan="(.+?)"').findall(link)
    fourkmatch = re.compile('4k="(.+?)"').findall(link)
    teneightymatch = re.compile('1080="(.+?)"').findall(link)
    seventwentymatch = re.compile('720="(.+?)"').findall(link)
    threedmatch = re.compile('3D="(.+?)"').findall(link)
    dtsmatch = re.compile('DTS="(.+?)"').findall(link)
    reviewmatch = re.compile('total_review="(.+?)"').findall(link)
    cbmatch = re.compile('CB_Premium="(.+?)"').findall(link)
   
    name  = namematch[0] if (len(namematch) > 0) else ''
    manufacturer  = manufacturermatch[0] if (len(manufacturermatch) > 0) else ''
    videoguide1  = videoguide1match[0] if (len(videoguide1match) > 0) else 'None'
    videoguide2  = videoguide2match[0] if (len(videoguide2match) > 0) else 'None'
    videoguide3  = videoguide3match[0] if (len(videoguide3match) > 0) else 'None'
    videoguide4  = videoguide4match[0] if (len(videoguide4match) > 0) else 'None'
    videoguide5  = videoguide5match[0] if (len(videoguide5match) > 0) else 'None'
    videolabel1  = videolabel1match[0] if (len(videolabel1match) > 0) else 'None'
    videolabel2  = videolabel2match[0] if (len(videolabel2match) > 0) else 'None'
    videolabel3  = videolabel3match[0] if (len(videolabel3match) > 0) else 'None'
    videolabel4  = videolabel4match[0] if (len(videolabel4match) > 0) else 'None'
    videolabel5  = videolabel5match[0] if (len(videolabel5match) > 0) else 'None'
    shop  = shopmatch[0] if (len(shopmatch) > 0) else ''    
    description = descmatch[0] if (len(descmatch) > 0) else ''
    screenshot1 = screenshot1match[0] if (len(screenshot1match) > 0) else ''
    screenshot2 = screenshot2match[0] if (len(screenshot2match) > 0) else ''
    screenshot3 = screenshot3match[0] if (len(screenshot3match) > 0) else ''
    screenshot4 = screenshot4match[0] if (len(screenshot4match) > 0) else ''
    screenshot5 = screenshot5match[0] if (len(screenshot5match) > 0) else ''
    screenshot6 = screenshot6match[0] if (len(screenshot6match) > 0) else ''
    screenshot7 = screenshot7match[0] if (len(screenshot7match) > 0) else ''
    screenshot8 = screenshot8match[0] if (len(screenshot8match) > 0) else ''
    screenshot9 = screenshot9match[0] if (len(screenshot9match) > 0) else ''
    screenshot10 = screenshot10match[0] if (len(screenshot10match) > 0) else ''
    screenshot11 = screenshot11match[0] if (len(screenshot11match) > 0) else ''
    screenshot12 = screenshot12match[0] if (len(screenshot12match) > 0) else ''
    screenshot13 = screenshot13match[0] if (len(screenshot13match) > 0) else ''
    screenshot14 = screenshot14match[0] if (len(screenshot14match) > 0) else ''
    added = addedmatch[0] if (len(addedmatch) > 0) else ''
    platform = platformmatch[0] if (len(platformmatch) > 0) else ''
    chipset = chipsetmatch[0] if (len(chipsetmatch) > 0) else ''
    guide = guidematch[0] if (len(guidematch) > 0) else ''
    preview = previewmatch[0] if (len(previewmatch) > 0) else ''
    thumb = thumbmatch[0] if (len(thumbmatch) > 0) else ''
    stock = stockmatch[0] if (len(stockmatch) > 0) else ''
    CPU = cpumatch[0] if (len(cpumatch) > 0) else ''
    GPU = gpumatch[0] if (len(gpumatch) > 0) else ''
    RAM = rammatch[0] if (len(rammatch) > 0) else ''
    flash = flashmatch[0] if (len(flashmatch) > 0) else ''
    wifi = wifimatch[0] if (len(wifimatch) > 0) else ''
    bluetooth = bluetoothmatch[0] if (len(bluetoothmatch) > 0) else ''
    LAN = lanmatch[0] if (len(lanmatch) > 0) else ''
    xbmc_version = xbmcmatch[0] if (len(xbmcmatch) > 0) else ''
    pros = prosmatch[0] if (len(prosmatch) > 0) else ''
    cons = consmatch[0] if (len(consmatch) > 0) else ''
    library = librarymatch[0] if (len(librarymatch) > 0) else ''
    fourk = fourkmatch[0] if (len(fourkmatch) > 0) else ''
    teneighty = teneightymatch[0] if (len(teneightymatch) > 0) else ''
    seventwenty = seventwentymatch[0] if (len(seventwentymatch) > 0) else ''
    threed = threedmatch[0] if (len(threedmatch) > 0) else ''
    DTS = dtsmatch[0] if (len(dtsmatch) > 0) else ''
    review = reviewmatch[0] if (len(reviewmatch) > 0) else ''
    cb = cbmatch[0] if (len(cbmatch) > 0) else ''
    official_description = str('[COLOR=gold]Available From: [/COLOR]'+shop+' @ [COLOR=lime]www.totalboxshop.tv[/COLOR][CR][CR][COLOR=dodgerblue]Added: [/COLOR]'+added+'[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]'+manufacturer+'[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]'+platform+'[CR][COLOR=dodgerblue]Chipset: [/COLOR]'+chipset+'[CR][COLOR=dodgerblue]CPU: [/COLOR]'+CPU+'[CR][COLOR=dodgerblue]GPU: [/COLOR]'+GPU+'[CR][COLOR=dodgerblue]RAM: [/COLOR]'+RAM+'[CR][COLOR=dodgerblue]Flash: [/COLOR]'+flash+'[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]'+wifi+'[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]'+bluetooth+'[CR][COLOR=dodgerblue]LAN: [/COLOR]'+LAN+'[CR][CR][COLOR=yellow]About: [/COLOR]'+description)
    official_description2 = str('[COLOR=gold]Availability: [/COLOR]Sorry this device is currently unavailable at [COLOR=lime]www.totalboxshop.tv[/COLOR][CR][CR][COLOR=dodgerblue]Added: [/COLOR]'+added+'[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]'+manufacturer+'[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]'+platform+'[CR][COLOR=dodgerblue]Chipset: [/COLOR]'+chipset+'[CR][COLOR=dodgerblue]CPU: [/COLOR]'+CPU+'[CR][COLOR=dodgerblue]GPU: [/COLOR]'+GPU+'[CR][COLOR=dodgerblue]RAM: [/COLOR]'+RAM+'[CR][COLOR=dodgerblue]Flash: [/COLOR]'+flash+'[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]'+wifi+'[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]'+bluetooth+'[CR][COLOR=dodgerblue]LAN: [/COLOR]'+LAN+'[CR][CR][COLOR=yellow]About: [/COLOR]'+description)
    total_review = str('[COLOR=gold]Available From: [/COLOR]'+shop+' @ [COLOR=lime]www.totalboxshop.tv[/COLOR][CR][CR][COLOR=dodgerblue]Added: [/COLOR]'+added+'[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]'+manufacturer+'[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]'+platform+'[CR][COLOR=dodgerblue]Chipset: [/COLOR]'+chipset+'[CR][COLOR=dodgerblue]CPU: [/COLOR]'+CPU+'[CR][COLOR=dodgerblue]GPU: [/COLOR]'+GPU+'[CR][COLOR=dodgerblue]RAM: [/COLOR]'+RAM+'[CR][COLOR=dodgerblue]Flash: [/COLOR]'+flash+'[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]'+wifi+'[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]'+bluetooth+'[CR][COLOR=dodgerblue]LAN: [/COLOR]'+LAN+'[CR][CR][COLOR=yellow]About: [/COLOR]'+review+'[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    '+pros+'[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  '+cons+'[CR][CR][COLOR=gold]4k Playback:[/COLOR]  '+fourk+'[CR][CR][COLOR=gold]1080p Playback:[/COLOR]  '+teneighty+'[CR][CR][COLOR=gold]720p Playback:[/COLOR]  '+seventwenty+'[CR][CR][COLOR=gold]DTS Compatibility:[/COLOR]  '+DTS+'[CR][CR][COLOR=gold]Time taken to scan 100 movies:[/COLOR]  '+library)
    total_review2 = str('[COLOR=gold]Availability: [/COLOR]Sorry this device is currently unavailable at [COLOR=lime]www.totalboxshop.tv[/COLOR][CR][CR][COLOR=dodgerblue]Added: [/COLOR]'+added+'[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]'+manufacturer+'[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]'+platform+'[CR][COLOR=dodgerblue]Chipset: [/COLOR]'+chipset+'[CR][COLOR=dodgerblue]CPU: [/COLOR]'+CPU+'[CR][COLOR=dodgerblue]GPU: [/COLOR]'+GPU+'[CR][COLOR=dodgerblue]RAM: [/COLOR]'+RAM+'[CR][COLOR=dodgerblue]Flash: [/COLOR]'+flash+'[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]'+wifi+'[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]'+bluetooth+'[CR][COLOR=dodgerblue]LAN: [/COLOR]'+LAN+'[CR][CR][COLOR=yellow]About: [/COLOR]'+review+'[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    '+pros+'[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  '+cons+'[CR][CR][COLOR=gold]4k Playback:[/COLOR]  '+fourk+'[CR][CR][COLOR=gold]1080p Playback:[/COLOR]  '+teneighty+'[CR][CR][COLOR=gold]720p Playback:[/COLOR]  '+seventwenty+'[CR][CR][COLOR=gold]DTS Compatibility:[/COLOR]  '+DTS+'[CR][CR][COLOR=gold]Time taken to scan 100 movies:[/COLOR]  '+library)
    if description != '' and shop !='':
        extras.addDir('','[COLOR=yellow][Text Guide][/COLOR]  Official Description',official_description,'text_guide','TotalXBMC_Guides.png',FANART,'','')    
    if description != '' and shop =='':
        extras.addDir('','[COLOR=yellow][Text Guide][/COLOR]  Official Description',official_description2,'text_guide','TotalXBMC_Guides.png',FANART,'','')    
    if review != '' and shop !='':
        extras.addDir('','[COLOR=yellow][Text Guide][/COLOR]  TotalXBMC Review',total_review,'text_guide','TotalXBMC_Guides.png',FANART,'','')    
    if review != '' and shop =='':
        extras.addDir('','[COLOR=yellow][Text Guide][/COLOR]  TotalXBMC Review',total_review2,'text_guide','TotalXBMC_Guides.png',FANART,'','')    
    if preview != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]   Official Video Preview',preview,'play_video','Video_Guide.png',FANART,'','')    
    if guide != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]   Official Video Guide',guide,'play_video','Video_Guide.png',FANART,'','')    
    if videoguide1 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel1,videoguide1,'play_video','Video_Guide.png',FANART,'','')    
    if videoguide2 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel2,videoguide2,'play_video','Video_Guide.png',FANART,'','')    
    if videoguide3 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel3,videoguide3,'play_video','Video_Guide.png',FANART,'','')    
    if videoguide4 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel4,videoguide4,'play_video','Video_Guide.png',FANART,'','')    
    if videoguide5 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel5,videoguide5,'play_video','Video_Guide.png',FANART,'','')    
#---------------------------------------------------------------------------------------------------
#Search in description
def Manual_Search():
    extras.addDir('folder','Search By Name','name','search_builds','Manual_Search.png','','','')
    extras.addDir('folder','Search By Uploader','author','search_builds','Search_Genre.png','','','')
    extras.addDir('folder','Search By Audio Addons Installed','audio','search_builds','Search_Addons.png','','','')
    extras.addDir('folder','Search By Picture Addons Installed','pics','search_builds','Search_Addons.png','','','')
    extras.addDir('folder','Search By Program Addons Installed','progs','search_builds','Search_Addons.png','','','')
    extras.addDir('folder','Search By Video Addons Installed','vids','search_builds','Search_Addons.png','','','')
    extras.addDir('folder','Search By Skins Installed','skins','search_builds','Search_Addons.png','','','')
#---------------------------------------------------------------------------------------------------
# This creates the final menu showing build details, video and install link
def News_Menu(url):
    BaseURL='http://totalxbmc.com/totalrevolution/LatestNews/LatestNews.php?id=%s' % (url)
    link = extras.Open_URL(BaseURL).replace('\n','').replace('\r','')
    namematch = re.compile('name="(.+?)"').findall(link)
    authormatch = re.compile('author="(.+?)"').findall(link)
    datematch = re.compile('date="(.+?)"').findall(link)
    contentmatch = re.compile('content="(.+?)###END###"').findall(link)
   
    name  = namematch[0] if (len(namematch) > 0) else ''
    author  = authormatch[0] if (len(authormatch) > 0) else ''
    date = datematch[0] if (len(datematch) > 0) else ''
    content = contentmatch[0] if (len(contentmatch) > 0) else ''
    clean_text = Clean_HTML(content)
    description = str('[COLOR=gold]Source: [/COLOR]'+author+'     [COLOR=gold]Date: [/COLOR]'+date+'[CR][CR][COLOR=lime]Details: [/COLOR][CR]'+clean_text)
    extras.Text_Boxes(name,description)
#---------------------------------------------------------------------------------------------------
#Show full description of build
def Text_Guide(name,url):
    extras.Text_Boxes(name,url)
#---------------------------------------------------------------------------------------------------
# This creates the final menu showing build details, video and install link
def Tutorial_Menu(url):
    incremental = 'http://totalxbmc.com/totalrevolution/TutorialPortal/downloadcount.php?id=%s' % (url)
    extras.Open_URL(incremental)
    BaseURL='http://totalxbmc.com/totalrevolution/TutorialPortal/tutorialdetails.php?id=%s' % (url)
    link = extras.Open_URL(BaseURL).replace('\n','').replace('\r','')
    namematch = re.compile('name="(.+?)"').findall(link)
    authormatch = re.compile('author="(.+?)"').findall(link)
    videoguide1match = re.compile('video_guide1="(.+?)"').findall(link)
    videoguide2match = re.compile('video_guide2="(.+?)"').findall(link)
    videoguide3match = re.compile('video_guide3="(.+?)"').findall(link)
    videoguide4match = re.compile('video_guide4="(.+?)"').findall(link)
    videoguide5match = re.compile('video_guide5="(.+?)"').findall(link)
    videolabel1match = re.compile('video_label1="(.+?)"').findall(link)
    videolabel2match = re.compile('video_label2="(.+?)"').findall(link)
    videolabel3match = re.compile('video_label3="(.+?)"').findall(link)
    videolabel4match = re.compile('video_label4="(.+?)"').findall(link)
    videolabel5match = re.compile('video_label5="(.+?)"').findall(link)
    aboutmatch = re.compile('about="(.+?)"').findall(link)
    step1match = re.compile('step1="(.+?)"').findall(link)
    step2match = re.compile('step2="(.+?)"').findall(link)
    step3match = re.compile('step3="(.+?)"').findall(link)
    step4match = re.compile('step4="(.+?)"').findall(link)
    step5match = re.compile('step5="(.+?)"').findall(link)
    step6match = re.compile('step6="(.+?)"').findall(link)
    step7match = re.compile('step7="(.+?)"').findall(link)
    step8match = re.compile('step8="(.+?)"').findall(link)
    step9match = re.compile('step9="(.+?)"').findall(link)
    step10match = re.compile('step10="(.+?)"').findall(link)
    step11match = re.compile('step11="(.+?)"').findall(link)
    step12match = re.compile('step12="(.+?)"').findall(link)
    step13match = re.compile('step13="(.+?)"').findall(link)
    step14match = re.compile('step14="(.+?)"').findall(link)
    step15match = re.compile('step15="(.+?)"').findall(link)
    screenshot1match = re.compile('screenshot1="(.+?)"').findall(link)
    screenshot2match = re.compile('screenshot2="(.+?)"').findall(link)
    screenshot3match = re.compile('screenshot3="(.+?)"').findall(link)
    screenshot4match = re.compile('screenshot4="(.+?)"').findall(link)
    screenshot5match = re.compile('screenshot5="(.+?)"').findall(link)
    screenshot6match = re.compile('screenshot6="(.+?)"').findall(link)
    screenshot7match = re.compile('screenshot7="(.+?)"').findall(link)
    screenshot8match = re.compile('screenshot8="(.+?)"').findall(link)
    screenshot9match = re.compile('screenshot9="(.+?)"').findall(link)
    screenshot10match = re.compile('screenshot10="(.+?)"').findall(link)
    screenshot11match = re.compile('screenshot11="(.+?)"').findall(link)
    screenshot12match = re.compile('screenshot12="(.+?)"').findall(link)
    screenshot13match = re.compile('screenshot13="(.+?)"').findall(link)
    screenshot14match = re.compile('screenshot14="(.+?)"').findall(link)
    screenshot15match = re.compile('screenshot15="(.+?)"').findall(link)
   
    name  = namematch[0] if (len(namematch) > 0) else ''
    author  = authormatch[0] if (len(authormatch) > 0) else ''
    videoguide1  = videoguide1match[0] if (len(videoguide1match) > 0) else 'None'
    videoguide2  = videoguide2match[0] if (len(videoguide2match) > 0) else 'None'
    videoguide3  = videoguide3match[0] if (len(videoguide3match) > 0) else 'None'
    videoguide4  = videoguide4match[0] if (len(videoguide4match) > 0) else 'None'
    videoguide5  = videoguide5match[0] if (len(videoguide5match) > 0) else 'None'
    videolabel1  = videolabel1match[0] if (len(videolabel1match) > 0) else 'None'
    videolabel2  = videolabel2match[0] if (len(videolabel2match) > 0) else 'None'
    videolabel3  = videolabel3match[0] if (len(videolabel3match) > 0) else 'None'
    videolabel4  = videolabel4match[0] if (len(videolabel4match) > 0) else 'None'
    videolabel5  = videolabel5match[0] if (len(videolabel5match) > 0) else 'None'
    about  = aboutmatch[0] if (len(aboutmatch) > 0) else ''
    step1 = '[CR][CR][COLOR=dodgerblue]Step 1:[/COLOR][CR]'+step1match[0] if (len(step1match) > 0) else ''
    step2 = '[CR][CR][COLOR=dodgerblue]Step 2:[/COLOR][CR]'+step2match[0] if (len(step2match) > 0) else ''
    step3 = '[CR][CR][COLOR=dodgerblue]Step 3:[/COLOR][CR]'+step3match[0] if (len(step3match) > 0) else ''
    step4 = '[CR][CR][COLOR=dodgerblue]Step 4:[/COLOR][CR]'+step4match[0] if (len(step4match) > 0) else ''
    step5 = '[CR][CR][COLOR=dodgerblue]Step 5:[/COLOR][CR]'+step5match[0] if (len(step5match) > 0) else ''
    step6 = '[CR][CR][COLOR=dodgerblue]Step 6:[/COLOR][CR]'+step6match[0] if (len(step6match) > 0) else ''
    step7 = '[CR][CR][COLOR=dodgerblue]Step 7:[/COLOR][CR]'+step7match[0] if (len(step7match) > 0) else ''
    step8 = '[CR][CR][COLOR=dodgerblue]Step 8:[/COLOR][CR]'+step8match[0] if (len(step8match) > 0) else ''
    step9 = '[CR][CR][COLOR=dodgerblue]Step 9:[/COLOR][CR]'+step9match[0] if (len(step9match) > 0) else ''
    step10 = '[CR][CR][COLOR=dodgerblue]Step 10:[/COLOR][CR]'+step10match[0] if (len(step10match) > 0) else ''
    step11 = '[CR][CR][COLOR=dodgerblue]Step 11:[/COLOR][CR]'+step11match[0] if (len(step11match) > 0) else ''
    step12 = '[CR][CR][COLOR=dodgerblue]Step 12:[/COLOR][CR]'+step12match[0] if (len(step12match) > 0) else ''
    step13 = '[CR][CR][COLOR=dodgerblue]Step 13:[/COLOR][CR]'+step13match[0] if (len(step13match) > 0) else ''
    step14 = '[CR][CR][COLOR=dodgerblue]Step 14:[/COLOR][CR]'+step14match[0] if (len(step14match) > 0) else ''
    step15 = '[CR][CR][COLOR=dodgerblue]Step 15:[/COLOR][CR]'+step15match[0] if (len(step15match) > 0) else ''
    screenshot1 = screenshot1match[0] if (len(screenshot1match) > 0) else ''
    screenshot2 = screenshot2match[0] if (len(screenshot2match) > 0) else ''
    screenshot3 = screenshot3match[0] if (len(screenshot3match) > 0) else ''
    screenshot4 = screenshot4match[0] if (len(screenshot4match) > 0) else ''
    screenshot5 = screenshot5match[0] if (len(screenshot5match) > 0) else ''
    screenshot6 = screenshot6match[0] if (len(screenshot6match) > 0) else ''
    screenshot7 = screenshot7match[0] if (len(screenshot7match) > 0) else ''
    screenshot8 = screenshot8match[0] if (len(screenshot8match) > 0) else ''
    screenshot9 = screenshot9match[0] if (len(screenshot9match) > 0) else ''
    screenshot10 = screenshot10match[0] if (len(screenshot10match) > 0) else ''
    screenshot11 = screenshot11match[0] if (len(screenshot11match) > 0) else ''
    screenshot12 = screenshot12match[0] if (len(screenshot12match) > 0) else ''
    screenshot13 = screenshot13match[0] if (len(screenshot13match) > 0) else ''
    screenshot14 = screenshot14match[0] if (len(screenshot14match) > 0) else ''
    screenshot15 = screenshot15match[0] if (len(screenshot15match) > 0) else ''
    description = str('[COLOR=gold]Author: [/COLOR]'+author+'[CR][CR][COLOR=lime]About: [/COLOR]'+about+step1+step2+step3+step4+step5+step6+step7+step8+step9+step10+step11+step12+step13+step14+step15)
    if step1 != '':
        extras.addDir('','[COLOR=yellow][Text Guide][/COLOR]  '+name,description,'text_guide','How_To.png',FANART,about,'')    
    if videoguide1 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel1,videoguide1,'play_video','Video_Guide.png',FANART,'','')    
    if videoguide2 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel2,videoguide2,'play_video','Video_Guide.png',FANART,'','')    
    if videoguide3 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel3,videoguide3,'play_video','Video_Guide.png',FANART,'','')    
    if videoguide4 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel4,videoguide4,'play_video','Video_Guide.png',FANART,'','')    
    if videoguide5 != 'None':
        extras.addDir('','[COLOR=lime][VIDEO][/COLOR]  '+videolabel5,videoguide5,'play_video','Video_Guide.png',FANART,'','')    
#-----------------------------------------------------------------------------------------------------------------
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