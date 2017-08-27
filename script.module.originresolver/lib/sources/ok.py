import requests
import re

#streams are being pulled in segments by browser, not sure how to replicate atm

domain = 'ok.ru'

def resolve(url):
    pass
'''    html = requests.get(url).content
    match = re.findall('BaseURL(.+?)/BaseURL',html)[0]
    u = match.replace('\\\\u003E','').replace('\\\\u0026','').replace('amp;','&').replace('\\\\u003C','').replace('UNKNOWN','GECKO').replace('%3B',';')
#    u = u + '&bytes=0-11628440'
    expires = re.findall('expires=(.+?)&',str(u))[0]
    srcIp = re.findall('srcIp=(.+?)&',str(u))[0]
    srcAg = re.findall('srcAg=(.+?)&',str(u))[0]
    Type = re.findall('type=(.+?)&',str(u))[0]
    sig = re.findall('sig=(.+?)&',str(u))[0]
    ct = re.findall('ct=(.+?)&',str(u))[0]
    urls = re.findall('urls=(.+?)&',str(u))[0]
    clientType = re.findall('clientType=(.+?)&',str(u))[0]
    ID = re.findall('id=(.+?)>',str(u)+'>')[0]
#    Bytes = '0-11628440'

    headers = {
                "origin":"https://ok.ru",
                "referer":url,
                "host":"vd0.mycdn.me",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                }

    data = {
            "expires":expires,
            "srcIp":srcIp,
            "srcAg":srcAg,
            "type":Type,
            "sig":sig,
            "ct":ct,
            "urls":urls,
            "clientType":clientType,
            "id":ID
            }
            

    h = requests.post(u,headers=headers,data=data).json()
    print u
    
    

#https://vd0.mycdn.me/?expires=1503324063743&srcIp=77.102.110.38&srcAg=GECKO&type=4&sig=688f98cf08879aef8c8c69f7c36ca56a74992703&ct=4&
#urls=217.20.157.211;5.61.21.104;5.61.22.71&clientType=0&id=297687714406'''
