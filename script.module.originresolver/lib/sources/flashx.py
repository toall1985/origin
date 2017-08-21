import re
import requests
import time

domain = 'flashx.tv'
name = 'Flashx'
sources = []
test = 'https://www.flashx.tv/dl?playthis'

def resolve(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
    html = requests.get(url,headers=headers).content
    op = re.findall('name="op" value="(.+?)"',html)[0]
    ID = re.findall('name="id" value="(.+?)"',html)[0]
    fname = re.findall('name="fname" value="(.+?)"',html)[0]
    Hash = re.findall('"hash" value="(.+?)"',html)[0]
    time.sleep(5)
    headers = {
            "Referer":"https://www.flashx.tv/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
            "Content-Type":"application/x-www-form-urlencoded"
            }
    data = {
        "op":op,
        "id":ID,
        "fname":fname,
        "hash":Hash,
        "imhuman":"Proceed+to+video"
        }
    html2 = requests.post(test,headers=headers,data=data).content
    print html2
    match2 = re.compile("src: '(.+?)'.+?res: (.+?)}").findall(html2)
    for u,q in match2:
        sources.append({'source': name, 'quality': q, 'scraper': name, 'url': u,'direct': True})
    return sources


