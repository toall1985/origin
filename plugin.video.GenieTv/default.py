# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
from imports import cloudflare , googleplus , client , cleantitle
from imports import yt
import httplib
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2 , urllib , glob , traceback
import re
from imports import extract
from imports import downloader
import plugintools
import zipfile
import time
import ntpath
import cookielib
import buggalo
from imports import Parse , CNF_Studio_Indexer
try :
 import json
except :
 import simplejson as json
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from imports . tvGuide import gui
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = ''
def oo ( i , t1 , t2 = [ ] ) :
 i1iII1IiiIiI1 = o0OO00
 for iIiiiI1IiI1I1 in t1 :
  i1iII1IiiIiI1 += chr ( iIiiiI1IiI1I1 )
  i += 1
  if i > 1 :
   i1iII1IiiIiI1 = i1iII1IiiIiI1 [ : - 1 ]
   i = 0
 for iIiiiI1IiI1I1 in t2 :
  i1iII1IiiIiI1 += chr ( iIiiiI1IiI1I1 )
  i += 1
  if i > 1 :
   i1iII1IiiIiI1 = i1iII1IiiIiI1 [ : - 1 ]
   i = 0
 return i1iII1IiiIiI1
 if 87 - 87: OoOoOO00
 if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
 if 73 - 73: OOooOOo / ii11ii1ii
O00ooOO = "2.7.1"
I1iII1iiII = xbmc . translatePath ( 'special://home/addons/repository.GenieTv' )
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/' )
i1i1II = xbmc . translatePath ( 'special://home/addonsbroke/' )
O0oo0OO0 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
I1i1iiI1 = 'plugin.video.GenieTv'
iiIIIII1i1iI = [ 'plugin.video.GenieTv' , 'script.module.addon.common' , 'repository.GenieTv' ]
o0oO0 = xbmcaddon . Addon ( id = I1i1iiI1 )
oo00 = xbmc . translatePath ( 'special://home/media' )
o00 = 'plugin.video.GenieTv'
Oo0oO0ooo = xbmcgui . DialogProgress ( )
o0oOoO00o = "[COLORgreen]GenieTv[/COLOR]"
i1 = Net ( )
oOOoo00O0O = xbmcgui . Dialog ( )
i1111 = base64 . decodestring
i11 = o0oO0 . getSetting ( 'Build' )
I11 = o0oO0 . getSetting ( 'Local' )
Oo0o0000o0o0 = o0oO0 . getSetting ( 'Remote' )
oOo0oooo00o = o0oO0 . getSetting ( 'LocalM3u' )
oO0o0o0ooO0oO = o0oO0 . getSetting ( 'User' )
oo0o0O00 = o0oO0 . getSetting ( 'Pass' )
oO = o0oO0 . getSetting ( 'AdultPass' )
i1iiIIiiI111 = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
i1iiIII111ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1i1iiI1 , 'fanart.jpg' ) )
i1iIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1i1iiI1 , 'icon.png' , i1iiIII111ii , '' ) )
ii11iIi1I = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
iI111I11I1I1 = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
OOooO0OOoo = xbmc . translatePath ( 'special://database' )
iIii1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
oOOoO0 = xbmc . translatePath ( 'special://thumbnails' ) ;
O0OoO000O0OO = "GenieTv"
iiI1IiI = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
ooOoOoo0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
OooO0 = 'http://'
II11iiii1Ii = base64 . decodestring ( 'LnBocA==' )
OO0o = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
Ooo = [ ]
O0o0Oo = o0oO0 . getLocalizedString
Oo00OOOOO = CookieJar ( )
O0O = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( Oo00OOOOO ) )
O0O . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O00o0OO = int ( sys . argv [ 1 ] )
I11i1 = xbmc . translatePath ( o0oO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iIi1ii1I1 = os . path . join ( I11i1 , 'favorites' )
o0 = iIii1 + '/addons.ini'
I11II1i = xbmc . translatePath ( 'special://home/userdata/' )
IIIII = xbmc . translatePath ( 'special://home/userdatabroke/' )
ooooooO0oo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
if os . path . exists ( iIi1ii1I1 ) == True :
 OOOO = open ( iIi1ii1I1 ) . read ( )
else : OOOO = [ ]
OOO00 = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
 if 21 - 21: ii - Ii11I
def OOO0OOO00oo ( ) :
 if not os . path . exists ( I1iII1iiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  Iii111II = 'genie tv repo not being installed '
  iiii11I ( Iii111II )
 Ooo0OO0oOO ( )
 ii11i1 ( )
 IIIii1II1II ( )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  i1I1iI ( '[COLORgreen]WIZARD[/COLOR]' , iiI1IiI , 4001 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  i1I1iI ( '[COLORgreen]STREAMS[/COLOR]' , iiI1IiI , 4002 , ii11iIi1I + 'streams.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  i1I1iI ( '[COLORgreen]Music[/COLOR]' , iiI1IiI , 4003 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
  if 93 - 93: IiiIIi11I % oOo00oOO0O . O0O0O
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  i1I1iI ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , iiI1IiI , 32 , ii11iIi1I + 'builderstoolbox.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  i1I1iI ( '[COLORgreen]SOURCE LIST[/COLOR]' , iiI1IiI , 46 , ii11iIi1I + 'sources.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  i1I1iI ( '[COLORgreen]MAINTENANCE[/COLOR]' , iiI1IiI , 3 , ii11iIi1I + 'MAIN6.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  i1I1iI ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , ii11iIi1I + 'ADDONS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  i1I1iI ( '[COLORgreen]APK TOOL[/COLOR]' , iiI1IiI , 2 , ii11iIi1I + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  i1I1iI ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , iiI1IiI , 39 , ii11iIi1I + 'RSS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons Packs' ) == 'true' :
  i1I1iI ( '[COLORgreen]ADDONS PACKS[/COLOR]' , iiI1IiI , 30 , ii11iIi1I + 'ADDONP.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
 if 54 - 54: oo0Oo - I1II11IiII % OOO0OOo
def I1I111 ( ) :
 i1I1iI ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , iiI1IiI , 10060 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , iiI1IiI , 49 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]WIPE GENIE[/COLOR]' , iiI1IiI , 41 , ii11iIi1I + 'wipegenie.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]WISHES PC[/COLOR]' , iiI1IiI , 1 , ii11iIi1I + 'WISHESPC.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]WISHES ANDROID[/COLOR]' , iiI1IiI , 44 , ii11iIi1I + 'WISHESAN.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
def i11iiI111I ( ) :
 if oO == '5knuckleshuffle' :
  i1I1iI ( '[COLORgreen]XVID[/COLOR]' , iiI1IiI , 10100 , ii11iIi1I + 'JIZBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  i1I1iI ( '[COLORgreen]FAVOURITES[/COLOR]' , iiI1IiI , 10057 , ii11iIi1I + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  i1I1iI ( '[COLORgreen]SEARCH[/COLOR]' , iiI1IiI , 9000 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Live TV[/COLOR]' , iiI1IiI , 4009 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]MOVIES[/COLOR]' , iiI1IiI , 4004 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]TV SHOWS[/COLOR]' , iiI1IiI , 4005 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]STREAM TEAM[/COLOR]' , iiI1IiI , 4006 , ii11iIi1I + 'streamteam.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 4007 , ii11iIi1I + 'KIDSv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]HOBBIES[/COLOR]' , iiI1IiI , 4008 , ii11iIi1I + 'hobbies.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  i1I1iI ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , iiI1IiI , 10064 , ii11iIi1I + 'youtube.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  i1I1iI ( '[COLORgreen]REQUESTS[/COLOR]' , iiI1IiI + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ii11iIi1I + 'requests.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  i1I1iI ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  i1I1iI ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , iiI1IiI , 8040 , ii11iIi1I + 'documentary.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  i1I1iI ( '[COLORgreen]DISCLOSE TV[/COLOR]' , iiI1IiI , 7001 , ii11iIi1I + 'disclose.png' , i1iiIII111ii , '' )
  if 10 - 10: Ooo00oOo00o * I1II11IiII % oOo00oOO0O . OoOoOO00
  if 38 - 38: OOooOOo
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  i1I1iI ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , iiI1IiI , 3000 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
  if 57 - 57: O0 / ii * I1II11IiII / I1IiI . OoOoOO00
  if 26 - 26: O0O0O
  if 91 - 91: Ooo00oOo00o . ii11ii1ii + Ooo00oOo00o - O0O0O / OoooooooOO
  if 39 - 39: ii11ii1ii / OOO0OOo - OoOoOO00
  if 98 - 98: ii11ii1ii / IiiIIi11I % ii . I1IiI
  if 91 - 91: ii % Oo
  if 64 - 64: IiiIIi11I % O0O0O - I1II11IiII - ii
  if 31 - 31: IiiIIi11I - OoOoOO00 . IiiIIi11I
  if 18 - 18: OOooOOo
  if 98 - 98: O0O0O * O0O0O / O0O0O + IiiIIi11I
  if 34 - 34: OOO0OOo
  if 15 - 15: IiiIIi11I * OOO0OOo * Oo % i11iIiiIii % I1IiI - Ii11I
  if 68 - 68: I1II11IiII % i1IIi . oo0Oo . ii11ii1ii
 oO0Oo ( 'movies' , 'MAIN' )
 if 92 - 92: O0O0O . I1II11IiII
def Ooo0OO0oOO ( ) :
 if not os . path . exists ( ooOoOoo0O ) :
  i1i ( 'Change Log 24/04/16 - v2.7.1' , 'Just a little one to add in [COLORred]ITV section[/COLOR] into [COLORblue]streams - stream team[/COLOR], it is a film noir section for you fans. Hope you enjoy' )
  os . makedirs ( ooOoOoo0O )
  if 50 - 50: oo0Oo
  if 14 - 14: IiiIIi11I % Ooo00oOo00o * IiiIIi11I
def iII ( ) :
 i1I1iI ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  i1I1iI ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , ii11iIi1I + 'popcorn.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ii11iIi1I + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  i1I1iI ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ii11iIi1I + 'classicmovies.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
def oO00o0 ( ) :
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  i1I1iI ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  OOoo0O ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 OOoo0O ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 67 - 67: i11iIiiIii - i1IIi % ii11ii1ii . O0
 if 77 - 77: oo0Oo / OOOo0
def I1 ( ) :
 i1I1iI ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  i1I1iI ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  i1I1iI ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ii11iIi1I + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ii11iIi1I + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  i1I1iI ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , ii11iIi1I + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  i1I1iI ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , ii11iIi1I + 'classictv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ii11iIi1I + 'tvtrailers.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'tvschedule.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
def iiIii ( ) :
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  i1I1iI ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  i1I1iI ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  i1I1iI ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , ii11iIi1I + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  i1I1iI ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ii11iIi1I + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  i1I1iI ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  i1I1iI ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'redemption.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
 if 79 - 79: OoooooooOO / O0
def OO0OoO0o00 ( ) :
 i1I1iI ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'http://5.135.207.96/Scrapes/main.php' ) ) , 1016 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 53 - 53: O0 * Ooo00oOo00o + Ii11I
 if 50 - 50: O0 . O0 - ii / OOOo0 - OOooOOo * I1IiI
 if 61 - 61: IiiIIi11I
def O0oOoOOOoOO ( ) :
 i1I1iI ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  i1I1iI ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , ii11iIi1I + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  i1I1iI ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  i1I1iI ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ii11iIi1I + 'anime.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
def ii1ii11IIIiiI ( ) :
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  i1I1iI ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  i1I1iI ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ii11iIi1I + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  i1I1iI ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , ii11iIi1I + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  i1I1iI ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ii11iIi1I + 'geniekitchen.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
 if 67 - 67: IiiIIi11I * ii * ii11ii1ii + Ii11I / i1IIi
 if 11 - 11: oOo00oOO0O + O0O0O - OOO0OOo * ii % i11iIiiIii - I1II11IiII
 if 83 - 83: IiiIIi11I / OOOo0
def IIIii1II1II ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://architects.x10host.com/wizarddelete.txt' )
 oo0O0oO = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( iIIiIi1iIII1 )
 for ooooo in oo0O0oO :
  print ooooo
  ooooo = ( str ( ooooo ) )
  if os . path . exists ( xbmc . translatePath ( ooooo ) ) :
   II1I = os . path . join ( I11II1i , 'guisettings.xml' )
   O0i1II1Iiii1I11 = open ( II1I , "w+" )
   if 9 - 9: ii11ii1ii / Oo - OOOo0 / OoooooooOO / iIii1I11I1II1 - OOooOOo
   O0i1II1Iiii1I11 . write ( r'.' )
   o00oooO0Oo ( )
  else :
   pass
   if 78 - 78: oOo00oOO0O % I1II11IiII + ii11ii1ii
def ii11i1 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://architects.x10host.com/testdelete.txt' )
 oo0O0oO = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( iIIiIi1iIII1 )
 for Iii111II in oo0O0oO :
  Iii111II = ( str ( Iii111II ) )
  if os . path . exists ( xbmc . translatePath ( Iii111II ) ) :
   iiii11I ( Iii111II )
   OOooOoooOoOo ( )
  else :
   pass
   if 84 - 84: oo0Oo
def iiii11I ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 II1I = os . path . join ( II , 'default.py' )
 O0i1II1Iiii1I11 = open ( II1I , "w+" )
 if 86 - 86: I1IiI - oOo00oOO0O - Ooo00oOo00o * O0O0O
 O0i1II1Iiii1I11 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 O0i1II1Iiii1I11 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 O0i1II1Iiii1I11 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 66 - 66: OoooooooOO + O0
 if 11 - 11: IiiIIi11I + OoooooooOO - Ooo00oOo00o / OOooOOo + Oo . OoOoOO00
def o00oooO0Oo ( ) :
 iIIiIi1iIII1 = OooOOOOo ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 i1Iii1i1I = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OOoO00 , i1Iii1i1I in i1Iii1i1I :
  OOoO00 = OOoO00
  oo0O0oO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1Iii1i1I ) )
  for IiI111111IIII , i1Ii in oo0O0oO :
   i1i ( OOoO00 , IiI111111IIII , i1Ii )
   if 14 - 14: O0O0O
   if 11 - 11: oo0Oo * OOOo0 . iIii1I11I1II1 % OoooooooOO + O0O0O
   if 78 - 78: Ooo00oOo00o . Ii11I + Ooo00oOo00o / IiiIIi11I / Ooo00oOo00o
   if 54 - 54: I1IiI % O0O0O
   if 37 - 37: I1IiI * Oo / OOO0OOo - O0O0O % OoOoOO00 . ii
   if 88 - 88: O0O0O . OoOoOO00 * OoOoOO00 % I1II11IiII
   if 15 - 15: i1IIi * OOOo0 + i11iIiiIii
   if 6 - 6: OOO0OOo / i11iIiiIii + O0O0O * ii
   if 80 - 80: OoOoOO00
   if 83 - 83: IiiIIi11I . i11iIiiIii + OoOoOO00 . OOooOOo * IiiIIi11I
   if 53 - 53: OoOoOO00
   if 31 - 31: Ooo00oOo00o
   if 80 - 80: I1II11IiII . i11iIiiIii - OOooOOo
   if 25 - 25: Ooo00oOo00o
   if 62 - 62: Ii11I + O0
   if 98 - 98: OOooOOo
   if 51 - 51: Oo - ii + OoOoOO00 * oOo00oOO0O . IiiIIi11I + ii
def OoO0o ( ) :
 i1I1iI ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 i1I1iI ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 i1I1iI ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 i1I1iI ( 'Search' , '' , 10078 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 if 78 - 78: ii % O0 % oOo00oOO0O
def iiI1Ii1iI1 ( ) :
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO0O = 'http://imoviemax.se/?s=' + ( oO0 ) . replace ( ' ' , '+' )
 OO = O0OO0O . lower ( )
 OoOoO ( OO )
def Ii1I1i ( url ) :
 OOI1iI1ii1II = [ ]
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , O0O0OOOOoo in oo0O0oO :
  if IiI111111IIII in OOI1iI1ii1II :
   pass
  else :
   i1I1iI ( IiI111111IIII + ' - ' + O0O0OOOOoo + ' Films' , url , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
   OOI1iI1ii1II . append ( IiI111111IIII )
   if 74 - 74: ii11ii1ii + OoOoOO00 / Ooo00oOo00o
def oOo0O0Oo00oO ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , I111I1Iiii1i in oo0O0oO :
  i1I1iI ( IiI111111IIII + ' - Views:' + I111I1Iiii1i , url , 10075 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
  if 56 - 56: ii11ii1ii % O0 - OOOo0
  if 100 - 100: oOo00oOO0O - O0 % ii * Ii11I + OOOo0
def OoOoO ( url ) :
 Oo0O0oooo = [ ]
 iIIiIi1iIII1 = OooOOOOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( iIIiIi1iIII1 )
 for next in next :
  i1I1iI ( 'NEXT PAGE' , next , 10074 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 oo0O0oO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , IiI111111IIII , url in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 10075 , I111iI , I111iI , '' )
  Oo0O0oooo . append ( IiI111111IIII )
  if 56 - 56: OOOo0
def O0oO ( img , name , url ) :
 img = img
 name = name
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , url in oo0O0oO :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  oO00oooOOoOo0 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + oO00oooOOoOo0
  OoOOoOooooOOo = ( OO0ooOOO0OOO ) . replace ( 'play-' , 'Server ' )
  OOoo0O ( OoOOoOooooOOo , oO00oooOOoOo0 , 10076 , img , img , '' )
  if 87 - 87: OOOo0
def oOOOoo0O0oO ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( iIIiIi1iIII1 )
 for iIII1I111III in oo0O0oO :
  if '=m' in iIII1I111III :
   IIo0o0O0O00oOOo ( iIII1I111III )
  elif 'php' in iIII1I111III :
   oOOOoo0O0oO ( url )
  else :
   iIIiIi1iIII1 = OooOOOOo ( iIII1I111III )
   oo0O0oO = re . compile ( 'content="(.+?)">' ) . findall ( iIIiIi1iIII1 )
   for iIIIiIi in oo0O0oO :
    IIo0o0O0O00oOOo ( iIII1I111III )
    if 100 - 100: OOOo0 / OOooOOo % OoOoOO00 % Oo % Ii11I
    if 98 - 98: IiiIIi11I % i11iIiiIii % OOO0OOo + oOo00oOO0O
    if 78 - 78: ii11ii1ii % ii / O0O0O - iIii1I11I1II1
def ooooo0O0000oo ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 iIii1II11 = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OOoO00 , OooOo0ooo in iIii1II11 :
  print 'there ><><><><><><><><><><><><'
  OOoO00 = OOoO00
  oo0O0oO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OooOo0ooo ) )
  for IiI111111IIII , i1Ii in oo0O0oO :
   print 'here <><><><><><><><><><><><>'
   i1I1iI ( '[COLORred]' + OOoO00 + '[/COLOR] - ' + IiI111111IIII + ' - [COLORgreen]' + i1Ii + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 i1Iii1i1I = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OOoO00 , o00oo0 in i1Iii1i1I :
  print 'there ><><><><><><><><><><><><'
  OOoO00 = OOoO00
  oo0O0oO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o00oo0 ) )
  for IiI111111IIII , i1Ii in oo0O0oO :
   print 'here <><><><><><><><><><><><>'
   i1I1iI ( '[COLORred]' + OOoO00 + '[/COLOR] - ' + IiI111111IIII + ' - [COLORgreen]' + i1Ii + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
   if 38 - 38: OOO0OOo % OoOoOO00 % IiiIIi11I / Ooo00oOo00o + I1IiI / i1IIi
   if 54 - 54: iIii1I11I1II1 % ii11ii1ii - Ii11I / ii - Ooo00oOo00o . IiiIIi11I
   if 11 - 11: ii11ii1ii . Ooo00oOo00o * oo0Oo * OoooooooOO + OOO0OOo
def IiII111i1i11 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for i1Iii1i1I in i1Iii1i1I :
  IiI111111IIII = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
  for IiI111111IIII in IiI111111IIII :
   IiI111111IIII = ( IiI111111IIII ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1Iii1i1I ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  i111iIi1i1II1 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
  for i111iIi1i1II1 in i111iIi1i1II1 :
   i111iIi1i1II1 = 'http:' + i111iIi1i1II1
  OOoo0O ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i111iIi1i1II1 , '' , '' )
  if 86 - 86: iIii1I11I1II1 / I1IiI . OoOoOO00
  if 19 - 19: ii11ii1ii % OoooooooOO % oo0Oo * OOooOOo % O0
  if 67 - 67: OOOo0 . i1IIi
  if 27 - 27: OOO0OOo % OOOo0
def o0oooOO00 ( url ) :
 if 32 - 32: I1II11IiII
 Iii1 = [ ]
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for iIII1I111III , I111iI , IiI111111IIII , oOOOoo00 in oo0O0oO :
  IiI111111IIII = ( IiI111111IIII ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  iiIiIIIiiI = OooOOOOo ( iIII1I111III )
  iiI1IIIi = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iiIiIIIiiI )
  for II11IiIi11 , IIOOO0O00O0OOOO in iiI1IIIi :
   I1iiii1I = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( IIOOO0O00O0OOOO ) )
   for OOo0 in I1iiii1I :
    if IiI111111IIII in Iii1 :
     pass
    else :
     OOoo0O ( IiI111111IIII , II11IiIi11 , 8043 , I111iI , I111iI , OOo0 )
     oO0Oo ( 'movies' , 'INFO' )
     Iii1 . append ( IiI111111IIII )
     if 73 - 73: O0O0O
     if 42 - 42: i11iIiiIii * iIii1I11I1II1 / ii11ii1ii . i11iIiiIii % IiiIIi11I
def i1iI ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IiI1iiiIii )
 for url , I1i111I , OOo0 , OooOo0oo0O0o00O , IiI111111IIII in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 10065 , I1i111I , OooOo0oo0O0o00O , OOo0 )
 oO0Oo ( 'movies' , 'INFO' )
 if 48 - 48: OOO0OOo / I1II11IiII . iIii1I11I1II1 * I1IiI * ii / i1IIi
