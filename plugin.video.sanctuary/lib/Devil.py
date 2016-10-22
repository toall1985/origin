import re,process,urllib,search,base64

def White_Devil():
	HTML = process.OPEN_URL('http://kodimaniacs.com/HdStreams.xml')
	match = re.compile('<dir>(.+?)</dir>',re.DOTALL).findall(base64.decodestring(HTML))
	for item in match:
		name = re.compile('<name>(.+?)</name>').findall(str(item))
		for name in name:
			name = name
		url = re.compile('<link>(.+?)</link>').findall(str(item))
		for url in url:
			url = url
		iconimage = re.compile('<thumbnail>(.+?)</thumbnail>').findall(str(item))
		for iconimage in iconimage:
			iconimage = iconimage
		process.Menu(name,url,1801,iconimage,'','','')
		
def White_Devil_Loop(url):
	HTML = process.OPEN_URL(url)
	plugin = re.compile('<plugin>.+?<name>(.+?)</name>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?</plugin>',re.DOTALL).findall(HTML)
	for name,url,iconimage in plugin:
		if 'utube' in url:
			if 'playlist' in url:
        		from pyramid.pyramid import addLink
		        total = len(plugin)
		        addLink(url[0],name.encode('utf-8', 'ignore'),iconimage,'','','','',True,None,'',total)