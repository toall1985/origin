import re
import requests

domain = ['yesmovies.to']
name = 'Yesmovies'

def resolve(url):
    sources = []
    qual = 'SD'
    html = requests.get(url).content
    match = re.findall('favorite\((.+?),',html)[0]
    second_url = 'https://yesmovies.to/ajax/v4_movie_episodes/'+match
    html2 = requests.get(second_url).content
    match2 = re.compile('data-id=.+?"(.+?)\"').findall(html2)
    for m in match2:
        m = m.replace('\\','')
        if len(m)==6:
            url = 'https://yesmovies.to/ajax/movie_token?eid='+m+'&mid='+match
            html3 = requests.get(url).content
            x,y = re.findall("_x='(.+?)', _y='(.+?)'",html3)[0]
            fin_url = 'https://yesmovies.to/ajax/movie_sources/'+m+'?x='+x+'&y='+y
            h = requests.get(fin_url).content
            source = re.findall('"sources":\[(.+?)\]',h)
            single = re.findall('{(.+?)}',str(source))
            for s in single:
                playlink = re.findall('"file":"(.+?)"',str(s))
                q = re.compile('"label":"(.+?)"').findall(str(s))
                for h in q:
                    qual = h
                    for p in playlink:
			p = p.replace('\\','')
                        if 'lemon' in p:
                            p = p+'|User-Agent=Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0&Host=streaming.lemonstream.me:1443&Referer=https://yesmovies.to'
                        if 'http' in p:
                            sources.append({'source': 'Gvideo', 'quality': qual, 'scraper': name, 'url': p,'direct': True})
    return sources
 
