# -*- coding: utf-8 -*-
'''
    Template Add-on
    Copyright (C) 2016 Origin

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
	
    However if you have come to meerly use my code that i've wrote to 
    get a hardon with you're little fan boys then dont expect me to be pleased
    or thank you for rubbing it in my faces. This code is obfuscated because 
    i choose what happens to my code, whatever source you believe your code to 
    be on the system you use it on is your decision, what i write is what i call
    my code and ill do what the hell i want, i wont be dicatated to....
'''

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
if 23 - 23: i11iIiiIii + I1IiiI
oOo = datetime . now ( ) . strftime ( '%Y' )
oOoOoO = datetime . now ( ) . strftime ( '%m' )
ii1I = datetime . now ( ) . strftime ( '%d' )
OooO0 = datetime . now ( ) . strftime ( '%H' )
II11iiii1Ii = datetime . now ( ) . strftime ( '%M' )
OO0o = str ( ( int ( OooO0 ) * 60 ) + int ( II11iiii1Ii ) )
if 82 - 82: i11iIiiIii . OOooOOo / Oo0Ooo * O0 % oO0o % iIii1I11I1II1
if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iII111i + iII111i
def I11I11i1I ( ) :
 for ii11i1iIII , Ii1IOo0o0 , file in os . walk ( O0OoO000O0OO ) :
  for dir in Ii1IOo0o0 :
   if 'anonymous' in dir . lower ( ) :
    if iIii1 . getSetting ( 'Delete' ) == 'true' :
     III1ii1iII ( dir )
    else :
     oOOoO0 . ok ( 'Something has to go' , 'A addon has been found that is leeching content' , 'your next choice is up to you' , 'if you cancel vendetta will be removed' )
     oo0oooooO0 = [ 'Remove ' + dir , 'Remove vendetta' , 'Remove both' ]
     i11Iiii = xbmcgui . Dialog ( ) . select ( 'What is going to be removed?' , oo0oooooO0 )
     if i11Iiii == 0 :
      III1ii1iII ( dir )
     elif i11Iiii == 1 :
      III1ii1iII ( 'plugin.video.vendetta' )
     elif i11Iiii == 2 :
      III1ii1iII ( dir )
      III1ii1iII ( 'plugin.video.vendetta' )
     else :
      III1ii1iII ( 'plugin.video.vendetta' )
      if 23 - 23: o0oOOo0O0Ooo . II111iiii
def III1ii1iII ( dir ) :
 Oo0O0OOOoo = O0OoO000O0OO + dir
 shutil . rmtree ( Oo0O0OOOoo )
 if 95 - 95: OoO0O00 % oO0o . O0
def I1i1I ( ) :
 I11I11i1I ( )
 oOO00oOO ( 'Search' , '' , 1 , '' , '' , '' , '' )
 oOO00oOO ( 'UK ONLY - Whats on now' , '' , 2 , '' , '' , '' , '' )
 oOO00oOO ( 'Lists' , '' , 3 , '' , '' , '' , '' )
 oOO00oOO ( 'By Country' , '' , 4 , '' , '' , '' , '' )
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
 OooOooo = { "User-Agent" : "Mozilla/5.0" }
 O000oo0O = requests . get ( 'http://www.iptvultra.com/' , headers = OooOooo ) . text
 OOOO = re . compile ( '<span class="link"><a href="(.+?)">(.+?)</a>' ) . findall ( O000oo0O )
 for i11i1 , IIIii1II1II in OOOO :
  oOO00oOO ( IIIii1II1II , i11i1 , 12 , '' , '' , '' , '' )
  if 42 - 42: Ii1I + oO0o
