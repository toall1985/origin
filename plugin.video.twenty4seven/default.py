# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
import requests , xbmcgui , xbmcplugin , xbmc , re , sys , os , xbmcaddon , json , urllib
from threading import Thread
from lib . jsunpack import unpack as packets
from lib . common import random_agent
from BeautifulSoup import BeautifulSoup
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = xbmc . translatePath ( 'special://home/addons/plugin.video.twenty4seven/' )
oo = o0OO00 + 'icon.png'
i1iII1IiiIiI1 = o0OO00 + 'fanart.jpg'
iIiiiI1IiI1I1 = xbmc . translatePath ( 'special://home/userdata/addon_data' )
o0OoOoOO00 = iIiiiI1IiI1I1 + '/plugin.video.twenty4seven/'
I11i = o0OoOoOO00 + 'favourites.txt'
if not os . path . exists ( o0OoOoOO00 ) :
 os . makedirs ( o0OoOoOO00 )
if os . path . exists ( I11i ) == True :
 O0O = open ( I11i ) . read ( )
else :
 O0O = [ ]
 if 78 - 78: i11ii11iIi11i . oOoO0oo0OOOo + IiiI / Iii1ii1II11i
def iI111iI ( ) :
 IiII ( '[COLORorangered]24/7 Tv Shows[/COLOR]' , '' , 1 , oo , i1iII1IiiIiI1 , '' , '' )
 IiII ( '[COLORorangered]24/7 Movies[/COLOR]' , '' , 2 , oo , i1iII1IiiIiI1 , '' , '' )
 IiII ( '[COLORorangered]24/7 Cable[/COLOR]' , '' , 4 , oo , i1iII1IiiIiI1 , '' , '' )
 IiII ( '[COLORorangered]24/7 Random Stream[/COLOR]' , '' , 3 , oo , i1iII1IiiIiI1 , '' , '' )
 if os . path . exists ( I11i ) == True :
  IiII ( '[COLORorangered]24/7 Favs[/COLOR]' , '' , 10 , oo , i1iII1IiiIiI1 , '' , '' )
 iI1Ii11111iIi = 'http://arconaitv.me/'
 i1i1II = 'index.php#shows'
 if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
 o0oOoO00o = BeautifulSoup ( requests . get ( iI1Ii11111iIi + i1i1II ) . content )
 i1 = o0oOoO00o . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for oOOoo00O0O in i1 :
  i1111 = oOOoo00O0O . findAll ( 'a' )
  for i11 in i1111 :
   if i11 . has_key ( 'href' ) :
    I11 = iI1Ii11111iIi + i11 [ 'href' ]
   if i11 . has_key ( 'title' ) :
    Oo0o0000o0o0 = i11 [ 'title' ]
   oOo0oooo00o = i11 . findAll ( 'img' )
   for oO0o0o0ooO0oO in oOo0oooo00o :
    oo0o0O00 = iI1Ii11111iIi + oO0o0o0ooO0oO [ 'src' ]
    oO = { 'User-Agent' : random_agent ( ) }
    i1iiIIiiI111 = requests . get ( I11 , headers = oO ) . content
    oooOOOOO = packets ( i1iiIIiiI111 )
    if 22 - 22: oOO * OooooO0oOO + IiIi11i
    iIii1I111I11I = re . compile ( "'https:(.+?)'" ) . findall ( oooOOOOO )
    for OO00OooO0OO in iIii1I111I11I :
     OO00OooO0OO = OO00OooO0OO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
     iiiIi = 'https:' + OO00OooO0OO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     IiIIIiI1I1 ( Oo0o0000o0o0 , iiiIi , 20 , oo0o0O00 , oo0o0O00 , '' , '' )
     if 86 - 86: i11I1IIiiIi + oOo + i11iIiiIii - I1i1iI1i + i11iIiiIii
