import requests, urllib, urllib2, time, re, HTMLParser, xbmc, xbmcgui, os
from bs4 import BeautifulStoneSoup, BeautifulSoup
#from BeautifulSoup import BeautifulSOAP
ADDON_ID = 'plugin.video.entertainmentlounge'
LeagueDump = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + ADDON_ID , 'LeagueDump.txt'))

def request(url, close=True, error=False, proxy=None, post=None, headers=None, mobile=False, safe=False, referer=None, cookie=None, output='', timeout='30'):
    try:
        handlers = []
        if not proxy == None:
            handlers += [urllib2.ProxyHandler({'http':'%s' % (proxy)}), urllib2.HTTPHandler]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        if output == 'cookie' or not close == True:
            import cookielib
            cookies = cookielib.LWPCookieJar()
            handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookies)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        try:
            if sys.version_info < (2, 7, 9): raise Exception()
            import ssl; ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            handlers += [urllib2.HTTPSHandler(context=ssl_context)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        except:
            pass

        try: headers.update(headers)
        except: headers = {}
        if 'User-Agent' in headers:
            pass
        elif not mobile == True:
            headers['User-Agent'] = 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
        else:
            headers['User-Agent'] = 'Apple-iPhone/701.341'
        if 'referer' in headers:
            pass
        elif referer == None:
            headers['referer'] = url
        else:
            headers['referer'] = referer
        if not 'Accept-Language' in headers:
            headers['Accept-Language'] = 'en-US'
        if 'cookie' in headers:
            pass
        elif not cookie == None:
            headers['cookie'] = cookie

        request = urllib2.Request(url, data=post, headers=headers)

        try:
            response = urllib2.urlopen(request, timeout=int(timeout))
        except urllib2.HTTPError as response:
            if error == False: return

        if output == 'cookie':
            result = []
            for c in cookies: result.append('%s=%s' % (c.name, c.value))
            result = "; ".join(result)
        elif output == 'response':
            if safe == True:
                result = (str(response), response.read(224 * 1024))
            else:
                result = (str(response), response.read())
        elif output == 'chunk':
            content = int(response.headers['Content-Length'])
            if content < (2048 * 1024): return
            result = response.read(16 * 1024)
        elif output == 'geturl':
            result = response.geturl()
        else:
            if safe == True:
                result = response.read(224 * 1024)
            else:
                result = response.read()
        if close == True:
            response.close()

        return result
    except:
        return

def Text_Boxes(heading,anounce):
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
      try: f=open(anounce); text=f.read()
      except: text=anounce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox() 
		
def Premier_League_Table():
    url = 'http://www.premierleague.com/en-gb/matchday/league-table.html'
    link = request(url)
    soup = BeautifulSoup(link)
    rownumber = 1
    DumpFile = open(LeagueDump,'w')
    
    while rownumber <= 20:
        RowNo = 'row'+str(rownumber)
        GetRow = soup.find_all('tr', {'class': RowNo})
        
        DumpFile.close()
        for row in GetRow:
            clubData = []
            positionTD = row.find_all('td', {'class': 'col-pos'})
            ClubName = row.find_all('td', {'class': 'col-club'})
            Clubplayed = row.find_all('td', {'class': 'col-p'})
            Clubwon = row.find_all('td', {'class': 'col-w'})
            Clubdrew = row.find_all('td', {'class': 'col-d'})
            Clublost = row.find_all('td', {'class': 'col-l'})
            ClubGF = row.find_all('td', {'class': 'col-gf'})
            ClubGA = row.find_all('td', {'class': 'col-ga'})
            ClubGD = row.find_all('td', {'class': 'col-gd'})
            ClubPTS = row.find_all('td', {'class': 'col-pts'})

            for position in positionTD:
                position = re.findall(r'<td class="col-pos">(.*?)</td>',str(position))
                for Position in position:
                    clubData.append(Position)
            
            for Club_name in ClubName:
                Club_name = Club_name.text
                clubData.append(Club_name)
            
            for Club_played in Clubplayed:
                Club_played = Club_played.text
                clubData.append(Club_played)

            for Club_won in Clubwon:
                Club_won = Club_won.text
                clubData.append(Club_won)

            for Club_drew in Clubdrew:
                Club_drew = Club_drew.text
                clubData.append(Club_drew)

            for Club_lost in Clublost:
                Club_lost = Club_lost.text
                clubData.append(Club_lost)

            for Club_gf in ClubGF:
                Club_gf  = Club_gf.text
                clubData.append(Club_gf)

            for Club_ga in ClubGA:
                Club_ga  = Club_ga.text
                clubData.append(Club_ga)

            for Club_gd in ClubGD:
                Club_gd  = Club_gd.text
                clubData.append(Club_gd)

            for Club_pts in ClubPTS:
                Club_pts  = Club_pts.text
                clubData.append(Club_pts)

            Pos = clubData[0]
            clubname = clubData[1]
            clubplayed = clubData[2]
            clubwon = clubData[3]
            clubdrew = clubData[4]
            clublost = clubData[5]
            Clubgf = clubData[6]
            Clubga = clubData[7]
            Clubgd = clubData[8]
            Club_pts = clubData[9]
            if rownumber < 10:
                ClubResults = 'POS:   ' + Pos + ':  ' + clubname + '    P ' + clubplayed + '    W ' + clubwon + '    D ' + clubdrew + '    L ' + clublost + '    GF ' + Clubgf + '    GA ' + Clubga + '    GD ' + Clubgd + '    PTS ' + Club_pts + '\n'
                
            else:
                ClubResults = 'POS: ' + Pos + ':  ' + clubname + '    P ' + clubplayed + '    W ' + clubwon + '    D ' + clubdrew + '    L ' + clublost + '    GF ' + Clubgf + '    GA ' + Clubga + '    GD ' + Clubgd + '    PTS ' + Club_pts + '\n'

            
            AppendDump = open(LeagueDump,'a')
            AppendDump.write(ClubResults)
        
        rownumber += 1
		
			
    else:
		AppendDump = open(LeagueDump,'a')
		AppendDump.write('********** END OF TABLE ************')
		opendumpedtable = open(LeagueDump,'r')
		dumpedtable = opendumpedtable.read()
		Text_Boxes('Premier League Table',dumpedtable)
		AppendDump.close()






        
        