def OOOOoOOo0O0 ( ) :
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OO0O = 'https://www.youtube.com/results?search_query=' + ( oO0 ) . replace ( ' ' , '+' )
 OO = O0OO0O . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( OO )
 oo0O0oO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 in next :
  oOooo0 = 'https://www.youtube.com' + oOooo0
  i1I1iI ( '[COLORgreen] NEXT [/COLOR]' , oOooo0 , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for I111iI , oOooo0 , IiI111111IIII , ooO , IIOOO0O00O0OOOO in oo0O0oO :
  Ooo . append ( IiI111111IIII )
  oO0Oo ( 'tvshows' , 'INFO' )
  i111iIi1i1II1 = 'http:' + ( I111iI ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i111iIi1i1II1
  oOooo0 = 'http://www.youtube.com' + oOooo0
  OOoo0O ( '[COLORred]' + ooO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( oOooo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i111iIi1i1II1 , i111iIi1i1II1 , IIOOO0O00O0OOOO )
 else :
  oo0O0oO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for I111iI , oOooo0 , IiI111111IIII , ooO in oo0O0oO :
   print 'im doing it'
   oO0Oo ( 'tvshows' , 'INFO' )
   i111iIi1i1II1 = 'http:' + ( I111iI ) . replace ( 'https:' , '' )
   oOooo0 = 'http://www.youtube.com' + oOooo0
   if '&' in oOooo0 :
    print ' i got here'
    iIIiIi1iIII1 = OooOOOOo ( oOooo0 )
    i1Iii1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
    for i1Iii1i1I in i1Iii1i1I :
     IiI111111IIII = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
     for IiI111111IIII in IiI111111IIII :
      IiI111111IIII = ( IiI111111IIII ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     oOooo0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1Iii1i1I ) )
     for oOooo0 in oOooo0 :
      oOooo0 = 'https://www.youtube.com/w' + oOooo0
     i111iIi1i1II1 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
     for i111iIi1i1II1 in i111iIi1i1II1 :
      i111iIi1i1II1 = 'http:' + i111iIi1i1II1
     OOoo0O ( '[COLORred]' + ooO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( oOooo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i111iIi1i1II1 , i1iiIII111ii , '' )
   elif IiI111111IIII in Ooo :
    pass
   elif 'user' in oOooo0 or 'elete' in IiI111111IIII :
    pass
   elif 'hannel' in oOooo0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oOooo0
    iIIiIi1iIII1 = OooOOOOo ( oOooo0 )
    o0o00OOo0 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
    for I111iI , oOooo0 , IiI111111IIII in o0o00OOo0 :
     if 'outube' in oOooo0 or 'list' in oOooo0 :
      pass
     elif 'atch' in oOooo0 :
      oOooo0 = ( oOooo0 ) . replace ( '/watch?v=' , '' )
      OOoo0O ( '[COLORred]' + ooO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( oOooo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I111iI , 'http:' + I111iI , '' )
     else :
      pass
   else :
    OOoo0O ( '[COLORred]' + ooO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( oOooo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i111iIi1i1II1 , i111iIi1i1II1 , '' )
    if 17 - 17: I1II11IiII + ii - i11iIiiIii . I1II11IiII * Ii11I
def oo0oOOO0OOOo ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( iIIiIi1iIII1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  i1I1iI ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for I111iI , url , IiI111111IIII , ooO , IIOOO0O00O0OOOO in oo0O0oO :
  Ooo . append ( IiI111111IIII )
  oO0Oo ( 'tvshows' , 'INFO' )
  i111iIi1i1II1 = 'http:' + ( I111iI ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i111iIi1i1II1
  url = 'http://www.youtube.com' + url
  OOoo0O ( '[COLORred]' + ooO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i111iIi1i1II1 , i111iIi1i1II1 , IIOOO0O00O0OOOO )
 else :
  oo0O0oO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for I111iI , url , IiI111111IIII , ooO in oo0O0oO :
   oO0Oo ( 'tvshows' , 'INFO' )
   i111iIi1i1II1 = 'http:' + ( I111iI ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    iIIiIi1iIII1 = OooOOOOo ( url )
    i1Iii1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
    for i1Iii1i1I in i1Iii1i1I :
     IiI111111IIII = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
     for IiI111111IIII in IiI111111IIII :
      IiI111111IIII = ( IiI111111IIII ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1Iii1i1I ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     i111iIi1i1II1 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
     for i111iIi1i1II1 in i111iIi1i1II1 :
      i111iIi1i1II1 = 'http:' + i111iIi1i1II1
     OOoo0O ( '[COLORred]' + ooO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i111iIi1i1II1 , i1iiIII111ii , '' )
   elif IiI111111IIII in Ooo :
    pass
   elif 'user' in url or 'elete' in IiI111111IIII :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    iIIiIi1iIII1 = OooOOOOo ( url )
    o0o00OOo0 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
    for I111iI , url , IiI111111IIII in o0o00OOo0 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOoo0O ( '[COLORred]' + ooO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I111iI , 'http:' + I111iI , '' )
     else :
      pass
   else :
    OOoo0O ( '[COLORred]' + ooO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i111iIi1i1II1 , i111iIi1i1II1 , '' )
    if 56 - 56: OOooOOo
    if 28 - 28: O0O0O . O0O0O % iIii1I11I1II1 * iIii1I11I1II1 . OOooOOo / O0O0O
def iII1i1 ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  O0oOOoooOO0O = open ( o0 )
  oo0O0oO = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( O0oOOoooOO0O ) )
  for ooo00Ooo , Oo0o0O00 in oo0O0oO :
   if ooo00Ooo == 'needs replacing' or Oo0o0O00 == 'needs replacing' :
    ii1 ( )
  i1I1iI ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelist.m3u' , 7080 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 39 - 39: oOo00oOO0O / OOO0OOo . OOooOOo % O0 * O0O0O + OOOo0
def O0oo0O ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 i1iiIIiiI111 . ok ( '[COLOR=red]Reset Any Previous linked streams[/COLOR]' , 'For best results you\'ll need to clear previous linked streams' , 'Go to TVGuide tab then reset database at the bottom' , 'Then go back and guide should be all linked up and ready to go' )
 o0oO0 . openSettings ( sys . argv [ 0 ] )
 ii1 ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 36 - 36: Ii11I + O0 - oOo00oOO0O - O0 % IiiIIi11I . ii
def ooo ( ) :
 try :
  iiI = gui . TVGuide ( )
  iiI . doModal ( )
  del iiI
  if 56 - 56: Oo . ii11ii1ii . OOOo0
 except :
  import sys
  import traceback as tb
  ( ii111I , iiIiIiiiII , traceback ) = sys . exc_info ( )
  tb . print_exception ( ii111I , iiIiIiiiII , traceback )
  if 20 - 20: OOOo0
def o0oO000oo ( ) :
 i1I1iI ( 'Full Backup' , '' , 10061 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( oOoOooOo0o0 ) :
  i1I1iI ( 'Backup Genie Favourites' , oOooo0 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  i1I1iI ( 'Backup Ivue Config' , IIiiiiiiIi1I1 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( I1IIIii ) :
  i1I1iI ( 'Backup Kodi Favourites' , I1IIIii , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 95 - 95: OOO0OOo / OOO0OOo
  if 30 - 30: ii11ii1ii + Oo / Oo % ii11ii1ii . ii11ii1ii
  if 55 - 55: OOO0OOo - IiiIIi11I + OoOoOO00 + O0O0O % oOo00oOO0O
zip = o0oO0 . getSetting ( 'zip' )
iiI11i1II = xbmc . translatePath ( os . path . join ( zip ) )
def OO0O0OOo0O ( ) :
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 78 - 78: OOOo0 - iIii1I11I1II1 . OOO0OOo + iIii1I11I1II1
  if 95 - 95: OOOo0
  if 46 - 46: I1IiI + Ooo00oOo00o
def o0o0O ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = oOoOooOo0o0
  elif 'Ivue' in name :
   url = IIiiiiiiIi1I1
  elif 'Kodi' in name :
   url = I1IIIii
  OO0O0OOo0O ( )
  ooooO0oOoOOoO = open ( url ) . read ( )
  I1i11i = os . path . join ( iiI11i1II , description . split ( 'Your ' ) [ 1 ] )
  IiIi = open ( I1i11i , mode = 'w' )
  IiIi . write ( ooooO0oOoOOoO )
  IiIi . close ( )
 else :
  if 'guisettings.xml' in description :
   OOOOO0O00 = open ( os . path . join ( iiI11i1II , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Iii = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   oo0O0oO = re . compile ( Iii ) . findall ( OOOOO0O00 )
   for type , iIIiIiI1I1 , ooOii in oo0O0oO :
    ooOii = ooOii . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , iIIiIiI1I1 , ooOii ) )
  else :
   I1i11i = os . path . join ( url )
   ooooO0oOoOOoO = open ( os . path . join ( iiI11i1II , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiIi = open ( I1i11i , mode = 'w' )
   IiIi . write ( ooooO0oOoOOoO )
   IiIi . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 82 - 82: I1IiI - Ooo00oOo00o % I1IiI * i11iIiiIii . OoOoOO00 % OoOoOO00
 if 54 - 54: IiiIIi11I + oOo00oOO0O
 if 55 - 55: iIii1I11I1II1
 if 78 - 78: O0O0O + IiiIIi11I . OOO0OOo - O0O0O . oOo00oOO0O
def II1I11i ( ) :
 O0Oooo = 1
 OO0O0OOo0O ( )
 iiIi1i = xbmc . translatePath ( os . path . join ( iiI11i1II , 'Build Backup' , 'Full Backup' , '' ) )
 I1i11111i1i11 = xbmc . translatePath ( os . path . join ( iiI11i1II , 'Build Backup' , 'my_full_backup.zip' ) )
 OOoOOO0 = xbmc . translatePath ( os . path . join ( iiI11i1II , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iiIi1i ) :
  os . makedirs ( iiIi1i )
 I1I1i = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not I1I1i ) : return False , 0
 I1IIIiIiIi = I1I1i
 IIIII1 = xbmc . translatePath ( os . path . join ( iiIi1i , I1IIIiIiIi + '.zip' ) )
 iIi1Ii1i1iI = [ 'plugin.video.GenieTv' ]
 IIiI1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 i1iI1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 ii1I1IiiI1ii1i = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 O0o = "Creating full backup of existing build"
 oO0OoO00o = "Creating Community Build"
 II1iiiiII = "Archiving..."
 O0OoOO0oo0 = ""
 oOO = "Please Wait"
 O0o0OO0000ooo ( oooOOOOO , IIIII1 , oO0OoO00o , II1iiiiII , O0OoOO0oo0 , oOO , i1iI1 , ii1I1IiiI1ii1i )
 time . sleep ( 1 )
 iIIII1iIIii = xbmc . translatePath ( os . path . join ( iiIi1i , I1IIIiIiIi + '_guisettings.zip' ) )
 oOOO00o000o = zipfile . ZipFile ( iIIII1iIIii , mode = 'w' )
 try :
  oOOO00o000o . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oOOO00o000o . close ( )
 if O0Oooo == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I1i11111i1i11 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + IIIII1 + '[/COLOR]' )
  if 9 - 9: ii + IiiIIi11I / IiiIIi11I
def O0o0OO0000ooo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 Ii1I11ii1i = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 O0iIiIIIIIii = len ( sourcefile )
 OOo0ii11I1 = [ ]
 oO0oo = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for Ii111iIi1iIi , IIIIIo0ooOoO000oO , OOo in os . walk ( sourcefile ) :
  for file in OOo :
   oO0oo . append ( file )
 i1i11I1I1iii1 = len ( oO0oo )
 for Ii111iIi1iIi , IIIIIo0ooOoO000oO , OOo in os . walk ( sourcefile ) :
  IIIIIo0ooOoO000oO [ : ] = [ I1iii11 for I1iii11 in IIIIIo0ooOoO000oO if I1iii11 not in exclude_dirs ]
  OOo [ : ] = [ IiIi for IiIi in OOo if IiIi not in exclude_files ]
  for file in OOo :
   OOo0ii11I1 . append ( file )
   ooo0O = len ( OOo0ii11I1 ) / float ( i1i11I1I1iii1 ) * 100
   Oo0oO0ooo . update ( int ( ooo0O ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iII1iii = os . path . join ( Ii111iIi1iIi , file )
   if not 'temp' in IIIIIo0ooOoO000oO :
    if not 'plugin.program.originwizard' in IIIIIo0ooOoO000oO :
     import time
     i11i1iiiII = '01/01/1980'
     ooOO0oO0oo00o = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iII1iii ) ) )
     if ooOO0oO0oo00o > i11i1iiiII :
      Ii1I11ii1i . write ( iII1iii , iII1iii [ O0iIiIIIIIii : ] )
 Ii1I11ii1i . close ( )
 Oo0oO0ooo . close ( )
 if 83 - 83: ii - OoOoOO00 - O0O0O
 if 3 - 3: I1II11IiII
def i1iiIiI1Ii1i ( ) :
 i1I1iI ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if 22 - 22: oo0Oo / i11iIiiIii
 if 62 - 62: Ooo00oOo00o / ii11ii1ii
def ii1O000OOO0OOo ( ) :
 i1I1iI ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 32 - 32: oOo00oOO0O * O0
 if 100 - 100: OOO0OOo % iIii1I11I1II1 * OoOoOO00 - O0O0O
 if 92 - 92: OOO0OOo
 if 22 - 22: Oo % O0O0O * ii11ii1ii / Ii11I % i11iIiiIii * IiiIIi11I
def Oo00OoOo ( ) :
 i1I1iI ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , ii11iIi1I + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  i1I1iI ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ii11iIi1I + 'concerts.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ii11iIi1I + 'kodible.png' , i1iiIII111ii , '' )
 if 24 - 24: i11iIiiIii - I1II11IiII
 oO0Oo ( 'movies' , 'MAIN' )
 if 21 - 21: IiiIIi11I
def OoO00 ( ) :
 if 85 - 85: Oo * Oo * OOOo0 . OoooooooOO . oOo00oOO0O * OOO0OOo
 OOoo0O ( 'DELETE CACHE' , 'url' , 14 , ii11iIi1I + 'MAIN5.png' , i1iiIII111ii , '' )
 OOoo0O ( 'DELETE PACKAGES' , 'url' , 6 , ii11iIi1I + 'MAIN4.png' , i1iiIII111ii , '' )
 OOoo0O ( 'FORCE REFRESH' , 'url' , 10 , ii11iIi1I + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 65 - 65: Ii11I * I1II11IiII
 OOoo0O ( 'CHECK MY IP' , 'url' , 12 , ii11iIi1I + 'MAIN2.png' , i1iiIII111ii , '' )
 OOoo0O ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ii11iIi1I + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 i1I1iI ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , ii11iIi1I + 'URLFIX.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
 if 79 - 79: OoooooooOO - OOOo0
 if 69 - 69: IiiIIi11I
def iI1Ii11111iIi ( ) :
 i1I1iI ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ii11iIi1I + 'repos.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , ii11iIi1I + 'NEW.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , ii11iIi1I + 'IPTV.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , ii11iIi1I + 'VIDEO.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , ii11iIi1I + 'SPORTS.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , ii11iIi1I + 'KIDS.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , ii11iIi1I + 'PROGRAMS.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ii11iIi1I + 'XXX.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
 if 95 - 95: OOO0OOo + i11iIiiIii * I1II11IiII - i1IIi * I1II11IiII - iIii1I11I1II1
 if 75 - 75: OoooooooOO * oo0Oo
def I1Iiiiiii ( ) :
 OOoo0O ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 OOoo0O ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 OOoo0O ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 OOoo0O ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 OOoo0O ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 OOoo0O ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 OOoo0O ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 OOoo0O ( 'DELETE XML' , iiI1IiI , 11 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
 if 39 - 39: oo0Oo * Oo + iIii1I11I1II1 - oo0Oo + Ii11I
def o0iiiI1I1iIIIi1 ( ) :
 OOoo0O ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 OOoo0O ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / IiiIIi11I % OoOoOO00 % i1IIi / i11iIiiIii
def OOO ( ) :
 OOoo0O ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , ii11iIi1I + 'FTV4.png' , i1iiIII111ii , '' )
 OOoo0O ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , ii11iIi1I + 'FTV3.png' , i1iiIII111ii , '' )
 OOoo0O ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ii11iIi1I + 'FTV1.png' , i1iiIII111ii , '' )
 OOoo0O ( 'RESET FTV DATABASE' , 'url' , 18 , ii11iIi1I + 'FTV2.png' , i1iiIII111ii , '' )
 if 30 - 30: OoooooooOO - OoooooooOO . O0 / O0O0O
 if 31 - 31: Ii11I + OOooOOo . OoooooooOO
 if 89 - 89: OoOoOO00 + i1IIi + OoOoOO00
def IiII1II11I ( ) :
 i1I1iI ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , ii11iIi1I + 'skinp.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , ii11iIi1I + 'artp.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ii11iIi1I + 'GUI.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
 if 54 - 54: oo0Oo + O0 + IiiIIi11I * I1II11IiII - Ii11I % ii
def I111 ( url ) :
 iI1I1i11iIIii = OooOOOOo ( IIIIIiI111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 5 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 11 - 11: OOOo0 - Ooo00oOo00o
def iiiiI1i1i ( ) :
 i1I1iI ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , ii11iIi1I + 'GSKIN.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , ii11iIi1I + 'HSKIN.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ii11iIi1I + 'ISKIN.png' , i1iiIII111ii , '' )
 oO0Oo ( 'movies' , 'MAIN' )
 if 24 - 24: oo0Oo * O0O0O . OoOoOO00 / Ii11I + O0
def oO0oOOoo00000 ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + oOo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 3 - 3: O0O0O % i1IIi
def Ii1IIiiIIi ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + Oo000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 39 - 39: ii11ii1ii
def O0oOo00o0 ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + OooOOOOoO00OoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 85 - 85: ii - iIii1I11I1II1 / O0
def Oo00oo0000OO ( url ) :
 iI1I1i11iIIii = OooOOOOo ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 69 - 69: OOO0OOo - Ooo00oOo00o / i11iIiiIii + ii11ii1ii % OoooooooOO
def o000O000 ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + ii1oOoO0o0ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 40 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 86 - 86: ii11ii1ii * O0 * oo0Oo
def Ooo0oo ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + IIi11IIiIii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 5 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 17 - 17: oOo00oOO0O + ii . Ooo00oOo00o - Oo * i11iIiiIii
def iioOo0OoOOo0 ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1iiiIii )
 for oOooo0 , i111iIi1i1II1 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , oOooo0 , 2031 , i111iIi1i1II1 )
  if 92 - 92: IiiIIi11I / IiiIIi11I . ii11ii1ii
def ii1iIi1II ( name , url , description ) :
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( IIIIi1I , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 IiIi1i1ii = os . path . join ( I1o0OooOOOOOO , name + '.apk' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 11 - 11: OoOoOO00 / OOooOOo
def IiIi1 ( url ) :
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 IiIi1i1ii = os . path . join ( I1o0OooOOOOOO , IiI111111IIII + '.mp4' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 34 - 34: Ii11I
 if 91 - 91: iIii1I11I1II1 % OOooOOo . iIii1I11I1II1 % i1IIi / OoOoOO00 * I1IiI
def iioo0o0OoOOO ( name , url , description ) :
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 IiIi1i1ii = os . path . join ( I1o0OooOOOOOO , name )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 ooO0oO00O0o = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print ooO0oO00O0o
 print '======================================='
 extract . all ( IiIi1i1ii , ooO0oO00O0o , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 70 - 70: I1II11IiII
 if 16 - 16: O0O0O - OoooooooOO % Oo
def i11i1iIiii ( url ) :
 iI1I1i11iIIii = OooOOOOo ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 5 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 try :
  iI1I1i11iIIii = OooOOOOo ( OOO00OO0oOo + oO0o0o0ooO0oO + I1I1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
  for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
   i1I1iI ( IiI111111IIII , url , 5 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 except : pass
 oO0Oo ( 'movies' , 'INFO' )
 if 16 - 16: oo0Oo * I1IiI . OOO0OOo / i1IIi . Ooo00oOo00o - i1IIi
 if 46 - 46: oo0Oo + iIii1I11I1II1 + Ii11I + Ooo00oOo00o . ii11ii1ii
def iIiIi11Ii ( url ) :
 iI1I1i11iIIii = OooOOOOo ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 43 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 try :
  iI1I1i11iIIii = OooOOOOo ( OOO00OO0oOo + oO0o0o0ooO0oO + I1I1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
  for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
   i1I1iI ( IiI111111IIII , url , 43 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 except : pass
 oO0Oo ( 'movies' , 'INFO' )
 if 23 - 23: ii - Ii11I + IiiIIi11I
 if 12 - 12: OOOo0 / OOO0OOo % OOooOOo / i11iIiiIii % OoooooooOO
def IiIi1II11i ( name , url , description ) :
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 IiIi1i1ii = os . path . join ( I1o0OooOOOOOO , name + '.zip' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II1II1iIIi11
 print '======================================='
 extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OOooOoooOoOo ( )
 if 49 - 49: OoooooooOO * IiiIIi11I - Oo . ii
 if 89 - 89: OOO0OOo + oOo00oOO0O * OOO0OOo / OOO0OOo
def i11i11 ( name , url , description ) :
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IiIi1i1ii = os . path . join ( I1o0OooOOOOOO , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II1II1iIIi11
 print '======================================='
 extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OoOoO00O0 ( )
 if 51 - 51: iIii1I11I1II1 / I1IiI + Ii11I - IiiIIi11I + O0O0O
def IIii1i1iii1 ( name , url , description ) :
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IiIi1i1ii = os . path . join ( I1o0OooOOOOOO , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II1II1iIIi11
 print '======================================='
 extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 70 - 70: i11iIiiIii % O0O0O
 if 11 - 11: oo0Oo % ii11ii1ii % oOo00oOO0O / OoOoOO00 % I1II11IiII - Oo
def OOooO ( name , url , description ) :
 II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 IiIi1i1ii = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print II1II1iIIi11
 print '======================================='
 extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 79 - 79: I1II11IiII % ii % OOooOOo % oOo00oOO0O - OoOoOO00 * OoooooooOO
 if 69 - 69: OOooOOo / Oo
def OoOoO00O0 ( ) :
 IIi = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if IIi == 0 :
  return
 elif IIi == 1 :
  pass
 IiiIIIII1iii = IIiiii ( )
 print "Platform: " + str ( IiiIIIII1iii )
 if IiiIIIII1iii == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IiiIIIII1iii == 'linux' :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IiiIIIII1iii == 'android' :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
 elif IiiIIIII1iii == 'windows' :
  print "############   try windows force close  #################"
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill XBMC.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill Kodi.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im Kodi.exe /f' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im XBMC.exe /f' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
  if 37 - 37: OOooOOo % OOO0OOo
def IIiiii ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) :
  return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) :
  return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) :
  return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) :
  return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) :
  return 'ios'
  if 83 - 83: Ii11I . I1II11IiII + ii - Ii11I * I1II11IiII / I1II11IiII
  if 39 - 39: I1II11IiII / Oo % Ooo00oOo00o % i11iIiiIii
  if 90 - 90: I1II11IiII - OoooooooOO
def OoOOoO000O00oO ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( url ) :
  for file in OOo :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    OOOOO0O00 = open ( ( os . path . join ( i1OoOO , file ) ) ) . read ( )
    iIII1I1i1i = OOOOO0O00 . replace ( oooOOOOO , 'special://home/' )
    IiIi = open ( ( os . path . join ( i1OoOO , file ) ) , mode = 'w' )
    IiIi . write ( str ( iIII1I1i1i ) )
    IiIi . close ( )
 OoOoO00O0 ( )
 if 79 - 79: oOo00oOO0O . Ooo00oOo00o
def IIiI1I1 ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 oo0O0oO = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( IiI1iiiIii )
 for IiI111111IIII , oOooo0 in oo0O0oO :
  I11I1IIiiII1 ( IiI111111IIII , oOooo0 , 222 , ii11iIi1I + 'radio.png' )
  if 31 - 31: OOOo0 * ii + OoooooooOO - O0O0O / OoooooooOO
def I111IIiii1Ii ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.toonjet.com/' + oOooo0 , 8051 , ii11iIi1I + 'classictoons.png' )
def II1 ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( IiI1iiiIii )
 for url , I111iI in oo0O0oO :
  if 'ol.gif' in I111iI :
   pass
  elif 'link_block_' in I111iI :
   pass
  elif '.png' in I111iI :
   pass
  else :
   iII11I1Ii1 ( ( I111iI ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ii11iIi1I + 'vod.png' )
 for url in iiI1IIIi :
  iII11I1Ii1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ii11iIi1I + 'Next.png' )
def iiIIIiIii ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  I11I1IIiiII1 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ii11iIi1I + 'classictoons.png' )
  if 23 - 23: O0O0O + IiiIIi11I . I1IiI * OOOo0 + ii11ii1ii
  if 18 - 18: oo0Oo * OOooOOo . oo0Oo / O0
def iiIII1II ( ) :
 oOo00oOOOOO ( 'Audio Books' , '' , 30011 , ii11iIi1I + 'audiobooks.png' , ii11iIi1I + 'audiobooks.png' , '' )
 oOo00oOOOOO ( 'Kids Audio Books' , '' , 30006 , ii11iIi1I + 'kidsaudiobooks.png' , ii11iIi1I + 'kidsaudiobooks.png' , '' )
 if 85 - 85: OoooooooOO - Ooo00oOo00o - I1II11IiII / OOO0OOo - IiiIIi11I
def iIiI ( ) :
 oOo00oOOOOO ( 'All' , '' , 30001 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 oOo00oOOOOO ( 'Popular' , '' , 30012 , ii11iIi1I + 'POPULARv.png' , ii11iIi1I + 'POPULARv.png' , '' )
 oOo00oOOOOO ( 'Search' , '' , 30013 , ii11iIi1I + 'search.png' , ii11iIi1I + 'search.png' , '' )
 if 5 - 5: Oo * I1IiI
def ii1I11iIiIII1 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( OO0o + 'books' + II11iiii1Ii )
 oo0O0oO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , oOooo0 , oOO0OOOOoooO in oo0O0oO :
  if 'Parent' in IiI111111IIII :
   pass
  elif '2' in oOO0OOOOoooO :
   oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooo0 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 22 - 22: IiiIIi11I + iIii1I11I1II1
def IIIii1iiIi ( ) :
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( OO0o + 'books' + II11iiii1Ii )
 oo0O0oO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , oOooo0 , oOO0OOOOoooO in oo0O0oO :
  if oO0 in IiI111111IIII . lower ( ) :
   if '1' in oOO0OOOOoooO :
    oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooo0 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '2' in oOO0OOOOoooO :
    oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooo0 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '3' in oOO0OOOOoooO :
    oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooo0 , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 63 - 63: ii11ii1ii
    if 6 - 6: OOO0OOo / ii11ii1ii
def oOooO00o0O ( ) :
 iIIiIi1iIII1 = OooOOOOo ( OO0o + 'books' + II11iiii1Ii )
 oo0O0oO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , oOooo0 , oOO0OOOOoooO in oo0O0oO :
  if '1' in oOO0OOOOoooO :
   oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooo0 , 3010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '2' in oOO0OOOOoooO :
   oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooo0 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '3' in oOO0OOOOoooO :
   oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooo0 , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 80 - 80: Ii11I / IiiIIi11I / I1IiI + i1IIi - Oo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11: OOooOOo * Ooo00oOo00o
def iIi1IiI ( url ) :
 iIII1I111III = url
 iIIiIi1iIII1 = OooOOOOo ( url )
 iiI1IIIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in iiI1IIIi :
  if 'mp3' in IiI111111IIII :
   i1I1iI ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) , iIII1I111III + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'wma' in IiI111111IIII :
   i1I1iI ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) , iIII1I111III + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'm4b' in IiI111111IIII :
   i1I1iI ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) , iIII1I111III + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '/' in IiI111111IIII :
   oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIII1I111III + url , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 14 - 14: oo0Oo % ii % Oo - i11iIiiIii
   if 53 - 53: oOo00oOO0O % Oo
   if 59 - 59: Ii11I % iIii1I11I1II1 . i1IIi + OoOoOO00 * oo0Oo
def i1IiiI1iIi ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 iIII1I111III = url
 oo0O0oO = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  if 'Parent' in IiI111111IIII :
   pass
  elif '.db' in IiI111111IIII :
   pass
  elif '.jpg' in IiI111111IIII :
   pass
  elif '.html' in IiI111111IIII :
   pass
  elif '.doc' in IiI111111IIII :
   pass
  elif 'mp3' in IiI111111IIII :
   i1I1iI ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIII1I111III + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif 'm4a' in IiI111111IIII :
   i1I1iI ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIII1I111III + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIII1I111III + url , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 66 - 66: Ooo00oOo00o * Oo
   if 28 - 28: Ooo00oOo00o % I1IiI % ii11ii1ii + OOOo0 / OOOo0
def OO0O0ooOOO00 ( ) :
 oOo00oOOOOO ( 'A-Z' , '' , 7 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 oOo00oOOOOO ( 'All' , '' , 3 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 oOo00oOOOOO ( 'Search' , '' , 14 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 if 17 - 17: O0 . I1II11IiII . O0 + O0 / Oo . OOO0OOo
def OO00OOoO0o ( ) :
 iIIiIi1iIII1 = OooOOOOo ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 oo0O0oO = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , I111iI in oo0O0oO :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oOooo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in I111iI :
   pass
  else :
   oOo00oOOOOO ( I111iI , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oOooo0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + I111iI + '.gif' , ii11iIi1I + 'kodible.png' , '' )
   if 4 - 4: i1IIi - i11iIiiIii / i11iIiiIii / OoooooooOO
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 100 - 100: Oo + OOooOOo - O0 % OoOoOO00 . O0O0O
 if 92 - 92: OoOoOO00 * OoooooooOO - I1II11IiII
def oooo00 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  if '</a>' in IiI111111IIII :
   pass
  elif '(' in IiI111111IIII :
   oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   i1I1iI ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 96 - 96: ii11ii1ii % OOO0OOo % oOo00oOO0O - OOO0OOo % I1IiI + ii11ii1ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: O0
def Ooo0Oo0oo0 ( ) :
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 oo0O0oO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if oO0 in IiI111111IIII . lower ( ) :
   if '</a>' in IiI111111IIII :
    pass
   elif '(' in IiI111111IIII :
    oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooo0 , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   else :
    i1I1iI ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooo0 , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 83 - 83: I1II11IiII
    if 48 - 48: OoOoOO00 * Ii11I * I1II11IiII
def i1iiiIii11 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 oo0O0oO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if '</a>' in IiI111111IIII :
   pass
  elif '(' in IiI111111IIII :
   oOo00oOOOOO ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooo0 , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   i1I1iI ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooo0 , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 67 - 67: OOooOOo % I1IiI . I1IiI - OOO0OOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: OOO0OOo + OoOoOO00 * ii11ii1ii / oOo00oOO0O . OOooOOo + OOooOOo
 if 40 - 40: OOO0OOo / I1IiI % i11iIiiIii % ii11ii1ii / OOOo0
def ooOOOOo0 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  iIII1I111III = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( iIII1I111III )
  if 38 - 38: OoooooooOO / ii11ii1ii . O0 / i1IIi / Oo + iIii1I11I1II1
def ooO00O00oOO ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , url in oo0O0oO :
  if '<p align' in IiI111111IIII :
   pass
  elif '&nbsp;' in IiI111111IIII :
   pass
  else :
   i1I1iI ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 40 - 40: O0O0O . ii + OOOo0 + ii11ii1ii + I1II11IiII
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: iIii1I11I1II1
 if 87 - 87: ii11ii1ii / OoooooooOO - Oo % I1IiI % oo0Oo % Oo
def Ii1 ( ) :
 iIIiIi1iIII1 = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 oo0O0oO = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if 'ongoing' in oOooo0 :
   i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 21005 , ii11iIi1I + 'on-going.png' , '' , '' )
  if 'cartoon-series' in oOooo0 :
   i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 21005 , ii11iIi1I + 'cartoonseries.png' , '' , '' )
  if 'disney' in oOooo0 :
   i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 21005 , ii11iIi1I + 'disneytoons.png' , '' , '' )
  if 'genre' in oOooo0 :
   i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 21005 , ii11iIi1I + 'cartoongenre.png' , '' , '' )
  if 'years' in oOooo0 :
   i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 21005 , ii11iIi1I + 'years.png' , '' , '' )
def I1iiiiii ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 o0OO0Oo = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , I111iI in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 21006 , I111iI , I111iI , IiI111111IIII )
 for url , IiI111111IIII in o0OO0Oo :
  i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in next :
  i1I1iI ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ii11iIi1I + 'Next.png' , '' , '' )
def I11iiii1I ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 iiiiI1iiiIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 o0oO0OoO0 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIIiIi1iIII1 )
 oOOOOOoOO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 21007 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in o0oO0OoO0 :
  i1I1iI ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url , IiI111111IIII in iiiiI1iiiIi :
  OOoo0O ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 else :
  i1I1iI ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
def oooo00i1 ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  OOoo0O ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
  if 95 - 95: Ooo00oOo00o . i1IIi / i11iIiiIii
def iIi1IIiI ( ) :
 iII11I1Ii1 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 iII11I1Ii1 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 24 - 24: O0O0O * OoOoOO00 % O0O0O % oo0Oo + OoooooooOO
def IiIiiiIii ( ) :
 iII11I1Ii1 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ii11iIi1I + 'ORIGINCARTOON.png' )
 iII11I1Ii1 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 27 - 27: i1IIi % I1IiI . OOOo0 + OOO0OOo % I1IiI
def o0o0oOo000o0 ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  if '?c=' in url :
   iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 25 - 25: IiiIIi11I + I1IiI . OOooOOo % I1IiI * Ii11I
def ii1IiIi11 ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , iiiii1ii1 , IiI111111IIII in oo0O0oO :
  if 'Genre' in url :
   iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 48 - 48: O0 + O0 . I1II11IiII - OOO0OOo
def o00oo0000 ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , iiiii1ii1 , IiI111111IIII in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , iiiii1ii1 )
  if 44 - 44: Oo % iIii1I11I1II1
def oo0ooO0 ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , iiiii1ii1 , IiI111111IIII in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , iiiii1ii1 )
  if 28 - 28: ii11ii1ii * OoooooooOO . OoOoOO00 / i11iIiiIii + ii
  if 38 - 38: oo0Oo . oOo00oOO0O
  if 24 - 24: OOooOOo - OOooOOo + ii11ii1ii + OOOo0 - ii
  if 12 - 12: O0O0O . oo0Oo . I1IiI / O0
  if 58 - 58: OOooOOo - OoOoOO00 % ii + I1II11IiII . I1IiI / oo0Oo
def IIo00ooo ( ) :
 if 31 - 31: O0 * OOooOOo % OOooOOo / ii / IiiIIi11I / Ooo00oOo00o
 i1I1iI ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 11 - 11: I1IiI + oo0Oo - OoooooooOO / Ooo00oOo00o
def iIIi1iI1I1IIi ( ) :
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 oo0O0oO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if oO0 in IiI111111IIII . lower ( ) :
   if 'Dad!' in IiI111111IIII :
    pass
   elif 'Family Guy' in IiI111111IIII :
    pass
   elif '2 Stupid' in IiI111111IIII :
    pass
   elif 'The Zelfs' in IiI111111IIII :
    pass
   elif 'A Clone' in IiI111111IIII :
    pass
   elif 'A.T.O.M' in IiI111111IIII :
    pass
   elif 'Almost Naked' in IiI111111IIII :
    pass
   elif 'Angry Kid' in IiI111111IIII :
    pass
   elif 'Annoying Orange' in IiI111111IIII :
    pass
   elif 'Aqua Teen' in IiI111111IIII :
    pass
   elif 'Assy Mcgee' in IiI111111IIII :
    pass
   elif 'Astroblast' in IiI111111IIII :
    pass
   elif 'Atomic Betty' in IiI111111IIII :
    pass
   elif 'Axe Cop' in IiI111111IIII :
    pass
   elif 'Baby Playpen' in IiI111111IIII :
    pass
   elif 'Beavis and Butt' in IiI111111IIII :
    pass
   elif 'Celebrity Deathmatch' in IiI111111IIII :
    pass
   elif 'Clerks The' in IiI111111IIII :
    pass
   elif 'Crapston Villas' in IiI111111IIII :
    pass
   elif 'Duckman:' in IiI111111IIII :
    pass
   elif 'Stripperella' in IiI111111IIII :
    pass
   elif 'Vixen' in IiI111111IIII :
    pass
   else :
    i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: OOO0OOo / Oo + OOO0OOo % OOooOOo - OOOo0 * OOOo0
def I1oO0ooOoO ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  if 'Dad!' in IiI111111IIII :
   pass
  elif 'Family Guy' in IiI111111IIII :
   pass
  elif '2 Stupid' in IiI111111IIII :
   pass
  elif 'The Zelfs' in IiI111111IIII :
   pass
  elif 'A Clone' in IiI111111IIII :
   pass
  elif 'A.T.O.M' in IiI111111IIII :
   pass
  elif 'Almost Naked' in IiI111111IIII :
   pass
  elif 'Angry Kid' in IiI111111IIII :
   pass
  elif 'Annoying Orange' in IiI111111IIII :
   pass
  elif 'Aqua Teen' in IiI111111IIII :
   pass
  elif 'Assy Mcgee' in IiI111111IIII :
   pass
  elif 'Astroblast' in IiI111111IIII :
   pass
  elif 'Atomic Betty' in IiI111111IIII :
   pass
  elif 'Axe Cop' in IiI111111IIII :
   pass
  elif 'Baby Playpen' in IiI111111IIII :
   pass
  elif 'Beavis and Butt' in IiI111111IIII :
   pass
  elif 'Celebrity Deathmatch' in IiI111111IIII :
   pass
  elif 'Clerks The' in IiI111111IIII :
   pass
  elif 'Crapston Villas' in IiI111111IIII :
   pass
  elif 'Duckman:' in IiI111111IIII :
   pass
  elif 'Stripperella' in IiI111111IIII :
   pass
  elif 'Vixen' in IiI111111IIII :
   pass
  else :
   i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: O0 % Oo
def O0o00O0Oo0 ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 iiI1IIIi = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IiI1iiiIii )
 for I111iI in iiI1IIIi :
  o0I11iII = I111iI
 IiiIiI = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( IiI1iiiIii )
 for url in IiiIiI :
  i1I1iI ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 oo0O0oO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 10007 , o0I11iII )
  if 23 - 23: IiiIIi11I
  if 40 - 40: OOooOOo - OoOoOO00 / Oo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: ii11ii1ii
def iI1 ( url , IMAGE ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( IiI1iiiIii )
 for IiI111111IIII , url in oo0O0oO :
  print IiI111111IIII + '     ' + url
  if 'easy' in url :
   iIIiI1ii ( url )
   if 78 - 78: O0 * Ii11I
   if 43 - 43: ii11ii1ii / OOOo0 . OOO0OOo
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 62 - 62: iIii1I11I1II1 + O0O0O . Oo / oo0Oo % O0 . I1II11IiII
def iIIiI1ii ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( "url: '(.+?)'," ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  Oo0oOooOoOo ( url )
  if 49 - 49: Ii11I . ii11ii1ii . i11iIiiIii - OoOoOO00 / oOo00oOO0O
  if 62 - 62: Ii11I
  if 1 - 1: oo0Oo / oo0Oo - i11iIiiIii
def OO0oIiII1iiI ( ) :
 if 34 - 34: OOOo0 . ii + i1IIi
 i1I1iI ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 98 - 98: ii % oo0Oo * i11iIiiIii % ii11ii1ii
def iIiI1IIiii11 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , I111iI , IiI111111IIII in oo0O0oO :
  if 'elete' in IiI111111IIII :
   pass
  else :
   I11I1IIiiII1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 222 , I111iI )
   if 33 - 33: iIii1I11I1II1 / O0O0O - OOOo0 * IiiIIi11I
def o0o00oO0oo000 ( ) :
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oO000o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , o0Oo , iIiiiI1IiI1I1 in oO000o :
  for oO0 in o0Oo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   o0O0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for oOooo0 , IiI111111IIII in o0O0 :
    if 'tube' in oOooo0 :
     pass
    elif 'stage' in oOooo0 :
     I11I1IIiiII1 ( '[COLORgreen]' + o0Oo + '   -   ' + IiI111111IIII + '[/COLOR]' , ( oOooo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I111iI , )
    elif 'vee' in oOooo0 :
     pass
     if 48 - 48: IiiIIi11I - oo0Oo + iIii1I11I1II1 + OoooooooOO
def Ii ( ) :
 iIIiIi1iIII1 = OooOOOOo ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oO000o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , o0Oo , iIiiiI1IiI1I1 in oO000o :
  o0O0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for oOooo0 , IiI111111IIII in o0O0 :
   if 'tube' in oOooo0 :
    pass
   elif 'stage' in oOooo0 :
    I11I1IIiiII1 ( '[COLORgreen]' + o0Oo + '   -   ' + IiI111111IIII + '[/COLOR]' , ( oOooo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I111iI )
   elif 'vee' in oOooo0 :
    pass
    if 42 - 42: oOo00oOO0O * I1II11IiII . oo0Oo * OOOo0 + I1IiI
    if 25 - 25: IiiIIi11I . OOOo0 + ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: oo0Oo - OOooOOo % O0O0O + i11iIiiIii
def O0OOOo ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11IiIi11 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( iIIiIi1iIII1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( II11IiIi11 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in II11IiIi11 :
  Oo0oOooOoOo ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 30 - 30: O0O0O / Ooo00oOo00o + ii
  if 6 - 6: O0O0O . IiiIIi11I + oOo00oOO0O . I1II11IiII
  if 70 - 70: Ooo00oOo00o
  if 46 - 46: IiiIIi11I - i1IIi
  if 46 - 46: I1II11IiII % oOo00oOO0O
  if 72 - 72: iIii1I11I1II1
  if 45 - 45: Oo - OOooOOo % I1II11IiII
def i1IIi1i1Ii1 ( ) :
 if 45 - 45: iIii1I11I1II1 . ii / I1IiI / oo0Oo
 ooOOOoOoOOO0 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 ooOOOoOoOOO0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 5 - 5: Ii11I
 oO0Oo ( 'movies' , 'MAIN' )
 if 4 - 4: O0O0O % I1II11IiII / Ooo00oOo00o . Ii11I / Ii11I - ii11ii1ii
def oO0ooOO ( ) :
 ooOOOoOoOOO0 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 ooOOOoOoOOO0 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 7 - 7: OoOoOO00 - Ii11I . OoOoOO00
 oO0Oo ( 'movies' , 'MAIN' )
def OOo0O0O000 ( ) :
 if 29 - 29: OOooOOo / Oo * ii11ii1ii . OOooOOo
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 oO00 = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 1 - 1: ii
 for I1IIIIiii1i in oO00 :
  o0IiiiI111I = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  iIIiIi1iIII1 = OooOOOOo ( o0IiiiI111I )
  oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIiIi1iIII1 )
  for oOooo0 , I1i111I , OOo0 , OooOo0oo0O0o00O , IiI111111IIII in oo0O0oO :
   if oO0 in IiI111111IIII . lower ( ) :
    III1I11i1iIi ( IiI111111IIII , oOooo0 , 222 , I1i111I , OooOo0oo0O0o00O , OOo0 )
    if 69 - 69: Oo * OoOoOO00 * OOO0OOo . O0O0O - ii11ii1ii
    oO0Oo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 39 - 39: oOo00oOO0O * OOOo0 % Ooo00oOo00o . I1IiI
    if 24 - 24: i1IIi * iIii1I11I1II1 / oOo00oOO0O
def OoOOo00 ( ) :
 if 53 - 53: oo0Oo . I1II11IiII % iIii1I11I1II1 % I1IiI % IiiIIi11I
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 oO00 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 53 - 53: I1II11IiII
 for I1IIIIiii1i in oO00 :
  OOoOOo0o = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  iIIiIi1iIII1 = OooOOOOo ( OOoOOo0o )
  oo0O0oO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for IiI111111IIII , OOo0 , oOooo0 , I111iI , OooOo0oo0O0o00O , iIiii in oo0O0oO :
   if oO0 in IiI111111IIII . lower ( ) :
    ooOOOoOoOOO0 ( IiI111111IIII , oOooo0 , iIiii , I111iI , OooOo0oo0O0o00O , OOo0 )
    if 2 - 2: i1IIi - OOOo0 + IiiIIi11I . OoOoOO00
    oO0Oo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 25 - 25: ii
    if 34 - 34: I1IiI . iIii1I11I1II1 % O0
def iI11Ii111 ( ) :
 if 54 - 54: I1IiI % O0O0O . I1IiI * Ii11I + I1IiI % i1IIi
 IiI1iiiIii = OooOOOOo ( ooooooO0oo + 'spongemain.php' )
 oo0O0oO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for IiI111111IIII , OOo0 , oOooo0 , I111iI , OooOo0oo0O0o00O , iIiii in oo0O0oO :
  ooOOOoOoOOO0 ( IiI111111IIII , oOooo0 , iIiii , I111iI , OooOo0oo0O0o00O , OOo0 )
  oO0Oo ( 'movies' , 'MAIN' )
def I1I1I11Ii ( url ) :
 if 48 - 48: OoooooooOO + ii % iIii1I11I1II1
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiI1IIIII1I = ( '%s%s' % ( I1I1IiIi1 , url ) )
 iI1I1i11iIIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1I1i11iIIii )
 for url , I1i111I , OOo0 , oOO0o0oo0 , IiI111111IIII in oo0O0oO :
  III1I11i1iIi ( IiI111111IIII , url , 222 , I1i111I , oOO0o0oo0 , OOo0 )
  if 78 - 78: Ii11I + O0O0O . oo0Oo
  oO0Oo ( 'movies' , 'MAIN' )
  if 91 - 91: iIii1I11I1II1 . OOooOOo . ii11ii1ii + OoooooooOO
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 69 - 69: I1II11IiII - OOOo0
  if 95 - 95: OOOo0 * i11iIiiIii . OOO0OOo
def iIIi1 ( url ) :
 if 83 - 83: oo0Oo * IiiIIi11I / Oo
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for IiI111111IIII , OOo0 , url , I111iI , OooOo0oo0O0o00O , iIiii in oo0O0oO :
  ooOOOoOoOOO0 ( IiI111111IIII , url , iIiii , I111iI , OooOo0oo0O0o00O , OOo0 )
  if 32 - 32: OOooOOo + I1IiI - OoooooooOO
  oO0Oo ( 'movies' , 'MAIN' )
  if 39 - 39: OoooooooOO * Ii11I * O0 . IiiIIi11I . Ooo00oOo00o + OOO0OOo
  if 9 - 9: I1IiI + ii % OoooooooOO + OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: OoooooooOO + ii11ii1ii - O0O0O
def III1I11i1iIi ( name , url , mode , iconimage , fanart , description ) :
 if 24 - 24: OOooOOo + OOO0OOo + IiiIIi11I - iIii1I11I1II1
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = False )
 return IiiI1III1I1
 if 29 - 29: OOooOOo
def ooOOOoOoOOO0 ( name , url , mode , iconimage , fanart , description ) :
 if 86 - 86: OoOoOO00 . oo0Oo
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
if 2 - 2: OoooooooOO
if 60 - 60: Ooo00oOo00o
if 81 - 81: I1IiI % oOo00oOO0O
if 87 - 87: iIii1I11I1II1 . OoooooooOO * I1IiI
if 100 - 100: Ooo00oOo00o / i1IIi - OOOo0 % oOo00oOO0O - iIii1I11I1II1
if 17 - 17: IiiIIi11I / OOooOOo % Oo
if 71 - 71: oo0Oo . I1II11IiII . Ooo00oOo00o
if 68 - 68: i11iIiiIii % ii * Ooo00oOo00o * oo0Oo * OoOoOO00 + O0
if 66 - 66: IiiIIi11I % ii11ii1ii % OoooooooOO
if 34 - 34: OOooOOo / O0O0O % O0 . Ooo00oOo00o . i1IIi
if 29 - 29: O0 . I1II11IiII
if 66 - 66: ii * iIii1I11I1II1 % iIii1I11I1II1 * oo0Oo - OOO0OOo - oo0Oo
if 70 - 70: I1II11IiII + ii
if 93 - 93: I1II11IiII + oOo00oOO0O
if 33 - 33: O0
def oo0oO ( string ) :
 if OOO00 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % I1II11IiII - iIii1I11I1II1 % O0
def o0oO0Oo ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OO0OO000 = [ ]
 try :
  if 55 - 55: OOO0OOo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iIi1ii1I1 ) == False :
  oo0oO ( 'Making Favorites File' )
  OO0OO000 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  OOOOO0O00 = open ( iIi1ii1I1 , "w" )
  OOOOO0O00 . write ( json . dumps ( OO0OO000 ) )
  OOOOO0O00 . close ( )
 else :
  oo0oO ( 'Appending Favorites' )
  OOOOO0O00 = open ( iIi1ii1I1 ) . read ( )
  o0O0OO0o = json . loads ( OOOOO0O00 )
  o0O0OO0o . append ( ( name , url , iconimage , fanart , mode ) )
  iIII1I1i1i = open ( iIi1ii1I1 , "w" )
  iIII1I1i1i . write ( json . dumps ( o0O0OO0o ) )
  iIII1I1i1i . close ( )
  if 54 - 54: I1IiI . ii % i11iIiiIii / OoooooooOO + oo0Oo % ii
  if 36 - 36: ii
def o0OO ( ) :
 II1I1 = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 iii11I11iI1 = len ( II1I1 )
 for iI1i1iiii in II1I1 :
  IiI111111IIII = iI1i1iiii [ 0 ]
  oOooo0 = iI1i1iiii [ 1 ]
  I1i111I = iI1i1iiii [ 2 ]
  try :
   oO0o = iI1i1iiii [ 3 ]
   if oO0o == None :
    raise
  except :
   if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
    oO0o = I1i111I
   else :
    oO0o = OooOo0oo0O0o00O
  try : I1I1 = iI1i1iiii [ 5 ]
  except : I1I1 = None
  try : O0Oo0 = iI1i1iiii [ 6 ]
  except : O0Oo0 = None
  if 80 - 80: OOOo0 - iIii1I11I1II1 . Ii11I + Ooo00oOo00o - I1II11IiII
  if iI1i1iiii [ 4 ] == 0 :
   i1I1iI ( IiI111111IIII , oOooo0 , '' , I1i111I , OooOo0oo0O0o00O , '' , 'fav' )
  else :
   i1I1iI ( IiI111111IIII , oOooo0 , iI1i1iiii [ 4 ] , I1i111I , OooOo0oo0O0o00O , '' , 'fav' )
   if 5 - 5: O0O0O
def OOiI1 ( name ) :
 o0O0OO0o = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 for I1iIII1IiiI in range ( len ( o0O0OO0o ) ) :
  if o0O0OO0o [ I1iIII1IiiI ] [ 0 ] == name :
   del o0O0OO0o [ I1iIII1IiiI ]
   iIII1I1i1i = open ( iIi1ii1I1 , "w" )
   iIII1I1i1i . write ( json . dumps ( o0O0OO0o ) )
   iIII1I1i1i . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 96 - 96: OOOo0 % i1IIi . OOooOOo . O0
 if 37 - 37: i1IIi - Ii11I % OoooooooOO / Ii11I % OOO0OOo
def ii1 ( ) :
 iiIiII11i1 = os . path . join ( iIii1 , 'addons.ini' )
 oOo00Ooo0o0 = open ( iiIiII11i1 , "w+" )
 if 33 - 33: IiiIIi11I
 oOo00Ooo0o0 . write ( r'# This file contains the "built-in" channels' + '\n' )
 oOo00Ooo0o0 . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 oOo00Ooo0o0 . write ( r'[plugin.video.GenieTv]' + '\n' )
 oOo00Ooo0o0 . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F394.m3u8&mode=10012&name=[COLORgreen]BBC+One+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BBC Ent MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F435.m3u8&mode=10012&name=[COLORgreen]BBC+Entertainment+MX%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F408.m3u8&mode=10012&name=[COLORgreen]Watch+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F410.m3u8&mode=10012&name=[COLORgreen]Pick+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F430.m3u8&mode=10012&name=[COLORgreen]Gold+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F411.m3u8&mode=10012&name=[COLORgreen]Yesterday+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F398.m3u8&mode=10012&name=[COLORgreen]Disney+Channel+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F397.m3u8&mode=10012&name=[COLORgreen]Disney+Junior+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F395.m3u8&mode=10012&name=[COLORgreen]Discovery+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F396.m3u8&mode=10012&name=[COLORgreen]Discovery+Science+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F428.m3u8&mode=10012&name=[COLORgreen]Animal+Planet+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F431.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F429.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F409.m3u8&mode=10012&name=[COLORgreen]MTV+Music+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'MTV Canada=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F417.m3u8&mode=10012&name=[COLORgreen]MTV+2+Ca%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F37.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F39.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F40.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F43.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F41.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F44.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F47.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F48.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Fox Movies HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F436.m3u8&mode=10012&name=[COLORgreen]Fox+Movies+HD+MX%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Film Zone MX HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F437.m3u8&mode=10012&name=[COLORgreen]Film+Zone+MX+HD%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F403.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F404.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F405.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F406.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F407.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F412.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F423.m3u8&mode=10012&name=[COLORgreen]BT+Sports+1%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F413.m3u8&mode=10012&name=[COLORgreen]BT+Sports+2%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Fox Sports 1 HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F439.m3u8&mode=10012&name=[COLORgreen]Fox+Sports+1+HD+MX%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ESPN 1 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F440.m3u8&mode=10012&name=[COLORgreen]ESPN+1+HD+ES%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ESPN 2 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F441.m3u8&mode=10012&name=[COLORgreen]ESPN+2+HD+ES%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F427.m3u8&mode=10012&name=[COLORgreen]At+The+Races+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F426.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[/COLOR]' + '\n' )
 if 87 - 87: I1IiI / oo0Oo + iIii1I11I1II1
 if 93 - 93: iIii1I11I1II1 + ii % OOO0OOo
 if 21 - 21: Ii11I
def iIiI1I1IIi11 ( ) :
 if 9 - 9: OOO0OOo + O0O0O - IiiIIi11I / i1IIi % ii11ii1ii / oo0Oo
 i1I1iI ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 60 - 60: ii11ii1ii
def IIoO00OoOo ( ) :
 if 74 - 74: OoOoOO00 . O0 - OOOo0 + oo0Oo % i11iIiiIii % I1IiI
 IiI1iiiIii = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 oo0O0oO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for oOooo0 , I111iI , IiI111111IIII , i1Ii in oo0O0oO :
  i1I1iI ( IiI111111IIII + '  -  ' + ( i1Ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOooo0 , 10023 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 78 - 78: oOo00oOO0O + I1IiI + oo0Oo - oo0Oo . i11iIiiIii / Ooo00oOo00o
  if 27 - 27: oOo00oOO0O - O0 % IiiIIi11I * I1II11IiII . oo0Oo % iIii1I11I1II1
  if 37 - 37: OoooooooOO + O0 - i1IIi % OOO0OOo
def i1I1i1i ( ) :
 if 36 - 36: OoOoOO00 % O0
 i1I1iI ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 35 - 35: iIii1I11I1II1 - Ii11I % OOooOOo
def I111i1Ii1i1 ( url ) :
 oO00oooOOoOo0 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 iIIiIi1iIII1 = cloudflare . source ( oO00oooOOoOo0 )
 oo0O0oO = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 10022 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 11 - 11: I1IiI % oo0Oo
  if 53 - 53: OOO0OOo / iIii1I11I1II1 - Ooo00oOo00o + ii
  if 30 - 30: oo0Oo
  if 24 - 24: Ooo00oOo00o - ii + ii11ii1ii / O0O0O % OOOo0 + iIii1I11I1II1
def oO00o ( ) :
 if 36 - 36: I1II11IiII . OoOoOO00 % OOO0OOo
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 oOooo0 = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oO0 ) . replace ( ' ' , '+' )
 iIIiIi1iIII1 = cloudflare . source ( oOooo0 )
 oo0O0oO = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , I111iI , IiI111111IIII in oo0O0oO :
  if oO0 in IiI111111IIII . lower ( ) :
   i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 10022 , ii11iIi1I + 'dtv.png' )
   if 84 - 84: OoooooooOO - i11iIiiIii / iIii1I11I1II1 / OoooooooOO / ii11ii1ii
   if 4 - 4: Oo + OOooOOo
   if 17 - 17: Ooo00oOo00o * I1IiI
def ii11i ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for iIII1I111III , o00Oo , O000oOo , IiI111111IIII in oo0O0oO :
  IiiIIi1 = ( O000oOo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iI1iIiiI = ( o00Oo ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Oo0OOo = 'Season ' + iI1iIiiI + 'Episode ' + IiiIIi1 + IiI111111IIII
  Ii1I11i11I1i ( Oo0OOo , iIII1I111III )
  if 59 - 59: i1IIi
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 48 - 48: O0 * oOo00oOO0O * Ooo00oOo00o . Ooo00oOo00o * IiiIIi11I - oOo00oOO0O
  if 14 - 14: ii11ii1ii + i11iIiiIii
def Ii1I11i11I1i ( name , url ) :
 iIII1I111III = url
 OOOoo = name
 iiIiIIIiiI = cloudflare . source ( iIII1I111III )
 iiI1IIIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( iiIiIIIiiI )
 for II11IiIi11 , III1II1iii1i in iiI1IIIi :
  I11I1IIiiII1 ( '[COLORgreen]' + OOOoo + III1II1iii1i + '[/COLOR]' , II11IiIi11 , 10012 , ii11iIi1I + 'dtv.png' )
  if 75 - 75: oo0Oo - I1IiI - iIii1I11I1II1 % OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: O0 . oo0Oo / OoooooooOO . Ooo00oOo00o / Oo * OoOoOO00
 if 53 - 53: oOo00oOO0O - O0 / OOooOOo % O0O0O * OOOo0 % Ii11I
def o0oOOOO0 ( ) :
 if 11 - 11: i1IIi
 if 19 - 19: O0O0O - OOooOOo - oOo00oOO0O - I1IiI . O0O0O . I1II11IiII
 if 48 - 48: O0O0O + oo0Oo
 if 60 - 60: IiiIIi11I + O0O0O . oo0Oo / i1IIi . iIii1I11I1II1
 if 14 - 14: Ii11I
 if 79 - 79: oOo00oOO0O
 if 76 - 76: iIii1I11I1II1
 if 80 - 80: iIii1I11I1II1 . O0 / oOo00oOO0O % oOo00oOO0O
 if 93 - 93: OoooooooOO * Oo
 if 10 - 10: I1II11IiII * OoooooooOO + IiiIIi11I - ii11ii1ii / ii11ii1ii . i11iIiiIii
 if 22 - 22: I1II11IiII / OOooOOo
 if 98 - 98: i1IIi
 if 51 - 51: ii11ii1ii + OOO0OOo + Oo / i1IIi + i1IIi
 if 12 - 12: iIii1I11I1II1 . oOo00oOO0O . ii11ii1ii % OOOo0 . OoOoOO00 . ii
 if 32 - 32: ii11ii1ii + oo0Oo / O0 / I1IiI * OoooooooOO % OOO0OOo
 i1I1iI ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 i1I1iI ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 i1I1iI ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 if 50 - 50: Ooo00oOo00o
 if 66 - 66: iIii1I11I1II1
def I11II1i11 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 oo0O0oO = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( i1Iii1i1I ) )
 for url , IiI111111IIII in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 28 - 28: OoOoOO00 - ii % I1IiI + Ooo00oOo00o - I1IiI
def IiI ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 63 - 63: O0
def i1I1iIii11 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 iiI1IIIi = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in iiI1IIIi :
  i1I1iI ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ii11iIi1I + 'Next.png' , '' , '' )
  if 80 - 80: I1IiI - OoOoOO00
  if 35 - 35: OOO0OOo - Ooo00oOo00o . Oo * Oo / i11iIiiIii + ii11ii1ii
def oOo0Oo0O0O ( ) :
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1II1i = 'http://www.watchseries.li/search/' + oO0 . replace ( ' ' , '%20' )
 iIIiIi1iIII1 = OooOOOOo ( III1II1i )
 oo0O0oO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , oOooo0 , IiI111111IIII in oo0O0oO :
  if 'watch online' in IiI111111IIII :
   pass
  else :
   print oOooo0
   i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.watchseries.li' + oOooo0 , 10044 , I111iI , '' , '' )
   if 3 - 3: O0O0O
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 35 - 35: oo0Oo . O0 + Oo + Ii11I + i1IIi
def OooOooO0O0o0 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , url , IiI111111IIII , O000oOo , OOo0 in oo0O0oO :
  OOO0o0 = ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( O000oOo ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  i1I1iI ( '[COLORgreen]' + OOO0o0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , I111iI , '' , OOo0 )
  if 34 - 34: OOOo0 % Oo - I1IiI + O0O0O
def Ooo0Oo0o ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 iiI1IIIi = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  OOO0o0 = ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  i1I1iI ( '[COLORgreen]' + OOO0o0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in iiI1IIIi :
  i1I1iI ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ii11iIi1I + 'Next.png' , '' , '' )
  if 85 - 85: OOOo0
def Ii1Ii1I ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 iiI1IIIi = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , I111iI in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , I111iI , '' , '' )
 for url in iiI1IIIi :
  i1I1iI ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ii11iIi1I + 'Next.png' , '' , '' )
  if 54 - 54: ii + I1IiI
def o0O00O ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for o00Oo , oO000o in i1Iii1i1I :
  oo0O0oO = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( oO000o ) )
  for url , IiI111111IIII in oo0O0oO :
   OOO0o0 = ( o00Oo ) . replace ( '  ' , '' ) + ' ' + ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   i1I1iI ( '[COLORgreen]' + OOO0o0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 iiI1IIIi = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url in iiI1IIIi :
  i1I1iI ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'Next.png' , '' , '' )
  if 94 - 94: oOo00oOO0O - ii11ii1ii + OOooOOo - Oo
  if 15 - 15: Ii11I