def o0O0o0Oo ( url ) :
 OooOooo = { "User-Agent" : "Mozilla/5.0" }
 O000oo0O = requests . get ( url , headers = OooOooo ) . text
 OOOO = re . compile ( '".+?[@](.+?)[@].+?[@].+?[@](.+?)"' ) . findall ( O000oo0O )
 for IIIii1II1II , Ii11Ii1I in OOOO :
  IIIii1II1II = IIIii1II1II . replace ( '[' , '' ) . replace ( ']' , '' )
  if IIIii1II1II [ 0 ] == ' ' :
   IIIii1II1II = IIIii1II1II [ 1 : ]
  if IIIii1II1II [ - 1 ] == ' ' :
   IIIii1II1II = IIIii1II1II [ : - 1 ]
  O00oO = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + Ii11Ii1I . replace ( '[' , '' ) . replace ( ']' , '' ) + ';name=vendetta'
  I11i1I1I ( IIIii1II1II , O00oO , 10 , '' , '' , '' , '' )
  if 83 - 83: I1ii11iIi11i / ooOoO0o
def iIIIIii1 ( ) :
 O000oo0O = requests . get ( 'http://www.shadow-net.org' ) . text
 OOOO = re . compile ( '<li class=""><a href="(.+?)">(.+?)</a>' ) . findall ( O000oo0O )
 for i11i1 , IIIii1II1II in OOOO :
  IIIii1II1II = IIIii1II1II . replace ( '&amp;' , '&' )
  if 'p2p' in IIIii1II1II . lower ( ) :
   pass
  else :
   oOO00oOO ( IIIii1II1II , i11i1 , 8 , '' , '' , '' , '' )
   if 58 - 58: i11iIiiIii % I11i
   if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
   if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
   if 16 - 16: I1IiiI * oO0o % IiII
def Oo000o ( ) :
 I11IiI1I11i1i = oOOoO0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI1ii1Ii = I11IiI1I11i1i . lower ( )
 oooo000 ( iI1ii1Ii )
 if 16 - 16: I1ii11iIi11i + OoO0O00 - II111iiii
def oooo000 ( name ) :
 iI1ii1Ii = name
 OooOooo = { "User-Agent" : "Mozilla/5.0" }
 oOoOO0 = [ ]
 IiI11iII1 = [ ]
 IIII11I1I = [ ]
 OOO0o = xbmcgui . DialogProgress ( )
 O000oo0O = requests . get ( 'http://www.iptvultra.com/' , headers = OooOooo ) . text
 OOOO = re . compile ( '<span class="link"><a href="(.+?)">(.+?)</a>' ) . findall ( O000oo0O )
 for i11i1 , name in OOOO :
  IiI11iII1 . append ( i11i1 [ 0 ] )
  IiI1 = len ( IiI11iII1 )
 for i11i1 , name in OOOO :
  oOoOO0 . append ( i11i1 [ 0 ] )
  Oo0O00Oo0o0 = len ( oOoOO0 ) / float ( IiI1 ) * 100
  OOO0o . create ( 'Checking for stream' )
  OOO0o . update ( int ( Oo0O00Oo0o0 ) , 'Checking list ' + str ( len ( oOoOO0 ) ) + '/' + str ( len ( OOOO ) ) , str ( len ( IIII11I1I ) ) + ' Results' )
  if OOO0o . iscanceled ( ) :
   return
  O00O0oOO00O00 = requests . get ( i11i1 , headers = OooOooo ) . text
  i1 = re . compile ( '".+?[@](.+?)[@].+?[@].+?[@](.+?)"' ) . findall ( O00O0oOO00O00 )
  for name , Ii11Ii1I in i1 :
   name = name . replace ( '[' , '' ) . replace ( ']' , '' )
   if name [ 0 ] == ' ' :
    name = name [ 1 : ]
   if name [ - 1 ] == ' ' :
    name = name [ : - 1 ]
   Oo00 = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=' + Ii11Ii1I . replace ( '[' , '' ) . replace ( ']' , '' ) + ';name=vendetta'
   if ( iI1ii1Ii ) . replace ( ' ' , '' ) in ( name ) . replace ( ' ' , '' ) . lower ( ) :
    IIII11I1I . append ( i11i1 [ 0 ] )
    I11i1I1I ( name , Oo00 , 10 , '' , '' , '' , '' )
    if 31 - 31: I1Ii111 . OoOoOO00 / O0
