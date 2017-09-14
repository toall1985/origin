import re
import requests

domain = ['rutube.ru']
name = 'Rutube'
sources = []

def resolve(url):
    if 'embed' in url:
        url = url
    else:
        ht = requests.get(url).content
        m = re.findall('link rel="video_src" href="(.+?)"',ht)[0]
        if 'embed' in m:
            url = m
    html = requests.get(url).content
    api = 'https://rutube.ru/api/play/options/'+url.replace('https://rutube.ru/play/embed/','')+'/?format=json&sqr4374_compat=1&no_404=true&referer='+url
    headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
               "Referer": url,
               "Host":"rutube.ru"
               }				
    h = requests.get(api,headers=headers).content
    m3u8 = re.compile('"m3u8": "(.+?)"').findall(str(h))
    for link in m3u8:
        last = link+'&referer='+url
        h = requests.get(last).content
        m = re.compile('".+?"\n(.+?)\n',re.DOTALL).findall(h)
        for l in m:
            try:
                qual = re.findall('i=.+?x(.+?)_',str(l))[0]
            except:
                qual = 'SD'
            sources.append({'source': name, 'quality': qual+'p', 'scraper': name, 'url': l,'direct': True})
    return sources
