import re,process,urllib,search

def Todays_Football_Menu():
	process.Menu('Mainstream Channels','',1751,'','','','')
	process.Menu('LiveOnSat Channels [COLORred]NOT WORKING - will be in a future update[/COLOR]','','','','','','')

def Todays_Football():
	HTML = process.OPEN_URL('http://www.live-footballontv.com/')
	block = re.compile('<div id="listings"><div class="container" align="center"><div class="row-fluid"><div class="span12 matchdate">(.+?)<div class="span12 matchdate">',re.DOTALL).findall(HTML)
	items = re.compile('span4 matchfixture">(.+?)</div>.+?span4 competition">(.+?)</div>.+?span1 kickofftime">(.+?)</div>.+?span3 channels">(.+?)</div>').findall(str(block))
	for name,comp,time,channels in items:
		name2 = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&#39;','\'').replace('&amp;','&').replace('&quot;','"')
		comp2 = (comp).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&#39;','\'').replace('&amp;','&').replace('&quot;','"')
		channels2 = (channels).replace('&nbsp;','-').replace('-','').replace('&#039;','\'').replace('&#39;','\'').replace('&amp;','&').replace('&quot;','"')
		process.Menu(time+' : '+name2+' - '+channels2,channels2,1752,'','',comp2,'')
		
def Search_Channels_Mainstream(url):
	splitter = url + '/'
	match = re.compile('(.+?)/').findall(str(splitter))
	for url in match:
		Search_name = (url).lower()
		search.Live_TV(Search_name)
		
