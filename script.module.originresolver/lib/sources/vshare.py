import re
import requests
import time

domain = ['vshare.eu']
name = 'Vshare'
sources = []

def resolve(url):
    html = requests.get(url).content
    op = re.findall('<input type="hidden" name="op" value="(.+?)">',html)[0]
    ID = re.findall('<input type="hidden" name="id" value="(.+?)">',html)[0]
    fname = re.findall('<input type="hidden" name="fname" value="(.+?)">',html)[0]
    headers = {
            "referer":url,
            "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":'__utma=254669071.73767129.1504312517.1504312517.1504312517.1; __utmz=254669071.1504312517.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aff=2920; ref_url=http%3A%2F%2Fvshare.eu%2Fj2swq8r2636c.htm'
            }
    data = {
        "op":op,
        "id":ID,
        "fname":fname,
        'usr_login':'',
        'referer':url,
        "method_free":"Proceed+to+video"
        }
    time.sleep(5)
    html2 = requests.post(url,headers=headers,data=data).content
    play = re.findall("file:'(.+?)'",html2)
    for playlink in play:
        if '/vid.mp4' in playlink:
            sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})

    return sources

