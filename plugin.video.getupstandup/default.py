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
import urllib2,re,os,base64,xbmc,xbmcplugin,xbmcaddon,xbmcgui,urlparse,urllib
import urlresolver,yt
try:
    import json
except:
    import simplejson as json
from threading import Thread

Dialog = xbmcgui.Dialog()
Decode = base64.decodestring
CAT=Decode('LnBocA==')
BASE = 'http://www.couchtripper.com/forum2/page.php?page=3'
addon_id='plugin.video.getupstandup'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "Get Up - Stand Up"
VERSION = "1.0.1"
dp = xbmcgui.DialogProgress()
ADDON = xbmcaddon.Addon(id=addon_id)
debug = ADDON.getSetting('debug')
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/'+PATH+'/'
favourites = ADDON_DATA + 'favourites'
if not os.path.exists(ADDON_DATA):
    os.makedirs(ADDON_DATA)
if os.path.exists(favourites)==True:
    FAV = open(favourites).read()
else: FAV = []
#if not os.path.exists(favourites):
#    open(favourites,'w+')



ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART         =  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
IMAGES 		=  ART + 'icon.png'
Main 		= 'http://www.watchseries.ac'

def Main_Menu():

    Menu('Stand Up','',10,IMAGES,FANART,'','')
    Menu('Tv Shows','',4,IMAGES,FANART,'','')
    Menu('Movies','',6,IMAGES,FANART,'','')
    Menu('Favourites','',103,IMAGES,FANART,'','')
	
def Stand_up_Menu():
    Menu('Youtube Playlists','',11,IMAGES,FANART,'','')
    Menu('Couch Tripper','',1,IMAGES,FANART,'','')
	
