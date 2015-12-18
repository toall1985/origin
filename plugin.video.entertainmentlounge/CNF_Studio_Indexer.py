import urllib2, re, os, sys, HTMLParser, 
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from bs4 import BeautifulSoup
from resources.modules import modules

#*************************************************************************************************************************************************************
# Variables Needed Global

Dialog = xbmcgui.Dialog()


#*************************************************************************************************************************************************************
#*************************************************************************************************************************************************************
#*************************************************************************************************************************************************************

# TEST MODE VARIABLES - TO BE DELETED

# GENRE URLS
#url = 'http://cnfstudio.com/genre/action/'
#url = 'http://cnfstudio.com/genre/adventure/'
#url = 'http://cnfstudio.com/genre/animation/'

# Next & Previous Page Test URL's
#url = 'http://cnfstudio.com/genre/action/page/2/'



# ****** NOTES ******
'''
> List_Genres 
	requires a url
	Get_Genres = find main genre body

'''

# INDEXER MODULES START HERE

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GET GENERES

# Actions - used to flip mode for movies and tv shows

action = 'Movies'

def List_genres(url):
	HTML = Open_Url(url)
	Soup = BeautifulSoup(HTML)
	Get_Genres = Soup.find_all('ul', {'class': 'generos'})
	for Genre_Link in Get_Genres:
		Page_Links = Genre_Link.find_all('a')
	for Page in Page_Links:
		Page = re.findall(r'<a href="(.*?)">(.*?)</a>',str(Page))
		for url, genre in Page:
			modules.addDir(genre,url,65,'','','')
	
	xbmcplugin.endOfDirectory(int(sys.argv[1]))
	modules.AUTO_VIEW('700')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LIST MOVIES

