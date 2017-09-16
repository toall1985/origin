import re
import requests
import time

domain = ['vidtodo.com']
name = 'Vidtodo'
sources = []

def resolve(url):
    if url.startswith('http'):
        if not url.startswith('https'):
            url = url.replace('http','https').replace('httpss','https')
    html = requests.get(url).content
    if 'embed' in url:
        u = re.findall('(.+?)-(.+?)-',str(url))
        for one,two in u:
            url = one.replace('embed','')+two
            m = re.compile('mp4\|(.+?)\|').findall(html)
            for n in m:
                playlink = 'http://94.176.148.22/'+n+'/v.mp4'
                sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    else:
        form = re.findall('<form method="post".+?>(.+?)</form>',html.lower(),re.DOTALL)[0]
        op = re.findall('name="op" value="(.+?)"',str(form))[0]
        usr_login = re.findall('name="usr_login" value="(.*?)"',str(form))[0]
        ID = re.findall('name="id" value="(.+?)"',str(form))[0]
        fname = re.findall('name="fname" value="(.*?)"',str(form))[0]
        referer = re.findall('name="referer" value="(.*?)"',str(form))[0]
        Hash = re.findall('name="hash" value="(.*?)"',str(form))[0]
        imhuman = re.findall('name="imhuman" value="(.*?)"',str(form))[0]
        imhuman = imhuman.replace(' ','+')
        time.sleep(2)
        headers = {'Referer':url,
                   'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
                   'Host':'vidtodo.com'
                   }
        data = {'op':op,'usr_login':usr_login,'id':ID,'fname':fname,'referer':referer,'hash':Hash,'imhuman':imhuman}
        html2 = requests.post(url,headers=headers,data=data).content
        server = re.findall("<span id='vplayer'><img src=\"https://(.+?).vidtodo.com/",html2)
        for serve in server:
            serve = serve
        m = re.compile('mp4\|(.+?)\|').findall(html2)[0]
        playlink = 'https://'+serve+'.vidtodo.com/'+m+'/v.mp4'
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})

    return sources

#resolve('http://vidtodo.com/8x4jaglspe3z')