def youtube_lists():
    Menu('Lee Evans','https://www.youtube.com/playlist?list=PLmGADpej_IqYn1peGTM-PlUoNTP6YRmW2',7,IMAGES,FANART,'','')
    Menu('Billy Connolly','https://www.youtube.com/playlist?list=PL-sIpqBXHUeW2SZXro5grac2RRzDZbTdy',7,IMAGES,FANART,'','')
    Menu('Jeff Dunham','https://www.youtube.com/playlist?list=PLVGwpSsVPIyeyhxVdkOIM2xTWLCmzC9ro',7,IMAGES,FANART,'','')
    Menu('Micheal McIntyre','https://www.youtube.com/playlist?list=PLukH15qkkXW3p8qURB8vZBoWNRv9rcjvL',7,IMAGES,FANART,'','')
    Menu('Russell Howard - Wonderbox','https://www.youtube.com/playlist?list=PLc-G9pxRSfWCTX-loZYOFVZH-99WQ40on',7,IMAGES,FANART,'','')
    Menu('Russell Howard - Right Here Right Now','https://www.youtube.com/playlist?list=PLpUoBDdDG_GIilpA71JaApmyC2AGPH58z',7,IMAGES,FANART,'','')
    Menu('Peter Kay','https://www.youtube.com/playlist?list=PLLc_AXLqnRkicIdXYmEfkQJnWq--9rUoM',7,IMAGES,FANART,'','')
    Menu('Franky Boyle','https://www.youtube.com/playlist?list=PLLfOAtDlewmXsYaKE4SImlpM5PQg88-7x',7,IMAGES,FANART,'','')
    Menu('Live at the apollo','https://www.youtube.com/playlist?list=PLSfpk6g1yv1ECV_yExW4JbvfTaMj87ciH',7,IMAGES,FANART,'','')
    Menu('John Richardson','https://www.youtube.com/playlist?list=PLUIO3ZrfeKR2q3nX8JDEPVkdkPzwf1wat',7,IMAGES,FANART,'','')
    Menu('Russell Howard Stand up central','https://www.youtube.com/playlist?list=PL22ZgI9qmtA6sEru_f64dG4ODDdtyi6eC',7,IMAGES,FANART,'','')
    Menu('Al Murray Pub Landlord','https://www.youtube.com/playlist?list=PLqhIkwVbGgsPvxy9Dl2UJSR99_TCSrQ-G',7,IMAGES,FANART,'','')
    Menu('Jimmy Carr','https://www.youtube.com/playlist?list=PLguKsLyN-1VbbhtfWXGYKOIevffZ4NLp7',7,IMAGES,FANART,'','')
    Menu('Hemming Wehn','https://www.youtube.com/playlist?list=PL2HTCtUu6np9g68qlFx-Vb-u0Km8XJ1DJ',7,IMAGES,FANART,'','')
    Menu('Stewart Lee','https://www.youtube.com/playlist?list=PL63YoPP0alkI3vw5NlISsE_BeguO_yFHW',7,IMAGES,FANART,'','')
    Menu('Lee Mack','https://www.youtube.com/playlist?list=PLQaxtOhG2kUeF4CNpPP0fsa4FMePhZee3',7,IMAGES,FANART,'','')
    Menu('David Mitchell','https://www.youtube.com/playlist?list=PLwJQG83FpnCKgYMkhXIZyYLWgaYQQCjOE',7,IMAGES,FANART,'','')
    Menu('James Acaster','https://www.youtube.com/playlist?list=PLY4fDOOF15ePIbftBBlc2y3BcY0VOlQXV',7,IMAGES,FANART,'','')
    Menu('Comedy Central Roasts','https://www.youtube.com/playlist?list=PLIdyfW1oW4yRFsmF6TqiB_4_wjjD2kowB',7,IMAGES,FANART,'','')
    Menu('Def Comedy Jam','https://www.youtube.com/playlist?list=PLq7hdysfg2VY44dxNDJIAcM8IT7srFa0T',7,IMAGES,FANART,'','')
    Menu('John Bishop','https://www.youtube.com/playlist?list=PLYqwECIWbOqUUGot2XO3MlSIN2HEe_KNX',7,IMAGES,FANART,'','')
    Menu('Robin Williams','https://www.youtube.com/playlist?list=PLRhgN48a00wFEidK8LJo6XgDJNwovdbZf',7,IMAGES,FANART,'','')	
    Menu('Eddie Murphy','https://www.youtube.com/playlist?list=PLJbfEvH1D-9cNid901Bzg3k6sKrHhiE2Q',7,IMAGES,FANART,'','')
    Menu('Kevin Hart','https://www.youtube.com/playlist?list=PLXVEZ4buSvJ3rVCuNH_102NR6Ok9QTXW9',7,IMAGES,FANART,'','')
    Menu('Bottom Live','https://www.youtube.com/playlist?list=PLKU3MYHoGMoe1XxX_UItvUfZ5yStn2InB',7,IMAGES,FANART,'','')
    Menu('Martin Lawrence','https://www.youtube.com/playlist?list=PLq7hdysfg2VbbydJSjTreWm72wdSJal-X',7,IMAGES,FANART,'','')
    Menu('Eddie Izzard','https://www.youtube.com/playlist?list=PL3NUTkvcEcP2HViSBKHQbaocflssSXiCr',7,IMAGES,FANART,'','')
    Menu('Jim Davidson','https://www.youtube.com/playlist?list=PLh2UAeVyPH6_iI6lyqGriqqjwHUyQ6pIl',7,IMAGES,FANART,'','')
    Menu('Tim Allen','https://www.youtube.com/playlist?list=PLkhnRzSnbeLvdF1HusC7BmE0W2DE8Vs3W',7,IMAGES,FANART,'','')
    Menu('Jo Brand','https://www.youtube.com/playlist?list=PLR4y5cpLlJoMHAMMsZ1FAi5XCgfuGjHcZ',7,IMAGES,FANART,'','')
    Menu('Katherine Ryan','https://www.youtube.com/playlist?list=PL3OzKtVwVVv0xnaTxdM9qcBOSsfMGSc9D',7,IMAGES,FANART,'','')

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

	
def TV_Shows():
    Menu('Father Ted','http://www.watchseries.ac/serie/father_ted',100,'https://pbs.twimg.com/profile_images/670345562097627137/OgizKymo.jpg','https://images.metadata.sky.com/pd-image/b93f0c08-e986-43a6-9ee2-ce453f1fef29/16-9','','Father Ted')
    Menu('The Inbetweeners','http://www.watchseries.ac/serie/inbetweeners',100,'https://pbs.twimg.com/profile_images/3180357159/c7707e276c04ad6d71c0dedb76c43942.jpeg','https://images.susu.org/unionfilms/films/backgrounds/hd/the-inbetweeners-movie.jpg','','The Inbetweeners')
    Menu('Friends','http://www.watchseries.ac/serie/friends',100,'http://icons.iconseeker.com/png/fullsize/tv-shows/friends-1.png','http://stuffpoint.com/friends/image/84659-friends-friends.jpg','','Friends')
    Menu('Last Man on Earth','http://www.watchseries.ac/serie/the_last_man_on_earth',100,'http://orig11.deviantart.net/7d8f/f/2015/059/5/9/the_last_man_on_earth_by_rest_in_torment-d8jx3s4.png','http://www.wallpapermade.com/images/wallpapers/originals/phil-miller-posing-on-the-armchair-in-the-desert-the-last-man-on-earth-wallpaper-4123.jpg','','The Last Man on Earth')
    Menu('Still Game','http://www.watchseries.ac/serie/still_game',100,'https://i.ytimg.com/vi/O4IvpKFRkgg/hqdefault.jpg','https://ichef.bbci.co.uk/images/ic/1920x1080/p027nv1g.jpg','','Still Game')
    Menu('Chewing the Fat','https://www.youtube.com/playlist?list=PLgcub1spLIcmzkbI9MvfX9FZT8H4cAgN8',7,'https://pbs.twimg.com/profile_images/687812427740655616/WDo7rawL.jpg','https://i.ytimg.com/vi/lCrldZnuGi8/maxresdefault.jpg','','Chewing the Fat')
    Menu('Only Fools and Horses','http://www.watchseries.ac/serie/only_fools_and_horses',100,'http://www.retro36.com/images/product/o/only-fools-and-horses-set-of-4-coasters-256px-256px.jpg','http://res.cloudinary.com/uktv/image/upload/q_80/v1360341877/t9ktxw9sqvfxhbmatyvn.jpg','','Only Fools and Horses')
    Menu('Mock the Week','https://www.youtube.com/playlist?list=PLp5ALmVTEYr2jWLsqAsLApjYrrtVpDq51',7,'https://lh3.googleusercontent.com/proxy/fgiBY4J0OIuAaorbYmwePh3RTlXcgQJy41N15QE7dzFw0W5dyGoWJIC-AggwElPses9u401kawy7CjrIFDzTBn5Fag=w426-h240-n','https://i.ytimg.com/vi/eE5ovCv_QFk/maxresdefault.jpg','','Mock the week')
    Menu('Would I lie to you','https://www.youtube.com/playlist?list=PLE4-InHSpklCGGYMmxosxBqzkb5LLgIUQ',7,'https://i.ytimg.com/vi/iqcl40X88HQ/maxresdefault.jpg','https://fanart.tv/fanart/tv/82548/tvthumb/would-i-lie-to-you-5699e55169b48.jpg','','Would i lie to you')
    Menu('Bad Education','http://www.watchseries.ac/serie/bad_education',100,'https://getpopcorntime.org/wp-content/uploads/thumbnail-for-19291.jpg','https://ichef.bbci.co.uk/images/ic/1920x1080/p01gw09j.jpg','','Bad Education')	
    Menu('School of hard sums','https://www.youtube.com/playlist?list=PLZpinh_mIvOornkMUjfHReeqMDK0Vv5X6',7,'http://www.mathswithgraham.org.uk/wp-content/uploads/2012/05/schoolofhardsums-300x163.jpg','https://i.ytimg.com/vi/LbFbWvGntKY/maxresdefault.jpg','','School of hard sums')	
    Menu('Men Behaving Badly','https://www.youtube.com/playlist?list=PLtXXnONw0GVQ_Y7zQCpZ9E1YB91IaKOl2',7,'https://upload.wikimedia.org/wikipedia/en/b/bf/Men_Behaving_Badly_title_card.jpg','https://ichef.bbci.co.uk/images/ic/1920x1080/p01h8kbk.jpg','','Men Behaving Badly')
    Menu('As yet untitled','https://www.youtube.com/playlist?list=PLIEcCay6vNO9WPztOVNF74mFWDlU2_pjW',7,'https://upload.wikimedia.org/wikipedia/en/3/3f/As_Yet_Untitled.jpg','https://www.comedy.co.uk/images/library/comedies/900x450_eps/a/alan_davies_as_yet_untitled_0307.jpg','','')
    Menu('The Ricky Gervais Show','https://www.youtube.com/playlist?list=PLj-sGZK2R0VkUZo6KdX761v1OLqE2_qRx',7,'https://upload.wikimedia.org/wikipedia/en/1/12/Ricky_Gervais_Show_Season_4_(The_Podfather)_Cover.JPG','http://www.entertainmentwallpaper.com/images/res1920x1080/movie/tv-the-ricky-gervais-show03.jpg','','')
    Menu('The Black Adder','http://www.watchseries.ac/serie/blackadder',100,'http://vignette3.wikia.nocookie.net/blackadder/images/6/60/Simon_Partridge.jpg/revision/latest?cb=20141115181613','http://www.watchseries.ac/serie/blackadder','','The Black Adder')
    Menu('Mr. Bean','http://www.watchseries.ac/serie/mr._bean',100,'http://vignette3.wikia.nocookie.net/uncyclopedia/images/c/cc/Mr-bean.jpg/revision/latest?cb=20090819184827','http://eskipaper.com/images/mr-bean-1.jpg','','Mr. Bean')
    Menu('Fawlty Towers','https://www.youtube.com/playlist?list=PLNW_KNDiLrwPFBSJMWP_i6JSvAD2c3N1l',100,'http://vignette2.wikia.nocookie.net/bbcfawltytowers/images/1/1f/Fawlty_Towers.jpg/revision/latest?cb=20111115153724','http://www.hotel-r.net/im/hotel/it/fawlty-towers-12.jpg','','Fawlty Towers')
    Menu('2 Broke Girls','http://www.watchseries.ac/serie/2_broke_girls',100,'https://upload.wikimedia.org/wikipedia/en/a/a4/2Broke_Girls_-_The_Complete_First_Season_DVD.jpg','http://ihdwallpapers.com/download/2_broke_girls_tv_series-1920x1080.jpg','','2 Broke Girls')
    Menu('How I Met Your Mother','http://www.watchseries.ac/serie/how_i_met_your_mother',100,'https://upload.wikimedia.org/wikipedia/en/d/d9/How_I_Met_Your_Mother_Season_2_DVD_Cover.jpg','http://t.wallpaperweb.org/wallpaper/movies/1920x1080/How_I_Met_Your_Mother_2.jpg','','How I Met Your Mother')
    Menu('Bottom','http://www.watchseries.ac/episode/bottom_s3_e1.html',100,'https://fanart.tv/fanart/tv/78050/tvthumb/bottom-50c84a42c95c6.jpg','https://i.ytimg.com/vi/brD6kqOawdU/maxresdefault.jpg','','Bottom')
    Menu('Max and Paddy\'s Road to Nowhere','http://www.watchseries.ac/serie/max_and_paddys_road_to_nowhere',100,"https://upload.wikimedia.org/wikipedia/en/f/f5/Max_and_Paddy's_Road_to_Nowhere_--_S01E01.jpg",'http://image.tmdb.org/t/p/w1920/aJueBWoB3ZsKEHWTMM9WfzLSPb4.jpg','','Max and Paddy\'s Road to Nowhere')
    Menu('New Girl','http://www.watchseries.ac/serie/new_girl',100,'https://upload.wikimedia.org/wikipedia/en/1/18/New_Girl_S4.jpg','http://www.entertainmentwallpaper.com/images/res1920x1080/movie/tv-new-girl26.jpg','','New girl')
    Menu('The Simpsons','http://www.watchseries.ac/serie/the_simpsons_1',100,'http://bigtentjudaism.org/uploads/simpsons.thumbnail.jpg','http://wallpaper.pickywallpapers.com/1920x1080/simpsons-sopranos-style.jpg','','The Simpsons')
    Menu('Futurama','http://www.watchseries.ac/serie/futurama',100,'https://upload.wikimedia.org/wikipedia/en/2/2d/Futurama_Volume_1.png','https://images8.alphacoders.com/455/455759.jpg','','Futurama')
    Menu('Family Guy','http://www.watchseries.ac/serie/family_guy',100,'https://i1.ytimg.com/sh/eYTaRhlD15w/showposter.jpg?v=5037ecb8','http://www.wallpapersxl.com/get/5950868','','Family Guy')
    Menu('American Dad','http://www.watchseries.ac/serie/american_dad',100,'https://upload.wikimedia.org/wikipedia/en/7/75/American_Dad_season_11.png','http://cdn2us.denofgeek.com/sites/denofgeekus/files/american-dad-american-dad.jpg','','American Dad')
    Menu('Impractical Jokers','http://www.watchseries.ac/serie/impractical_jokers',100,'https://upload.wikimedia.org/wikipedia/en/b/b9/Impractical_Jokers_Title.png','https://s3.graphiq.com/sites/default/files/8464/media/images/Impractical_Jokers_8102594.jpg','','Impractical Jokers US')
    Menu('Impractical Jokers UK','http://www.watchseries.ac/serie/impractical_jokers_uk_',100,'https://upload.wikimedia.org/wikipedia/en/thumb/3/38/Impractical_Jokers_UK_Titlecard.png/320px-Impractical_Jokers_UK_Titlecard.png','https://ichef.bbci.co.uk/images/ic/480x270/p01tbh8y.jpg','','Impractical Jokers UK')
    Menu('Two and a half men','http://www.watchseries.ac/serie/two_and_a_half_men',100,'https://upload.wikimedia.org/wikipedia/en/5/51/Two_and_a_Half_Men-title.png','http://www.wallpaper.ge/download/two_and_a_half_men_s5-1920x1080.jpg','','name')
    Menu('Silicon Valley','http://www.watchseries.ac/serie/silicon_valley',100,'http://download.nowhdtime.com/download/movies/TV%20Series%20%26%20Others/English/Silicon%20Valley/landscape.jpg','https://pmcvariety.files.wordpress.com/2014/02/silicon-valley.jpg','','name')
    Menu('8 Out of 10 Cats does countdown','http://www.watchseries.ac/serie/8_out_of_10_cats_does_countdown',100,'https://upload.wikimedia.org/wikipedia/en/a/a7/8_Out_Of_10_Cats_Does_Countdown_Logo.jpg','https://i.ytimg.com/vi/ekuR1pG1syE/maxresdefault.jpg','','name')
    Menu('8 out of 10 cats','http://www.watchseries.ac/serie/8_out_of_10_cats',100,'http://vignette2.wikia.nocookie.net/britquiz/images/9/91/400px-8_out_of_10_cats_2008_cast.jpg/revision/latest?cb=20150119144708','http://pogd.es/assets/bg/8-Out-of-10-Cats.jpg','','name')
    Menu('Dave Gorman Modern Life is Goodish','http://www.watchseries.ac/serie/dave_gorman_modern_life_is_goodish',100,'https://cdn1.lockerdome.com/uploads/73cabf2642c6277882b9b3e215bda1f39e19b0008e07f0f43c53f170680955ac_thumb_medium','http://happyhourproductions.co.uk/news/wp-content/uploads/2013/09/DaveGorman51.jpg','','name')

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

	
def Movies():
    Menu('.These are youtube lists, check pics for film','',100,'image','fanart','','name')
    Menu('.as titles may not be accurate, if not use a different addon as','url',100,'image','fanart','','name')
    Menu('.movies can be harder to keep on top of and if im honest i cant be bothered','url',100,'image','fanart','','name')
    Menu('[COLORred]Trailers[/COLOR]','https://www.youtube.com/playlist?list=PLSBlhbfM-l3tayic6LrrHNTBwEgC99zsq',7,IMAGES,FANART,'','name')
    Menu('List 1','https://www.youtube.com/playlist?list=PLjuR5ouJJf7oFy9kYTjeOdc8n6yGm_U64',7,IMAGES,FANART,'','name')
    Menu('List 2','https://www.youtube.com/playlist?list=PLwByQ6h-_Dd7_TSIwkToSJyrQwB4k-GCr',7,IMAGES,FANART,'','name')
    Menu('British Sitcom and Comedy','https://www.youtube.com/playlist?list=PL6oFy0ak-CyIMBA5AGsRHAoyym-wifb28',7,IMAGES,FANART,'','name')
    Menu('Rom Com','https://www.youtube.com/playlist?list=PL472D9F565A037F14',7,IMAGES,FANART,'','name')
    Menu('Silent Movies','https://www.youtube.com/playlist?list=PLsX9PShhztBhO8NT3sbBn_h_PunWV1Hrj',7,IMAGES,FANART,'','name')
    Menu('"Full stoner" Movies','https://www.youtube.com/playlist?list=PLCQNxPV-JejpowNXY4RpLH_X562_ZXWXm',7,IMAGES,FANART,'','name')
    Menu('British Comedy Films','https://www.youtube.com/playlist?list=PLdsHPthC90DxwBmmqy3T28rTmNJdj1InX',7,IMAGES,FANART,'','name')
    Menu('Rom Com 2','https://www.youtube.com/playlist?list=PLa8JdFPfSyoWmOi4g-T_GHxAHEM8jHbt6',7,IMAGES,FANART,'','name')
    Menu('80\'s Movies','https://www.youtube.com/playlist?list=PLwby6XrbM4tBQrEKliMUZGJsqM_0WItsr',7,IMAGES,FANART,'','name')
    Menu('British TV Series Films','https://www.youtube.com/playlist?list=PL4g1XnupBKvVtVoOvvX7DK7Ahd6Nhhugv',7,IMAGES,FANART,'','name')
    Menu('Classic Comedy','https://www.youtube.com/playlist?list=PLMbPbsn-u_g2v3InoON58c1872B1Tel4_',7,IMAGES,FANART,'','name')
    Menu('Black Comedy','https://www.youtube.com/playlist?list=PL_SN8T3Rw7by6_A-j-qovI7ufKcCIA-ng',7,IMAGES,FANART,'','name')
    Menu('Classic British Comedy','https://www.youtube.com/playlist?list=PLFPgkkKPTGxS9EpnyrdwbTjVMU7zv3imk',7,IMAGES,FANART,'','name')
    Menu('Classic Rom Com','https://www.youtube.com/playlist?list=PLScQrH5cf7WUwcI3zdDQYhGbV5QT3oBHh',7,IMAGES,FANART,'','name')
    Menu('Westerns','https://www.youtube.com/playlist?list=PLD3363FF38E2801F2',7,IMAGES,FANART,'','name')
    Menu('List 3','https://www.youtube.com/playlist?list=PL08mBQFKEHsfAzzxnhW-ds1uEMWd8_YHK',7,IMAGES,FANART,'','name')
	
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);		
	
