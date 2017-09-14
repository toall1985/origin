import re
import requests

domain = ['speedvid.net']
name = 'Speedvid'
sources = []

def resolve(url):
    server = ''
    no = ''
    html = requests.get(url).content
    n = re.findall('\|primary\|(.+?)\|(.+?)\|.+?mp4\|(.+?)\|',html)
    for no,server,i in n:
        no = no
        server = server
        playlink = 'http://'+server+'.speedvid.net:'+no+'/' + i + '/v.mp4'
        sources.append({'source': name, 'quality': 'SD', 'scraper': name, 'url': playlink,'direct': True})
    return sources