def ooOoo0O ( ) :
 iI1Ii11111iIi = 'http://arconaitv.me/'
 i1i1II = 'index.php#shows'
 o0oOoO00o = BeautifulSoup ( requests . get ( iI1Ii11111iIi + i1i1II ) . content )
 i1 = o0oOoO00o . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for oOOoo00O0O in i1 :
  i1111 = oOOoo00O0O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for i11 in i1111 :
   OooO0 = i11 . text
  II11iiii1Ii = oOOoo00O0O . findAll ( 'a' )
  for i11 in II11iiii1Ii :
   if i11 . has_key ( 'href' ) :
    I11 = iI1Ii11111iIi + i11 [ 'href' ]
   if i11 . has_key ( 'title' ) :
    Oo0o0000o0o0 = i11 [ 'title' ]
   oO = { 'User-Agent' : random_agent ( ) }
   i1iiIIiiI111 = requests . get ( I11 , headers = oO ) . content
   oooOOOOO = packets ( i1iiIIiiI111 )
   if 70 - 70: o00ooo0 / iIii1I11I1II1 % oOo % i11iIiiIii . oOoO0oo0OOOo
   iIii1I111I11I = re . compile ( "'https:(.+?)'" ) . findall ( oooOOOOO )
   for OO00OooO0OO in iIii1I111I11I :
    OO00OooO0OO = OO00OooO0OO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    iiiIi = 'https:' + OO00OooO0OO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    IiIIIiI1I1 ( Oo0o0000o0o0 , iiiIi , 20 , oo , i1iII1IiiIiI1 , '' , '' )
    if 68 - 68: Oo0oO0ooo + o00 . iIii1I11I1II1 - IiIi11i % iIii1I11I1II1 - oOo
    if 79 - 79: IiiI + oOoO0oo0OOOo - OooooO0oOO
def oO00O00o0OOO0 ( ) :
 iI1Ii11111iIi = 'http://arconaitv.me/'
 i1i1II = 'index.php#movies'
 o0oOoO00o = BeautifulSoup ( requests . get ( iI1Ii11111iIi + i1i1II ) . content )
 i1 = o0oOoO00o . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for oOOoo00O0O in i1 :
  i1111 = oOOoo00O0O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for i11 in i1111 :
   OooO0 = i11 . text
  II11iiii1Ii = oOOoo00O0O . findAll ( 'a' )
  for i11 in II11iiii1Ii :
   if i11 . has_key ( 'href' ) :
    I11 = iI1Ii11111iIi + i11 [ 'href' ]
   if i11 . has_key ( 'title' ) :
    Oo0o0000o0o0 = i11 [ 'title' ]
   oO = { 'User-Agent' : random_agent ( ) }
   i1iiIIiiI111 = requests . get ( I11 , headers = oO ) . content
   oooOOOOO = packets ( i1iiIIiiI111 )
   if 27 - 27: O0 % i1IIi * o00ooo0 + i11iIiiIii + OoooooooOO * i1IIi
   iIii1I111I11I = re . compile ( "'https:(.+?)'" ) . findall ( oooOOOOO )
   for OO00OooO0OO in iIii1I111I11I :
    OO00OooO0OO = OO00OooO0OO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    iiiIi = 'https:' + OO00OooO0OO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    IiIIIiI1I1 ( Oo0o0000o0o0 , iiiIi , 20 , oo , i1iII1IiiIiI1 , '' , '' )
    if 80 - 80: Oo0oO0ooo * i11iIiiIii / i11I1IIiiIi
    if 9 - 9: oOO + o00ooo0 % oOO + i1IIi . o00
def III1i1i ( ) :
 iI1Ii11111iIi = 'http://arconaitv.me/'
 i1i1II = 'index.php#cable'
 o0oOoO00o = BeautifulSoup ( requests . get ( iI1Ii11111iIi + i1i1II ) . content )
 i1 = o0oOoO00o . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for oOOoo00O0O in i1 :
  i1111 = oOOoo00O0O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for i11 in i1111 :
   OooO0 = i11 . text
  II11iiii1Ii = oOOoo00O0O . findAll ( 'a' )
  for i11 in II11iiii1Ii :
   if i11 . has_key ( 'href' ) :
    I11 = iI1Ii11111iIi + i11 [ 'href' ]
   if i11 . has_key ( 'title' ) :
    Oo0o0000o0o0 = i11 [ 'title' ]
   oO = { 'User-Agent' : random_agent ( ) }
   i1iiIIiiI111 = requests . get ( I11 , headers = oO ) . content
   oooOOOOO = packets ( i1iiIIiiI111 )
   if 26 - 26: OoooooooOO
   iIii1I111I11I = re . compile ( "'https:(.+?)'" ) . findall ( oooOOOOO )
   for OO00OooO0OO in iIii1I111I11I :
    OO00OooO0OO = OO00OooO0OO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    iiiIi = 'https:' + OO00OooO0OO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    IiIIIiI1I1 ( Oo0o0000o0o0 , iiiIi , 20 , oo , i1iII1IiiIiI1 , '' , '' )
    if 12 - 12: OoooooooOO % o0OO0 / oOo % Oo0ooO0oo0oO