#100 = watchseries link      7 = youtube Playlist       9 = youtube single


	
def grab_youtube_playlist(url):

    HTML = OPEN_URL(url)
    block_set = re.compile('<tr class="pl-video yt-uix-tile(.+?)</tr>',re.DOTALL).findall(HTML)
    for block in block_set:
        image = re.compile('data-thumb="(.+?)"').findall(str(block))
        for image in image:
            image = image
        name = re.compile('data-title="(.+?)"').findall(str(block))
        for name in name:
            if 'elete Vid' in name:
                pass
            elif 'rivate Vid' in name:
                pass
            else:
    			name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
        duration = re.compile('<div class="timestamp"><span aria-label=".+?">(.+?)</span>').findall(str(block))
        for duration in duration:
            duration = duration
        url = re.compile('data-video-ids="(.+?)">').findall(str(block))
        for url in url:
            url = url
        Play('[COLORred]'+duration+'[/COLOR] : '+name,url,9,image,FANART,'','' )


#    image = ''
#    HTML = OPEN_URL(url)
#    block_set = re.compile('<li class="yt-uix-scroller-scroll-unit "(.+?)</li>',re.DOTALL).findall(HTML)
#    for block in block_set:
#        name = re.compile('data-video-title="(.+?)"').findall(str(block))
#        for name in name:
#            name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
#        url = re.compile('<a href="/w(.+?)&').findall(str(block))
#       for url in url:
#            url = (url).replace('atch?v=','')
#        image = re.compile('data-thumbnail-url="(.+?)"').findall(str(block))
#        for image in image:
#            image = image
#        if 'elete' in name:
#            pass
#        if 'rivate ' in name:
#            pass        
#        else:
#            Play(name,url,9,image,FANART,'','')

