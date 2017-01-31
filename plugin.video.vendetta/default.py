# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
import requests , urllib2 , xbmcgui , urllib , xbmcplugin , re , xbmc , os , shutil , xbmcaddon
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
if 68 - 68: Ii1I / O0
if 46 - 46: O0 * II111iiii / IiII * Oo0Ooo * iII111i . I11i
if 62 - 62: i11iIiiIii - II111iiii % I1Ii111 - iIii1I11I1II1 . I1ii11iIi11i . II111iiii
if 61 - 61: oO0o / OoOoOO00 / iII111i * OoO0O00 . II111iiii
if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + IiII . I1Ii111
if 55 - 55: iIii1I11I1II1 - I1IiiI . Ii1I * IiII * i1IIi / iIii1I11I1II1
if 79 - 79: oO0o + I1Ii111 . ooOoO0o * IiII % I11i . I1IiiI
if 94 - 94: iII111i * Ii1I / IiII . i1IIi * iII111i
if 47 - 47: i1IIi % i11iIiiIii
if 20 - 20: ooOoO0o * II111iiii
if 65 - 65: o0oOOo0O0Ooo * iIii1I11I1II1 * ooOoO0o
if 18 - 18: iIii1I11I1II1 / I11i + oO0o / Oo0Ooo - II111iiii - I11i
if 1 - 1: I11i - OOooOOo % O0 + I1IiiI - iII111i / I11i
if 31 - 31: OoO0O00 + II111iiii
if 13 - 13: OOooOOo * oO0o * I1IiiI
from datetime import datetime
if 55 - 55: II111iiii
IIIiI11ii = xbmc . translatePath ( 'special://home/addons/plugin.video.vendetta/' )
O000oo = xbmc . translatePath ( 'special://home/userdata/addon_data' )
i1iIIi1 = O000oo + '/plugin.video.vendetta/'
ii11iIi1I = IIIiI11ii + 'icon.png'
iI111I11I1I1 = IIIiI11ii + 'fanart.jpg'
OOooO0OOoo = 'plugin.video.vendetta'
iIii1 = xbmcaddon . Addon ( id = OOooO0OOoo )
oOOoO0 = xbmcgui . Dialog ( )
O0OoO000O0OO = xbmc . translatePath ( 'special://home/addons/' )
iiI1IiI = 'http://footytube.com'
II = int ( sys . argv [ 1 ] )
if 57 - 57: oO0o
iI = datetime . now ( ) . strftime ( '%Y' )
iI11iiiI1II = datetime . now ( ) . strftime ( '%m' )
O0oooo0Oo00 = datetime . now ( ) . strftime ( '%d' )
Ii11iii11I = datetime . now ( ) . strftime ( '%H' )
oOo00Oo00O = datetime . now ( ) . strftime ( '%M' )
iI11i1I1 = str ( ( int ( Ii11iii11I ) * 60 ) + int ( oOo00Oo00O ) )
if 71 - 71: ooOoO0o % iII111i / o0oOOo0O0Ooo
if 49 - 49: II111iiii % iII111i * O0
def oOOo0oo ( ) :
 for o0oo0o0O00OO , o0oO , file in os . walk ( O0OoO000O0OO ) :
  for dir in o0oO :
   if 'anonymous' in dir . lower ( ) :
    if iIii1 . getSetting ( 'Delete' ) == 'true' :
     I1i1iii ( dir )
    else :
     oOOoO0 . ok ( 'Something has to go' , 'A addon has been found that is leeching content' , 'your next choice is up to you' , 'if you cancel vendetta will be removed' )
     i1iiI11I = [ 'Remove ' + dir , 'Remove vendetta' , 'Remove both' ]
     iiii = xbmcgui . Dialog ( ) . select ( 'What is going to be removed?' , i1iiI11I )
     if iiii == 0 :
      I1i1iii ( dir )
     elif iiii == 1 :
      I1i1iii ( 'plugin.video.vendetta' )
     elif iiii == 2 :
      I1i1iii ( dir )
      I1i1iii ( 'plugin.video.vendetta' )
     else :
      I1i1iii ( 'plugin.video.vendetta' )
      if 54 - 54: I1ii11iIi11i * OOooOOo
def I1i1iii ( dir ) :
 I1IIIii = O0OoO000O0OO + dir
 shutil . rmtree ( I1IIIii )
 if 95 - 95: OoO0O00 % oO0o . O0
def I1i1I ( ) :
 oOOo0oo ( )
 oOO00oOO ( 'Search' , '' , 1 , '' , '' , '' , '' )
 oOO00oOO ( 'UK ONLY - Whats on now' , '' , 2 , '' , '' , '' , '' )
 oOO00oOO ( 'Lists' , '' , 3 , '' , '' , '' , '' )
 oOO00oOO ( 'By Country' , '' , 4 , '' , '' , '' , '' )
 oOO00oOO ( 'Todays Sports' , '' , 13 , '' , '' , '' , '' )
 oOO00oOO ( 'Football Replays' , '' , 14 , '' , '' , '' , '' )
 if 75 - 75: i1IIi / OoooooooOO - O0 / OoOoOO00 . II111iiii - i1IIi
