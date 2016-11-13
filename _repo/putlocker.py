import re
import requests
title = 'the flash'
season = '3'
episode = '5'

class Putlocker():
    name = "Putlocker"
    domains = ['http://putlockers.ch/']
    Sources = ['vodlocker','vidbull']
    List = []
    sources = []

    def __init__(self):
        self.base_link = 'http://putlockers.ch/'
        self.scrape_episode(title,season,episode)

    def scrape_episode(self, title, season, episode):
        try:
            print 'scrape_episode'
            url = self.base_link + 'watch-'+title.replace(' ','-').lower()+'-tvshow-season-'+season+'-episode-'+episode+'-online-free-putlocker.html'
            OPEN = requests.get(url).text
            match = re.compile('<td class="entry">.+?href="(.+?)" target="').findall(OPEN)
            for url in match:
                print url
                for item in self.Sources:
                    print 'item'
                    if item in url:
                        print item
                        self.link_sources(url)
            print 'Sources = '+str(self.sources)
        except:
            pass
            return []

    def link_sources(self, url):
        try:
            print 'link_sources'
            HTML = requests.get(url).text
            match = re.compile('<iframe style=.+?" src="(.+?)"').findall(HTML)
            match2 = re.compile('<IFRAME SRC="(.+?)"').findall(HTML)
            match3 = re.compile('<IFRAME style=".+?" SRC="(.+?)"').findall(HTML)
            for url in match:
                print 'main:'+url
                self.main(url)
            for url in match2:
                print 'main2:'+url
                self.main(url)
            for url in match3:
                print 'main3:'+url
                self.main(url)
        except:
            pass

    def main(self, url):
        print 'main'
        if 'vidbull' in url:
            self.vidbull(url)
        elif 'vodlocker' in url:
            self.vodlocker(url)
        elif 'vidto' in url:
            self.vidto(url)
        else:
            pass

    def vidbull(self,url):
        print 'vidbull'
        try:
            HTML = requests.get(url).text
            match = recompile('<source.+?src="(.+?)"').findall(HTML)
            for Link in match:
                self.sources.append(
                    {'source': 'vidbull', 'quality': 'SD', 'scraper': self.name, 'url': Link, 'direct': False})
        except:
            pass
			
    def vidto(self, url):
        try:
            HTML = requests.get(url).text
            match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"', re.DOTALL).findall(HTML)
            for Link, name in match:
                self.sources.append(
                    {'source': 'vidto', 'quality': 'SD', 'scraper': self.name, 'url': Link, 'direct': False})
        except:
            pass

    def vodlocker(self, url):
        try:
            HTML = requests.get(url).text
            match = re.compile('file: "(.+?)",.+?skin', re.DOTALL).findall(HTML)
            for Link in match:
                self.sources.append(
                    {'source': 'vodlocker', 'quality': 'SD', 'scraper': self.name, 'url': Link, 'direct': False})
        except:
            pass


Putlocker()