def Stand_up():
    HTML = OPEN_URL(BASE)
    Block = re.compile('<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>',re.DOTALL).findall(HTML)
    for img, comic, c in Block:
	find_URL = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(c)
        for url, name in find_URL:
            if 'tube' in url:
                pass
            elif 'stage' in url:
				Play(comic + '   -   ' + name,(url).replace('" target="_blank',''),3,'http://couchtripper.com/'+img,FANART,'','')
            elif 'vee' in url:
                pass
			    

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def Youtube_StandUP_grab():
    pass
	
###########################Watch series Grab##########################################

def Grab_Season(iconimage,url,extra):
    image = ' '
    description = ' '
    fanart = ' '
    season = ' '
    OPEN = OPEN_URL(url)
    image = re.compile('<img src="(.+?)">').findall(OPEN)
    for image in image:
        image = image
    background = re.compile('style="background-image: url\((.+?)\)">').findall(OPEN)
    for fanart in background:
        fanart = fanart	
    match = re.compile('itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>',re.DOTALL).findall(OPEN)
    for url,season in match:
        season = 'S'+(season).replace('  ','').replace('\n','').replace('    ','').replace('	','')
        url = Main + url
        Menu((season).replace('  ',''),url,101,image,fanart,description,'')
        setView('Movies', 'INFO')
	