def O000OO0 ( ) :
 oOO00oOO ( 'Search by channel number' , '' , 5 , '' , '' , '' , '' )
 oOO00oOO ( 'Popular' , '7' , 6 , '' , '' , '' , '' )
 oOO00oOO ( 'Freeview' , '3' , 6 , '' , '' , '' , '' )
 oOO00oOO ( 'Sky' , '5' , 6 , '' , '' , '' , '' )
 oOO00oOO ( 'Virgin XL' , '25' , 6 , '' , '' , '' , '' )
 oOO00oOO ( 'Freesat' , '19' , 6 , '' , '' , '' , '' )
 oOO00oOO ( 'BT' , '22' , 6 , '' , '' , '' , '' )
 if 43 - 43: I1Ii111 - O0 % I1IiiI . I11i
def o00 ( ) :
 oOO00oOO ( '[COLORred]Long loading time, go make a brew!! it will search each list for each channel[/COLOR]' , '' , '' , '' , '' , '' , '' )
 oOO00oOO ( '[COLORred]Cancel at any time to move on to next channel if your happy with stream results[/COLOR]' , '' , '' , '' , '' , '' , '' )
 oOO00oOO ( 'Mainstream Channels' , '' , 24 , '' , '' , '' , '' )
 oOO00oOO ( 'LiveOnSat Channels - Some searchs may take a sec - if empty menu means no results' , '' , 25 , '' , '' , '' , '' )
 oOO00oOO ( 'Mama Hd - resolved by sports devil' , '' , 27 , '' , '' , '' , '' )
 if 95 - 95: O0 + OoO0O00 . II111iiii / O0
def O000oo0O ( ) :
 OOOO = i11i1 ( 'http://www.mamahd.com/' )
 IIIii1II1II = re . compile ( '<div class="schedule">(.+?)<div id="pagination">' , re . DOTALL ) . findall ( OOOO )
 for i1I1iI in IIIii1II1II :
  oo0OooOOo0 = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)"></div>.+?<div class="home cell">.+?<span>(.+?)</span>.+?<div class="away cell">.+?<span>(.+?)</span>.+?</a>' , re . DOTALL ) . findall ( str ( IIIii1II1II ) )
  for o0O , O00oO , I11i1I1I , oO0Oo in oo0OooOOo0 :
   oOOoo0Oo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + o0O
   o00OO00OoO ( I11i1I1I + ' vs ' + oO0Oo , oOOoo0Oo , 10 , O00oO , '' , '' , '' )
   if 60 - 60: OoO0O00 * OoOoOO00 - OoO0O00 % OoooooooOO - ooOoO0o + I1IiiI
