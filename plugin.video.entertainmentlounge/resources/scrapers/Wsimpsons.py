import urllib2, re, cookielib
from urllib2 import urlopen
from cookielib import CookieJar
from resources.modules import modules # change this to your default py where your addDir is mate or what ever you want to pull to list item

#-------------------------------------------------------------------------------------

BaseURL = 'http://watch-simpsons.com/downloads/'
cookieJar = CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
urlOpener.addheaders = [('User-Agent', 'Mozilla/5.0')]
#----------------Test URL'S-----------------------------------------------------------
#url = 'http://watch-simpsons.com/downloads/Bones%20-%20The%20Complete%20Season%207%20%5bHDTV%5d/'
#url = 'http://watch-simpsons.com/downloads/CSI%20Miami%20Season%2010%20(Complete)%20%5bLuke1382%5d/'
#url = 'http://watch-simpsons.com/downloads/Two%20and%20a%20Half%20Men%20Season%201%20Complete%20480p%20HDTV%20x264%20%5bVectoR%5d/'
#url = 'http://watch-simpsons.com/downloads/The.Big.Bang.Theory.S02.Season.2.720p.5.1Ch.BluRay.ReEnc-DeeJayAhmed/'
#url = 'http://watch-simpsons.com/downloads/Criminal%20Minds%20Season%209%20Complete/'
#url = 'http://watch-simpsons.com/downloads/The.Mentalist.S05.Season.5.720p.HDTV.X264-DIMENSION%20%5bPublicHD%5d/'
#url = 'http://watch-simpsons.com/downloads/The.Big.Bang.Theory.S02.Season.2.720p.5.1Ch.BluRay.ReEnc-DeeJayAhmed/'
#url = ''
#url = ''
#-------------------------------------------------------------------------------------

def ParseURL(url): # make sure to send url when setting mode up
	response = urlOpener.open(url).read()
		
	try:
		Titles = re.findall(r'<a .*?>(.*?)</a>',response)
		Links = re.findall(r'<a.*?href="(.*?)">',response)
			
		for link in Links:
			if '.gif' in link:
				pass
			elif '/downloads/' in link:
				pass
			elif '.txt' in link:
				pass
			else:
				name = link
				if 'txt' in name:
					pass
				if 'HDTV' in name:
					name = name.replace ('HDTV', '')
				if 'XviD-LOL' in name:
					name = name.replace ('XviD-LOL', '')
				if 'x264-LOL' in name:
					name = name.replace ('x264-LOL', '')
				if 'X264-DIMENSION' in name:
					name = name.replace ('X264-DIMENSION', '')
				if '720p' in name:
					name = name.replace ('720p', '')
				if 'avi' in name:
					name = name.replace ('avi', '')
				if 'mp4' in name:
					name = name.replace ('mp4', '')
				if 'mkv' in name:
					name = name.replace ('mkv', '')
				if '%20' in name:
					name = name.replace ('%20', ' ')
				if '%5bVTV%5d' in name:
					name = name.replace ('%5bVTV%5d', ' ')
				if 'DeeJayAhmed' in name:
					name = name.replace ('DeeJayAhmed', '')
				if '-' in name:
					name = name.replace ('-', '')
				if '1Ch' in name:
					name = name.replace ('1Ch', '')
				if 'BluRay' in name:
					name = name.replace ('BluRay', '')
				if 'ReEnc' in name:
					name = name.replace ('ReEnc', '')
				#if '5' in name:
					#name = name.replace ('5', '')
				if '.' in name:
					name = name.replace('.', ' ')
								
				modules.AddTestDir(name ,url+link, 28, "", isFolder=False) # This is where the links are added so what every you use for your play links
	except Exception, e:
		print str(e)
		
'''
you need to make a list with the folder url you want in there like i have got test ones at the top

then parse that out as you would normally but instead of listing as a link list as a folder

then send to here mate which will spit out a link for each one in there folder on site so if its updated it updates in your list

very nice sounds good to me less work is better haha

yeah i was going to scrape the first big folder as well but would be hard to seperate the movies from shows

ive got all the movie links in php files if you want them mate

yeah mate send them over ill intergrate it into this :)
sweet g oiodl luck ill save and send over now mate

cheers nice one ill let you fetch missus then pester you later haha ;-)sound mate

'''