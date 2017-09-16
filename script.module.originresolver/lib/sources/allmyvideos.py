import re
import requests

domain = ['allmyvideos.net']
name = 'Allmyvideos'
sources = []
url = 'http://allmyvideos.net/r6r5pzs8vydq'

def resolve(url):
    if not 'embed' in url:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
                   'Referer':url
                   }
        html = requests.get('http://allmyvideos.net/download1.html',headers=headers).content
        match = re.findall('iframe src="(.+?)"',html)[0]
        print match
#        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
 #   print sources

resolve(url)