def iiii ( ) :
 oO0o0O0OOOoo0 = 'http://arconaitv.me/stream.php?id=random'
 oO = { 'User-Agent' : random_agent ( ) }
 i1iiIIiiI111 = requests . get ( oO0o0O0OOOoo0 , headers = oO ) . content
 oooOOOOO = packets ( i1iiIIiiI111 )
 if 48 - 48: O0 + O0 - I1i1iI1i . oOo / iIii1I11I1II1
 iIii1I111I11I = re . compile ( "'https:(.+?)'" ) . findall ( oooOOOOO )
 for OO00OooO0OO in iIii1I111I11I :
  OO00OooO0OO = OO00OooO0OO . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
  iiiIi = 'https:' + OO00OooO0OO + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  IiIIIiI1I1 ( 'Random Pick' , iiiIi , 20 , oo , i1iII1IiiIiI1 , '' , '' )
  if 77 - 77: i1IIi % o0OO0 - IiIi11i + oOo
  if 31 - 31: Oo0oO0ooo - i1IIi * o00 / OoooooooOO
  if 18 - 18: i11iIiiIii
  if 46 - 46: i1IIi / Oo0oO0ooo % o00 + i11I1IIiiIi
def O0OOO00oo ( ) :
 Iii111II = REPLACE_SEARCH
 iiii11I = xbmcgui . Dialog ( )
 Ooo0OO0oOO = iiii11I . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii11i1 = Ooo0OO0oOO . replace ( ' ' , '%20' ) . lower ( )
 Iii111II = Iii111II + ii11i1
 if 29 - 29: I1i1iI1i % oOoO0oo0OOOo + oOo / Oo0ooO0oo0oO + o00 * Oo0ooO0oo0oO
def i1I1iI ( content , viewType ) :
 if 93 - 93: iIii1I11I1II1 % o00ooo0 * i1IIi
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if ADDON . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % ADDON . getSetting ( viewType ) )
  if 16 - 16: O0 - i11I1IIiiIi * iIii1I11I1II1 + OooooO0oOO
  if 50 - 50: i11ii11iIi11i - oOo * I1i1iI1i / i11I1IIiiIi + Oo0ooO0oo0oO