def Grab_Episode(url,name,fanart,extra,iconimage):
    main_name = extra 
    season = name
    OPEN = OPEN_URL(url)
    image = iconimage
    match = re.compile('<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>',re.DOTALL).findall(OPEN)
    for url,name,date in match:
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        url = Main+url
        date = date
        full_name = name+' - [COLORred]'+date+'[/COLOR]'
        Menu(full_name,url,102,image,fanart,'Aired : '+date,full_name)

class Watchseries():

        List = []
        source_list = []   
        Sources = ['daclips','filehoot','thevideo','allmyvideos','vidspot','vodlocker','vidto']		
        def __init__(self,name,url,full_name):

            full_name = full_name
            season_name = name
            self.Get_Sources(url,season_name,full_name)
			

        def Get_Sources(self,URL,season_name,full_name):
            dp = xbmcgui.DialogProgress()
            HTML = OPEN_URL(URL)
            match = re.compile('<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n',re.DOTALL).findall(HTML)
            for url,name in match:
                URL = 'http://www.watchseries.ac/link/' + url
                self.Get_site_link(URL,season_name,full_name)
            if len(match)<=0:
                Menu('[COLORred]NO STREAMS AVAILABLE[/COLOR]','','','','','','')

				
        def Get_site_link(self,url,season_name,full_name):
            HTML = OPEN_URL(url)
            match = re.compile('<iframe style=.+?" src="(.+?)"').findall(HTML)
            match2 = re.compile('<IFRAME SRC="(.+?)"').findall(HTML)
            match3 = re.compile('<IFRAME style=".+?" SRC="(.+?)"').findall(HTML)
            for url in match:
                for item in self.Sources:
                    if item in url:
                        s1=Thread(target=self.main,args=(url,season_name,full_name))
                        s1.start()
                    else:
                        pass
            for url in match2:
                for item in self.Sources:
                    if item in url:
                        s2=Thread(target=self.main,args=(url,season_name,full_name))
                        s2.start()
                    else:
                        pass
            for url in match3:
                for item in self.Sources:
                    if item in url:
                        s3=Thread(target=self.main,args=(url,season_name,full_name))
                        s3.start()
                    else:
                        pass

        def main(self,url,season_name,full_name):
                dp.create("[COLORwhite]Origin[/COLOR]","Getting Sources",'','Please Wait')
                if 'daclips.in' in url:
                    source_name = 'DACLIPS'
                    if source_name in Watchseries.source_list:
					    pass
                    else:
                        t1 = Thread(target=self.daclips,args=(url,season_name,source_name,full_name))
                        dp.update(0,"", "Getting Daclips Links")
                        t1.start()
                else:
                    if 'filehoot.com' in url:
                        source_name = 'FILEHOOT'
                        if source_name in Watchseries.source_list:
					        pass
                        else:         
                            dp.update(0,"", "Getting Filehoot Links")
                            t2 = Thread(target=self.filehoot,args=(url,season_name,source_name,full_name))
                            t2.start()
                    else:
                        if 'thevideo.me' in url:
                            source_name = 'THEVIDEO'
                            if source_name in Watchseries.source_list:
					            pass					        
                            else:                           
                                t3=Thread(target=self.thevideo,args=(url,season_name,source_name,full_name))
                                dp.update(0,"", "Getting Thevideo Links")
                                t3.start()								
                        else:
                            if 'allmyvideos.net' in url:
                                source_name = 'ALLMYVIDEOS'
                                if source_name in Watchseries.source_list:
                                    pass                    
                                else:						
                                    t4=Thread(target=self.allmyvid,args=(url,season_name,source_name,full_name))
                                    dp.update(0,"", "Getting Allmyvideo Links")
                                    t4.start()
                            else:
                                if 'vidspot.net' in url:
                                    source_name = 'VIDSPOT'
                                    if source_name in Watchseries.source_list:
					                    pass                            
                                    else:
                                        t5=Thread(target=self.vidspot,args=(url,season_name,source_name,full_name))
                                        dp.update(0,"", "Getting Vidspot Links")
                                        t5.start()
                                else:
                                    if 'vodlocker' in url:
                                        source_name = 'VODLOCKER'
                                        if source_name in Watchseries.source_list:
					                        pass                                
                                        else:
                                            t6=Thread(target=self.vodlocker,args=(url,season_name,source_name,full_name))
                                            dp.update(0,"", "Getting Vodlocker Links")
                                            t6.start()	
                                        if 'vidto' in url:
											source_name = 'VIDTO'
											if source_name in Watchseries.source_list:
												pass                                
											else:
												t6=Thread(target=self.vodlocker,args=(url,season_name,source_name,full_name))
												dp.update(0,"", "Getting vidto Links")
												t6.start()	


        def vidto(self,url,season_name,source_name,full_name):
            HTML = OPEN_URL(url)
            match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"',re.DOTALL).findall(HTML)
            for Link,name in match:
                    self.Printer(Link,season_name,source_name,full_name)

												
        def allmyvid(self,url,season_name,source_name,full_name):
            HTML = OPEN_URL(url)
            match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"',re.DOTALL).findall(HTML)
            for Link,name in match:
                    self.Printer(Link,season_name,source_name,full_name)

        def vidspot(self,url,season_name,source_name,full_name):
            HTML = OPEN_URL(url)
            match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"').findall(HTML)
            for Link,name in match:
                    self.Printer(Link,season_name,source_name,full_name)

        def thevideo(self,url,season_name,source_name,full_name):
            HTML = OPEN_URL(url)
            match = re.compile("{ label: '.+?', file: '(.+?)' }").findall(HTML)
            for Link in match:
                    pass

        def vodlocker(self,url,season_name,source_name,full_name):
            HTML = OPEN_URL(url)
            match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name,full_name)

        def daclips(self,url,season_name,source_name,full_name):
            HTML = OPEN_URL(url)
            match = re.compile('{ file: "(.+?)", type:"video" }').findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name,full_name)

        def filehoot(self,url,season_name,source_name,full_name):
            HTML = OPEN_URL(url)
            match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name,full_name)

        def Printer(self,Link,season_name,source_name,full_name):


                if Link in Watchseries.List:
                    pass
                elif full_name not in Watchseries.List:
                    Watchseries.List.append(full_name) 
                else:
                    if 'http:/' in Link:
                        Play(source_name,Link,5,IMAGES,FANART,'','')
                        dp.update(100,"", "Got Source")
                        Watchseries.List.append(Link)                    
                                       

					
		    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
