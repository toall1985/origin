import requests
import re
from HTMLParser import HTMLParser

domain = ['ok.ru']
name = 'Ok.Ru'
sources = []


def resolve(url):
    headers = {
            'Referer':url,
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
            'host':'ok.ru'
            }
    html = requests.get(url,headers=headers).content
    h = ''.join(html.replace('\\','').replace('u0026','&').replace('&quot;',''))
    match = re.compile('name:(.+?),url:(.+?),').findall(h)
    for qual,m in match:
        m = m.replace('srcAg=UNKNOWN','srcAg=GECKO').replace('%3B',';').replace('ct=0','ct=4')
        if 'type=' in m:
            qual = qual.replace('lowest','v bad').replace('low','bad').replace('mobile','v v bad')
            sources.append({'source': name, 'quality': qual, 'scraper': name, 'url': m,'direct': True})
    return sources