def List_Movies(url):
    HTML = Open_Url(url)   
    Movie_Links = re.compile('<div class="movie">(.+?)<span class="year">.+?</span></div>',re.DOTALL).findall(HTML)

    for Movie in Movie_Links:
        Get_Title = re.compile('<h2>(.+?)</h2>',re.DOTALL).findall(Movie)
        Get_Page = re.compile('<a href="(.+?)"><span class="player"></span></a>',re.DOTALL).findall(Movie)
        Get_Image = re.compile('<img src="(.+?)" alt=".+?">',re.DOTALL).findall(Movie)
        #Get_Rating = re.compile('<div class="imdb"><span class="icon-grade"></span>(.+?)</div>',re.DOTALL).findall(Movie)
        Movie_Data = []
        for Title in Get_Title:
            Title = Clean_UP(Title)
            Movie_Data.append(Title)
        
        for Page in Get_Page:
            print Page
            Movie_Data.append(Page)
        
        for Image in Get_Image:
            Movie_Data.append(Image)
        
        #for Rating in Get_Rating:
        #    Movie_Data.append(Rating)
        
        #print Movie_Data[0]
        #print Movie_Data[1]
        #print Movie_Data[2]
        #print Movie_Data[3]
        
        modules.AddTestDir(Movie_Data[0], Movie_Data[1], 69, Movie_Data[2], description='', isFolder=False, background='')
    
    Next_Page(url)
    
    endDirectory('movies', False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
	
	
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 20 Most Viewed

def MV_Movies(url):
    HTML = Open_Url(url)
    Soup = BeautifulSoup(HTML)
    Movie_Links = Soup.find_all('ul', {'class': 'lista'})
    Movie_Content = re.compile('<li>(.+?)</li>',re.DOTALL).findall(str(Movie_Links))
        
    for item in Movie_Content:
        Collect_Data = []
        Movie_ViewedNo = re.compile('<b>(.+?)</b>',re.DOTALL).findall(item)
        Movie_Link = re.compile('<a href="(.+?)">.+?</a>',re.DOTALL).findall(item)
        Movie_Title = re.compile('<a href=".+?">(.+?)</a>',re.DOTALL).findall(item)
                
        for Viewed_No in Movie_ViewedNo: Collect_Data.append(Viewed_No)
        for Link in Movie_Link: Collect_Data.append(Link)
        for Title in Movie_Title:
            Title = Clean_UP(Title)
            Collect_Data.append(Title)


        #print Collect_Data[0]
        #print Collect_Data[1]
        #print Collect_Data[2]
        modules.AddTestDir(Collect_Data[0]+' : '+Collect_Data[2] , Collect_Data[1], 69, '', description='', isFolder=False, background='')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Movies By Year

def Movie_ByYear(url):
    HTML = Open_Url(url)
    Soup = BeautifulSoup(HTML)
    Year_Links = Soup.find_all('ul', {'class': 'years'})
    Year_Content = re.compile('<li>(.+?)</li>',re.DOTALL).findall(str(Year_Links))
        
    for item in Year_Content:
        Year_Data = []
        Year = re.compile('<a class="ito" href=".+?">(.+?)</a>',re.DOTALL).findall(item)
        URL_Link = re.compile('<a class="ito" href="(.+?)">.+?</a>',re.DOTALL).findall(item)
                
        for Link in URL_Link: Year_Data.append(Link)
        for YR in Year: Year_Data.append(YR)


        #print Year_Data[0]
        #print Year_Data[1]
        if int(Year_Data[1]) >= 2001:
            modules.addDir(Year_Data[1],Year_Data[0],65,'','','')
        else: pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SEARCH MOVIES

def Search_Movie():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Name = Search_Name.lower()
    #Search_Name = Search_Name.replace(' ', '%22')
    search_URL = 'http://cnfstudio.com/?s=' + Search_Name
    HTML = Open_Url(search_URL)
    Soup = BeautifulSoup(HTML)
    
    Movie_Links = Soup.find_all('div', {'class': 'movie'})
    for Movie in Movie_Links:
        Get_Title = re.compile('<h2>(.+?)</h2>',re.DOTALL).findall(str(Movie))
        Get_Page = re.compile('<a href="(.+?)"><span class="player"></span></a>',re.DOTALL).findall(str(Movie))
        Get_Image = re.compile('<img alt=".+?" src="(.+?)"/>',re.DOTALL).findall(str(Movie))
        Get_Rating = re.compile('<div class="imdb"><span class="icon-grade"></span>(.+?)</div>',re.DOTALL).findall(str(Movie))
        Movie_Data = []
        for Title in Get_Title:
            Title = Clean_UP(Title)
            Movie_Data.append(Title)
        
        for Page in Get_Page: Movie_Data.append(Page)
        
        for Image in Get_Image: Movie_Data.append(Image)
        
        for Rating in Get_Rating: Movie_Data.append(Rating)

        Name_Switch = Movie_Data[0]
        if Search_Name in Name_Switch: modules.AddTestDir(Movie_Data[0], Movie_Data[1], 69, Movie_Data[2], description=Movie_Data[3], isFolder=False, background='')
        else: pass
		
		

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LIST TV SHOWS



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LIST TV SHOWS / SEASONS



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LIST TV SHOWS / SEASONS / EPISODES



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SEARCH TV SHOWS



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NEXT PAGE

def Next_Page(url):
	HTML = Open_Url(url)
	Soup = BeautifulSoup(HTML)
	PageLink = Soup.find_all('a', {'class': 'previouspostslink'})
	Page_Links = Soup.find_all('a', {'class': 'page larger'})
	#print len(PageLink)
	#print len(Page_Links)
	if len(PageLink) == 1:
		for Link in PageLink:
			next = re.compile('<a class="previouspostslink" href="(.+?)" rel="nofollow"><span class="icon-chevron-right2"></span></a>').findall(str(Link))
			for url in next:
				modules.addDir('Next Page',url,65,'','','')
				

	elif len(Page_Links) > 0:
		for Link in Page_Links:
			#print Link
			next = re.compile('<a class="page larger" href="(.+?)">(.+?)</a>').findall(str(Link))
			for url, PageNo in next:
				if '" rel="nofollow' in url:
					url = url.replace('" rel="nofollow', '')
				modules.addDir('Page: ' + PageNo,url,65,'','','')
				
				
	
	else: pass
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PREVIOUS PAGE

def Previous_Page(url):
	HTML = Open_Url(url)
	Soup = BeautifulSoup(HTML)
	PrevPageLink = Soup.find_all('a', {'class': 'previouspostslink'})
	print len(PrevPageLink)
	if len(PrevPageLink) > 0:
		
		for Link in PrevPageLink:
			print Link
			Prev = re.compile('<a class=".+?" href="(.+?)" rel=".+?"><span class="icon-chevron-left2"></span></a>').findall(str(Link))
			print 'hello'
			print Prev
			for url in Prev:
				print url
	
	else: pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# Decide if to move or keep

def Open_Url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def Get_Movie_Page(url):
	HTML = Open_Url(url)
	Page_Link = re.compile('<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe></div>',re.DOTALL).findall(HTML)
	No_PageLinks = len(Page_Link)

	for PageLink in Page_Link:
		PageLink = PageLink.replace('player','watch')
		Resolve_Link = PageLink + '&fv=&sou='
		Resolve_Page = Open_Url(Resolve_Link)
		Resolved = re.compile('<source src="(.+?)" type=".+?">',re.DOTALL).findall(Resolve_Page)
		for Link in Resolved:
			if Link == None: return 'No Link'
			else: return Link

			

def MoviePlayURL(url):
	HTML = Open_Url(url)

def normalize(title):
    try:
        try: return title.decode('ascii').encode("utf-8")
        except: pass

        t = ''
        for i in title:
            c = unicodedata.normalize('NFKD',unicode(i,"ISO-8859-1"))
            c = c.encode("ascii","ignore").strip()
            if i == ' ': c = i
            t += c

        return t.encode("utf-8")
    except:
        return title

def endDirectory(content, close):
    if content in ['movies', 'tvshows', 'seasons', 'episodes']:
        control.content(int(sys.argv[1]), content)

    if close == True: control.directory(int(sys.argv[1]), cacheToDisc=True)

    if close == True and content in ['movies', 'tvshows', 'seasons', 'episodes']:
        views.setView(content)


def Clean_UP(Title):
	if '&#8217;' in Title: Title = Title.replace('&#8217;', '\'')
	if '&#8211;' in Title: Title = Title.replace('&#8211;', '-')
	if '&#8216;' in Title: Title = Title.replace('&#8216;', '\'')
	if '&#038;' in Title: Title = Title.replace('&#038;', '&')
	Title = Title.lower()
	return Title
		
# To Be Deleted

def Resolve_CNF_Link(name, url):
	CNF_Link = Get_Movie_Page(url)
	print 'Returned >>> : ' + str(CNF_Link)
	Plp.resolveUrl(name, CNF_Link, '', '', '', '', '')

	

# RUN MODES FOR TESTING PURPOSES!!!!!!

# List All Genres
#List_genres(url)

# List All Movies
#List_Movies(url)

# Next Page
#Next_Page(url)

# Previous Page
#Previous_Page(url)



