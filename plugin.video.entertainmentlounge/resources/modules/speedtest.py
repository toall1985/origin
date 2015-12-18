# This code is licensed under The GNU General Public License version 2 (GPLv2)
# If you decide to fork this code please obey by the licensing rules.
#
#Thanks go to the-one who created the initial speedtest code for me in early 2014
#That code broke but it didn't take too much to fix it, if you get problems it's most likely
#down to the fact that you need to use another download link that plays nicely with XBMC/Kodi

import xbmc, xbmcplugin
import xbmcgui
import xbmcaddon
import urllib
import time
import os
import sys

ADDON_ID   = 'plugin.video.entertainmentlounge'
ADDON      =  xbmcaddon.Addon(id=ADDON_ID)
HOME       =  ADDON.getAddonInfo('path')
ARTPATH    =  xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
FANART     =  xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))
addon_name="Speed Test"

max_Bps = 0.0
currently_downloaded_bytes = 0.0

#-----------------------------------------------------------------------------------------------------------------
def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("Speed Test","Testing your internet speed...",' ', ' ')
    dp.update(0)
    start_time=time.time()
    
    try:
        urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
    except:
        pass
    
    # return time taken
    return ( time.time() - start_time )
     
#-----------------------------------------------------------------------------------------------------------------
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        
        global max_Bps
        global currently_downloaded_bytes
        
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded_bytes = float(numblocks) * blocksize
            currently_downloaded = currently_downloaded_bytes / (1024 * 1024) 
            Bps_speed = currently_downloaded_bytes / (time.time() - start_time) 
            if Bps_speed > 0:                                                 
                eta = (filesize - numblocks * blocksize) / Bps_speed 
                if Bps_speed > max_Bps: max_Bps = Bps_speed
            else: 
                eta = 0 
            kbps_speed = Bps_speed * 8 / 1024 
            mbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Mb/s ' % mbps_speed
            e += 'ETA: %02d:%02d' % divmod(eta, 60) 
            dp.update(percent, mbs, e)
        except: 
            currently_downloaded_bytes = float(filesize)
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 
            raise Exception("Cancelled")     

#-----------------------------------------------------------------------------------------------------------------
def make_dir(mypath, dirname):
    ''' Creates sub-directories if they are not found. '''
    import xbmcvfs
    
    if not xbmcvfs.exists(mypath): 
        try:
            xbmcvfs.mkdirs(mypath)
        except:
            xbmcvfs.mkdir(mypath)
    
    subpath = os.path.join(mypath, dirname)
    
    if not xbmcvfs.exists(subpath): 
        try:
            xbmcvfs.mkdirs(subpath)
        except:
            xbmcvfs.mkdir(subpath)
            
    return subpath
    
#-----------------------------------------------------------------------------------------------------------------
def GetEpochStr():
    import datetime
    time_now=datetime.datetime.now()
    
    import time
    epoch=time.mktime(time_now.timetuple())+(time_now.microsecond/1000000.)
    
    epoch_str = str('%f' % epoch)
    epoch_str = epoch_str.replace('.','')
    epoch_str = epoch_str[:-3]

    return epoch_str

#-----------------------------------------------------------------------------------------------------------------
def addDir(name, url, mode, iconimage = ''): 
    if len(iconimage) > 0:
        iconimage = ARTPATH + iconimage
    else:
        iconimage = 'DefaultFolder.png'
    u  = sys.argv[0]
    u += "?url="  + urllib.quote_plus(url)
    u += "&name=" + urllib.quote_plus(name)
    u += "&mode=" + str(mode)

    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty("Fanart_Image", FANART )    
    addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)

#-----------------------------------------------------------------------------------------------------------------  
def addDirectoryItem(handle, url, listitem, isFolder):
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder)
    
