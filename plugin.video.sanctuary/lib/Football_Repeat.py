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
# Credit to MK for Live Mix (which i studied to work out how GUI Windows work, have adapted some of the code to suit)    

import sys
import urlparse
import urllib,urllib2,datetime,re,os,base64,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs,traceback,cookielib,urlparse,httplib,time
import urlresolver
import yt
import pyxbmct
from threading import Thread

Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
League_Table_Url = 'http://www.sportinglife.com'
footy = 'http://footytube.com'
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.sanctuary/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
icon = ICON
text = '0xffffffff'
background = 'http://herovision.x10host.com/fb_replays/fixtureback.jpg'
power = 'http://herovision.x10host.com/fb_replays/power.png'
power_focus = 'http://herovision.x10host.com/fb_replays/power_focus.png'
addon_button = 'http://herovision.x10host.com/fb_replays/addon_button.png'
addon_button_focus = 'http://herovision.x10host.com/fb_replays/addon_button_focus.png'
metalliq_button = 'http://herovision.x10host.com/fb_replays/metalliq.jpg'
metalliq_button_focus = 'http://herovision.x10host.com/fb_replays/metalliq_focus.jpg'

window  = pyxbmct.AddonDialogWindow('')
window.setGeometry(1250, 650, 100, 50)

Background=pyxbmct.Image(background)
List = pyxbmct.addonwindow.List(_space=11,_itemTextYOffset=0,textColor=text)
Icon=pyxbmct.Image('', aspectRatio=2)
addon_label = pyxbmct.Label('[B][COLORsteelblue]What channels are in addons :-[/COLOR][/B]', alignment=pyxbmct.ALIGN_LEFT)
label = pyxbmct.Label('Kodification.co.uk', alignment=pyxbmct.ALIGN_LEFT)
metalliq_label = pyxbmct.Label('[B][COLORsteelblue]Use Metallic search[/COLOR][/B]', alignment=pyxbmct.ALIGN_LEFT)
button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
one = pyxbmct.Button('1',focusTexture=addon_button_focus,noFocusTexture=addon_button,textColor=text,focusedColor=text)
two = pyxbmct.Button('2', noFocusTexture=addon_button,focusTexture=addon_button_focus)
three = pyxbmct.Button('3', noFocusTexture=addon_button,focusTexture=addon_button_focus)
four = pyxbmct.Button('4', noFocusTexture=addon_button,focusTexture=addon_button_focus)
five = pyxbmct.Button('5', noFocusTexture=addon_button,focusTexture=addon_button_focus)
six = pyxbmct.Button('6', noFocusTexture=addon_button,focusTexture=addon_button_focus)
seven = pyxbmct.Button('7', noFocusTexture=addon_button,focusTexture=addon_button_focus)
eight = pyxbmct.Button('8', noFocusTexture=addon_button,focusTexture=addon_button_focus)
nine = pyxbmct.Button('9', noFocusTexture=addon_button,focusTexture=addon_button_focus)
metalliq = pyxbmct.Button('', noFocusTexture=metalliq_button,focusTexture=metalliq_button_focus)
text_channel = pyxbmct.TextBox(textColor='0xFFFFFFFF')

window.placeControl(Background, -5, 0, 110, 51)
window.placeControl(List, 65, 1, 50, 20)
window.placeControl(Icon, 30, 0, 60, 18)
window.placeControl(addon_label, 35, 0, columnspan=15)
window.placeControl(label, 110, 0, columnspan=15)
window.placeControl(metalliq_label, 39, 23, columnspan=15)
window.placeControl(button, 110,48,10,3)
window.placeControl(text_channel, -5, 0, columnspan=40, rowspan=40)
window.placeControl(one, 43,0,7,4)
window.placeControl(two, 43,4,7,4)
window.placeControl(three, 43,8,7,4)
window.placeControl(four, 43,12,7,4)
window.placeControl(five, 43,16,7,4)
window.placeControl(six, 50,2,7,4)
window.placeControl(seven, 50,6,7,4)
window.placeControl(eight,50,10,7,4)
window.placeControl(nine, 50,14,7,4)
window.placeControl(metalliq, 45,25,12,4)


window.connect(button, window.close)
window.connect(pyxbmct.ACTION_NAV_BACK, window.close)

one.controlRight(two)
one.controlLeft(five)
one.controlDown(six)
one.controlUp(button)
two.controlRight(three)
two.controlLeft(one)
two.controlDown(seven)
two.controlUp(button)
three.controlRight(four)
three.controlLeft(two)
three.controlDown(eight)
three.controlUp(button)
four.controlRight(five)
four.controlLeft(three)
four.controlDown(nine)
four.controlUp(button)
five.controlRight(metalliq)
five.controlLeft(four)
five.controlDown(nine)
five.controlUp(button)
six.controlRight(seven)
six.controlLeft(nine)
six.controlDown(List)
six.controlUp(one)
seven.controlRight(eight)
seven.controlLeft(six)
seven.controlDown(List)
seven.controlUp(two)
eight.controlRight(nine)
eight.controlLeft(seven)
eight.controlDown(List)
eight.controlUp(three)
nine.controlRight(metalliq)
nine.controlLeft(eight)
nine.controlDown(List)
nine.controlUp(four)
metalliq.controlRight(button)
metalliq.controlLeft(five)
metalliq.controlDown(List)
metalliq.controlUp(button)
List.controlRight(button)
List.controlLeft(button)
List.controlUp(seven)
button.controlLeft(List)
button.controlRight(List)
button.controlDown(two)
button.controlUp(metalliq)

def ONE():
    window_addon  = pyxbmct.AddonDialogWindow('')
    window_addon.setGeometry(1250, 650, 100, 50)
    button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
    window_addon.placeControl(button, 110,48,10,3)
    window_addon.connect(button, window_addon.close)
    window_addon.setFocus(button)
    label = pyxbmct.Label('[B][COLORsteelblue]Press enter to return to last menu if back doesn\'t work --->[/COLOR][/B]', alignment=pyxbmct.ALIGN_LEFT) 
    window_addon.placeControl(label, 111, 22, columnspan=25)
    bckg = 'http://herovision.x10host.com/fb_replays/SPORTS_LIST1.jpg'
    Background_one=pyxbmct.Image(bckg)
    window_addon.placeControl(Background_one, -5, 0, 110, 51)
    window_addon.doModal()
    window_addon.connect(pyxbmct.ACTION_NAV_BACK, window_addon.close)
    del window_addon	

def TWO():
    window_addon  = pyxbmct.AddonDialogWindow('')
    window_addon.setGeometry(1250, 650, 100, 50)
    button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
    window_addon.placeControl(button, 110,48,10,3)
    window_addon.connect(button, window_addon.close)
    window_addon.setFocus(button)
    bckg = 'http://herovision.x10host.com/fb_replays/SPORTS_LIST2.jpg'
    Background_two=pyxbmct.Image(bckg)
    window_addon.placeControl(Background_two, -5, 0, 110, 51)
    window_addon.doModal()
    window_addon.connect(pyxbmct.ACTION_NAV_BACK, window_addon.close)
    del window_addon	

def THREE():
    window_addon  = pyxbmct.AddonDialogWindow('')
    window_addon.setGeometry(1250, 650, 100, 50)
    button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
    window_addon.placeControl(button, 110,48,10,3)
    window_addon.connect(button, window_addon.close)
    window_addon.setFocus(button)
    bckg = 'http://herovision.x10host.com/fb_replays/SPORTS_LIST3.jpg'
    Background_three=pyxbmct.Image(bckg)
    window_addon.placeControl(Background_three, -5, 0, 110, 51)
    window_addon.doModal()
    window_addon.connect(pyxbmct.ACTION_NAV_BACK, window_addon.close)
    del window_addon	

def FOUR():
    window_addon  = pyxbmct.AddonDialogWindow('')
    window_addon.setGeometry(1250, 650, 100, 50)
    button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
    window_addon.placeControl(button, 110,48,10,3)
    window_addon.connect(button, window_addon.close)
    window_addon.setFocus(button)
    bckg = 'http://herovision.x10host.com/fb_replays/SPORTS_LIST4.jpg'
    Background_four=pyxbmct.Image(bckg)
    window_addon.placeControl(Background_four, -5, 0, 110, 51)
    window_addon.doModal()
    window_addon.connect(pyxbmct.ACTION_NAV_BACK, window_addon.close)
    del window_addon	

def FIVE():
    window_addon  = pyxbmct.AddonDialogWindow('')
    window_addon.setGeometry(1250, 650, 100, 50)
    button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
    window_addon.placeControl(button, 110,48,10,3)
    window_addon.connect(button, window_addon.close)
    window_addon.setFocus(button)
    bckg = 'http://herovision.x10host.com/fb_replays/SPORTS_LIST5.jpg'
    Background_five=pyxbmct.Image(bckg)
    window_addon.placeControl(Background_five, -5, 0, 110, 51)
    window_addon.doModal()
    window_addon.connect(pyxbmct.ACTION_NAV_BACK, window_addon.close)
    del window_addon	

def SIX():
    window_addon  = pyxbmct.AddonDialogWindow('')
    window_addon.setGeometry(1250, 650, 100, 50)
    button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
    window_addon.placeControl(button, 110,48,10,3)
    window_addon.connect(button, window_addon.close)
    window_addon.setFocus(button)
    bckg = 'http://herovision.x10host.com/fb_replays/SPORTS_LIST6.jpg'
    Background_six=pyxbmct.Image(bckg)
    window_addon.placeControl(Background_six, -5, 0, 110, 51)
    window_addon.doModal()
    window_addon.connect(pyxbmct.ACTION_NAV_BACK, window_addon.close)
    del window_addon	

