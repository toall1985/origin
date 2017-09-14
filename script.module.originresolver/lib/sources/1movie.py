import re
import requests

domain = ['1movies.tv']
name = '1Movies'
sources = []

def resolve(url):
	html = requests.get(url).content
	match = re.compile('load_player\((.+?)\)').findall(html)
	for i in match:
		u = i
		headers = {
					"referer":url,
					"user-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
					"host":"1movies.tv"
				}
		item = 'http://1movies.tv/ajax/movie/load_player_v3?id='+u
		head_req = requests.post(item,headers=headers).content
		resp = re.compile('value":"(.+?)"').findall(head_req)
		for r in resp:
			new_headers = {
			"referer":url,
			"user-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
			"host":"xplay.1movies.tv"
			}
			newurl = 'http:'+r.replace('\\','')
			response = requests.post(newurl,headers=new_headers).json()
			results = response["playlist"]
			for item in results:
				playlink = item["file"]
				sources.append({'source': 'Gvideo', 'quality': 'HD', 'scraper': name, 'url': playlink,'direct': True})
	return sources