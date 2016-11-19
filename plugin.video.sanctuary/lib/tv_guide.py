import re,process,requests, urllib
from datetime import datetime
Year = datetime.now().strftime('%Y')
Month = datetime.now().strftime('%m')
Day = datetime.now().strftime('%d')
Hour = datetime.now().strftime('%H')
Minute = datetime.now().strftime('%M')
time_now_number = str((int(Hour)*60)+int(Minute))

def TV_GUIDE_MENU():
    process.Menu('Telegraph TV Guide','',2201,'','','','')
    process.Menu('TVGuide.co.uk','',2204,'','','','')
	
def TV_GUIDE_CO_UK_CATS():
    process.Menu('Popular','7',2205,'','','','')
    process.Menu('Freeview','3',2205,'','','','')
    process.Menu('Sky','5',2205,'','','','')
    process.Menu('Virgin XL','25',2205,'','','','')
    process.Menu('Freesat','19',2205,'','','','')
    process.Menu('BT','22',2205,'','','','')

def tvguide_co_uk(url):


    List =[['All','http://www.tvguide.co.uk/?catcolor=&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Comedy','http://www.tvguide.co.uk/?catcolor=3253CF&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Sports','http://www.tvguide.co.uk/?catcolor=53CE32&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Music','http://www.tvguide.co.uk/?catcolor=FF9933&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Film','http://www.tvguide.co.uk/?catcolor=000000&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Soap','http://www.tvguide.co.uk/?catcolor=AB337D&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Kids','http://www.tvguide.co.uk/?catcolor=E3BB00&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Drama','http://www.tvguide.co.uk/?catcolor=CE3D32&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Talk show','http://www.tvguide.co.uk/?catcolor=800000&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Game show','http://www.tvguide.co.uk/?catcolor=669999&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Sci-fi','http://www.tvguide.co.uk/?catcolor=666699&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Documentary','http://www.tvguide.co.uk/?catcolor=CCCCCC&systemid='+url+'&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Motor','http://www.tvguide.co.uk/?catcolor=996633&systemid=7&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323'],
    ['Horror','http://www.tvguide.co.uk/?catcolor=666633&systemid=7&thistime='+Hour+'&thisDay='+Month+'/'+Day+'/'+Year+'&gridspan=03:00&view=0&gw=1323']]
    for item in List:
        name = item[0]
        url = item[1]
        process.Menu(name,url,2206,'','','','')
		
def WhatsOnCOUK(url):
    try:
        html = requests.get(url).text
        channel_block = re.compile('<div class="div-epg-channel-progs">.+?<div class="div-epg-channel-name">(.+?)</div>(.+?)</div></div></div>',re.DOTALL).findall(html)
        for channel,block in channel_block:
            prog = re.compile('<a qt-title="(.+?)"(.+?)onmouse',re.DOTALL).findall(str(block.encode('utf-8')))
            for show_info, info in prog:
                time_finder = re.compile('(.+?)-(.+?) ').findall(str(show_info))
                for start,finish in time_finder:
                    stop = []
                    if len(stop)<10:
                        if 'am' in start:
                            time_split = re.compile('(.+?):(.+?)am').findall(str(start))
                            for hour,minute in time_split:
                                start_number = (int(hour) * 60) + int(minute)
                        elif 'pm' in start:
                            time_split = re.compile('(.+?):(.+?)pm').findall(str(start))
                            for hour,minute in time_split:
                                if hour =='12':
                                    start_number = (int(hour) * 60) + int(minute)
                                else:
                                    start_number = (int(hour) + 12) * 60 + int(minute)
                        if 'am' in finish:
                            time_split = re.compile('(.+?):(.+?)am').findall(str(finish))
                            for hour,minute in time_split:
                                finish_number = (int(hour) * 60) + int(minute)
                        elif 'pm' in finish:
                            time_split = re.compile('(.+?):(.+?)pm').findall(str(finish))
                            for hour,minute in time_split:
                                if hour =='12':
                                    finish_number = (int(hour) * 60) + int(minute)
                                else:
                                    finish_number = (int(hour) + 12) * 60 + int(minute)
                        if int(start_number)<int(time_now_number)<int(finish_number):
                            clean_channel = channel.replace('BBC1 London','BBC1').replace('BBC2 London','BBC2').replace('ITV London','ITV1')
                            process.Menu(clean_channel.encode('utf-8') + ': '+ show_info.encode('utf-8'),'',2203,'','','',clean_channel)
    except:
        pass



def whatsoncat():
    html=process.OPEN_URL('http://tvguideuk.telegraph.co.uk/')
    match = re.compile('<li class="tabs"><span><a href="(.+?)">(.+?)</a></span></li>').findall(html)
    for url,name in match:
        if 'amp;' in url:
			if int(hour)<12:
				time=str(hour)+'.'+minute+'am'
			else:
				pm=int(hour)-12
				time = str(pm)+'.'+minute+'pm'
			url = url.replace('amp;','').replace('oclock=','oclock='+time)
			process.Menu(name,'http://tvguideuk.telegraph.co.uk/' + url,2202,'','','','')
		
def whatson(url):
    html=process.OPEN_URL(url)
    match = re.compile('<div class="channel_name">(.+?)<.+?<div class="programme  showing".+?channel_id=(.+?).+?>(.+?)</a>',re.DOTALL).findall(html)
    for name,id,whatson in match:
        name = name.replace('(','').replace(')','').replace('Plus 1','+1').replace('London','').replace('Five','5')
        process.Menu(name + ' - ' + whatson,'',2203,'','','',name)
		
def search_split(extra):
    import search
    search.Live_TV(extra.lower().replace('hd','').replace(' ',''))