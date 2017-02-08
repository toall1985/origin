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
from datetime import datetime
from cookielib import CookieJar
import liveresolver
if 20 - 20: ooOoO0o * II111iiii
if 65 - 65: o0oOOo0O0Ooo * iIii1I11I1II1 * ooOoO0o
IiI1i = xbmc . translatePath ( 'special://home/addons/plugin.video.vendetta/' )
OOo0o0 = xbmc . translatePath ( 'special://home/userdata/addon_data' )
O0OoOoo00o = OOo0o0 + '/plugin.video.vendetta/'
iiiI11 = IiI1i + 'icon.png'
OOooO = IiI1i + 'fanart.jpg'
OOoO00o = 'plugin.video.vendetta'
II111iiiiII = xbmcaddon . Addon ( id = OOoO00o )
oOoOo00oOo = xbmcgui . Dialog ( )
Oo = xbmc . translatePath ( 'special://home/addons/' )
o00O00O0O0O = 'http://footytube.com'
OooO0OO = int ( sys . argv [ 1 ] )
if 28 - 28: II111iiii
iii11iII = datetime . now ( ) . strftime ( '%Y' )
i1I111I = datetime . now ( ) . strftime ( '%m' )
i11I1IIiiIi = datetime . now ( ) . strftime ( '%d' )
IiIiIi = datetime . now ( ) . strftime ( '%H' )
II = datetime . now ( ) . strftime ( '%M' )
iI = str ( ( int ( IiIiIi ) * 60 ) + int ( II ) )
iI11iiiI1II = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url='
O0oooo0Oo00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
if 17 - 17: iIii1I11I1II1 % ooOoO0o % i11iIiiIii . I1IiiI
if 68 - 68: I11i + OOooOOo . iIii1I11I1II1 - IiII % iIii1I11I1II1 - ooOoO0o
def oOOO00o ( ) :
 for O0O00o0OOO0 , Ii1iIIIi1ii , file in os . walk ( Oo ) :
  for dir in Ii1iIIIi1ii :
   if 'anonymous' in dir . lower ( ) :
    if II111iiiiII . getSetting ( 'Delete' ) == 'true' :
     o0oo0o0O00OO ( dir )
    else :
     oOoOo00oOo . ok ( 'Something has to go' , 'A addon has been found that is leeching content' , 'your next choice is up to you' , 'if you cancel vendetta will be removed' )
     o0oO = [ 'Remove ' + dir , 'Remove vendetta' , 'Remove both' ]
     I1i1iii = xbmcgui . Dialog ( ) . select ( 'What is going to be removed?' , o0oO )
     if I1i1iii == 0 :
      o0oo0o0O00OO ( dir )
     elif I1i1iii == 1 :
      o0oo0o0O00OO ( 'plugin.video.vendetta' )
     elif I1i1iii == 2 :
      o0oo0o0O00OO ( dir )
      o0oo0o0O00OO ( 'plugin.video.vendetta' )
     else :
      o0oo0o0O00OO ( 'plugin.video.vendetta' )
      if 20 - 20: o0oOOo0O0Ooo
def o0oo0o0O00OO ( dir ) :
 oO00 = Oo + dir
 shutil . rmtree ( oO00 )
 if 53 - 53: OoooooooOO . i1IIi
def ii1I1i1I ( ) :
 oOOO00o ( )
 OOoo0O0 ( 'Search' , '' , 28 , '' , '' , '' , '' )
 OOoo0O0 ( 'UK ONLY - Tv Guide' , '' , 2 , '' , '' , '' , '' )
 OOoo0O0 ( 'Lists' , '' , 3 , '' , '' , '' , '' )
 OOoo0O0 ( 'By Country' , '' , 4 , '' , '' , '' , '' )
 OOoo0O0 ( 'Todays Sports' , '' , 13 , '' , '' , '' , '' )
 OOoo0O0 ( 'Football Replays' , '' , 14 , '' , '' , '' , '' )
 if 41 - 41: oO0o
def ii1i1I1i ( ) :
 o0oO = [ 'Search for channel' , 'Search for live program - [COLORred]UK ONLY[/COLOR]' ]
 I1i1iii = xbmcgui . Dialog ( ) . select ( 'Search' , o0oO )
 if I1i1iii == 0 :
  o00oOO0 ( )
 elif I1i1iii == 1 :
  oOoo ( )
  if 8 - 8: OoOoOO00
def oOoo ( ) :
 o00O = oOoOo00oOo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0OOO00oo = o00O . lower ( )
 Iii111II = 'http://www.tvguide.co.uk/?catcolor=&systemid=25&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323'
 iiii11I ( OOO0OOO00oo , Iii111II , 'SEARCH_SPLIT' )
 if 96 - 96: II111iiii % Ii1I . OOooOOo + OoooooooOO * oO0o - OoOoOO00
def i11i1 ( ) :
 OOoo0O0 ( 'Search by channel number' , '' , 5 , '' , '' , '' , '' )
 OOoo0O0 ( 'Popular' , '7' , 6 , '' , '' , '' , '' )
 OOoo0O0 ( 'Freeview' , '3' , 6 , '' , '' , '' , '' )
 OOoo0O0 ( 'Sky' , '5' , 6 , '' , '' , '' , '' )
 OOoo0O0 ( 'Virgin XL' , '25' , 6 , '' , '' , '' , '' )
 OOoo0O0 ( 'Freesat' , '19' , 6 , '' , '' , '' , '' )
 OOoo0O0 ( 'BT' , '22' , 6 , '' , '' , '' , '' )
 if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
def i1I1iI ( ) :
 OOoo0O0 ( '[COLORred]Long loading time, go make a brew!! it will search each list for each channel[/COLOR]' , '' , '' , '' , '' , '' , '' )
 OOoo0O0 ( '[COLORred]Cancel at any time to move on to next channel if your happy with stream results[/COLOR]' , '' , '' , '' , '' , '' , '' )
 OOoo0O0 ( 'Mainstream Channels' , '' , 24 , '' , '' , '' , '' )
 OOoo0O0 ( 'Live on Sat' , '' , 29 , '' , '' , '' , '' )
 OOoo0O0 ( 'Wheres the match' , '' , 30 , '' , '' , '' , '' )
 if 93 - 93: iIii1I11I1II1 % oO0o * i1IIi
def Ii11Ii1I ( ) :
 O00oO = I11i1I1I ( 'http://www.wheresthematch.com/tv/home.asp' )
 oO0Oo = re . compile ( '<li><a class=".+?" href="(.+?)">(.+?)</a></li>' ) . findall ( O00oO )
 for Iii111II , oOOoo0Oo in oO0Oo :
  if not 'on TV' in oOOoo0Oo :
   OOoo0O0 ( oOOoo0Oo , Iii111II , 31 , '' , '' , '' , '' )
   if 78 - 78: I11i
def OO00Oo ( url ) :
 O00oO = I11i1I1I ( url )
 oO0Oo = re . compile ( '<td class="fixture-details">.+?<a class=" eventlink" href=".+?"><strong class="">(.+?)</strong></a></span>.+?<em class="">(.+?)</em>.+?class="time-channel ">.+?at (.+?) on (.+?) </span></span>' , re . DOTALL ) . findall ( O00oO )
 for O0OOO0OOoO0O , O00Oo000ooO0 , OoO0O00IIiII , o0 in oO0Oo :
  OOoo0O0 ( o0 + ':' + OoO0O00IIiII + ':' + O0OOO0OOoO0O + ':' + O00Oo000ooO0 , '' , 7 , '' , '' , '' , o0 )
 else :
  OOoo0O0 ( 'No listing today please check back another day' , '' , '' , '' , '' , '' , '' )
  if 62 - 62: iIii1I11I1II1 * OoOoOO00
def i1 ( ) :
 OOoo0O0 ( 'LiveOnSat Football - Some searchs may take a sec - if empty menu means no results' , 'http://liveonsat.com/daily.php' , 25 , '' , '' , '' , '' )
 OOoo0O0 ( 'LiveOnSat Boxing - Some searchs may take a sec - if empty menu means no results' , 'http://liveonsat.com/los_other_boxing.php' , 25 , '' , '' , '' , '' )
 OOoo0O0 ( 'LiveOnSat Rugby Union - Some searchs may take a sec - if empty menu means no results' , 'http://liveonsat.com/los_other_rugby_U.php' , 25 , '' , '' , '' , '' )
 OOoo0O0 ( 'LiveOnSat FIBA - Some searchs may take a sec - if empty menu means no results' , 'http://liveonsat.com/images/sport_fiba.jpg' , 25 , '' , '' , '' , '' )
 OOoo0O0 ( 'LiveOnSat NBA- Some searchs may take a sec - if empty menu means no results' , 'http://liveonsat.com/los_US_basketball.php' , 25 , '' , '' , '' , '' )
 OOoo0O0 ( 'LiveOnSat Handball - Some searchs may take a sec - if empty menu means no results' , 'http://liveonsat.com/los_other_handball.php' , 25 , '' , '' , '' , '' )
 OOoo0O0 ( 'LiveOnSat F1 - Some searchs may take a sec - if empty menu means no results' , 'http://liveonsat.com/los_other_motor.php' , 25 , '' , '' , '' , '' )
 OOoo0O0 ( 'LiveOnSat Other - Some searchs may take a sec - if empty menu means no results' , 'http://liveonsat.com/los_other_GAA.php' , 25 , '' , '' , '' , '' )
 if 91 - 91: OoO0O00 . I1ii11iIi11i + OoO0O00 - iII111i / OoooooooOO
 if 39 - 39: I1ii11iIi11i / ooOoO0o - II111iiii
 if 98 - 98: I1ii11iIi11i / I11i % oO0o . OoOoOO00
