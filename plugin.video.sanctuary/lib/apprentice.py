'''This section was kindly donated by the dev of the addon - The Apprentice, give him a follow on twitter to say thanks for this amazing section - @Apprentice007'''



import re, xbmcplugin, xbmcgui, process, base64, sys, urllib, comedy, yt, youtube_regex

addon_handle = int(sys.argv[1])
Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
CAT=Decode('LnBocA==')
Base_appren = (Decode('aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vY2FycmVyYS8='))
source_file1 = Base_appren + 'source_file1.php'
source_file2 = Base_appren + 'source_file2.php'
#1000
def apprentice_Main():
    
    process.Menu('[COLOR red]Suggested Movies[/COLOR]','',1301,Base_appren + 'mov.png',Base_appren + 'movback.png','','')
    process.Menu('[COLOR red]Suggested Tv Shows[/COLOR]','',1302,Base_appren + 'tv.png','Base_appren + tvback.png','','')
    process.Menu('[COLOR skyblue]Movies[/COLOR]','',1304,Base_appren + 'mov.png',Base_appren + 'movback.png','','')
    process.Menu('[COLOR skyblue]Tv Shows[/COLOR]','',1306,Base_appren + 'tv.png',Base_appren + 'tvback.png','','')
    process.Menu('[COLOR yellow]abracadabra[/COLOR]','',1307,Base_appren + 'abra.png',Base_appren + 'abra.jpg','','')
	
#    process.Menu('[COLOR green]Search[/COLOR]','',1303,'Base_appren + images.jpg','','','')

    xbmcplugin.setContent(addon_handle, 'movies')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))		
#1001
def Magic_Menu():
    OPEN = process.OPEN_URL(Base_appren +Decode('bWFnaWMucGhw'))
    Regex = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(OPEN)
    for url,img,desc,fanart,name in Regex:
        if 'php' in url:
            process.Menu(name,url,1303,img,fanart,desc,'')
        elif 'playlist' in url:
            process.Menu(name,url,10002,img,fanart,desc,'')
        elif 'watchseries' in url:
            process.Menu(name,url,112,img,fanart,desc,'')
        elif not 'http' in url:
            process.Play(name,url,10003,img,fanart,desc,'')
        else:
            process.Play(name,url,906,img,fanart,desc,'')
    xbmcplugin.setContent(addon_handle, 'movies')
	
def Mov_Menu():
    OPEN = process.OPEN_URL(Base_appren +Decode('bWFpbjIucGhw'))
    Regex = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(OPEN)
    for url,img,desc,fanart,name in Regex:
        if 'php' in url:
            process.Menu(name,url,1303,img,fanart,desc,'')
        elif 'playlink' in url:
            process.Menu(name,url,10002,img,fanart,desc,'')
        elif 'watchseries' in url:
            process.Menu(name,url,112,img,fanart,desc,'')
        elif not 'http' in url:
            process.Play(name,url,10003,img,fanart,desc,'')
        else:
            process.Play(name,url,906,img,fanart,desc,'')
    xbmcplugin.setContent(addon_handle, 'movies')
#1002
def Tv_Menu():
    OPEN = process.OPEN_URL(Base_appren +Decode('bWFpbjMucGhw'))
    Regex = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(OPEN)
    for url,img,desc,fanart,name in Regex:
        if 'php' in url:
            process.Menu(name,url,1303,img,fanart,desc,'')
        elif 'playlink' in url:
            process.Menu(name,url,10002,img,fanart,desc,'')
        elif 'watchseries' in url:
            process.Menu(name,url,112,img,fanart,desc,'')
        elif not 'http' in url:
            process.Play(name,url,10003,img,fanart,desc,'')
        else:
            process.Play(name,url,906,img,fanart,desc,'')
    xbmcplugin.setContent(addon_handle, 'movies')
	
#1003	
def Second_Menu(url):
    OPEN = process.OPEN_URL(url)
    Regex = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(OPEN)
    for url,img,desc,fanart,name in Regex:
        if 'php' in url:
            process.Menu(name,url,1303,img,fanart,desc,'')
        elif 'playlist' in url:
            process.Menu(name,url,10002,img,fanart,desc,'')
        elif 'watchseries' in url:
            process.Menu(name,url,112,img,fanart,desc,'')
        elif not 'http' in url:
            process.Play(name,url,10003,img,fanart,desc,'')
        else:
            process.Play(name,url,906,img,fanart,desc,'')
    xbmcplugin.setContent(addon_handle, 'movies')
#1004
def Index_List_Mov():
    OPEN = process.OPEN_URL(source_file1)
    Regex = re.compile('url="(.+?)">name="(.+?)"').findall(OPEN)
    for url,name in Regex:
            process.Menu(name,url,1305,'','','','')
			
#1006
def Index_List_Tv():
    OPEN = process.OPEN_URL(source_file2)
    Regex = re.compile('url="(.+?)">name="(.+?)"').findall(OPEN)
    for url,name in Regex:
            process.Menu(name,url,1305,'','','','')
			
#####################################MAIN REGEX LOOP ###############################
#1005
def Main_Loop(url):
    HTML = process.OPEN_URL(url)
    match = re.compile('<a href="(.+?)">(.+?)</a>').findall(HTML)
    for url2,name in match:
        url3 = url + url2
        if '..' in url3:
            pass
        elif 'rar' in url3:
            pass
        elif 'jpg' in url3:
            pass
        elif 'vtx' in url3:
            pass
        elif 'srt' in url3:
            pass
        elif 'C=' in url2:
            pass
        elif '/' in url2:
            process.Menu((name).replace('/',''),url3,1305,'','','','')
            
        else:
            Clean_name(name,url3)