def o000O0o ( ) :
 oo0oooooO0 = [ 'Select by Virgin No.' , 'Select by Sky No.' , 'Select by Freeview No.' ]
 i11Iiii = xbmcgui . Dialog ( ) . select ( 'Search by channel number' , oo0oooooO0 )
 if i11Iiii == 0 :
  iI1iII1 (
 'http://www.tvguide.co.uk/?catcolor=&systemid=25&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ,
 'Virgin' )
 if i11Iiii == 1 :
  iI1iII1 (
 'http://www.tvguide.co.uk/?catcolor=&systemid=5&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ,
 'Sky' )
 if i11Iiii == 2 :
  iI1iII1 (
 'http://www.tvguide.co.uk/?catcolor=&systemid=3&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ,
 'Freeview' )
  if 86 - 86: OOooOOo
  if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
def iI1iII1 ( url , name ) :
 ii1ii1ii = xbmcgui . Dialog ( ) . input ( "Channel No" , type = xbmcgui . INPUT_NUMERIC )
 oooooOoo0ooo = requests . get ( url ) . text
 OOOO = re . compile ( 'qt-text="(.+?)" title="(.+?)"' ) . findall ( oooooOoo0ooo )
 for I1I1IiI1 , III1iII1I1ii in OOOO :
  III1iII1I1ii = III1iII1I1ii . replace ( ' TV listings' , '' )
  I1I1IiI1 = I1I1IiI1 . replace ( 'Channel Numbers<br> ' , '' )
  if ':' in I1I1IiI1 :
   if name == 'Sky' :
    oOOo0 = re . compile ( 'Sky:(.+?) ' ) . findall ( str ( I1I1IiI1 ) )
    for IiI11iII1 in oOOo0 :
     if ii1ii1ii in oOOo0 :
      oo00O00oO ( url , str ( III1iII1I1ii ) )
   elif name == 'Virgin' :
    iIiIIIi = re . compile ( 'Virgin:(.+?) ' ) . findall ( str ( I1I1IiI1 ) )
    for IiI11iII1 in iIiIIIi :
     if ii1ii1ii in iIiIIIi :
      oo00O00oO ( url , str ( III1iII1I1ii ) )
   elif name == 'Freeview' :
    ooo00OOOooO = re . compile ( 'Freeview:(.+?) ' ) . findall ( str ( I1I1IiI1 ) )
    for IiI11iII1 in ooo00OOOooO :
     if ii1ii1ii in ooo00OOOooO :
      oo00O00oO ( url , str ( III1iII1I1ii ) )
      if 67 - 67: I11i * oO0o * I1ii11iIi11i + OOooOOo / i1IIi