#-----------------------------------------------------------------------------------------------------------------
def menu():
    addDir('[COLOR=blue]Instructions - Read Me First[/COLOR]', 'none', 'instructions', 'DownloadInstructions.png')
    addDir('Download 16MB Test File   - [COLOR=blue]Server 1[/COLOR]', 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/16MB.txt', 'runtest', 'Download16.png')
    addDir('Download 32MB Test File   - [COLOR=blue]Server 1[/COLOR]', 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/32MB.txt', 'runtest', 'Download32.png')
    addDir('Download 64MB Test File   - [COLOR=blue]Server 1[/COLOR]', 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/64MB.txt', 'runtest', 'Download64.png')
    addDir('Download 128MB Test File - [COLOR=blue]Server 1[/COLOR]', 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/128MB.txt', 'runtest', 'Download128.png')
    addDir('Download 10MB Test File   - [COLOR=green]Server 2[/COLOR]', 'http://www.wswd.net/testdownloadfiles/10MB.zip', 'runtest', 'Download10.png')

#-----------------------------------------------------------------------------------------------------------------
def runtest(url):
    addon_profile_path = xbmc.translatePath(ADDON.getAddonInfo('profile'))
    speed_test_files_dir = make_dir(addon_profile_path, 'speedtestfiles')
    speed_test_download_file = os.path.join(speed_test_files_dir, GetEpochStr() + '.speedtest')
    timetaken = download(url, speed_test_download_file)
    os.remove(speed_test_download_file)
    avgspeed = ((currently_downloaded_bytes / timetaken) * 8 / ( 1024 * 1024 ))
    maxspeed = (max_Bps * 8/(1024*1024))
    if avgspeed < 2:
        livestreams = 'Very low quality streams may work'
        onlinevids = 'Expect buffering, do not try HD'
    elif avgspeed < 2.5:
        livestreams = 'You should be ok for SD content only'
        onlinevids = 'SD/DVD quality should be ok, do not try HD'
    elif avgspeed < 5:
        livestreams = 'Some HD streams may struggle, SD will be fine'
        onlinevids = 'Most will be fine, some Blurays may struggle'
    elif avgspeed < 10:
        livestreams = 'All streams including HD should stream fine'
        onlinevids = 'Most will be fine, some Blurays may struggle'
    else:
        livestreams = 'All streams including HD should stream fine'
        onlinevids = 'You can play all files with no problems'
    print "Average Speed: " + str(avgspeed)
    print "Max. Speed: " + str(maxspeed)
    dialog = xbmcgui.Dialog()
    ok = dialog.ok('Speed Test - Results',
#    '[COLOR blue]Duration:[/COLOR] %.02f secs' % timetaken,
    '[COLOR blue]Average Speed:[/COLOR] %.02f Mb/s ' % avgspeed,
    '[COLOR blue]Live Streams:[/COLOR] ' + livestreams,
    '[COLOR blue]Online Video:[/COLOR] ' + onlinevids,
#    '[COLOR blue]Maximum Speed:[/COLOR] %.02f Mb/s ' % maxspeed,
    )
    
#-----------------------------------------------------------------------------------------------------------------
def instructions():
    TextBoxes('Speed Test Instructions', '[COLOR=blue][B]What file should I use: [/B][/COLOR][CR]This function will download a file and will work out your speed based on how long it took to download. You will then be notified of '
    'what quality streams you can expect to stream without buffering. You can choose to download a 10MB, 16MB, 32MB, 64MB or 128MB file to use with the test. Using the larger files will give you a better '
    'indication of how reliable your speeds are but obviously if you have a limited amount of bandwidth allowance you may want to opt for a smaller file.'
    '[CR][CR][COLOR=blue][B]How accurate is this speed test:[/B][/COLOR][CR]Not very accurate at all! As this test is based on downloading a file from a server it\'s reliant on the server not having a go-slow day '
    'but the servers used should be pretty reliable. The 10MB file is hosted on a different server to the others so if you\'re not getting the results expected please try another file. If you have a fast fiber '
    'connection the chances are your speed will show as considerably slower than your real download speed due to the server not being able to send the file as fast as your download speed allows. Essentially the '
    'test results will be limited by the speed of the server but you will at least be able to see if it\'s your connection that\'s causing buffering or if it\'s the host you\'re trying to stream from'
    '[CR][CR][COLOR=blue][B]What is the differnce between Live Streams and Online Video:[/COLOR][/B][CR]When you run the test you\'ll see results based on your speeds and these let you know the quality you should expect to '
    'be able stream with your connection. Live Streams as the title suggests are like traditional TV channels, they are being streamed live so for example if you wanted to watch CNN this would fall into this category. '
    'Online Videos relates to movies, tv shows, youtube clips etc. Basically anything that isn\'t live - if you\'re new to the world of streaming then think of it as On Demand content, this is content that\'s been recorded and stored on the web.'
    '[CR][CR][COLOR=blue][B]Why am I still getting buffering:[/COLOR][/B][CR]The results you get from this test are strictly based on your download speed, there are many other factors that can cause buffering and contrary to popular belief '
    'having a massively fast internet connection will not make any difference to your buffering issues if the server you\'re trying to get the content from is unable to send it fast enough. This can often happen and is usually '
    'down to heavy traffic (too many users accessing the same server). A 10 Mb/s connection should be plenty fast enough for almost all content as it\'s very rare a server can send it any quicker than that.'
    '[CR][CR][COLOR=blue][B]What\'s the difference between MB/s and Mb/s:[/COLOR][/B][CR]A lot of people think the speed they see advertised by their ISP is Megabytes (MB/S) per second - this is not true. Speeds are usually shown as Mb/s '
    'which is Megabit per second - there are 8 of these to a megabyte so if you want to work out how many megabytes per second you\'re getting you need to divide the speed by 8. It may sound sneaky but really it\'s just the unit that has always been used.'
    )
#-----------------------------------------------------------------------------------------------------------------
def TextBoxes(heading,anounce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(anounce); text=f.read()
      except: text=anounce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()  

#---------------------------------------------------------------------------------------------------
def get_params():    
    if len(sys.argv[2]) < 2:
        return []

    param = []

    params        = sys.argv[2]
    cleanedparams = params.replace('?','')

    if (params[len(params)-1] == '/'):
        params = params[0:len(params)-2]

    pairsofparams = cleanedparams.split('&')
    param         = {}

    for i in range(len(pairsofparams)):
        splitparams = {}
        splitparams = pairsofparams[i].split('=')

        if (len(splitparams)) == 2:
            param[splitparams[0]] = splitparams[1]

    return param

params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
fanart=None

try:    mode = urllib.unquote_plus(params['mode'])
except: mode = None

try:    url = urllib.unquote_plus(params['url'])
except: url = ''

try:    name = urllib.unquote_plus(params['name'])
except: name = ''

try:    iconimage=urllib.unquote_plus(params["iconimage"])
except: pass

try:    description=urllib.unquote_plus(params["description"])
except: pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass

if mode == 'runtest'              : runtest(url)
elif mode == 'instructions'       : instructions()