################################### TIDY UP NAME #############################

def Clean_name(name,url3):
    name1 = (name).replace('S01E','S01 E').replace('(MovIran).mkv','').replace('The.Walking.Dead','').replace('.mkv','').replace('Tehmovies.com.mkv','').replace('Nightsdl','').replace('Ganool','')
    name2=(name1).replace('.',' ').replace(' (ParsFilm).mkv','').replace('_TehMovies.Com.mkv','').replace(' (SaberFun.IR).mkv','').replace('[UpFilm].mkv','').replace('(Bia2Movies)','')
    name3=(name2).replace('.mkv','').replace('.Film2Movie_INFO.mkv','').replace('.HEVC.Film2Movie_INFO.mkv','').replace('.ParsFilm.mkv ','').replace('(SaberFunIR)','')
    name4=(name3).replace('.INTERNAL.','').replace('.Film2Movie_INFO.mkv','').replace('.web-dl.Tehmovies.net.mkv','').replace('S01E06','S01 E06').replace('S01E07','S01 E07')
    name5=(name4).replace('S01E08','S01 E08').replace('S01E09','S01 E09').replace('S01E10','S01 E10').replace('.Tehmovies.net','').replace('.WEBRip.Tehmovies.com.mkv','')
    name6=(name5).replace('.mp4','').replace('.mkv','').replace('.Tehmovies.ir','').replace('x265HEVC','').replace('Film2Movie_INFO','').replace('Tehmovies.com.mkv','')
    name7=(name6).replace(' (ParsFilm)','').replace('Tehmovies.ir.mkv','').replace('.480p',' 480p').replace('.WEBrip','').replace('.web-dl','').replace('.WEB-DL','')
    name8=(name7).replace('.','').replace('.Tehmovies.com','').replace('480p.Tehmovies.net</',' 480p').replace('720p.Tehmovies.net','720p').replace('.480p',' 480p')
    name9=(name8).replace('.480p.WEB-DL',' 480p').replace('.mkv','').replace('.INTERNAL.','').replace('720p',' 720p').replace('.Tehmovi..&gt;','').replace('.Tehmovies.net.mkv','')
    name10=(name9).replace('..720p',' 720p').replace('.REPACK.Tehmovies..&gt;','').replace('.Tehmovies.com.mkv','').replace('.Tehmovies..&gt;','').replace('Tehmovies.ir..&gt;','')
    name11=(name10).replace('Tehmovies.ne..&gt;','').replace('.HDTV.x264-mRs','').replace('...&gt;','').replace('.Tehmovies...&gt;','').replace('.Tehmovies.com.mp4','')
    name12=(name11).replace('.Tehmovies.com.mp4','').replace('_MovieFarsi','').replace('_MovieFar','').replace('_com','').replace('&gt;','').replace('avi','').replace('(1)','')
    name13=(name12).replace('(2)','').replace('cd 2','').replace('cd 1','').replace('-dos-xvid','').replace('divx','').replace('Xvid','').replace('DVD','').replace('DVDrip','')
    name14=(name13).replace('DvDrip-aXXo','').replace('[','').replace(']','').replace('(','').replace(')','').replace('XviD-TLF-','').replace('CD1','').replace('CD2','')
    name15=(name14).replace('CD3','').replace('mp4','').replace('&amp;','&').replace('HDRip','').replace('-','').replace('  ',' ').replace('xvid','').replace('1080p','').replace('HeyDL','')
    name16=(name15).replace('1970','').replace('1971','').replace('1972','').replace('1973','').replace('1974','').replace('1975','').replace('1976','').replace('1977','')
    name17=(name16).replace('1978','').replace('1979','').replace('1980','').replace('1981','').replace('1982','').replace('1983','').replace('1984','').replace('1985','')
    name18=(name17).replace('1986','').replace('1987','').replace('1988','').replace('1989','').replace('1990','').replace('1991','').replace('1992','').replace('1993','')
    name19=(name18).replace('1994','').replace('1995','').replace('1996','').replace('1997','').replace('1998','').replace('1999','').replace('2000','').replace('2001','')
    name20=(name19).replace('2002','').replace('2003','').replace('2004','').replace('2005','').replace('2006','').replace('2007','').replace('2008','').replace('2009','')
    name21=(name20).replace('2010','').replace('2011','').replace('2012','').replace('2013','').replace('2014','').replace('2015','').replace('2016','').replace('720p','')
    name22=(name21).replace('360p','').replace('  ',' ').replace('BluRay','').replace('rip','').replace('WEBDL','').replace('s01','').replace('s02','').replace('S02','')
    name23=(name22).replace('s03','').replace('s04','').replace('s05','').replace('s06','').replace('s07','').replace('s08','').replace('s09','').replace('S01','')
    name24=(name23).replace('S03','').replace('S04',' ').replace('S05','').replace('S06','').replace('S07','').replace('S08','').replace('S09','').replace('E01','')
    name25=(name24).replace('E02','').replace('E03','').replace('E04','').replace('E05','').replace('E06','').replace('E07','').replace('E08','').replace('E09','').replace('e01','')
    name25=(name24).replace('e02','').replace('e03','').replace('e04','').replace('e05','').replace('e06','').replace('e07','').replace('e08','').replace('e09','').replace('e01','')
    clean_name = name15
    search_name = name25
    process.Play(clean_name,url3,906,'','','','')