class i1iiI ( ) :
 if 83 - 83: ii / iIii1I11I1II1 + i1IIi / O0O0O
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 47 - 47: ii + OoooooooOO . OoOoOO00 . O0O0O
  OOO0o0 = name
  self . Get_Sources ( oOooo0 , OOO0o0 )
  if 66 - 66: OOO0OOo * I1IiI
  if 2 - 2: ii . I1II11IiII * Oo + O0 - IiiIIi11I * iIii1I11I1II1
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  iIIiIi1iIII1 = OooOOOOo ( URL )
  oo0O0oO = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for oOooo0 , IiI111111IIII in oo0O0oO :
   URL = 'http://www.watchseries.li/link/' + oOooo0
   self . Get_site_link ( URL , season_name )
   if 12 - 12: OOooOOo * I1II11IiII % OoOoOO00 * i1IIi * iIii1I11I1II1
 def Get_site_link ( self , url , season_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( iIIiIi1iIII1 )
  iiI1IIIi = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( iIIiIi1iIII1 )
  IiiIiI = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( iIIiIi1iIII1 )
  for url in oo0O0oO :
   self . main ( url , season_name )
  for url in iiI1IIIi :
   self . main ( url , season_name )
  for url in IiiIiI :
   self . main ( url , season_name )
   if 81 - 81: Oo - IiiIIi11I
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   ii1iII1iI111 = 'DACLIPS'
   if ii1iII1iI111 in i1iiI . source_list :
    pass
   else :
    self . daclips ( url , season_name , ii1iII1iI111 )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    ii1iII1iI111 = 'FILEHOOT'
    if ii1iII1iI111 in i1iiI . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , ii1iII1iI111 )
   else :
    if 'thevideo.me' in url :
     ii1iII1iI111 = 'THEVIDEO'
     if ii1iII1iI111 in i1iiI . source_list :
      pass
     else :
      self . thevideo ( url , season_name , ii1iII1iI111 )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      ii1iII1iI111 = 'ALLMYVIDEOS'
      if ii1iII1iI111 in i1iiI . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , ii1iII1iI111 )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       ii1iII1iI111 = 'VIDSPOT'
       if ii1iII1iI111 in i1iiI . source_list :
        pass
       else :
        self . vidspot ( url , season_name , ii1iII1iI111 )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        ii1iII1iI111 = 'VODLOCKER'
        if ii1iII1iI111 in i1iiI . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , ii1iII1iI111 )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 94 - 94: O0O0O % OOO0OOo . ii
         if 85 - 85: Ii11I * i1IIi % OOOo0 - OOO0OOo
 def allmyvid ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for I11I1ii1i , IiI111111IIII in oo0O0oO :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 22 - 22: ii * oOo00oOO0O * i11iIiiIii + O0O0O * I1IiI * Ooo00oOo00o
 def vidspot ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( iIIiIi1iIII1 )
  for I11I1ii1i , IiI111111IIII in oo0O0oO :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 85 - 85: O0O0O * Ii11I % Oo - O0O0O - IiiIIi11I
 def thevideo ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( iIIiIi1iIII1 )
  for I11I1ii1i in oo0O0oO :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 46 - 46: O0
 def vodlocker ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for I11I1ii1i in oo0O0oO :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 65 - 65: iIii1I11I1II1 % ii + O0 / OoooooooOO
 def daclips ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( iIIiIi1iIII1 )
  for I11I1ii1i in oo0O0oO :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 52 - 52: oOo00oOO0O % Ii11I * OOOo0 % IiiIIi11I + Ii11I / O0O0O
 def filehoot ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for I11I1ii1i in oo0O0oO :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 80 - 80: OoooooooOO + oo0Oo
 def Printer ( self , Link , season_name , source_name ) :
  if 95 - 95: I1II11IiII / ii * I1II11IiII - OoooooooOO * OoooooooOO % Ooo00oOo00o
  if Link in i1iiI . List :
   pass
  elif source_name in i1iiI . source_list :
   pass
  else :
   I11I1IIiiII1 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ii11iIi1I + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   i1iiI . List . append ( Link )
   i1iiI . source_list . append ( source_name )
   if 43 - 43: Oo . I1II11IiII
   xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 12 - 12: I1II11IiII + Ii11I + IiiIIi11I . oo0Oo / oOo00oOO0O
   if 29 - 29: oo0Oo . OOO0OOo - OoOoOO00
   if 68 - 68: iIii1I11I1II1 + OoOoOO00 / ii
   if 91 - 91: I1IiI % iIii1I11I1II1 . OOOo0
   if 70 - 70: IiiIIi11I % OoOoOO00 % O0 . i1IIi / I1II11IiII