def I1I111 ( url ) :
 Oo00oo0oO = [ [ 'All' , 'http://www.tvguide.co.uk/?catcolor=&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Comedy' , 'http://www.tvguide.co.uk/?catcolor=3253CF&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Sports' , 'http://www.tvguide.co.uk/?catcolor=53CE32&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Music' , 'http://www.tvguide.co.uk/?catcolor=FF9933&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Film' , 'http://www.tvguide.co.uk/?catcolor=000000&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Soap' , 'http://www.tvguide.co.uk/?catcolor=AB337D&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Kids' , 'http://www.tvguide.co.uk/?catcolor=E3BB00&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Drama' , 'http://www.tvguide.co.uk/?catcolor=CE3D32&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Talk show' , 'http://www.tvguide.co.uk/?catcolor=800000&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Game show' , 'http://www.tvguide.co.uk/?catcolor=669999&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Sci-fi' , 'http://www.tvguide.co.uk/?catcolor=666699&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Documentary' , 'http://www.tvguide.co.uk/?catcolor=CCCCCC&systemid=' + url + '&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Motor' , 'http://www.tvguide.co.uk/?catcolor=996633&systemid=7&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ,
 [ 'Horror' , 'http://www.tvguide.co.uk/?catcolor=666633&systemid=7&thistime=' + OooO0 + '&thisDay=' + oOoOoO + '/' + ii1I + '/' + oOo + '&gridspan=03:00&view=0&gw=1323' ] ]
 for IiI11iII1 in Oo00oo0oO :
  IIIii1II1II = IiI11iII1 [ 0 ]
  IIiIi1iI = IiI11iII1 [ 1 ]
  oOO00oOO ( IIIii1II1II , IIiIi1iI , 11 , '' , '' , '' , '' )
  if 35 - 35: Ii1I % O0 - O0
def IiIIIi1iIi ( url ) :
 Oo00oo0oO = [ ]
 O000oo0O = requests . get ( url ) . text
 ooOOoooooo = re . compile ( '<div class="Block CategoryContent Moveable Panel"(.+?)<br class="Clear" />' , re . DOTALL ) . findall ( O000oo0O )
 for IiI11iII1 in ooOOoooooo :
  OOOO = re . compile ( '<div class="ProductImage">.+?<a href="(.+?)".+?img src="(.+?)" alt="(.+?)" />' , re . DOTALL ) . findall ( str ( IiI11iII1 . encode ( 'utf-8' ) ) )
  for url , II1I , IIIii1II1II in OOOO :
   I11i1I1I ( IIIii1II1II , url , 9 , II1I , '' , '' , '' )
 next = re . compile ( '<div class="FloatRight"><a href="(.+?)">.+?</a>' ) . findall ( O000oo0O )
 for url in next :
  if 'skippy' not in Oo00oo0oO :
   oOO00oOO ( 'Next Page' , url , 8 , '' , '' , '' , '' )
   Oo00oo0oO . append ( 'skippy' )
   if 84 - 84: IiII . i11iIiiIii . IiII * I1ii11iIi11i - I11i
def ii ( name , url ) :
 Oo00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
 O000oo0O = requests . get ( url ) . text
 O0o0oOOOoOo = re . compile ( '<source src="(.+?)"' ) . findall ( O000oo0O )
 for IiI11iII1 in O0o0oOOOoOo :
  Oo00 = IiI11iII1
 II1 ( name , Oo00 )
 if 35 - 35: iII111i % iIii1I11I1II1 / oO0o / OOooOOo % OoooooooOO
 if 78 - 78: Ii1I % I1Ii111 + I1ii11iIi11i
def oo00O00oO ( url , extra ) :
 try :
  oooooOoo0ooo = requests . get ( url ) . text
  OOooOoooOoOo = re . compile ( '<div class="div-epg-channel-progs">.+?<div class="div-epg-channel-name">(.+?)</div>(.+?)</div></div></div>' , re . DOTALL ) . findall ( oooooOoo0ooo )
  for o0OOOO00O0Oo , ooOOoooooo in OOooOoooOoOo :
   iioOooOOOoOo = re . compile ( '<a qt-title="(.+?)"(.+?)onmouse' , re . DOTALL ) . findall ( str ( ooOOoooooo . encode ( 'utf-8' ) ) )
   for i1Iii1i1I , OOoO00 in iioOooOOOoOo :
    IiI111111IIII = re . compile ( '(.+?)-(.+?) ' ) . findall ( str ( i1Iii1i1I ) )
    for i1Ii , ii111iI1iIi1 in IiI111111IIII :
     if 'am' in i1Ii :
      OOO = re . compile ( '(.+?):(.+?)am' ) . findall ( str ( i1Ii ) )
      for oo0OOo0 , I11IiI in OOO :
       O0ooO0Oo00o = ( int ( oo0OOo0 ) * 60 ) + int ( I11IiI )
     elif 'pm' in i1Ii :
      OOO = re . compile ( '(.+?):(.+?)pm' ) . findall ( str ( i1Ii ) )
      for oo0OOo0 , I11IiI in OOO :
       if oo0OOo0 == '12' :
        O0ooO0Oo00o = ( int ( oo0OOo0 ) * 60 ) + int ( I11IiI )
       else :
        O0ooO0Oo00o = ( int ( oo0OOo0 ) + 12 ) * 60 + int ( I11IiI )
     if 'am' in ii111iI1iIi1 :
      OOO = re . compile ( '(.+?):(.+?)am' ) . findall ( str ( ii111iI1iIi1 ) )
      for oo0OOo0 , I11IiI in OOO :
       ooO0oOOooOo0 = ( int ( oo0OOo0 ) * 60 ) + int ( I11IiI )
     elif 'pm' in ii111iI1iIi1 :
      OOO = re . compile ( '(.+?):(.+?)pm' ) . findall ( str ( ii111iI1iIi1 ) )
      for oo0OOo0 , I11IiI in OOO :
       if oo0OOo0 == '12' :
        ooO0oOOooOo0 = ( int ( oo0OOo0 ) * 60 ) + int ( I11IiI )
       else :
        ooO0oOOooOo0 = ( int ( oo0OOo0 ) + 12 ) * 60 + int ( I11IiI )
     if int ( O0ooO0Oo00o ) < int ( OO0o ) < int ( ooO0oOOooOo0 ) :
      if not extra or extra == '' :
       i1I1ii11i1Iii = o0OOOO00O0Oo . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       oOO00oOO ( i1I1ii11i1Iii . encode ( 'utf-8' ) + ': ' + i1Iii1i1I . encode ( 'utf-8' ) , '' , 7 , '' , '' , '' , i1I1ii11i1Iii . replace ( 'HD' , '' ) )
      else :
       i1I1ii11i1Iii = o0OOOO00O0Oo . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       I1IiiiiI = extra . replace ( 'BBC1 London' , 'BBC1' ) . replace ( 'BBC2 London' , 'BBC2' ) . replace ( 'ITV London' , 'ITV1' )
       if I1IiiiiI == i1I1ii11i1Iii :
        oOO00oOO ( i1I1ii11i1Iii . encode ( 'utf-8' ) + ': ' + i1Iii1i1I . encode ( 'utf-8' ) , '' , 7 , '' , '' , '' , i1I1ii11i1Iii . replace ( 'HD' , '' ) )
       else :
        pass
 except :
  pass
  if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
def iIiIIi1 ( extra ) :
 oooo000 ( extra . lower ( ) . replace ( 'hd' , '' ) . replace ( ' ' , '' ) . replace ( 'christmasgold' , 'gold' ) )
 if 7 - 7: ooOoO0o - Oo0Ooo - oO0o + ooOoO0o
def iI1I11iiI1i ( url ) :
 oO0o0Ooooo = urllib2 . Request ( url )
 oO0o0Ooooo . add_header ( 'User-Agent' ,
 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOo0oO00ooO00 = ''
 oOO0O00oO0Ooo = ''
 try :
  OOo0oO00ooO00 = urllib2 . urlopen ( oO0o0Ooooo )
  oOO0O00oO0Ooo = OOo0oO00ooO00 . read ( )
  OOo0oO00ooO00 . close ( )
 except :
  pass
 if oOO0O00oO0Ooo != '' :
  return oOO0O00oO0Ooo
 else :
  oOO0O00oO0Ooo = 'Opened'
  return oOO0O00oO0Ooo
  if 67 - 67: OoO0O00 - OOooOOo
def II1 ( name , url ) :
 import urlresolver
 try :
  iI1i11iII111 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iI1i11iII111 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 15 - 15: i11iIiiIii % Ii1I . Oo0Ooo + I1ii11iIi11i
def oOO00oOO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 if iconimage == '' :
  iconimage = ii11iIi1I
 elif iconimage == ' ' :
  iconimage = ii11iIi1I
 if fanart == '' :
  fanart = iI111I11I1I1
 elif fanart == ' ' :
  fanart = iI111I11I1I1
 OO0OOOOoo0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 i1i1Ii1 = True
 Ii11iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii11iIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii11iIi . setProperty ( "Fanart_Image" , fanart )
 i1i1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0OOOOoo0OOO , listitem = Ii11iIi , isFolder = True )
 return i1i1Ii1
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 55 - 55: I11i * oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
def I11i1I1I ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 if iconimage == '' :
  iconimage = ii11iIi1I
 elif iconimage == ' ' :
  iconimage = ii11iIi1I
 if fanart == '' :
  fanart = iI111I11I1I1
 elif fanart == ' ' :
  fanart = iI111I11I1I1
 OO0OOOOoo0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 i1i1Ii1 = True
 Ii11iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii11iIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii11iIi . setProperty ( "Fanart_Image" , fanart )
 i1i1Ii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0OOOOoo0OOO , listitem = Ii11iIi , isFolder = False )
 return i1i1Ii1
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
def Oo0O0oooo ( ) :
 I111iI = [ ]
 oOOo0II1I1iiIII = sys . argv [ 2 ]
 if len ( oOOo0II1I1iiIII ) >= 2 :
  oOOo0O00o = sys . argv [ 2 ]
  iIiIi11 = oOOo0O00o . replace ( '?' , '' )
  if ( oOOo0O00o [ len ( oOOo0O00o ) - 1 ] == '/' ) :
   oOOo0O00o = oOOo0O00o [ 0 : len ( oOOo0O00o ) - 2 ]
  OOOiiiiI = iIiIi11 . split ( '&' )
  I111iI = { }
  for oooOo0OOOoo0 in range ( len ( OOOiiiiI ) ) :
   OOoO = { }
   OOoO = OOOiiiiI [ oooOo0OOOoo0 ] . split ( '=' )
   if ( len ( OOoO ) ) == 2 :
    I111iI [ OOoO [ 0 ] ] = OOoO [ 1 ]
    if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
 return I111iI
 if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
