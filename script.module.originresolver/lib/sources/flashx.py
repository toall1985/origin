import re
import requests
import time

domain = ['flashx.tv']
name = 'Flashx'
sources = []
test = 'https://www.flashx.tv/dl?playthis'

def resolve(url):
    if not '.jsp' in url:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
        response = requests.get('http://www.flashx.tv/embed-sjl7r6cd3lnq-600x406.html',headers=headers)
        next_url = response.url
        html = requests.get(next_url).content
        m = re.findall('window.location = "(.+?)"',html)
        for n in m:
            resp = requests.get(n,headers=headers)
            url = resp.url
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
    match2 = re.compile("src: '(.+?)'.+?res: (.+?)}").findall(html2)
    for u,q in match2:
        sources.append({'source': name, 'quality': q, 'scraper': name, 'url': u,'direct': True})
    return sources
