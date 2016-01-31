if 64 - 64: i11iIiiIii
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
import sys
import urlparse
import urllib , urllib2 , datetime , re , os , base64 , xbmc , xbmcplugin , xbmcgui , xbmcaddon , xbmcvfs , traceback , cookielib , urlparse , httplib , time
import urlresolver
import time
from t0mm0 . common . addon import Addon
from t0mm0 . common . net import Net
from datetime import datetime
if 79 - 79: oO0o + I1Ii111 . ooOoO0o * IiII % I11i . I1IiiI
O0o0o00o0Oo0 = xbmcgui . Dialog ( )
ii11 = base64 . decodestring
I1I1i1 = 'plugin.audio.kodible'
IiI1i = sys . argv [ 0 ]
OOo0o0 = int ( sys . argv [ 1 ] )
O0OoOoo00o = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
iiiI11 = "Kodible"
OOooO = "1.0.1"
OOoO00o = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
II111iiiiII = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
oOoOo00oOo = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
Oo = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
if 85 - 85: OOooOOo % I1ii11iIi11i * ooOoO0o
OO0O00OooO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
OoooooOoo = os . path . join ( OO0O00OooO , I1I1i1 , 'resources' , 'art' ) + os . sep
OO = xbmc . translatePath ( os . path . join ( OO0O00OooO , I1I1i1 , 'fanart.jpg' ) )
oO0O = base64 . decodestring ( 'LnBocA==' )
OOoO000O0OO = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
if 23 - 23: i11iIiiIii + I1IiiI
if 68 - 68: OoOoOO00 . oO0o . i11iIiiIii
def II ( ) :
 iI ( 'Audio Books' , '' , 11 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
 iI ( 'Kids Audio Books' , '' , 6 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
 if 22 - 22: Oo0Ooo % Ii1I
def oo ( ) :
 iI ( 'All' , '' , 1 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
 iI ( 'Popular' , '' , 12 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
 iI ( 'Search' , '' , 13 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
 if 54 - 54: OOooOOo + OOooOOo % I1Ii111 % i11iIiiIii / iIii1I11I1II1 . OOooOOo
def o0oO0o00oo ( ) :
 II1i1Ii11Ii11 = iII11i ( OOoO000O0OO + 'books' + oO0O )
 O0O00o0OOO0 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II1i1Ii11Ii11 )
 for Ii1iIIIi1ii , o0oo0o0O00OO , o0oO in O0O00o0OOO0 :
  if 'Parent' in Ii1iIIIi1ii :
   pass
  elif '2' in o0oO :
   iI ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0oo0o0O00OO , 10 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   if 48 - 48: I11i + I11i / II111iiii / iIii1I11I1II1
def i1iiI11I ( ) :
 iiii = O0o0o00o0Oo0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0O0OOOoo0 = iiii . lower ( )
 II1i1Ii11Ii11 = iII11i ( OOoO000O0OO + 'books' + oO0O )
 O0O00o0OOO0 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II1i1Ii11Ii11 )
 for Ii1iIIIi1ii , o0oo0o0O00OO , o0oO in O0O00o0OOO0 :
  if iiii in Ii1iIIIi1ii . lower ( ) :
   if '1' in o0oO :
    iI ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0oo0o0O00OO , 10 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   elif '2' in o0oO :
    iI ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0oo0o0O00OO , 10 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   elif '3' in o0oO :
    iI ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0oo0o0O00OO , 9 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
    if 48 - 48: O0 + O0 - I1ii11iIi11i . ooOoO0o / iIii1I11I1II1
    if 77 - 77: i1IIi % OoOoOO00 - IiII + ooOoO0o
def I11iiIiii ( ) :
 II1i1Ii11Ii11 = iII11i ( OOoO000O0OO + 'books' + oO0O )
 O0O00o0OOO0 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II1i1Ii11Ii11 )
 for Ii1iIIIi1ii , o0oo0o0O00OO , o0oO in O0O00o0OOO0 :
  if '1' in o0oO :
   iI ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0oo0o0O00OO , 10 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
  elif '2' in o0oO :
   iI ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0oo0o0O00OO , 10 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
  elif '3' in o0oO :
   iI ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0oo0o0O00OO , 9 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   if 1 - 1: II111iiii - I11i / I11i
 xbmcplugin . addSortMethod ( OOo0o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 46 - 46: Ii1I * OOooOOo - OoO0O00 * oO0o - I1Ii111
def oo0 ( url ) :
 o00 = url
 II1i1Ii11Ii11 = iII11i ( url )
 OooOooo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( II1i1Ii11Ii11 )
 for url , Ii1iIIIi1ii in OooOooo :
  if 'mp3' in Ii1iIIIi1ii :
   O000oo0O ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) , o00 + url , 2 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
  if 'wma' in Ii1iIIIi1ii :
   O000oo0O ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) , o00 + url , 2 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
  if 'm4b' in Ii1iIIIi1ii :
   O000oo0O ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) , o00 + url , 2 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
  elif '/' in Ii1iIIIi1ii :
   iI ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o00 + url , 9 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   if 66 - 66: I1ii11iIi11i / OoOoOO00 - I1IiiI . OOooOOo / I1IiiI * OOooOOo
   if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
   if 42 - 42: Ii1I + oO0o
