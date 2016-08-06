'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

import sys
import urlparse
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver
import yt

Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
CAT=Decode('LnBocA==')
Base_Pand = (Decode('aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi8='))
addon_id='plugin.video.footballrepeat'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Football Repeat"
VERSION = "1.0.1"
IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'

ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))



def Home_Menu():
    addDirFolder('Highlights','',3,ART + 'icon.png',FANART,'')
    addDirFolder('Fixtures','',4,ART + 'icon.png',FANART,'')
    addDirFolder('Premier League Table','http://www.sportinglife.com/football/premier-league/table',6,ART + 'icon.png',FANART,'')

def Prem_Table(url):	
    addDirFolder('[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]','','','','','')
    html=OPEN_URL(url)
    match = re.compile('<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>',re.DOTALL).findall(html)
    for pos,url,team,pl,w,d,l,f,a,pts,dif in match:
        team = team
        if 'Arsenal' in team:
            image = 'http://s018.radikal.ru/i519/1210/74/a0965770c1bd.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                                  '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Bournemouth' in team:
            image = 'http://soccerlogo.net/uploads/posts/2015-02/1424200737_fc-afc-bournemouth.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                       '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Burnley' in team:
            image = 'https://www.google.co.uk/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiOl4Xrna3OAhVqDcAKHYLQCWoQjRwIBw&url=http%3A%2F%2Fwww.sinfuliphone.com%2Fshowpost.php%3Fp%3D590636%26postcount%3D10&bvm=bv.129391328,d.ZGg&psig=AFQjCNFD5vNL2PaGAi-RtJbAYMcfGrGhiw&ust=1470588123447720'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                                   '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Chelsea' in team:
            image = 'http://soccerlogo.net/uploads/posts/2014-09/1410462243_fc-chelsea.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                                  '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Crystal' in team:
            image = 'http://jonwant.com/wp-content/uploads/2015/04/crystalpalace.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                       '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Everton' in team:
            image = 'http://megaicons.net/static/img/icons_sizes/257/622/256/everton-fc-icon.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                                   '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Hull' in team:
            image = 'http://www.fm-base.co.uk/forum/attachments/football-manager-2013-manager-stories/367359d1373707600-molineux-theatre-dreams-wolves-story-hull.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                                 '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Leicester' in team:
            image = 'http://soccerlogo.net/uploads/posts/2014-09/1410463960_fc-leicester-city.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                       '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Liverpool' in team:
            image = 'http://i641.photobucket.com/albums/uu140/marveljoe_bucket/Liverpool-FC-256x256.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                               '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Manchester City' in team:
            image = 'http://icons.iconseeker.com/png/fullsize/british-football-club/manchester-city.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]               '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Manchester United' in team:
            image = 'https://hdlogo.files.wordpress.com/2013/11/manchester-united.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]          '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Middlesbrough' in team:
            image = 'http://s25.postimg.org/g611tr767/Badge_Middlesbrough256x256.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                 '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Southampton' in team:
            image = 'http://s019.radikal.ru/i639/1210/48/3326d080e375.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                   '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Stoke City' in team:
            image = 'http://s55.radikal.ru/i147/1210/96/e3f610ab745c.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                          '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Sunderland' in team:
            image = 'http://futhead.cursecdn.com/static/img/16/clubs/106.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                        '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Swansea' in team:
            image = 'http://soccerlogo.net/uploads/posts/2014-09/1410462864_fc-swansea_city.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                    '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Tottenham' in team:
            image = 'http://s14.radikal.ru/i187/1210/d2/243ffe6f2f90.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]        '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Watford' in team:
            image = 'http://s25.postimg.org/bclw2n027/Badge_Watford256x256.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]                              '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'Bromwich' in team:
            image = 'http://s018.radikal.ru/i516/1210/6c/d0990201b8d2.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]   '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        elif 'West Ham' in team:
            image = 'http://s018.radikal.ru/i502/1210/60/c38b78fbbdb1.png'
            name = '[COLORwhite]'+pos+' - '+team+'[/COLOR]             '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts
        addDirFolder(str(name),(Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS8/cz0=')+team).replace(' ','+'),1,image,image,'')
    

def FootballFixturesDay():
    html=OPEN_URL(Decode('aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s'))
    match = re.compile('<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"',re.DOTALL).findall(html)
    for url,img,name in match:
        addDirFolder((name).replace('amp;',''),Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + url,5,Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + img,FANART,'')
		
def FootballFixturesGame(url):
    HTML = OPEN_URL(url)
    block = re.compile('AndClearL.+?><h2.+?head>(.*?)float',re.DOTALL).findall(HTML)
    for block in block:
        day = re.compile('(.*?)</h2>').findall(str(block))
        for Day in day:
            Day = Day
        game = re.compile('comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->',re.DOTALL).findall(str(block))
        for comp,img,time,chan in game:
            channel = re.compile(",CAPTION, '(.+?)&nbsp").findall(chan)
            addDirFolder(Day + ' - ' + comp + ' - ' + time,'',5,Decode('aHR0cDovL2xpdmVvbnNhdC5jb20=') + img,FANART,(str(channel)))
    if len(block)<= 0:
        addDirFolder('No Fixtures available yet, come back when season has started','','','','','')
    addDirFolder('[COLORred]Set view to media info 2 for full listings[/COLOR]','','','','','')
    setView('tvshows', 'Media Info 3')

def Football_Highlights():

    addDirFolder('Latest','http://www.fullmatchesandshows.com',8,'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png',FANART,'')
    addDirFolder('EURO 2016','http://www.fullmatchesandshows.com/euro-2016/',8,'http://football.mywapblog.com/files/uefa-euro-2016-logo.png',FANART,'')
    addDirFolder('Shows','http://www.fullmatchesandshows.com/category/show/',8,'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png',FANART,'')
    addDirFolder('Premier League','http://www.fullmatchesandshows.com/premier-league/',8,'https://footballseasons.files.wordpress.com/2013/05/premier-league.png',FANART,'')
    addDirFolder('La Liga','http://www.fullmatchesandshows.com/la-liga/',8,'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png',FANART,'')
    addDirFolder('Bundesliga','http://www.fullmatchesandshows.com/bundesliga/',8,'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg',FANART,'')
    addDirFolder('Champions League','http://www.fullmatchesandshows.com/champions-league/',8,'http://www.ecursuri.ro/images/teste/test-champions-league.jpg',FANART,'')
    addDirFolder('Serie A','http://www.fullmatchesandshows.com/category/serie-a/',8,'http://files.jcriccione.it/200000223-2484526782/serie%20a.png',FANART,'')
    addDirFolder('Ligue 1','http://www.fullmatchesandshows.com/category/ligue-1/',8,'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg',FANART,'')
    addDirFolder('Copa America 2015','http://www.fullmatchesandshows.com/copa-america-2015/',8,'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png',FANART,'')
    addDirFolder('CONCACAF','http://www.fullmatchesandshows.com/category/concacaf/',8,'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png',FANART,'')
    addDirFolder('Women World Cup','http://www.fullmatchesandshows.com/category/women-world-cup/',8,'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png',FANART,'' )


def Get_the_rows(url,iconimage):
    HTML = OPEN_URL(url)
    match2 = re.compile('<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)".+?"entry-thumb" src="(.+?)"').findall(HTML)
    for url,name,img in match2:
        if 'Full Match' in name:
    	    Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            addDirFolder(Name,url,7,img,'','')
        else:
    	    Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            addDir(Name,url,2,img,'','')
    Next = re.compile('<span class="current">.+?</span><a href="(.+?)" class="page" title=".+?">(.+?)</a>').findall(HTML)
    for url,name in Next:
        addDirFolder('NEXT PAGE',url,1,iconimage,FANART,'')
		
def get_All_Rows(url,iconimage):
    HTML = OPEN_URL(url)
    block = re.compile('<div class="td-block-span6">(.+?)<div class="td-pb-span4 td-main-sidebar">',re.DOTALL).findall(HTML)
    match2 = re.compile('<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)".+?"entry-thumb" src="(.+?)"').findall(str(block))
    for url,name,img in match2:
        if 'Full Match' in name:
    	    Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            addDirFolder(Name,url,7,img,'','')
        else:
    	    Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            addDir(Name,url,2,img,'','')
    Next = re.compile('<span class="current">.+?</span><a href="(.+?)" class="page" title=".+?">(.+?)</a>').findall(HTML)
    for url,name in Next:
        addDirFolder('NEXT PAGE',url,1,iconimage,FANART,'')

def get_Multi_Links(url,iconimage):
    addDir('Extended Highlights',url,2,iconimage,FANART,'')
    HTML = OPEN_URL(url)
    match = re.compile('<link href=".+?" rel="stylesheet" type="text/css"><li tabindex="0" class="button_style" id=".+?"><a href="(.+?)"><div class="acp_title">(.+?)</div></a></li>').findall(HTML)
    for url,name in match:
        name = (name).replace('HL English','English Highlights')
        addDir(name,url,2,iconimage,FANART,'')
		
def get_PLAYlink(url):
    HTML = OPEN_URL(url)
    match_youtube = re.compile('<iframe width="560" height="315" src="https://www.youtube.com/embed/(.+?)" frameborder="0" allowfullscreen>').findall(HTML)
    for url in match_youtube:
        yt.PlayVideo(url)
    match = re.compile('<script data-config="(.+?)" data-height').findall(HTML)
    for playlink in match:
        if 'div' in playlink:
            pass
        else:
            Playlink = (playlink).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
            Resolve('http:'+Playlink)

	

def addDir(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDirFolder(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 
	
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
iconimage=None
mode=None
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

def Resolve(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass

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

def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)


if mode == None     : Home_Menu()
elif mode == 1 		: get_All_Rows(url,iconimage)
elif mode == 2 		: get_PLAYlink(url)
elif mode == 3 		: Football_Highlights()
elif mode == 4 		: FootballFixturesDay()
elif mode == 5 		: FootballFixturesGame(url)
elif mode == 6 	 	: Prem_Table(url)
elif mode == 7 		: get_Multi_Links(url,iconimage)
elif mode == 8 		: Get_the_rows(url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