###########################################Watch series end###########################################			
	
def Play_Stage(url):
    HTML = OPEN_URL(url)
    playlink = re.compile("url\[.+?\] = '(.+?)';").findall(HTML)
    for url in playlink:
        Resolve((url).replace('[','').replace(']','').replace('\'',''))

def Menu(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Get Up Stand Up Favorites','XBMC.RunPlugin(%s?mode=105&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Get Up Stand Up Favorites','XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

		
def Play(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Get Up Stand Up Favorites','XBMC.RunPlugin(%s?mode=105&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Get Up Stand Up Favorites','XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def RESOLVE(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    url = (url).strip()
    try: play.play(url).strip()
    except: pass

		
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
		
		
#===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------

def addon_log(string):
    if debug == 'true':
        xbmc.log("[addon.live.GenieTV-%s]: %s" %(addon_version, string))

def addFavorite(name,url,iconimage,fanart,mode,playlist=None,regexs=None):
        favList = []
        try:
            # seems that after
            name = name.encode('utf-8', 'ignore')
        except:
            pass
        if os.path.exists(favourites)==False:
            addon_log('Making Favorites File')
            favList.append((name,url,iconimage,fanart,mode,playlist,regexs))
            a = open(favourites, "w")
            a.write(json.dumps(favList))
            a.close()
        else:
            addon_log('Appending Favorites')
            a = open(favourites).read()
            data = json.loads(a)
            data.append((name,url,iconimage,fanart,mode))
            b = open(favourites, "w")
            b.write(json.dumps(data))
            b.close()
		

def getFavorites():
        if os.path.exists(favourites)==False:
            favList = []
            addon_log('Making Favorites File')
            favList.append(('Get Up Stand Up Favourites Section','','','','','',''))
            a = open(favourites, "w")
            a.write(json.dumps(favList))
            a.close()        
        else:
			items = json.loads(open(favourites).read())
			total = len(items)
			for i in items:
				name = i[0]
				url = i[1]
				iconimage = i[2]
				try:
					fanArt = i[3]
					if fanArt == None:
						raise
				except:
					if ADDON.getSetting('use_thumb') == "true":
						fanArt = iconimage
					else:
						fanArt = fanart
				try: playlist = i[5]
				except: playlist = None
				try: regexs = i[6]
				except: regexs = None

				if i[4] == 0:
					Menu(name,url,'',iconimage,fanart,'','','fav')
				else:
					Menu(name,url,i[4],iconimage,fanart,'','','fav')

def rmFavorite(name):
        data = json.loads(open(favourites).read())
        for index in range(len(data)):
            if data[index][0]==name:
                del data[index]
                b = open(favourites, "w")
                b.write(json.dumps(data))
                b.close()
                break
        xbmc.executebuiltin("XBMC.Container.Refresh")
		
############################## FAVOURITES END ###############################
		
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
extra=None
fav_mode=None

try:
    fav_mode=int(params["fav_mode"])
except:
    pass
try:
    extra=urllib.unquote_plus(params["extra"])
except:
    pass
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
        
def Resolve(url): 
    play=xbmc.Player()
    import urlresolver
    try: play.play(url)
    except: pass

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = ''
    link = ''
    try: 
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    except: pass
    if link != '':
        return link
    else:
        link = 'Opened'
        return link

def setView(content, viewType):
	if content:
	    xbmcplugin.setContent(int(sys.argv[1]), content)


if mode == None     : Main_Menu()
elif mode == 1 		: Stand_up()
elif mode == 2    	: Search()
elif mode == 3 		: Play_Stage(url)
elif mode == 4 		: TV_Shows()
elif mode == 5    	: Resolve(url)
elif mode == 6 		: Movies()

elif mode == 7 		: grab_youtube_playlist(url)
elif mode == 9 	 	: yt.PlayVideo(url)

elif mode == 10 	: Stand_up_Menu()
elif mode == 11 	: youtube_lists()

elif mode == 100 	: Grab_Season(iconimage,url,extra)
elif mode == 101 	: Grab_Episode(url,name,fanart,extra,iconimage)
elif mode == 102	: Watchseries(name,url,extra)
elif mode==103:
    addon_log("getFavorites")
    getFavorites()
elif mode==104:
    addon_log("addFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name,url,iconimage,fanart,fav_mode)
elif mode==105:
    addon_log("rmFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

#def Search():
#    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
#    Search_Title = Search_Name.lower()
#    HTML = OPEN_URL(BASE)
#    Block = re.compile('<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>',re.DOTALL).findall(HTML)
#    for img, comic, c in Block:
#        for Search_Name in comic:
#            find_URL = re.compile('<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(c)
#            for url, name in find_URL:
#                if 'tube' in url:
#                    pass
#                elif 'stage' in url:
#                    Play(comic + '   -   ' + name,(url).replace('" target="_blank',''),3,'http://couchtripper.com/'+img,FANART,'')
#                elif 'vee' in url:
#			        pass
