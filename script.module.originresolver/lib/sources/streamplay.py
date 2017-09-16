import re
import requests
import time
import xbmc

domain = ['streamplay.to']
name = 'Streamplay'
sources = []

def resolve(url):
    html = requests.get(url).content
    op = re.findall('<input type="hidden" name="op" value="(.+?)"',str(html))[0]
    ID = re.findall('<input type="hidden" name="id" value="(.+?)"',str(html))[0]
    fname = re.findall('<input type="hidden" name="fname" value="(.+?)"',str(html))[0]
    Hash = re.findall('<input type="hidden" name="hash" value="(.+?)"',str(html))[0]
    try:
        referer = re.findall('<input type="hidden" name="referer" value="(.+?)"',str(html))[0]
    except:
        referer=''
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
               'referer':url}
    data = {'id':ID,
            'fname':fname,
            'hash':Hash,
            'op':op,
            'referer':referer,
            'imhuman':'Proceed+to+video'
            }
    print '1'
    time.sleep(5)
    print '2'
    h = requests.post(url,headers=headers,data=data).content
    info = re.findall('mp4\|(.+?)\|',str(h))[0]
    playlink = 'http://149.202.80.234/'+info+'/v.mp4'
    sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources


#resolve('http://streamplay.to/yyz8948ahf39')
