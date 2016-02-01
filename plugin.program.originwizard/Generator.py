import re,os.path, xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys,zipfile,time



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
        if self.action == 'newWizard':
            self.Wizard_Inputs()
        elif self.action == 'textFile':
            self.txt_file_inputs()
        else: pass
         	
		
    def Wizard_Inputs(self):
        Check_Download_Path()
        self.plugin_name = Dialog.input('[COLOR red]Input Name of Wizard[/COLOR]', type=xbmcgui.INPUT_ALPHANUM) 
        self.Wizard_name = self.plugin_name.lower()
        self.clean_plugin_name = (self.Wizard_name).replace(' ','')
        self.build_url =Dialog.input('[COLOR red]Input Online Txt File full URL - include http:[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
		
        self.generate_wizard_py(self)
	
	
	
    def txt_file_inputs(self):
        Check_Download_Path()
        self.build_name = Dialog.input('[COLOR red] Input Build Name[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.build_zip = Dialog.input('[COLOR red] Input Builds Online Zip Url[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.build_image = Dialog.input('[COLOR red] Input Builds Online Image Url[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.build_fanart = Dialog.input('[COLOR red] Input Builds Online Background Image[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.build_description = Dialog.input('[COLOR red] Input Builds Description[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
	
        self.generate_wizard_text()
		
    def generate_wizard_text(self):

        txt_complete_name = os.path.join(zip,self.txt_file_name)
        print_text_file = open(txt_complete_name,"w+")

        print_text_file.write(r'name=<' + self.build_name + '>\n')
        print_text_file.write(r'url=<' + self.build_zip + '>\n')
        print_text_file.write(r'img=<' + self.build_image + '>\n')
        print_text_file.write(r'fanart=<' + self.build_fanart + '>\n')
        print_text_file.write(r'description=<' + self.build_description + '>\n')
        print_text_file.close()
        choice = xbmcgui.Dialog().yesno("Is There Any More Builds?", 'Would You like to add another build into txt file?', '', 'This Will also show in your wizard when generated', yeslabel='Yes',nolabel='No')
        if choice == 1:
            self.txt_extra_file_inputs()
        elif choice ==0:
            Dialog.ok("[COLOR=white]Origin[/COLOR]", "Your Text File is now Created", '','')
	
    def txt_extra_file_inputs(self):
        Check_Download_Path()
        self.extra_build_name = Dialog.input('[COLOR red] Input Build Name[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.extra_build_zip = Dialog.input('[COLOR red] Input Builds Online Zip Url[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.extra_build_image = Dialog.input('[COLOR red] Input Builds Online Image Url[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.extra_build_fanart = Dialog.input('[COLOR red] Input Builds Online Background Image[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        self.extra_build_description = Dialog.input('[COLOR red] Input Builds Description[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
	
        self.extra_generate_wizard_text()	

    def extra_generate_wizard_text(self):

        txt_extra_complete_name = os.path.join(zip,self.txt_file_name)
        print_extra_text_file = open(txt_extra_complete_name,"a")

        print_extra_text_file.write(r'name=<' + self.extra_build_name + '>\n')
        print_extra_text_file.write(r'url=<' + self.extra_build_zip + '>\n')
        print_extra_text_file.write(r'img=<' + self.extra_build_image + '>\n')
        print_extra_text_file.write(r'fanart=<' + self.extra_build_fanart + '>\n')
        print_extra_text_file.write(r'description=<' + self.extra_build_description + '>\n')
        print_extra_text_file.close()
        choice = xbmcgui.Dialog().yesno("Is There Any More Builds?", 'Would You like to add another build into txt file?', '', 'This Will also show in your wizard when generated', yeslabel='Yes',nolabel='No')
        if choice == 1:
            self.txt_extra_file_inputs()
        elif choice ==0:
            Dialog.ok("[COLOR=white]Origin[/COLOR]", "Your Text File is now Created", '','')
	            
		
    def generate_wizard_py(self,name):


        py_complete_name = os.path.join(self.save_path,self.py_file_name)
        print_default_file = open(py_complete_name,"w+")


        print_default_file.write(r'import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os' +'\n')
        print_default_file.write(r'import shutil' +'\n')
        print_default_file.write(r'import urllib2,urllib' +'\n')
        print_default_file.write(r'import re' +'\n')
        print_default_file.write(r'import extract' +'\n')
        print_default_file.write(r'import downloader' +'\n')
        print_default_file.write(r'import time' +'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r"USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'"+'\n')
        print_default_file.write(r"base='" + self.plugin_name + '\'' +'\n')
        print_default_file.write(r"ADDON=xbmcaddon.Addon(id='plugin.video."+ self.clean_plugin_name + '\')' +'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')    
        print_default_file.write(r''+'\n')    
        print_default_file.write(r'VERSION = "1.0.0"' +'\n')
        print_default_file.write(r"PATH = '" + self.clean_plugin_name + '\'' + '\n')            
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')
        print_default_file.write(r''+'\n')    
        print_default_file.write(r'def CATEGORIES()' +':\n')
        print_default_file.write(r"    link = OPEN_URL('" + self.build_url + "')" +'\n')
        print_default_file.write(r"    match = re.compile('name=<(.+?)>.+?rl=<(.+?)>.+?mg=<(.+?)>.+?anart=<(.+?)>.+?escription=<(.+?)>',re.DOTALL).findall(link)" +'\n')
        print_default_file.write(r'    for name,url,iconimage,fanart,description in match:' +'\n')
        print_default_file.write(r'        addDir(name,url,1,iconimage,fanart,description)' +'\n')
        print_default_file.write(r"    setView('movies', 'MAIN'" +')\n')
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
        print_default_file.close()
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

        print_addon_file.close()
        self.Delay()
 
    def Delay(self):
        os.rename(Addons_path+'TEST',Addons_path +'plugin.video.'+self.clean_plugin_name)
        dp.create("[COLORwhite]Origin[/COLOR]","Writing Files",'','Please Wait')
        time.sleep(1)	
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
        zipobj.close()
        dp.close()
        os.rename(Addons_path +'plugin.video.'+self.clean_plugin_name,Addons_path+'TEST')
        Dialog.ok("[COLOR=white]Origin[/COLOR]", "Your wizard is now created", '','')   
		
		
go = Generator('','','','','','','','','','','','','','','','','','','')

