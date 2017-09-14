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
                        if 'lemon' not in p:
                            if 'http' in p:
                                p = p.replace('\\','')
                                sources.append({'source': 'Gvideo', 'quality': qual, 'scraper': name, 'url': p,'direct': True})
    return sources
 
