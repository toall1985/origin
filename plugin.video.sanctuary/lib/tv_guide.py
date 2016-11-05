import re,process
from datetime import datetime

def whatsoncat():
    html=process.OPEN_URL('http://tvguideuk.telegraph.co.uk/')
    match = re.compile('<li class="tabs"><span><a href="(.+?)">(.+?)</a></span></li>').findall(html)
    for url,name in match:
        if 'amp;' in url:
		time = datetime.now().strftime('%H')
        minute = datetime.now().strftime('%M')
        if int(time)<12:
            time=str(time)+'.'+minute+'am'
        else:
            pm=int(time)-12
            time = str(pm)+'.'+minute+'pm'
        url = url.replace('amp;','').replace('oclock=','oclock='+time)
        process.Menu(name,'http://tvguideuk.telegraph.co.uk/' + url,2201,'','','','')
		
def whatson(url):
    html=process.OPEN_URL(url)
    match = re.compile('<div class="channel_name">(.+?)<.+?<div class="programme  showing".+?channel_id=(.+?).+?>(.+?)</a>',re.DOTALL).findall(html)
    for name,id,whatson in match:
        name = name.replace('(','').replace(')','').replace('Plus 1','+1')
        process.Menu(name + ' - ' + whatson,'',2202,'','','',name)
		
def search_split(extra):
    import search
    search.Live_TV(extra.lower())