def SEVEN():
    window_addon  = pyxbmct.AddonDialogWindow('')
    window_addon.setGeometry(1250, 650, 100, 50)
    button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
    window_addon.placeControl(button, 110,48,10,3)
    window_addon.connect(button, window_addon.close)
    window_addon.setFocus(button)
    bckg = 'http://herovision.x10host.com/fb_replays/SPORTS_LIST7.jpg'
    Background_seven=pyxbmct.Image(bckg)
    window_addon.placeControl(Background_seven, -5, 0, 110, 51)
    window_addon.doModal()
    window_addon.connect(pyxbmct.ACTION_NAV_BACK, window_addon.close)
    del window_addon	

def EIGHT():
    window_addon  = pyxbmct.AddonDialogWindow('')
    window_addon.setGeometry(1250, 650, 100, 50)
    button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
    window_addon.placeControl(button, 110,48,10,3)
    window_addon.connect(button, window_addon.close)
    window_addon.setFocus(button)
    bckg = 'http://herovision.x10host.com/fb_replays/SPORTS_LIST8.jpg'
    Background_eight=pyxbmct.Image(bckg)
    window_addon.placeControl(Background_eight, -5, 0, 110, 51)
    window_addon.doModal()
    window_addon.connect(pyxbmct.ACTION_NAV_BACK, window_addon.close)
    del window_addon	

def NINE():
    window_addon  = pyxbmct.AddonDialogWindow('')
    window_addon.setGeometry(1250, 650, 100, 50)
    button = pyxbmct.Button('', noFocusTexture=power,focusTexture=power_focus)
    bckg = 'http://herovision.x10host.com/fb_replays/SPORTS_LIST9.jpg'
    Background_nine=pyxbmct.Image(bckg)
    window_addon.placeControl(Background_nine, -5, 0, 110, 51)
    window_addon.placeControl(button, 110,48,10,3)
    window_addon.connect(button, window_addon.close)
    window_addon.setFocus(button)
    window_addon.doModal()
    window_addon.connect(pyxbmct.ACTION_NAV_BACK, window_addon.close)
    del window_addon	
	

def METALLIQ_SEARCH():
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.metalliq/live/search)")
	
def METALLIQ():
    xbmc.executebuiltin("ActivateWindow(10025,plugin://plugin.video.metalliq/live,return)")
	
window.connect(one,ONE)
window.connect(two,TWO)
window.connect(three,THREE)
window.connect(four,FOUR)
window.connect(five,FIVE)
window.connect(six,SIX)
window.connect(seven,SEVEN)
window.connect(eight,EIGHT)
window.connect(nine,NINE)
window.connect(metalliq,METALLIQ_SEARCH)




def footy_Main_Menu():
    addDirFolder('Highlights','',403,ICON,FANART,'')
    addDirFolder('Fixtures','',404,ICON,FANART,'')
    addDirFolder('League Tables',League_Table_Url+'/football/tables',409,ICON,FANART,'')
    addDirFolder('Team Search',League_Table_Url+'/football/tables',410,ICON,FANART,'')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def FootballFixturesDay():
    html=OPEN_URL(Decode('aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s'))
    match = re.compile('<a target="_self" href="([^"]*)">.+?<img border="0" src="([^"]*)" alt="([^"]*)" width=".+?" height=".+?"></a>',re.DOTALL).findall(html)
    for url,img,name in match:
        if '</a>' in img:
            pass
        addDirFolder((name).replace('amp;',''),Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + url,405,Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + img,FANART,'')
		
def FootballFixturesGame(url,img):
    addDirFolder('[COLORblue]Metalliq Live TV List[/COLOR] - [COLORwhite]You will need to close Metalliq and[/COLOR]','',421,ICON,FANART,'')
    addDirFolder('[COLORwhite]return here if you press this[/COLOR]','',421,ICON,FANART,'')
    HTML = OPEN_URL(url)
    block = re.compile('AndClearL.+?><h2.+?= time_head>(.+?)</h2>(.*?)float',re.DOTALL).findall(HTML)
    for date,block in block:
        addDir(date,'',420,img,FANART,block)

def cleanHex(text):
	def fixup(m):
		text = m.group(0)
		if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
		else: return unichr(int(text[2:-1])).encode('utf-8')
	try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
	except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))

		
def FootballFixturesSingle(block):
    global channel_list
    global icon_list
    icon_list = []
    channel_list = []
    fix_List = []
    game = re.compile('comp_head>(.+?)-- around all of channel types ENDS 2-->',re.DOTALL).findall(str(block))
    for item in game:
        game = re.compile('comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->',re.DOTALL).findall(str(block))
        for comp,img,time,chan in game:
            channel = re.compile(",CAPTION, '(.+?)&nbsp").findall(chan)
            channel_final = (str(channel)).replace('[$]','').replace('\\xc3','n').replace('\'','').replace('[','').replace(']','').replace('\\xe2','').replace('\\x80','').replace('\\x99','').replace('\\xb1a','i')
            name = str(comp) + ' - ' + str(time)
            image = Decode('aHR0cDovL2xpdmVvbnNhdC5jb20=') + str(img)
            if not channel_final in fix_List:
#                addDirFolder(name,'',405,image,FANART,channel_final)
                fix_List.append(channel_final)
                List.addItem(name)
#                text_channel.addLabel(channel_final)
                channel_list.append(channel_final)
                icon_list.append(image)
                create_window(name,image,channel_final)
    if len(block)<= 0:
        addDirFolder('No Fixtures available yet, come back when season has started','','','','','')
#    addDirFolder('[COLORred]Set view to media info 2 for full listings[/COLOR]','','','','','')
#    setView('tvshows', 'Media Info 3')

def create_window(name,img,channel_final):
    global window
    window.setFocus(one)
    #capture mouse moves or up down arrows
    window.connectEventList(
    [pyxbmct.ACTION_MOVE_DOWN,
    pyxbmct.ACTION_MOVE_UP,
    pyxbmct.ACTION_MOUSE_MOVE],
    LIST_UPDATE)
    
def LIST_UPDATE():
    if window.getFocus() == List:    	
        pos=List.getSelectedPosition()
        iconimage=icon_list[pos]
        Icon.setImage(iconimage)
        channel_label = channel_list[pos]
        text_channel.setText(channel_label)
			
def Search():
    search_name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    url = Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS8/cz0=')+(search_name).replace(' ','+')
    origin_url = Decode('aHR0cDovL3d3dy5mb290YmFsbG9yZ2luLmNvbS8/cz0=')+(search_name).replace(' ','+')
    Origin_Highlights(origin_url)
    Get_the_rows(url,ICON)
    
def Origin_Highlights(url):
    HTML = OPEN_URL(url)
    match = re.compile('<article id=".+?" class=".+?<img width=".+?" height=".+?" src="(.+?)" class=.+?<h2 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h2>',re.DOTALL).findall(HTML)
    for img,url,name in match:
        name = (name).replace('&#8211;','-')
        addDirFolder(name,url,418,img,FANART,'')
		
def get_origin_playlink(url,img,FANART):
    List = []
    HTML = OPEN_URL(url)
    match = re.compile('1st Half<br />.+?<script data-config="(.+?)" data-height',re.DOTALL).findall(HTML)
    match2 = re.compile('2nd Half<br />.+?<script data-config="(.+?)" data-height',re.DOTALL).findall(HTML)
    match3 = re.compile('2nd Half<br />.+?<script data-config="(.+?)" data-height',re.DOTALL).findall(HTML)
    match4 = re.compile('<p>Watch Online Full Match Replay</p>.+?<p><script data-config="(.+?)" data-height',re.DOTALL).findall(HTML)
    match5 = re.compile('<p>&nbsp;<br />.+?<script data-config="(.+?)" data-height',re.DOTALL).findall(HTML)
    match6 = re.compile('<p>&nbsp;</p>.+?data-config="(.+?)" data-height=',re.DOTALL).findall(HTML)
    for url in match:
        Playlink = (url).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
        play_link = 'http:'+Playlink
        addDir('1st Half',play_link,419,img,FANART,'')
    for url in match2:
        Playlink = (url).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
        play_link = 'http:'+Playlink
        addDir('2nd Half',play_link,419,img,FANART,'')
        List.append('2nd Half')
    for url in match3:
        if '2nd Half' not in List:
            Playlink = (url).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
            play_link = 'http:'+Playlink
            addDir('2nd Half',play_link,419,img,FANART,'')
    for url in match4:
        if '2nd Half' not in List:
            if 'Full Match' not in List:
                Playlink = (url).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
                play_link = 'http:'+Playlink
                addDir('Full Match',play_link,419,img,FANART,'')
                List.append('Full Match')
    for url in match5:
        if '2nd Half' not in List:
            if 'Full Match' not in List:
                Playlink = (url).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
                play_link = 'http:'+Playlink
                addDir('Full Match',play_link,419,img,FANART,'')
                List.append('Full Match')
    for url in match6:
        if '2nd Half' not in List:
            if 'Full Match' not in List:
                Playlink = (url).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
                play_link = 'http:'+Playlink
                addDir('Full Match',play_link,419,img,FANART,'')
                List.append('Full Match')
 
	
