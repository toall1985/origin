import re
import requests
import xbmc
import xbmcgui
import time

domain = 'openload.co'
name = 'Openload'
sources = []

def resolve(url,count=None):
    if count==None:
        count = 0
    url = url
    Dialog = xbmcgui.DialogProgress()        
    api = 'https://api.openload.co/1'
    u = api + '/streaming/get?file='
    media_id = url.replace('https://openload.co/embed/','').replace('/','')
    html = requests.get(u+media_id).json()
    print html
    status = re.findall("'status': (.+?),",str(html))[0]
    if not '200' in status:
        count+=1
        msg = re.findall("'msg'.+?'(.+?)'",str(html))[0]
        pair_url = re.findall("http(.+?)',",str(html))[0]
        pair_url = 'http'+pair_url
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
    elif '200' in status:
        playlink = re.findall("'url'.+?'(.+?)'",str(html))
        for p in playlink:
            sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': p,'direct': True})
        return sources

