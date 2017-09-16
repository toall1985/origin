import re
import requests
import time

domain = ['vidto.me']
name = 'Vidto'
sources = []

def resolve(url):
    html = requests.get(url).content
    form = re.findall('<form method="post".+?>(.+?)</form>',html.lower(),re.DOTALL)[0]
    op = re.findall('name="op" value="(.+?)"',str(form))[0]
    usr_login = re.findall('name="usr_login" value="(.*?)"',str(form))[0]
    ID = re.findall('name="id" value="(.+?)"',str(form))[0]
    fname = re.findall('name="fname" value="(.*?)"',str(form))[0]
    referer = re.findall('name="referer" value="(.*?)"',str(form))[0]
    Hash = re.findall('name="hash" value="(.*?)"',str(form))[0]
    imhuman = re.findall('name="imhuman" value="(.*?)"',str(form))[0]
    imhuman = imhuman.replace(' ','+')
    time.sleep(6)
    headers = {'Referer':url,
               'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
               'Host':'vidto.me'
               }
    data = {'op':op,'usr_login':usr_login,'id':ID,'fname':fname,'referer':referer,'hash':Hash,'imhuman':imhuman}
    html2 = requests.post(url,headers=headers,data=data).content
    source_list = re.findall('sources: \[(.+?)\]',html2)[0]
    info = re.findall('file:"(.+?)".+?label:"(.+?)"',str(source_list))
    for playlink,quality in info:
        sources.append({'source': name, 'quality': quality, 'scraper': name, 'url': playlink,'direct': True})
    return sources