def IiII ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0O0O = mode
 oO0Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 oOOoo0Oo = True
 o00OO00OoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o00OO00OoO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o00OO00OoO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOOO0OOoO0O0 = [ ]
  if showcontext == 'fav' :
   OOOO0OOoO0O0 . append ( ( 'Remove from Twenty4Seven Favorites' , 'XBMC.RunPlugin(%s?mode=12&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0O :
   OOOO0OOoO0O0 . append ( ( 'Add to Twenty4Seven Favourites' , 'XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , O0O0O , urllib . quote_plus ( fanart ) , urllib . quote_plus ( description ) ) ) )
  o00OO00OoO . addContextMenuItems ( OOOO0OOoO0O0 )
 oOOoo0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0Oo , listitem = o00OO00OoO , isFolder = True )
 return oOOoo0Oo
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 65 - 65: IiIi11i * oOoO0oo0OOOo + oOO % i11iIiiIii * o00ooo0 . i11I1IIiiIi
 if 100 - 100: O0 + IiIi11i - o00 + i11iIiiIii * oOO
 if 30 - 30: Oo0ooO0oo0oO . oOO - OoooooooOO
def IiIIIiI1I1 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0O0O = mode
 oO0Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 oOOoo0Oo = True
 o00OO00OoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o00OO00OoO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o00OO00OoO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OOOO0OOoO0O0 = [ ]
  if showcontext == 'fav' :
   OOOO0OOoO0O0 . append ( ( 'Remove from Twenty4Seven Favorites' , 'XBMC.RunPlugin(%s?mode=12&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O0O :
   OOOO0OOoO0O0 . append ( ( 'Add to Twenty4Seven Favourites' , 'XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , O0O0O , urllib . quote_plus ( fanart ) , urllib . quote_plus ( description ) ) ) )
  o00OO00OoO . addContextMenuItems ( OOOO0OOoO0O0 )
  OOOO0OOoO0O0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=14)' % sys . argv [ 0 ] ) )
 oOOoo0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0Oo , listitem = o00OO00OoO , isFolder = False )
 return oOOoo0Oo
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 8 - 8: i1IIi - iIii1I11I1II1 * i11ii11iIi11i + i11iIiiIii / i11I1IIiiIi % o00
 if 16 - 16: I1i1iI1i + Iii1ii1II11i - i11ii11iIi11i
 if 85 - 85: o0OO0 + i1IIi
 if 58 - 58: i11ii11iIi11i * o00 * I1i1iI1i / o00
def oO0o0OOOO ( name , url , mode , iconimage , fanart , description , extra ) :
 O0O0OoOO0 = [ ]
 try :
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i ) == False :
  O0O0OoOO0 . append ( ( name , url , mode , iconimage , fanart , description , extra ) )
  iiiI1I11i1 = open ( I11i , "w" )
  iiiI1I11i1 . write ( json . dumps ( O0O0OoOO0 ) )
  iiiI1I11i1 . close ( )
 else :
  iiiI1I11i1 = open ( I11i ) . read ( )
  IIi1i11111 = json . loads ( iiiI1I11i1 )
  IIi1i11111 . append ( ( name , url , mode , iconimage , fanart , description , extra ) )
  ooOO00O00oo = open ( I11i , "w" )
  ooOO00O00oo . write ( json . dumps ( IIi1i11111 ) )
  ooOO00O00oo . close ( )
  if 3 - 3: i11I1IIiiIi - O0 / i11I1IIiiIi % Iii1ii1II11i / i11I1IIiiIi . oOoO0oo0OOOo
  if 50 - 50: IiIi11i
def i11I1iIiII ( ) :
 if not os . path . exists ( I11i ) :
  O0O0OoOO0 = [ ]
  O0O0OoOO0 . append ( ( 'Twenty4Seven Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  iiiI1I11i1 = open ( I11i , "w" )
  iiiI1I11i1 . write ( json . dumps ( O0O0OoOO0 ) )
  iiiI1I11i1 . close ( )
 else :
  oO00o0 = json . loads ( open ( I11i ) . read ( ) )
  for OOoo0O in oO00o0 :
   Oo0o0000o0o0 = OOoo0O [ 0 ]
   iI1Ii11111iIi = OOoo0O [ 1 ]
   try :
    Oo0ooOo0o = OOoo0O [ 3 ]
   except :
    Oo0ooOo0o = ''
   try :
    Ii1i1 = OOoo0O [ 4 ]
   except :
    Ii1i1 = ''
   try :
    iiIii = OOoo0O [ 5 ]
   except :
    iiIii = ''
   try :
    ooo0O = OOoo0O [ 6 ]
   except :
    ooo0O = ''
    if 75 - 75: Oo0ooO0oo0oO % Oo0ooO0oo0oO . i11I1IIiiIi
   if OOoo0O [ 2 ] == 20 :
    IiIIIiI1I1 ( Oo0o0000o0o0 , iI1Ii11111iIi , OOoo0O [ 2 ] , Oo0ooOo0o , Ii1i1 , iiIii , ooo0O , 'fav' )
   else :
    IiII ( Oo0o0000o0o0 , iI1Ii11111iIi , OOoo0O [ 2 ] , Oo0ooOo0o , Ii1i1 , iiIii , ooo0O , 'fav' )
    if 5 - 5: Oo0ooO0oo0oO * oOo + o0OO0 . o00 + o0OO0
    if 91 - 91: O0
def oOOo0 ( name ) :
 IIi1i11111 = json . loads ( open ( I11i ) . read ( ) )
 for i1i1II in range ( len ( IIi1i11111 ) ) :
  if IIi1i11111 [ i1i1II ] [ 0 ] == name :
   del IIi1i11111 [ i1i1II ]
   ooOO00O00oo = open ( I11i , "w" )
   ooOO00O00oo . write ( json . dumps ( IIi1i11111 ) )
   ooOO00O00oo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 54 - 54: O0 - IiIi11i % o00
def OOoO ( name , url ) :
 xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 46 - 46: Iii1ii1II11i . IiiI - OoooooooOO
def ooo00OOOooO ( ) :
 O00OOOoOoo0O = [ ]
 O000OOo00oo = sys . argv [ 2 ]
 if len ( O000OOo00oo ) >= 2 :
  oo0OOo = sys . argv [ 2 ]
  ooOOO00Ooo = oo0OOo . replace ( '?' , '' )
  if ( oo0OOo [ len ( oo0OOo ) - 1 ] == '/' ) :
   oo0OOo = oo0OOo [ 0 : len ( oo0OOo ) - 2 ]
  IiIIIi1iIi = ooOOO00Ooo . split ( '&' )
  O00OOOoOoo0O = { }
  for OOoo0O in range ( len ( IiIIIi1iIi ) ) :
   ooOOoooooo = { }
   ooOOoooooo = IiIIIi1iIi [ OOoo0O ] . split ( '=' )
   if ( len ( ooOOoooooo ) ) == 2 :
    O00OOOoOoo0O [ ooOOoooooo [ 0 ] ] = ooOOoooooo [ 1 ]
    if 1 - 1: IiiI / Oo0ooO0oo0oO % OooooO0oOO * IiIi11i . i11iIiiIii
 return O00OOOoOoo0O
 if 2 - 2: I1i1iI1i * Oo0oO0ooo - iIii1I11I1II1 + oOoO0oo0OOOo . o00ooo0 % OooooO0oOO
oo0OOo = ooo00OOOooO ( )
iI1Ii11111iIi = None
Oo0o0000o0o0 = None
Oo0ooOo0o = None
ooOOOoOooOoO = None
Ii1i1 = None
iiIii = None
o00oooO0Oo = None
O0O0O = None
ooo0O = None
if 78 - 78: oOO % i11I1IIiiIi + I1i1iI1i
try :
 ooo0O = urllib . unquote_plus ( oo0OOo [ "extra" ] )
except :
 pass
 if 64 - 64: o00ooo0 * O0 . oOoO0oo0OOOo + i11ii11iIi11i
try :
 O0O0O = int ( oo0OOo [ "fav_mode" ] )
except :
 pass
 if 6 - 6: o0OO0 / OooooO0oOO . IiIi11i . IiIi11i
try :
 iI1Ii11111iIi = urllib . unquote_plus ( oo0OOo [ "url" ] )
except :
 pass
try :
 Oo0o0000o0o0 = urllib . unquote_plus ( oo0OOo [ "name" ] )
except :
 pass
try :
 Oo0ooOo0o = urllib . unquote_plus ( oo0OOo [ "iconimage" ] )
except :
 pass
try :
 ooOOOoOooOoO = int ( oo0OOo [ "mode" ] )
except :
 pass
try :
 Ii1i1 = urllib . unquote_plus ( oo0OOo [ "fanart" ] )
except :
 pass
try :
 iiIii = urllib . unquote_plus ( oo0OOo [ "description" ] )
except :
 pass
 if 62 - 62: I1i1iI1i + IiIi11i % OooooO0oOO + o00
 if 33 - 33: O0 . IiIi11i . oOoO0oo0OOOo
 if 72 - 72: i1IIi / Iii1ii1II11i + OoooooooOO - IiiI
if ooOOOoOooOoO == None : iI111iI ( )
elif ooOOOoOooOoO == 1 : ooOoo0O ( )
elif ooOOOoOooOoO == 3 : iiii ( )
elif ooOOOoOooOoO == 2 : oO00O00o0OOO0 ( )
elif ooOOOoOooOoO == 4 : III1i1i ( )
if 29 - 29: I1i1iI1i + o00ooo0 % O0
elif ooOOOoOooOoO == 10 : i11I1iIiII ( )
elif ooOOOoOooOoO == 11 :
 try :
  Oo0o0000o0o0 = Oo0o0000o0o0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0o0000o0o0 = Oo0o0000o0o0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 oO0o0OOOO ( Oo0o0000o0o0 , iI1Ii11111iIi , O0O0O , Oo0ooOo0o , Ii1i1 , iiIii , ooo0O )
elif ooOOOoOooOoO == 12 :
 try :
  Oo0o0000o0o0 = Oo0o0000o0o0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0o0000o0o0 = Oo0o0000o0o0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 oOOo0 ( Oo0o0000o0o0 )
elif ooOOOoOooOoO == 14 : queueItem ( )
elif ooOOOoOooOoO == 20 : OOoO ( Oo0o0000o0o0 , iI1Ii11111iIi )
if 10 - 10: Oo0oO0ooo / i11I1IIiiIi - oOoO0oo0OOOo * iIii1I11I1II1 - oOoO0oo0OOOo
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
