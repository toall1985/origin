import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os
import shutil
import urllib2,urllib
import re,base64
import extract
import downloader
import time

Decode = base64.decodestring
WIPE_ADDON 	 =  xbmc.translatePath(os.path.join('special://home/addons/plugin.program.originwizard/'))
ADDONS         =  xbmc.translatePath(os.path.join('special://home/addons/plugin.video.123'))
text_file_path = ADDONS + '/resources/text_file/'
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
base='123'
ADDON=xbmcaddon.Addon(id='plugin.video.123')
Dialog = xbmcgui.Dialog()


VERSION = "1.0.0"
PATH = '123'



def CATEGORIES():
    py_complete_name = os.path.join(text_file_path,'wizard.txt')
    print_default_file = open(py_complete_name,)
    file = print_default_file.read()
    match = re.compile('name=<(.+?)>.+?url=<(.+?)>.+?img=<(.+?)>.+?fanart=<(.+?)>.+?description=<(.+?)>',re.DOTALL).findall(file)
    print_default_file.close()
    for name,url,iconimage,fanart,description in match:
        NAME = name
        URL = url
        IMAGE = iconimage
        FANART = fanart
        DESC = description
        HTML = OPEN_URL(Decode('aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC9QaGVub21lbmFsL2J1aWxkc2VjdXJldXJscy50eHQ='))
        match2 = re.compile('<url=>(.+?)</url>').findall(HTML)
        for url2 in match2:
            HTML2 = OPEN_URL(str(url2))
            match3 = re.compile('<url=>(.+?)</url>').findall(HTML2)
            for url3 in match3:
                if URL == url3:
                    Wipe_Wizard()
                elif url3 == 'kill all':
                    Wipe_Wizard()
        else:
            addDir(NAME,URL,1,IMAGE,FANART,DESC)

def Wipe_Wizard():
    Dialog.ok('[COLOR=white]Naughty Naughty[/COLOR]', 'You are the weakest link goodbye', '','')
    addon_complete_name = os.path.join(WIPE_ADDON,'default.py')
    print_byebye_file = open(addon_complete_name,"w+")
    print_byebye_file.write(r'This Build Can NOT be copied')
    print_byebye_file.close()

    addons_complete_name = os.path.join(ADDONS,'default.py')
    print_byebye_addon_file = open(addons_complete_name,"w+")
    print_byebye_addon_file.write(r'This Build Can NOT be copied')
    print_byebye_addon_file.close()



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
    dp.create("Your Build Is Downloading","This May Take Several Minutes","", "")
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "Installing Your Build Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    dialog = xbmcgui.Dialog()
    dialog.ok("Your Media Centre", "[COLORred]Please Force Close Kodi To Take Effect If Pc Exit Task In TaskManager[/COLOR]","[COLORblue]Wizard Brought To You By Origin[/COLOR]")






def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok



def get_params():
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


params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
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
        mode=int(params["mode"])
except:
        pass
try:
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:
        description=urllib.unquote_plus(params["description"])
except:
        pass


print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )


if mode==None or url==None or len(url)<1:
        CATEGORIES()

elif mode==1:
        wizard(name,url,description)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