def OO0ooOoOO0OOo ( ) :
 i1I1iI ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 51 - 51: iIii1I11I1II1 * OOooOOo / iIii1I11I1II1 . iIii1I11I1II1 . O0O0O * IiiIIi11I
def oO0oo0o00o0O ( ) :
 IiI1iiiIii = OooOOOOo ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 oo0O0oO = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( IiI1iiiIii )
 for oOooo0 , I111iI , IiI111111IIII in oo0O0oO :
  i1I1iI ( '[COLORgreen]' + ( IiI111111IIII ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOooo0 , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I111iI , i1iiIII111ii , '' )
  if 80 - 80: iIii1I11I1II1
def i1I11 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for i1Iii1i1I in i1Iii1i1I :
  iII11ii1ii = re . compile ( '(.*?)</h2>' ) . findall ( str ( i1Iii1i1I ) )
  for oOO0OOOo000o in iII11ii1ii :
   oOO0OOOo000o = oOO0OOOo000o
  OO00oo = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( i1Iii1i1I ) )
  for O0Oo0O0 , I111iI , time , I1IiiIiii1 in OO00oo :
   o0o00OOo0 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1IiiIiii1 )
   i1I1iI ( '[COLORgreen]' + oOO0OOOo000o + ' - ' + O0Oo0O0 + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I111iI , i1iiIII111ii , ( str ( o0o00OOo0 ) ) )
   if 39 - 39: OOO0OOo / O0 * oo0Oo
 oO0Oo ( 'tvshows' , 'Media Info 3' )
 if 17 - 17: oOo00oOO0O / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % Ii11I
def III1III11II ( ) :
 if 43 - 43: OOOo0
 i1I1iI ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ii11iIi1I + 'fanart.jpg' , '' )
 i1I1iI ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ii11iIi1I + 'fanart.jpg' , '' )
 if 47 - 47: OoooooooOO % I1IiI
def OO0Oo ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , url , IiI111111IIII in oo0O0oO :
  IIiiiiiIiIIi = IiI111111IIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  I11I1IIiiII1 ( '[COLORgreen]' + IIiiiiiIiIIi + '[/COLOR]' , url , 10013 , I111iI )
  if 26 - 26: OOooOOo
def IiIioO0Oo00oo ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( iIIiIi1iIII1 )
 for II11IiIi11 in oo0O0oO :
  OoOoooO000OO = ( II11IiIi11 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  Oo0oOooOoOo ( 'http:' + OoOoooO000OO )
  if 62 - 62: Ii11I + Oo % iIii1I11I1II1 / iIii1I11I1II1 . OOO0OOo . oo0Oo
  if 21 - 21: Ooo00oOo00o - oOo00oOO0O - OOOo0 / I1IiI
def ii1oOoO0ooO0000 ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII , I111iI in oo0O0oO :
  I11I1IIiiII1 ( IiI111111IIII , url , 8046 , I111iI )
 for url in iiI1IIIi :
  iII11I1Ii1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ii11iIi1I + 'Next.png' )
def OOOOO ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  Oo0oOooOoOo ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 68 - 68: IiiIIi11I + Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI
def I1iiiI ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  yt . PlayVideo ( url )
  if 24 - 24: OOOo0 * ii
def Oo0 ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , oOooo0 , 8041 , ii11iIi1I + 'documentary.png' )
def O0000Oo00o ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII , I111iI in oo0O0oO :
  iII11I1Ii1 ( ( IiI111111IIII ) . replace ( '&#039;s' , '' ) , url , 8042 , I111iI )
 for url in iiI1IIIi :
  iII11I1Ii1 ( 'NEXT PAGE' , url , 8041 , ii11iIi1I + 'Next.png' )
  if 20 - 20: Ooo00oOo00o . OOOo0 * i11iIiiIii / i11iIiiIii
  if 89 - 89: O0O0O . i11iIiiIii * O0
def Iiii1 ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( IiI1iiiIii )
 for IiI111111IIII , I111iI , url , iiiii1ii1 in oo0O0oO :
  I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , I111iI )
 for url in iiI1IIIi :
  iI111II1ii ( ( url ) . replace ( '//' , 'http://' ) )
  if 62 - 62: O0O0O * iIii1I11I1II1 . oo0Oo - OoooooooOO * OoOoOO00
def iI111II1ii ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  I11I1IIiiII1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii11iIi1I + 'documentary.png' )
  if 45 - 45: O0 % OOOo0 - O0O0O . Ooo00oOo00o
def I1II ( ) :
 iIIiIi1iIII1 = I1III1111iIi ( 'http://www.stream2watch.co/live-tv' )
 oo0O0oO = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , I111iI , IiI111111IIII , iIIi1Ii1III in oo0O0oO :
  iII11I1Ii1 ( ( IiI111111IIII + '[COLORgreen]' + iIIi1Ii1III + '[/COLOR]' ) , oOooo0 , 8086 , I111iI )
  if 86 - 86: i11iIiiIii + i11iIiiIii . I1II11IiII % OOOo0 . OOO0OOo
def iII1iI1IIiI ( url ) :
 iIIiIi1iIII1 = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 8087 , I111iI )
  if 69 - 69: IiiIIi11I / i11iIiiIii * OOooOOo / I1II11IiII
def oO0O ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  OOoooO00o0o ( url , IiI111111IIII )
  if 10 - 10: oOo00oOO0O - i11iIiiIii . ii11ii1ii % i1IIi
def OOoooO00o0o ( url , name ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  print url
  I11I1IIiiII1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 78 - 78: iIii1I11I1II1 * Oo . Oo - Ii11I . iIii1I11I1II1
def I111I1I ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 oo0O0oO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for oOooo0 , I111iI , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oOooo0 , 3002 , 'http://www.solie.org/alibrary/' + I111iI )
def Oo0000 ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I111iI )
def oO0OoOo ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( IiI1iiiIii )
 oOOOOOo = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( IiI1iiiIii )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ii11iIi1I + 'classicmovies.png' )
 for url , IiI111111IIII in oOOOOOo :
  iII11I1Ii1 ( '[COLORgreen]Season- ' + IiI111111IIII + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'classicmovies.png' )
 for url in next :
  iII11I1Ii1 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'Next.png' )
 for url , I111iI , IiI111111IIII in iiI1IIIi :
  iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I111iI )
def i1I11ii ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  o0ooO00O0O ( url )
def o0ooO00O0O ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  Oo0oOooOoOo ( url )
  if 41 - 41: ii11ii1ii
def i1iI1i ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 oo0O0oO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOooo0 , 8061 , ii11iIi1I + 'classicmovies.png' )
def o0o0OoO0OOO0 ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( "v.src = '([^']*)';" ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  Oo0oOooOoOo ( url )
  if 79 - 79: ii % OOooOOo % I1IiI
def ii1IIiII111I ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 oo0O0oO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOooo0 , 8061 , ii11iIi1I + 'classictv.png' )
def O00OoOoO ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( "v.src = '([^']*)';" ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  Oo0oOooOoOo ( url )
  if 58 - 58: ii11ii1ii
def ii1ii1i11I1I ( ) :
 iIIiIi1iIII1 = OooOOOOo ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oOooo0 , 8071 , ii11iIi1I + 'streams.png' )
def iiII1iiiiiii ( url ) :
 iIIiIi1iIII1 = I1III1111iIi ( url )
 oo0O0oO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , url in oo0O0oO :
  I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ii11iIi1I + 'streams.png' )
def iiIiii ( url ) :
 iIIiIi1iIII1 = I1III1111iIi ( url )
 oo0O0oO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , IiI111111IIII , url in oo0O0oO :
  url = ( ( i1111 ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . replace ( '.ts' , '.m3u8' ) , 10012 , I111iI )
  if 39 - 39: OOOo0 + Oo
def o0OOooO ( ) :
 oOo00oOOOOO ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOo00oOOOOO ( 'Genres' , 'http://www.xvideos.com' , 10106 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOo00oOOOOO ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOo00oOOOOO ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOo00oOOOOO ( 'Search' , '' , 10107 , ii11iIi1I + 'JIZBOX.png' , '' , '' , )
 if 41 - 41: i1IIi + OoOoOO00 * OOO0OOo
def o0oOoOo0 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 III1IiI1i1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( iIIiIi1iIII1 )
 for url in III1IiI1i1i :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , O0O0OOOOoo in oo0O0oO :
  oOo00oOOOOO ( IiI111111IIII + ' - No of Videos : ' + ( O0O0OOOOoo ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 94 - 94: O0O0O - Oo + ii
def O0oooOoO ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 III1IiI1i1i = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( iIIiIi1iIII1 )
 for url in III1IiI1i1i :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ii11iIi1I + 'Next.png' , '' , '' )
 oo0O0oO = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , url , IiI111111IIII , O0Oo0iIIIi1IiI11I1 in oo0O0oO :
  oOo00oOOOOO ( IiI111111IIII + '--' + O0Oo0iIIIi1IiI11I1 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( I111iI ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 71 - 71: oOo00oOO0O - O0 - O0O0O . Ii11I % Oo
  if 82 - 82: OoooooooOO + Ii11I % I1IiI . Ooo00oOo00o * i1IIi
def iIiIi1iIIi11i ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , url , IiI111111IIII , ooO , I1IIII in oo0O0oO :
  OOoo0O ( IiI111111IIII + ' - Porn Quality : ' + I1IIII + ' - ' + ooO , 'http://www.xvideos.com' + url , 10108 , I111iI , I111iI , I1IIII + ' - ' + ooO )
 OooooOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( iIIiIi1iIII1 )
 for url in OooooOoO :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 79 - 79: OOO0OOo % Ii11I
def oO0O0o0O ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 III1IiI1i1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( iIIiIi1iIII1 )
 for url in III1IiI1i1i :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ii11iIi1I + 'Next.png' , '' , '' )
 oo0O0oO = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( i1Iii1i1I ) )
 for url , IiI111111IIII in oo0O0oO :
  oOo00oOOOOO ( IiI111111IIII , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 100 - 100: I1IiI % Oo
  if 76 - 76: OoOoOO00 / Ooo00oOo00o + OoooooooOO . ii11ii1ii . IiiIIi11I . OOO0OOo
def iiiI ( ) :
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIIiiiIiI1 = ( oO0 ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 OO = iIIIiiiIiI1 . lower ( )
 O0OOoooo0 = 'http://www.xvideos.com/?k=' + OO
 print O0OOoooo0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 iIIiIi1iIII1 = OooOOOOo ( O0OOoooo0 )
 oo0O0oO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I111iI , oOooo0 , IiI111111IIII , ooO , I1IIII in oo0O0oO :
  OOoo0O ( IiI111111IIII + ' - Porn Quality : ' + I1IIII + ' - ' + ooO , 'http://www.xvideos.com' + oOooo0 , 10108 , I111iI , I111iI , I1IIII + ' - ' + ooO )
 OooooOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 in OooooOoO :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oOooo0 , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 7 - 7: I1II11IiII
def ii1IiIi1i ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'flv_url=(.+?)\;' ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  OOOO00OoooO = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  IIIi ( OOOO00OoooO )
  if 43 - 43: i1IIi + O0 % Ooo00oOo00o / oOo00oOO0O * OOOo0
def IIIi ( url ) :
 iiiiI1iiiIi = xbmc . Player ( OoO ( ) )
 import urlresolver
 try : iiiiI1iiiIi . play ( url )
 except : pass
 if 37 - 37: ii11ii1ii
 if 68 - 68: OOooOOo
def Ooo00O0 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 oo0O0oO = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + oOooo0 ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ii11iIi1I + 'gofish.png' )
def OoO0OOoO0 ( url ) :
 iIIiIi1iIII1 = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 iiI1IIIi = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ii11iIi1I + 'gofish.png' )
 for url , IiI111111IIII , I111iI in iiI1IIIi :
  I11I1IIiiII1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + I111iI )
 for url in next :
  iII11I1Ii1 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ii11iIi1I + 'Next.png' )
def iiI11i ( url ) :
 iIIiIi1iIII1 = I1III1111iIi ( url )
 oo0O0oO = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  yt . PlayVideo ( url )
  if 75 - 75: OOO0OOo / Oo
def iii ( url ) :
 Ooi1IIii11i1I1 = urllib2 . Request ( url )
 Ooi1IIii11i1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ii1I1 = ''
 iI1I1i11iIIii = ''
 try :
  Ii1I1 = urllib2 . urlopen ( Ooi1IIii11i1I1 )
  iI1I1i11iIIii = Ii1I1 . read ( )
  Ii1I1 . close ( )
 except : pass
 if iI1I1i11iIIii != '' :
  return iI1I1i11iIIii
 else :
  iI1I1i11iIIii = 'Failed'
  return iI1I1i11iIIii
  if 98 - 98: oo0Oo * iIii1I11I1II1 . oOo00oOO0O * Oo / ii11ii1ii + OOO0OOo
  if 25 - 25: ii
def Iii11111iiI ( ) :
 o0OOOOoO = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 oOooo0 = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 iIII1I111III = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 iIIIiIi = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OoO0Ooo = ( i1111 ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 Ii1I1I = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oOOoOOO0oOoo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0O0ooooooo00 = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oO0
 I1111ii11IIII = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 IiIi1II111I = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 o00o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 IIi1i1 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 84 - 84: Ii11I + oOo00oOO0O + OOooOOo
 iIIiIi1iIII1 = iii ( oOooo0 )
 iiIiIIIiiI = iii ( iIII1I111III )
 i1i1iIII11i = iii ( iIIIiIi )
 IiII = iii ( OoO0Ooo )
 oOo = iii ( Ii1I1I )
 oo0o = iii ( o0O0ooooooo00 )
 IioOooOOo00ooO = iii ( I1111ii11IIII )
 o0OO0oooo = iii ( IiIi1II111I )
 I11II1i1 = iii ( o00o )
 IiI1ii11I1 = iii ( IIi1i1 )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 if 19 - 19: I1II11IiII + oo0Oo / ii / OoOoOO00
 if 92 - 92: i1IIi % OOO0OOo + OOO0OOo - iIii1I11I1II1 . oOo00oOO0O
 if iIIiIi1iIII1 != 'Failed' :
  oo0O0oO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
  for iIIi1o0Ooo0o0Oo , IiI111111IIII in oo0O0oO :
   if oO0 in IiI111111IIII . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOooo0 + iIIi1o0Ooo0o0Oo ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if iiIiIIIiiI != 'Failed' :
  iiI1IIIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iiIiIIIiiI )
  for iIIi1o0Ooo0o0Oo , IiI111111IIII in iiI1IIIi :
   if oO0 in IiI111111IIII . lower ( ) :
    I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIII1I111III + iIIi1o0Ooo0o0Oo ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if i1i1iIII11i != 'Failed' :
  IiiIiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( i1i1iIII11i )
  for iIIi1o0Ooo0o0Oo , IiI111111IIII in IiiIiI :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIIIiIi + iIIi1o0Ooo0o0Oo ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if IiII != 'Failed' :
  oo00ooooOOo00 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IiII )
  for iIIi1o0Ooo0o0Oo , IiI111111IIII in oo00ooooOOo00 :
   if oO0 in IiI111111IIII . lower ( ) :
    I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OoO0Ooo + iIIi1o0Ooo0o0Oo ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Source 4 Links" )
 if oOo != 'Failed' :
  ii1i = [ ]
  OO00Oooo000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo )
  for oOooo0 , I1i111I , OOo0 , oOO0o0oo0 , IiI111111IIII in OO00Oooo000 :
   if oO0 in IiI111111IIII . lower ( ) :
    if IiI111111IIII in ii1i :
     pass
    else :
     i1I1iI ( ( '[COLORgreen]' + IiI111111IIII + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oOooo0 , 1016 , I1i111I , oOO0o0oo0 , OOo0 )
     ii1i . append ( IiI111111IIII )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     oO0Oo ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  iI1ii111iiIii = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oo0o )
  for oOooo0 , I111iI , IiI111111IIII in iI1ii111iiIii :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oOooo0 , 7067 , I111iI )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 57 - 57: OOooOOo / I1II11IiII
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if IioOooOOo00ooO != 'Failed' :
  iiIiII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IioOooOOo00ooO )
  for oOooo0 , I1i111I , OOo0 , oOO0o0oo0 , IiI111111IIII in iiIiII :
   if oO0 in IiI111111IIII . lower ( ) :
    OOoo0O ( ( '[COLORgreen]' + IiI111111IIII + '- source Redemption[/COLOR]' ) , oOooo0 , 222 , I1i111I , oOO0o0oo0 , OOo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 7 - 7: Oo - i1IIi . ii11ii1ii / iIii1I11I1II1 * OOooOOo
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if o0OO0oooo != 'Failed' :
  O0O0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OO0oooo )
  for oOooo0 , I1i111I , OOo0 , oOO0o0oo0 , IiI111111IIII in O0O0 :
   if oO0 in IiI111111IIII . lower ( ) :
    OOoo0O ( ( '[COLORgreen]' + IiI111111IIII + '- source Reaper[/COLOR]' ) , oOooo0 , 222 , I1i111I , oOO0o0oo0 , OOo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 70 - 70: Ii11I * ii / OOOo0 * I1IiI * OOOo0
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if I11II1i1 != 'Failed' :
  OOoO0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I11II1i1 )
  for oOooo0 , I1i111I , OOo0 , oOO0o0oo0 , IiI111111IIII in OOoO0o :
   if oO0 in IiI111111IIII . lower ( ) :
    OOoo0O ( ( '[COLORgreen]' + IiI111111IIII + '- source Herovision[/COLOR]' ) , oOooo0 , 222 , I1i111I , oOO0o0oo0 , OOo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 62 - 62: IiiIIi11I / ii % Oo . OoooooooOO / i11iIiiIii / I1II11IiII
    oO0Oo ( 'tvshows' , 'Media Info 3' )
    if 60 - 60: OOOo0 % ii / OOooOOo % ii * i11iIiiIii / O0O0O
 if IiI1ii11I1 != 'Failed' :
  i1Ii11II = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1ii11I1 )
  for oOooo0 , I1i111I , IiI111111IIII in i1Ii11II :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '- source Silent Hunter[/COLOR]' ) , oOooo0 , 222 , I1i111I )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 33 - 33: oo0Oo . OoooooooOO . ii
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 iI1o0 = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 32 - 32: OoooooooOO / OoOoOO00 / ii + oOo00oOO0O / O0
 for I1IIIIiii1i in iI1o0 :
  o0IiiiI111I = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  oOO0 = OooOOOOo ( o0IiiiI111I )
  if oOO0 != 'Failed' :
   OoO000Oo0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOO0 )
   for oOooo0 , I1i111I , OOo0 , oOO0o0oo0 , IiI111111IIII in OoO000Oo0oO :
    if oO0 in IiI111111IIII . lower ( ) :
     OOoo0O ( '[COLORgreen]' + IiI111111IIII + ' - Source Pandoras[/COLOR]' , oOooo0 , 222 , I1i111I , oOO0o0oo0 , OOo0 )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 46 - 46: O0 - I1IiI . OoooooooOO
     oO0Oo ( 'tvshows' , 'Media Info 3' )
     if 19 - 19: OOooOOo
 oO00 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 73 - 73: I1II11IiII * Oo * I1IiI
 if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
 for I1IIIIiii1i in oO00 :
  o0IiiiI111I = o0OOOOoO + I1IIIIiii1i
  III11I11ii = iii ( o0IiiiI111I )
  if oOo != 'Failed' :
   O0OoO0oO00 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( III11I11ii )
   for iIIi1o0Ooo0o0Oo , IiI111111IIII in O0OoO0oO00 :
    if oO0 in IiI111111IIII . lower ( ) :
     I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o0OOOOoO + I1IIIIiii1i + iIIi1o0Ooo0o0Oo ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 2 - 2: I1II11IiII - ii11ii1ii + OOooOOo * Ooo00oOo00o / O0O0O
     oO0Oo ( 'tvshows' , 'Media Info 3' )
     if 26 - 26: Ii11I * Oo
     if 31 - 31: IiiIIi11I * ii . oOo00oOO0O