def League_Tables(url):
    addDirFolder('Premier League','http://www.sportinglife.com/football/premier-league/table',406,ICON,FANART,'')
    addDirFolder('Scottish Premier','http://www.sportinglife.com/football/scottish-premier/table',406,ICON,FANART,'')
    addDirFolder('Championship','http://www.sportinglife.com/football/championship/table',406,ICON,FANART,'')
    addDirFolder('Champions League','http://www.sportinglife.com/football/champions-league/table',412,ICON,FANART,'')
    addDirFolder('Europa League','http://www.sportinglife.com/football/europa-league/table',412,ICON,FANART,'')
    addDirFolder('League One','http://www.sportinglife.com/football/league-one/table',411,ICON,FANART,'')
    addDirFolder('League Two','http://www.sportinglife.com/football/league-two/table',411,ICON,FANART,'')
    addDirFolder('Scottish Championship','http://www.sportinglife.com/football/scottish-championship/table',411,ICON,FANART,'')
    addDirFolder('Scottish League One','http://www.sportinglife.com/football/scottish-league-one/table',411,ICON,FANART,'')
    addDirFolder('Scottish League Two','http://www.sportinglife.com/football/scottish-league-two/table',411,ICON,FANART,'')
    addDirFolder('National League','http://www.sportinglife.com/football/national-league/table',411,ICON,FANART,'')
    addDirFolder('La Liga','http://www.sportinglife.com/football/la-liga/table',411,ICON,FANART,'')
    addDirFolder('Serie A','http://www.sportinglife.com/football/serie-a/table',411,ICON,FANART,'')
    addDirFolder('Bundesliga','http://www.sportinglife.com/football/bundesliga/table',411,ICON,FANART,'')
    addDirFolder('Ligue 1','http://www.sportinglife.com/football/ligue-1/table',411,ICON,FANART,'')
    addDirFolder('Eredivisie','http://www.sportinglife.com/football/eredivisie/table',411,ICON,FANART,'')
    addDirFolder('Portuguese Liga','http://www.sportinglife.com/football/portuguese-liga/table',411,ICON,FANART,'')

def champ_league(url):
    HTML = OPEN_URL(url)
    block = re.compile('class="hdr t2">(.+?)<span class="aside">(.+?)<h2 ',re.DOTALL).findall(HTML)
    for league,block in block:
        addDirFolder('[COLORwhite]                                                               '+(league).replace(' - Short table','')+'[/COLOR]','',411,ICON,FANART,'')
        addDirFolder('[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]','','','','','')
        match2 = re.compile('<td>(.+?)</td>.+?<td class="ixt div"><strong>(.+?)</strong></td>.+?<td class="div">(.+?)</td>.+?<td>(.+?)</td>.+?<td>(.+?)</td>.+?<td>(.+?)</td>.+?<td class="mobile-hdn">(.+?)</td>.+?<td class="mobile-hdn">(.+?)</td>.+?<td class="div">(.+?)</td>.+?<td class="div">(.+?)</td>.+?</tr>',re.DOTALL).findall(str(block))
        for pos,team,pl,w,d,l,f,a,pts,dif in match2:
            Cleaner(pos,team,pl,w,d,l,f,a,pts,dif)
        match = re.compile('<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td s="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>',re.DOTALL).findall(str(block))
        for pos,url,team,pl,w,d,l,f,a,pts,dif in match:
            Cleaner(pos,team,pl,w,d,l,f,a,pts,dif)

def Prem_Table(url):	
    addDirFolder('[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]','','','','','')
    html=OPEN_URL(url)
    match = re.compile('<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>',re.DOTALL).findall(html)
    for pos,url,team,pl,w,d,l,f,a,pts,dif in match:
        Cleaner(pos,team,pl,w,d,l,f,a,pts,dif)

def Prem_Table2(url):	
    addDirFolder('[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]','','','','','')
    html=OPEN_URL(url)
    match2 = re.compile('<tr id="team-.+?">.+?<td>(.+?)</td>.+?<td class="ixt div"><strong>(.+?)</strong></td>.+?<td class="div">(.+?)</td>.+?<td>(.+?)</td>.+?<td>(.+?)</td>.+?<td>(.+?)</td>.+?<td class="mobile-hdn">(.+?)</td>.+?<td class="mobile-hdn">(.+?)</td>.+?<td class="div">(.+?)</td>.+?<td class="div">(.+?)</td>.+?</tr>',re.DOTALL).findall(html)
    for pos,team,pl,w,d,l,f,a,pts,dif in match2:
        Cleaner(pos,team,pl,w,d,l,f,a,pts,dif)
		