def oOOOO00O0O0 ( ) :
 O00oO = I11i1I1I ( 'http://www.live-footballontv.com/' )
 oO0oo0o = re . compile ( '<div id="listings"><div class="container" align="center"><div class="row-fluid"><div class="span12 matchdate">(.+?)<div class="span12 matchdate">' , re . DOTALL ) . findall ( O00oO )
 II11i1I11Ii1i = re . compile ( 'span4 matchfixture">(.+?)</div>.+?span4 competition">(.+?)</div>.+?span1 kickofftime">(.+?)</div>.+?span3 channels">(.+?)</div>' ) . findall ( str ( oO0oo0o ) )
 for oOOoo0Oo , O000O0oOO0 , O0ooo0O0oo0 , oo0oOo in II11i1I11Ii1i :
  o000O0o = ( oOOoo0Oo ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  iI1iII1 = ( O000O0oOO0 ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  oO0OOoo0OO = ( oo0oOo ) . replace ( '&nbsp;' , '-' ) . replace ( '-' , '' ) . replace ( '&#039;' , '\'' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  OOoo0O0 ( O0ooo0O0oo0 + ' : ' + o000O0o + ' - ' + oO0OOoo0OO , oO0OOoo0OO , 26 , '' , '' , iI1iII1 , '' )
  if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
def iii1i1iiiiIi ( url ) :
 O00oO = I11i1I1I ( url )
 Iiii = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( O00oO )
 for O000O0oOO0 , OO0OoO0o00 , O0ooo0O0oo0 , ooOO0O0ooOooO in Iiii :
  oOOOo00O00oOo = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( ooOO0O0ooOooO )
  iiIIIi = ( str ( oOOOo00O00oOo ) ) . replace ( '[$]' , '' ) . replace ( '\\xc3' , 'n' ) . replace ( '\'' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\\xe2' , '' ) . replace ( '\\x80' , '' ) . replace ( '\\x99' , '' ) . replace ( '\\xb1a' , 'i' )
  oOOoo0Oo = str ( O000O0oOO0 ) + ' - ' + str ( O0ooo0O0oo0 )
  ooo00OOOooO = 'http://liveonsat.com' + str ( OO0OoO0o00 )
  OOoo0O0 ( oOOoo0Oo , ( iiIIIi ) . replace ( ',' , '/' ) . replace ( '|' , '' ) , 26 , ooo00OOOooO , '' , iiIIIi , '' )
  if 67 - 67: I11i * oO0o * I1ii11iIi11i + OOooOOo / i1IIi
  if 11 - 11: Ii1I + iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
def o0oOIIiIi1iI ( url ) :
 i1IiiiI1iI = [ ]
 i1iIi = url + '/'
 oO0Oo = re . compile ( '(.+?)/' ) . findall ( str ( i1iIi ) )
 for url in oO0Oo :
  if 'HD' in url :
   url = ( url ) . replace ( 'HD' , '' )
  elif '(' in url :
   ooOOoooooo = re . compile ( '(.+?)\(' ) . findall ( str ( url ) )
   for II1I in ooOOoooooo :
    url = II1I
    if url not in i1IiiiI1iI :
     OOO0OOO00oo = ( url ) . lower ( )
     O0i1II1Iiii1I11 ( OOO0OOO00oo )
     i1IiiiI1iI . append ( url )
  else :
   if url not in i1IiiiI1iI :
    OOO0OOO00oo = ( url ) . lower ( )
    O0i1II1Iiii1I11 ( OOO0OOO00oo )
    i1IiiiI1iI . append ( url )
    if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
def o00oooO0Oo ( ) :
 if 78 - 78: Ii1I % I1Ii111 + I1ii11iIi11i
 OOoo0O0 ( 'Footy Tube' , 'http://www.footytube.com/leagues' , 16 , iiiI11 , OOooO , '' , '' )
 OOoo0O0 ( 'Latest' , 'http://www.fullmatchesandshows.com' , 15 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , OOooO , '' , '' )
 OOoo0O0 ( 'Shows' , 'http://www.fullmatchesandshows.com/category/show/' , 15 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , OOooO , '' , '' )
 OOoo0O0 ( 'Premier League' , 'http://www.fullmatchesandshows.com/premier-league/' , 15 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , OOooO , '' , '' )
 OOoo0O0 ( 'La Liga' , 'http://www.fullmatchesandshows.com/la-liga/' , 15 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , OOooO , '' , '' )
 OOoo0O0 ( 'Bundesliga' , 'http://www.fullmatchesandshows.com/bundesliga/' , 15 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , OOooO , '' , '' )
 OOoo0O0 ( 'Champions League' , 'http://www.fullmatchesandshows.com/champions-league/' , 15 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , OOooO , '' , '' )
 OOoo0O0 ( 'Serie A' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 15 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , OOooO , '' , '' )
 OOoo0O0 ( 'Ligue 1' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 15 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , OOooO , '' , '' )
 if 64 - 64: oO0o * O0 . I1IiiI + II111iiii
def IIi1i ( url ) :
 O00oO = I11i1I1I ( url )
 OOOO00O0O = re . compile ( '<div class="headline_xlrg color_dgray"><img align="absmiddle" height="22" src="(.+?)">(.+?)</div>' ) . findall ( O00oO )
 for OO0OoO0o00 , oOOoo0Oo in OOOO00O0O :
  OOoo0O0 ( oOOoo0Oo , '' , 17 , o00O00O0O0O + OO0OoO0o00 , OOooO , '' , '' )
  xbmcplugin . addSortMethod ( OooO0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 33 - 33: O0 . IiII . I1IiiI
def OoOO ( name ) :
 Iii111II = 'http://www.footytube.com/leagues'
 ooOOO0 = name
 O00oO = I11i1I1I ( Iii111II )
 OOOO00O0O = re . compile ( '<div class="headline_xlrg color_dgray"><img align="absmiddle" height="22" src="(.+?)">' + name + '</div>(.+?)<div style="margin-bottom: 15px">' , re . DOTALL ) . findall ( O00oO )
 for OO0OoO0o00 , oO0oo0o in OOOO00O0O :
  o0o = re . compile ( '<div>.+?<a href="(.+?)" class="standard_link">(.+?)</a><br>.+?<span class="text_xsml">(.+?)</span>.+?</div>' , re . DOTALL ) . findall ( str ( oO0oo0o ) )
  for Iii111II , name , O0OOoO00OO0o in o0o :
   OOoo0O0 ( name + ' - ' + O0OOoO00OO0o , o00O00O0O0O + Iii111II , 18 , iiiI11 , OOooO , '' , '' )
  else :
   pass
   if 38 - 38: OOooOOo % I11i % o0oOOo0O0Ooo % OoO0O00 - Oo0Ooo
def i1Ii ( url ) :
 O00oO = I11i1I1I ( url )
 oO0Oo = re . compile ( '<div class=".+?" style = ".+?"><a href="(.+?)" class=".+?" >(.+?)</a></div>' ) . findall ( O00oO )
 for url , oOOoo0Oo in oO0Oo :
  OOoo0O0 ( oOOoo0Oo , o00O00O0O0O + url , 19 , iiiI11 , OOooO , '' , '' )
  if 14 - 14: iII111i
def I1iI1iIi111i ( url ) :
 O00oO = I11i1I1I ( url )
 oO0Oo = re . compile ( ' <div class="thumboverlay"> .+?<div><a href="(.+?)".+?<img src="(.+?)" width="165px" height="97px" /></a></div>.+?<div class="vid_title".+?class="standard_link">(.+?)</a><div class="vid_info">(.+?)</div>' , re . DOTALL ) . findall ( O00oO )
 for url , OO0OoO0o00 , oOOoo0Oo , iiIi1IIi1I in oO0Oo :
  o0OoOO000ooO0 ( oOOoo0Oo + ' - ' + iiIi1IIi1I , o00O00O0O0O + url , 20 , OO0OoO0o00 , OOooO , '' , '' )
  if 56 - 56: iII111i
  if 86 - 86: II111iiii % I1Ii111
def iiIIiiIi1Ii11 ( name , url ) :
 O00oO = I11i1I1I ( url )
 oO0Oo = re . compile ( '<iframe src="(.+?)" width=' ) . findall ( O00oO )
 for url in oO0Oo :
  url = o00O00O0O0O + url
  Oo0 ( url )
 oOooo0O0Oo = re . compile ( '<iframe id="ft_player" width="100%" height="100%" src="http://www.youtube.com/embed/(.+?)?rel=0&autoplay=1&enablejsapi=1" frameborder="0" allowfullscreen></iframe>' ) . findall ( O00oO )
 for url in oOooo0O0Oo :
  url = 'plugin://plugin.video.youtube/play/?video_id=' + url
  iIo0O ( name , url )
  if 2 - 2: iIii1I11I1II1 / oO0o + OoO0O00 / OOooOOo
def IIOOOO0oo0 ( url ) :
 O00oO = I11i1I1I ( url )
 oOooo0O0Oo = re . compile ( '<iframe width="560" height="315" src="https://www.youtube.com/embed/(.+?)" frameborder="0" allowfullscreen>' ) . findall ( O00oO )
 for url in oOooo0O0Oo :
  yt . PlayVideo ( url )
 oO0Oo = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( O00oO )
 for I11iiI1i1 in oO0Oo :
  if 'div' in I11iiI1i1 :
   pass
  else :
   I1i1Iiiii = ( I11iiI1i1 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
   iIo0O ( 'Enjoy' , 'http:' + I1i1Iiiii )
   if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
def Oo0 ( url ) :
 O00oO = I11i1I1I ( url )
 oOooo0O0Oo = re . compile ( '<iframe width="560" height="315" src="https://www.youtube.com/embed/(.+?)" frameborder="0" allowfullscreen>' ) . findall ( O00oO )
 for url in oOooo0O0Oo :
  url = 'plugin://plugin.video.youtube/play/?video_id=' + url
  iIo0O ( oOOoo0Oo , url )
 oO0Oo = re . compile ( '<script data-config="(.+?)" data-css=".+?" data-height="100%" data-width="100%" src=".+?" type="text/javascript"></script>' ) . findall ( O00oO )
 for I11iiI1i1 in oO0Oo :
  if 'div' in I11iiI1i1 :
   pass
  else :
   I1i1Iiiii = ( I11iiI1i1 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
   iIo0O ( 'Enjoy' , 'http:' + I1i1Iiiii )
   if 87 - 87: Oo0Ooo . IiII
def O0OO0O ( url , iconimage ) :
 O00oO = I11i1I1I ( url )
 OO = re . compile ( '<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)".+?"entry-thumb" src="(.+?)"' ) . findall ( O00oO )
 for url , oOOoo0Oo , OO0OoO0o00 in OO :
  if 'Full Match' in oOOoo0Oo :
   O00Oo000ooO0 = oOOoo0Oo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OOoo0O0 ( O00Oo000ooO0 , url , 21 , OO0OoO0o00 , '' , '' , '' )
  else :
   O00Oo000ooO0 = oOOoo0Oo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   o0OoOO000ooO0 ( O00Oo000ooO0 , url , 23 , OO0OoO0o00 , '' , '' , '' )
 OoOoO = re . compile ( '<span class="current">.+?</span><a href="(.+?)" class="page" title=".+?">(.+?)</a>' ) . findall ( O00oO )
 for url , oOOoo0Oo in OoOoO :
  OOoo0O0 ( 'NEXT PAGE' , url , 22 , iconimage , OOooO , '' , '' )
  if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
def o00oO0oo0OO ( url , iconimage ) :
 O00oO = I11i1I1I ( url )
 oO0oo0o = re . compile ( '<div class="td-block-span6">(.+?)<div class="td-pb-span4 td-main-sidebar">' , re . DOTALL ) . findall ( O00oO )
 OO = re . compile ( '<div class="td-module-thumb"><a href="(.+?)".+?title="(.+?)".+?"entry-thumb" src="(.+?)"' ) . findall ( str ( oO0oo0o ) )
 for url , oOOoo0Oo , OO0OoO0o00 in OO :
  if 'Full Match' in oOOoo0Oo :
   O00Oo000ooO0 = oOOoo0Oo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OOoo0O0 ( O00Oo000ooO0 , url , 21 , OO0OoO0o00 , '' , '' , '' )
  else :
   O00Oo000ooO0 = oOOoo0Oo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   o0OoOO000ooO0 ( O00Oo000ooO0 , url , 23 , OO0OoO0o00 , '' , '' , '' )
 OoOoO = re . compile ( '<span class="current">.+?</span><a href="(.+?)" class="page" title=".+?">(.+?)</a>' ) . findall ( O00oO )
 for url , oOOoo0Oo in OoOoO :
  OOoo0O0 ( 'NEXT PAGE' , url , 22 , iconimage , OOooO , '' , '' )
 if len ( OO ) <= 0 :
  OOoo0O0 ( 'No Replays available sorry' , url , 22 , iconimage , OOooO , '' , '' )
  if 57 - 57: I1Ii111 % Ii1I + o0oOOo0O0Ooo - Oo0Ooo
def o0O ( url , iconimage ) :
 o0OoOO000ooO0 ( 'Extended Highlights' , url , 23 , iconimage , OOooO , '' , '' )
 O00oO = I11i1I1I ( url )
 oO0Oo = re . compile ( '<link href=".+?" rel="stylesheet" type="text/css"><li tabindex="0" class="button_style" id=".+?"><a href="(.+?)"><div class="acp_title">(.+?)</div></a></li>' ) . findall ( O00oO )
 for IiI1io0O , oOOoo0Oo in oO0Oo :
  url = url + IiI1io0O
  oOOoo0Oo = ( oOOoo0Oo ) . replace ( 'HL English' , 'English Highlights' )
  o0OoOO000ooO0 ( oOOoo0Oo , url , 23 , iconimage , OOooO , '' , '' )
  if 90 - 90: OOooOOo . I1IiiI * I1IiiI
def I111I1Iiii1i ( ) :
 oOOoo00O00o = { "User-Agent" : "Mozilla/5.0" }
 O00oO = requests . get ( 'http://www.iptvultra.com/' , headers = oOOoo00O00o ) . text
 oO0Oo = re . compile ( '<span class="link"><a href="(.+?)">(.+?)</a>' ) . findall ( O00oO )
 for Iii111II , oOOoo0Oo in oO0Oo :
  if 'Premium List IPTV' in oOOoo0Oo :
   pass
  else :
   OOoo0O0 ( oOOoo0Oo , Iii111II , 12 , '' , '' , '' , '' )
   if 98 - 98: OOooOOo + IiII + oO0o % OoooooooOO
def oooooo0O000o ( url ) :
 oOOoo00O00o = { "User-Agent" : "Mozilla/5.0" }
 O00oO = requests . get ( url , headers = oOOoo00O00o ) . text
 oO0Oo = re . compile ( '".+?[@](.+?)[@].+?[@].+?[@](.+?)"' ) . findall ( O00oO )
 for oOOoo0Oo , IiI1io0O in oO0Oo :
  try :
   oOOoo0Oo = oOOoo0Oo . replace ( '[' , '' ) . replace ( ']' , '' )
   if oOOoo0Oo [ 0 ] == ' ' :
    oOOoo0Oo = oOOoo0Oo [ 1 : ]
   if oOOoo0Oo [ - 1 ] == ' ' :
    oOOoo0Oo = oOOoo0Oo [ : - 1 ]
   OoO = iI11iiiI1II + IiI1io0O . replace ( '[' , '' ) . replace ( ']' , '' ) + ';name=vendetta'
   o0OoOO000ooO0 ( oOOoo0Oo , OoO , 10 , '' , '' , '' , '' )
  except :
   pass
   if 51 - 51: OoooooooOO * OOooOOo
def OO0ooOOO0OOO ( ) :
 O00oO = requests . get ( 'http://www.shadow-net.org' ) . text
 oO0Oo = re . compile ( '<li class=""><a href="(.+?)">(.+?)</a>' ) . findall ( O00oO )
 for Iii111II , oOOoo0Oo in oO0Oo :
  oOOoo0Oo = oOOoo0Oo . replace ( '&amp;' , '&' )
  if 'p2p' in oOOoo0Oo . lower ( ) :
   pass
  else :
   OOoo0O0 ( oOOoo0Oo , Iii111II , 8 , '' , '' , '' , '' )
   if 63 - 63: OoOoOO00 * iII111i
oo = [ [ '4Music | Direct' , 'http://llnw.live.btv.simplestream.com/coder9/coder.channels.channel6/hls/4/playlist.m3u8' , 1201 ] ,
 [ '4Music | TVPlayer' , '128' , 1202 ] ,
 [ '5* | FilmOn' , 'https://www.filmon.com/tv/5-star' , 1201 ] ,
 [ '5USA | FilmOn' , 'https://www.filmon.com/tv/5usa' , 1201 ] ,
 [ 'Al Jazeera | TVPlayer' , '146' , 1202 ] ,
 [ 'Al Jazeera | FilmOn' , 'https://www.filmon.com/tv/al-jazeera' , 1201 ] ,
 [ 'BBC Alba | TVPlayer' , '236' , 1202 ] ,
 [ 'BBC Alba | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_1/live/bbc_alba/bbc_alba.isml/bbc_alba-pa3%3d96000-video%3d1604032.norewind.m3u8' , 1201 ] ,
 [ 'BBC Four HD | BBC iPlayer' , 'http://vs-hls-uk-live.akamaized.net/pool_33/live/bbc_four_hd/bbc_four_hd.isml/bbc_four_hd-pa4%3d128000-video%3d5070016.m3u8' , 1201 ] ,
 [ 'BBC Four | TVPlayer' , '110' , 1202 ] ,
 [ 'BBC Four | FilmOn' , 'https://www.filmon.com/tv/cbeebiesbbc-four' , 1201 ] ,
 [ 'BBC News HD | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_34/live/bbc_news_channel_hd/bbc_news_channel_hd.isml/bbc_news_channel_hd-pa4%3d128000-video%3d5070016.m3u8' , 1201 ] ,
 [ 'BBC News | TVPlayer' , '111' , 1202 ] ,
 [ 'BBC News | FilmOn' , 'https://www.filmon.com/tv/bbc-news' , 1201 ] ,
 [ 'BBC 1 HD | BBC iPlayer' , 'http://vs-hls-uk-live.akamaized.net/pool_30/live/bbc_one_hd/bbc_one_hd.isml/bbc_one_hd-pa4%3d128000-video%3d5070016.m3u8' , 1201 ] ,
 [ 'BBC 1 | TVPlayer' , '89' , 1202 ] ,
 [ 'BBC 1 | FilmOn' , 'https://www.filmon.com/tv/bbc-one' , 1201 ] ,
 [ 'BBC 1 Northern Ireland | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_4/live/bbc_one_northern_ireland_hd/bbc_one_northern_ireland_hd.isml/bbc_one_northern_ireland_hd-pa4%3d128000-video%3d5070016.m3u8' , 1201 ] ,
 [ 'BBC 1 Northern Ireland | FilmOn' , 'https://www.filmon.com/tv/bbc-1-north-ireland' , 1201 ] ,
 [ 'BBC 1 Scotland | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_5/live/bbc_one_scotland_hd/bbc_one_scotland_hd.isml/bbc_one_scotland_hd-pa4%3d128000-video%3d5070016.m3u8' , 1201 ] ,
 [ 'BBC 1 Scotland | FilmOn' , 'https://www.filmon.com/tv/bbc-1-scotland' , 1201 ] ,
 [ 'BBC 1 Wales | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_3/live/bbc_one_wales_hd/bbc_one_wales_hd.isml/bbc_one_wales_hd-pa4%3d128000-video%3d5070016.m3u8' , 1201 ] ,
 [ 'BBC 1 Wales | FilmOn' , 'https://www.filmon.com/tv/bbc-1-wales' , 1201 ] ,
 [ 'BBC 2 Northern Ireland | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_5/live/bbc_two_northern_ireland_digital/bbc_two_northern_ireland_digital.isml/bbc_two_northern_ireland_digital-pa3%3d96000-video%3d1604032.norewind.m3u8' , 1201 ] ,
 [ 'BBC 2 Scotland | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_5/live/bbc_two_scotland/bbc_two_scotland.isml/bbc_two_scotland-pa3%3d96000-video%3d1604032.norewind.m3u8' , 1201 ] ,
 [ 'BBC 2 Wales | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_5/live/bbc_two_wales_digital/bbc_two_wales_digital.isml/bbc_two_wales_digital-pa3%3d96000-video%3d1604032.norewind.m3u8' , 1201 ] ,
 [ 'BBC Parliament | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_1/live/bbc_parliament/bbc_parliament.isml/bbc_parliament-pa3%3d96000-video%3d1604032.norewind.m3u8' , 1201 ] ,
 [ 'BBC Parliament | TVPlayer' , '345' , 1202 ] ,
 [ 'BBC Parliament | FilmOn' , 'https://www.filmon.com/tv/bbc-parliament' , 1201 ] ,
 [ 'BBC 2 HD | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_31/live/bbc_two_hd/bbc_two_hd.isml/bbc_two_hd-pa4%3d128000-video%3d5070016.m3u8' , 1201 ] ,
 [ 'BBC 2 | TVPlayer' , '90' , 1202 ] ,
 [ 'BBC 2 | FilmOn' , 'https://www.filmon.com/tv/bbc-two' , 1201 ] ,
 [ 'Bloomberg | TVPlayer' , '514' , 1202 ] ,
 [ 'Bloomberg | FilmOn' , 'https://www.filmon.com/tv/bloomberg' , 1201 ] ,
 [ 'The Box | Direct' , 'http://llnw.live.btv.simplestream.com/coder9/coder.channels.channel12/hls/4/playlist.m3u8' , 1201 ] ,
 [ 'The Box | TVPlayer' , '129' , 1202 ] ,
 [ 'Box Hits | Direct' , 'http://llnw.live.btv.simplestream.com/coder9/coder.channels.channel2/hls/4/playlist.m3u8' , 1201 ] ,
 [ 'Box Hits | TVPlayer' , '130' , 1202 ] ,
 [ 'Box Upfront | Direct' , 'http://llnw.live.btv.simplestream.com/coder9/coder.channels.channel8/hls/4/playlist.m3u8' , 1201 ] ,
 [ 'Box Upfront | TVPlayer' , '158' , 1202 ] ,
 [ 'Capital TV | Direct' , 'http://ooyalahd2-f.akamaihd.net/i/globalradio01_delivery@156521/index_656_av-p.m3u8?sd=10&rebase=on' , 1201 ] ,
 [ 'Capital TV | TVPlayer' , '157' , 1202 ] ,
 [ 'CBBC HD | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_1/live/cbbc_hd/cbbc_hd.isml/cbbc_hd-pa4%3d128000-video%3d5070016.m3u8' , 1201 ] ,
 [ 'CBBC | TVPlayer' , '113' , 1202 ] ,
 [ 'CBBC | FilmOn' , 'https://www.filmon.com/tv/cbbc' , 1201 ] ,
 [ 'CBeebies HD | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_2/live/cbeebies_hd/cbeebies_hd.isml/cbeebies_hd-pa4%3d128000-video%3d5070016.m3u8' , 1201 ] ,
 [ 'CBeebies | TVPlayer' , '114' , 1202 ] ,
 [ 'CBeebies | FilmOn' , 'https://www.filmon.com/tv/cbeebies' , 1201 ] ,
 [ 'CBS Action | FilmOn' , 'https://www.filmon.com/tv/cbs-action' , 1201 ] ,
 [ 'CBS Drama | FilmOn' , 'https://www.filmon.com/tv/cbs-drama' , 1201 ] ,
 [ 'CBS Reality | FilmOn' , 'https://www.filmon.com/tv/cbs-reality' , 1201 ] ,
 [ 'CBS Reality+1 | FilmOn' , 'https://www.filmon.com/tv/cbs-reality1' , 1201 ] ,
 [ 'Channel 4 | TVPlayer' , '92' , 1202 ] ,
 [ 'Channel 4 | FilmOn' , 'https://www.filmon.com/tv/channel-4' , 1201 ] ,
 [ 'Channel 5 | TVPlayer' , '93' , 1202 ] ,
 [ 'Channel 5 | FilmOn' , 'https://www.filmon.com/tv/channel-5' , 1201 ] ,
 [ 'Channel AKA | Direct' , 'http://rrr.sz.xlcdn.com/?account=AATW&file=akanew&type=live&service=wowza&protocol=http&output=playlist.m3u8' , 1201 ] ,
 [ 'Channel AKA | TVPlayer' , '227' , 1202 ] ,
 [ 'Chilled | TVPlayer' , '226' , 1202 ] ,
 [ 'CITV | ITV Hub' , 'http://citvliveios-i.akamaihd.net/hls/live/207267/itvlive/CITVMN/master_Main1800.m3u8' , 1201 ] ,
 [ 'Clubbing TV | FilmOn' , 'https://www.filmon.com/tv/clubbing-tv' , 1201 ] ,
 [ 'Clubland | TVPlayer' , '225' , 1202 ] ,
 [ 'CNN International | TVPlayer' , '286' , 1202 ] ,
 [ 'Community Channel | TVPlayer' , '259' , 1202 ] ,
 [ 'The Craft Channel | TVPlayer' , '554' , 1202 ] ,
 [ 'Dave | TVPlayer' , '300' , 1202 ] ,
 [ 'Dave ja vu | TVPlayer' , '317' , 1202 ] ,
 [ 'Drama | TVPlayer' , '346' , 1202 ] ,
 [ 'E4 | FilmOn' , 'https://www.filmon.com/tv/e4' , 1201 ] ,
 [ 'Film4 | FilmOn' , 'https://www.filmon.com/tv/film-4' , 1201 ] ,
 [ 'Food Network | TVPlayer' , '125' , 1202 ] ,
 [ 'Food Network | FilmOn' , 'http://www.filmon.com/tv/food-network' , 1201 ] ,
 [ 'Food Network+1 | TVPlayer' , '254' , 1202 ] ,
 [ 'Food Network+1 | FilmOn' , 'http://www.filmon.com/tv/food-network-plus-1' , 1201 ] ,
 [ 'Forces TV | TVPlayer' , '555' , 1202 ] ,
 [ 'Heart TV | Direct' , 'http://ooyalahd2-f.akamaihd.net/i/globalradio02_delivery@156522/master.m3u8' , 1201 ] ,
 [ 'Heart TV | TVPlayer' , '153' , 1202 ] ,
 [ 'Home | TVPlayer' , '512' , 1202 ] ,
 [ 'Horror Channel | FilmOn' , 'https://www.filmon.com/tv/horror-channel' , 1201 ] ,
 [ 'ITV1 | ITV Hub' , 'http://itv1liveios-i.akamaihd.net/hls/live/203437/itvlive/ITV1MN/master_Main1800.m3u8' , 1201 ] ,
 [ 'ITV1 | TVPlayer' , '204' , 1202 ] ,
 [ 'ITV1 | FilmOn' , 'http://www.filmon.com/tv/itv1' , 1201 ] ,
 [ 'ITV1+1 | FilmOn' , 'https://www.filmon.com/tv/itv-plus-1' , 1201 ] ,
 [ 'ITV2 | ITV Hub' , 'http://itv2liveios-i.akamaihd.net/hls/live/203495/itvlive/ITV2MN/master_Main1800.m3u8' , 1201 ] ,
 [ 'ITV2 | FilmOn' , 'http://www.filmon.com/tv/itv2' , 1201 ] ,
 [ 'ITV2+1 | FilmOn' , 'https://www.filmon.com/tv/itv2-plus-1' , 1201 ] ,
 [ 'ITV3 | ITV Hub' , 'http://itv3liveios-i.akamaihd.net/hls/live/207262/itvlive/ITV3MN/master_Main1800.m3u8' , 1201 ] ,
 [ 'ITV3 | FilmOn' , 'http://www.filmon.com/tv/itv3' , 1201 ] ,
 [ 'ITV3+1 | FilmOn' , 'https://www.filmon.com/tv/itv3-plus-1' , 1201 ] ,
 [ 'ITV4 | ITV Hub' , 'http://itv4liveios-i.akamaihd.net/hls/live/207266/itvlive/ITV4MN/master_Main1800.m3u8' , 1201 ] ,
 [ 'ITV4 | FilmOn' , 'http://www.filmon.com/tv/itv4' , 1201 ] ,
 [ 'ITV4+1 | FilmOn' , 'https://www.filmon.com/tv/itv4-plus-1' , 1201 ] ,
 [ 'ITVBe | ITV Hub' , 'http://itvbeliveios-i.akamaihd.net/hls/live/219078/itvlive/ITVBE/master_Main1800.m3u8' , 1201 ] ,
 [ 'ITVBe | FilmOn' , 'http://www.filmon.com/tv/itvbe' , 1201 ] ,
 [ 'The Jewellery Channel | Direct' , 'https://d2hee8qk5g0egz.cloudfront.net/live/tjc_sdi1/bitrate1.isml/bitrate1-audio_track=64000-video=1800000.m3u8' , 1201 ] ,
 [ 'The Jewellery Channel | TVPlayer' , '545' , 1202 ] ,
 [ 'Keep It Country | TVPlayer' , '569' , 1202 ] ,
 [ 'Kerrang! | Direct' , 'http://llnw.live.btv.simplestream.com/coder11/coder.channels.channel4/hls/4/playlist.m3u8' , 1201 ] ,
 [ 'Kerrang! | TVPlayer' , '133' , 1202 ] ,
 [ 'Kiss | Direct' , 'http://llnw.live.btv.simplestream.com/coder9/coder.channels.channel14/hls/4/playlist.m3u8' , 1201 ] ,
 [ 'Kiss | TVPlayer' , '131' , 1202 ] ,
 [ 'Kix! | FilmOn' , 'https://www.filmon.com/tv/kix' , 1201 ] ,
 [ 'London Live | Direct' , 'http://bcoveliveios-i.akamaihd.net/hls/live/217434/3083279840001/master_900.m3u8' , 1201 ] ,
 [ 'Magic | Direct' , 'http://llnw.live.btv.simplestream.com/coder11/coder.channels.channel2/hls/4/playlist.m3u8' , 1201 ] ,
 [ 'Magic | TVPlayer' , '132' , 1202 ] ,
 [ 'More4 | FilmOn' , 'https://www.filmon.com/tv/more4' , 1201 ] ,
 [ 'NOW Music | Direct' , 'http://rrr.sz.xlcdn.com/?account=AATW&file=nowmusic&type=live&service=wowza&protocol=http&output=playlist.m3u8' , 1201 ] ,
 [ 'NOW Music | TVPlayer' , '228' , 1202 ] ,
 [ 'POP | FilmOn' , 'https://www.filmon.com/tv/pop' , 1201 ] ,
 [ 'Pick | FilmOn' , 'https://www.filmon.com/tv/pick-tv' , 1201 ] ,
 [ 'QUEST | TVPlayer' , '327' , 1202 ] ,
 [ 'QUEST | FilmOn' , 'http://www.filmon.tv/tv/quest' , 1201 ] ,
 [ 'QUEST+1 | TVPlayer' , '336' , 1202 ] ,
 [ 'QVC Beauty | TVPlayer' , '250' , 1202 ] ,
 [ 'QVC Extra | TVPlayer' , '248' , 1202 ] ,
 [ 'QVC Plus | TVPlayer' , '344' , 1202 ] ,
 [ 'QVC Style | TVPlayer' , '249' , 1202 ] ,
 [ 'QVC | TVPlayer' , '247' , 1202 ] ,
 [ 'Really | TVPlayer' , '306' , 1202 ] ,
 [ 'Really | FilmOn' , 'http://www.filmon.tv/tv/really' , 1201 ] ,
 [ 'S4C | BBC iPlayer' , 'http://vs-hls-uk-live.edgesuite.net/pool_9/live/s4cpbs/s4cpbs.isml/s4cpbs-pa3%3d96000-video%3d1604032.norewind.m3u8' , 1201 ] ,
 [ 'S4C | TVPlayer' , '251' , 1202 ] ,
 [ 'Sky News | YouTube' , 'https://www.youtube.com/watch?v=y60wDzZt8yg' , 1201 ] ,
 [ 'Tiny Pop | FilmOn' , 'https://www.filmon.com/tv/tiny-pop' , 1201 ] ,
 [ 'Travel Channel | TVPlayer' , '126' , 1202 ] ,
 [ 'Travel Channel+1 | TVPlayer' , '255' , 1202 ] ,
 [ 'Travel Channel+1 | FilmOn' , 'http://www.filmon.tv/tv/travel-channel1' , 1201 ] ,
 [ 'Yesterday | TVPlayer' , '308' , 1202 ] ,
 [ 'Yesterday | FilmOn' , 'http://www.filmon.tv/tv/yesterday' , 1201 ] ,
 [ 'Yesterday+1 | TVPlayer' , '318' , 1202 ] ,
 [ 'truTV | Direct' , 'http://llnw.live.btv.simplestream.com/coder5/coder.channels.channel2/hls/4/playlist.m3u8' , 1201 ] ,
 [ 'truTV | TVPlayer' , '295' , 1202 ] ,
 [ 'truTV | FilmOn' , 'http://www.filmon.tv/tv/tru-tv' , 1201 ] ,
 [ 'Blaze | Direct' , 'http://live.blaze.simplestreamcdn.com/live/blaze/bitrate1.isml/bitrate1-audio_track=64000-video=3500000.m3u8' , 1201 ] ]
if 44 - 44: oO0o / I11i / I11i
OOO = [ [ 'Sony SIX' , 'http://www.liveonlinetv247.info/watch.php?title=Sony SIX&channel=sonysix' ] ,
 [ 'TEN 1' , 'http://www.liveonlinetv247.info/watch.php?title=TEN 1&channel=ten1' ] ,
 [ 'Sky Sports 1' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sports 1&channel=skysports1' ] ,
 [ 'Sky Sports 2' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sports 2&channel=skysports2' ] ,
 [ 'Sky Sports 3' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sports 3&channel=skysports3' ] ,
 [ 'Sky Sports 4' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sports 4&channel=skysports4' ] ,
 [ 'Sky Sports 5' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sports 5&channel=skysports5' ] ,
 [ 'Sky Sports News' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sports News&channel=skysportsnews' ] ,
 [ 'Sky Sports F1' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sports F1&channel=skysportsf1' ] ,
 [ 'Sky Sports Cricket' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sports Cricket&channel=skysportscricket' ] ,
 [ 'Sky Sports Box Office' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sports Box Office&channel=skysportsboxoffice' ] ,
 [ 'BT Sport 1' , 'http://www.liveonlinetv247.info/watch.php?title=BT Sport 1&channel=btsport1' ] ,
 [ 'BT Sport 2' , 'http://www.liveonlinetv247.info/watch.php?title=BT Sport 2&channel=btsport2' ] ,
 [ 'BT Sport Europe' , 'http://www.liveonlinetv247.info/watch.php?title=BT Sport Europe&channel=btsporteurope' ] ,
 [ 'BT Sport ESPN' , 'http://www.liveonlinetv247.info/watch.php?title=BT Sport ESPN&channel=btsportespn' ] ,
 [ 'ESPN' , 'http://www.liveonlinetv247.info/watch.php?title=ESPN&channel=espn' ] ,
 [ 'Canal+ Fútbol' , 'http://www.liveonlinetv247.info/watch.php?title=Canal%2B Fútbol&channel=canal%2Bfutbol' ] ,
 [ 'Canal+ Liga' , 'http://www.liveonlinetv247.info/watch.php?title=Canal%2B Liga&channel=canal%2Bliga' ] ,
 [ 'Canal+ Sport' , 'http://www.liveonlinetv247.info/watch.php?title=Canal%2B Sport&channel=canal%2Bsport' ] ,
 [ 'Eurosport' , 'http://www.liveonlinetv247.info/watch.php?title=Eurosport&channel=eurosport' ] ,
 [ 'Eurosport 2' , 'http://www.liveonlinetv247.info/watch.php?title=Eurosport 2&channel=eurosport2' ] ,
 [ 'WWE Network' , 'http://www.liveonlinetv247.info/watch.php?title=WWE Network&channel=wwenetwork' ] ,
 [ 'Premier Sports' , 'http://www.liveonlinetv247.info/watch.php?title=Premier Sports&channel=premiersports' ] ,
 [ 'BoxNation' , 'http://www.liveonlinetv247.info/watch.php?title=BoxNation&channel=boxnation' ] ,
 [ 'Willow TV' , 'http://www.liveonlinetv247.info/watch.php?title=Willow TV&channel=willowtv' ] ,
 [ 'Fox Sports 1' , 'http://www.liveonlinetv247.info/watch.php?title=Fox Sports 1&channel=foxsports1' ] ,
 [ 'Fox Sports 2' , 'http://www.liveonlinetv247.info/watch.php?title=Fox Sports 2&channel=foxsports2' ] ,
 [ 'NBA TV' , 'http://www.liveonlinetv247.info/watch.php?title=NBA TV&channel=nbatv' ] ,
 [ 'beIN Sports News' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports News&channel=beinsportsnews' ] ,
 [ 'beIN Sports 1' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 1&channel=beinsports1' ] ,
 [ 'beIN Sports 2' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 2&channel=beinsports2' ] ,
 [ 'beIN Sports 3' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 3&channel=beinsports3' ] ,
 [ 'beIN Sports 4' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 4&channel=beinsports4' ] ,
 [ 'beIN Sports 5' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 5&channel=beinsports5' ] ,
 [ 'beIN Sports 6' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 6&channel=beinsports6' ] ,
 [ 'beIN Sports 7' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 7&channel=beinsports7' ] ,
 [ 'beIN Sports 8' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 8&channel=beinsports8' ] ,
 [ 'beIN Sports 9' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 9&channel=beinsports9' ] ,
 [ 'beIN Sports 10' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 10&channel=beinsports10' ] ,
 [ 'beIN Sports 11 English' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 11 English&channel=beinsports11' ] ,
 [ 'beIN Sports 12 English' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 12 English&channel=beinsports12' ] ,
 [ 'beIN Sports 13 English' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 13 English&channel=beinsports13' ] ,
 [ 'beIN Sports 1 France' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 1 France&channel=beinsports1france' ] ,
 [ 'beIN Sports 2 France' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 2 France&channel=beinsports2france' ] ,
 [ 'beIN Sports 3 France' , 'http://www.liveonlinetv247.info/watch.php?title=beIN Sports 3 France&channel=beinsports3france' ] ,
 [ 'Sky Sport 1 Italia' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sport 1 Italia&channel=skysport1italia' ] ,
 [ 'Sky Sport 2 Italia' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sport 2 Italia&channel=skysport2italia' ] ,
 [ 'Sky Sport 3 Italia' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sport 3 Italia&channel=skysport3italia' ] ,
 [ 'Sky Sport 24 Italia' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sport 24 Italia&channel=skysport24italia' ] ,
 [ 'Sky Calcio' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Calcio&channel=skycalcio' ] ,
 [ 'Sky Sport MotoGP' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Sport MotoGP&channel=skysportmotogp' ] ,
 [ 'Racing UK' , 'http://www.liveonlinetv247.info/watch.php?title=Racing UK&channel=racinguk' ] ,
 [ 'At The Races' , 'http://www.liveonlinetv247.info/watch.php?title=At The Races&channel=attheraces' ] ,
 [ 'LFCTV' , 'http://www.liveonlinetv247.info/watch.php?title=LFCTV&channel=lfctv' ] ,
 [ 'MUTV' , 'http://www.liveonlinetv247.info/watch.php?title=MUTV&channel=mutv' ] ,
 [ 'Chelsea TV' , 'http://www.liveonlinetv247.info/watch.php?title=Chelsea TV&channel=chelseatv' ] ,
 [ 'Motors TV' , 'http://www.liveonlinetv247.info/watch.php?title=Motors TV&channel=motorstv' ] ,
 [ 'Golf Channel' , 'http://www.liveonlinetv247.info/watch.php?title=Golf Channel&channel=golfchannel' ] ,
 [ 'Setanta Sports' , 'http://www.liveonlinetv247.info/watch.php?title=Setanta Sports&channel=setantasports' ] ,
 [ 'TSN' , 'http://www.liveonlinetv247.info/watch.php?title=TSN&channel=tsn' ] ,
 [ 'TSN2' , 'http://www.liveonlinetv247.info/watch.php?title=TSN2&channel=tsn2' ] ,
 [ 'Sport TV 1' , 'http://www.liveonlinetv247.info/watch.php?title=Sport TV 1&channel=sporttv1' ] ,
 [ 'Sport TV 2' , 'http://www.liveonlinetv247.info/watch.php?title=Sport TV 2&channel=sporttv2' ] ,
 [ 'Sport TV 3' , 'http://www.liveonlinetv247.info/watch.php?title=Sport TV 3&channel=sporttv3' ] ,
 [ 'Sport TV 4' , 'http://www.liveonlinetv247.info/watch.php?title=Sport TV 4&channel=sporttv4' ] ,
 [ 'Sport TV 5' , 'http://www.liveonlinetv247.info/watch.php?title=Sport TV 5&channel=sporttv5' ] ,
 [ 'NFL Network' , 'http://www.liveonlinetv247.info/watch.php?title=NFL Network&channel=nflnetwork' ] ,
 [ 'PTV Sports' , 'http://www.liveonlinetv247.info/watch.php?title=PTV Sports&channel=ptvsports' ] ,
 [ 'NBCSN' , 'http://www.liveonlinetv247.info/watch.php?title=NBCSN&channel=nbcsn' ] ,
 [ 'Geo Super' , 'http://www.liveonlinetv247.info/watch.php?title=Geo Super&channel=geosuper' ] ,
 [ 'Star Sports' , 'http://www.liveonlinetv247.info/watch.php?title=Star Sports&channel=starsports' ] ,
 [ 'Star Cricket' , 'http://www.liveonlinetv247.info/watch.php?title=Star Cricket&channel=starcricket' ] ,
 [ 'Sportsnet World' , 'http://www.liveonlinetv247.info/watch.php?title=Sportsnet World&channel=sportsnetworld' ] ,
 [ 'Sportsnet ONE' , 'http://www.liveonlinetv247.info/watch.php?title=Sportsnet ONE&channel=sportsnetone' ] ,
 [ 'Sportsnet Ontario' , 'http://www.liveonlinetv247.info/watch.php?title=Sportsnet Ontario&channel=sportsnetontario' ] ,
 [ 'WWE TV' , 'http://www.liveonlinetv247.info/watch.php?title=WWE TV&channel=wwetv' ] ,
 [ 'BBC One' , 'http://www.liveonlinetv247.info/bbcone.php' ] ,
 [ 'BBC Two' , 'http://www.liveonlinetv247.info/bbctwo.php' ] ,
 [ 'ITV1' , 'http://www.liveonlinetv247.info/itv1.php' ] ,
 [ 'ITV2' , 'http://www.liveonlinetv247.info/itv2.php' ] ,
 [ 'AMC' , 'http://www.liveonlinetv247.info/amc.php' ] ,
 [ 'HBO' , 'http://www.liveonlinetv247.info/hbo.php' ] ,
 [ 'HBO HD' , 'http://www.liveonlinetv247.info/hbohd.php' ] ,
 [ 'Sky Atlantic' , 'http://www.liveonlinetv247.info/skyatlantic.php' ] ,
 [ 'FOX' , 'http://www.liveonlinetv247.info/fox.php' ] ,
 [ 'FX' , 'http://www.liveonlinetv247.info/fx.php' ] ,
 [ 'AXN' , 'http://www.liveonlinetv247.info/axn.php' ] ,
 [ 'Star Movies' , 'http://www.liveonlinetv247.info/starmovies.php' ] ,
 [ 'TLC' , 'http://www.liveonlinetv247.info/tlc.php' ] ,
 [ 'Syfy' , 'http://www.liveonlinetv247.info/syfy.php' ] ,
 [ 'TNT' , 'http://www.liveonlinetv247.info/tnt.php' ] ,
 [ 'ABC' , 'http://www.liveonlinetv247.info/abc.php' ] ,
 [ 'ABC Family' , 'http://www.liveonlinetv247.info/abcfamily.php' ] ,
 [ 'CBS' , 'http://www.liveonlinetv247.info/cbs.php' ] ,
 [ 'USA Network' , 'http://www.liveonlinetv247.info/usanetwork.php' ] ,
 [ 'CW TV' , 'http://www.liveonlinetv247.info/cwtv.php' ] ,
 [ 'Star World' , 'http://www.liveonlinetv247.info/starworld.php' ] ,
 [ 'Channel 5' , 'http://www.liveonlinetv247.info/channel5.php' ] ,
 [ 'beIN Movies 1' , 'http://www.liveonlinetv247.info/beinmovies1.php' ] ,
 [ 'beIN Movies 2' , 'http://www.liveonlinetv247.info/beinmovies2.php' ] ,
 [ 'beIN Movies 3' , 'http://www.liveonlinetv247.info/beinmovies3.php' ] ,
 [ 'Sky Movies Action' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Movies Action&channel=skymoviesaction' ] ,
 [ 'Sky Movies Comedy' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Movies Comedy&channel=skymoviescomedy' ] ,
 [ 'Sky Movies Crime' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Movies Crime&channel=skymoviescrime' ] ,
 [ 'Sky Movies Disney' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Movies Disney&channel=skymoviesdisney' ] ,
 [ 'Sky Movies Family' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Movies Family&channel=skymoviesfamily' ] ,
 [ 'Sky Movies Premiere' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Movies Premiere&channel=skymoviespremiere' ] ,
 [ 'Sky Movies Select' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Movies Select&channel=skymoviesselect' ] ,
 [ 'Sky Movies Showcase' , 'http://www.liveonlinetv247.info/watch.php?title=Sky Movies Showcase&channel=skymoviesshowcase' ] ]
if 32 - 32: i1IIi / II111iiii . Oo0Ooo
if 62 - 62: OoooooooOO * I1IiiI
oOOOoo0O0oO = [ [ 'http://mamahd.com/sky-sports-1-live-free-stream-1.html' , 'Sky Sports 1' ] ,
 [ 'http://mamahd.com/sky-sports-2-live-stream-1.html' , 'Sky Sports 2' ] ,
 [ 'http://mamahd.com/sky-sports-3-live-stream-1.html' , 'Sky Sports 3' ] ,
 [ 'http://mamahd.com/sky-sports-4-live-stream-1.html' , 'Sky Sports 4' ] ,
 [ 'http://mamahd.com/sky-sports-5-live-stream-1.html' , 'Sky Sports 5' ] ,
 [ 'http://mamahd.com/sky-sports-formula-1-live-stream-1.html' , 'Sky Sports F1' ] ,
 [ 'http://mamahd.com/bt-sport-1-live-stream1-1.html' , 'BT Sport 1' ] ,
 [ 'http://mamahd.com/bt-sport-2-live-stream-1.html' , 'BT Sport 2' ] ,
 [ 'http://mamahd.com/bt-sport-3-live-stream-1.html' , 'BT Sport 3' ] ,
 [ 'http://mamahd.com/foxsports-1-live-stream-1.html' , 'Foxsports 1' ] ,
 [ 'http://mamahd.com/foxsports-live-stream-1.html' , 'Foxsports 2' ] ,
 [ 'http://mamahd.com/box-nation-live-streaming-free-1.html' , 'Boxnation' ] ,
 [ 'http://mamahd.com/nfl-network-live-stream-free-1.html' , 'NFL Network' ] ,
 [ 'http://mamahd.com/sky-sports-hd1-germany-live-stream-1.html' , 'Sky HD1 DE' ] ,
 [ 'http://mamahd.com/sky-sports-hd2-germany-live-stream-1.html' , 'Sky HD2 DE' ] ,
 [ 'http://mamahd.com/watch-sky-bundesliga-1-live-streaming-1.html' , 'Bundesliga 1' ] ,
 [ 'http://mamahd.com/watch-bein-1-france-live-stream-1.html' , 'BeIn 1 FR' ] ,
 [ 'http://mamahd.com/watch-bein-2-france-live-stream-1.html' , 'BeIn 2 FR' ] ]
if 6 - 6: OOooOOo * o0oOOo0O0Ooo + iII111i
I1IIIiIiI1 = [ [ 'A&E' , 'http://www.shadow-net.org/channels/A%26E.html' , 'http://www.shadow-net.org/product_images/h/192/ae_tv__99609_thumb.jpg' ] ,
 [ 'ABC 2 Atlanta' , 'http://www.shadow-net.org/channels/ABC-2-Atlanta.html' , 'http://www.shadow-net.org/product_images/q/384/WSB-TV_ABC_1994__68454_thumb.PNG' ] ,
 [ 'ABC 27' , 'http://www.shadow-net.org/channels/ABC-27.html' , 'http://www.shadow-net.org/product_images/q/639/abc27__39425_thumb.jpg' ] ,
 [ 'ABC 7 New York' , 'http://www.shadow-net.org/channels/ABC-7-New-York.html' , 'http://www.shadow-net.org/product_images/b/900/wabc_abc7_new_york__26026_thumb.jpg' ] ,
 [ 'ABC Family' , 'http://www.shadow-net.org/channels/ABC-Family.html' , 'http://www.shadow-net.org/product_images/t/232/abc_family__05204_thumb.jpg' ] ,
 [ 'ABC News' , 'http://www.shadow-net.org/channels/ABC-News.html' , 'http://www.shadow-net.org/product_images/f/799/abc_news_now__18019_thumb.jpg' ] ,
 [ 'AFN Sports 2' , 'http://www.shadow-net.org/channels/AFN-Sports-2.html' , 'http://www.shadow-net.org/product_images/g/369/afn_sports2__04612_thumb.jpg' ] ,
 [ 'Al Jazeera America' , 'http://www.shadow-net.org/channels/Al-Jazeera-America.html' , 'http://www.shadow-net.org/product_images/r/030/Al_Jazeera_America_Logo__32655_thumb.png' ] ,
 [ 'AMC East' , 'http://www.shadow-net.org/channels/AMC-East.html' , 'http://www.shadow-net.org/product_images/r/604/amc__85163_thumb.jpg' ] ,
 [ 'Animal Planet US' , 'http://www.shadow-net.org/channels/Animal-Planet-US.html' , 'http://www.shadow-net.org/product_images/z/026/Animal_Planet_logo_%28black_and_green%29__59139_thumb.png' ] ,
 [ 'Bloomberg TV' , 'http://www.shadow-net.org/channels/Bloomberg-TV.html' , 'http://www.shadow-net.org/product_images/f/355/bloomberg__80284_thumb.jpg' ] ,
 [ 'Bravo' , 'http://www.shadow-net.org/channels/Bravo.html' , 'http://www.shadow-net.org/product_images/g/338/bravo_us__11790_thumb.jpg' ] ,
 [ 'Cartoon Network US' , 'http://www.shadow-net.org/channels/Cartoon-Network-US.html' , 'http://www.shadow-net.org/product_images/n/286/cartoon_network__82102_thumb.jpg' ] ,
 [ 'CBS 2 New York' , 'http://www.shadow-net.org/channels/CBS-2-New-York.html' , 'http://www.shadow-net.org/product_images/a/024/wcbs_cbs2_new_york__91850_thumb.jpg' ] ,
 [ 'CBS East' , 'http://www.shadow-net.org/channels/CBS-East.html' , 'http://www.shadow-net.org/product_images/z/021/cbs__60685_thumb.jpg' ] ,
 [ 'CBS News' , 'http://www.shadow-net.org/channels/CBS-News.html' , 'http://www.shadow-net.org/product_images/i/269/CBS_News2__07317_thumb.jpg' ] ,
 [ 'CNN International' , 'http://www.shadow-net.org/channels/CNN-International.html' , 'http://www.shadow-net.org/product_images/j/051/cnn_international__19122_thumb.jpg' ] ,
 [ 'CNN USA' , 'http://www.shadow-net.org/channels/CNN-USA.html' , 'http://www.shadow-net.org/product_images/p/470/cnn_usa__34139_thumb.jpg' ] ,
 [ 'Comedy Central' , 'http://www.shadow-net.org/channels/Comedy-Central.html' , 'http://www.shadow-net.org/product_images/o/226/comedy_central_us__62938_thumb.jpg' ] ,
 [ 'CW' , 'http://www.shadow-net.org/channels/CW.html' , 'http://www.shadow-net.org/product_images/r/672/CW_logo_color_v__09334_thumb.jpg' ] ,
 [ 'Discovery Investigation US' , 'http://www.shadow-net.org/channels/Discovery-Investigation-US.html' , 'http://www.shadow-net.org/product_images/w/036/investigation_discovery__91066_thumb.jpg' ] ,
 [ 'Discovery US' , 'http://www.shadow-net.org/channels/Discovery-US.html' , 'http://www.shadow-net.org/product_images/k/583/discovery_us__51096_thumb.jpg' ] ,
 [ 'Disney Channel US' , 'http://www.shadow-net.org/channels/Disney-Channel-US.html' , 'http://www.shadow-net.org/product_images/e/907/disney_channel__34733_thumb.jpg' ] ,
 [ 'ESPN 2' , 'http://www.shadow-net.org/channels/ESPN-2.html' , 'http://www.shadow-net.org/product_images/a/831/ESPN2_logo__59298_thumb.png' ] ,
 [ 'ESPN US' , 'http://www.shadow-net.org/channels/ESPN-US.html' , 'http://www.shadow-net.org/product_images/y/742/ESPN__66232_thumb.png' ] ,
 [ 'Fight Network' , 'http://www.shadow-net.org/channels/Fight-Network.html' , 'http://www.shadow-net.org/product_images/s/834/Fight_network_logo__56393_thumb.png' ] ,
 [ 'Food Network US' , 'http://www.shadow-net.org/channels/Food-Network-US.html' , 'http://www.shadow-net.org/product_images/z/857/food_network_uk__16280_thumb.jpg' ] ,
 [ 'FOX 13 News Tampa Bay' , 'http://www.shadow-net.org/channels/FOX-13-News-Tampa-Bay.html' , 'http://www.shadow-net.org/product_images/e/939/WTVT_Fox_13_logo__37207_thumb.png' ] ,
 [ 'FOX 2 St. Louis' , 'http://www.shadow-net.org/channels/FOX-2-St.-Louis.html' , 'http://www.shadow-net.org/product_images/v/930/KTVI_2_logo__11697_thumb.png' ] ,
 [ 'Fox 5 Washington DC' , 'http://www.shadow-net.org/channels/Fox-5-Washington-DC.html' , 'http://www.shadow-net.org/product_images/x/136/Wttg__90022_thumb.jpg' ] ,
 [ 'FOX News' , 'http://www.shadow-net.org/channels/FOX-News.html' , 'http://www.shadow-net.org/product_images/k/488/Fox_News_Channel_logo__03178_thumb.png' ] ,
 [ 'Golf Channel' , 'http://www.shadow-net.org/channels/Golf-Channel.html' , 'http://www.shadow-net.org/product_images/s/418/golf_channel_us__36323_thumb.jpg' ] ,
 [ 'H2' , 'http://www.shadow-net.org/channels/H2.html' , 'http://www.shadow-net.org/product_images/a/786/H2_TV_logo__18213_thumb.png' ] ,
 [ 'Hallmark Channel' , 'http://www.shadow-net.org/channels/Hallmark-Channel.html' , 'http://www.shadow-net.org/product_images/m/968/Hallmark-Channel-The-Heart-of-TV-Logo__99555_thumb.jpg' ] ,
 [ 'HGTV' , 'http://www.shadow-net.org/channels/HGTV.html' , 'http://www.shadow-net.org/product_images/v/595/HGTV_logo_2015__20364_thumb.png' ] ,
 [ 'History US' , 'http://www.shadow-net.org/channels/History-US.html' , 'http://www.shadow-net.org/product_images/c/576/history_europe__24065_thumb.jpg' ] ,
 [ 'HLN' , 'http://www.shadow-net.org/channels/HLN.html' , 'http://www.shadow-net.org/product_images/z/904/hln__89483_thumb.jpg' ] ,
 [ 'KRON 4 News San Francisco' , 'http://www.shadow-net.org/channels/KRON-4-News-San-Francisco.html' , 'http://www.shadow-net.org/product_images/v/424/KRON_4_Main_Logo__41805_thumb.png' ] ,
 [ 'KTLA 5' , 'http://www.shadow-net.org/channels/KTLA-5.html' , 'http://www.shadow-net.org/product_images/j/728/ktla_cw5_los_angeles__81822_thumb.jpg' ] ,
 [ 'Lifetime' , 'http://www.shadow-net.org/channels/Lifetime.html' , 'http://www.shadow-net.org/product_images/b/056/Lifetime_logo_2013__32042_thumb.png' ] ,
 [ 'MLB Network' , 'http://www.shadow-net.org/channels/MLB-Network.html' , 'http://www.shadow-net.org/product_images/o/660/mlb_network__27352_thumb.jpg' ] ,
 [ 'MSNBC' , 'http://www.shadow-net.org/channels/MSNBC.html' , 'http://www.shadow-net.org/product_images/e/114/msnbc__44837_thumb.jpg' ] ,
 [ 'MTV US' , 'http://www.shadow-net.org/channels/MTV-US.html' , 'http://www.shadow-net.org/product_images/w/104/MTV_Logo_2010__92640_thumb.png' ] ,
 [ 'NASA TV' , 'http://www.shadow-net.org/channels/NASA-TV.html' , 'http://www.shadow-net.org/product_images/m/506/nasa_tv_us__35798_thumb.jpg' ] ,
 [ 'National Geographic US' , 'http://www.shadow-net.org/channels/National-Geographic-US.html' , 'http://www.shadow-net.org/product_images/w/100/National_Geographic_Channel__77803_thumb.png' ] ,
 [ 'NBA TV' , 'http://www.shadow-net.org/channels/NBA-TV.html' , 'http://www.shadow-net.org/product_images/u/073/nba_tv__20518_thumb.jpg' ] ,
 [ 'NBC 4 New York' , 'http://www.shadow-net.org/channels/NBC-4-New-York.html' , 'http://www.shadow-net.org/product_images/c/970/wnbc_nbc4_new_york__88786_thumb.jpg' ] ,
 [ 'NBC East' , 'http://www.shadow-net.org/channels/NBC-East.html' , 'http://www.shadow-net.org/product_images/w/554/nbc__14605_thumb.gif' ] ,
 [ 'NBC Sports Netw.' , 'http://www.shadow-net.org/channels/NBC-Sports-Netw..html' , 'http://www.shadow-net.org/product_images/q/063/nbc_sports_network__66246_thumb.jpg' ] ,
 [ 'NFL Network' , 'http://www.shadow-net.org/channels/NFL-Network.html' , 'http://www.shadow-net.org/product_images/n/410/nfl_network__08611_thumb.jpg' ] ,
 [ 'NHL Network' , 'http://www.shadow-net.org/channels/NHL-Network.html' , 'http://www.shadow-net.org/product_images/v/462/NHL_Network_2011__53239_thumb.png' ] ,
 [ 'Nickelodeon US' , 'http://www.shadow-net.org/channels/Nickelodeon-US.html' , 'http://www.shadow-net.org/product_images/w/877/Nickelodeon_logo_new__07923_thumb.png' ] ,
 [ 'Pac 12 Arizona' , 'http://www.shadow-net.org/channels/Pac-12-Arizona.html' , 'http://www.shadow-net.org/product_images/f/860/Pac-12_Networks_logo__13866_thumb.png' ] ,
 [ 'Pac 12 Bay Area' , 'http://www.shadow-net.org/channels/Pac-12-Bay-Area.html' , 'http://www.shadow-net.org/product_images/c/453/Pac-12_Networks_logo__07345_thumb.png' ] ,
 [ 'Pac 12 Los Angeles' , 'http://www.shadow-net.org/channels/Pac-12-Los-Angeles.html' , 'http://www.shadow-net.org/product_images/y/660/Pac-12_Networks_logo__02467_thumb.png' ] ,
 [ 'Pac 12 Mountain' , 'http://www.shadow-net.org/channels/Pac-12-Mountain.html' , 'http://www.shadow-net.org/product_images/n/028/Pac-12_Networks_logo__03916_thumb.png' ] ,
 [ 'Pac 12 National Network' , 'http://www.shadow-net.org/channels/Pac-12-National-Network.html' , 'http://www.shadow-net.org/product_images/f/759/Pac-12_Networks_logo__13527_thumb.png' ] ,
 [ 'Pac 12 Oregon' , 'http://www.shadow-net.org/channels/Pac-12-Oregon.html' , 'http://www.shadow-net.org/product_images/d/706/Pac-12_Networks_logo__50740_thumb.png' ] ,
 [ 'Pac 12 Washington' , 'http://www.shadow-net.org/channels/Pac-12-Washington.html' , 'http://www.shadow-net.org/product_images/d/574/Pac-12_Networks_logo__54056_thumb.png' ] ,
 [ 'PBS Wisconsin' , 'http://www.shadow-net.org/channels/PBS-Wisconsin.html' , 'http://www.shadow-net.org/product_images/p/766/pbs_east__81153_thumb.jpg' ] ,
 [ 'RT America' , 'http://www.shadow-net.org/channels/RT-America.html' , 'http://www.shadow-net.org/product_images/l/726/Russia-today-logo__86701_thumb.png' ] ,
 [ 'Spike' , 'http://www.shadow-net.org/channels/Spike.html' , 'http://www.shadow-net.org/product_images/z/232/Spike_logo_2015__98357_thumb.png' ] ,
 [ 'Sportsnet 360' , 'http://www.shadow-net.org/channels/Sportsnet-360.html' , 'http://www.shadow-net.org/product_images/a/095/Sportsnet-360-Logo__31086_thumb.jpg' ] ,
 [ 'Sportsnet One' , 'http://www.shadow-net.org/channels/Sportsnet-One.html' , 'http://www.shadow-net.org/product_images/x/985/Sportsnetone2011__31537_thumb.png' ] ,
 [ 'Sportsnet World' , 'http://www.shadow-net.org/channels/Sportsnet-World.html' , 'http://www.shadow-net.org/product_images/e/626/SportsnetWorld__37094_thumb.png' ] ,
 [ 'Starz' , 'http://www.shadow-net.org/channels/Starz.html' , 'http://www.shadow-net.org/product_images/f/200/Starz_2008__56778_thumb.png' ] ,
 [ 'Syfy' , 'http://www.shadow-net.org/channels/Syfy.html' , 'http://www.shadow-net.org/product_images/f/954/syfy__52943_thumb.jpg' ] ,
 [ 'TBS' , 'http://www.shadow-net.org/channels/TBS.html' , 'http://www.shadow-net.org/product_images/f/523/TBS.svg__23453_thumb.png' ] ,
 [ 'TLC' , 'http://www.shadow-net.org/channels/TLC.html' , 'http://www.shadow-net.org/product_images/g/894/TLC_USA_logo__18952_thumb.png' ] ,
 [ 'TNT' , 'http://www.shadow-net.org/channels/TNT.html' , 'http://www.shadow-net.org/product_images/e/600/tnt__28275_thumb.jpg' ] ,
 [ 'Travel Channel US' , 'http://www.shadow-net.org/channels/Travel-Channel-US.html' , 'http://www.shadow-net.org/product_images/f/359/Travel_Channel_HD_2013__46217_thumb.png' ] ,
 [ 'TruTV' , 'http://www.shadow-net.org/channels/TruTV.html' , 'http://www.shadow-net.org/product_images/l/545/TruTV_logo_2014__51891_thumb.png' ] ,
 [ 'TSN 1' , 'http://www.shadow-net.org/channels/TSN-1.html' , 'http://www.shadow-net.org/product_images/u/487/tsn__98863_thumb.jpg' ] ,
 [ 'TSN 2' , 'http://www.shadow-net.org/channels/TSN-2.html' , 'http://www.shadow-net.org/product_images/b/342/tsn2__61112_thumb.jpg' ] ,
 [ 'TSN 3' , 'http://www.shadow-net.org/channels/TSN-3.html' , 'http://www.shadow-net.org/product_images/f/245/tsn3__97431_thumb.png' ] ,
 [ 'TSN 4' , 'http://www.shadow-net.org/channels/TSN-4.html' , 'http://www.shadow-net.org/product_images/y/045/tsn4__75023_thumb.png' ] ,
 [ 'USA Network' , 'http://www.shadow-net.org/channels/USA-Network.html' , 'http://www.shadow-net.org/product_images/a/517/usa_network__57030_thumb.jpg' ] ,
 [ 'VH1' , 'http://www.shadow-net.org/channels/VH1.html' , 'http://www.shadow-net.org/product_images/l/556/VH1_logonew__62136_thumb.png' ] ,
 [ 'WeatherNation' , 'http://www.shadow-net.org/channels/WeatherNation.html' , 'http://www.shadow-net.org/product_images/h/491/WeatherNation_logo__53910_thumb.png' ] ,
 [ 'WJHL Tennessee' , 'http://www.shadow-net.org/channels/WJHL-Tennessee.html' , 'http://www.shadow-net.org/product_images/l/084/WJHL-TV_2012_logo__63534_thumb.png' ] ,
 [ 'WTHI Terre Haute' , 'http://www.shadow-net.org/channels/WTHI-Terre-Haute.html' , 'http://www.shadow-net.org/product_images/j/981/WTHI_2012_Logo__76059_thumb.png' ] ,
 [ 'WWE Network' , 'http://www.shadow-net.org/channels/WWE-Network.html' , 'http://www.shadow-net.org/product_images/h/880/world_wrestling_entertainment__70123_thumb.jpg' ] ,
 [ '5Star' , 'http://www.shadow-net.org/channels/5Star.html' , 'http://www.shadow-net.org/product_images/i/018/channel_5_uk_star__59646_thumb.png' ] ,
 [ '5USA' , 'http://www.shadow-net.org/channels/5USA.html' , 'http://www.shadow-net.org/product_images/s/311/channel5_usa__70905_thumb.jpg' ] ,
 [ 'Animal Planet UK' , 'http://www.shadow-net.org/channels/Animal-Planet-UK.html' , 'http://www.shadow-net.org/product_images/w/160/Animal_Planet_logo_%28black_and_green%29__98995_thumb.png' ] ,
 [ 'At The Races' , 'http://www.shadow-net.org/channels/At-The-Races.html' , 'http://www.shadow-net.org/product_images/s/772/at_the_races_uk__25721_thumb.jpg' ] ,
 [ 'BBC 1' , 'http://www.shadow-net.org/channels/BBC-1.html' , 'http://www.shadow-net.org/product_images/r/418/BBC_One_2002__20962_thumb.png' ] ,
 [ 'BBC 2' , 'http://www.shadow-net.org/channels/BBC-2.html' , 'http://www.shadow-net.org/product_images/x/270/BBC_Two.svg_%281%29__18552_thumb.png' ] ,
 [ 'BBC 3' , 'http://www.shadow-net.org/channels/BBC-3.html' , 'http://www.shadow-net.org/product_images/z/431/bbc3__58300_thumb.jpg' ] ,
 [ 'BBC 4' , 'http://www.shadow-net.org/channels/BBC-4.html' , 'http://www.shadow-net.org/product_images/u/402/bbc4__60255_thumb.jpg' ] ,
 [ 'BBC News' , 'http://www.shadow-net.org/channels/BBC-News.html' , 'http://www.shadow-net.org/product_images/u/125/bbc_news__39343_thumb.jpg' ] ,
 [ 'BBC Wold News' , 'http://www.shadow-net.org/channels/BBC-Wold-News.html' , 'http://www.shadow-net.org/product_images/p/302/bbc_world__60450_thumb.jpg' ] ,
 [ 'BoxNation' , 'http://www.shadow-net.org/channels/BoxNation.html' , 'http://www.shadow-net.org/product_images/h/426/box_nation__84194_thumb.jpg' ] ,
 [ 'British Eurosport 1' , 'http://www.shadow-net.org/channels/British-Eurosport-1.html' , 'http://www.shadow-net.org/product_images/g/814/british_eurosport__44049_thumb.jpg' ] ,
 [ 'British Eurosport 2' , 'http://www.shadow-net.org/channels/British-Eurosport-2.html' , 'http://www.shadow-net.org/product_images/f/591/british_eurosport2__58698_thumb.jpg' ] ,
 [ 'BT Sport 1' , 'http://www.shadow-net.org/channels/BT-Sport-1.html' , 'http://www.shadow-net.org/product_images/z/622/bt_sport_1__18746_thumb.jpg' ] ,
 [ 'BT Sport 2' , 'http://www.shadow-net.org/channels/BT-Sport-2.html' , 'http://www.shadow-net.org/product_images/y/951/bt_sport_2__63983_thumb.jpg' ] ,
 [ 'BT Sport ESPN' , 'http://www.shadow-net.org/channels/BT-Sport-ESPN.html' , 'http://www.shadow-net.org/product_images/t/735/BT_Sport_ESPN_logo__79357_thumb.png' ] ,
 [ 'BT Sport Europe' , 'http://www.shadow-net.org/channels/BT-Sport-Europe.html' , 'http://www.shadow-net.org/product_images/b/335/bt_sport_europe_uk__81016_thumb.jpg' ] ,
 [ 'Capital' , 'http://www.shadow-net.org/channels/Capital.html' , 'http://www.shadow-net.org/product_images/r/954/Capital_TV_logo__27138_thumb.png' ] ,
 [ 'Cartoon Network UK' , 'http://www.shadow-net.org/channels/Cartoon-Network-UK.html' , 'http://www.shadow-net.org/product_images/x/048/cartoon_network__02584_thumb.jpg' ] ,
 [ 'CBS Action' , 'http://www.shadow-net.org/channels/CBS-Action.html' , 'http://www.shadow-net.org/product_images/k/353/cbs_action_uk__54811_thumb.png' ] ,
 [ 'CBS Drama' , 'http://www.shadow-net.org/channels/CBS-Drama.html' , 'http://www.shadow-net.org/product_images/u/097/cbs_drama_eu__13760_thumb.png' ] ,
 [ 'CBS Reality' , 'http://www.shadow-net.org/channels/CBS-Reality.html' , 'http://www.shadow-net.org/product_images/u/279/cbs_reality__44213_thumb.jpg' ] ,
 [ 'CBS Reality +1' , 'http://www.shadow-net.org/channels/CBS-Reality-%252b1.html' , 'http://www.shadow-net.org/product_images/n/056/cbs_reality_plus1__81996_thumb.png' ] ,
 [ 'Channel 4' , 'http://www.shadow-net.org/channels/Channel-4.html' , 'http://www.shadow-net.org/product_images/s/715/channel4__56690_thumb.jpg' ] ,
 [ 'Channel 5' , 'http://www.shadow-net.org/channels/Channel-5.html' , 'http://www.shadow-net.org/product_images/m/671/channel5_uk__99265_thumb.jpg' ] ,
 [ 'Chelsea TV' , 'http://www.shadow-net.org/channels/Chelsea-TV.html' , 'http://www.shadow-net.org/product_images/s/436/chelsea_tv__40010_thumb.jpg' ] ,
 [ 'Comedy Central UK' , 'http://www.shadow-net.org/channels/Comedy-Central-UK.html' , 'http://www.shadow-net.org/product_images/u/379/comedy_central_us__55592__60778_thumb.jpg' ] ,
 [ 'Dave' , 'http://www.shadow-net.org/channels/Dave.html' , 'http://www.shadow-net.org/product_images/q/672/dave__30048_thumb.jpg' ] ,
 [ 'Discovery History' , 'http://www.shadow-net.org/channels/Discovery-History.html' , 'http://www.shadow-net.org/product_images/q/707/Discovery_History_2010__01621_thumb.png' ] ,
 [ 'Discovery Investigation UK' , 'http://www.shadow-net.org/channels/Discovery-Investigation-UK.html' , 'http://www.shadow-net.org/product_images/x/369/investigation_discovery__87602_thumb.jpg' ] ,
 [ 'Discovery Science UK' , 'http://www.shadow-net.org/channels/Discovery-Science-UK.html' , 'http://www.shadow-net.org/product_images/t/726/Discovery_Science_h__96606_thumb.png' ] ,
 [ 'Discovery UK' , 'http://www.shadow-net.org/channels/Discovery-UK.html' , 'http://www.shadow-net.org/product_images/j/140/discovery_us__02242_thumb.jpg' ] ,
 [ 'Disney Channel UK' , 'http://www.shadow-net.org/channels/Disney-Channel-UK.html' , 'http://www.shadow-net.org/product_images/g/535/disney_channel__10345_thumb.jpg' ] ,
 [ 'E! Entertainment' , 'http://www.shadow-net.org/channels/E%21-Entertainment.html' , 'http://www.shadow-net.org/product_images/r/548/E%21_Logo_2012__59361_thumb.png' ] ,
 [ 'E4' , 'http://www.shadow-net.org/channels/E4.html' , 'http://www.shadow-net.org/product_images/x/573/e4_uk__72574_thumb.jpg' ] ,
 [ 'Euronews' , 'http://www.shadow-net.org/channels/Euronews.html' , 'http://www.shadow-net.org/product_images/l/724/euronews__73752_thumb.jpg' ] ,
 [ 'Film 4' , 'http://www.shadow-net.org/channels/Film-4.html' , 'http://www.shadow-net.org/product_images/v/827/film4__52400_thumb.jpg' ] ,
 [ 'Food Network +1' , 'http://www.shadow-net.org/channels/Food-Network-%252b1.html' , 'http://www.shadow-net.org/product_images/m/359/food_network_uk__23707_thumb.jpg' ] ,
 [ 'Food Network UK' , 'http://www.shadow-net.org/channels/Food-Network-UK.html' , 'http://www.shadow-net.org/product_images/q/298/food_network_uk__02476_thumb.jpg' ] ,
 [ 'Gold' , 'http://www.shadow-net.org/channels/Gold.html' , 'http://www.shadow-net.org/product_images/c/241/gold_black_background__91302_thumb.jpg' ] ,
 [ 'Heart TV' , 'http://www.shadow-net.org/channels/Heart-TV.html' , 'http://www.shadow-net.org/product_images/z/606/Heart_TV_logo__58712_thumb.png' ] ,
 [ 'History UK' , 'http://www.shadow-net.org/channels/History-UK.html' , 'http://www.shadow-net.org/product_images/z/917/history_europe__17235_thumb.jpg' ] ,
 [ 'ITV 1' , 'http://www.shadow-net.org/channels/ITV-1.html' , 'http://www.shadow-net.org/product_images/p/615/itv_uk__27094_thumb.jpg' ] ,
 [ 'ITV 1+1' , 'http://www.shadow-net.org/channels/ITV-1%252b1.html' , 'http://www.shadow-net.org/product_images/y/695/itv1_plus1__81714_thumb.jpg' ] ,
 [ 'ITV 2' , 'http://www.shadow-net.org/channels/ITV-2.html' , 'http://www.shadow-net.org/product_images/x/104/itv2__44555_thumb.jpg' ] ,
 [ 'ITV 2+1' , 'http://www.shadow-net.org/channels/ITV-2%252b1.html' , 'http://www.shadow-net.org/product_images/p/722/itv2_plus1__56577_thumb.jpg' ] ,
 [ 'ITV 3' , 'http://www.shadow-net.org/channels/ITV-3.html' , 'http://www.shadow-net.org/product_images/k/294/itv3__61186_thumb.jpg' ] ,
 [ 'ITV 3+1' , 'http://www.shadow-net.org/channels/ITV-3%252b1.html' , 'http://www.shadow-net.org/product_images/z/673/itv3_plus1__43817_thumb.jpg' ] ,
 [ 'ITV 4' , 'http://www.shadow-net.org/channels/ITV-4.html' , 'http://www.shadow-net.org/product_images/r/387/itv4__95441_thumb.jpg' ] ,
 [ 'ITV 4+1' , 'http://www.shadow-net.org/channels/ITV-4%252b1.html' , 'http://www.shadow-net.org/product_images/i/517/itv4_plus1__96475_thumb.jpg' ] ,
 [ 'ITV Be' , 'http://www.shadow-net.org/channels/ITV-Be.html' , 'http://www.shadow-net.org/product_images/x/968/ITVBe_logo_2014-__58951_thumb.png' ] ,
 [ 'London Live' , 'http://www.shadow-net.org/channels/London-Live.html' , 'http://www.shadow-net.org/product_images/v/648/london_live__38073_thumb.png' ] ,
 [ 'Manchester United TV' , 'http://www.shadow-net.org/channels/Manchester-United-TV.html' , 'http://www.shadow-net.org/product_images/i/675/mutv__18782_thumb.jpg' ] ,
 [ 'More 4' , 'http://www.shadow-net.org/channels/More-4.html' , 'http://www.shadow-net.org/product_images/w/935/more4__90180_thumb.jpg' ] ,
 [ 'Motors TV' , 'http://www.shadow-net.org/channels/Motors-TV.html' , 'http://www.shadow-net.org/product_images/s/922/MotorsTV-logo__73046_thumb.png' ] ,
 [ 'MTV Classic UK' , 'http://www.shadow-net.org/channels/MTV-Classic-UK.html' , 'http://www.shadow-net.org/product_images/z/697/MTV_Classic_logo_2013__65812_thumb.png' ] ,
 [ 'MTV Dance' , 'http://www.shadow-net.org/channels/MTV-Dance.html' , 'http://www.shadow-net.org/product_images/x/506/MTV_Dance_2013__40554_thumb.png' ] ,
 [ 'MTV Hits' , 'http://www.shadow-net.org/channels/MTV-Hits.html' , 'http://www.shadow-net.org/product_images/b/347/MTV_Hits_Logo_2012__61325_thumb.png' ] ,
 [ 'MTV Rocks' , 'http://www.shadow-net.org/channels/MTV-Rocks.html' , 'http://www.shadow-net.org/product_images/w/993/MTV_Rocks_logo_2013__21136_thumb.png' ] ,
 [ 'Nat Geo Wild UK' , 'http://www.shadow-net.org/channels/Nat-Geo-Wild-UK.html' , 'http://www.shadow-net.org/product_images/s/246/nat_geo_wild__16696_thumb.jpg' ] ,
 [ 'National Geographic UK' , 'http://www.shadow-net.org/channels/National-Geographic-UK.html' , 'http://www.shadow-net.org/product_images/h/958/National_Geographic_Channel__15826_thumb.png' ] ,
 [ 'Premier Sports' , 'http://www.shadow-net.org/channels/Premier-Sports.html' , 'http://www.shadow-net.org/product_images/i/771/Premier_Sports_logo__59689_thumb.png' ] ,
 [ 'Quest' , 'http://www.shadow-net.org/channels/Quest.html' , 'http://www.shadow-net.org/product_images/e/017/quest__28625_thumb.jpg' ] ,
 [ 'Racing UK' , 'http://www.shadow-net.org/channels/Racing-UK.html' , 'http://www.shadow-net.org/product_images/h/544/racing_uk__87840_thumb.jpg' ] ,
 [ 'Really' , 'http://www.shadow-net.org/channels/Really.html' , 'http://www.shadow-net.org/product_images/c/248/Really_logo_2013__65352_thumb.png' ] ,
 [ 'RTE One' , 'http://www.shadow-net.org/channels/RTE-One.html' , 'http://www.shadow-net.org/product_images/m/283/rte_one__12324_thumb.jpg' ] ,
 [ 'RTE Two' , 'http://www.shadow-net.org/channels/RTE-Two.html' , 'http://www.shadow-net.org/product_images/c/249/rte_two__61649_thumb.jpg' ] ,
 [ 'Setanta Ireland' , 'http://www.shadow-net.org/channels/Setanta-Ireland.html' , 'http://www.shadow-net.org/product_images/t/788/setanta_sports_ie__75006_thumb.jpg' ] ,
 [ 'Sky 1' , 'http://www.shadow-net.org/channels/Sky-1.html' , 'http://www.shadow-net.org/product_images/a/865/sky_uk_1__64403_thumb.jpg' ] ,
 [ 'Sky 2' , 'http://www.shadow-net.org/channels/Sky-2.html' , 'http://www.shadow-net.org/product_images/n/296/sky_uk_2__94151_thumb.jpg' ] ,
 [ 'Sky Atlantic' , 'http://www.shadow-net.org/channels/Sky-Atlantic.html' , 'http://www.shadow-net.org/product_images/t/541/sky_uk_atlantic__46552_thumb.jpg' ] ,
 [ 'Sky News' , 'http://www.shadow-net.org/channels/Sky-News.html' , 'http://www.shadow-net.org/product_images/j/542/sky_news__04995_thumb.jpg' ] ,
 [ 'Sky Sports 5' , 'http://www.shadow-net.org/channels/Sky-Sports-5.html' , 'http://www.shadow-net.org/product_images/k/949/sky_uk_sports5__60555_thumb.png' ] ,
 [ 'Sky Sports F1' , 'http://www.shadow-net.org/channels/Sky-Sports-F1.html' , 'http://www.shadow-net.org/product_images/m/296/sky_uk_sports_f1__96235_thumb.jpg' ] ,
 [ 'Sky Sports News' , 'http://www.shadow-net.org/channels/Sky-Sports-News.html' , 'http://www.shadow-net.org/product_images/j/929/sky_uk_sports_news_hq__53705_thumb.jpg' ] ,
 [ 'Sky Sports1' , 'http://www.shadow-net.org/channels/Sky-Sports1.html' , 'http://www.shadow-net.org/product_images/g/437/sky_sports1__15526_thumb.jpg' ] ,
 [ 'TG4 Ireland' , 'http://www.shadow-net.org/channels/TG4-Ireland.html' , 'http://www.shadow-net.org/product_images/i/427/TG4_logo__50346_thumb.png' ] ,
 [ 'The Vault' , 'http://www.shadow-net.org/channels/The-Vault.html' , 'http://www.shadow-net.org/product_images/x/145/The_Vault_TV_channel_logo_2014__13912_thumb.png' ] ,
 [ 'Travel Channel +1' , 'http://www.shadow-net.org/channels/Travel-Channel-%252b1.html' , 'http://www.shadow-net.org/product_images/w/588/Travel_Channel_HD_2013__76743_thumb.png' ] ,
 [ 'TruTV UK' , 'http://www.shadow-net.org/channels/TruTV-UK.html' , 'http://www.shadow-net.org/product_images/s/962/TruTV_logo_2014__66876_thumb.png' ] ,
 [ 'Yesterday' , 'http://www.shadow-net.org/channels/Yesterday.html' , 'http://www.shadow-net.org/product_images/m/948/Yesterday_logo_2012__75992_thumb.png' ] ,
 [ '1 Music Channel' , 'http://www.shadow-net.org/channels/1-Music-Channel.html' , 'http://www.shadow-net.org/product_images/j/674/1music_channel__45014_thumb.jpg' ] ,
 [ '2 Plus Moldova' , 'http://www.shadow-net.org/channels/2-Plus-Moldova.html' , 'http://www.shadow-net.org/product_images/f/797/2plus__71764_thumb.jpg' ] ,
 [ 'Acasa TV' , 'http://www.shadow-net.org/channels/Acasa-TV.html' , 'http://www.shadow-net.org/product_images/y/598/acasatv__35745_thumb.jpg' ] ,
 [ 'Acasa TV Gold' , 'http://www.shadow-net.org/channels/Acasa-TV-Gold.html' , 'http://www.shadow-net.org/product_images/t/614/acasatv_gold__73715_thumb.jpg' ] ,
 [ 'Antena 3' , 'http://www.shadow-net.org/channels/Antena-3.html' , 'http://www.shadow-net.org/product_images/x/167/antena_3__63718_thumb.jpg' ] ,
 [ 'Antena Stars' , 'http://www.shadow-net.org/channels/Antena-Stars.html' , 'http://www.shadow-net.org/product_images/d/566/antena_stars_ro__84231_thumb.png' ] ,
 [ 'AXN Black' , 'http://www.shadow-net.org/channels/AXN-Black.html' , 'http://www.shadow-net.org/product_images/v/621/axn_black__67969_thumb.jpg' ] ,
 [ 'AXN Romania' , 'http://www.shadow-net.org/channels/AXN-Romania.html' , 'http://www.shadow-net.org/product_images/w/585/axn__49217_thumb.jpg' ] ,
 [ 'AXN Spin' , 'http://www.shadow-net.org/channels/AXN-Spin.html' , 'http://www.shadow-net.org/product_images/p/623/axn_spin__27350_thumb.jpg' ] ,
 [ 'AXN White' , 'http://www.shadow-net.org/channels/AXN-White.html' , 'http://www.shadow-net.org/product_images/t/218/axn_white__53602_thumb.jpg' ] ,
 [ 'B1 TV' , 'http://www.shadow-net.org/channels/B1-TV.html' , 'http://www.shadow-net.org/product_images/o/122/b__04086_thumb.JPG' ] ,
 [ 'Boomerang RO' , 'http://www.shadow-net.org/channels/Boomerang-RO.html' , 'http://www.shadow-net.org/product_images/o/308/Boomerang_2014_logo__68388_thumb.png' ] ,
 [ 'Busuioc TV' , 'http://www.shadow-net.org/channels/Busuioc-TV.html' , 'http://www.shadow-net.org/product_images/y/696/busuioc-tv1__38947_thumb.png' ] ,
 [ 'Cartoon Network RO' , 'http://www.shadow-net.org/channels/Cartoon-Network-RO.html' , 'http://www.shadow-net.org/product_images/l/311/cartoon_network__89253_thumb.jpg' ] ,
 [ 'Discovery Channel RO' , 'http://www.shadow-net.org/channels/Discovery-Channel-RO.html' , 'http://www.shadow-net.org/product_images/t/481/discovery_us__36360_thumb.jpg' ] ,
 [ 'Discovery Investigation RO' , 'http://www.shadow-net.org/channels/Discovery-Investigation-RO.html' , 'http://www.shadow-net.org/product_images/c/338/investigation_discovery__43034_thumb.jpg' ] ,
 [ 'Discovery Science RO' , 'http://www.shadow-net.org/channels/Discovery-Science-RO.html' , 'http://www.shadow-net.org/product_images/v/176/discovery_science__39598_thumb.jpg' ] ,
 [ 'Discovery World RO' , 'http://www.shadow-net.org/channels/Discovery-World-RO.html' , 'http://www.shadow-net.org/product_images/a/473/discovery_world__84339_thumb.jpg' ] ,
 [ 'Disney Channel RO' , 'http://www.shadow-net.org/channels/Disney-Channel-RO.html' , 'http://www.shadow-net.org/product_images/d/186/disney_channel__22318_thumb.jpg' ] ,
 [ 'Disney Junior RO' , 'http://www.shadow-net.org/channels/Disney-Junior-RO.html' , 'http://www.shadow-net.org/product_images/x/975/disney_junior__56938_thumb.jpg' ] ,
 [ 'DIVA Universal' , 'http://www.shadow-net.org/channels/DIVA-Universal.html' , 'http://www.shadow-net.org/product_images/b/137/diva_universal__81331_thumb.jpg' ] ,
 [ 'Euforia TV' , 'http://www.shadow-net.org/channels/Euforia-TV.html' , 'http://www.shadow-net.org/product_images/b/079/euforia__17340_thumb.jpg' ] ,
 [ 'Europa Plus TV' , 'http://www.shadow-net.org/channels/Europa-Plus-TV.html' , 'http://www.shadow-net.org/product_images/t/445/europa_plus_tv__13286_thumb.jpg' ] ,
 [ 'Film Cafe' , 'http://www.shadow-net.org/channels/Film-Cafe.html' , 'http://www.shadow-net.org/product_images/k/094/film_cafe__88821_thumb.jpg' ] ,
 [ 'History Channel RO' , 'http://www.shadow-net.org/channels/History-Channel-RO.html' , 'http://www.shadow-net.org/product_images/c/633/history_europe__92303_thumb.jpg' ] ,
 [ 'Kanal D' , 'http://www.shadow-net.org/channels/Kanal-D.html' , 'http://www.shadow-net.org/product_images/k/016/kanald__51428_thumb.jpg' ] ,
 [ 'Kanal D SOP' , 'http://www.shadow-net.org/channels/Kanal-D-SOP.html' , 'http://www.shadow-net.org/product_images/w/449/kanald__77882_thumb.jpg' ] ,
 [ 'Look TV' , 'http://www.shadow-net.org/channels/Look-TV.html' , 'http://www.shadow-net.org/product_images/w/748/look_tv_ro__91074_thumb.jpg' ] ,
 [ 'MBC Moldova' , 'http://www.shadow-net.org/channels/MBC-Moldova.html' , 'http://www.shadow-net.org/product_images/e/655/mbc_md__92415_thumb.jpg' ] ,
 [ 'Minimax RO' , 'http://www.shadow-net.org/channels/Minimax-RO.html' , 'http://www.shadow-net.org/product_images/a/080/minimax__47002_thumb.jpg' ] ,
 [ 'Moldova 1' , 'http://www.shadow-net.org/channels/Moldova-1.html' , 'http://www.shadow-net.org/product_images/x/931/moldova1__66582_thumb.jpg' ] ,
 [ 'Nat Geo Wild RO' , 'http://www.shadow-net.org/channels/Nat-Geo-Wild-RO.html' , 'http://www.shadow-net.org/product_images/a/060/nat_geo_wild__45489_thumb.jpg' ] ,
 [ 'National Geographic RO' , 'http://www.shadow-net.org/channels/National-Geographic-RO.html' , 'http://www.shadow-net.org/product_images/q/711/nat_geo_channel__71158_thumb.jpg' ] ,
 [ 'National TV' , 'http://www.shadow-net.org/channels/National-TV.html' , 'http://www.shadow-net.org/product_images/a/855/ntv_ro__82947_thumb.jpg' ] ,
 [ 'Nick Jr. RO' , 'http://www.shadow-net.org/channels/Nick-Jr.-RO.html' , 'http://www.shadow-net.org/product_images/l/551/nick_jr__68462_thumb.jpg' ] ,
 [ 'Nickelodeon RO' , 'http://www.shadow-net.org/channels/Nickelodeon-RO.html' , 'http://www.shadow-net.org/product_images/k/445/nickelodeon_us__87438_thumb.jpg' ] ,
 [ 'Noroc TV' , 'http://www.shadow-net.org/channels/Noroc-TV.html' , 'http://www.shadow-net.org/product_images/g/451/noroc_tv__33489_thumb.jpg' ] ,
 [ 'Paramount Channel' , 'http://www.shadow-net.org/channels/Paramount-Channel.html' , 'http://www.shadow-net.org/product_images/o/159/paramount_channel__04267_thumb.jpg' ] ,
 [ 'Prima TV' , 'http://www.shadow-net.org/channels/Prima-TV.html' , 'http://www.shadow-net.org/product_images/a/793/prima_tv__85329_thumb.jpg' ] ,
 [ 'Pro Cinema' , 'http://www.shadow-net.org/channels/Pro-Cinema.html' , 'http://www.shadow-net.org/product_images/c/484/pro_cinema__85098_thumb.jpg' ] ,
 [ 'PRO TV Chisinau' , 'http://www.shadow-net.org/channels/PRO-TV-Chisinau.html' , 'http://www.shadow-net.org/product_images/l/060/pro_tv_chisinau__82297_thumb.jpg' ] ,
 [ 'ProTV' , 'http://www.shadow-net.org/channels/ProTV.html' , 'http://www.shadow-net.org/product_images/a/051/pro_tv_hd__02175_thumb.jpg' ] ,
 [ 'Publika Moldova' , 'http://www.shadow-net.org/channels/Publika-Moldova.html' , 'http://www.shadow-net.org/product_images/o/560/publika_md__63811_thumb.jpg' ] ,
 [ 'PV TV' , 'http://www.shadow-net.org/channels/PV-TV.html' , 'http://www.shadow-net.org/product_images/r/202/pv_tv__21819_thumb.jpg' ] ,
 [ 'Realitatea TV' , 'http://www.shadow-net.org/channels/Realitatea-TV.html' , 'http://www.shadow-net.org/product_images/t/836/realitatea_tv__98067_thumb.jpg' ] ,
 [ 'Realitatea TV Sop' , 'http://www.shadow-net.org/channels/Realitatea-TV-Sop.html' , 'http://www.shadow-net.org/product_images/y/807/realitatea_tv__90437_thumb.jpg' ] ,
 [ 'REN TV' , 'http://www.shadow-net.org/channels/REN-TV.html' , 'http://www.shadow-net.org/product_images/r/761/ren_tv__86337_thumb.jpg' ] ,
 [ 'Romania TV Sop' , 'http://www.shadow-net.org/channels/Romania-TV-Sop.html' , 'http://www.shadow-net.org/product_images/u/201/rtv__77670_thumb.jpg' ] ,
 [ 'Romania TV VLC' , 'http://www.shadow-net.org/channels/Romania-TV-VLC.html' , 'http://www.shadow-net.org/product_images/s/251/rtv__06919_thumb.jpg' ] ,
 [ 'Taraf TV' , 'http://www.shadow-net.org/channels/Taraf-TV.html' , 'http://www.shadow-net.org/product_images/k/042/taraftv__74457_thumb.jpg' ] ,
 [ 'TV 1000' , 'http://www.shadow-net.org/channels/TV-1000.html' , 'http://www.shadow-net.org/product_images/y/342/tv1000__26849_thumb.jpg' ] ,
 [ 'TV7 Moldova' , 'http://www.shadow-net.org/channels/TV7-Moldova.html' , 'http://www.shadow-net.org/product_images/k/609/tv7_md__03464_thumb.jpg' ] ,
 [ 'TVC 21' , 'http://www.shadow-net.org/channels/TVC-21.html' , 'http://www.shadow-net.org/product_images/f/539/tvc_21_md__08116_thumb.jpg' ] ,
 [ 'TVR1' , 'http://www.shadow-net.org/channels/TVR1.html' , 'http://www.shadow-net.org/product_images/y/593/tvr1__58209_thumb.jpg' ] ,
 [ 'TVR2' , 'http://www.shadow-net.org/channels/TVR2.html' , 'http://www.shadow-net.org/product_images/o/307/tvr2__87976_thumb.jpg' ] ,
 [ 'UTV' , 'http://www.shadow-net.org/channels/UTV.html' , 'http://www.shadow-net.org/product_images/c/088/u_tv__51904_thumb.jpg' ] ,
 [ 'Viasat Explore' , 'http://www.shadow-net.org/channels/Viasat-Explore.html' , 'http://www.shadow-net.org/product_images/f/967/viasat_explore__28460_thumb.jpg' ] ,
 [ 'Viasat History' , 'http://www.shadow-net.org/channels/Viasat-History.html' , 'http://www.shadow-net.org/product_images/j/357/viasat_history__39867_thumb.jpg' ] ,
 [ 'Viasat Nature' , 'http://www.shadow-net.org/channels/Viasat-Nature.html' , 'http://www.shadow-net.org/product_images/n/686/viasat_nature_east__80761_thumb.jpg' ] ,
 [ 'Das Erste' , 'http://www.shadow-net.org/channels/Das-Erste.html' , 'http://www.shadow-net.org/product_images/w/786/ard__19793_thumb.jpg' ] ,
 [ 'Deutsche Welle' , 'http://www.shadow-net.org/channels/Deutsche-Welle.html' , 'http://www.shadow-net.org/product_images/a/044/dw_tv__63402_thumb.jpg' ] ,
 [ 'Disney Channel DE' , 'http://www.shadow-net.org/channels/Disney-Channel-DE.html' , 'http://www.shadow-net.org/product_images/y/352/disney_channel__26154_thumb.jpg' ] ,
 [ 'Kabel Eins' , 'http://www.shadow-net.org/channels/Kabel-Eins.html' , 'http://www.shadow-net.org/product_images/t/152/kabel1__63893_thumb.jpg' ] ,
 [ 'KiKa' , 'http://www.shadow-net.org/channels/KiKa.html' , 'http://www.shadow-net.org/product_images/g/009/kinderkanal__49484_thumb.jpg' ] ,
 [ 'N-TV' , 'http://www.shadow-net.org/channels/N%252dTV.html' , 'http://www.shadow-net.org/product_images/l/779/ntv_de__93235_thumb.jpg' ] ,
 [ 'One' , 'http://www.shadow-net.org/channels/One.html' , 'http://www.shadow-net.org/product_images/b/702/One_TV_Logo__93960_thumb.png' ] ,
 [ 'ORF 1' , 'http://www.shadow-net.org/channels/ORF-1.html' , 'http://www.shadow-net.org/product_images/q/474/orf1__10981_thumb.jpg' ] ,
 [ 'ORF 2' , 'http://www.shadow-net.org/channels/ORF-2.html' , 'http://www.shadow-net.org/product_images/i/440/orf2__54577_thumb.jpg' ] ,
 [ 'ORF 3' , 'http://www.shadow-net.org/channels/ORF-3.html' , 'http://www.shadow-net.org/product_images/o/172/orf3__13173_thumb.jpg' ] ,
 [ 'ORF Sport Plus' , 'http://www.shadow-net.org/channels/ORF-Sport-Plus.html' , 'http://www.shadow-net.org/product_images/l/294/orf_sport_plus__00985_thumb.jpg' ] ,
 [ 'Phoenix' , 'http://www.shadow-net.org/channels/Phoenix.html' , 'http://www.shadow-net.org/product_images/x/727/Phoenix_Logo_2012.svg__42553_thumb.png' ] ,
 [ 'ProSieben' , 'http://www.shadow-net.org/channels/ProSieben.html' , 'http://www.shadow-net.org/product_images/j/009/pro7__88480_thumb.jpg' ] ,
 [ 'RBB Berlin' , 'http://www.shadow-net.org/channels/RBB-Berlin.html' , 'http://www.shadow-net.org/product_images/j/738/rbb_de__66295_thumb.jpg' ] ,
 [ 'RTL' , 'http://www.shadow-net.org/channels/RTL.html' , 'http://www.shadow-net.org/product_images/i/119/rtl__48257_thumb.jpg' ] ,
 [ 'RTL 2' , 'http://www.shadow-net.org/channels/RTL-2.html' , 'http://www.shadow-net.org/product_images/p/269/rtl__41751_thumb.jpg' ] ,
 [ 'Sat.1' , 'http://www.shadow-net.org/channels/Sat.1.html' , 'http://www.shadow-net.org/product_images/f/936/sat1__13963_thumb.jpg' ] ,
 [ 'Servus TV' , 'http://www.shadow-net.org/channels/Servus-TV.html' , 'http://www.shadow-net.org/product_images/o/951/servus_tv_de__91079_thumb.jpg' ] ,
 [ 'Sky Sport News' , 'http://www.shadow-net.org/channels/Sky-Sport-News.html' , 'http://www.shadow-net.org/product_images/w/904/ssn-de__00706_thumb.jpg' ] ,
 [ 'SWR' , 'http://www.shadow-net.org/channels/SWR.html' , 'http://www.shadow-net.org/product_images/m/405/swr__19794_thumb.jpg' ] ,
 [ 'tagesschau24' , 'http://www.shadow-net.org/channels/tagesschau24.html' , 'http://www.shadow-net.org/product_images/f/462/301px-Tagesschau24-2012__84641_thumb.png' ] ,
 [ 'WDR Fernsehen' , 'http://www.shadow-net.org/channels/WDR-Fernsehen.html' , 'http://www.shadow-net.org/product_images/p/281/wdr_fernsehen_koln__11515_thumb.jpg' ] ,
 [ 'ZDF' , 'http://www.shadow-net.org/channels/ZDF.html' , 'http://www.shadow-net.org/product_images/l/154/zdf__67759_thumb.jpg' ] ,
 [ 'ZDF Neo' , 'http://www.shadow-net.org/channels/ZDF-Neo.html' , 'http://www.shadow-net.org/product_images/a/558/zdf_neo__47353_thumb.jpg' ] ,
 [ 'Cielo' , 'http://www.shadow-net.org/channels/Cielo.html' , 'http://www.shadow-net.org/product_images/c/953/cielo__18877_thumb.jpg' ] ,
 [ 'Moto GP' , 'http://www.shadow-net.org/channels/Moto-GP.html' , 'http://www.shadow-net.org/product_images/b/103/Moto_Gp_logo__65728_thumb.png' ] ,
 [ 'Rai 1' , 'http://www.shadow-net.org/channels/Rai-1.html' , 'http://www.shadow-net.org/product_images/m/362/Rai_1_logo__67635_thumb.png' ] ,
 [ 'Rai 2' , 'http://www.shadow-net.org/channels/Rai-2.html' , 'http://www.shadow-net.org/product_images/t/148/Rai_2_logo__79173_thumb.png' ] ,
 [ 'Rai 3' , 'http://www.shadow-net.org/channels/Rai-3.html' , 'http://www.shadow-net.org/product_images/w/005/Rai_3_logo__60097_thumb.png' ] ,
 [ 'Rai 4' , 'http://www.shadow-net.org/channels/Rai-4.html' , 'http://www.shadow-net.org/product_images/o/852/Rai_4_2010__78387_thumb.png' ] ,
 [ 'Rai 5' , 'http://www.shadow-net.org/channels/Rai-5.html' , 'http://www.shadow-net.org/product_images/a/799/Rai_5_logo__81811_thumb.png' ] ,
 [ 'Rai Movie' , 'http://www.shadow-net.org/channels/Rai-Movie.html' , 'http://www.shadow-net.org/product_images/l/506/RAI_Movie_2010_Logo__63887_thumb.png' ] ,
 [ 'RSI La 1' , 'http://www.shadow-net.org/channels/RSI-La-1.html' , 'http://www.shadow-net.org/product_images/i/330/rsi_la1__95748_thumb.jpg' ] ,
 [ 'RSI La 2' , 'http://www.shadow-net.org/channels/RSI-La-2.html' , 'http://www.shadow-net.org/product_images/q/536/rsi_la2__31571_thumb.jpg' ] ,
 [ 'Sky Calcio' , 'http://www.shadow-net.org/channels/Sky-Calcio.html' , 'http://www.shadow-net.org/product_images/a/134/sky_it_calcio__42011_thumb.png' ] ,
 [ 'Sky Sport 1' , 'http://www.shadow-net.org/channels/Sky-Sport-1.html' , 'http://www.shadow-net.org/product_images/z/059/sky_iit_sport1__99735_thumb.jpg' ] ,
 [ 'Sky Sport 2' , 'http://www.shadow-net.org/channels/Sky-Sport-2.html' , 'http://www.shadow-net.org/product_images/j/187/sky_iit_sport2__17630_thumb.jpg' ] ,
 [ 'Sky Sport 24' , 'http://www.shadow-net.org/channels/Sky-Sport-24.html' , 'http://www.shadow-net.org/product_images/h/134/skysport24italia__08307_thumb.png' ] ,
 [ 'Sky TG24' , 'http://www.shadow-net.org/channels/Sky-TG24.html' , 'http://www.shadow-net.org/product_images/u/637/SKY_TG24__09392_thumb.png' ] ,
 [ 'Bein Sport 1 FR' , 'http://www.shadow-net.org/channels/Bein-Sport-1-FR.html' , 'http://www.shadow-net.org/product_images/b/770/beinsport-2012_logo_chaine1__77633_thumb.jpg' ] ,
 [ 'Bein Sport 3 FR' , 'http://www.shadow-net.org/channels/Bein-Sport-3-FR.html' , 'http://www.shadow-net.org/product_images/s/959/bein_sports3__90672_thumb.png' ] ,
 [ 'BFM TV' , 'http://www.shadow-net.org/channels/BFM-TV.html' , 'http://www.shadow-net.org/product_images/j/523/BFMTV__21435_thumb.png' ] ,
 [ 'Canal+ Sport' , 'http://www.shadow-net.org/channels/Canal%252b-Sport.html' , 'http://www.shadow-net.org/product_images/l/502/Canal__Sport_logo_2009__01668_thumb.png' ] ,
 [ 'Clubbing TV' , 'http://www.shadow-net.org/channels/Clubbing-TV.html' , 'http://www.shadow-net.org/product_images/z/053/Clubbing_TV__57209_thumb.png' ] ,
 [ 'Euronews FR' , 'http://www.shadow-net.org/channels/Euronews-FR.html' , 'http://www.shadow-net.org/product_images/f/716/euronews__96297_thumb.jpg' ] ,
 [ 'Eurosport France' , 'http://www.shadow-net.org/channels/Eurosport-France.html' , 'http://www.shadow-net.org/product_images/g/221/eurosport__72244_thumb.jpg' ] ,
 [ 'FashionTV' , 'http://www.shadow-net.org/channels/FashionTV.html' , 'http://www.shadow-net.org/product_images/f/442/fashion_tv__10290_thumb.jpg' ] ,
 [ 'France 2' , 'http://www.shadow-net.org/channels/France-2.html' , 'http://www.shadow-net.org/product_images/y/747/france2__29267_thumb.jpg' ] ,
 [ 'France 24 FR' , 'http://www.shadow-net.org/channels/France-24-FR.html' , 'http://www.shadow-net.org/product_images/i/642/FRANCE_24_logo__69539_thumb.png' ] ,
 [ 'France 3' , 'http://www.shadow-net.org/channels/France-3.html' , 'http://www.shadow-net.org/product_images/j/518/france3__66917_thumb.jpg' ] ,
 [ 'France 4' , 'http://www.shadow-net.org/channels/France-4.html' , 'http://www.shadow-net.org/product_images/z/320/france4__06723_thumb.jpg' ] ,
 [ 'France 5' , 'http://www.shadow-net.org/channels/France-5.html' , 'http://www.shadow-net.org/product_images/x/498/france5__26772_thumb.jpg' ] ,
 [ 'France Ã”' , 'http://www.shadow-net.org/channels/France-%C3%94.html' , 'http://www.shadow-net.org/product_images/n/983/france_o__96943_thumb.jpg' ] ,
 [ 'M6' , 'http://www.shadow-net.org/channels/M6.html' , 'http://www.shadow-net.org/product_images/t/686/m6__79935_thumb.jpg' ] ,
 [ 'RTS Deux' , 'http://www.shadow-net.org/channels/RTS-Deux.html' , 'http://www.shadow-net.org/product_images/y/153/rts_deux__51855_thumb.jpg' ] ,
 [ 'RTS Un' , 'http://www.shadow-net.org/channels/RTS-Un.html' , 'http://www.shadow-net.org/product_images/y/407/rts_un__92413_thumb.jpg' ] ,
 [ 'TF1' , 'http://www.shadow-net.org/channels/TF1.html' , 'http://www.shadow-net.org/product_images/w/668/tf1__68155_thumb.jpg' ] ,
 [ 'SRF 1' , 'http://www.shadow-net.org/channels/SRF-1.html' , 'http://www.shadow-net.org/product_images/p/122/srf_1_ch__27802_thumb.jpg' ] ,
 [ 'SRF 2' , 'http://www.shadow-net.org/channels/SRF-2.html' , 'http://www.shadow-net.org/product_images/u/790/srf_2_ch__91017_thumb.png' ] ,
 [ 'SRF Info' , 'http://www.shadow-net.org/channels/SRF-Info.html' , 'http://www.shadow-net.org/product_images/k/191/srf_info_ch__59722_thumb.jpg' ] ,
 [ 'SVT1' , 'http://www.shadow-net.org/channels/SVT1.html' , 'http://www.shadow-net.org/product_images/j/839/svt_1__03141_thumb.jpg' ] ,
 [ 'SVT2' , 'http://www.shadow-net.org/channels/SVT2.html' , 'http://www.shadow-net.org/product_images/d/662/svt_2__30340_thumb.jpg' ] ,
 [ 'TV4 Sweden' , 'http://www.shadow-net.org/channels/TV4-Sweden.html' , 'http://www.shadow-net.org/product_images/k/588/tv4__72223_thumb.jpg' ] ,
 [ 'Al Jazeera Arabic' , 'http://www.shadow-net.org/channels/Al-Jazeera-Arabic.html' , 'http://www.shadow-net.org/product_images/n/253/aljazeera__84338_thumb.png' ] ,
 [ 'Al Jazeera Documentary' , 'http://www.shadow-net.org/channels/Al-Jazeera-Documentary.html' , 'http://www.shadow-net.org/product_images/b/160/Al_Jazeera_Documentary_Channel__34510_thumb.png' ] ,
 [ 'BBC Arabic' , 'http://www.shadow-net.org/channels/BBC-Arabic.html' , 'http://www.shadow-net.org/product_images/x/782/bbc_arabic__71485_thumb.PNG' ] ,
 [ 'Bein Sports 1' , 'http://www.shadow-net.org/channels/Bein-Sports-1.html' , 'http://www.shadow-net.org/product_images/h/891/bein_sports1__51322_thumb.png' ] ,
 [ 'Bein Sports 10' , 'http://www.shadow-net.org/channels/Bein-Sports-10.html' , 'http://www.shadow-net.org/product_images/k/284/bein_sports10__25010_thumb.png' ] ,
 [ 'Bein Sports 11' , 'http://www.shadow-net.org/channels/Bein-Sports-11.html' , 'http://www.shadow-net.org/product_images/g/582/bein_sports11__25618_thumb.png' ] ,
 [ 'Bein Sports 12' , 'http://www.shadow-net.org/channels/Bein-Sports-12.html' , 'http://www.shadow-net.org/product_images/f/600/bein_sports12__01362_thumb.png' ] ,
 [ 'Bein Sports 2' , 'http://www.shadow-net.org/channels/Bein-Sports-2.html' , 'http://www.shadow-net.org/product_images/x/414/BeIN_SPORTS_2HD_Couleur__35070_thumb.jpg' ] ,
 [ 'Bein Sports 3' , 'http://www.shadow-net.org/channels/Bein-Sports-3.html' , 'http://www.shadow-net.org/product_images/s/745/bein-sports-3-hd_14gzpciv0r55j1l92btw93npju__75859_thumb.png' ] ,
 [ 'Bein Sports 4' , 'http://www.shadow-net.org/channels/Bein-Sports-4.html' , 'http://www.shadow-net.org/product_images/g/293/Bein_4__71534_thumb.png' ] ,
 [ 'Bein Sports 5' , 'http://www.shadow-net.org/channels/Bein-Sports-5.html' , 'http://www.shadow-net.org/product_images/k/320/bein_sports5__41625_thumb.png' ] ,
 [ 'Bein Sports 6' , 'http://www.shadow-net.org/channels/Bein-Sports-6.html' , 'http://www.shadow-net.org/product_images/y/276/bein_sports6__65337_thumb.png' ] ,
 [ 'Bein Sports 7' , 'http://www.shadow-net.org/channels/Bein-Sports-7.html' , 'http://www.shadow-net.org/product_images/v/858/bein_sports7__44128_thumb.png' ] ,
 [ 'Bein Sports 8' , 'http://www.shadow-net.org/channels/Bein-Sports-8.html' , 'http://www.shadow-net.org/product_images/g/028/bein_sports8__04092_thumb.png' ] ,
 [ 'Bein Sports 9' , 'http://www.shadow-net.org/channels/Bein-Sports-9.html' , 'http://www.shadow-net.org/product_images/w/291/bein_sport_9hd__26067_thumb.png' ] ,
 [ 'Dubai Racing 2' , 'http://www.shadow-net.org/channels/Dubai-Racing-2.html' , 'http://www.shadow-net.org/product_images/a/902/dubai_ae_racing_2__14904_thumb.png' ] ,
 [ 'Dubai Sports' , 'http://www.shadow-net.org/channels/Dubai-Sports.html' , 'http://www.shadow-net.org/product_images/g/112/dubai_sports_1__09676_thumb.jpg' ] ,
 [ 'Rotana' , 'http://www.shadow-net.org/channels/Rotana.html' , 'http://www.shadow-net.org/product_images/h/109/rotana__51692_thumb.png' ] ,
 [ 'Rotana Aflam' , 'http://www.shadow-net.org/channels/Rotana-Aflam.html' , 'http://www.shadow-net.org/product_images/s/576/rotana-aflam__90584_thumb.jpg' ] ,
 [ 'Rotana Cinema' , 'http://www.shadow-net.org/channels/Rotana-Cinema.html' , 'http://www.shadow-net.org/product_images/v/166/rotana_cinema__49210_thumb.png' ] ,
 [ 'Sky News Arabia' , 'http://www.shadow-net.org/channels/Sky-News-Arabia.html' , 'http://www.shadow-net.org/product_images/z/091/Sky_News_Arabia_logo__60552_thumb.png' ] ,
 [ 'Cartoon Network India' , 'http://www.shadow-net.org/channels/Cartoon-Network-India.html' , 'http://www.shadow-net.org/product_images/c/252/cartoon_network__59462_thumb.jpg' ] ,
 [ 'Geo News' , 'http://www.shadow-net.org/channels/Geo-News.html' , 'http://www.shadow-net.org/product_images/a/380/Geo_News_logo__24770_thumb.png' ] ,
 [ 'Geo Super' , 'http://www.shadow-net.org/channels/Geo-Super.html' , 'http://www.shadow-net.org/product_images/z/651/Geo_Super_logo__26737_thumb.png' ] ,
 [ 'PTV Sports' , 'http://www.shadow-net.org/channels/PTV-Sports.html' , 'http://www.shadow-net.org/product_images/f/847/ptv_sports_pk__13660_thumb.jpg' ] ,
 [ 'Sony Six' , 'http://www.shadow-net.org/channels/Sony-Six.html' , 'http://www.shadow-net.org/product_images/l/133/sony_six_in__32068_thumb.jpg' ] ,
 [ 'Astro Supersport 1' , 'http://www.shadow-net.org/channels/Astro-Supersport-1.html' , 'http://www.shadow-net.org/product_images/o/658/astro_supersport__73976_thumb.png' ] ,
 [ 'Astro Supersport 2' , 'http://www.shadow-net.org/channels/Astro-Supersport-2.html' , 'http://www.shadow-net.org/product_images/m/406/Astro_SuperSport2__81600_thumb.jpg' ] ,
 [ 'Astro Supersport 3' , 'http://www.shadow-net.org/channels/Astro-Supersport-3.html' , 'http://www.shadow-net.org/product_images/y/587/Astro_SuperSport_3_logo__27574_thumb.png' ] ,
 [ 'Astro Supersport 4' , 'http://www.shadow-net.org/channels/Astro-Supersport-4.html' , 'http://www.shadow-net.org/product_images/i/619/gambar_astro_supersport_4__72673_thumb.JPG' ] ,
 [ 'Real Madrid TV' , 'http://www.shadow-net.org/channels/Real-Madrid-TV.html' , 'http://www.shadow-net.org/product_images/u/980/real_madrid_tv_es__39458_thumb.png' ] ,
 [ 'BritAsia TV' , 'http://www.shadow-net.org/channels/BritAsia-TV.html' , 'http://www.shadow-net.org/product_images/a/374/brit_asia_tv__34173_thumb.jpg' ] ]
if 28 - 28: iIii1I11I1II1 % Oo0Ooo * I1IiiI % Ii1I * o0oOOo0O0Ooo / o0oOOo0O0Ooo
def o00oOO0 ( ) :
 o00O = oOoOo00oOo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0OOO00oo = o00O . lower ( )
 O0i1II1Iiii1I11 ( OOO0OOO00oo )
 if 5 - 5: I1IiiI
def O0i1II1Iiii1I11 ( name ) :
 try :
  OOO0OOO00oo = name
  oOOoo00O00o = { "User-Agent" : "Mozilla/5.0" }
  iIiIi11iI = [ ]
  Oo0O00O000 = [ ]
  i11I1IiII1i1i = [ ]
  ooI1111i = '5'
  iIIii = xbmcgui . DialogProgress ( )
  iIiIi11iI . append ( 'a' )
  o00O0O = int ( II111iiiiII . getSetting ( 'Results' ) ) / float ( len ( iIiIi11iI ) ) * 100
  O00oO = requests . get ( 'http://www.iptvultra.com/' , headers = oOOoo00O00o ) . text
  oO0Oo = re . compile ( '<span class="link"><a href="(.+?)">(.+?)</a>' ) . findall ( O00oO )
  iIIii . create ( 'Checking for stream - ' + OOO0OOO00oo )
  iIIii . update ( int ( o00O0O ) , 'You can always cancel if you\'re happy with results' , str ( len ( iIiIi11iI ) - 1 ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Results' ) ) ) + ' Results' )
  if II111iiiiII . getSetting ( 'Freeworld' ) == 'true' :
   if int ( len ( iIiIi11iI ) - 1 ) <= int ( II111iiiiII . getSetting ( 'Results' ) ) :
    ii1iii1i = I11i1I1I ( 'http://freeworldwideiptv.com/' )
    Iii1I1111ii = re . compile ( '<h2 class="title">.+?<a href="(.+?)"' , re . DOTALL ) . findall ( ii1iii1i )
    for ooOoO00 in Iii1I1111ii :
     i11I1IiII1i1i . append ( ooOoO00 [ 0 ] )
     Ii1IIiI1i = I11i1I1I ( ooOoO00 )
     o0O00Oo0 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( Ii1IIiI1i )
     for IiII111i1i11 , i111iIi1i1II1 in o0O00Oo0 :
      if ( OOO0OOO00oo ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) in ( IiII111i1i11 ) . lower ( ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) :
       iIIii . update ( int ( o00O0O ) , 'Checking Freeworld ' + str ( len ( i11I1IiII1i1i ) ) + '/' + str ( len ( Iii1I1111ii ) ) , str ( len ( iIiIi11iI ) - 1 ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Results' ) ) ) + ' Results' )
       iIiIi11iI . append ( i111iIi1i1II1 [ 0 ] )
       i111iIi1i1II1 = iI11iiiI1II + i111iIi1i1II1
       o0OoOO000ooO0 ( 'Freeworld | ' + IiII111i1i11 , i111iIi1i1II1 , 10 , '' , '' , '' , '' )
   else :
    pass
  if II111iiiiII . getSetting ( 'Live_Online' ) == 'true' :
   if int ( len ( iIiIi11iI ) - 1 ) <= int ( II111iiiiII . getSetting ( 'Results' ) ) :
    for oooO in OOO :
     name = oooO [ 0 ]
     Iii111II = O0oooo0Oo00 + oooO [ 1 ]
     if ( OOO0OOO00oo ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) in ( name ) . lower ( ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) :
      try :
       iIIii . update ( int ( o00O0O ) , 'Checking Live Online' , str ( len ( iIiIi11iI ) - 1 ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Results' ) ) ) + ' Results' )
      except :
       pass
      iIiIi11iI . append ( Iii111II [ 0 ] )
      o0OoOO000ooO0 ( 'LiveOnline | ' + name , Iii111II , 10 , '' , '' , '' , '' )
   else :
    pass
  if II111iiiiII . getSetting ( 'Shadow' ) == 'true' :
   if int ( len ( iIiIi11iI ) - 1 ) <= int ( II111iiiiII . getSetting ( 'Results' ) ) :
    for II1I in I1IIIiIiI1 :
     name = II1I [ 0 ]
     Iii111II = II1I [ 1 ]
     ooo00OOOooO = II1I [ 2 ]
     if ( OOO0OOO00oo ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) in ( name ) . lower ( ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) :
      iIiIi11iI . append ( Iii111II [ 0 ] )
      iIIii . update ( int ( o00O0O ) , 'Checking Shadow' , str ( len ( iIiIi11iI ) - 1 ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Results' ) ) ) + ' Results' )
      o0OoOO000ooO0 ( 'Shadow | ' + name , Iii111II , 9 , ooo00OOOooO , '' , '' , '' )
   else :
    pass
  if II111iiiiII . getSetting ( 'Freeview' ) == 'true' :
   if int ( len ( iIiIi11iI ) - 1 ) <= int ( II111iiiiII . getSetting ( 'Results' ) ) :
    for object in oo :
     I11iiI1i1 = object [ 1 ]
     name = object [ 0 ]
     I11iiI1i1 = object [ 1 ]
     i1I1i111Ii = object [ 2 ]
     if ( OOO0OOO00oo ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) in ( name ) . lower ( ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) :
      iIiIi11iI . append ( Iii111II [ 0 ] )
      iIIii . update ( int ( o00O0O ) , 'Checking Freeview' , str ( len ( iIiIi11iI ) - 1 ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Results' ) ) ) + ' Results' )
      try :
       ooo ( 'Freeview | ' + name , I11iiI1i1 , i1I1i111Ii , '' )
      except :
       pass
   else :
    pass
  if II111iiiiII . getSetting ( 'Mama_HD' ) == 'true' :
   if int ( len ( iIiIi11iI ) - 1 ) <= int ( II111iiiiII . getSetting ( 'Results' ) ) :
    for i1i1iI1iiiI in oOOOoo0O0oO :
     Ooo0oOooo0 = i1i1iI1iiiI [ 0 ]
     name = i1i1iI1iiiI [ 1 ]
     if ( OOO0OOO00oo ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) in ( name ) . lower ( ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) :
      iIIii . update ( int ( o00O0O ) , 'Checking Mama HD' , str ( len ( iIiIi11iI ) - 1 ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Results' ) ) ) + ' Results' )
      iIiIi11iI . append ( Iii111II [ 0 ] )
      o0OoOO000ooO0 ( 'Mama Hd | ' + name , O0oooo0Oo00 + Ooo0oOooo0 , 10 , '' , '' , '' , '' )
   else :
    pass
  if II111iiiiII . getSetting ( 'IPTVsat' ) == 'true' :
   if int ( len ( iIiIi11iI ) - 1 ) <= int ( II111iiiiII . getSetting ( 'Results' ) ) :
    oOOOoo00 = I11i1I1I ( 'http://www.iptvsat.com/' )
    OO = re . compile ( "<h2 class='post-title entry-title.+?<a href='(.+?)'>(.+?)</a>" , re . DOTALL ) . findall ( oOOOoo00 )
    for Iii111II , name in OO :
     iiIiIIIiiI = I11i1I1I ( Iii111II )
     iiI1IIIi = re . compile ( '#EXTINF:-1,(.+?)</h4>\n<h4 style="clear: both; text-align: center;">\n(.+?)</h4>' ) . findall ( iiIiIIIiiI )
     for o000O0o , IiI1io0O in iiI1IIIi :
      if ( OOO0OOO00oo ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) in ( o000O0o ) . lower ( ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) :
       iIIii . update ( int ( o00O0O ) , 'Checking IPTVsat' , str ( len ( iIiIi11iI ) - 1 ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Results' ) ) ) + ' Results' )
       iIiIi11iI . append ( Iii111II [ 0 ] )
       o0OoOO000ooO0 ( 'IPTVSat | ' + o000O0o , iI11iiiI1II + Ooo0oOooo0 , 10 , '' , '' , '' , '' )
   else :
    pass
  if II111iiiiII . getSetting ( 'IPTVUrl' ) == 'true' :
   if int ( len ( iIiIi11iI ) - 1 ) <= int ( II111iiiiII . getSetting ( 'Results' ) ) :
    II11IiIi11 = I11i1I1I ( 'http://www.iptvurllist.com/' )
    IIOOO0O00O0OOOO = re . compile ( '<h1><a href="(.+?)">' ) . findall ( II11IiIi11 )
    for I1iiii1I in IIOOO0O00O0OOOO :
     i111iIi1i1II1 = 'http://www.iptvurllist.com/' + I1iiii1I
     OOo0 = I11i1I1I ( i111iIi1i1II1 )
     oO00ooooO0o = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n' ) . findall ( OOo0 )
     for name , oo0o in oO00ooooO0o :
      if ( OOO0OOO00oo ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) in ( name ) . lower ( ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) :
       iIIii . update ( int ( o00O0O ) , 'Checking IPTVUrl' , str ( len ( iIiIi11iI ) - 1 ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Results' ) ) ) + ' Results' )
       iIiIi11iI . append ( Iii111II [ 0 ] )
       o0OoOO000ooO0 ( 'IPTVUrl | ' + name , iI11iiiI1II + oo0o , 10 , '' , '' , '' , '' )
   else :
    pass
  if II111iiiiII . getSetting ( 'Ingenious' ) == 'true' :
   for Iii111II , name in oO0Oo :
    try :
     Oo0O00O000 . append ( Iii111II [ 0 ] )
     if int ( len ( Oo0O00O000 ) ) <= int ( II111iiiiII . getSetting ( 'Sources' ) ) and int ( len ( iIiIi11iI ) - 1 ) <= int ( II111iiiiII . getSetting ( 'Results' ) ) :
      iIIii . update ( int ( o00O0O ) , 'Checking Ingenious list ' + str ( len ( Oo0O00O000 ) ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Sources' ) ) ) , str ( len ( iIiIi11iI ) ) + '/' + str ( int ( II111iiiiII . getSetting ( 'Results' ) ) ) + ' Results' )
      if iIIii . iscanceled ( ) :
       return
      oOOOoo00 = requests . get ( Iii111II , headers = oOOoo00O00o ) . text
      OO = re . compile ( '".+?[@](.+?)[@].+?[@].+?[@](.+?)"' ) . findall ( oOOOoo00 )
      for name , IiI1io0O in OO :
       name = name . replace ( '[' , '' ) . replace ( ']' , '' )
       if name [ 0 ] == ' ' :
        name = name [ 1 : ]
       elif name [ - 1 ] == ' ' :
        name = name [ : - 1 ]
       I11iiI1i1 = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + IiI1io0O . replace ( '[' , '' ) . replace ( ']' , '' ) + ';name=vendetta'
       if ( OOO0OOO00oo ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) in ( name ) . lower ( ) . replace ( ' ' , '' ) . replace ( 'sports' , 'sport' ) :
        iIiIi11iI . append ( Iii111II [ 0 ] )
        try :
         o0OoOO000ooO0 ( 'Ingenious | ' + name , I11iiI1i1 , 10 , '' , '' , '' , '' )
        except :
         pass
     else :
      pass
    except :
     pass
 except :
  pass
  if 51 - 51: I11i % I1IiiI
def ooo ( name , url , mode , iconimage ) :
 OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i11III1111iIi = True
 I1i111I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i111I . setProperty ( 'fanart_image' , Ooo )
 I1i111I . setProperty ( "IsPlayable" , "true" )
 i11III1111iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOo , listitem = I1i111I , isFolder = False )
 return i11III1111iIi
 if 65 - 65: O0 * OoooooooOO % OOooOOo / IiII - Ii1I / I11i
 if 56 - 56: I1IiiI * i11iIiiIii * I1Ii111
def oOoOo0O0OOOoO ( Search_name , next_url ) :
 oOOOoo00 = requests . get ( next_url ) . text
 oO0oo0o = re . compile ( '<ul class="ProductList  Clear" >(.+?)<br class="Clear" />' , re . DOTALL ) . findall ( oOOOoo00 )
 for oooO in oO0oo0o :
  OO = re . compile ( '<div class="ProductImage">.+?<a href="(.+?)".+?img src="(.+?)" alt="(.+?)" />' , re . DOTALL ) . findall ( str ( oooO . encode ( 'utf-8' ) ) )
  for Iii111II , ooo00OOOooO , oOOoo0Oo in OO :
   if ( Search_name ) . replace ( ' ' , '' ) in ( oOOoo0Oo ) . replace ( ' ' , '' ) . lower ( ) :
    o0OoOO000ooO0 ( 'Shadow | ' + oOOoo0Oo , Iii111II , 9 , ooo00OOOooO , '' , '' , '' )
    if 50 - 50: ooOoO0o
    if 47 - 47: Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / OoO0O00 - OoooooooOO
    if 33 - 33: OoOoOO00 * OOooOOo - II111iiii
def OOo0o0O0O ( url ) :
 o0OO0o0oOOO0O = liveresolver . resolve ( url )
 II1I = xbmcgui . ListItem ( path = o0OO0o0oOOO0O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , II1I )
 if 49 - 49: I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii
def o000ooooO0o ( name , url ) :
 import re , urllib , json
 iI1i11 = OoOOoooOO0O ( "http://tvplayer.com/watch/" )
 ooo00Ooo = url
 Oo0o0O00 = re . findall ( 'var validate = "(.*?)"' , iI1i11 ) [ 0 ]
 if 40 - 40: OoooooooOO
 I1i1i1 = CookieJar ( )
 OoO0O00O0oo0O = urllib . urlencode ( { 'service' : '1' , 'platform' : 'website' , 'token' : 'null' , 'validate' : Oo0o0O00 , 'id' : ooo00Ooo } )
 oOOoo00O00o = { 'Referer' : 'http://tvplayer.com/watch/' , 'Origin' : 'http://tvplayer.com' , 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }
 I1IiI11 = OoOOoooOO0O ( "http://api.tvplayer.com/api/v2/stream/live" , data = OoO0O00O0oo0O , headers = oOOoo00O00o , cj = I1i1i1 ) ;
 iI1iiiiIii = json . loads ( I1IiI11 )
 if 19 - 19: OoO0O00 - Oo0Ooo . O0
 I1i1i1 = CookieJar ( )
 ooOo00 = iI1iiiiIii [ "tvplayer" ] [ "response" ] [ "stream" ]
 OoOOoooOO0O ( ooOo00 , headers = oOOoo00O00o , cj = I1i1i1 ) ;
 ooOo00 = ooOo00 + '|Cookie=%s&User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36&X-Requested-With=ShockwaveFlash/22.0.0.209&Referer=http://tvplayer.com/watch/' % OOoo ( I1i1i1 )
 iIo0O ( name , ooOo00 )
 return
 if 50 - 50: OoO0O00
def OoOOoooOO0O ( url , data = None , headers = None , cj = None ) :
 ii = urllib2 . HTTPCookieProcessor ( cj )
 Iiii1iI1i = urllib2 . build_opener ( ii , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
 IIiI1Ii = urllib2 . Request ( url )
 if 57 - 57: OOooOOo - ooOoO0o - I11i + OoO0O00
 IIiI1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 if headers :
  for I1IIIiI11i1 in headers :
   IIiI1Ii . add_header ( I1IIIiI11i1 , headers [ I1IIIiI11i1 ] )
 i11I1I1I = Iiii1iI1i . open ( IIiI1Ii , data = data )
 Ooo0oOooo0 = i11I1I1I . read ( )
 i11I1I1I . close ( )
 return Ooo0oOooo0
 if 64 - 64: Ii1I
def OOoo ( cookieJar ) :
 try :
  oo00O00Oo = ""
  for IIIII1II , iI1 in enumerate ( cookieJar ) :
   oo00O00Oo += iI1 . name + "=" + iI1 . value + ";"
 except : pass
 if 12 - 12: I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI / iII111i
 return oo00O00Oo
 if 12 - 12: OOooOOo - ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
def IiIiII1 ( ) :
 o0oO = [ 'Select by Virgin No.' , 'Select by Sky No.' , 'Select by Freeview No.' ]
 I1i1iii = xbmcgui . Dialog ( ) . select ( 'Search by channel number' , o0oO )
 if I1i1iii == 0 :
  Iii1iiIi1II (
 'http://www.tvguide.co.uk/?catcolor=&systemid=25&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ,
 'Virgin' )
 if I1i1iii == 1 :
  Iii1iiIi1II (
 'http://www.tvguide.co.uk/?catcolor=&systemid=5&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ,
 'Sky' )
 if I1i1iii == 2 :
  Iii1iiIi1II (
 'http://www.tvguide.co.uk/?catcolor=&systemid=3&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ,
 'Freeview' )
  if 60 - 60: I1IiiI - oO0o * I11i % II111iiii
  if 62 - 62: iIii1I11I1II1
def Iii1iiIi1II ( url , name ) :
 i1II = xbmcgui . Dialog ( ) . input ( "Channel No" , type = xbmcgui . INPUT_NUMERIC )
 iI1I = requests . get ( url ) . text
 oO0Oo = re . compile ( 'qt-text="(.+?)" title="(.+?)"' ) . findall ( iI1I )
 for OooOoOo , III1I1Iii1iiI in oO0Oo :
  III1I1Iii1iiI = III1I1Iii1iiI . replace ( ' TV listings' , '' )
  OooOoOo = OooOoOo . replace ( 'Channel Numbers<br> ' , '' )
  if ':' in OooOoOo :
   if name == 'Sky' :
    i1Iii11I1i = re . compile ( 'Sky:(.+?) ' ) . findall ( str ( OooOoOo ) )
    for II1I in i1Iii11I1i :
     if i1II in i1Iii11I1i :
      iiii11I ( '' , url , str ( III1I1Iii1iiI ) )
   elif name == 'Virgin' :
    Oo00o0OO0O00o = re . compile ( 'Virgin:(.+?) ' ) . findall ( str ( OooOoOo ) )
    for II1I in Oo00o0OO0O00o :
     if i1II in Oo00o0OO0O00o :
      iiii11I ( '' , url , str ( III1I1Iii1iiI ) )
   elif name == 'Freeview' :
    O0Oooo = re . compile ( 'Freeview:(.+?) ' ) . findall ( str ( OooOoOo ) )
    for II1I in O0Oooo :
     if i1II in O0Oooo :
      iiii11I ( '' , url , str ( III1I1Iii1iiI ) )
      if 21 - 21: Oo0Ooo
def I1ii1 ( url ) :
 i1IiiiI1iI = [ [ 'All' , 'http://www.tvguide.co.uk/?catcolor=&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Comedy' , 'http://www.tvguide.co.uk/?catcolor=3253CF&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Sports' , 'http://www.tvguide.co.uk/?catcolor=53CE32&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Music' , 'http://www.tvguide.co.uk/?catcolor=FF9933&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Film' , 'http://www.tvguide.co.uk/?catcolor=000000&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Soap' , 'http://www.tvguide.co.uk/?catcolor=AB337D&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Kids' , 'http://www.tvguide.co.uk/?catcolor=E3BB00&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Drama' , 'http://www.tvguide.co.uk/?catcolor=CE3D32&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Talk show' , 'http://www.tvguide.co.uk/?catcolor=800000&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Game show' , 'http://www.tvguide.co.uk/?catcolor=669999&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Sci-fi' , 'http://www.tvguide.co.uk/?catcolor=666699&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Documentary' , 'http://www.tvguide.co.uk/?catcolor=CCCCCC&systemid=' + url + '&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Motor' , 'http://www.tvguide.co.uk/?catcolor=996633&systemid=7&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Horror' , 'http://www.tvguide.co.uk/?catcolor=666633&systemid=7&thistime=' + IiIiIi + '&thisDay=' + i1I111I + '/' + i11I1IIiiIi + '/' + iii11iII + '&gridspan=03:00&view=0&gw=1323' ] ]
 for II1I in i1IiiiI1iI :
  oOOoo0Oo = II1I [ 0 ]
  O00 = II1I [ 1 ]
  OOoo0O0 ( oOOoo0Oo , O00 , 11 , '' , '' , '' , '' )
  if 92 - 92: iIii1I11I1II1 * i1IIi * iII111i % OOooOOo % I1ii11iIi11i + II111iiii
def i1iIi1I1i ( url ) :
 i1IiiiI1iI = [ ]
 O00oO = requests . get ( url ) . text
 oO0oo0o = re . compile ( '<div class="Block CategoryContent Moveable Panel"(.+?)<br class="Clear" />' , re . DOTALL ) . findall ( O00oO )
 for II1I in oO0oo0o :
  oO0Oo = re . compile ( '<div class="ProductImage">.+?<a href="(.+?)".+?img src="(.+?)" alt="(.+?)" />' , re . DOTALL ) . findall ( str ( II1I . encode ( 'utf-8' ) ) )
  for url , ooo00OOOooO , oOOoo0Oo in oO0Oo :
   o0OoOO000ooO0 ( oOOoo0Oo , url , 9 , ooo00OOOooO , '' , '' , '' )
 next = re . compile ( '<div class="FloatRight"><a href="(.+?)">.+?</a>' ) . findall ( O00oO )
 for url in next :
  if 'skippy' not in i1IiiiI1iI :
   OOoo0O0 ( 'Next Page' , url , 8 , '' , '' , '' , '' )
   i1IiiiI1iI . append ( 'skippy' )
   if 1 - 1: I11i % OOooOOo + O0 + i1IIi - OoO0O00
def iIIIII1ii1I ( name , url ) :
 I11iiI1i1 = O0oooo0Oo00 + url
 O00oO = requests . get ( url ) . text
 Ii1i1iI = re . compile ( '<source src="(.+?)"' ) . findall ( O00oO )
 for II1I in Ii1i1iI :
  I11iiI1i1 = II1I
 iIo0O ( name , I11iiI1i1 )
 if 16 - 16: OOooOOo / Oo0Ooo / OoooooooOO * I1IiiI + i1IIi % OOooOOo
 if 71 - 71: OoOoOO00
def iiii11I ( name , url , extra ) :
 try :
  iI1I = requests . get ( url ) . text
  ii111IiiI1 = re . compile ( '<div class="div-epg-channel-progs">.+?<div class="div-epg-channel-name">(.+?)</div>(.+?)</div></div></div>' , re . DOTALL ) . findall ( iI1I )
  for oOOOo00O00oOo , oO0oo0o in ii111IiiI1 :
   ii11i1iIiII1 = re . compile ( '<a qt-title="(.+?)"(.+?)onmouse' , re . DOTALL ) . findall ( str ( oO0oo0o . encode ( 'utf-8' ) ) )
   for o00oo0 , oooooOOO000Oo in ii11i1iIiII1 :
    Ooo00OoOOO = re . compile ( '(.+?)-(.+?) ' ) . findall ( str ( o00oo0 ) )
    for Oo0OO0000oooo , IIII1iII in Ooo00OoOOO :
     if 'am' in Oo0OO0000oooo :
      ii1III11 = re . compile ( '(.+?):(.+?)am' ) . findall ( str ( Oo0OO0000oooo ) )
      for I1iiIIIi11 , Ii1I11ii1i in ii1III11 :
       O0iIiIIIIIii = ( int ( I1iiIIIi11 ) * 60 ) + int ( Ii1I11ii1i )
     elif 'pm' in Oo0OO0000oooo :
      ii1III11 = re . compile ( '(.+?):(.+?)pm' ) . findall ( str ( Oo0OO0000oooo ) )
      for I1iiIIIi11 , Ii1I11ii1i in ii1III11 :
       if I1iiIIIi11 == '12' :
        O0iIiIIIIIii = ( int ( I1iiIIIi11 ) * 60 ) + int ( Ii1I11ii1i )
       else :
        O0iIiIIIIIii = ( int ( I1iiIIIi11 ) + 12 ) * 60 + int ( Ii1I11ii1i )
     if 'am' in IIII1iII :
      ii1III11 = re . compile ( '(.+?):(.+?)am' ) . findall ( str ( IIII1iII ) )
      for I1iiIIIi11 , Ii1I11ii1i in ii1III11 :
       OOo0ii11I1 = ( int ( I1iiIIIi11 ) * 60 ) + int ( Ii1I11ii1i )
     elif 'pm' in IIII1iII :
      ii1III11 = re . compile ( '(.+?):(.+?)pm' ) . findall ( str ( IIII1iII ) )
      for I1iiIIIi11 , Ii1I11ii1i in ii1III11 :
       if I1iiIIIi11 == '12' :
        OOo0ii11I1 = ( int ( I1iiIIIi11 ) * 60 ) + int ( Ii1I11ii1i )
       else :
        OOo0ii11I1 = ( int ( I1iiIIIi11 ) + 12 ) * 60 + int ( Ii1I11ii1i )
     if int ( O0iIiIIIIIii ) < int ( iI ) < int ( OOo0ii11I1 ) :
      if not extra or extra == '' :
       oO0oo = oOOOo00O00oOo . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       OOoo0O0 ( oO0oo . encode ( 'utf-8' ) + ': ' + o00oo0 . encode ( 'utf-8' ) , '' , 7 , '' , '' , '' , oO0oo . replace ( 'HD' , '' ) )
      elif extra == 'SEARCH_SPLIT' :
       oO0oo = oOOOo00O00oOo . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       if name . lower ( ) . replace ( ' ' , '' ) in o00oo0 . lower ( ) . replace ( ' ' , '' ) . encode ( 'utf-8' ) :
        OOoo0O0 ( oO0oo . encode ( 'utf-8' ) + ': ' + o00oo0 . encode ( 'utf-8' ) , '' , 7 , '' , '' , '' , oO0oo . replace ( 'HD' , '' ) )
      else :
       oO0oo = oOOOo00O00oOo . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       Ii111iIi1iIi = extra . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       if Ii111iIi1iIi == oO0oo :
        OOoo0O0 ( oO0oo . encode ( 'utf-8' ) + ': ' + o00oo0 . encode ( 'utf-8' ) , '' , 7 , '' , '' , '' , oO0oo . replace ( 'HD' , '' ) )
       else :
        pass
 except :
  pass
  if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
def OoOo ( extra ) :
 O0i1II1Iiii1I11 ( extra . lower ( ) . replace ( 'hd' , '' ) . replace ( ' ' , '' ) . replace ( 'christmasgold' , 'gold' ) )
 if 35 - 35: ooOoO0o * OOooOOo . I11i * o0oOOo0O0Ooo . OoOoOO00 / O0
def I11i1I1I ( url ) :
 IIiI1Ii = urllib2 . Request ( url )
 IIiI1Ii . add_header ( 'User-Agent' ,
 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i11I1I1I = ''
 Ooo0oOooo0 = ''
 try :
  i11I1I1I = urllib2 . urlopen ( IIiI1Ii )
  Ooo0oOooo0 = i11I1I1I . read ( )
  i11I1I1I . close ( )
 except :
  pass
 if Ooo0oOooo0 != '' :
  return Ooo0oOooo0
 else :
  Ooo0oOooo0 = 'Opened'
  return Ooo0oOooo0
  if 100 - 100: I1Ii111 . o0oOOo0O0Ooo * Oo0Ooo % O0 * O0
def iIo0O ( name , url ) :
 import urlresolver
 try :
  IIIii1 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( IIIii1 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
 if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
def OOoo0O0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 if iconimage == '' :
  iconimage = iiiI11
 elif iconimage == ' ' :
  iconimage = iiiI11
 if fanart == '' :
  fanart = OOooO
 elif fanart == ' ' :
  fanart = OOooO
 OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 i11III1111iIi = True
 I1i111I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i111I . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1i111I . setProperty ( "Fanart_Image" , fanart )
 i11III1111iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOo , listitem = I1i111I , isFolder = True )
 return i11III1111iIi
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
 if 100 - 100: OoO0O00
def o0OoOO000ooO0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 if iconimage == '' :
  iconimage = iiiI11
 elif iconimage == ' ' :
  iconimage = iiiI11
 if fanart == '' :
  fanart = OOooO
 elif fanart == ' ' :
  fanart = OOooO
 OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 i11III1111iIi = True
 I1i111I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i111I . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1i111I . setProperty ( "Fanart_Image" , fanart )
 i11III1111iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOo , listitem = I1i111I , isFolder = False )
 return i11III1111iIi
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
def IIi1ii1Ii ( ) :
 OoOoOo0 = [ ]
 ii1i = sys . argv [ 2 ]
 if len ( ii1i ) >= 2 :
  oOOoo = sys . argv [ 2 ]
  iII1111III1I = oOOoo . replace ( '?' , '' )
  if ( oOOoo [ len ( oOOoo ) - 1 ] == '/' ) :
   oOOoo = oOOoo [ 0 : len ( oOOoo ) - 2 ]
  ii11i = iII1111III1I . split ( '&' )
  OoOoOo0 = { }
  for O00oOo00o0o in range ( len ( ii11i ) ) :
   O00oO0 = { }
   O00oO0 = ii11i [ O00oOo00o0o ] . split ( '=' )
   if ( len ( O00oO0 ) ) == 2 :
    OoOoOo0 [ O00oO0 [ 0 ] ] = O00oO0 [ 1 ]
    if 70 - 70: I11i . I1ii11iIi11i * OoooooooOO - IiII * I1IiiI + OoOoOO00
 return OoOoOo0
 if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
oOOoo = IIi1ii1Ii ( )
Iii111II = None
oOOoo0Oo = None
o00 = None
i1I1i111Ii = None
oO = None
O00O0Ooooo00 = None
Ooo = None
O000 = None
ooo0o000O = None
OOOO0o = None
if 75 - 75: OoooooooOO * IiII
try :
 ooo0o000O = oOOoo [ "regexs" ]
except :
 pass
 if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
try :
 O000 = int ( oOOoo [ "fav_mode" ] )
except :
 pass
try :
 O00O0Ooooo00 = urllib . unquote_plus ( oOOoo [ "extra" ] )
except :
 pass
try :
 Iii111II = urllib . unquote_plus ( oOOoo [ "url" ] )
except :
 pass
try :
 oOOoo0Oo = urllib . unquote_plus ( oOOoo [ "name" ] )
except :
 pass
try :
 o00 = urllib . unquote_plus ( oOOoo [ "iconimage" ] )
except :
 pass
try :
 i1I1i111Ii = int ( oOOoo [ "mode" ] )
except :
 pass
try :
 Ooo = urllib . unquote_plus ( oOOoo [ "fanart" ] )
except :
 pass
try :
 oO = urllib . unquote_plus ( oOOoo [ "description" ] )
except :
 pass
try :
 I1IIIiI1I1ii1 = urllib . unquote_plus ( oOOoo [ "playitem" ] )
except :
 pass
try :
 OOOO0o = eval ( urllib . unquote_plus ( oOOoo [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 ooo0o000O = oOOoo [ "regexs" ]
except :
 pass
 if 30 - 30: O0 * OoooooooOO
if i1I1i111Ii == None : ii1I1i1I ( )
elif i1I1i111Ii == 1 : o00oOO0 ( )
elif i1I1i111Ii == 2 : i11i1 ( )
elif i1I1i111Ii == 3 : I111I1Iiii1i ( )
elif i1I1i111Ii == 4 : OO0ooOOO0OOO ( )
elif i1I1i111Ii == 5 : IiIiII1 ( )
elif i1I1i111Ii == 6 : I1ii1 ( Iii111II )
elif i1I1i111Ii == 7 : OoOo ( O00O0Ooooo00 )
elif i1I1i111Ii == 8 : i1iIi1I1i ( Iii111II )
elif i1I1i111Ii == 9 : iIIIII1ii1I ( oOOoo0Oo , Iii111II )
elif i1I1i111Ii == 10 : iIo0O ( oOOoo0Oo , Iii111II )
elif i1I1i111Ii == 11 : iiii11I ( oOOoo0Oo , Iii111II , O00O0Ooooo00 )
elif i1I1i111Ii == 12 : oooooo0O000o ( Iii111II )
elif i1I1i111Ii == 13 : i1I1iI ( )
elif i1I1i111Ii == 14 : o00oooO0Oo ( )
elif i1I1i111Ii == 15 : O0OO0O ( Iii111II , o00 )
elif i1I1i111Ii == 16 : IIi1i ( Iii111II )
elif i1I1i111Ii == 17 : OoOO ( oOOoo0Oo )
elif i1I1i111Ii == 18 : i1Ii ( Iii111II )
elif i1I1i111Ii == 19 : I1iI1iIi111i ( Iii111II )
elif i1I1i111Ii == 20 : iiIIiiIi1Ii11 ( oOOoo0Oo , Iii111II )
elif i1I1i111Ii == 21 : o0O ( Iii111II , o00 )
elif i1I1i111Ii == 22 : o00oO0oo0OO ( Iii111II , o00 )
elif i1I1i111Ii == 23 : IIOOOO0oo0 ( Iii111II )
elif i1I1i111Ii == 24 : oOOOO00O0O0 ( )
elif i1I1i111Ii == 25 : iii1i1iiiiIi ( Iii111II )
elif i1I1i111Ii == 26 : o0oOIIiIi1iI ( Iii111II )
elif i1I1i111Ii == 27 : Mama_hd ( )
elif i1I1i111Ii == 28 : ii1i1I1i ( )
elif i1I1i111Ii == 29 : i1 ( )
elif i1I1i111Ii == 30 : Ii11Ii1I ( )
elif i1I1i111Ii == 31 : OO00Oo ( Iii111II )
elif i1I1i111Ii == 1201 : OOo0o0O0O ( Iii111II )
elif i1I1i111Ii == 1202 : o000ooooO0o ( oOOoo0Oo , Iii111II )
if 38 - 38: IiII - I1ii11iIi11i . OoOoOO00 - I1Ii111 . OoooooooOO
if 89 - 89: iIii1I11I1II1
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