def i1Ii11ii1I ( ) :
 if 66 - 66: Oo / OoooooooOO % I1II11IiII / O0O0O + OoooooooOO
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 IiIi1II111I = ( i1111 ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( oO0 ) . replace ( ' ' , '+' )
 oOooo0 = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 iIII1I111III = ( i1111 ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 iIIIiIi = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 OoO0Ooo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 Ii1I1I = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oO0 ) . replace ( ' ' , '+' )
 oOOoOOO0oOoo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 o0O0ooooooo00 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 I1111ii11IIII = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 6 - 6: OoOoOO00 % I1II11IiII
 o0OO0oooo = iii ( IiIi1II111I )
 iIIiIi1iIII1 = iii ( oOooo0 )
 iiIiIIIiiI = iii ( iIII1I111III )
 i1i1iIII11i = iii ( iIIIiIi )
 IiII = iii ( OoO0Ooo )
 oOo = cloudflare . source ( Ii1I1I )
 III11I11ii = iii ( oOOoOOO0oOoo )
 oo0o = iii ( o0O0ooooooo00 )
 IioOooOOo00ooO = iii ( I1111ii11IIII )
 if 41 - 41: oo0Oo - OoOoOO00 . OoOoOO00 + OOOo0
 if IioOooOOo00ooO != 'Failed' :
  iiIiII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IioOooOOo00ooO )
  for oOooo0 , I1i111I , OOo0 , oOO0o0oo0 , IiI111111IIII in iiIiII :
   if oO0 in IiI111111IIII . lower ( ) :
    i1I1iI ( ( '[COLORgreen]' + IiI111111IIII + '- source HeroVision[/COLOR]' ) , oOooo0 , 1016 , I1i111I , oOO0o0oo0 , OOo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 59 - 59: iIii1I11I1II1 % oOo00oOO0O . i11iIiiIii
    oO0Oo ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: OOooOOo . ii . oOo00oOO0O * I1IiI * Ooo00oOo00o + Oo
 if oo0o != 'Failed' :
  iI1ii111iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0o )
  for oOooo0 , I1i111I , OOo0 , oOO0o0oo0 , IiI111111IIII in iI1ii111iiIii :
   if oO0 in IiI111111IIII . lower ( ) :
    i1I1iI ( ( '[COLORgreen]' + IiI111111IIII + '- source Reaper[/COLOR]' ) , oOooo0 , 1016 , I1i111I , oOO0o0oo0 , OOo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 90 - 90: I1II11IiII % Oo - Oo . iIii1I11I1II1 / Ii11I + IiiIIi11I
    oO0Oo ( 'tvshows' , 'Media Info 3' )
    if 89 - 89: ii
 if o0OO0oooo != 'Failed' :
  O0O0 = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( o0OO0oooo )
  for oOooo0 , I111iI , IiI111111IIII in O0O0 :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + ' CoolSeries[/COLOR]' , oOooo0 , 7052 , I111iI )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 87 - 87: O0O0O % Oo
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if iIIiIi1iIII1 != 'Failed' :
  oo0O0oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIiIi1iIII1 )
  for IiI111111IIII in oo0O0oO :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( '[COLORgreen]' + ( IiI111111IIII ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( oOooo0 + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 62 - 62: Ooo00oOo00o + OOO0OOo / O0O0O * i11iIiiIii
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if iiIiIIIiiI != 'Failed' :
  iiI1IIIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiIiIIIiiI )
  for IiI111111IIII in iiI1IIIi :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( ( IiI111111IIII + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIII1I111III + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 37 - 37: O0O0O
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if i1i1iIII11i != 'Failed' :
  IiiIiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i1i1iIII11i )
  for IiI111111IIII in iiI1IIIi :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( ( IiI111111IIII + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIIIiIi + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 33 - 33: Ooo00oOo00o - O0 - Ooo00oOo00o
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if IiII != 'Failed' :
  oo00ooooOOo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IiII )
  for IiI111111IIII in iiI1IIIi :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( ( IiI111111IIII + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OoO0Ooo + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 94 - 94: oo0Oo * IiiIIi11I * OoooooooOO / OOooOOo . oo0Oo - OOooOOo
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if oOo != 'Failed' :
  OO00Oooo000 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oOo )
  for oOooo0 , I111iI , IiI111111IIII in OO00Oooo000 :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + ' - Source - Dizi[/COLOR]' , oOooo0 , 8062 , I111iI )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 13 - 13: Ii11I / oo0Oo - Ooo00oOo00o / Ii11I . i1IIi
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if III11I11ii != 'Failed' :
  O0OoO0oO00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( III11I11ii )
  for oOooo0 , I1i111I , OOo0 , oOO0o0oo0 , IiI111111IIII in O0OoO0oO00 :
   if oO0 in IiI111111IIII . lower ( ) :
    i1I1iI ( ( '[COLORgreen]' + IiI111111IIII + '- Source Scooby[/COLOR]' ) , oOooo0 , 1016 , I1i111I , oOO0o0oo0 , OOo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 22 - 22: O0 - IiiIIi11I + I1II11IiII . oOo00oOO0O * i1IIi
    oO0Oo ( 'tvshows' , 'Media Info 3' )
    if 26 - 26: iIii1I11I1II1 * OOooOOo . IiiIIi11I
 I11III11III1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 81 - 81: O0 . O0
 for I1IIIIiii1i in I11III11III1 :
  o0IiiiI111I = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  I11II1i1 = OooOOOOo ( o0IiiiI111I )
  if I11II1i1 != 'Failed' :
   OOoO0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I11II1i1 )
   for IiI111111IIII , OOo0 , oOooo0 , I111iI , OooOo0oo0O0o00O , iIiii in OOoO0o :
    if oO0 in IiI111111IIII . lower ( ) :
     i1I1iI ( '[COLORgreen]' + IiI111111IIII + ' - Source Pandoras[/COLOR]' , oOooo0 , iIiii , I111iI , OooOo0oo0O0o00O , OOo0 )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 75 - 75: iIii1I11I1II1 % oo0Oo + ii11ii1ii * O0 . O0O0O - OOO0OOo
     oO0Oo ( 'tvshows' , 'Media Info 3' )
     if 32 - 32: oOo00oOO0O % ii - i1IIi
     if 40 - 40: iIii1I11I1II1 + O0O0O * I1IiI + ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1Ii1i11I1I ( ) :
 if 71 - 71: OOOo0 * i1IIi % IiiIIi11I
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 oOooo0 = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iIIiIi1iIII1 = OooOOOOo ( oOooo0 )
 oo0O0oO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , I111iI , O0i1I11I in oo0O0oO :
  I1IIi1i1Ii1I1 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I111iI ) . replace ( '\\' , '' )
  if oO0 in IiI111111IIII . lower ( ) :
   iII11I1Ii1 ( IiI111111IIII , '' , 7022 , I1IIi1i1Ii1I1 )
   if 85 - 85: OoooooooOO + Ii11I . iIii1I11I1II1 / IiiIIi11I / IiiIIi11I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: Ii11I - iIii1I11I1II1 * Ooo00oOo00o * I1II11IiII * O0
 if 98 - 98: OOO0OOo . Ii11I
def OOooO00OO ( url ) :
 O00OoOOoo = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( O00OoOOoo )
 for url , o00Oo , i1Ii , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( ( o00Oo ) . replace ( 'Sezon' , ' Season ' ) + ( i1Ii ) . replace ( 'Bölüm' , ' Episode ' ) + IiI111111IIII , url , 8063 , '' )
  if 49 - 49: i11iIiiIii - ii11ii1ii - IiiIIi11I / OoooooooOO % I1IiI
  if 65 - 65: O0 - I1II11IiII . oOo00oOO0O
  if 19 - 19: ii11ii1ii . O0O0O - OOooOOo + IiiIIi11I - oOo00oOO0O
  if 13 - 13: oo0Oo * ii11ii1ii / ii11ii1ii / iIii1I11I1II1 % iIii1I11I1II1
def i1i1IIII ( url ) :
 O00OoOOoo = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( O00OoOOoo )
 for url , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( IiI111111IIII , url , 222 , '' )
  if 95 - 95: OOOo0
  if 95 - 95: Ii11I % ii11ii1ii + OOooOOo % OOO0OOo
  if 36 - 36: O0 / i1IIi % OoOoOO00 / O0O0O
  if 96 - 96: Oo / ii . OoOoOO00 . Oo
def ooIi111iII ( ) :
 if 83 - 83: OoooooooOO + Ooo00oOo00o * ii . O0
 O00OoOOoo = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 oo0O0oO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O00OoOOoo )
 for oOooo0 , I111iI , IiI111111IIII , i1Ii in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII + '  -  ' + ( i1Ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOooo0 , 8063 , I111iI )
  if 13 - 13: OOooOOo
def IIi1ii ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII , I111iI in oo0O0oO :
  I11I1IIiiII1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 8002 , I111iI )
def Ii1i1i ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for I111iI , time , url , IiI111111IIII , iiiii1ii1 in oo0O0oO :
  i1I1iI ( '%s %s' % ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , time ) , url , 1015 , I111iI , iiiii1ii1 )
  if 83 - 83: IiiIIi11I - ii11ii1ii * ii
def oOO00OO0OooOo ( ) :
 if 13 - 13: O0 % OOO0OOo % IiiIIi11I
 iII11I1Ii1 ( 'Coronation Street' , '' , 8001 , '' )
 iII11I1Ii1 ( 'Eastenders' , '' , 8002 , '' )
 iII11I1Ii1 ( 'Emmerdale' , '' , 8003 , '' )
 iII11I1Ii1 ( 'Hollyoaks' , '' , 8004 , '' )
 iII11I1Ii1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 25 - 25: OoooooooOO % oOo00oOO0O * OoOoOO00 - Ooo00oOo00o
 if 95 - 95: OOOo0 % I1II11IiII * OOOo0 + O0 . I1II11IiII % OoooooooOO
 if 6 - 6: I1IiI - OOO0OOo * OOooOOo + I1IiI % OOooOOo
 if 100 - 100: Ooo00oOo00o % I1II11IiII - IiiIIi11I % IiiIIi11I % IiiIIi11I / OOO0OOo
def OOO000Oo ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if 'Holly' in IiI111111IIII :
   I111iI = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oOooo0 :
    I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooo0 . replace ( '\\/' , '/' ) , 8006 , I111iI )
   else :
    pass
    if 8 - 8: OOO0OOo - Oo + iIii1I11I1II1 + i1IIi * oOo00oOO0O - iIii1I11I1II1
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 30 - 30: IiiIIi11I / ii11ii1ii
def iI1iIIIIIiIi1 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if 'East' in IiI111111IIII :
   I111iI = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oOooo0 :
    I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooo0 . replace ( '\\/' , '/' ) , 8006 , I111iI )
   else :
    pass
    if 19 - 19: I1IiI . OOooOOo . OoooooooOO
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: Ii11I . Oo / OoOoOO00
def iiI1iIII1ii ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if 'Emmer' in IiI111111IIII :
   I111iI = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oOooo0 :
    I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooo0 . replace ( '\\/' , '/' ) , 8006 , I111iI )
   else :
    pass
    if 5 - 5: I1II11IiII % OoooooooOO . I1IiI
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: ii11ii1ii + oOo00oOO0O
def o0O00OooooO ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if 'Coro' in IiI111111IIII :
   I111iI = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oOooo0 :
    I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooo0 . replace ( '\\/' , '/' ) , 8006 , I111iI )
   else :
    pass
    if 77 - 77: OOOo0 % OOO0OOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: I1IiI / i1IIi % OoooooooOO
def o00o0o000Oo ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if 'Celeb' in IiI111111IIII :
   I111iI = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oOooo0 :
    I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooo0 . replace ( '\\/' , '/' ) , 8006 , I111iI )
   else :
    pass
    if 100 - 100: i1IIi - i11iIiiIii . I1II11IiII * Ooo00oOo00o
def oOIIII ( name , url ) :
 ooOOo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if ooOOo :
  i1iii1IiiiI1i1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  IiI1iiiIii = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( IiI1iiiIii ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  IiI1iiiIii = open_url ( url )
  IIIiI1i1 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( IiI1iiiIii ) [ - 1 ]
  i1iii1IiiiI1i1 = IIIiI1i1 . replace ( '\\/' , '/' )
 o0OoOoo00O = xbmcgui . ListItem ( name , '' , '' )
 o0OoOoo00O . setPath ( i1iii1IiiiI1i1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOoo00O )
 if 13 - 13: Ii11I * IiiIIi11I / O0 * OOooOOo
 if 35 - 35: i1IIi * i11iIiiIii % ii11ii1ii / oo0Oo / oo0Oo
def OO00oO0OoO0o ( ) :
 IiI1iiiIii = OooOOOOo ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 oo0O0oO = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oOooo0 , 7071 , ii11iIi1I + 'popcorn.png' )
 for oOooo0 , IiI111111IIII in iiI1IIIi :
  iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oOooo0 , 7071 , ii11iIi1I + 'popcorn.png' )
  if 5 - 5: Ii11I % Oo % oo0Oo % OOO0OOo
def I1Iiii ( ) :
 IiI1iiiIii = OooOOOOo ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 oo0O0oO = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  if 'Movies' in IiI111111IIII :
   iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( oOooo0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ii11iIi1I + 'popcorn.png' )
def I1I1Iii1Iiii ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IiI1iiiIii )
 oo0O0oO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I111iI )
 for url in iiI1IIIi :
  iII11I1Ii1 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ii11iIi1I + 'Next.png' )
  if 4 - 4: oo0Oo
  if 93 - 93: ii % i1IIi
def OOo0OOoo00 ( url ) :
 IiI1iiiIii = OooOOOOo ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 oo0O0oO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I111iI )
  if 22 - 22: OOO0OOo / OOO0OOo - oOo00oOO0O % IiiIIi11I . Ii11I + oo0Oo
  if 64 - 64: i1IIi % ii11ii1ii / oOo00oOO0O % OoooooooOO
def I1iii1 ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I111iI )
  if 19 - 19: ii % OoooooooOO . OoooooooOO
def IiIiI11IIi11Iii ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  ii11i1I1i ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 49 - 49: OoooooooOO + OoooooooOO / Ii11I . ii
def ii11i1I1i ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 222 , ii11iIi1I + 'popcorn.png' )
  if 13 - 13: OoOoOO00 . O0O0O - I1II11IiII . Ooo00oOo00o . iIii1I11I1II1
  if 66 - 66: Oo * oo0Oo
  if 83 - 83: OoooooooOO
  if 12 - 12: OOO0OOo
def I11OOO0 ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  if '(cooltvseries.com)' in IiI111111IIII :
   I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
 for url , IiI111111IIII in iiI1IIIi :
  if '(cooltvseries.com)' in IiI111111IIII :
   I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
def I1Ii1 ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  Oo0oOooOoOo ( ( url ) . replace ( ' ' , '%20' ) )
  if 67 - 67: IiiIIi11I % i11iIiiIii . iIii1I11I1II1 * OOOo0 - IiiIIi11I + oOo00oOO0O
  if 48 - 48: ii11ii1ii
def o0o ( ) :
 IiI1iiiIii = OooOOOOo ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 oo0O0oO = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII , I111iI in oo0O0oO :
  I11I1IIiiII1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( oOooo0 ) ) , 222 , I111iI )
  if 39 - 39: Ii11I + Ooo00oOo00o
def oOoOOOO0OOO ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( IiI1iiiIii )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( IiI1iiiIii )
 for I111iI , url , IiI111111IIII in oo0O0oO :
  if 'youtu' in url :
   I11I1IIiiII1 ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + I111iI )
 for url in next :
  iII11I1Ii1 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ii11iIi1I + 'Next.png' )
  if 58 - 58: IiiIIi11I % i11iIiiIii / i11iIiiIii * OOO0OOo - I1II11IiII
def i11ii111i1ii ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 97 - 97: i11iIiiIii + Oo * Ii11I % O0O0O . oo0Oo
def iiOo0 ( url ) :
 IiI1iiiIii = OooOOOOo
 oo0O0oO = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 222 , I111iI )
  if 75 - 75: Ooo00oOo00o / oOo00oOO0O + OoOoOO00 % oo0Oo . i11iIiiIii
  if 76 - 76: O0O0O . oo0Oo % O0O0O - I1II11IiII
  if 51 - 51: OoooooooOO + OOooOOo * iIii1I11I1II1 * ii / i1IIi
  if 19 - 19: O0O0O - I1IiI % ii / OoooooooOO % O0O0O
  if 65 - 65: O0 . ii
def oOoO0 ( ) :
 if 31 - 31: i11iIiiIii - OOO0OOo / ii11ii1ii - oOo00oOO0O
 iII11I1Ii1 ( 'All Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Entertainment' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Movies' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Music' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'News' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Sports' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Documentary' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Kids' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Food' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Religious' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'USA Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Other' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 if 5 - 5: i11iIiiIii * Oo
 if 29 - 29: oOo00oOO0O / OOO0OOo % IiiIIi11I
def ii1iIII1ii ( Cat_Name ) :
 if 47 - 47: IiiIIi11I . O0O0O * oOo00oOO0O - OOO0OOo . IiiIIi11I - Ii11I
 oOO0O00OoOo = False
 I1i1I11 = '0'
 if Cat_Name == 'All Channels' : oOO0O00OoOo = True
 if Cat_Name == 'Entertainment' : I1i1I11 = '1'
 if Cat_Name == 'Movies' : I1i1I11 = '2'
 if Cat_Name == 'Music' : I1i1I11 = '3'
 if Cat_Name == 'News' : I1i1I11 = '4'
 if Cat_Name == 'Sports' : I1i1I11 = '5'
 if Cat_Name == 'Documentary' : I1i1I11 = '6'
 if Cat_Name == 'Kids' : I1i1I11 = '7'
 if Cat_Name == 'Food' : I1i1I11 = '8'
 if Cat_Name == 'Religious' : I1i1I11 = '9'
 if Cat_Name == 'USA Channels' : I1i1I11 = '10'
 if Cat_Name == 'Other' : I1i1I11 = '11'
 if 9 - 9: OOOo0
 IiI1iiiIii = OooOOOOo ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oo0O0oO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IiI1iiiIii )
 print 'Len Match: >>>' + str ( len ( oo0O0oO ) )
 for IiI111111IIII , I111iI , O0i1I11I in oo0O0oO :
  I1IIi1i1Ii1I1 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I111iI ) . replace ( '\\' , '' )
  if O0i1I11I == I1i1I11 :
   iII11I1Ii1 ( IiI111111IIII , '' , 7022 , I1IIi1i1Ii1I1 )
  elif oOO0O00OoOo == True :
   iII11I1Ii1 ( IiI111111IIII , '' , 7022 , I1IIi1i1Ii1I1 )
  else : pass
  if 94 - 94: OoOoOO00
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 37 - 37: OoooooooOO
def oo0OooO ( Search_Name ) :
 IiI1iiiIii = OooOOOOo ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oo0O0oO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( IiI1iiiIii )
 oo0O0oO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( IiI1iiiIii )
 for I111iI , oOooo0 , iIII1I111III , iIIIiIi in oo0O0oO :
  I1IIi1i1Ii1I1 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I111iI ) . replace ( '\\' , '' )
  I11I1IIiiII1 ( Search_Name + ': Link 1' , ( oOooo0 ) . replace ( '\\' , '' ) , 222 , I1IIi1i1Ii1I1 )
  I11I1IIiiII1 ( Search_Name + ': Link 2' , ( iIII1I111III ) . replace ( '\\' , '' ) , 222 , I1IIi1i1Ii1I1 )
  I11I1IIiiII1 ( Search_Name + ': Link 3' , ( iIIIiIi ) . replace ( '\\' , '' ) , 222 , I1IIi1i1Ii1I1 )
  if 4 - 4: oo0Oo + iIii1I11I1II1 * O0O0O + Oo * OOooOOo % OoOoOO00
def OO0o0o0oo ( ) :
 IiI1iiiIii = OooOOOOo ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 oo0O0oO = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( IiI1iiiIii )
 for IiI111111IIII , oOooo0 in oo0O0oO :
  I11I1IIiiII1 ( IiI111111IIII , ( oOooo0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ii11iIi1I + 'english.png' )
def iIiII1 ( ) :
 IiI1iiiIii = OooOOOOo ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 oo0O0oO = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( IiI1iiiIii )
 for IiI111111IIII , oOooo0 in oo0O0oO :
  I11I1IIiiII1 ( IiI111111IIII , ( oOooo0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'xxx.png' )
def i111iii1I1 ( ) :
 IiI1iiiIii = OooOOOOo ( i1111 ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 oo0O0oO = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( IiI1iiiIii )
 for IiI111111IIII , oOooo0 in oo0O0oO :
  I11I1IIiiII1 ( IiI111111IIII , ( oOooo0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'vod(1).png' )
  if 48 - 48: OoooooooOO . I1IiI
def oOIIIi11 ( url ) :
 url
 oooOo00O0 = xbmcgui . ListItem ( IiI111111IIII , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oooOo00O0 )
 return
 if 26 - 26: I1II11IiII . oOo00oOO0O + OOOo0 . I1IiI + Ii11I
 if 17 - 17: Ii11I + i11iIiiIii + ii11ii1ii % Ii11I . ii
def I11iiIi1i1IIi ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( IiI1iiiIii )
 for url , OOo0 , I111iI , IiI111111IIII in oo0O0oO :
  i1I1iI ( IiI111111IIII , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + I111iI , '' , ( OOo0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  oO0Oo ( 'tvshows' , 'Media Info 3' )
 for url in iiI1IIIi :
  iII11I1Ii1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ii11iIi1I + 'Next.png' )
  if 46 - 46: Ooo00oOo00o . O0 * OOO0OOo / OOooOOo + OoooooooOO
def i1Ii1i1I11III ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , OOo0 , I111iI in oo0O0oO :
  OOoo0O ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + I111iI , '' , OOo0 )
  oO0Oo ( 'tvshows' , 'Media Info 3' )
 oO000o = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for I1iiIiII in oO000o :
  IIiI1111iI = ( I1iiIiII ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  i1I1iI ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I111iI , '' , IIiI1111iI )
  if 62 - 62: oOo00oOO0O + O0 * Ooo00oOo00o
def oOoOO ( INFO ) :
 i1i ( 'info for workout' , INFO )
 if 20 - 20: OOO0OOo . Ooo00oOo00o * O0O0O
 if 71 - 71: Oo . OoOoOO00 / OoOoOO00 * oOo00oOO0O * Ooo00oOo00o
 if 25 - 25: i11iIiiIii + Oo . O0O0O % OOOo0 - OOO0OOo * i1IIi
def o00OoO0o0 ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , url , 9031 , ii11iIi1I + 'icon.png' )
def o0O ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , url , 9032 , ii11iIi1I + 'icon.png' )
def OOoO0ooOOOo0 ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( IiI1iiiIii )
 for IiI111111IIII , url in oo0O0oO :
  if '://' in IiI111111IIII :
   pass
   I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ii11iIi1I + 'icon.png' )
def o0oOOO ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( IiI1iiiIii )
 for IiI111111IIII , url in oo0O0oO :
  I11I1IIiiII1 ( IiI111111IIII , url , 222 , ii11iIi1I + 'icon.png' )
  if 24 - 24: OOooOOo / oOo00oOO0O / oOo00oOO0O % OoOoOO00 - ii * ii
  if 58 - 58: I1IiI
  if 60 - 60: OoOoOO00
def oO0OOoo ( ) :
 IiI1iiiIii = OooOOOOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 oo0O0oO = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , 'http://www.disclose.tv/' + oOooo0 , 7010 , ii11iIi1I + 'disclose.png' )
  if 96 - 96: Ii11I
  if 38 - 38: O0O0O * OoooooooOO
def iIi11III ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( IiI1iiiIii )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII , I111iI in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , 'http://www.disclose.tv/' + url , 7011 , I111iI )
 for url in next :
  iII11I1Ii1 ( 'NEXT' , url , 7010 , ii11iIi1I + 'Next.png' )
  if 16 - 16: OoooooooOO * i11iIiiIii . OoooooooOO - iIii1I11I1II1 * i1IIi
  if 33 - 33: I1II11IiII % OoOoOO00
def IIi1II ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  if 'http' in url :
   I11I1IIiiII1 ( 'video/flv' , url , 222 , ii11iIi1I + 'disclose.png' )
 for url , IiI111111IIII in iiI1IIIi :
  I11I1IIiiII1 ( IiI111111IIII , url , 222 , ii11iIi1I + 'disclose.png' )
  if 40 - 40: Ii11I / oo0Oo
  if 29 - 29: oOo00oOO0O - oOo00oOO0O / OOO0OOo
def I11IIII ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ii11iIi1I + 'icon.png' )
  if 38 - 38: OoooooooOO . OOooOOo . OoOoOO00 - O0O0O
def Oooo0O ( name , url , img ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 I1iiii = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 IIIIIiiI11i1 = len ( I1iiii )
 if 43 - 43: OOOo0 / O0O0O / OOO0OOo + iIii1I11I1II1 + OoooooooOO
 if 33 - 33: OoOoOO00 - oo0Oo - OOO0OOo
 if IIIIIiiI11i1 == 1 :
  for oO00oOoo00o0 in I1iiii :
   oO00oOoo00o0 = oO00oOoo00o0 . replace ( 'player' , 'watch' )
   III1I = oO00oOoo00o0 + '&fv=&sou='
   OOOii = OooOOOOo ( III1I )
   Iii1I11 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( OOOii )
   for I11I1ii1i in Iii1I11 :
    O0o0o = False
    Resolve ( I11I1ii1i )
    if 33 - 33: OoOoOO00 % iIii1I11I1II1 / iIii1I11I1II1 + oo0Oo
 elif IIIIIiiI11i1 > 1 :
  if 76 - 76: Ooo00oOo00o * iIii1I11I1II1 + ii11ii1ii - OOO0OOo - IiiIIi11I / i1IIi
  for oO00oOoo00o0 in I1iiii :
   iI = OooOOOOo ( oO00oOoo00o0 )
   Ooo0ooo0oo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iI )
   I11iIiI1 = Ooo0ooo0oo
   I11iIiI1 = ( str ( I11iIiI1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + I11iIiI1
   I11I1IIiiII1 ( 'DOUBLE LINK' , I11iIiI1 , 424 , '' )
   if 22 - 22: oo0Oo * oOo00oOO0O - OoooooooOO
   for url in Ooo0ooo0oo :
    iII11I1Ii1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iIII1I111III = Google . resolve ( url )
    except :
     pass
    try :
     i1Ii1 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iIII1I111III ) )
     for oooOOo0oOoOO , iI1iIIII1 in i1Ii1 :
      if 65 - 65: O0 / OoOoOO00 . iIii1I11I1II1 . ii / Oo % iIii1I11I1II1
      HD_URLS . append ( oooOOo0oOoOO )
      SD_URLS . append ( iI1iIIII1 )
    except :
     pass
 else :
  pass
  if 74 - 74: i1IIi / OOOo0 % ii11ii1ii / O0 % IiiIIi11I - I1IiI
def Iiii ( ) :
 if 90 - 90: i11iIiiIii
 if 48 - 48: OoOoOO00 / Ii11I . oo0Oo
 iII11I1Ii1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ii11iIi1I + 'Movies.png' )
 if 60 - 60: I1IiI - iIii1I11I1II1 / ii11ii1ii % O0O0O * OoooooooOO - iIii1I11I1II1
 iII11I1Ii1 ( 'Search Movies' , '' , 7017 , ii11iIi1I + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 10 - 10: I1IiI % IiiIIi11I
 if 99 - 99: Oo + i11iIiiIii
def I111Ii11i11I ( ) :
 IiI1iiiIii = OooOOOOo ( 'http://cnfstudio.com/' )
 oo0O0oO = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , 'http://cnfstudio.com/genre/' + oOooo0 , 7003 , ii11iIi1I + 'icon.png' )
  if 15 - 15: IiiIIi11I / Oo * IiiIIi11I
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 20 - 20: OOO0OOo - Ii11I * Ooo00oOo00o * OOooOOo * Ii11I / oo0Oo
if 40 - 40: OOOo0 * OOooOOo . OOOo0
def o00o0O0 ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( IiI1iiiIii )
 iIIii1iiiIiiI = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( IiI1iiiIii )
 for I111iI , url , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I111iI )
 iIIii1iiiIiiI = iIIii1iiiIiiI
 for url in iIIii1iiiIiiI :
  iII11I1Ii1 ( 'Next Page' , url , 7003 , ii11iIi1I + 'Next.png' )
  if 67 - 67: OoOoOO00
def iI1iii1iIiiI ( url ) :
 if 36 - 36: Ooo00oOo00o - O0 * OOOo0 / ii11ii1ii / Ii11I
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  iI1I1i11iIIii = url + '&fv=&sou='
  iI1I1i11iIIii = iI1I1i11iIIii . replace ( 'player' , 'watch' )
  IiiIiiIIII = oOoOOOOoO0 ( iI1I1i11iIIii )
  IiiIiIIi1 = oOoOOOOoO0 ( url )
  if 40 - 40: O0O0O . I1IiI * O0
  if 6 - 6: OOOo0 - OoOoOO00 . OOOo0 + IiiIIi11I . Ii11I
def oOoOOOOoO0 ( url ) :
 if 74 - 74: i1IIi
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  IIo0o0O0O00oOOo ( url )
  if 15 - 15: i1IIi + oo0Oo % OOOo0 / i11iIiiIii * I1IiI
  if 69 - 69: i11iIiiIii