def Cleaner(pos,team,pl,w,d,l,f,a,pts,dif):
    image = ICON
    gap = ' '
    if '<a href' in team:
        pass
    else:
        if 'Arsenal' in team:
            image = 'http://s018.radikal.ru/i519/1210/74/a0965770c1bd.png'
            gap = '                                   '
        elif 'Bournemouth' in team:
            image = 'http://soccerlogo.net/uploads/posts/2015-02/1424200737_fc-afc-bournemouth.png'
            gap = '                        '
        elif 'Burnley' in team:
            image = 'http://s019.radikal.ru/i627/1212/a9/cc25ae83d515.png'
            gap = '                                    '
        elif 'Chelsea' in team:
            image = 'http://soccerlogo.net/uploads/posts/2014-09/1410462243_fc-chelsea.png'
            gap = '                                   '
        elif 'Crystal' in team:
            image = 'http://jonwant.com/wp-content/uploads/2015/04/crystalpalace.png'
            gap = '                        '
        elif 'Everton' in team:
            image = 'http://megaicons.net/static/img/icons_sizes/257/622/256/everton-fc-icon.png'
            gap = '                                     '
        elif 'Hull' in team:
            image = 'http://www.fm-base.co.uk/forum/attachments/football-manager-2013-manager-stories/367359d1373707600-molineux-theatre-dreams-wolves-story-hull.png'
            gap = '                                   '
        elif 'Leicester' in team:
            image = 'http://soccerlogo.net/uploads/posts/2014-09/1410463960_fc-leicester-city.png'
            gap = '                          '
        elif 'Liverpool' in team:
            image = 'http://i641.photobucket.com/albums/uu140/marveljoe_bucket/Liverpool-FC-256x256.png'
            gap = '                                  '
        elif 'Manchester City' in team:
            image = 'http://icons.iconseeker.com/png/fullsize/british-football-club/manchester-city.png'
            gap = '                   '
        elif 'Manchester United' in team:
            image = 'https://hdlogo.files.wordpress.com/2013/11/manchester-united.png'
            gap = '              '
        elif 'Middlesbrough' in team:
            image = 'http://s25.postimg.org/g611tr767/Badge_Middlesbrough256x256.png'
            gap = '                     '
        elif 'Southampton' in team:
            image = 'http://s019.radikal.ru/i639/1210/48/3326d080e375.png'
            gap = '                       '
        elif 'Stoke City' in team:
            image = 'http://s55.radikal.ru/i147/1210/96/e3f610ab745c.png'
            gap = '                              '
        elif 'Sunderland' in team:
            image = 'http://futhead.cursecdn.com/static/img/16/clubs/106.png'
            gap = '                            '
        elif 'Swansea' in team:
            image = 'http://soccerlogo.net/uploads/posts/2014-09/1410462864_fc-swansea_city.png'
            gap = '                        '
        elif 'Tottenham' in team:
            image = 'http://s14.radikal.ru/i187/1210/d2/243ffe6f2f90.png'
            gap = '            '
        elif 'Watford' in team:
            image = 'http://s25.postimg.org/bclw2n027/Badge_Watford256x256.png'
            gap = '                                  '
        elif 'Bromwich' in team:
            image = 'http://s018.radikal.ru/i516/1210/6c/d0990201b8d2.png'
            gap = '       '
        elif 'West Ham' in team:
            image = 'http://s018.radikal.ru/i502/1210/60/c38b78fbbdb1.png'
            gap = '                 '
        elif team == 'Rangers':
            gap = '                                 '
            image = 'http://www.futbol24.com/upload/team/Scotland/Rangers-FC.png'        
        elif team == 'Dundee':
			gap = '                                  '
			image = 'http://s019.radikal.ru/i619/1302/45/89c176826ee0.png'
        elif team == 'Partick Thistle':
			gap = '                      '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415187200_fc-partick-thistle.png'
        elif team == 'Celtic':
			gap = '                                      '
			image = 'http://images.all-free-download.com/images/graphicthumb/celtic_89609.jpg'
        elif team == 'Motherwell':
			gap = '                            '
			image = 'http://s017.radikal.ru/i402/1302/ff/6e26b9690585.png'
        elif team == 'Hamilton Academical':
			gap = '         '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415187107_fc-hamilton-academical.png'
        elif team == 'Aberdeen':
			gap = '                               '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415187671_fc-aberdeen.png'
        elif team == 'St Johnstone':
			gap = '                        '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415186466_fc-st.png'
        elif team == 'Hearts':
			gap = '                                     '
			image = 'http://s018.radikal.ru/i517/1302/ee/78ffa50b46ef.png'
        elif team == 'Kilmarnock':
			gap = '                           '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415187304_fc-kilmarnock.png'
        elif team == 'Ross County':
			gap = '                        '
			image = 'http://e0.365dm.com/football/badges/192/578.png'
        elif team == 'Inverness CT':
			gap = '                       '
			image = 'http://s44.radikal.ru/i103/1302/ef/5ca4bc61d7fb.png'
        elif team == 'Norwich City':
			gap = '                         '
			image = 'http://images.all-free-download.com/images/graphicthumb/norwich_city_89629.jpg'
        elif team == 'Queens Park Rangers':
			gap = '         '
			image = 'http://images.all-free-download.com/images/graphicthumb/queens_park_rangers_91721.jpg'
        elif team == 'Ipswich Town':
			gap = '                       '
			image = 'http://images.all-free-download.com/images/graphicthumb/ipswich_town_89618.jpg'
        elif team == 'Nottingham Forest':
			gap = '              '
			image = 'http://images.all-free-download.com/images/graphicthumb/nottingham_forest_89630.jpg'
        elif team == 'Bristol City':
			gap = '                             '
			image = 'http://images.all-free-download.com/images/graphicthumb/bristol_city_91708.jpg'
        elif team == 'Huddersfield Town':
			gap = '              '
			image = 'http://megaicons.net/static/img/icons_sizes/257/622/256/huddersfield-town-icon.png'
        elif team == 'Fulham':
			gap = '                                    '
			image = 'http://images.all-free-download.com/images/graphicthumb/fulham_fc_89615.jpg'
        elif team == 'Reading':
			gap = '                                   '
			image = 'http://megaicons.net/static/img/icons_sizes/257/622/256/reading-fc-icon.png'
        elif team == 'Sheffield Wednesday':
			gap = '           '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424204019_fc-sheffield-wednesday.png'
        elif team == 'Rotherham United':
			gap = '              '
			image = 'http://megaicons.net/static/img/icons_sizes/257/622/256/rotherham-united-icon.png'
        elif team == 'Wolverhampton Wanderers':
			team = 'Wolves'
			gap = '                                   '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424203819_fc-wolverhampton-wanderers.png'
        elif team == 'Birmingham City':
			gap = '                  '
			image = 'http://images.all-free-download.com/images/graphicthumb/birmingham_city_89604.jpg'
        elif team == 'Brighton and Hove Albion':
			gap = ' '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424204174_fc-brighton-hove-albion.png'
        elif team == 'Cardiff City':
			gap = '                            '
			image = 'http://s25.postimg.org/jbq8xpf67/Cardiff256x256.png'
        elif team == 'Derby County':
			gap = '                        '
			image = 'http://images.all-free-download.com/images/graphicthumb/derby_county_89612.jpg'
        elif team == 'Burton Albion':
			gap = '                        '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424286586_fc-burton-albion.png'
        elif team == 'Brentford':
			gap = '                                '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424202784_fc-brentford.png'
        elif team == 'Wigan Athletic':
			gap = '                       '
			image = 'http://megaicons.net/static/img/icons_sizes/257/622/256/wigan-athletic-icon.png'
        elif team == 'Aston Villa':
			gap = '                              '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410464618_fc-aston-villa.png'
        elif team == 'Newcastle United':
			gap = '                  '
			image = 'http://images.all-free-download.com/images/graphicthumb/newcastle_united_89627.jpg'
        elif team == 'Preston North End':
			gap = '               '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424258180_fc-preston-north-end.png'
        elif team == 'Barnsley':
			gap = '                                  '
			image = 'http://images.all-free-download.com/images/graphicthumb/barnsley_fc_91706.jpg'
        elif team == 'Blackburn Rovers':
			gap = '                  '
			image = 'http://images.all-free-download.com/images/graphicthumb/blackburn_rovers_89605.jpg'
        elif team == 'Leeds United':
			gap = '                          '  
			image = 'http://images.all-free-download.com/images/graphicthumb/leeds_united_89620.jpg'
        elif team == 'Molde':
			gap = '                                    '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs_large/417.png'
        elif team == 'Fenerbahce':
			gap = '                          '
			image = 'https://d2r1vs3d9006ap.cloudfront.net/s3_images/1436615/RackMultipart20160619-892-iw4va9-Fenerbah_e_v2_inline.PNG?1466374766'
        elif team == 'Ajax':
			gap = '                                        '
			image = 'http://images.all-free-download.com/images/graphicthumb/ajax_91238.jpg'
        elif team == 'FC Sion':
			gap = '                                  '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/110770.png'
        elif team == 'Rubin Kazan':
			gap = '                         '
			image = 'https://1.bp.blogspot.com/-1MTXvM-8Mi0/V2ScueWJ36I/AAAAAAAAR74/f5vygdh-IZAAwJBexs_GJvMJ7sAchEfoQCLcB/s400/rubin-kazan4.png'
        elif team == 'Bordeaux':
			gap = '                               '
			image = 'http://images.all-free-download.com/images/graphicthumb/girordins_de_bordeaux_91762.jpg'
        elif team == 'Krasnodar':
			gap = '                             '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/112218.png'
        elif team == 'Borussia Dortmund':
			gap = '            '
			image = 'http://images.all-free-download.com/images/graphicthumb/borussia_dortmund_92032.jpg'
        elif team == 'PAOK Salonika':
			gap = '                     '
			image = 'http://images.all-free-download.com/images/graphicthumb/paok_salonika_92192.jpg'
        elif team == 'FK Qabala':
			gap = '                              '
			image = 'http://fr.bar-sports.com/assets/images/flags/256_code/sk.png'
        elif team == 'Napoli':
			gap = '                                     '   
			image = 'http://images.all-free-download.com/images/graphicthumb/napoli_93544.jpg'
        elif team == 'FC Midtjylland':
			gap = '                      '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/1516.png'
        elif team == 'Club Brugge':
			gap = '                          '
			image = 'http://images.all-free-download.com/images/graphicthumb/club_america_101002.jpg'
        elif team == 'Legia Warsaw':
			gap = '                       '
			image = 'https://pbs.twimg.com/profile_images/681809569979445248/BCFEEmAV.jpg'
        elif team == 'Rapid Vienna':
			gap = '                         '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs_large/254.png'
        elif team == 'Villarreal':
			gap = '                                 '
			image = 'http://www.director11.com/wp-content/uploads/2013/06/VillarrealCF.png'
        elif team == 'FC Viktoria Plzen':
			gap = '                 '
			image = 'http://3.bp.blogspot.com/-Qv-ZO7gNHog/Ul1IZX6H9mI/AAAAAAAAFIo/i62-pDbVoms/s1600/FC-Viktoria-Plze%C5%88.png'
        elif team == 'Dinamo Minsk':
			gap = '                      '
			image = 'http://www.futbol24.com/upload/team/Belarus/Dinamo-Minsk.png'
        elif team == 'Braga':
			gap = '                                      '
			image = 'http://images.all-free-download.com/images/graphicthumb/sporting_braga_98327.jpg'
        elif team == 'Marseille':
			gap = '                                '
			image = 'http://images.all-free-download.com/images/graphicthumb/olumpique_de_marseille_91766.jpg'
        elif team == 'Slovan Liberec':
			gap = '                      '
			image = 'http://www.futbol24.com/upload/team/Czech-Rep/Slovan-Liberec.png'
        elif team == 'Groningen':
			gap = '                              '
			image = 'http://images.all-free-download.com/images/graphicthumb/fc_groningen_91242.jpg'
        elif team == 'Lazio':
			gap = '                                        '
			image = 'http://images.all-free-download.com/images/graphicthumb/ss_lazio_93548.jpg'
        elif team == 'St Etienne':
			gap = '                               '
			image = 'http://images.all-free-download.com/images/graphicthumb/as_saint_etienne_91751.jpg'
        elif team == 'Dnipro':
			gap = '                                      '
			image = 'http://www.futbol24.com/upload/team/Ukraine/Dnipro.png'
        elif team == 'Rosenborg':
			gap = '                              '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/298.png'
        elif team == 'Lokomotiv Moscow':
			gap = '              '
			image = 'http://cdn.staticneo.com/w/pes/1/18/Lokomotiv.png'
        elif team == 'Sporting Lisbon':
			gap = '                     '
			image = 'http://images.all-free-download.com/images/graphicthumb/sporting_cp_lisbon_98328.jpg'
        elif team == 'Besiktas':
			gap = '                                  '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/327.png'
        elif team == 'Skenderbeu':
			gap = '                            '
			image = 'http://www.futbol24.com/upload/team/Albania/Skenderbeu.png'
        elif team == 'Basel':
			gap = '                                        '
			image = 'http://www.futbol24.com/upload/team/Switzerland/FC-Basel.png'
        elif team == 'Fiorentina':
			gap = '                                '
			image = 'http://images.all-free-download.com/images/graphicthumb/fiorentina_93537.jpg'
        elif team == 'Lech Poznan':
			gap = '                           '
			image = 'http://www.futbol24.com/upload/team/Poland/Lech-Poznan.png'
        elif team == 'Belenenses':
			gap = '                              '
			image = 'http://images.all-free-download.com/images/graphicthumb/cf_belenenses_98318.jpg'
        elif team == 'Anderlecht':
			gap = '                               '
			image = 'http://www.futbol24.com/upload/team/Belgium/Anderlecht.png'
        elif team == 'Monaco':
			gap = '                                    '
			image = 'http://images.all-free-download.com/images/graphicthumb/monaco_93386.jpg'
        elif team == 'Qarabag FK':
			gap = '                              '
			image = 'http://www.futbol24.com/upload/team/Azerbaijan/Karabakh-Agdam.png'
        elif team == 'Schalke':
			gap = '                                     '
			image = 'http://images.all-free-download.com/images/graphicthumb/schalke_04_92042.jpg'
        elif team == 'Sparta Prague':
			gap = '                          '
			image = 'http://images.all-free-download.com/images/graphicthumb/sparta_rotterdam_91254.jpg'
        elif team == 'Asteras Tripoli':
			gap = '                         '
			image = 'http://www.futbol24.com/upload/team/Greece/Asteras-Tripoli.png'
        elif team == 'Apoel Nicosia':
			gap = '                           '
			image = 'http://images.all-free-download.com/images/graphicthumb/apoel_nicosia_92176.jpg'
        elif team == 'Athletic Bilbao':
			gap = '                          '
			image = 'http://images.all-free-download.com/images/graphicthumb/athletic_bilbao_101023.jpg'
        elif team == 'FC Augsburg':
			gap = '                            '
			image = 'http://futhead.cursecdn.com/static//img/15/clubs_large/100409.png'
        elif team == 'Partizan Belgrade':
			gap = '                    '
			image = 'http://www.futbol24.com/upload/team/Serbia/FK-Partizan.png'
        elif team == 'AZ Alkmaar':
			gap = '                               '
			image = 'http://images.all-free-download.com/images/graphicthumb/az_alkmaar_91239.jpg'
        elif team == 'Celtic':
			gap = '                                        '
			image = 'http://images.all-free-download.com/images/graphicthumb/celtic_89609.jpg'
        elif team == 'Liverpool':
			gap = '                                     '
			image = 'http://images.all-free-download.com/images/graphicthumb/liverpool_fc_94224.jpg'
        elif team == 'Tottenham Hotspur':
			gap = '                                   '
			image = ICON
        elif team == 'Millwall':
			gap = '                                    '
			image = 'http://images.all-free-download.com/images/graphicthumb/millwall_fc_89626.jpg'
        elif team == 'Gillingham':
			gap = '                               '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs_large/1802.png'
        elif team == 'Scunthorpe United':
			gap = '                '
			image = 'http://images.all-free-download.com/images/graphicthumb/scunthorpe_united_91722.jpg'
        elif team == 'Walsall':
			gap = '                                     '
			image = 'http://s60.radikal.ru/i168/1302/43/e47a3b82757f.png'
        elif team == 'Bury':
			gap = '                                          '
			image = 'http://s019.radikal.ru/i607/1301/bc/3e44a5e6d735.png'
        elif team == 'Peterborough United':
			gap = '            '
			image = 'http://s017.radikal.ru/i413/1301/a2/1eed98e86295.png'
        elif team == 'Bolton Wanderers':
			gap = '                  '
			image = 'http://images.all-free-download.com/images/graphicthumb/bolton_wanderers_89606.jpg'
        elif team == 'Milton Keynes Dons':
			gap = '              '
			image = 'http://s019.radikal.ru/i613/1301/71/290b11408b23.png'
        elif team == 'Swindon Town':
			gap = '                        '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424258908_fc-swindon-town.png'
        elif team == 'Chesterfield':
			gap = '                            '
			image = 'http://futhead.cursecdn.com/static/img/15/clubs_large/1924.png'
        elif team == 'Fleetwood Town':
			gap = '                    '
			image = 'http://s019.radikal.ru/i610/1303/a6/6d38e456e151.png'
        elif team == 'Northampton Town':
			gap = '              '
			image = 'http://www.fm-base.co.uk/forum/attachments/football-manager-2014-manager-stories/568102d1398805400-northampton-town-fc-ntfc-club-logo.png'
        elif team == 'Oxford United':
			gap = '                          '
			image = 'http://s017.radikal.ru/i404/1303/b1/bac792eac719.png'
        elif team == 'Bradford City':
			gap = '                           '
			image = 'http://s020.radikal.ru/i713/1302/75/c5e4f6a092cc.png'
        elif team == 'Port Vale':
			gap = '                                   '
			image = 'http://s08.radikal.ru/i181/1303/9e/df52ec2736ee.png'
        elif team == 'Rochdale':
			gap = '                                  '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/1955.png'
        elif team == 'Coventry City':
			gap = '                          '
			image = 'http://images.all-free-download.com/images/graphicthumb/coventry_city_89611.jpg'
        elif team == 'Sheffield United':
			gap = '                      '
			image = 'http://images.all-free-download.com/images/graphicthumb/sheffield_united_91723.jpg'
        elif team == 'Shrewsbury Town':
			gap = '                 '
			image = 'http://s019.radikal.ru/i623/1302/a6/a7a0d8925f45.png'
        elif team == 'AFC Wimbledon':
			gap = '                     '
			image = 'http://s020.radikal.ru/i718/1302/7d/cf79728da54e.png'
        elif team == 'Bristol Rovers':
			gap = '                         '
			image = 'http://s53.radikal.ru/i140/1302/28/745dee7c958b.png'
        elif team == 'Southend United':
			gap = '                   '
			image = 'http://s020.radikal.ru/i716/1303/7c/6a03145306cf.png'
        elif team == 'Charlton Athletic':
			gap = '                    '
			image = 'http://images.all-free-download.com/images/graphicthumb/charlton_athletic_91711.jpg'
        elif team == 'Oldham Athletic':
			gap = '                     '
			image = 'http://s001.radikal.ru/i195/1302/4a/b61c6d79aebc.png'
        elif team == 'Luton Town':
			gap = '                            '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/1923.png'
        elif team == 'Blackpool':
			gap = '                                '
			image = 'http://images.all-free-download.com/images/graphicthumb/blackpool_fc_91707.jpg'
        elif team == 'Grimsby Town':
			gap = '                        '
			image = 'http://www.futbol24.com/upload/team/England/Grimsby-Town.png'
        elif team == 'Yeovil Town':
			gap = '                            '
			image = 'http://s51.radikal.ru/i133/1302/80/0d9438a6c1f2.png'
        elif team == 'Accrington Stanley':
			gap = '                '
			image = 'https://pbs.twimg.com/profile_images/598068430173032448/rxBIIHgq.png'
        elif team == 'Mansfield Town':
			gap = '                     '
			image = 'http://futhead.cursecdn.com/static/img/14/clubs/1940.png'
        elif team == 'Crewe Alexandra':
			gap = '                    '
			image = 'http://s020.radikal.ru/i703/1301/35/76d73ccd1304.png'
        elif team == 'Crawley Town':
			gap = '                          '
			image = 'http://s017.radikal.ru/i433/1301/63/089bcc6eb033.png'
        elif team == 'Barnet':
			gap = '                                        '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/135.png'
        elif team == 'Cambridge United':
			gap = '                  '
			image = 'http://megaicons.net/static/img/icons_sizes/257/622/256/cambridge-united-icon.png'
        elif team == 'Carlisle United':
			gap = '                        '
			image = 'http://s019.radikal.ru/i607/1301/9c/8916f0f64322.png'
        elif team == 'Cheltenham Town':
			gap = '                 '
			image = 'http://s005.radikal.ru/i212/1302/b2/b10d1e1a0da3.png'
        elif team == 'Colchester United':
			gap = '                   '
			image = 'http://images.all-free-download.com/images/graphicthumb/colchester_united_91712.jpg'
        elif team == 'Hartlepool United':
			gap = '                    '
			image = 'http://s019.radikal.ru/i633/1301/95/5d69de7b37d0.png'
        elif team == 'Leyton Orient':
			gap = '                           '
			image = 'http://s019.radikal.ru/i626/1301/0d/09d5892497b5.png'
        elif team == 'Portsmouth':
			gap = '                              '
			image = 'http://images.all-free-download.com/images/graphicthumb/portsmouth_fc_89631.jpg'
        elif team == 'Doncaster Rovers':
			gap = '                    '
			image = 'http://futhead.cursecdn.com/static//img/14/clubs/142.png'
        elif team == 'Newport County AFC':
			gap = '             '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/112254.png'
        elif team == 'Stevenage':
			gap = '                                 '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/361.png'
        elif team == 'Wycombe Wanderers':
			gap = '            '
			image = 'http://s019.radikal.ru/i614/1303/75/8b5464994d08.png'
        elif team == 'Exeter City':
			gap = '                                 '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/143.png'
        elif team == 'Morecambe':
			gap = '                               '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/357.png'
        elif team == 'Notts County':
			gap = '                            '
			image = 'http://s45.radikal.ru/i107/1302/df/ffe6a93b7048.png'
        elif team == 'Plymouth Argyle':
			gap = '                       '
			image = 'http://images.all-free-download.com/images/graphicthumb/plymouth_argyle_91719.jpg'
        elif team == 'Raith Rovers':
			gap = '                           '
			image = 'http://www.futbol24.com/upload/team/Scotland/Raith-Rovers.png'
        elif team == 'Dunfermline Athletic':
			gap = '            '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415192222_fc-dunfermline-athletic.png'
        elif team == 'Hibernian':
			gap = '                                '
			image = 'http://s019.radikal.ru/i601/1302/32/ddfaeba15d3b.png'
        elif team == 'Dundee United':
			gap = '                       '
			image = 'http://s019.radikal.ru/i619/1302/45/89c176826ee0.png'
        elif team == 'Morton':
			gap = '                                     '
			image = 'http://www.futbol24.com/upload/team/Scotland/Greenock-Morton.png'
        elif team == 'Queen Of The South':
			gap = '             '
			image = 'http://www.futbol24.com/upload/team/Scotland/Queen-of-the-South.png'
        elif team == 'St Mirren':
			gap = '                                  '
			image = 'http://www.futbol24.com/upload/team/Scotland/St-Mirren.png'
        elif team == 'Dumbarton':
			gap = '                              '
			image = 'http://www.futbol24.com/upload/team/Scotland/Dumbarton-FC.png'
        elif team == 'Falkirk':
			gap = '                                       '
			image = 'http://www.futbol24.com/upload/team/Scotland/Falkirk-FC.png'
        elif team == 'Ayr United':
			gap = '                               '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415189232_fc-ayr-united.png'
        elif team == 'Livingston':
			gap = '                               '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415188763_fc-livingston.png'
        elif team == 'Alloa Athletic':
			gap = '                          '
			image = 'http://www.futbol24.com/upload/team/Scotland/Alloa-Athletic.png'
        elif team == 'Airdrieonians':
			gap = '                          '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415191003_fc-airdrieonians.png'
        elif team == 'Brechin City':
			gap = '                            '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415191956_fc-brechin-city.png'
        elif team == 'Albion Rovers':
			gap = '                         '
			image = 'http://www.futbol24.com/upload/team/Scotland/Albion-Rovers.png'
        elif team == 'East Fife':
			gap = '                                   '
			image = 'http://www.futbol24.com/upload/team/Scotland/East-Fife.png'
        elif team == 'Stenhousemuir':
			gap = '                       '
			image = 'http://www.futbol24.com/upload/team/Scotland/Stenhousemuir-FC.png'
        elif team == 'Queen\'s Park':
			gap = '                           '
			image = 'http://www.futbol24.com/upload/team/Scotland/Queens-Park-FC.png'
        elif team == 'Stranraer':
			gap = '                                  '
			image = 'http://www.futbol24.com/upload/team/Scotland/Stranraer-FC.png'
        elif team == 'Peterhead':
			gap = '                               '
			image = 'http://www.futbol24.com/upload/team/Scotland/Peterhead-FC.png'
        elif team == 'Annan Athletic':
			gap = '                      '
			image = 'http://www.futbol24.com/upload/team/Scotland/Annan-Athletic.png'
        elif team == 'Forfar Athletic':
			gap = '                       '
			image = 'http://www.futbol24.com/upload/team/Scotland/Forfar-Athletic.png'
        elif team == 'Clyde':
			gap = '                                       '
			image = 'http://www.futbol24.com/upload/team/Scotland/Clyde-FC.png'
        elif team == 'Elgin City':
			gap = '                                '
			image = 'http://www.futbol24.com/upload/team/Scotland/Elgin-City.png'
        elif team == 'Arbroath':
			gap = '                                 '
			image = 'http://www.futbol24.com/upload/team/Scotland/Arbroath-FC.png'
        elif team == 'Berwick Rangers':
			gap = '                  '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415189705_fc-berwick-rangers.png'
        elif team == 'Edinburgh City':
			gap = '                      '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415189899_fc-edinburgh-city.png'
        elif team == 'Stirling Albion':
			gap = '                        '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415188166_fc-stirling-albion.png'
        elif team == 'Montrose':
			gap = '                                '
			image = 'http://www.futbol24.com/upload/team/Scotland/Montrose-FC.png'
        elif team == 'Cowdenbeath':
			gap = '                       '
			image = 'http://www.futbol24.com/upload/team/Scotland/Cowdenbeath.png'
        elif team == 'Dagenham & Redbridge':
			gap = '      '
			image = 'http://www.futbol24.com/upload/team/England/Dagenham--Red.png'
        elif team == 'Gateshead':
			gap = '                              '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424537057_gateshead-fc.png'
        elif team == 'Lincoln City':
			gap = '                            '
			image = 'http://www.futbol24.com/upload/team/England/Lincoln-City.png'
        elif team == 'Solihull Moors':
			gap = '                       '
			image = 'http://www.futbol24.com/upload/team/England/Solihull-Moors.png'
        elif team == 'Macclesfield Town':
			gap = '               '
			image = 'http://www.futbol24.com/upload/team/England/Macclesfield.png'
        elif team == 'Tranmere Rovers':
			gap = '                   '
			image = 'http://www.futbol24.com/upload/team/England/Tranmere-Rovers.png'
        elif team == 'Eastleigh':
			gap = '                                 '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424535623_fc-eastleigh.png'
        elif team == 'Barrow':
			gap = '                                     '
			image = 'http://www.futbol24.com/upload/team/England/Barrow-AFC.png'
        elif team == 'Boreham Wood':
			gap = '                      '
			image = 'http://www.swindon-town-fc.co.uk/images/Badges/3D/180/Boreham%20Wood.png'
        elif team == 'Maidstone Utd':
			gap = '                      '
			image = 'http://www.futbol24.com/upload/team/England/Maidstone-United.png'
        elif team == 'York City':
			gap = '                                '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424289128_fc-york-city.png'
        elif team == 'Braintree Town':
			gap = '                     '
			image = 'http://www.futbol24.com/upload/team/England/Braintree-Town.png'
        elif team == 'Dover':
			gap = '                                      '
			image = 'http://www.futbol24.com/upload/team/England/Dover-Athletic.png'
        elif team == 'North Ferriby Utd':
			gap = '                  '
			image = 'http://fansonline.net/images/hullcity/northferriby.jpg'
        elif team == 'Wrexham':
			gap = '                                '
			image = 'http://www.futbol24.com/upload/team/England/Wrexham-FC.png'
        elif team == 'Guiseley':
			gap = '                                 '
			image = 'http://www.futbol24.com/upload/team/England/Guiseley-AFC.png'
        elif team == 'Aldershot Town':
			gap = '                    '
			image = 'http://www.futbol24.com/upload/team/England/Aldershot-Town.png'
        elif team == 'Forest Green Rovers':
			gap = '             '
			image = 'https://www.venuetoolbox.com/forestgreenrovers/DMS/fgr_logo_green_300dpi.png'
        elif team == 'Sutton United':
			gap = '                         '
			image = 'http://www.futbol24.com/upload/team/England/Sutton-United.png'
        elif team == 'Woking':
			gap = '                                   '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424538334_fc-woking.png'
        elif team == 'Bromley':
			gap = '                                  '
			image = 'http://www.futbol24.com/upload/team/England/Bromley-FC.png'
        elif team == 'Torquay United':
			gap = '                     '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424538399_fc-torquay-united.png'
        elif team == 'Chester FC':
			gap = '                             '
			image = 'http://i2.chesterchronicle.co.uk/incoming/article5121522.ece/ALTERNATES/s615/chester-fc-logo-image-3-730161524.jpg'
        elif team == 'Southport':
			gap = '                                '
			image = 'http://soccerlogo.net/uploads/posts/2015-02/1424535938_fc-southport.png'
        elif team == 'Alaves':
			gap = '                                     '
			image = 'http://www.futbol24.com/upload/team/Spain/Deportivo-Alaves.png'
        elif team == 'Athletic Bilbao':
			gap = '                '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410534572_fc-athletic-bilbao-256.png'
        elif team == 'Atletico Madrid':
			gap = '                     '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410535764_fc-atletico-madrid-256.png'
        elif team == 'Barcelona':
			gap = '                               '
			image = 'http://images.all-free-download.com/images/graphiclarge/fc_barcelona_101029.jpg'
        elif team == 'Celta Vigo':
			gap = '                               '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410856827_fc-villarreal-256.png'
        elif team == 'Deportivo La Coruna':
			gap = '            '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410857432_fc-deportivo-la-coruna-256.png'
        elif team == 'Eibar':
			gap = '                                         '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410857092_fc-eibar-256.png'
        elif team == 'Espanyol':
			gap = '                                 '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410854906_fc-espanyol-256.png'
        elif team == 'Granada':
			gap = '                                  '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410856595_fc-granada-256.png'
        elif team == 'Las Palmas':
			gap = '                           '
			image = 'http://www.megaicons.net/static/img/icons_sizes/257/1552/256/ud-las-palmas-icon.png'
        elif team == 'Leganes':
			gap = '                                '
			image = 'http://www.futbol24.com/upload/team/Spain/CD-Leganes.png'
        elif team == 'Malaga':
			gap = '                                   '
			image = 'http://megaicons.net/static/img/icons_sizes/257/1552/256/malaga-cf-icon.png'
        elif team == 'Osasuna':
			gap = '                                  '
			image = 'http://1.bp.blogspot.com/-dYDeQG4ttrc/Tzu11GGHF8I/AAAAAAAAAM0/kFzhraTl1wE/s1600/osasuna%2Blogo.png'
        elif team == 'Real Betis':
			gap = '                                '
			image = 'http://megaicons.net/static/img/icons_sizes/257/1552/256/real-betis-icon.png'
        elif team == 'Real Madrid':
			gap = '                            '
			image = 'http://megaicons.net/static/img/icons_sizes/257/1552/256/real-madrid-icon.png'
        elif team == 'Real Sociedad':
			gap = '                        '
			image = 'http://megaicons.net/static/img/icons_sizes/257/1552/256/real-sociedad-icon.png'
        elif team == 'Sevilla':
			gap = '                                       '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410855169_fc-sevilla-256.png'
        elif team == 'Sporting Gijon':
			gap = '                        '
			image = 'http://megaicons.net/static/img/icons_sizes/257/1552/256/sporting-gijon-icon.png'
        elif team == 'Valencia':
			gap = '                                  '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410854553_fc-valencia-256.png'
        elif team == 'Villarreal':
			gap = '                                     '
			image = 'http://dota2bestyolo.com/uploads/Villarreal.png'
        elif team == 'Atalanta':
			gap = '                                  '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410466573_fc-atalanta.png'
        elif team == 'Bologna':
			gap = '                                   '
			image = 'http://www.futbol24.com/upload/team/Italy/Bologna-FC.png'
        elif team == 'Cagliari':
			gap = '                                     '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410466463_fc-cagliari.png'
        elif team == 'Chievo':
			gap = '                                      '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410467329_fc-chievo-verona.png'
        elif team == 'Crotone':
			gap = '                                    '
			image = 'http://www.futbol24.com/upload/team/Italy/FC-Crotone.png'
        elif team == 'Empoli':
			gap = '                                       '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410465261_fc-empoli.png'
        elif team == 'Fiorentina':
			gap = '                                    '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410466605_fc-fiorentina.png'
        elif team == 'Genoa':
			gap = '                                        '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410466764_fc-genoa.png'
        elif team == 'Inter Milan':
			gap = '                                '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410466849_fc-inter_milan.png'
        elif team == 'Juventus':
			gap = '                                 '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410465737_fc-juventus.png'
        elif team == 'Lazio':
			gap = '                                         '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410467022_fc-lazio.png'
        elif team == 'AC Milan':
			gap = '                                  '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410467610_fc-ac-milan.png'
        elif team == 'Napoli':
			gap = '                                          '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410467265_fc-ssc-napoli.png'
        elif team == 'Palermo':
			gap = '                                   '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410467775_fc-palermo.png'
        elif team == 'Pescara':
			gap = '                                    '
			image = 'http://www.futbol24.com/upload/team/Italy/Pescara-Calcio.png'
        elif team == 'Roma':
			gap = '                                        '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410465414_fc-roma.png'
        elif team == 'Sampdoria':
			gap = '                                '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410466220_fc-sampdoria.png'
        elif team == 'Sassuolo':
			gap = '                                  '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410466918_fc-sassuolo.png'
        elif team == 'Torino':
			gap = '                                       '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410466363_fc-torino.png'
        elif team == 'Udinese':
			gap = '                                    '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410465864_fc-udinese.png'
        elif team == 'Bayer Leverkusen':
			gap = '                 '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410883734_fc-bayer-leverkusen-256.png'
        elif team == 'Mainz':
			gap = '                                       '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413536846_fc-mainz-05.png'
        elif team == 'FC Ingolstadt 04':
			gap = '                   '
			image = 'https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/FC_Ingolstadt_04_logo.svg/926px-FC_Ingolstadt_04_logo.svg.png'
        elif team == 'SV Darmstadt 98':
			gap = '                   '
			image = 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Darmstadt_98_football_club_new_logo_2015.png'
        elif team == 'Eintracht Frankfurt':
			gap = '                '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413537689_fc-eintracht-frankfurt.png'
        elif team == 'Werder Bremen':
			gap = '                      '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413536147_fc-werder-bremen.png'
        elif team == 'Hoffenheim':
			gap = '                             '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413537050_fc-hoffenheim.png'
        elif team == 'FC Augsburg':
			gap = '                            '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413537782_fc-augsburg.png'
        elif team == 'Hamburg':
			gap = '                                 '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413538097_fc-hamburger-sv.png'
        elif team == 'Hertha Berlin':
			gap = '                         '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413536747_fc-hertha-berlin.png'
        elif team == 'RB Leipzig':
			gap = '                              '
			image = 'http://www.futbol24.com/upload/team/Germany/RB-Leipzig.png'
        elif team == 'Borussia Dortmund':
			gap = '                                     '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413536456_fc-borussia-dortmund.png'
        elif team == 'Cologne':
			gap = '                                  '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413537491_fc-cologne.png'
        elif team == 'SC Freiburg':
			gap = '                            '
			image = 'http://images.all-free-download.com/images/graphicthumb/karlsruher_sc_92040.jpg'
        elif team == 'Bayern Munich':
			gap = '                       '
			image = 'http://managerfdf.com/images/escudos/43.png'
        elif team == 'Schalke':
			gap = '                                      '
			image = 'http://images.all-free-download.com/images/graphicthumb/schalke_04_92042.jpg'
        elif team == 'Borussia Monchengladbach':
			gap = ''
			image = 'http://images.all-free-download.com/images/graphicthumb/borussia_monchengladbach_92033.jpg'
        elif team == 'Wolfsburg':
			gap = '                                 '
			image = 'http://images.all-free-download.com/images/graphicthumb/vfl_wolfsburg_92046.jpg'
        elif team == 'Angers':
			gap = '                                   '
			image = 'http://images.all-free-download.com/images/graphicthumb/sco_angers_91773.jpg'
        elif team == 'Bastia':
			gap = '                                     '
			image = 'http://images.all-free-download.com/images/graphicthumb/sc_bastia_91774.jpg'
        elif team == 'Bordeaux':
			gap = '                                       '
			image = 'http://images.all-free-download.com/images/graphicthumb/girordins_de_bordeaux_91762.jpg'
        elif team == 'Caen':
			gap = '                                       '
			image = 'http://images.all-free-download.com/images/graphicthumb/sm_caen_91775.jpg'
        elif team == 'Dijon':
			gap = '                                       '
			image = 'http://www.futbol24.com/upload/team/France/Dijon-FCO.png'
        elif team == 'Guingamp':
			gap = '                             '
			image = 'http://images.all-free-download.com/images/graphicthumb/en_avant_guingamp_91754.jpg'
        elif team == 'Lille':
			gap = '                                         '
			image = 'http://images.all-free-download.com/images/graphicthumb/lille_osc_91763.jpg'
        elif team == 'Lorient':
			gap = '                                    '
			image = 'http://images.all-free-download.com/images/graphicthumb/fc_lorient_91756.jpg'
        elif team == 'Lyon':
			gap = '                                        '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413538266_fc-lyon.png'
        elif team == 'Marseille':
			gap = '                                     '
			image = 'http://images.all-free-download.com/images/graphicthumb/olumpique_de_marseille_91766.jpg'
        elif team == 'Metz':
			gap = '                                       '
			image = 'http://images.all-free-download.com/images/graphicthumb/fc_metz_91757.jpg'
        elif team == 'Monaco':
			gap = '                               '
			image = 'http://images.all-free-download.com/images/graphicthumb/monaco_93386.jpg'
        elif team == 'Montpellier':
			gap = '                           '
			image = 'http://images.all-free-download.com/images/graphicthumb/montpellier_91764.jpg'
        elif team == 'Nancy':
			gap = '                                     '
			image = 'http://images.all-free-download.com/images/graphicthumb/as_nancy_lorraine_91750.jpg'
        elif team == 'Nantes':
			gap = '                                   '
			image = 'http://images.all-free-download.com/images/graphicthumb/fc_nantes_atlantique_91758.jpg'
        elif team == 'Nice':
			gap = '                                        '
			image = 'http://images.all-free-download.com/images/graphicthumb/ogc_nice_91765.jpg'
        elif team == 'Paris Saint-Germain':
			gap = '            '
			image = 'http://images.all-free-download.com/images/graphicthumb/paris_saint_germain_91769.jpg'
        elif team == 'Rennes':
			gap = '                                   '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413538522_fc-rennes.png'
        elif team == 'St Etienne':
			gap = '                                '
			image = 'http://images.all-free-download.com/images/graphicthumb/as_saint_etienne_91751.jpg'
        elif team == 'Toulouse':
			gap = '                              '
			image = 'http://images.all-free-download.com/images/graphicthumb/toulouse_fc_91780.jpg'
        elif team == 'Feyenoord':
			gap = '                              '
			image = 'http://images.all-free-download.com/images/graphicthumb/feyenoord_91246.jpg'
        elif team == 'Vitesse Arnhem':
			gap = '                    '
			image = 'http://images.all-free-download.com/images/graphicthumb/vitesse_arnhem_91255.jpg'
        elif team == 'ADO Den Haag':
			gap = '                      '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413562336_fc-ado-den-haag.png'
        elif team == 'Ajax':
			gap = '                                             '
			image = 'http://images.all-free-download.com/images/graphicthumb/ajax_91238.jpg'
        elif team == 'Excelsior':
			gap = '                                 '
			image = 'http://images.all-free-download.com/images/graphicthumb/excelsior_91241.jpg'
        elif team == 'PSV Eindhoven':
			gap = '                      '
			image = 'http://images.all-free-download.com/images/graphicthumb/psv_eindhoven_91252.jpg'
        elif team == 'Heerenveen':
			gap = '                            '
			image = 'http://images.all-free-download.com/images/graphicthumb/heerenveen_91247.jpg'
        elif team == 'AZ Alkmaar':
			gap = '                          '
			image = 'http://images.all-free-download.com/images/graphicthumb/az_alkmaar_91239.jpg'
        elif team == 'Heracles Almelo':
			gap = '                     '
			image = 'http://images.all-free-download.com/images/graphicthumb/heracles_almelo_91248.jpg'
        elif team == 'PEC Zwolle':
			gap = '                            '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413563096_fc-pec-zwolle.png'
        elif team == 'NEC Nijmegen':
			gap = '                       '
			image = 'http://images.all-free-download.com/images/graphicthumb/nec_nijmegen_91250.jpg'
        elif team == 'Roda JC Kerk':
			gap = '                        '
			image = 'http://images.all-free-download.com/images/graphicthumb/roda_jc_kerkrade_91253.jpg'
        elif team == 'FC Twente':
			gap = '                              '
			image = 'http://images.all-free-download.com/images/graphicthumb/fc_twente_enschede_91244.jpg'
        elif team == 'FC Utrecht':
			gap = '                               '
			image = 'http://images.all-free-download.com/images/graphicthumb/fc_utrecht_91245.jpg'
        elif team == 'Sparta Rotterdam':
			gap = '                   '
			image = 'http://images.all-free-download.com/images/graphicthumb/sparta_rotterdam_91254.jpg'
        elif team == 'Willem II':
			gap = '                                  '
			image = 'http://images.all-free-download.com/images/graphicthumb/willem_ii_91257.jpg'
        elif team == 'Go Ahead Eagles':
			gap = '                    '
			image = 'http://soccerlogo.net/uploads/posts/2014-10/1413562905_fc-go-ahead-eagles.png'
        elif team == 'Groningen':
			gap = '                                      '
			image = 'http://images.all-free-download.com/images/graphicthumb/fc_groningen_91242.jpg'
        elif team == 'Arouca':
			gap = '                                     '
			image = 'http://futhead.cursecdn.com/static/img/16/clubs/112513.png'
        elif team == 'Belenenses':
			gap = '                                 '
			image = 'http://images.all-free-download.com/images/graphicthumb/cf_belenenses_98318.jpg'
        elif team == 'Benfica':
			gap = '                                    '
			image = 'http://images.all-free-download.com/images/graphicthumb/benfica_98316.jpg'
        elif team == 'Boavista':
			gap = '                                  '
			image = 'http://images.all-free-download.com/images/graphicthumb/boavista_98317.jpg'
        elif team == 'Nacional':
			gap = '                                 '
			image = 'http://images.all-free-download.com/images/graphicthumb/nacional_funchal_98323.jpg'
        elif team == 'Estoril':
			gap = '                                      '
			image = 'http://s57.radikal.ru/i156/1211/68/34385307d85b.png'
        elif team == 'FC Porto':
			gap = '                                  '
			image = 'http://images.all-free-download.com/images/graphicthumb/fc_porto_98320.jpg'
        elif team == 'Feirense':
			gap = '                                   '
			image = 'http://www.futbol24.com/upload/team/Brazil/Feirense-BA.png'
        elif team == 'GD Chaves':
			gap = '                               '
			image = 'http://www.futbol24.com/upload/team/Portugal/GD-Chaves.png'
        elif team == 'Maritimo':
			gap = '                                 '
			image = 'http://images.all-free-download.com/images/graphicthumb/maritimo_funchal_98322.jpg'
        elif team == 'Moreirense':
			gap = '                             '
			image = 'http://futhead.cursecdn.com/static/img/15/clubs_large/1900.png'
        elif team == 'Pacos Ferreira':
			gap = '                        '
			image = 'http://images.all-free-download.com/images/graphicthumb/pacos_de_ferreira_98325.jpg'
        elif team == 'Rio Ave':
			gap = '                                     '
			image = 'http://s019.radikal.ru/i601/1211/98/41e68d6f7cba.png'
        elif team == 'Braga':
			gap = '                                            '
			image = 'http://images.all-free-download.com/images/graphicthumb/sporting_braga_98327.jpg'
        elif team == 'Sporting Lisbon':
			gap = '                                   '
			image = 'http://images.all-free-download.com/images/graphicthumb/sporting_cp_lisbon_98328.jpg'
        elif team == 'Tondela':
			gap = '                                   '
			image = 'http://static.memrise.com/uploads/things/images/65974942_150718_1927_21.png'
        elif team == 'Vitoria de Guimaraes':
			gap = '            '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415179358_fc-vitoria-de-guimaraes.png'
        elif team == 'Vitoria Futebol Clube Setubal':
			gap = ''
			image = 'http://www.futbol24.com/upload/team/Portugal/Vitoria-Setubal.png'
        elif team == 'Shakhtar Donetsk':
			gap = '                '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410887586_fc-shakhtar-donetsk-256.png'
        elif team == 'Malmo FF':
			gap = '                              '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410882361_fc-malmo-ff-256.png'
        elif team == 'CSKA Moscow':
			gap = '                    '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410886570_fc-cska-moscow-256.png'
        elif team == 'Galatasaray':
			gap = '                           '
			image = 'http://megaicons.net/static/img/icons_sizes/252/611/256/galatasaray-icon.png'
        elif team == 'Astana':
			gap = '                                    '
			image = 'http://www.fcaktobe-fans.kz/logo/2014/Astana.png'
        elif team == 'BATE Borisov':
			gap = '                         '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410887865_fc-bate-borisov-256.png'
        elif team == 'Olympiakos FC':
			gap = '                       '
			image = 'https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/Olympiacos_FC_logo.svg/635px-Olympiacos_FC_logo.svg.png'
        elif team == 'Dynamo Kiev':
			gap = '                          '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410894624_fc-dynamo-kyiv-256.png'
        elif team == 'Dinamo Zagreb':
			gap = '                       '
			image = 'http://soccerlogo.net/uploads/posts/2014-09/1410889673_fc-dinamo-zagreb-256.png'
        elif team == 'Maccabi Tel Aviv':
			gap = '                  '
			image = 'http://soccerlogo.net/uploads/posts/2014-11/1415121691_fk-maccabi-tel-aviv.png'
        elif team == 'Zenit St. Petersburg':
			gap = '             '
			image = 'http://www.futbol24.com/upload/team/Russia/Zenit.png'
        elif team == 'AA Gent (Bel)':
			gap = '                        '
			image = 'http://www.futbol24.com/upload/team/Belgium/KAA-Gent.png'
        pos_space = len((pos + ' - ')) * ' '
        spacer_pl = '        '
        spacer_w = '        '
        spacer_d = '        '
        spacer_l = '        '
        spacer_f = '        '
        spacer_a = '        '
        if int(pl)>=100:
            spacer_pl = '     '
        elif int(pl)>=10:
            spacer_pl = '      '
        if int(w)>=100:
            spacer_w = '     '
        if int(w)>=10:
            spacer_w = '      '
        if int(d)>=100:
            spacer_d = '     '
        elif int(d)>=10:
            spacer_d = '      '
        elif int(l)>=10:
            spacer_l = '     '
        if int(l)>=10:
            spacer_l = '      '
        if int(f)>=100:
            spacer_f = '     '
        elif int(f)>=10:
            spacer_f = '      '
        if int(a)>=100:
            spacer_a = '     '
        elif int(a)>=10:
            spacer_a = '      '
        addDirFolder(team+gap+pos_space+pl+spacer_pl+w+spacer_w+d+spacer_d+l+spacer_l+f+spacer_f+a+spacer_a+pts,(Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS8/cz0=')+team).replace(' ','+'),401,image,FANART,'')



def Football_Highlights():

    addDirFolder('Footy Tube','http://www.footytube.com/leagues',413,ICON,FANART,'')
    addDirFolder('Latest','http://www.fullmatchesandshows.com',408,'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png',FANART,'')
    addDirFolder('Shows','http://www.fullmatchesandshows.com/category/show/',408,'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png',FANART,'')
    addDirFolder('Premier League','http://www.fullmatchesandshows.com/premier-league/',408,'https://footballseasons.files.wordpress.com/2013/05/premier-league.png',FANART,'')
    addDirFolder('La Liga','http://www.fullmatchesandshows.com/la-liga/',408,'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png',FANART,'')
    addDirFolder('Bundesliga','http://www.fullmatchesandshows.com/bundesliga/',408,'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg',FANART,'')
    addDirFolder('Champions League','http://www.fullmatchesandshows.com/champions-league/',408,'http://www.ecursuri.ro/images/teste/test-champions-league.jpg',FANART,'')
    addDirFolder('Serie A','http://www.fullmatchesandshows.com/category/serie-a/',408,'http://files.jcriccione.it/200000223-2484526782/serie%20a.png',FANART,'')
    addDirFolder('Ligue 1','http://www.fullmatchesandshows.com/category/ligue-1/',408,'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg',FANART,'')

def footytube(url):
    HTML = OPEN_URL(url)
    block_and_name = re.compile('<div class="headline_xlrg color_dgray"><img align="absmiddle" height="22" src="(.+?)">(.+?)</div>').findall(HTML)
    for img,name in block_and_name:
        addDirFolder(name,'',414,footy+img,FANART,'')
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

		
def footytube_leagues(name):
    url = 'http://www.footytube.com/leagues'
    check = name
    HTML = OPEN_URL(url)
    block_and_name = re.compile('<div class="headline_xlrg color_dgray"><img align="absmiddle" height="22" src="(.+?)">'+name+'</div>(.+?)<div style="margin-bottom: 15px">',re.DOTALL).findall(HTML)
    for img,block in block_and_name:
        leagues = re.compile('<div>.+?<a href="(.+?)" class="standard_link">(.+?)</a><br>.+?<span class="text_xsml">(.+?)</span>.+?</div>',re.DOTALL).findall(str(block))
        for url,name,qty in leagues:
            addDirFolder(name + ' - ' + qty,footy+url,415,ICON,FANART,'')
        else:
            pass		
			
def footytube_teams(url):
    HTML = OPEN_URL(url)
    match = re.compile('<div class=".+?" style = ".+?"><a href="(.+?)" class=".+?" >(.+?)</a></div>').findall(HTML)
    for url,name in match:
        addDirFolder(name,footy+url,416,ICON,FANART,'')
        	
def footytube_videos(url):
    HTML = OPEN_URL(url)
    match = re.compile(' <div class="thumboverlay"> .+?<div><a href="(.+?)".+?<img src="(.+?)" width="165px" height="97px" /></a></div>.+?<div class="vid_title".+?class="standard_link">(.+?)</a><div class="vid_info">(.+?)</div>',re.DOTALL).findall(HTML)
    for url,img,name,age in match:
        addDir(name + ' - ' + age, footy+url,417,img,FANART,'')

		
def footytube_frame(url):
    HTML = OPEN_URL(url)
    match = re.compile('<iframe src="(.+?)" width=').findall(HTML)
    for url in match:
        url = footy + url
        get_footytube_PLAYlink(url)	
    match_youtube = re.compile('<iframe id="ft_player" width="100%" height="100%" src="http://www.youtube.com/embed/(.+?)?rel=0&autoplay=1&enablejsapi=1" frameborder="0" allowfullscreen></iframe>').findall(HTML)
    for url in match_youtube:
        yt.PlayVideo(url)

		
def get_footytube_PLAYlink(url):
    HTML = OPEN_URL(url)
    match_youtube = re.compile('<iframe width="560" height="315" src="https://www.youtube.com/embed/(.+?)" frameborder="0" allowfullscreen>').findall(HTML)
    for url in match_youtube:
        yt.PlayVideo(url)
    match = re.compile('<script data-config="(.+?)" data-css=".+?" data-height="100%" data-width="100%" src=".+?" type="text/javascript"></script>').findall(HTML)
    for playlink in match:
        if 'div' in playlink:
            pass
        else:
            Playlink = (playlink).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
            Resolve('http:'+Playlink)
		
		
def Get_the_rows(url,iconimage):
    HTML = OPEN_URL(url)
    match2 = re.compile('<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)".+?"entry-thumb" src="(.+?)"').findall(HTML)
    for url,name,img in match2:
        if 'Full Match' in name:
    	    Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            addDirFolder(Name,url,407,img,'','')
        else:
    	    Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            addDir(Name,url,402,img,'','')
    Next = re.compile('<span class="current">.+?</span><a href="(.+?)" class="page" title=".+?">(.+?)</a>').findall(HTML)
    for url,name in Next:
        addDirFolder('NEXT PAGE',url,401,iconimage,FANART,'')
		
def get_All_Rows(url,iconimage):
    HTML = OPEN_URL(url)
    block = re.compile('<div class="td-block-span6">(.+?)<div class="td-pb-span4 td-main-sidebar">',re.DOTALL).findall(HTML)
    match2 = re.compile('<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)".+?"entry-thumb" src="(.+?)"').findall(str(block))
    for url,name,img in match2:
        if 'Full Match' in name:
    	    Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            addDirFolder(Name,url,407,img,'','')
        else:
    	    Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            addDir(Name,url,402,img,'','')
    Next = re.compile('<span class="current">.+?</span><a href="(.+?)" class="page" title=".+?">(.+?)</a>').findall(HTML)
    for url,name in Next:
        addDirFolder('NEXT PAGE',url,401,iconimage,FANART,'')
    if len(match2)<=0:
        addDirFolder('No Replays available sorry',url,401,iconimage,FANART,'')


def get_Multi_Links(url,iconimage):
    addDir('Extended Highlights',url,402,iconimage,FANART,'')
    HTML = OPEN_URL(url)
    match = re.compile('<link href=".+?" rel="stylesheet" type="text/css"><li tabindex="0" class="button_style" id=".+?"><a href="(.+?)"><div class="acp_title">(.+?)</div></a></li>').findall(HTML)
    for url2,name in match:
        url = url+url2
        name = (name).replace('HL English','English Highlights')
        addDir(name,url,402,iconimage,FANART,'')
		
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

	
def TextBoxes(heading,announce):
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
      try: f=open(announce); text=f.read()
      except: text=announce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()
  TextBox()


def Resolve(url): 
    play=xbmc.Player()
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