oOOo0O00o = Oo0O0oooo ( )
i11i1 = None
IIIii1II1II = None
o0o0O0O00oOOo = None
iIIIiIi = None
OO0O0 = None
I11I11 = None
o000O0O = None
I1i1i1iii = None
I1111i = None
iIIii = None
if 92 - 92: Ii1I + oO0o % OOooOOo
try :
 I1111i = oOOo0O00o [ "regexs" ]
except :
 pass
 if 62 - 62: I1ii11iIi11i / i1IIi
try :
 I1i1i1iii = int ( oOOo0O00o [ "fav_mode" ] )
except :
 pass
try :
 I11I11 = urllib . unquote_plus ( oOOo0O00o [ "extra" ] )
except :
 pass
try :
 i11i1 = urllib . unquote_plus ( oOOo0O00o [ "url" ] )
except :
 pass
try :
 IIIii1II1II = urllib . unquote_plus ( oOOo0O00o [ "name" ] )
except :
 pass
try :
 o0o0O0O00oOOo = urllib . unquote_plus ( oOOo0O00o [ "iconimage" ] )
except :
 pass
try :
 iIIIiIi = int ( oOOo0O00o [ "mode" ] )
except :
 pass
try :
 o000O0O = urllib . unquote_plus ( oOOo0O00o [ "fanart" ] )