def ooOoo ( ) :
 i1I1iI ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 41 - 41: O0O0O % O0O0O - oo0Oo % Ooo00oOo00o - OoooooooOO - O0O0O
def oOOo00O0O0 ( url ) :
 oo0O0oO = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for iiIIiiI , IiI111111IIII , url in oo0O0oO :
  I11I1IIiiII1 ( IiI111111IIII , url , 222 , ii11iIi1I + 'streams.png' )
  if 90 - 90: I1II11IiII . I1IiI * OoOoOO00 % OOO0OOo
  if 36 - 36: OOOo0 - Oo % Ii11I . IiiIIi11I + IiiIIi11I + oOo00oOO0O
def II1II ( ) :
 i1I1iI ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 i1I1iI ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 48 - 48: I1II11IiII - OOooOOo % OOOo0 . OOO0OOo
 if 35 - 35: i11iIiiIii + OoooooooOO * iIii1I11I1II1 . I1II11IiII
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
I11i1i11IiIi1 = 'https://addons.tvaddons.ag/'
if 8 - 8: O0O0O - OOOo0 * Oo % ii11ii1ii * OoooooooOO
def iii11 ( ) :
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 O0OOoooo0 = 'https://addons.tvaddons.ag/search/?keyword=' + OO
 iIIiIi1iIII1 = OooOOOOo ( O0OOoooo0 )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , i111iIi1i1II1 , IiI111111IIII in oo0O0oO :
  i1I1iI ( IiI111111IIII , oOooo0 , 10054 , 'https://addons.tvaddons.ag/' + i111iIi1i1II1 , i1iiIII111ii , '' )
  if 20 - 20: Ii11I - O0O0O / Oo * Ooo00oOo00o
  if 55 - 55: OoooooooOO
def OO0OOOOOo ( ) :
 iIIiIi1iIII1 = OooOOOOo ( I11i1i11IiIi1 )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iIIiIi1iIII1 )
 for oOooo0 , I111iI , IiI111111IIII in oo0O0oO :
  if 'Repositories' in IiI111111IIII :
   pass
  elif 'Services' in IiI111111IIII :
   pass
  elif 'International' in IiI111111IIII :
   pass
  else :
   i1I1iI ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOooo0 , 10053 , 'https://addons.tvaddons.ag/' + I111iI , i1iiIII111ii , '' )
   if 7 - 7: O0 + oOo00oOO0O . OoOoOO00
   if 12 - 12: OOOo0 - i1IIi
def Addon ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 O0o00 = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( iIIiIi1iIII1 )
 for url in O0o00 :
  i1I1iI ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iIIiIi1iIII1 )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  if 'Please' in IiI111111IIII :
   pass
  else :
   i1I1iI ( IiI111111IIII , url , 10054 , 'https://addons.tvaddons.ag/' + I111iI , i1iiIII111ii , '' )
   if 8 - 8: I1II11IiII * Oo - Ii11I . iIii1I11I1II1
   if 48 - 48: i11iIiiIii / OoOoOO00 + oOo00oOO0O + OOooOOo . I1II11IiII % Ii11I
def o0Oo00OOoO0oo ( url , name ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)"' ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   IiIi1i1ii = os . path . join ( I1o0OooOOOOOO , name + '.zip' )
   try :
    os . remove ( IiIi1i1ii )
   except :
    pass
   downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
   II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print II1II1iIIi11
   print '======================================='
   extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
   OOooOoooOoOo ( )
   if 4 - 4: Ooo00oOo00o - O0O0O / i11iIiiIii * O0
def OOooOoooOoOo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 78 - 78: oo0Oo - IiiIIi11I % O0 - Ii11I % Ooo00oOo00o
 if 43 - 43: Ooo00oOo00o
def OoOooO ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1iiiIii )
 for oOooo0 , i111iIi1i1II1 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , oOooo0 , 1007 , i111iIi1i1II1 )
def I1I1i11iiiiI ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1iiiIii )
 for url , i111iIi1i1II1 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 1006 , i111iIi1i1II1 )
  if 66 - 66: ii / I1IiI
  if 13 - 13: OoOoOO00
def oO0o000oOO ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IiI1iiiIii )
 for url , I1i111I , OOo0 , OooOo0oo0O0o00O , IiI111111IIII in oo0O0oO :
  if '.php' in url :
   ooOOOoOoOOO0 ( IiI111111IIII , url , 1016 , I1i111I , OooOo0oo0O0o00O , OOo0 )
  else :
   if 'youtube' in url :
    III1I11i1iIi ( IiI111111IIII , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1i111I , OooOo0oo0O0o00O , OOo0 )
   else :
    III1I11i1iIi ( IiI111111IIII , url , 222 , I1i111I , OooOo0oo0O0o00O , OOo0 )
    oO0Oo ( 'movies' , 'INFO' )
    if 27 - 27: O0 - IiiIIi11I * OoOoOO00 - iIii1I11I1II1 / OOO0OOo
 else :
  oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1iiiIii )
  for url , i111iIi1i1II1 , IiI111111IIII in oo0O0oO :
   if '.php' in url :
    iII11I1Ii1 ( IiI111111IIII , url , 1016 , i111iIi1i1II1 )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     I11I1IIiiII1 ( IiI111111IIII , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i111iIi1i1II1 )
    else :
     I11I1IIiiII1 ( IiI111111IIII , url , 222 , i111iIi1i1II1 )
     oO0Oo ( 'movies' , 'INFO' )
     if 24 - 24: Oo / iIii1I11I1II1 % Ii11I * I1IiI - iIii1I11I1II1
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 50 - 50: OoOoOO00
def IiIIiiiIi ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1iiiIii )
 for oOooo0 , i111iIi1i1II1 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , oOooo0 , 1007 , i111iIi1i1II1 )
def IiI111 ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1iiiIii )
 for url , i111iIi1i1II1 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 1006 , i111iIi1i1II1 )
  if 82 - 82: OOOo0 % Ooo00oOo00o % IiiIIi11I + IiiIIi11I
def i1111I ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OoO00oo0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OoO00oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoO00oo0 )
 if 96 - 96: i1IIi
 if 55 - 55: ii + Ii11I + oOo00oOO0O
def OOoiII1I1i ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1iiiIii )
 for url , I111iI , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 1006 , I111iI )
def IIiii ( url ) :
 IiI1iiiIii = I1III1111iIi ( url )
 OOOO00OoooO = url
 oo0O0oO = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  if '.mp3' in IiI111111IIII :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ii11iIi1I + 'music.png' )
  else :
   iII11I1Ii1 ( ( IiI111111IIII ) . replace ( '/' , '' ) , OOOO00OoooO + url , 1011 , ii11iIi1I + 'music.png' )
def ooOoOooo00Oo ( ) :
 IiI1iiiIii = I1III1111iIi ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 oo0O0oO = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for oOooo0 , I111iI , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , ( 'http://www.cyn.net/music/' + oOooo0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I111iI ) . replace ( ' ' , '%20' ) )
def ooo00O0OOo ( url , img ) :
 IiI1iiiIii = I1III1111iIi ( url )
 iIII1I111III = url
 img = img
 oo0O0oO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( ( IiI111111IIII ) . replace ( '.mp3' , '' ) , ( iIII1I111III + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 45 - 45: OOOo0 / O0O0O + ii + oo0Oo
  if 15 - 15: OOOo0 % Ooo00oOo00o
def oOoo00oO0O0OO ( ) :
 o0OOOOoO = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO = oO0 . lower ( )
 oOooo0 = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iIII1I111III = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 iIIIiIi = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 35 - 35: i11iIiiIii % IiiIIi11I
 iIIiIi1iIII1 = iii ( oOooo0 )
 iiIiIIIiiI = iii ( iIII1I111III )
 i1i1iIII11i = iii ( iIIIiIi )
 if 39 - 39: O0 . i1IIi * ii11ii1ii - Ooo00oOo00o - O0O0O % OOooOOo
 if iIIiIi1iIII1 != 'Failed' :
  oo0O0oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIiIi1iIII1 )
  for IiI111111IIII in oo0O0oO :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( ( IiI111111IIII + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOooo0 + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 6 - 6: Ooo00oOo00o - O0O0O / OoOoOO00
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if iiIiIIIiiI != 'Failed' :
  iiI1IIIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIiIi1iIII1 )
  for IiI111111IIII in iiI1IIIi :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( ( IiI111111IIII + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIII1I111III + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 25 - 25: Oo % I1IiI
    oO0Oo ( 'tvshows' , 'Media Info 3' )
 if i1i1iIII11i != 'Failed' :
  IiiIiI = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( i1i1iIII11i )
  for IiI111111IIII in IiiIiI :
   if oO0 in IiI111111IIII . lower ( ) :
    iII11I1Ii1 ( ( IiI111111IIII + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIIIiIi + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 75 - 75: i1IIi
    oO0Oo ( 'tvshows' , 'Media Info 3' )
    if 74 - 74: Oo + I1II11IiII - ii - Ooo00oOo00o + O0O0O - iIii1I11I1II1
    if 54 - 54: ii11ii1ii + OoOoOO00 . OOOo0 / Ooo00oOo00o . OOO0OOo
    if 58 - 58: oo0Oo % i11iIiiIii * OoOoOO00 . ii11ii1ii
    if 94 - 94: i11iIiiIii . Ii11I + iIii1I11I1II1 * I1II11IiII * I1II11IiII
    if 36 - 36: IiiIIi11I - oo0Oo . oo0Oo
    if 60 - 60: i11iIiiIii * Oo % Ooo00oOo00o + Ooo00oOo00o
def ooo000o ( ) :
 IiI1iiiIii = OooOOOOo ( 'http://www.iwatchseries.me/tv-list/' )
 oo0O0oO = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , oOooo0 , 8021 , ii11iIi1I + 'iwatch.png' )
def OOOOOO ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII , I1IIIiIiIi in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII + I1IIIiIiIi , url , 8022 , ii11iIi1I + 'iwatch.png' )
def oOO0O ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oooo0 ( url )
def oooo0 ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( IiI1iiiIii )
 iiI1IIIi = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IiI1iiiIii )
 IiiIiI = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( 'VidSpot - ' + IiI111111IIII , url , 222 , ii11iIi1I + 'iwatch.png' )
 for url in iiI1IIIi :
  I11I1IIiiII1 ( 'VodLocker' , url , 222 , ii11iIi1I + 'iwatch.png' )
 for IiI111111IIII , url in IiiIiI :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   I11I1IIiiII1 ( 'TheVideo - ' + IiI111111IIII , url , 222 , ii11iIi1I + 'iwatch.png' )
   if 74 - 74: OOooOOo / ii - OoOoOO00 . OoOoOO00 . oo0Oo + OoOoOO00
def O0Ooo00o00O ( ) :
 IiI1iiiIii = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 oo0O0oO = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , oOooo0 , 1021 , ii11iIi1I + 'anime.png' )
  if 80 - 80: O0O0O
  if 3 - 3: ii11ii1ii * IiiIIi11I
def Oo00O ( ) :
 IiI1iiiIii = OooOOOOo ( 'http://www.animetoon.org/cartoon' )
 oo0O0oO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IiI1iiiIii )
 for oOooo0 , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , oOooo0 , 1002 , ii11iIi1I + 'anime.png' )
  if 44 - 44: OOO0OOo * IiiIIi11I
  if 12 - 12: oOo00oOO0O . OOOo0 % OOooOOo
  if 28 - 28: oOo00oOO0O - OOOo0 % Ooo00oOo00o * I1II11IiII
def oO0oOooO00oo ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 iiI1IIIi = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IiI1iiiIii )
 for I111iI in iiI1IIIi :
  o0I11iII = I111iI
 IiiIiI = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( IiI1iiiIii )
 for url in IiiIiI :
  iII11I1Ii1 ( 'NEXT PAGE' , url , 1002 , ii11iIi1I + 'Next.png' )
 oo0O0oO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( IiI1iiiIii )
 for url , IiI111111IIII in oo0O0oO :
  iII11I1Ii1 ( IiI111111IIII , url , 1003 , o0I11iII )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo000 ( url , IMAGE ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( IiI1iiiIii )
 for IiI111111IIII , url in oo0O0oO :
  print IiI111111IIII + '     ' + url
  if 'easy' in url :
   oOiiIIIII ( url )
  elif 'playpanda' in url :
   oOiiIIIII ( url )
   if 19 - 19: OoOoOO00 / I1IiI
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOiiIIIII ( url ) :
 IiI1iiiIii = OooOOOOo ( url )
 oo0O0oO = re . compile ( "url: '(.+?)'," ) . findall ( IiI1iiiIii )
 for url in oo0O0oO :
  I11I1IIiiII1 ( 'STREAM' , url , 222 , ii11iIi1I + 'anime.png' )
  if 80 - 80: I1IiI + iIii1I11I1II1 . oo0Oo
  if 76 - 76: OOOo0 * Ii11I
def ii111 ( url ) :
 Ooi1IIii11i1I1 = urllib2 . Request ( url )
 Ooi1IIii11i1I1 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Ooi1IIii11i1I1 . add_header ( 'referer' , url )
 Ii1I1 = urllib2 . urlopen ( Ooi1IIii11i1I1 )
 iI1I1i11iIIii = Ii1I1 . read ( )
 Ii1I1 . close ( )
 return iI1I1i11iIIii
 if 49 - 49: Ooo00oOo00o + OoOoOO00 / oo0Oo - O0 % oOo00oOO0O
def I1III1111iIi ( url ) :
 Ooi1IIii11i1I1 = urllib2 . Request ( url )
 Ooi1IIii11i1I1 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Ii1I1 = urllib2 . urlopen ( Ooi1IIii11i1I1 )
 iI1I1i11iIIii = Ii1I1 . read ( )
 Ii1I1 . close ( )
 return iI1I1i11iIIii
 if 27 - 27: Ooo00oOo00o + Oo
def oO0oOOooO0 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiI1IIIII1I = ( '%s%s' % ( I1I1IiIi1 , url ) )
 iI1I1i11iIIii = I1III1111iIi ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1I1i11iIIii )
 for url , i111iIi1i1II1 , IiI111111IIII in oo0O0oO :
  I11I1IIiiII1 ( '%s' % ( IiI111111IIII ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , i111iIi1i1II1 )
  if 62 - 62: i11iIiiIii - IiiIIi11I
def IIo0o0O0O00oOOo ( url ) :
 iiiiI1iiiIi = xbmc . Player ( OoO ( ) )
 import urlresolver
 try : iiiiI1iiiIi . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( IiI111111IIII ) )
 iiiiI1iiiIi = xbmc . Player ( OoO ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iiiiI1iiiIi . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 81 - 81: IiiIIi11I
def OOOOooO0 ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % IiI111111IIII )
 xbmc . sleep ( 1 )
 iiiiI1iiiIi = xbmc . Player ( OoO ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % IiI111111IIII )
 xbmc . sleep ( 1 )
 iiiiI1iiiIi . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 23 - 23: OOOo0 * IiiIIi11I / i11iIiiIii * I1II11IiII . iIii1I11I1II1
def Oo0oOooOoOo ( url ) :
 iiiiI1iiiIi = xbmc . Player ( OoO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iiiiI1iiiIi . play ( url ) . strip ( )
 except : pass
 if 40 - 40: OOOo0 . oOo00oOO0O / i1IIi
 if 28 - 28: oOo00oOO0O
def OoO ( ) :
 try :
  oooo00Oo0O = getSet ( "core-player" )
  if ( oooo00Oo0O == 'DVDPLAYER' ) : IiIiiIiiiiI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oooo00Oo0O == 'MPLAYER' ) : IiIiiIiiiiI = xbmc . PLAYER_CORE_MPLAYER
  elif ( oooo00Oo0O == 'PAPLAYER' ) : IiIiiIiiiiI = xbmc . PLAYER_CORE_PAPLAYER
  else : IiIiiIiiiiI = xbmc . PLAYER_CORE_AUTO
 except : IiIiiIiiiiI = xbmc . PLAYER_CORE_AUTO
 return IiIiiIiiiiI
 return True
 if 48 - 48: OOO0OOo . ii11ii1ii
def iII11I1Ii1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiiIIIIi = [ ]
  if showcontext == 'fav' :
   IiiIIIIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   IiiIIIIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0OoOoo00O . addContextMenuItems ( IiiIIIIi )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
 if 23 - 23: i1IIi + ii11ii1ii + OOOo0 - OOO0OOo % OoooooooOO . oo0Oo
def oOo00oOOOOO ( name , url , mode , iconimage , fanart , description ) :
 if 49 - 49: ii . I1IiI
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
 if 73 - 73: oOo00oOO0O / OOOo0 / OoooooooOO + OOOo0
def I11I1IIiiII1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiiIIIIi = [ ]
  if showcontext == 'fav' :
   IiiIIIIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   IiiIIIIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0OoOoo00O . addContextMenuItems ( IiiIIIIi )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = False )
 return IiiI1III1I1
 if 57 - 57: Ii11I . oOo00oOO0O % OOooOOo
 if 32 - 32: IiiIIi11I / oo0Oo - O0 * iIii1I11I1II1
 if 70 - 70: OoooooooOO % OoooooooOO % Ooo00oOo00o
 if 98 - 98: Ooo00oOo00o
 if 18 - 18: IiiIIi11I + Oo - Ooo00oOo00o / I1II11IiII / Ii11I
 if 53 - 53: Ii11I + OOooOOo . ii / IiiIIi11I
def i1i ( heading , announce ) :
 class o0000oO ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : IiIi = open ( announce ) ; ooo0oo = IiIi . read ( )
   except : ooo0oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( ooo0oo ) )
   return
 o0000oO ( )
 o0000oO ( )
 if 70 - 70: O0 / OoooooooOO + ii11ii1ii + i1IIi
def O00Oo ( ) :
 i1i ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 63 - 63: OOooOOo / O0 - OoooooooOO
 if 74 - 74: iIii1I11I1II1 / oOo00oOO0O
 if 59 - 59: oOo00oOO0O / OoOoOO00 - oo0Oo % I1IiI % OoooooooOO
 if 79 - 79: O0O0O . OoooooooOO . OOOo0 * O0 * Ooo00oOo00o - Ii11I
 if 33 - 33: ii11ii1ii . Oo + OOOo0 + OOooOOo
def OOooOoooOoOo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 54 - 54: OOO0OOo * O0O0O * O0O0O % I1IiI - Ii11I % ii11ii1ii
 if 44 - 44: Oo . Ii11I + IiiIIi11I
 if 22 - 22: I1II11IiII * OoooooooOO + i11iIiiIii % Ooo00oOo00o
 if 53 - 53: OOOo0
 if 10 - 10: I1II11IiII / i11iIiiIii - OoOoOO00
 if 48 - 48: Ii11I
 if 26 - 26: O0O0O * I1II11IiII * ii * I1IiI
 if 48 - 48: O0O0O % i11iIiiIii . OoooooooOO * oo0Oo % Ooo00oOo00o . O0O0O
 if 6 - 6: O0 . OOO0OOo - ii / i11iIiiIii
 if 84 - 84: IiiIIi11I / ii11ii1ii * OOooOOo * Ooo00oOo00o * Ii11I * O0
 if 83 - 83: O0 % OoOoOO00 + OOooOOo / OoooooooOO
 if 75 - 75: OoOoOO00 . OOOo0 + Ii11I - I1IiI - O0 . IiiIIi11I
 if 19 - 19: oOo00oOO0O * i1IIi % O0 + IiiIIi11I
 if 25 - 25: I1II11IiII - oOo00oOO0O / O0 . OoooooooOO % OOOo0 . i1IIi
 if 19 - 19: OoOoOO00 / OoOoOO00 % ii11ii1ii + ii + ii + O0O0O
 if 4 - 4: OOooOOo + IiiIIi11I / O0O0O + i1IIi % OOooOOo % O0O0O
 if 80 - 80: oOo00oOO0O
 if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 if 59 - 59: ii11ii1ii + IiiIIi11I . ii
 if 87 - 87: Ooo00oOo00o
 if 34 - 34: I1II11IiII . I1IiI / i11iIiiIii / O0O0O
 if 46 - 46: Oo + OoOoOO00 * OOOo0 + Ii11I
 if 31 - 31: oOo00oOO0O * OOooOOo * oOo00oOO0O + Ooo00oOo00o * OOooOOo . I1II11IiII
 if 89 - 89: OoooooooOO * oOo00oOO0O * OOOo0 . OOO0OOo * oOo00oOO0O / O0O0O
def iioo ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + i11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 48 - 48: Ii11I + I1II11IiII % Ii11I
def Ooo0o0000OO ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + iIiI1II1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 92 - 92: OoooooooOO . Ooo00oOo00o / Ii11I + Ooo00oOo00o
def ii1Ii11Ii1i ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + OooO0O0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 64 - 64: I1IiI % I1IiI + OOooOOo + Oo
def OO0oO0Oo ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + OoooOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 69 - 69: OoOoOO00 + O0O0O
def oooOOO ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + Iii1o00o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 84 - 84: I1IiI - Oo . OOO0OOo . oo0Oo - Oo
def o0Oo0oO00Oooo ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + Ii1II1I11i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 91 - 91: Ooo00oOo00o / Ooo00oOo00o . OoOoOO00 . OOO0OOo - OOOo0
def iii11OO0oO ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + i1i11ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 86 - 86: ii11ii1ii - i1IIi + Oo * OOOo0 / i11iIiiIii % ii
def i1i1IIi ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + o0oo0Ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 74 - 74: oOo00oOO0O + ii11ii1ii + OOOo0
def i11iII1II1I1 ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + iIIi1II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 42 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 42 - 42: iIii1I11I1II1 - OOO0OOo - IiiIIi11I - I1II11IiII
def iIiI11II ( url ) :
 iI1I1i11iIIii = OooOOOOo ( iiI1IiI + OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for IiI111111IIII , url , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO in oo0O0oO :
  i1I1iI ( IiI111111IIII , url , 5 , I1i111I , OooOo0oo0O0o00O , IIOOO0O00O0OOOO )
 oO0Oo ( 'movies' , 'MAIN' )
 if 18 - 18: OOOo0 * oo0Oo / I1IiI / ii / oOo00oOO0O * OOO0OOo
 if 51 - 51: ii
 if 34 - 34: I1IiI . i11iIiiIii * Ii11I . OOO0OOo * O0 * Ooo00oOo00o
 if 27 - 27: oOo00oOO0O . OOooOOo - I1IiI . OoOoOO00 % Oo
 if 83 - 83: IiiIIi11I + ii - iIii1I11I1II1 + OoOoOO00 . O0O0O
 if 76 - 76: OoooooooOO
 if 42 - 42: oOo00oOO0O * O0 / ii
 if 8 - 8: i1IIi + OoOoOO00 / oOo00oOO0O + ii11ii1ii % oOo00oOO0O - iIii1I11I1II1
 if 29 - 29: Oo + OoOoOO00
def oOOo00ooO ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oOOoO0 ) :
     ooOo = 0
     ooOo += len ( OOo )
     if ooOo > 0 :
      for IiIi in OOo :
       os . unlink ( os . path . join ( i1OoOO , IiIi ) )
  OOOoOo0oO0OoO = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( OOOoOo0oO0OoO )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 18 - 18: I1II11IiII . OOOo0 + OoOoOO00 / oOo00oOO0O % Oo - I1IiI
 if 92 - 92: O0O0O * OOooOOo % i1IIi / Oo - OOOo0 . O0
 if 56 - 56: oo0Oo % O0 * i1IIi - OoOoOO00
 if 74 - 74: i1IIi - I1IiI % ii . O0 - OoooooooOO
 if 84 - 84: I1II11IiII
 if 53 - 53: i1IIi
 if 59 - 59: OOooOOo + OOOo0 % OoooooooOO - iIii1I11I1II1
 if 9 - 9: i1IIi - I1IiI
 if 57 - 57: iIii1I11I1II1 * oOo00oOO0O * O0O0O / ii
