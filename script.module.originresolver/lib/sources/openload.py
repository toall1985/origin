import re
import requests
import xbmc
import xbmcgui
import os
import time

domain = ['openload.co','openload.link']
name = 'Openload'
sources = []
Dialog = xbmcgui.DialogProgress()

def resolve(url,count=None):
    global pair_url
    if '.link' in url:
        html = requests.get(url).content
        match = re.compile('<iframe src="(.+?)"').findall(html)
        for u in match:
            url = u
    if count == None:
        count = 0
    xbmc.log(str(count),xbmc.LOGNOTICE)
    api = 'https://api.openload.co/1'
    u = api + '/streaming/get?file='
    if 'mp4' in url:
        media_id = re.findall('openload.co/.+?/(.+?)/',str(url))[0]
    elif 'embed' in url:
        media_id = url.replace('https://openload.co/embed/','').replace('/','')
    html = requests.get(u+media_id).json()
    print html
    status = re.findall("'status': (.+?),",str(html))[0]
    if not '200' in status:
        xbmc.log(str(html),xbmc.LOGNOTICE)
        if count == 0:
            count +=1
            msg = re.findall("'msg'.+?'(.+?)'",str(html))[0]
            pair_url = re.findall("http(.+?)',",str(html))[0]
            pair_url = 'http'+pair_url
            line4 = "Would you like to open the pairing url: [B][COLOR blue]"+pair_url+"[/COLOR][/B]"
            choice = xbmcgui.Dialog().yesno('You need to pair to use this link',msg,'NEVER enter credit card details for this process!!',line4,nolabel='[COLOR red]No[/COLOR]',yeslabel='[COLOR cyan]Yes[/COLOR]')
            if choice == 1:
                if xbmc.getCondVisibility('system.platform.android'):
                    try: xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","","'+pair_url+'")')
                    except: pass
                elif xbmc.getCondVisibility('system.platform.linux'):
                    try: os.system('xdg-open '+pair_url)
                    except: pass
                elif xbmc.getCondVisibility('system.platform.windows'):
                    try: os.system('start '+pair_url)
                    except: pass
                elif xbmc.getCondVisibility('system.platform.osx'):
                    try: os.system('open '+pair_url)
                    except: pass
                elif xbmc.getCondVisibility('system.platform.ios'):
                    try: os.system('open '+pair_url)
                    except: pass
                timer(url,count)
            else:
                return []
        elif count >=1:
            count += 1
            timer(url,count)
    elif '200' in status:
        playlink = re.findall("'url'.+?'(.+?)'",str(html))
        for p in playlink:
            sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': p,'direct': True})
        return sources

def timer(url,count):
    if count == 1:
        Dialog.create('Pairing needed', 'You need to visit '+pair_url+' to pair')
        time.sleep(1)
    else:
        Dialog.create('Pairing needed', 'You need to visit '+pair_url+' to pair')
    Dialog.update(int(100/25*count),'You need to visit '+pair_url+' to pair','Awaiting Pairing '+str(30-int(count)))
    time.sleep(1)
    if Dialog.iscanceled():
        xbmcgui.Dialog().notification("Origin resolvers", "Pairing Unsuccesful")
        return []
        sys.exit()
    if count<30:
        resolve(url,count=count)
    elif count == 30:
        xbmcgui.Dialog().notification("Origin resolvers", "Pairing Unsuccesful")