def o0O0o0Oo ( url ) :
 II1i1Ii11Ii11 = iII11i ( url )
 o00 = url
 O0O00o0OOO0 = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( II1i1Ii11Ii11 )
 for url , Ii1iIIIi1ii in O0O00o0OOO0 :
  if 'Parent' in Ii1iIIIi1ii :
   pass
  elif '.db' in Ii1iIIIi1ii :
   pass
  elif '.jpg' in Ii1iIIIi1ii :
   pass
  elif '.html' in Ii1iIIIi1ii :
   pass
  elif '.doc' in Ii1iIIIi1ii :
   pass
  elif 'mp3' in Ii1iIIIi1ii :
   O000oo0O ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o00 + url , 2 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
  elif 'm4a' in Ii1iIIIi1ii :
   O000oo0O ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o00 + url , 2 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
  else :
   iI ( ( Ii1iIIIi1ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o00 + url , 10 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   if 16 - 16: O0 - I1Ii111 * iIii1I11I1II1 + iII111i
   if 50 - 50: II111iiii - ooOoO0o * I1ii11iIi11i / I1Ii111 + o0oOOo0O0Ooo
def O0O0O ( ) :
 iI ( 'A-Z' , '' , 7 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
 iI ( 'All' , '' , 3 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
 iI ( 'Search' , '' , 14 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
 if 83 - 83: I1ii11iIi11i / ooOoO0o
def iIIIIii1 ( ) :
 II1i1Ii11Ii11 = iII11i ( ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 O0O00o0OOO0 = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II1i1Ii11Ii11 )
 for o0oo0o0O00OO , oo000OO00Oo in O0O00o0OOO0 :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + o0oo0o0O00OO + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oo000OO00Oo :
   pass
  else :
   iI ( oo000OO00Oo , ( ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( o0oo0o0O00OO ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 8 , ( ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oo000OO00Oo + '.gif' , OoooooOoo + 'fanart.jpg' , '' )
   if 51 - 51: IiII * o0oOOo0O0Ooo + I11i + OoO0O00
 xbmcplugin . addSortMethod ( OOo0o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66: OoOoOO00
 if 97 - 97: oO0o % IiII * IiII
def i11iiI111I ( url ) :
 II1i1Ii11Ii11 = iII11i ( url )
 O0O00o0OOO0 = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II1i1Ii11Ii11 )
 for url , Ii1iIIIi1ii in O0O00o0OOO0 :
  if '</a>' in Ii1iIIIi1ii :
   pass
  elif '(' in Ii1iIIIi1ii :
   iI ( ( Ii1iIIIi1ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 5 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
  else :
   O000oo0O ( ( Ii1iIIIi1ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 4 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   if 10 - 10: OoO0O00 * I1Ii111 % Ii1I . II111iiii
 xbmcplugin . addSortMethod ( OOo0o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: o0oOOo0O0Ooo
def Oo0O ( ) :
 iiii = O0o0o00o0Oo0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0O0OOOoo0 = iiii . lower ( )
 II1i1Ii11Ii11 = iII11i ( ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 O0O00o0OOO0 = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II1i1Ii11Ii11 )
 for o0oo0o0O00OO , Ii1iIIIi1ii in O0O00o0OOO0 :
  if iiii in Ii1iIIIi1ii . lower ( ) :
   if '</a>' in Ii1iIIIi1ii :
    pass
   elif '(' in Ii1iIIIi1ii :
    iI ( ( Ii1iIIIi1ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0oo0o0O00OO , 5 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   else :
    O000oo0O ( ( Ii1iIIIi1ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0oo0o0O00OO , 4 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
    if 25 - 25: OoOoOO00 . II111iiii / iII111i . OOooOOo * OoO0O00 . I1IiiI
    if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
def Oo0OoO00oOO0o ( ) :
 II1i1Ii11Ii11 = iII11i ( ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 O0O00o0OOO0 = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II1i1Ii11Ii11 )
 for o0oo0o0O00OO , Ii1iIIIi1ii in O0O00o0OOO0 :
  if '</a>' in Ii1iIIIi1ii :
   pass
  elif '(' in Ii1iIIIi1ii :
   iI ( ( Ii1iIIIi1ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0oo0o0O00OO , 5 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
  else :
   O000oo0O ( ( Ii1iIIIi1ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0oo0o0O00OO , 4 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   if 80 - 80: oO0o + OOooOOo - OOooOOo % iII111i
 xbmcplugin . addSortMethod ( OOo0o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: I1IiiI - I1ii11iIi11i + O0 % I11i / iIii1I11I1II1 / o0oOOo0O0Ooo
 if 98 - 98: iII111i * iII111i / iII111i + I11i
def ii111111I1iII ( url ) :
 II1i1Ii11Ii11 = iII11i ( url )
 O0O00o0OOO0 = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( II1i1Ii11Ii11 )
 for url in O0O00o0OOO0 :
  o00 = ( ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  O00ooo0O0 ( o00 )
  if 23 - 23: iII111i
def oo0oOo ( url ) :
 II1i1Ii11Ii11 = iII11i ( url )
 O0O00o0OOO0 = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( II1i1Ii11Ii11 )
 for Ii1iIIIi1ii , url in O0O00o0OOO0 :
  if '<p align' in Ii1iIIIi1ii :
   pass
  elif '&nbsp;' in Ii1iIIIi1ii :
   pass
  else :
   O000oo0O ( ( Ii1iIIIi1ii ) . replace ( '&nbsp;' , '' ) , ii11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 2 , OoooooOoo + 'icon.png' , OoooooOoo + 'fanart.jpg' , '' )
   if 89 - 89: OoOoOO00
 xbmcplugin . addSortMethod ( OOo0o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + ooOoO0o
def O000oo0O ( name , url , mode , iconimage , fanart , description ) :
 if 4 - 4: ooOoO0o + O0 * OOooOOo
 OOoo0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo0ooOo0o = True
 Ii1i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1 . setProperty ( "Fanart_Image" , fanart )
 Oo0ooOo0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0O , listitem = Ii1i1 , isFolder = False )
 return Oo0ooOo0o
 if 15 - 15: II111iiii
def iI ( name , url , mode , iconimage , fanart , description ) :
 if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 OOoo0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo0ooOo0o = True
 Ii1i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1 . setProperty ( "Fanart_Image" , fanart )
 Oo0ooOo0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoo0O , listitem = Ii1i1 , isFolder = True )
 return Oo0ooOo0o
 if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
def III1iII1I1ii ( ) :
 oOOo0 = [ ]
 oo00O00oO = sys . argv [ 2 ]
 if len ( oo00O00oO ) >= 2 :
  iIiIIIi = sys . argv [ 2 ]
  ooo00OOOooO = iIiIIIi . replace ( '?' , '' )
  if ( iIiIIIi [ len ( iIiIIIi ) - 1 ] == '/' ) :
   iIiIIIi = iIiIIIi [ 0 : len ( iIiIIIi ) - 2 ]
  O00OOOoOoo0O = ooo00OOOooO . split ( '&' )
  oOOo0 = { }
  for O000OOo00oo in range ( len ( O00OOOoOoo0O ) ) :
   oo0OOo = { }
   oo0OOo = O00OOOoOoo0O [ O000OOo00oo ] . split ( '=' )
   if ( len ( oo0OOo ) ) == 2 :
    oOOo0 [ oo0OOo [ 0 ] ] = oo0OOo [ 1 ]
    if 64 - 64: I11i
 return oOOo0
 if 22 - 22: Oo0Ooo + Ii1I % I1ii11iIi11i
iIiIIIi = III1iII1I1ii ( )
o0oo0o0O00OO = None
Ii1iIIIi1ii = None
iI1 = None
IIi1iIi = None
ooOOoooooo = None
if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iII111i
try :
 o0oo0o0O00OO = urllib . unquote_plus ( iIiIIIi [ "url" ] )
except :
 pass
try :
 Ii1iIIIi1ii = urllib . unquote_plus ( iIiIIIi [ "name" ] )
except :
 pass
try :
 iI1 = urllib . unquote_plus ( iIiIIIi [ "iconimage" ] )
except :
 pass
try :
 IIi1iIi = int ( iIiIIIi [ "mode" ] )
except :
 pass
try :
 ooOOOoOooOoO = urllib . unquote_plus ( iIiIIIi [ "fanart" ] )
except :
 pass
try :
 ooOOoooooo = urllib . unquote_plus ( iIiIIIi [ "description" ] )
except :
 pass
 if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
 if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
print str ( iiiI11 ) + ': ' + str ( OOooO )
print "Mode: " + str ( IIi1iIi )
print "URL: " + str ( o0oo0o0O00OO )
print "Name: " + str ( Ii1iIIIi1ii )
print "IconImage: " + str ( iI1 )
if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
def oo0o00O ( ) :
 try :
  o00O0OoO = getSet ( "core-player" )
  if ( o00O0OoO == 'DVDPLAYER' ) : i1I = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o00O0OoO == 'MPLAYER' ) : i1I = xbmc . PLAYER_CORE_MPLAYER
  elif ( o00O0OoO == 'PAPLAYER' ) : i1I = xbmc . PLAYER_CORE_PAPLAYER
  else : i1I = xbmc . PLAYER_CORE_AUTO
 except : i1I = xbmc . PLAYER_CORE_AUTO
 return i1I
 return True
 if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
 if 29 - 29: I1ii11iIi11i + oO0o % O0
def O00ooo0O0 ( url ) :
 I1I11 = xbmc . Player ( oo0o00O ( ) )
 import urlresolver
 try : I1I11 . play ( url )
 except : pass
 if 34 - 34: I1IiiI . OOooOOo * I1ii11iIi11i + I1Ii111
def iII11i ( url ) :
 i11111IIIII = urllib2 . Request ( url )
 OOoO00o = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
 II111iiiiII = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
 oOoOo00oOo = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
 Oo = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
 i11111IIIII . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iIiii1i111iI1 = urllib2 . urlopen ( i11111IIIII )
 i11 = iIiii1i111iI1 . read ( )
 iIiii1i111iI1 . close ( )
 return i11
 if 81 - 81: OoO0O00
def IIi1 ( content , viewType ) :
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
  if 45 - 45: iII111i / iII111i + I1Ii111 + ooOoO0o
  if 47 - 47: o0oOOo0O0Ooo + ooOoO0o
if IIi1iIi == None : II ( )
elif IIi1iIi == 1 : I11iiIiii ( )
elif IIi1iIi == 2 : O00ooo0O0 ( o0oo0o0O00OO )
elif IIi1iIi == 3 : Oo0OoO00oOO0o ( )
elif IIi1iIi == 4 : ii111111I1iII ( o0oo0o0O00OO )
elif IIi1iIi == 5 : oo0oOo ( o0oo0o0O00OO )
elif IIi1iIi == 6 : O0O0O ( )
elif IIi1iIi == 7 : iIIIIii1 ( )
elif IIi1iIi == 8 : i11iiI111I ( o0oo0o0O00OO )
elif IIi1iIi == 9 : oo0 ( o0oo0o0O00OO )
elif IIi1iIi == 10 : o0O0o0Oo ( o0oo0o0O00OO )
elif IIi1iIi == 11 : oo ( )
elif IIi1iIi == 12 : o0oO0o00oo ( )
elif IIi1iIi == 13 : i1iiI11I ( )
elif IIi1iIi == 14 : Oo0O ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