def iIIiII1i1ii ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 o00Oo0O = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( o00Oo0O ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( o00Oo0O ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 17 - 17: Ooo00oOo00o
   if 31 - 31: ii + OoooooooOO - oOo00oOO0O % OOooOOo / OOooOOo / iIii1I11I1II1
   if ooOo > 0 :
    if 31 - 31: OoooooooOO - oOo00oOO0O . oo0Oo % ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 16 - 16: Ii11I * oOo00oOO0O % I1II11IiII / oo0Oo + iIii1I11I1II1 / OOOo0
     for IiIi in OOo :
      try :
       os . unlink ( os . path . join ( i1OoOO , IiIi ) )
      except :
       pass
     for I1iii11 in IIIIIo0ooOoO000oO :
      try :
       shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      except :
       pass
       if 36 - 36: Ooo00oOo00o + Ooo00oOo00o + Ooo00oOo00o % Oo * O0O0O
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  O0IIi1i = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 56 - 56: OOooOOo / oo0Oo
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( O0IIi1i ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 11 - 11: I1IiI / IiiIIi11I
   if ooOo > 0 :
    if 47 - 47: Ii11I . I1II11IiII % OoOoOO00 + Oo - ii . OoOoOO00
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( ooOo ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 37 - 37: iIii1I11I1II1 . OOOo0 % Ooo00oOo00o % OoooooooOO . OoooooooOO / O0
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 25 - 25: OoOoOO00 % OoOoOO00 - oOo00oOO0O . O0
   else :
    pass
  O00O0 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 19 - 19: OOOo0 + IiiIIi11I % OoOoOO00
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( O00O0 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 75 - 75: iIii1I11I1II1
   if ooOo > 0 :
    if 42 - 42: i11iIiiIii + I1II11IiII - OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( ooOo ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 2 - 2: OOooOOo . oOo00oOO0O % I1IiI
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 58 - 58: ii11ii1ii % oOo00oOO0O * oOo00oOO0O - O0O0O
   else :
    pass
    if 9 - 9: OOO0OOo - oOo00oOO0O % OoOoOO00 + oo0Oo + Ii11I % O0
    if 65 - 65: Ii11I - Ooo00oOo00o % i11iIiiIii
    if 58 - 58: O0O0O
    if 2 - 2: OoOoOO00 + i1IIi
 oO0OO00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( oO0OO00 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oO0OO00 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 16 - 16: OoooooooOO / ii . oOo00oOO0O * OOO0OOo - OOOo0
   if 32 - 32: OOOo0 / Ooo00oOo00o
   if ooOo > 0 :
    if 28 - 28: Oo / oo0Oo . O0O0O + Ooo00oOo00o + IiiIIi11I % Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 45 - 45: Oo / O0 % OoooooooOO
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 92 - 92: oOo00oOO0O . I1IiI . IiiIIi11I - OoooooooOO / OOO0OOo
   else :
    pass
    if 80 - 80: iIii1I11I1II1 / i11iIiiIii + O0O0O
    if 41 - 41: I1II11IiII + Ooo00oOo00o * OOOo0 * O0 * Oo - I1IiI
 ooooOoo00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( ooooOoo00 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( ooooOoo00 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 7 - 7: Ii11I * Ooo00oOo00o + OoooooooOO . OOO0OOo * IiiIIi11I
   if 82 - 82: iIii1I11I1II1 * OoooooooOO
   if ooOo > 0 :
    if 50 - 50: I1II11IiII - OoOoOO00
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: oo0Oo / oo0Oo . i11iIiiIii * ii11ii1ii + OOooOOo
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 16 - 16: oo0Oo
   else :
    pass
    if 10 - 10: I1IiI . oo0Oo * iIii1I11I1II1 - ii - I1IiI / I1II11IiII
    if 13 - 13: ii + I1IiI % oo0Oo % OoooooooOO
 iiiiI1iiiIi11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( iiiiI1iiiIi11 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( iiiiI1iiiIi11 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 52 - 52: oOo00oOO0O * Ooo00oOo00o . ii11ii1ii - I1II11IiII
   if 4 - 4: i11iIiiIii + OoooooooOO / i11iIiiIii . OoooooooOO % ii11ii1ii / I1IiI
   if ooOo > 0 :
    if 35 - 35: ii11ii1ii % i1IIi + OOooOOo - iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: OOOo0 * OoOoOO00 * I1IiI % Ii11I - Ii11I
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 35 - 35: Oo . OOO0OOo - i1IIi . I1IiI
   else :
    pass
    if 12 - 12: oo0Oo / Ooo00oOo00o / O0 * oo0Oo
    if 51 - 51: OOO0OOo * O0O0O / i1IIi
    if 2 - 2: ii + oo0Oo . O0O0O - i1IIi + I1II11IiII
 ooOOo0O0o00o00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( ooOOo0O0o00o00 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( ooOOo0O0o00o00 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 90 - 90: I1II11IiII . OoOoOO00 . ii11ii1ii
   if 32 - 32: OOO0OOo - Ooo00oOo00o . O0O0O . O0O0O % i1IIi * oOo00oOO0O
   if ooOo > 0 :
    if 65 - 65: O0O0O / OOO0OOo . OoOoOO00
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 90 - 90: IiiIIi11I
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 95 - 95: Ooo00oOo00o
   else :
    pass
    if 68 - 68: iIii1I11I1II1 . iIii1I11I1II1 / I1IiI - OoOoOO00 - iIii1I11I1II1
    if 75 - 75: OOO0OOo . OOOo0 * OoOoOO00
 ooOO0000oo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( ooOO0000oo0O ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 60 - 60: Ii11I * OOO0OOo * Ooo00oOo00o
   if 64 - 64: IiiIIi11I / OoOoOO00 / Ooo00oOo00o - OOO0OOo * iIii1I11I1II1 . O0O0O
   if ooOo > 0 :
    if 25 - 25: Ii11I - oOo00oOO0O . IiiIIi11I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 57 - 57: OOooOOo + Oo * ii11ii1ii - OOO0OOo % iIii1I11I1II1 - oOo00oOO0O
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 37 - 37: Ooo00oOo00o * IiiIIi11I + oOo00oOO0O + ii11ii1ii * OOooOOo
   else :
    pass
    if 95 - 95: oOo00oOO0O - i11iIiiIii % i11iIiiIii - O0 * I1II11IiII
    if 81 - 81: OoOoOO00 * OOOo0 % i1IIi * i11iIiiIii + I1IiI
 oo0OoOO000O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oo0OoOO000O ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 62 - 62: i1IIi * iIii1I11I1II1 % ii % I1IiI / OoooooooOO
   if 39 - 39: Oo % O0O0O
   if ooOo > 0 :
    if 90 - 90: OOOo0 * ii11ii1ii . IiiIIi11I * oOo00oOO0O - OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 40 - 40: O0 / oo0Oo - OoOoOO00 + OOooOOo % Oo
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 93 - 93: OOO0OOo
   else :
    pass
    if 82 - 82: ii11ii1ii / OOO0OOo . i11iIiiIii + Ii11I - I1IiI / O0O0O
    if 99 - 99: ii / i1IIi
 iIoOO0OO00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( iIoOO0OO00 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 75 - 75: O0O0O * Oo / I1II11IiII * Oo / OOO0OOo
   if 14 - 14: i1IIi * iIii1I11I1II1 - oOo00oOO0O * I1IiI - O0O0O / ii
   if ooOo > 0 :
    if 73 - 73: ii11ii1ii - I1IiI * O0 - I1IiI - Ooo00oOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 96 - 96: ii11ii1ii - O0
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 35 - 35: Ii11I . IiiIIi11I . I1II11IiII - IiiIIi11I % IiiIIi11I + I1II11IiII
   else :
    pass
    if 99 - 99: OOooOOo + Ii11I
    if 34 - 34: I1II11IiII * OOooOOo . OOOo0 % i11iIiiIii
 Oo0OO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( Oo0OO0 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 74 - 74: oOo00oOO0O - OoooooooOO
   if 19 - 19: iIii1I11I1II1 + I1II11IiII . I1II11IiII - Oo
   if ooOo > 0 :
    if 41 - 41: OOOo0 . Oo . oo0Oo % OoooooooOO + Ooo00oOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 23 - 23: OOOo0 - OOooOOo % ii . O0 * OoooooooOO + OOO0OOo
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 53 - 53: Oo
   else :
    pass
    if 3 - 3: oo0Oo - OoooooooOO * OoooooooOO - OOOo0 / I1II11IiII * ii11ii1ii
    if 58 - 58: oo0Oo % iIii1I11I1II1 / i11iIiiIii % OOooOOo . I1II11IiII * O0O0O
 iiI1II = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( iiI1II ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 100 - 100: I1II11IiII * Oo - iIii1I11I1II1 + OOOo0 - i1IIi + O0O0O
   if 19 - 19: I1II11IiII + O0O0O * I1II11IiII
   if ooOo > 0 :
    if 71 - 71: OOooOOo . OOOo0 - ii11ii1ii - Oo - i1IIi - OOOo0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 45 - 45: Ooo00oOo00o * Ooo00oOo00o
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 9 - 9: iIii1I11I1II1
   else :
    pass
    if 57 - 57: OOO0OOo / oOo00oOO0O % OOooOOo % i11iIiiIii
    if 95 - 95: I1II11IiII - OOooOOo
 Oooo0o00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( Oooo0o00 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 74 - 74: Oo / I1II11IiII % I1II11IiII . oo0Oo
   if 72 - 72: i1IIi
   if ooOo > 0 :
    if 21 - 21: I1II11IiII . Ii11I / i11iIiiIii * i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 82 - 82: OOO0OOo * Oo % i11iIiiIii * i1IIi . Ii11I
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 89 - 89: oo0Oo - i1IIi - oo0Oo
   else :
    pass
    if 74 - 74: Ooo00oOo00o % Ooo00oOo00o
    if 28 - 28: I1IiI % ii - Ii11I + Ii11I + ii / iIii1I11I1II1
 oo0oOOoOoo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oo0oOOoOoo ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % oOo00oOO0O
   if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
   if ooOo > 0 :
    if 60 - 60: I1II11IiII
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 77 - 77: OOOo0 / ii11ii1ii
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 95 - 95: I1II11IiII * i1IIi + ii
   else :
    pass
    if 40 - 40: OoOoOO00
    if 7 - 7: Ii11I / Ooo00oOo00o
    if 88 - 88: i1IIi
 O0ooOo0Oooo = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   I1iiIIiI11I = os . path . join ( O0ooOo0Oooo , "cache.db" )
   os . unlink ( I1iiIIiI11I )
   if 29 - 29: IiiIIi11I + ii % OOO0OOo + I1IiI
 except :
  pass
  if 92 - 92: OOooOOo
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 37 - 37: ii
 if 18 - 18: oo0Oo * i11iIiiIii + iIii1I11I1II1 % IiiIIi11I + i1IIi - Ooo00oOo00o
 if 85 - 85: Ooo00oOo00o * IiiIIi11I + Ooo00oOo00o
 if 39 - 39: Oo / i1IIi % i1IIi
 if 20 - 20: Ii11I * ii
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . Ii11I
 if 31 - 31: ii % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
 if 45 - 45: Ii11I + IiiIIi11I / OoooooooOO - oOo00oOO0O + OoooooooOO
 if 42 - 42: iIii1I11I1II1 * OOOo0 * I1II11IiII
def O00oo0o0o0oo ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1I1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( I1I1I1 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 29 - 29: ii11ii1ii
   if 91 - 91: Ooo00oOo00o
   if ooOo > 0 :
    if 54 - 54: ii11ii1ii . OOO0OOo + I1II11IiII % OOO0OOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 67 - 67: Ooo00oOo00o
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
     i1iiIIiiI111 = xbmcgui . Dialog ( )
     i1iiIIiiI111 . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    i1iiIIiiI111 . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 76 - 76: Oo
 if 38 - 38: Ii11I . O0O0O
 if 94 - 94: oo0Oo / I1II11IiII * oo0Oo - OOO0OOo
 if 89 - 89: iIii1I11I1II1
 if 31 - 31: OOO0OOo . Ii11I % OOO0OOo
 if 33 - 33: O0 * oOo00oOO0O - oo0Oo . OoooooooOO + oo0Oo
 if 20 - 20: I1II11IiII - I1IiI
 if 91 - 91: i1IIi
 if 31 - 31: i11iIiiIii + oOo00oOO0O % I1IiI
def I1I ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1I1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( I1I1I1 ) :
   ooOo = 0
   ooOo += len ( OOo )
   if 74 - 74: Oo
   if 91 - 91: Ii11I . OOOo0 % O0O0O
   if ooOo > 0 :
    if 86 - 86: OOOo0 + IiiIIi11I * I1IiI - I1II11IiII / I1II11IiII
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 9 - 9: OOooOOo / O0O0O . iIii1I11I1II1 % O0
     for IiIi in OOo :
      os . unlink ( os . path . join ( i1OoOO , IiIi ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
     i1iiIIiiI111 = xbmcgui . Dialog ( )
     i1iiIIiiI111 . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    i1iiIIiiI111 . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 iIIiII1i1ii ( url )
 if 38 - 38: O0O0O
 if 78 - 78: i11iIiiIii . oo0Oo % OoooooooOO - oo0Oo - oo0Oo + oOo00oOO0O
 if 11 - 11: IiiIIi11I
 if 20 - 20: O0 . i11iIiiIii * i1IIi % O0 . OOOo0
 if 53 - 53: OOO0OOo / OoooooooOO - OoOoOO00
 if 68 - 68: OoooooooOO . OoooooooOO . iIii1I11I1II1 / OOO0OOo - IiiIIi11I % O0
 if 19 - 19: OoooooooOO * ii
 if 60 - 60: OoOoOO00 - O0O0O + OOooOOo % Ii11I
 if 97 - 97: O0 % O0
def I1i11i1iI ( url , name ) :
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0oo0O0OO0 = os . path . join ( I1o0OooOOOOOO , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 IIiI = os . path . join ( I1o0OooOOOOOO , 'advancedsettings.xml.bak' )
 if os . path . exists ( IIiI ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o0oo0O0OO0 = os . path . join ( I1o0OooOOOOOO , 'advancedsettings.xml' )
   try :
    os . remove ( o0oo0O0OO0 )
    print '=== GenieTv - REMOVING    ' + str ( o0oo0O0OO0 ) + '    ==='
   except :
    pass
   iI1I1i11iIIii = i1 . http_GET ( url ) . content
   OOOOO0O00 = open ( o0oo0O0OO0 , "w" )
   OOOOO0O00 . write ( iI1I1i11iIIii )
   OOOOO0O00 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o0oo0O0OO0 ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o0oo0O0OO0 = os . path . join ( I1o0OooOOOOOO , 'advancedsettings.xml' )
  try :
   os . remove ( o0oo0O0OO0 )
   print '=== GenieTv - REMOVING    ' + str ( o0oo0O0OO0 ) + '    ==='
  except :
   pass
  iI1I1i11iIIii = i1 . http_GET ( url ) . content
  OOOOO0O00 = open ( o0oo0O0OO0 , "w" )
  OOOOO0O00 . write ( iI1I1i11iIIii )
  OOOOO0O00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0oo0O0OO0 ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 47 - 47: O0O0O * I1IiI * oo0Oo
def iIiii1IIi1I ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0oo0O0OO0 = os . path . join ( I1o0OooOOOOOO , 'advancedsettings.xml' )
 try :
  OOOOO0O00 = open ( o0oo0O0OO0 ) . read ( )
  if 'zero' in OOOOO0O00 :
   name = '0CACHE'
  elif 'tuxen' in OOOOO0O00 :
   name = 'TUXENS'
  elif 'muckys' in OOOOO0O00 :
   name = 'MUCKYS'
  elif 'p2p1' in OOOOO0O00 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in OOOOO0O00 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in OOOOO0O00 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 18 - 18: O0 / iIii1I11I1II1 + i11iIiiIii + Oo
def IiI1I1i1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0oo0O0OO0 = os . path . join ( I1o0OooOOOOOO , 'advancedsettings.xml' )
 try :
  os . remove ( o0oo0O0OO0 )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o0oo0O0OO0 ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 6 - 6: OOOo0 . OoOoOO00 + I1II11IiII / Ooo00oOo00o % OOOo0 . OoooooooOO
 if 64 - 64: iIii1I11I1II1 + OoOoOO00 . O0O0O % Oo * OOO0OOo
 if 7 - 7: i1IIi + i1IIi / oo0Oo
 if 32 - 32: oOo00oOO0O * ii11ii1ii - OoooooooOO / OOOo0 . OOO0OOo - i1IIi
 if 60 - 60: I1IiI % I1IiI
 if 2 - 2: oOo00oOO0O . O0 - ii + oo0Oo
 if 96 - 96: oOo00oOO0O + oOo00oOO0O
 if 28 - 28: O0O0O
 if 6 - 6: OOOo0 - O0O0O
 if 49 - 49: OoOoOO00
def II1I1Ii11 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 oo0O0oO = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for I1I1iiI , o0oOOO0 , i1Iii , oOOo0OOOOo0o in oo0O0oO :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % I1I1iiI , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % i1Iii , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % oOOo0OOOOo0o )
  inc = inc + 1
  if 29 - 29: oo0Oo - IiiIIi11I . O0 . O0
  if 16 - 16: i1IIi * OOO0OOo % Ooo00oOo00o + oOo00oOO0O
  if 50 - 50: ii - OoooooooOO + O0O0O % Ooo00oOo00o
  if 12 - 12: i1IIi / ii11ii1ii - O0O0O . i11iIiiIii / i1IIi / OoooooooOO
  if 88 - 88: oOo00oOO0O / i11iIiiIii % I1IiI % Ii11I
  if 70 - 70: ii11ii1ii . ii11ii1ii / IiiIIi11I . ii11ii1ii
  if 37 - 37: i1IIi . I1II11IiII - OoOoOO00 % OOooOOo - i1IIi . ii
  if 34 - 34: iIii1I11I1II1 / OoOoOO00
  if 3 - 3: OOooOOo - OoooooooOO + O0O0O . IiiIIi11I
def o00000Oo ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0oo0O0OO0 = os . path . join ( I1o0OooOOOOOO , 'addons2.ini' )
  iI1I1i11iIIii = i1 . http_GET ( url ) . content
  OOOOO0O00 = open ( o0oo0O0OO0 , "w" )
  OOOOO0O00 . write ( iI1I1i11iIIii )
  OOOOO0O00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0oo0O0OO0 ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 63 - 63: OoOoOO00 * OOOo0 - OoooooooOO / OOOo0
def III11II111 ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  I1o0OooOOOOOO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0oo0O0OO0 = os . path . join ( I1o0OooOOOOOO , 'settings.xml' )
  iI1I1i11iIIii = i1 . http_GET ( url ) . content
  OOOOO0O00 = open ( o0oo0O0OO0 , "w" )
  OOOOO0O00 . write ( iI1I1i11iIIii )
  OOOOO0O00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0oo0O0OO0 ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 8 - 8: i11iIiiIii
 if 4 - 4: i11iIiiIii
def i11iII1 ( ) :
 try :
  oOooo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( oOooo ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    i11iI1111ii1I = os . path . join ( oOooo , "source.db" )
    os . unlink ( i11iI1111ii1I )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 89 - 89: i11iIiiIii / O0 - i1IIi % Oo + i11iIiiIii
 if 44 - 44: i11iIiiIii / Ii11I * OOO0OOo
 if 88 - 88: i1IIi % Ii11I / OoooooooOO * O0O0O % OOO0OOo
 if 5 - 5: ii11ii1ii * oOo00oOO0O % IiiIIi11I % OoOoOO00
 if 9 - 9: OOooOOo % I1II11IiII + IiiIIi11I
def OooOOOOo ( url ) :
 Ooi1IIii11i1I1 = urllib2 . Request ( url )
 Ooi1IIii11i1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ii1I1 = urllib2 . urlopen ( Ooi1IIii11i1I1 )
 iI1I1i11iIIii = Ii1I1 . read ( )
 Ii1I1 . close ( )
 return iI1I1i11iIIii
 if 55 - 55: Ooo00oOo00o - ii11ii1ii
 if 38 - 38: iIii1I11I1II1 % oo0Oo % Ooo00oOo00o % O0 * iIii1I11I1II1 / I1II11IiII
 if 65 - 65: Ii11I - OOOo0 * I1II11IiII
 if 99 - 99: OOOo0
 if 64 - 64: ii11ii1ii * oOo00oOO0O * Oo % oo0Oo % OOO0OOo
 if 55 - 55: OoOoOO00 - I1II11IiII - Ii11I % oOo00oOO0O
 if 49 - 49: Oo * I1II11IiII
def OOO0 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; I11ii1I = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if I11ii1I :
  i1iIi1iiii1ii = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; i1iIi1iiii1ii = xbmc . translatePath ( i1iIi1iiii1ii ) ;
  oO0oOo = os . path . join ( i1iIi1iiii1ii , ".." , ".." ) ; oO0oOo = os . path . abspath ( oO0oOo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + oO0oOo ) ; IIiIiii = False
  try :
   for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oO0oOo , topdown = True ) :
    IIIIIo0ooOoO000oO [ : ] = [ I1iii11 for I1iii11 in IIIIIo0ooOoO000oO if I1iii11 not in iiIIIII1i1iI ]
    for IiI111111IIII in OOo :
     try : os . remove ( os . path . join ( i1OoOO , IiI111111IIII ) )
     except :
      if IiI111111IIII not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIiIiii = True
      plugintools . log ( "Error removing " + i1OoOO + " " + IiI111111IIII )
    for IiI111111IIII in IIIIIo0ooOoO000oO :
     try : os . rmdir ( os . path . join ( i1OoOO , IiI111111IIII ) )
     except :
      if IiI111111IIII not in [ "Database" , "userdata" ] : IIiIiii = True
      plugintools . log ( "Error removing " + i1OoOO + " " + IiI111111IIII )
   if not IIiIiii : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OoOoO00O0 ( )
 if 71 - 71: OOooOOo + Ii11I . Oo - I1IiI * i11iIiiIii . I1IiI
 if 91 - 91: O0 - IiiIIi11I % I1II11IiII
 if 46 - 46: OOO0OOo / OOOo0 . oo0Oo % Ooo00oOo00o / i11iIiiIii
def I1III1I1IiI ( ) :
 ooooooo0oOo0 = [ ]
 OooO00oO00o = sys . argv [ 2 ]
 if len ( OooO00oO00o ) >= 2 :
  IIII1iI1IiIiI = sys . argv [ 2 ]
  i1II1 = IIII1iI1IiIiI . replace ( '?' , '' )
  if ( IIII1iI1IiIiI [ len ( IIII1iI1IiIiI ) - 1 ] == '/' ) :
   IIII1iI1IiIiI = IIII1iI1IiIiI [ 0 : len ( IIII1iI1IiIiI ) - 2 ]
  OoOoOoo0oOOooo0o = i1II1 . split ( '&' )
  ooooooo0oOo0 = { }
  for iI1i1iiii in range ( len ( OoOoOoo0oOOooo0o ) ) :
   III = { }
   III = OoOoOoo0oOOooo0o [ iI1i1iiii ] . split ( '=' )
   if ( len ( III ) ) == 2 :
    ooooooo0oOo0 [ III [ 0 ] ] = III [ 1 ]
    if 1 - 1: I1II11IiII . O0O0O * I1IiI / O0 + ii + OOooOOo
 return ooooooo0oOo0
 if 81 - 81: iIii1I11I1II1
OOO00OO0oOo = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
IIIIi1I = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
I1I1iI = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OOO00O = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
IIIIIiI111I = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
iIO0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
i11I = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
o00oO00O0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
iIiI1II1I1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OooO0O0oo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OoooOO0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Iii1o00o0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Ii1II1I11i1I = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
i1i11ii = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
o0oo0Ooo0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iIIi1II1 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
IIi11IIiIii1 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
I1Iii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
ii1oOoO0o0ooo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oOo00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
Oo000o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OooOOOOoO00OoOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
OO0 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
I1I1IiIi1 = base64 . decodestring ( 'Q1VOVA==' )
def i1I1iI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiiIIIIi = [ ]
  if showcontext == 'fav' :
   IiiIIIIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   IiiIIIIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  o0OoOoo00O . addContextMenuItems ( IiiIIIIi )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
 if 9 - 9: ii . Oo + O0O0O + OOOo0 * OOOo0 - OOOo0
def OOoo0O ( name , url , mode , iconimage , fanart , description ) :
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = False )
 return IiiI1III1I1
 if 95 - 95: oo0Oo + Ii11I % ii * Ii11I
 if 58 - 58: I1IiI . OOooOOo + ii
IIII1iI1IiIiI = I1III1I1IiI ( )
oOooo0 = None
IiI111111IIII = None
iIiii = None
I1i111I = None
OooOo0oo0O0o00O = None
IIOOO0O00O0OOOO = None
iiIi1 = None
if 91 - 91: OOOo0 + OOooOOo % OoOoOO00 + Ooo00oOo00o
if 66 - 66: iIii1I11I1II1 * OoOoOO00 % Oo % OOOo0 - oOo00oOO0O
try :
 iiIi1 = int ( IIII1iI1IiIiI [ "fav_mode" ] )
except :
 pass
 if 59 - 59: oo0Oo % ii
try :
 oOooo0 = urllib . unquote_plus ( IIII1iI1IiIiI [ "url" ] )
except :
 pass
try :
 IiI111111IIII = urllib . unquote_plus ( IIII1iI1IiIiI [ "name" ] )
except :
 pass
try :
 I1i111I = urllib . unquote_plus ( IIII1iI1IiIiI [ "iconimage" ] )
except :
 pass
try :
 iIiii = int ( IIII1iI1IiIiI [ "mode" ] )
except :
 pass
try :
 OooOo0oo0O0o00O = urllib . unquote_plus ( IIII1iI1IiIiI [ "fanart" ] )
except :
 pass
try :
 IIOOO0O00O0OOOO = urllib . unquote_plus ( IIII1iI1IiIiI [ "description" ] )
except :
 pass
 if 21 - 21: OoooooooOO % I1IiI - I1IiI / ii11ii1ii / OOooOOo
 if 15 - 15: OOO0OOo / OOO0OOo % OoooooooOO . I1II11IiII
print str ( O0OoO000O0OO ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( iIiii )
print "URL: " + str ( oOooo0 )
print "Name: " + str ( IiI111111IIII )
print "IconImage: " + str ( I1i111I )
if 93 - 93: ii11ii1ii * ii11ii1ii / OoooooooOO
if 6 - 6: ii11ii1ii * Oo + iIii1I11I1II1
def oO0Oo ( content , viewType ) :
 if 19 - 19: O0 % OoOoOO00 * OOooOOo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 27 - 27: Ii11I * oo0Oo / i11iIiiIii - ii + OoOoOO00
  if 43 - 43: ii11ii1ii - OoOoOO00
if iIiii == None :
 OOO0OOO00oo ( )
 if 56 - 56: ii11ii1ii . i1IIi / O0O0O % ii / O0 * IiiIIi11I
elif iIiii == 1 :
 i11i1iIiii ( oOooo0 )
 if 98 - 98: O0 + O0O0O
elif iIiii == 44 :
 iIiIi11Ii ( oOooo0 )
 if 23 - 23: OoooooooOO . iIii1I11I1II1 / i1IIi
elif iIiii == 2 :
 iioOo0OoOOo0 ( )
 if 31 - 31: Oo - iIii1I11I1II1 / IiiIIi11I . Ooo00oOo00o
elif iIiii == 3 :
 OoO00 ( )
 if 74 - 74: Oo - OoOoOO00 - oo0Oo
elif iIiii == 21 :
 iI1Ii11111iIi ( )
 if 50 - 50: OOOo0 - ii + ii * IiiIIi11I + ii
elif iIiii == 4 :
 I1Iiiiiii ( )
 if 70 - 70: i1IIi % Ooo00oOo00o / i1IIi
elif iIiii == 5 :
 i11i11 ( IiI111111IIII , oOooo0 , IIOOO0O00O0OOOO )
 if 30 - 30: I1IiI - i11iIiiIii
elif iIiii == 6 :
 O00oo0o0o0oo ( oOooo0 )
 if 94 - 94: I1IiI % O0O0O
elif iIiii == 7 :
 I1i11i1iI ( oOooo0 , IiI111111IIII )
 if 39 - 39: I1IiI + I1II11IiII % O0
elif iIiii == 8 :
 iIiii1IIi1I ( oOooo0 , IiI111111IIII )
 if 26 - 26: OOO0OOo + I1IiI
elif iIiii == 9 :
 FIXREPOSADDONS ( oOooo0 )
 if 17 - 17: ii11ii1ii - O0O0O % Oo * O0 % O0 * Ii11I
elif iIiii == 10 :
 OOooOoooOoOo ( )
 if 6 - 6: I1II11IiII
elif iIiii == 11 :
 IiI1I1i1 ( oOooo0 )
 if 46 - 46: OoOoOO00 * I1II11IiII
elif iIiii == 12 :
 II1I1Ii11 ( )
 if 23 - 23: i1IIi - O0
elif iIiii == 13 :
 oOOo00ooO ( )
 if 6 - 6: OOO0OOo % OoooooooOO * I1II11IiII - oo0Oo
elif iIiii == 14 :
 iIIiII1i1ii ( oOooo0 )
 if 24 - 24: IiiIIi11I / iIii1I11I1II1 . OoooooooOO % I1IiI . oOo00oOO0O
elif iIiii == 15 :
 OOO ( )
 if 73 - 73: I1II11IiII
elif iIiii == 16 :
 o00000Oo ( oOooo0 , IiI111111IIII )
 if 25 - 25: oo0Oo
elif iIiii == 17 :
 III11II111 ( oOooo0 , IiI111111IIII )
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
elif iIiii == 18 :
 i11iII1 ( )
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . oOo00oOO0O - Oo . i11iIiiIii
elif iIiii == 19 :
 ii1iIi1II ( IiI111111IIII , oOooo0 , IIOOO0O00O0OOOO )
 if 47 - 47: Oo % Ooo00oOo00o - OOO0OOo - Oo * ii
elif iIiii == 40 :
 iioo0o0OoOOO ( IiI111111IIII , oOooo0 , IIOOO0O00O0OOOO )
 if 72 - 72: OOooOOo % OOooOOo + O0O0O + ii11ii1ii / Oo
elif iIiii == 42 :
 IiIi1II11i ( IiI111111IIII , oOooo0 , IIOOO0O00O0OOOO )
 if 30 - 30: Oo + OOOo0 + i11iIiiIii / Ooo00oOo00o
elif iIiii == 43 :
 IIii1i1iii1 ( IiI111111IIII , oOooo0 , IIOOO0O00O0OOOO )
 if 64 - 64: oo0Oo
elif iIiii == 20 :
 I111 ( oOooo0 )
 if 80 - 80: OOOo0 - i11iIiiIii / Ooo00oOo00o / I1IiI + I1IiI
elif iIiii == 22 :
 iioo ( oOooo0 )
 if 89 - 89: O0 + oo0Oo * I1II11IiII
elif iIiii == 23 :
 Ooo0o0000OO ( oOooo0 )
 if 30 - 30: I1IiI
elif iIiii == 24 :
 ii1Ii11Ii1i ( oOooo0 )
 if 39 - 39: ii11ii1ii + OOooOOo + I1II11IiII + oo0Oo
elif iIiii == 25 :
 OO0oO0Oo ( oOooo0 )
 if 48 - 48: I1II11IiII / OOO0OOo . iIii1I11I1II1
elif iIiii == 26 :
 oooOOO ( oOooo0 )
 if 72 - 72: i1IIi . OOooOOo
elif iIiii == 27 :
 o0Oo0oO00Oooo ( oOooo0 )
 if 3 - 3: I1IiI % OoOoOO00 - O0
elif iIiii == 28 :
 iii11OO0oO ( oOooo0 )
 if 52 - 52: Ooo00oOo00o
elif iIiii == 29 :
 i1i1IIi ( oOooo0 )
 if 49 - 49: oOo00oOO0O . ii11ii1ii % OOO0OOo . Oo * Ii11I
elif iIiii == 30 :
 Ooo0oo ( oOooo0 )
 if 44 - 44: iIii1I11I1II1 / O0 * Oo + OOOo0 . OOO0OOo
elif iIiii == 31 :
 i11iII1II1I1 ( oOooo0 )
 if 20 - 20: O0O0O + OOooOOo . I1II11IiII / i11iIiiIii
elif iIiii == 32 :
 IiII1II11I ( )
 if 7 - 7: I1IiI / I1IiI . I1II11IiII * O0 + oo0Oo + ii
elif iIiii == 33 :
 iiiiI1i1i ( )
 if 98 - 98: OoOoOO00 * oo0Oo - OOOo0 % OOooOOo - O0O0O % ii11ii1ii
elif iIiii == 35 :
 OoOOoO000O00oO ( oOooo0 )
 if 69 - 69: i1IIi % Ooo00oOo00o % I1II11IiII / OOO0OOo / OOO0OOo
elif iIiii == 34 :
 o000O000 ( oOooo0 )
 if 6 - 6: OoOoOO00 % ii11ii1ii % i1IIi * OOO0OOo
elif iIiii == 36 :
 oO0oOOoo00000 ( oOooo0 )
 if 47 - 47: O0
elif iIiii == 37 :
 Ii1IIiiIIi ( oOooo0 )
 if 55 - 55: Ooo00oOo00o % O0 / OoooooooOO
elif iIiii == 38 :
 O0oOo00o0 ( oOooo0 )
 if 49 - 49: OOOo0 . Ooo00oOo00o * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
elif iIiii == 41 :
 OOO0 ( IIII1iI1IiIiI )
 if 88 - 88: ii11ii1ii * O0O0O + OoOoOO00
elif iIiii == 39 :
 iIiI11II ( oOooo0 )
 if 62 - 62: OoooooooOO
elif iIiii == 45 :
 TEXTS ( )
 if 33 - 33: O0 . i11iIiiIii % OOooOOo
elif iIiii == 46 :
 O00Oo ( )
 if 50 - 50: OOO0OOo
elif iIiii == 47 :
 GEVID ( )
 if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo * Ii11I
elif iIiii == 48 :
 OOooO ( IiI111111IIII , oOooo0 , IIOOO0O00O0OOOO )
 if 83 - 83: i11iIiiIii - OOOo0 * i11iIiiIii
elif iIiii == 49 :
 o0iiiI1I1iIIIi1 ( )
 if 59 - 59: O0O0O - OoooooooOO / OOO0OOo + ii11ii1ii . OOooOOo - O0O0O
elif iIiii == 222 :
 IIo0o0O0O00oOOo ( oOooo0 )
 if 29 - 29: ii
elif iIiii == 333 :
 oO0oOOooO0 ( oOooo0 )
 if 26 - 26: O0 % Ii11I - oo0Oo . Ii11I
 if 70 - 70: OOooOOo + IiiIIi11I / O0O0O + OOO0OOo / OOOo0
elif iIiii == 1020 :
 O0Ooo00o00O ( )
 if 33 - 33: OoooooooOO . O0
elif iIiii == 1021 :
 ANIMEEP ( )
 if 59 - 59: iIii1I11I1II1
elif iIiii == 1022 :
 ANIMEPLAY ( oOooo0 )
 if 45 - 45: O0
elif iIiii == 1001 :
 Oo00O ( )
 if 78 - 78: IiiIIi11I - iIii1I11I1II1 + I1II11IiII - ii11ii1ii - I1II11IiII
elif iIiii == 1005 :
 IiIIiiiIi ( )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
elif iIiii == 1007 :
 IiI111 ( oOooo0 )
 if 86 - 86: I1IiI / Ii11I
elif iIiii == 1010 :
 OOoiII1I1i ( oOooo0 )
 if 40 - 40: iIii1I11I1II1 / OOO0OOo / OOOo0 + ii11ii1ii * Ii11I
elif iIiii == 1011 :
 IIiii ( oOooo0 )
 if 1 - 1: Ooo00oOo00o * OOO0OOo + oo0Oo . ii / OOO0OOo
elif iIiii == 1030 :
 ooOoOooo00Oo ( )
 if 91 - 91: oOo00oOO0O + IiiIIi11I - Oo % I1IiI . O0O0O
elif iIiii == 1031 :
 ooo00O0OOo ( oOooo0 , I1i111I )
 if 51 - 51: Ii11I / IiiIIi11I
elif iIiii == 1006 :
 Parse . ParseURL ( oOooo0 )
 if 51 - 51: OOO0OOo * ii - I1II11IiII + O0O0O
elif iIiii == 2030 :
 Parse . addonParseURL ( oOooo0 )
 if 46 - 46: OOooOOo - i11iIiiIii % Ooo00oOo00o / oOo00oOO0O - I1IiI
elif iIiii == 2031 :
 Parse . apkParseURL ( oOooo0 )
 if 88 - 88: ii * OOOo0 / Ooo00oOo00o - Ii11I / i1IIi . I1II11IiII
elif iIiii == 1002 :
 oO0oOooO00oo ( oOooo0 )
 if 26 - 26: i11iIiiIii - OOO0OOo
elif iIiii == 1003 :
 Oo000 ( oOooo0 , I1i111I )
 if 45 - 45: OOO0OOo + OoOoOO00 % O0O0O
elif iIiii == 1004 :
 oOiiIIIII ( oOooo0 )
 if 55 - 55: OOO0OOo - ii % OOOo0
elif iIiii == 1008 :
 o0o ( )
 if 61 - 61: OOO0OOo
elif iIiii == 1009 :
 M3UPLAY ( oOooo0 )
 if 22 - 22: iIii1I11I1II1 / OOO0OOo / OOOo0 - OOooOOo
elif iIiii == 2001 :
 oOOo00O0O0 ( oOooo0 )
 if 21 - 21: ii . i11iIiiIii * IiiIIi11I . Ii11I / Ii11I
elif iIiii == 1013 :
 IIiI1I1 ( )
 if 42 - 42: OoooooooOO / I1II11IiII . OOooOOo / O0 - oo0Oo * oo0Oo
elif iIiii == 1014 :
 IIi1ii ( )
 if 1 - 1: oOo00oOO0O % I1II11IiII
elif iIiii == 1015 :
 Ii1i1i ( oOooo0 )
 if 97 - 97: I1IiI
elif iIiii == 1016 :
 oO0o000oOO ( oOooo0 )
 if 13 - 13: I1IiI % Ii11I . O0 / Oo % Oo
elif iIiii == 1023 :
 i1iiIiI1Ii1i ( )
 if 19 - 19: I1II11IiII % OOO0OOo - OOO0OOo % OOOo0 . Ii11I - OoooooooOO
elif iIiii == 1024 :
 OoOooO ( )
 if 100 - 100: OOOo0 + oOo00oOO0O + OOooOOo . i1IIi % OoooooooOO
elif iIiii == 1025 :
 I1I1i11iiiiI ( oOooo0 )
 if 64 - 64: O0 % i1IIi * I1II11IiII - oOo00oOO0O + Oo
elif iIiii == 4001 :
 I1I111 ( )
 if 65 - 65: I1IiI . i11iIiiIii
elif iIiii == 4002 :
 i11iiI111I ( )
 if 36 - 36: ii * O0O0O + oo0Oo * O0O0O . ii11ii1ii - iIii1I11I1II1
elif iIiii == 4003 :
 Oo00OoOo ( )
 if 14 - 14: IiiIIi11I * ii + i11iIiiIii
elif iIiii == 4004 :
 iII ( )
 if 84 - 84: O0O0O / OoOoOO00
elif iIiii == 4005 :
 I1 ( )
 if 86 - 86: OOOo0
elif iIiii == 4006 :
 iiIii ( )
 if 97 - 97: OoOoOO00
elif iIiii == 4007 :
 O0oOoOOOoOO ( )
 if 38 - 38: OOOo0
elif iIiii == 4008 :
 ii1ii11IIIiiI ( )
 if 42 - 42: OOooOOo
elif iIiii == 4009 : oO00o0 ( )
elif iIiii == 4010 : O0oo0O ( )
elif iIiii == 3000 :
 ooOoo ( )
 if 8 - 8: i11iIiiIii / OOO0OOo
elif iIiii == 3001 :
 I111I1I ( )
 if 33 - 33: I1II11IiII * oo0Oo - O0 + OOOo0 / oo0Oo
elif iIiii == 3002 :
 Oo0000 ( oOooo0 )
 if 19 - 19: i1IIi % OoOoOO00
elif iIiii == 3003 :
 oO0OoOo ( oOooo0 )
 if 85 - 85: oo0Oo - OOooOOo % Ii11I - OoOoOO00
elif iIiii == 3004 :
 i1I11ii ( oOooo0 )
 if 56 - 56: oOo00oOO0O * i11iIiiIii
elif iIiii == 404 :
 i1111I ( IiI111111IIII , oOooo0 , I1i111I )
 if 92 - 92: OoOoOO00 - O0 . I1II11IiII
elif iIiii == 405 :
 OOOOooO0 ( oOooo0 )
 if 59 - 59: I1IiI
elif iIiii == 7030 :
 oOoO0 ( )
 if 47 - 47: OoOoOO00 - ii11ii1ii - oOo00oOO0O
elif iIiii == 7021 :
 ii1iIII1ii ( IiI111111IIII )
 if 9 - 9: ii11ii1ii - oo0Oo
elif iIiii == 7022 :
 oo0OooO ( IiI111111IIII )
 if 64 - 64: i1IIi
elif iIiii == 7000 :
 Oooo0O ( IiI111111IIII , oOooo0 , img )
 if 71 - 71: oo0Oo * OOooOOo
elif iIiii == 7050 :
 oOoOOOO0OOO ( oOooo0 )
 if 99 - 99: OOooOOo
elif iIiii == 7051 :
 i11ii111i1ii ( oOooo0 )
 if 28 - 28: OoooooooOO % O0 - Ii11I / OOooOOo / OOOo0
elif iIiii == 7052 :
 I11OOO0 ( oOooo0 )
 if 41 - 41: OoOoOO00 * oo0Oo / Ooo00oOo00o . ii
elif iIiii == 7053 :
 I1Ii1 ( oOooo0 )
 if 50 - 50: OoooooooOO + iIii1I11I1II1 / ii / Ii11I . i11iIiiIii . OOO0OOo
elif iIiii == 7054 :
 CoolPlay ( oOooo0 )
 if 75 - 75: iIii1I11I1II1 % OOO0OOo / Ii11I - O0O0O % i11iIiiIii
elif iIiii == 7060 :
 I1Iiii ( )
 if 11 - 11: IiiIIi11I . oOo00oOO0O
elif iIiii == 7061 :
 OOo0OOoo00 ( oOooo0 )
 if 87 - 87: Ii11I + Ii11I
elif iIiii == 7063 :
 I1I1Iii1Iiii ( oOooo0 )
 if 45 - 45: i1IIi - Oo
elif iIiii == 7062 :
 I1iii1 ( oOooo0 )
 if 87 - 87: I1IiI - Ooo00oOo00o * Ooo00oOo00o / oOo00oOO0O . IiiIIi11I * OOooOOo
elif iIiii == 7064 :
 NATatozcat ( )
 if 21 - 21: OoOoOO00
elif iIiii == 7067 :
 IiIiI11IIi11Iii ( oOooo0 )
 if 29 - 29: I1IiI % oOo00oOO0O
elif iIiii == 7066 :
 NATatozA ( oOooo0 )
 if 7 - 7: i1IIi / oo0Oo / O0O0O
elif iIiii == 7065 :
 ii11i1I1i ( oOooo0 )
 if 97 - 97: Ooo00oOo00o + iIii1I11I1II1
elif iIiii == 7070 :
 OO00oO0OoO0o ( )
 if 79 - 79: OOO0OOo + ii - OoOoOO00 . Oo
elif iIiii == 7071 :
 DIZIlist ( oOooo0 )
 if 26 - 26: oo0Oo
elif iIiii == 7072 :
 DIZIpull ( oOooo0 )
 if 52 - 52: O0 + OOO0OOo
elif iIiii == 7073 :
 WATCHDIZI ( oOooo0 )
 if 11 - 11: i1IIi / I1II11IiII * ii11ii1ii * I1II11IiII * OOO0OOo - i11iIiiIii
elif iIiii == 7002 :
 I111Ii11i11I ( )
 if 96 - 96: ii11ii1ii % ii11ii1ii
elif iIiii == 7003 :
 o00o0O0 ( oOooo0 )
 if 1 - 1: OOOo0 . oOo00oOO0O
elif iIiii == 7004 :
 iI1iii1iIiiI ( oOooo0 )
 if 26 - 26: ii - OOO0OOo % Oo - ii + oo0Oo
elif iIiii == 7020 :
 oOoOOOOoO0 ( oOooo0 )
 if 33 - 33: oOo00oOO0O + I1IiI - ii11ii1ii + iIii1I11I1II1 % i1IIi * oo0Oo
elif iIiii == 7001 :
 oO0OOoo ( )
 if 21 - 21: O0 * OOO0OOo % Ooo00oOo00o
elif iIiii == 7010 :
 iIi11III ( oOooo0 )
 if 14 - 14: O0 / I1II11IiII / OOO0OOo + oo0Oo - oo0Oo
elif iIiii == 7011 :
 IIi1II ( oOooo0 )
 if 10 - 10: O0 - ii11ii1ii / I1II11IiII % I1IiI / OoooooooOO / oOo00oOO0O
elif iIiii == 7012 :
 I11IIII ( oOooo0 )
 if 73 - 73: OOO0OOo + oo0Oo % OOooOOo . ii11ii1ii / Ii11I . I1II11IiII
elif iIiii == 7013 :
 cnfTVPlay2 ( oOooo0 )
elif iIiii == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oOooo0 )
elif iIiii == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oOooo0 )
elif iIiii == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( IiI111111IIII , oOooo0 , I1i111I )
elif iIiii == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iIiii == 7018 :
 Iiii ( )
elif iIiii == 7019 :
 CNF_Studio_Indexer . List_Movies ( oOooo0 )
elif iIiii == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oOooo0 )
elif iIiii == 7024 :
 CNF_Studio_Indexer . Box_Office ( oOooo0 )
 if 76 - 76: IiiIIi11I . ii11ii1ii * OoooooooOO % O0O0O
elif iIiii == 8000 :
 oOO00OO0OooOo ( )
elif iIiii == 8001 :
 o0O00OooooO ( )
elif iIiii == 8002 :
 iI1iIIIIIiIi1 ( )
elif iIiii == 8003 :
 iiI1iIII1ii ( )
elif iIiii == 8004 :
 OOO000Oo ( )
elif iIiii == 8005 :
 o00o0o000Oo ( )
elif iIiii == 8006 :
 oOIIII ( IiI111111IIII , oOooo0 )
elif iIiii == 8030 :
 Oo00oo0000OO ( oOooo0 )
elif iIiii == 8045 :
 ii1oOoO0ooO0000 ( oOooo0 )
elif iIiii == 8046 :
 OOOOO ( oOooo0 )
elif iIiii == 8047 :
 I1iiiI ( oOooo0 )
elif iIiii == 8020 :
 ooo000o ( )
elif iIiii == 8021 :
 OOOOOO ( oOooo0 )
elif iIiii == 8022 :
 oOO0O ( oOooo0 )
elif iIiii == 8023 :
 oooo0 ( oOooo0 )
elif iIiii == 8040 :
 Oo0 ( )
elif iIiii == 8041 :
 O0000Oo00o ( oOooo0 )
elif iIiii == 8042 :
 Iiii1 ( oOooo0 )
elif iIiii == 8043 :
 yt . PlayVideo ( oOooo0 )
elif iIiii == 8044 :
 iI111II1ii ( oOooo0 )
elif iIiii == 8060 :
 i1iI1i ( )
elif iIiii == 8061 :
 o0o0OoO0OOO0 ( oOooo0 )
elif iIiii == 8064 :
 ii1IIiII111I ( )
elif iIiii == 8065 :
 O00OoOoO ( oOooo0 )
elif iIiii == 8070 :
 ii1ii1i11I1I ( )
elif iIiii == 8071 :
 iiII1iiiiiii ( oOooo0 )
elif iIiii == 7080 :
 iiIiii ( oOooo0 )
elif iIiii == 8090 :
 Ooo00O0 ( )
elif iIiii == 8091 :
 OoO0OOoO0 ( oOooo0 )
elif iIiii == 8092 :
 iiI11i ( oOooo0 )
elif iIiii == 8081 :
 ooIi111iII ( )
elif iIiii == 8062 :
 OOooO00OO ( oOooo0 )
elif iIiii == 8063 :
 i1i1IIII ( oOooo0 )
elif iIiii == 8050 :
 I111IIiii1Ii ( )
elif iIiii == 8051 :
 II1 ( oOooo0 )
elif iIiii == 8052 :
 iiIIIiIii ( oOooo0 )
elif iIiii == 8085 :
 I1II ( )
elif iIiii == 8086 :
 iII1iI1IIiI ( oOooo0 )
elif iIiii == 8087 :
 oO0O ( oOooo0 )
elif iIiii == 8088 :
 OOoooO00o0o ( oOooo0 , IiI111111IIII )
elif iIiii == 9000 :
 ii1O000OOO0OOo ( )
elif iIiii == 1111 :
 oOoo00oO0O0OO ( )
elif iIiii == 9001 :
 Iii11111iiI ( )
elif iIiii == 9002 :
 i1Ii11ii1I ( )
elif iIiii == 9003 :
 I1Ii1i11I1I ( )
elif iIiii == 50 :
 IiIi1 ( oOooo0 )
elif iIiii == 9020 :
 champlist ( )
elif iIiii == 9021 :
 OO0o0o0oo ( )
elif iIiii == 9022 :
 iIiII1 ( )
elif iIiii == 9023 :
 i111iii1I1 ( )
elif iIiii == 9024 :
 oOIIIi11 ( oOooo0 )
elif iIiii == 9030 :
 o00OoO0o0 ( oOooo0 )
elif iIiii == 9031 :
 o0O ( oOooo0 )
elif iIiii == 9032 :
 OOoO0ooOOOo0 ( oOooo0 )
elif iIiii == 9033 :
 o0oOOO ( oOooo0 )
elif iIiii == 7085 :
 I11iiIi1i1IIi ( oOooo0 )
elif iIiii == 7086 :
 i1Ii1i1I11III ( oOooo0 )
elif iIiii == 7087 :
 oOoOO ( IIOOO0O00O0OOOO )
elif iIiii == 9666 :
 I1I ( oOooo0 )
elif iIiii == 10100 : o0OOooO ( )
elif iIiii == 10105 : iIiIi1iIIi11i ( oOooo0 )
elif iIiii == 10106 : oO0O0o0O ( oOooo0 )
elif iIiii == 10104 : O0oooOoO ( oOooo0 )
elif iIiii == 10107 : iiiI ( )
elif iIiii == 10103 : o0oOoOo0 ( oOooo0 )
elif iIiii == 10108 : ii1IiIi1i ( oOooo0 )
elif iIiii == 10107 : iiiI ( )
elif iIiii == 10000 : Origin_Menu ( )
elif iIiii == 10001 : IIo00ooo ( )
elif iIiii == 10002 : OO0ooOoOO0OOo ( )
elif iIiii == 10003 : OO0oIiII1iiI ( )
elif iIiii == 10004 : I1oO0ooOoO ( oOooo0 )
elif iIiii == 10005 : iIIi1iI1I1IIi ( )
elif iIiii == 10006 : O0o00O0Oo0 ( oOooo0 )
elif iIiii == 10007 : iI1 ( oOooo0 , I1i111I )
elif iIiii == 10008 : III1III11II ( )
elif iIiii == 10009 : oO0oo0o00o0O ( )
elif iIiii == 10010 : i1I11 ( oOooo0 )
elif iIiii == 10011 : OO0Oo ( oOooo0 )
elif iIiii == 10012 : Oo0oOooOoOo ( oOooo0 )
elif iIiii == 10013 : IiIioO0Oo00oo ( oOooo0 )
elif iIiii == 10014 : Ii ( )
elif iIiii == 10015 : o0o00oO0oo000 ( )
elif iIiii == 10016 : O0OOOo ( oOooo0 )
elif iIiii == 10017 : iIiI1IIiii11 ( )
elif iIiii == 10018 : iIiI1I1IIi11 ( )
elif iIiii == 10019 : IIoO00OoOo ( )
elif iIiii == 10020 : i1I1i1i ( )
elif iIiii == 10021 : oO00o ( )
elif iIiii == 10022 : ii11i ( oOooo0 )
elif iIiii == 10023 : Ii1I11i11I1i ( IiI111111IIII , oOooo0 )
elif iIiii == 10024 : I111i1Ii1i1 ( oOooo0 )
elif iIiii == 10025 : i1IIi1i1Ii1 ( )
elif iIiii == 10026 : oO0ooOO ( )
elif iIiii == 10027 : OOo0O0O000 ( )
elif iIiii == 10028 : OoOOo00 ( )
elif iIiii == 10029 : iI11Ii111 ( )
elif iIiii == 423 : iIIi1 ( oOooo0 )
elif iIiii == 426 : I1I1I11Ii ( oOooo0 )
elif iIiii == 10030 : Izle_Films ( )
elif iIiii == 10031 : Latest_Izle_Movies ( )
elif iIiii == 10032 : Izle_Genres ( )
elif iIiii == 10033 : Izle_Pop_Movies ( )
elif iIiii == 10034 : Izle_Boxsets ( )
elif iIiii == 10035 : Izle_Search ( )
elif iIiii == 10036 : Izle_Genres_Movie ( oOooo0 )
elif iIiii == 10037 : Izle_Boxset_single ( oOooo0 )
elif iIiii == 10038 : Izle_IFRAME ( )
elif iIiii == 10039 : Izle_Boxsets_Next ( oOooo0 )
elif iIiii == 10040 : o0oOOOO0 ( )
elif iIiii == 10041 : Ii1Ii1I ( oOooo0 )
elif iIiii == 10042 : OooOooO0O0o0 ( oOooo0 )
elif iIiii == 10043 : oOo0Oo0O0O ( )
elif iIiii == 10044 : o0O00O ( oOooo0 )
elif iIiii == 10045 : i1iiI ( IiI111111IIII )
elif iIiii == 10046 : Ooo0Oo0o ( oOooo0 )
elif iIiii == 10047 : I11II1i11 ( oOooo0 )
elif iIiii == 10048 : IiI ( oOooo0 )
elif iIiii == 10049 : i1I1iIii11 ( oOooo0 )
elif iIiii == 10050 : II1II ( )
elif iIiii == 10051 : OO0OOOOOo ( )
elif iIiii == 10052 : iii11 ( )
elif iIiii == 10053 : Addon ( oOooo0 )
elif iIiii == 10054 : o0Oo00OOoO0oo ( oOooo0 , IiI111111IIII )
elif iIiii == 10055 :
 oo0oO ( "addFavorite" )
 try :
  IiI111111IIII = IiI111111IIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiI111111IIII = IiI111111IIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0oO0Oo ( IiI111111IIII , oOooo0 , I1i111I , OooOo0oo0O0o00O , iiIi1 )
elif iIiii == 10056 :
 oo0oO ( "rmFavorite" )
 try :
  IiI111111IIII = IiI111111IIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiI111111IIII = IiI111111IIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOiI1 ( IiI111111IIII )
elif iIiii == 10057 :
 oo0oO ( "getFavorites" )
 o0OO ( )
elif iIiii == 10058 : iII1i1 ( )
elif iIiii == 10059 : Donators_Guide ( )
elif iIiii == 10060 : o0oO000oo ( )
elif iIiii == 10061 : II1I11i ( )
elif iIiii == 10062 : o0o0O ( IiI111111IIII , oOooo0 , IIOOO0O00O0OOOO )
elif iIiii == 10063 : ooo ( )
elif iIiii == 10064 : OOOOoOOo0O0 ( )
elif iIiii == 10065 : oo0oOOO0OOOo ( oOooo0 )
elif iIiii == 10066 : i1iI ( oOooo0 )
elif iIiii == 10068 : o0oooOO00 ( oOooo0 )
elif iIiii == 10069 : IiII111i1i11 ( oOooo0 )
elif iIiii == 10070 : ooooo0O0000oo ( oOooo0 )
elif iIiii == 10071 : Genie_Watch ( )
elif iIiii == 10072 : OoO0o ( )
elif iIiii == 10073 : Ii1I1i ( oOooo0 )
elif iIiii == 10074 : OoOoO ( oOooo0 )
elif iIiii == 10075 : O0oO ( I1i111I , IiI111111IIII , oOooo0 )
elif iIiii == 10076 : oOOOoo0O0oO ( oOooo0 )
elif iIiii == 10077 : oOo0O0Oo00oO ( oOooo0 )
elif iIiii == 10078 : iiI1Ii1iI1 ( )
elif iIiii == 10079 : Genie_Watch_Tv_Shows ( )
elif iIiii == 10080 : Genie_Watch_Tv_Genre ( oOooo0 )
elif iIiii == 10081 : Genie_Watch_TV_PlayRun ( oOooo0 )
elif iIiii == 10082 : Genie_Watch_TV_Episodes ( oOooo0 , I1i111I )
elif iIiii == 10083 : Genie_Watch_Tv_Recent ( oOooo0 )
elif iIiii == 10084 : OO0OoO0o00 ( )
elif iIiii == 20000 : iIi1IIiI ( )
elif iIiii == 20001 : IiIiiiIii ( )
elif iIiii == 20002 : o0o0oOo000o0 ( oOooo0 )
elif iIiii == 20003 : ii1IiIi11 ( oOooo0 )
elif iIiii == 20004 : o00oo0000 ( oOooo0 )
elif iIiii == 21004 : Ii1 ( )
elif iIiii == 21005 : I1iiiiii ( oOooo0 )
elif iIiii == 21006 : I11iiii1I ( oOooo0 )
elif iIiii == 21007 : oooo00i1 ( oOooo0 )
elif iIiii == 30000 : iiIII1II ( )
elif iIiii == 30001 : oOooO00o0O ( )
elif iIiii == 10012 : Resolve ( oOooo0 )
elif iIiii == 30003 : i1iiiIii11 ( )
elif iIiii == 30004 : ooOOOOo0 ( oOooo0 )
elif iIiii == 30005 : ooO00O00oOO ( oOooo0 )
elif iIiii == 30006 : OO0O0ooOOO00 ( )
elif iIiii == 30007 : OO00OOoO0o ( )
elif iIiii == 30008 : oooo00 ( oOooo0 )
elif iIiii == 30009 : iIi1IiI ( oOooo0 )
elif iIiii == 30010 : i1IiiI1iIi ( oOooo0 )
elif iIiii == 30011 : iIiI ( )
elif iIiii == 30012 : ii1I11iIiIII1 ( )
elif iIiii == 30013 : IIIii1iiIi ( )
elif iIiii == 30014 : Ooo0Oo0oo0 ( )
if 24 - 24: OoooooooOO
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