except :
 pass
try :
 OO0O0 = urllib . unquote_plus ( oOOo0O00o [ "description" ] )
except :
 pass
try :
 oo0oO = urllib . unquote_plus ( oOOo0O00o [ "playitem" ] )
except :
 pass
try :
 iIIii = eval ( urllib . unquote_plus ( oOOo0O00o [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 I1111i = oOOo0O00o [ "regexs" ]
except :
 pass
 if 94 - 94: iIii1I11I1II1 / Oo0Ooo % iII111i * iII111i * II111iiii
if iIIIiIi == None : I1i1I ( )
elif iIIIiIi == 1 : Oo000o ( )
elif iIIIiIi == 2 : O000OO0 ( )
elif iIIIiIi == 3 : o00 ( )
elif iIIIiIi == 4 : iIIIIii1 ( )
elif iIIIiIi == 5 : o000O0o ( )
elif iIIIiIi == 6 : I1I111 ( i11i1 )
elif iIIIiIi == 7 : iIiIIi1 ( I11I11 )
elif iIIIiIi == 8 : IiIIIi1iIi ( i11i1 )
elif iIIIiIi == 9 : ii ( IIIii1II1II , i11i1 )
elif iIIIiIi == 10 : II1 ( IIIii1II1II , i11i1 )
elif iIIIiIi == 11 : oo00O00oO ( i11i1 , I11I11 )
elif iIIIiIi == 12 : o0O0o0Oo ( i11i1 )
if 29 - 29: OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / OOooOOo * iIii1I11I1II1
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