def O00Oo000ooO0 ( ) :
 OOOO = i11i1 ( 'http://www.live-footballontv.com/' )
 IIIii1II1II = re . compile ( '<div id="listings"><div class="container" align="center"><div class="row-fluid"><div class="span12 matchdate">(.+?)<div class="span12 matchdate">' , re . DOTALL ) . findall ( OOOO )
 OoO0O00IIiII = re . compile ( 'span4 matchfixture">(.+?)</div>.+?span4 competition">(.+?)</div>.+?span1 kickofftime">(.+?)</div>.+?span3 channels">(.+?)</div>' ) . findall ( str ( IIIii1II1II ) )
 for o0 , ooOooo000oOO , Oo0oOOo , Oo0OoO00oOO0o in OoO0O00IIiII :
  OOO00O = ( o0 ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  OOoOO0oo0ooO = ( ooOooo000oOO ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  O0o0O00Oo0o0 = ( Oo0OoO00oOO0o ) . replace ( '&nbsp;' , '-' ) . replace ( '-' , '' ) . replace ( '&#039;' , '\'' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  oOO00oOO ( Oo0oOOo + ' : ' + OOO00O + ' - ' + O0o0O00Oo0o0 , O0o0O00Oo0o0 , 26 , '' , '' , OOoOO0oo0ooO , '' )
  if 87 - 87: ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
def O0ooo0O0oo0 ( ) :
 OOOO = i11i1 ( 'http://liveonsat.com/daily.php' )
 oo0oOo = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( OOOO )
 for ooOooo000oOO , O00oO , Oo0oOOo , o000O0o in oo0oOo :
  iI1iII1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( o000O0o )
  oO0OOoo0OO = ( str ( iI1iII1 ) ) . replace ( '[$]' , '' ) . replace ( '\\xc3' , 'n' ) . replace ( '\'' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\\xe2' , '' ) . replace ( '\\x80' , '' ) . replace ( '\\x99' , '' ) . replace ( '\\xb1a' , 'i' )
  o0 = str ( ooOooo000oOO ) + ' - ' + str ( Oo0oOOo )
  O0ii1ii1ii = 'http://liveonsat.com' + str ( O00oO )
  oOO00oOO ( o0 , ( oO0OOoo0OO ) . replace ( ',' , '/' ) . replace ( '|' , '' ) , 26 , O0ii1ii1ii , '' , oO0OOoo0OO , '' )
  if 91 - 91: IiII
  if 15 - 15: II111iiii
def Ii ( url ) :
 ooo0O = [ ]
 oOoO0o00OO0 = url + '/'
 i1I1ii = re . compile ( '(.+?)/' ) . findall ( str ( oOoO0o00OO0 ) )
 for url in i1I1ii :
  if 'HD' in url :
   url = ( url ) . replace ( 'HD' , '' )
  elif '(' in url :
   oOOo0 = re . compile ( '(.+?)\(' ) . findall ( str ( url ) )
   for i1I1iI in oOOo0 :
    url = i1I1iI
    if url not in ooo0O :
     oo00O00oO = ( url ) . lower ( )
     search . Live_TV ( oo00O00oO )
     ooo0O . append ( url )
  else :
   if url not in ooo0O :
    oo00O00oO = ( url ) . lower ( )
    iIiIIIi ( oo00O00oO )
    ooo0O . append ( url )
    if 93 - 93: iII111i
def i1IIIiiII1 ( ) :
 if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
 oOO00oOO ( 'Footy Tube' , 'http://www.footytube.com/leagues' , 16 , ii11iIi1I , iI111I11I1I1 , '' , '' )
 oOO00oOO ( 'Latest' , 'http://www.fullmatchesandshows.com' , 15 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , iI111I11I1I1 , '' , '' )
 oOO00oOO ( 'Shows' , 'http://www.fullmatchesandshows.com/category/show/' , 15 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iI111I11I1I1 , '' , '' )
 oOO00oOO ( 'Premier League' , 'http://www.fullmatchesandshows.com/premier-league/' , 15 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iI111I11I1I1 , '' , '' )
 oOO00oOO ( 'La Liga' , 'http://www.fullmatchesandshows.com/la-liga/' , 15 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iI111I11I1I1 , '' , '' )
 oOO00oOO ( 'Bundesliga' , 'http://www.fullmatchesandshows.com/bundesliga/' , 15 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iI111I11I1I1 , '' , '' )
 oOO00oOO ( 'Champions League' , 'http://www.fullmatchesandshows.com/champions-league/' , 15 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iI111I11I1I1 , '' , '' )
 oOO00oOO ( 'Serie A' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 15 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iI111I11I1I1 , '' , '' )
 oOO00oOO ( 'Ligue 1' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 15 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iI111I11I1I1 , '' , '' )
 if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
def o0oOIIiIi1iI ( url ) :
 OOOO = i11i1 ( url )
 i1IiiiI1iI = re . compile ( '<div class="headline_xlrg color_dgray"><img align="absmiddle" height="22" src="(.+?)">(.+?)</div>' ) . findall ( OOOO )
 for O00oO , o0 in i1IiiiI1iI :
  oOO00oOO ( o0 , '' , 17 , iiI1IiI + O00oO , iI111I11I1I1 , '' , '' )
  xbmcplugin . addSortMethod ( II , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 49 - 49: Ii1I / OoO0O00 . II111iiii
def ooOOoooooo ( name ) :
 o0O = 'http://www.footytube.com/leagues'
 II1I = name
 OOOO = i11i1 ( o0O )
 i1IiiiI1iI = re . compile ( '<div class="headline_xlrg color_dgray"><img align="absmiddle" height="22" src="(.+?)">' + name + '</div>(.+?)<div style="margin-bottom: 15px">' , re . DOTALL ) . findall ( OOOO )
 for O00oO , IIIii1II1II in i1IiiiI1iI :
  O0i1II1Iiii1I11 = re . compile ( '<div>.+?<a href="(.+?)" class="standard_link">(.+?)</a><br>.+?<span class="text_xsml">(.+?)</span>.+?</div>' , re . DOTALL ) . findall ( str ( IIIii1II1II ) )
  for o0O , name , IIII in O0i1II1Iiii1I11 :
   oOO00oOO ( name + ' - ' + IIII , iiI1IiI + o0O , 18 , ii11iIi1I , iI111I11I1I1 , '' , '' )
  else :
   pass
   if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
def o00oooO0Oo ( url ) :
 OOOO = i11i1 ( url )
 i1I1ii = re . compile ( '<div class=".+?" style = ".+?"><a href="(.+?)" class=".+?" >(.+?)</a></div>' ) . findall ( OOOO )
 for url , o0 in i1I1ii :
  oOO00oOO ( o0 , iiI1IiI + url , 19 , ii11iIi1I , iI111I11I1I1 , '' , '' )
  if 78 - 78: Ii1I % I1Ii111 + I1ii11iIi11i
def OOooOoooOoOo ( url ) :
 OOOO = i11i1 ( url )
 i1I1ii = re . compile ( ' <div class="thumboverlay"> .+?<div><a href="(.+?)".+?<img src="(.+?)" width="165px" height="97px" /></a></div>.+?<div class="vid_title".+?class="standard_link">(.+?)</a><div class="vid_info">(.+?)</div>' , re . DOTALL ) . findall ( OOOO )
 for url , O00oO , o0 , o0OOOO00O0Oo in i1I1ii :
  o00OO00OoO ( o0 + ' - ' + o0OOOO00O0Oo , iiI1IiI + url , 20 , O00oO , iI111I11I1I1 , '' , '' )
  if 48 - 48: O0
  if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
def i1Iii1i1I ( name , url ) :
 OOOO = i11i1 ( url )
 i1I1ii = re . compile ( '<iframe src="(.+?)" width=' ) . findall ( OOOO )
 for url in i1I1ii :
  url = iiI1IiI + url
  OOoO00 ( url )
 IiI111111IIII = re . compile ( '<iframe id="ft_player" width="100%" height="100%" src="http://www.youtube.com/embed/(.+?)?rel=0&autoplay=1&enablejsapi=1" frameborder="0" allowfullscreen></iframe>' ) . findall ( OOOO )
 for url in IiI111111IIII :
  url = 'plugin://plugin.video.youtube/play/?video_id=' + url
  i1Ii ( name , url )
  if 14 - 14: iII111i
def I1iI1iIi111i ( url ) :
 OOOO = i11i1 ( url )
 IiI111111IIII = re . compile ( '<iframe width="560" height="315" src="https://www.youtube.com/embed/(.+?)" frameborder="0" allowfullscreen>' ) . findall ( OOOO )
 for url in IiI111111IIII :
  yt . PlayVideo ( url )
 i1I1ii = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( OOOO )
 for iiIi1IIi1I in i1I1ii :
  if 'div' in iiIi1IIi1I :
   pass
  else :
   o0OoOO000ooO0 = ( iiIi1IIi1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
   i1Ii ( 'Enjoy' , 'http:' + o0OoOO000ooO0 )
   if 56 - 56: iII111i
def OOoO00 ( url ) :
 OOOO = i11i1 ( url )
 IiI111111IIII = re . compile ( '<iframe width="560" height="315" src="https://www.youtube.com/embed/(.+?)" frameborder="0" allowfullscreen>' ) . findall ( OOOO )
 for url in IiI111111IIII :
  url = 'plugin://plugin.video.youtube/play/?video_id=' + url
  i1Ii ( o0 , url )
 i1I1ii = re . compile ( '<script data-config="(.+?)" data-css=".+?" data-height="100%" data-width="100%" src=".+?" type="text/javascript"></script>' ) . findall ( OOOO )
 for iiIi1IIi1I in i1I1ii :
  if 'div' in iiIi1IIi1I :
   pass
  else :
   o0OoOO000ooO0 = ( iiIi1IIi1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
   i1Ii ( 'Enjoy' , 'http:' + o0OoOO000ooO0 )
   if 86 - 86: II111iiii % I1Ii111
def iiIIiiIi1Ii11 ( url , iconimage ) :
 OOOO = i11i1 ( url )
 Oo0 = re . compile ( '<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)".+?"entry-thumb" src="(.+?)"' ) . findall ( OOOO )
 for url , o0 , O00oO in Oo0 :
  if 'Full Match' in o0 :
   oOooo0O0Oo = o0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   oOO00oOO ( oOooo0O0Oo , url , 21 , O00oO , '' , '' , '' )
  else :
   oOooo0O0Oo = o0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   o00OO00OoO ( oOooo0O0Oo , url , 23 , O00oO , '' , '' , '' )
 iIo0O = re . compile ( '<span class="current">.+?</span><a href="(.+?)" class="page" title=".+?">(.+?)</a>' ) . findall ( OOOO )
 for url , o0 in iIo0O :
  oOO00oOO ( 'NEXT PAGE' , url , 22 , iconimage , iI111I11I1I1 , '' , '' )
  if 2 - 2: iIii1I11I1II1 / oO0o + OoO0O00 / OOooOOo
def IIOOOO0oo0 ( url , iconimage ) :
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="td-block-span6">(.+?)<div class="td-pb-span4 td-main-sidebar">' , re . DOTALL ) . findall ( OOOO )
 Oo0 = re . compile ( '<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)".+?"entry-thumb" src="(.+?)"' ) . findall ( str ( IIIii1II1II ) )
 for url , o0 , O00oO in Oo0 :
  if 'Full Match' in o0 :
   oOooo0O0Oo = o0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   oOO00oOO ( oOooo0O0Oo , url , 21 , O00oO , '' , '' , '' )
  else :
   oOooo0O0Oo = o0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   o00OO00OoO ( oOooo0O0Oo , url , 23 , O00oO , '' , '' , '' )
 iIo0O = re . compile ( '<span class="current">.+?</span><a href="(.+?)" class="page" title=".+?">(.+?)</a>' ) . findall ( OOOO )
 for url , o0 in iIo0O :
  oOO00oOO ( 'NEXT PAGE' , url , 22 , iconimage , iI111I11I1I1 , '' , '' )
 if len ( Oo0 ) <= 0 :
  oOO00oOO ( 'No Replays available sorry' , url , 22 , iconimage , iI111I11I1I1 , '' , '' )
  if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
def I1i1Iiiii ( url , iconimage ) :
 o00OO00OoO ( 'Extended Highlights' , url , 23 , iconimage , iI111I11I1I1 , '' , '' )
 OOOO = i11i1 ( url )
 i1I1ii = re . compile ( '<link href=".+?" rel="stylesheet" type="text/css"><li tabindex="0" class="button_style" id=".+?"><a href="(.+?)"><div class="acp_title">(.+?)</div></a></li>' ) . findall ( OOOO )
 for OOo0oO00ooO00 , o0 in i1I1ii :
  url = url + OOo0oO00ooO00
  o0 = ( o0 ) . replace ( 'HL English' , 'English Highlights' )
  o00OO00OoO ( o0 , url , 23 , iconimage , iI111I11I1I1 , '' , '' )
  if 90 - 90: OoOoOO00 * I1Ii111 + o0oOOo0O0Ooo
def OO ( ) :
 OoOoO = { "User-Agent" : "Mozilla/5.0" }
 OOOO = requests . get ( 'http://www.iptvultra.com/' , headers = OoOoO ) . text
 i1I1ii = re . compile ( '<span class="link"><a href="(.+?)">(.+?)</a>' ) . findall ( OOOO )
 for o0O , o0 in i1I1ii :
  oOO00oOO ( o0 , o0O , 12 , '' , '' , '' , '' )
  if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
def o00oO0oo0OO ( url ) :
 OoOoO = { "User-Agent" : "Mozilla/5.0" }
 OOOO = requests . get ( url , headers = OoOoO ) . text
 i1I1ii = re . compile ( '".+?[@](.+?)[@].+?[@].+?[@](.+?)"' ) . findall ( OOOO )
 for o0 , OOo0oO00ooO00 in i1I1ii :
  o0 = o0 . replace ( '[' , '' ) . replace ( ']' , '' )
  if o0 [ 0 ] == ' ' :
   o0 = o0 [ 1 : ]
  if o0 [ - 1 ] == ' ' :
   o0 = o0 [ : - 1 ]
  O0O0OOOOoo = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + OOo0oO00ooO00 . replace ( '[' , '' ) . replace ( ']' , '' ) + ';name=vendetta'
  o00OO00OoO ( o0 , O0O0OOOOoo , 10 , '' , '' , '' , '' )
  if 74 - 74: I1ii11iIi11i + II111iiii / OoO0O00
def oOo0O0Oo00oO ( ) :
 OOOO = requests . get ( 'http://www.shadow-net.org' ) . text
 i1I1ii = re . compile ( '<li class=""><a href="(.+?)">(.+?)</a>' ) . findall ( OOOO )
 for o0O , o0 in i1I1ii :
  o0 = o0 . replace ( '&amp;' , '&' )
  if 'p2p' in o0 . lower ( ) :
   pass
  else :
   oOO00oOO ( o0 , o0O , 8 , '' , '' , '' , '' )
   if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
   if 13 - 13: Ii1I . i11iIiiIii
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
def Oo0O0oooo ( ) :
 I111iI = oOOoO0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo00O00oO = I111iI . lower ( )
 iIiIIIi ( oo00O00oO )
 if 56 - 56: I1IiiI
def iIiIIIi ( name ) :
 oo00O00oO = name
 OoOoO = { "User-Agent" : "Mozilla/5.0" }
 O0oO = [ ]
 i1I1iI = [ ]
 OO0ooOOO0OOO = [ ]
 oO00oooOOoOo0 = xbmcgui . DialogProgress ( )
 OOOO = requests . get ( 'http://www.iptvultra.com/' , headers = OoOoO ) . text
 i1I1ii = re . compile ( '<span class="link"><a href="(.+?)">(.+?)</a>' ) . findall ( OOOO )
 for o0O , name in i1I1ii :
  i1I1iI . append ( o0O [ 0 ] )
  OoO0O00IIiII = len ( i1I1iI )
 for o0O , name in i1I1ii :
  O0oO . append ( o0O [ 0 ] )
  OoOOoOooooOOo = len ( O0oO ) / float ( OoO0O00IIiII ) * 100
  oO00oooOOoOo0 . create ( 'Checking for stream' )
  oO00oooOOoOo0 . update ( int ( OoOOoOooooOOo ) , 'Checking list ' + str ( len ( O0oO ) ) + '/' + str ( len ( i1I1ii ) ) , str ( len ( OO0ooOOO0OOO ) ) + ' Results' )
  if oO00oooOOoOo0 . iscanceled ( ) :
   return
  oOo0O = requests . get ( o0O , headers = OoOoO ) . text
  Oo0 = re . compile ( '".+?[@](.+?)[@].+?[@].+?[@](.+?)"' ) . findall ( oOo0O )
  for name , OOo0oO00ooO00 in Oo0 :
   name = name . replace ( '[' , '' ) . replace ( ']' , '' )
   if name [ 0 ] == ' ' :
    name = name [ 1 : ]
   elif name [ - 1 ] == ' ' :
    name = name [ : - 1 ]
   iiIi1IIi1I = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + OOo0oO00ooO00 . replace ( '[' , '' ) . replace ( ']' , '' ) + ';name=vendetta'
   if ( oo00O00oO ) . replace ( ' ' , '' ) in ( name ) . replace ( ' ' , '' ) . lower ( ) :
    OO0ooOOO0OOO . append ( o0O [ 0 ] )
    try :
     o00OO00OoO ( name , iiIi1IIi1I , 10 , '' , '' , '' , '' )
    except :
     pass
     if 52 - 52: i11iIiiIii / o0oOOo0O0Ooo * ooOoO0o
def iIOO0O000 ( ) :
 i1iiI11I = [ 'Select by Virgin No.' , 'Select by Sky No.' , 'Select by Freeview No.' ]
 iiii = xbmcgui . Dialog ( ) . select ( 'Search by channel number' , i1iiI11I )
 if iiii == 0 :
  iiIiI1i1 (
 'http://www.tvguide.co.uk/?catcolor=&systemid=25&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ,
 'Virgin' )
 if iiii == 1 :
  iiIiI1i1 (
 'http://www.tvguide.co.uk/?catcolor=&systemid=5&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ,
 'Sky' )
 if iiii == 2 :
  iiIiI1i1 (
 'http://www.tvguide.co.uk/?catcolor=&systemid=3&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ,
 'Freeview' )
  if 69 - 69: ooOoO0o
  if 40 - 40: I1Ii111 + OoooooooOO % o0oOOo0O0Ooo - iIii1I11I1II1 . I1IiiI
def iiIiI1i1 ( url , name ) :
 iIiIi11iI = xbmcgui . Dialog ( ) . input ( "Channel No" , type = xbmcgui . INPUT_NUMERIC )
 Oo0O00O000 = requests . get ( url ) . text
 i1I1ii = re . compile ( 'qt-text="(.+?)" title="(.+?)"' ) . findall ( Oo0O00O000 )
 for i11I1IiII1i1i , oo in i1I1ii :
  oo = oo . replace ( ' TV listings' , '' )
  i11I1IiII1i1i = i11I1IiII1i1i . replace ( 'Channel Numbers<br> ' , '' )
  if ':' in i11I1IiII1i1i :
   if name == 'Sky' :
    I1111i = re . compile ( 'Sky:(.+?) ' ) . findall ( str ( i11I1IiII1i1i ) )
    for i1I1iI in I1111i :
     if iIiIi11iI in I1111i :
      iIIii ( url , str ( oo ) )
   elif name == 'Virgin' :
    o00O0O = re . compile ( 'Virgin:(.+?) ' ) . findall ( str ( i11I1IiII1i1i ) )
    for i1I1iI in o00O0O :
     if iIiIi11iI in o00O0O :
      iIIii ( url , str ( oo ) )
   elif name == 'Freeview' :
    ii1iii1i = re . compile ( 'Freeview:(.+?) ' ) . findall ( str ( i11I1IiII1i1i ) )
    for i1I1iI in ii1iii1i :
     if iIiIi11iI in ii1iii1i :
      iIIii ( url , str ( oo ) )
      if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
def ooOoO00 ( url ) :
 ooo0O = [ [ 'All' , 'http://www.tvguide.co.uk/?catcolor=&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Comedy' , 'http://www.tvguide.co.uk/?catcolor=3253CF&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Sports' , 'http://www.tvguide.co.uk/?catcolor=53CE32&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Music' , 'http://www.tvguide.co.uk/?catcolor=FF9933&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Film' , 'http://www.tvguide.co.uk/?catcolor=000000&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Soap' , 'http://www.tvguide.co.uk/?catcolor=AB337D&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Kids' , 'http://www.tvguide.co.uk/?catcolor=E3BB00&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Drama' , 'http://www.tvguide.co.uk/?catcolor=CE3D32&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Talk show' , 'http://www.tvguide.co.uk/?catcolor=800000&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Game show' , 'http://www.tvguide.co.uk/?catcolor=669999&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Sci-fi' , 'http://www.tvguide.co.uk/?catcolor=666699&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Documentary' , 'http://www.tvguide.co.uk/?catcolor=CCCCCC&systemid=' + url + '&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Motor' , 'http://www.tvguide.co.uk/?catcolor=996633&systemid=7&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Horror' , 'http://www.tvguide.co.uk/?catcolor=666633&systemid=7&thistime=' + Ii11iii11I + '&thisDay=' + iI11iiiI1II + '/' + O0oooo0Oo00 + '/' + iI + '&gridspan=03:00&view=0&gw=1323' ] ]
 for i1I1iI in ooo0O :
  o0 = i1I1iI [ 0 ]
  Ii1IIiI1i = i1I1iI [ 1 ]
  oOO00oOO ( o0 , Ii1IIiI1i , 11 , '' , '' , '' , '' )
  if 78 - 78: I1ii11iIi11i
def o0Oo0oO0oOO00 ( url ) :
 ooo0O = [ ]
 OOOO = requests . get ( url ) . text
 IIIii1II1II = re . compile ( '<div class="Block CategoryContent Moveable Panel"(.+?)<br class="Clear" />' , re . DOTALL ) . findall ( OOOO )
 for i1I1iI in IIIii1II1II :
  i1I1ii = re . compile ( '<div class="ProductImage">.+?<a href="(.+?)".+?img src="(.+?)" alt="(.+?)" />' , re . DOTALL ) . findall ( str ( i1I1iI . encode ( 'utf-8' ) ) )
  for url , O0ii1ii1ii , o0 in i1I1ii :
   o00OO00OoO ( o0 , url , 9 , O0ii1ii1ii , '' , '' , '' )
 next = re . compile ( '<div class="FloatRight"><a href="(.+?)">.+?</a>' ) . findall ( OOOO )
 for url in next :
  if 'skippy' not in ooo0O :
   oOO00oOO ( 'Next Page' , url , 8 , '' , '' , '' , '' )
   ooo0O . append ( 'skippy' )
   if 92 - 92: OoooooooOO * I1Ii111
def o0000oO ( name , url ) :
 iiIi1IIi1I = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
 OOOO = requests . get ( url ) . text
 I1II1 = re . compile ( '<source src="(.+?)"' ) . findall ( OOOO )
 for i1I1iI in I1II1 :
  iiIi1IIi1I = i1I1iI
 i1Ii ( name , iiIi1IIi1I )
 if 86 - 86: iIii1I11I1II1 / OoOoOO00 . II111iiii
 if 19 - 19: I1ii11iIi11i % OoooooooOO % IiII * o0oOOo0O0Ooo % O0
def iIIii ( url , extra ) :
 try :
  Oo0O00O000 = requests . get ( url ) . text
  ooo = re . compile ( '<div class="div-epg-channel-progs">.+?<div class="div-epg-channel-name">(.+?)</div>(.+?)</div></div></div>' , re . DOTALL ) . findall ( Oo0O00O000 )
  for iI1iII1 , IIIii1II1II in ooo :
   i1i1iI1iiiI = re . compile ( '<a qt-title="(.+?)"(.+?)onmouse' , re . DOTALL ) . findall ( str ( IIIii1II1II . encode ( 'utf-8' ) ) )
   for Ooo0oOooo0 , oOOOoo00 in i1i1iI1iiiI :
    iiIiIIIiiI = re . compile ( '(.+?)-(.+?) ' ) . findall ( str ( Ooo0oOooo0 ) )
    for iiI1IIIi , II11IiIi11 in iiIiIIIiiI :
     if 'am' in iiI1IIIi :
      IIOOO0O00O0OOOO = re . compile ( '(.+?):(.+?)am' ) . findall ( str ( iiI1IIIi ) )
      for I1iiii1I , OOo0 in IIOOO0O00O0OOOO :
       oO00ooooO0o = ( int ( I1iiii1I ) * 60 ) + int ( OOo0 )
     elif 'pm' in iiI1IIIi :
      IIOOO0O00O0OOOO = re . compile ( '(.+?):(.+?)pm' ) . findall ( str ( iiI1IIIi ) )
      for I1iiii1I , OOo0 in IIOOO0O00O0OOOO :
       if I1iiii1I == '12' :
        oO00ooooO0o = ( int ( I1iiii1I ) * 60 ) + int ( OOo0 )
       else :
        oO00ooooO0o = ( int ( I1iiii1I ) + 12 ) * 60 + int ( OOo0 )
     if 'am' in II11IiIi11 :
      IIOOO0O00O0OOOO = re . compile ( '(.+?):(.+?)am' ) . findall ( str ( II11IiIi11 ) )
      for I1iiii1I , OOo0 in IIOOO0O00O0OOOO :
       oo0o = ( int ( I1iiii1I ) * 60 ) + int ( OOo0 )
     elif 'pm' in II11IiIi11 :
      IIOOO0O00O0OOOO = re . compile ( '(.+?):(.+?)pm' ) . findall ( str ( II11IiIi11 ) )
      for I1iiii1I , OOo0 in IIOOO0O00O0OOOO :
       if I1iiii1I == '12' :
        oo0o = ( int ( I1iiii1I ) * 60 ) + int ( OOo0 )
       else :
        oo0o = ( int ( I1iiii1I ) + 12 ) * 60 + int ( OOo0 )
     if int ( oO00ooooO0o ) < int ( iI11i1I1 ) < int ( oo0o ) :
      if not extra or extra == '' :
       o0oO0oooOoo = iI1iII1 . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       oOO00oOO ( o0oO0oooOoo . encode ( 'utf-8' ) + ': ' + Ooo0oOooo0 . encode ( 'utf-8' ) , '' , 7 , '' , '' , '' , o0oO0oooOoo . replace ( 'HD' , '' ) )
      else :
       o0oO0oooOoo = iI1iII1 . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       I1III1111iIi = extra . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       if I1III1111iIi == o0oO0oooOoo :
        oOO00oOO ( o0oO0oooOoo . encode ( 'utf-8' ) + ': ' + Ooo0oOooo0 . encode ( 'utf-8' ) , '' , 7 , '' , '' , '' , o0oO0oooOoo . replace ( 'HD' , '' ) )
       else :
        pass
 except :
  pass
  if 38 - 38: iII111i + I11i / I1Ii111 % ooOoO0o - I1ii11iIi11i
def iI11 ( extra ) :
 iIiIIIi ( extra . lower ( ) . replace ( 'hd' , '' ) . replace ( ' ' , '' ) . replace ( 'christmasgold' , 'gold' ) )
 if 10 - 10: II111iiii / oO0o % OoooooooOO * I11i % I1ii11iIi11i
def i11i1 ( url ) :
 I1i11 = urllib2 . Request ( url )
 I1i11 . add_header ( 'User-Agent' ,
 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 IiIi1I1 = ''
 IiIIi1 = ''
 try :
  IiIi1I1 = urllib2 . urlopen ( I1i11 )
  IiIIi1 = IiIi1I1 . read ( )
  IiIi1I1 . close ( )
 except :
  pass
 if IiIIi1 != '' :
  return IiIIi1
 else :
  IiIIi1 = 'Opened'
  return IiIIi1
  if 47 - 47: Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / OoO0O00 - OoooooooOO
def i1Ii ( name , url ) :
 import urlresolver
 try :
  iII1i11IIi1i = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iII1i11IIi1i , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
def oOO00oOO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 if iconimage == '' :
  iconimage = ii11iIi1I
 elif iconimage == ' ' :
  iconimage = ii11iIi1I
 if fanart == '' :
  fanart = iI111I11I1I1
 elif fanart == ' ' :
  fanart = iI111I11I1I1
 O0O0o0oOOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 OOoOoOo = True
 o000ooooO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o000ooooO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o000ooooO0o . setProperty ( "Fanart_Image" , fanart )
 OOoOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0O0o0oOOO , listitem = o000ooooO0o , isFolder = True )
 return OOoOoOo
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 40 - 40: I1ii11iIi11i + i1IIi * OOooOOo
 if 85 - 85: Ii1I * Oo0Ooo . O0 - i11iIiiIii
def o00OO00OoO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 if iconimage == '' :
  iconimage = ii11iIi1I
 elif iconimage == ' ' :
  iconimage = ii11iIi1I
 if fanart == '' :
  fanart = iI111I11I1I1
 elif fanart == ' ' :
  fanart = iI111I11I1I1
 O0O0o0oOOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 OOoOoOo = True
 o000ooooO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o000ooooO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o000ooooO0o . setProperty ( "Fanart_Image" , fanart )
 OOoOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0O0o0oOOO , listitem = o000ooooO0o , isFolder = False )
 return OOoOoOo
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 18 - 18: Ii1I + IiII - O0
def o00O ( ) :
 i1Ii1i1I11Iii = [ ]
 I1i1i1 = sys . argv [ 2 ]
 if len ( I1i1i1 ) >= 2 :
  OoO0O00O0oo0O = sys . argv [ 2 ]
  I1IiI11 = OoO0O00O0oo0O . replace ( '?' , '' )
  if ( OoO0O00O0oo0O [ len ( OoO0O00O0oo0O ) - 1 ] == '/' ) :
   OoO0O00O0oo0O = OoO0O00O0oo0O [ 0 : len ( OoO0O00O0oo0O ) - 2 ]
  iI1iiiiIii = I1IiI11 . split ( '&' )
  i1Ii1i1I11Iii = { }
  for iIiIiIiI in range ( len ( iI1iiiiIii ) ) :
   i11 = { }
   i11 = iI1iiiiIii [ iIiIiIiI ] . split ( '=' )
   if ( len ( i11 ) ) == 2 :
    i1Ii1i1I11Iii [ i11 [ 0 ] ] = i11 [ 1 ]
    if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
 return i1Ii1i1I11Iii
 if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
OoO0O00O0oo0O = o00O ( )
o0O = None
o0 = None
i1iI1 = None
i11ii1ii11i = None
ooO0OoOO = None
O0O0Oo00 = None
oOoO00o = None
oO00O0 = None
IIi1IIIi = None
O00Ooo = None
if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
try :
 IIi1IIIi = OoO0O00O0oo0O [ "regexs" ]
except :
 pass
 if 35 - 35: iIii1I11I1II1
try :
 oO00O0 = int ( OoO0O00O0oo0O [ "fav_mode" ] )
except :
 pass
try :
 O0O0Oo00 = urllib . unquote_plus ( OoO0O00O0oo0O [ "extra" ] )
except :
 pass
try :
 o0O = urllib . unquote_plus ( OoO0O00O0oo0O [ "url" ] )
except :
 pass
try :
 o0 = urllib . unquote_plus ( OoO0O00O0oo0O [ "name" ] )
except :
 pass
try :
 i1iI1 = urllib . unquote_plus ( OoO0O00O0oo0O [ "iconimage" ] )
except :
 pass
try :
 i11ii1ii11i = int ( OoO0O00O0oo0O [ "mode" ] )
except :
 pass
try :
 oOoO00o = urllib . unquote_plus ( OoO0O00O0oo0O [ "fanart" ] )
except :
 pass
try :
 ooO0OoOO = urllib . unquote_plus ( OoO0O00O0oo0O [ "description" ] )
except :
 pass
try :
 I1i = urllib . unquote_plus ( OoO0O00O0oo0O [ "playitem" ] )
except :
 pass
try :
 O00Ooo = eval ( urllib . unquote_plus ( OoO0O00O0oo0O [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 IIi1IIIi = OoO0O00O0oo0O [ "regexs" ]
except :
 pass
 if 32 - 32: OoOoOO00 / OoO0O00 + OOooOOo
if i11ii1ii11i == None : I1i1I ( )
elif i11ii1ii11i == 1 : Oo0O0oooo ( )
elif i11ii1ii11i == 2 : O000OO0 ( )
elif i11ii1ii11i == 3 : OO ( )
elif i11ii1ii11i == 4 : oOo0O0Oo00oO ( )
elif i11ii1ii11i == 5 : iIOO0O000 ( )
elif i11ii1ii11i == 6 : ooOoO00 ( o0O )
elif i11ii1ii11i == 7 : iI11 ( O0O0Oo00 )
elif i11ii1ii11i == 8 : o0Oo0oO0oOO00 ( o0O )
elif i11ii1ii11i == 9 : o0000oO ( o0 , o0O )
elif i11ii1ii11i == 10 : i1Ii ( o0 , o0O )
elif i11ii1ii11i == 11 : iIIii ( o0O , O0O0Oo00 )
elif i11ii1ii11i == 12 : o00oO0oo0OO ( o0O )
elif i11ii1ii11i == 13 : o00 ( )
elif i11ii1ii11i == 14 : i1IIIiiII1 ( )
elif i11ii1ii11i == 15 : iiIIiiIi1Ii11 ( o0O , i1iI1 )
elif i11ii1ii11i == 16 : o0oOIIiIi1iI ( o0O )
elif i11ii1ii11i == 17 : ooOOoooooo ( o0 )
elif i11ii1ii11i == 18 : o00oooO0Oo ( o0O )
elif i11ii1ii11i == 19 : OOooOoooOoOo ( o0O )
elif i11ii1ii11i == 20 : i1Iii1i1I ( o0 , o0O )
elif i11ii1ii11i == 21 : I1i1Iiiii ( o0O , i1iI1 )
elif i11ii1ii11i == 22 : IIOOOO0oo0 ( o0O , i1iI1 )
elif i11ii1ii11i == 23 : I1iI1iIi111i ( o0O )
elif i11ii1ii11i == 24 : O00Oo000ooO0 ( )
elif i11ii1ii11i == 25 : O0ooo0O0oo0 ( )
elif i11ii1ii11i == 26 : Ii ( o0O )
elif i11ii1ii11i == 27 : O000oo0O ( )
if 32 - 32: iIii1I11I1II1 % iII111i
if 65 - 65: ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
