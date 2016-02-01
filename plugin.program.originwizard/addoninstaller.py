import re,os.path, xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys,zipfile,time,urllib,urllib2,extras,downloader,extract

ADDON        =  xbmcaddon.Addon(id='plugin.program.originwizard')
zip 		 =  ADDON.getSetting('zip')
Addons_path  = xbmc.translatePath(os.path.join('special://home/addons/plugin.program.originwizard/Generated/'))
Generated 	 = 'TEST'
Folders_path = Addons_path + Generated
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
        extras.addDir('folder','NEXT PAGE',url, 'Addon','','','','')
    match = re.compile('<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>').findall(HTML)
    for url,img,name in match:
        extras.addDir('',name,url, 'Addon_Extract','https://addons.tvaddons.ag/'+img,'','','')


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
			

