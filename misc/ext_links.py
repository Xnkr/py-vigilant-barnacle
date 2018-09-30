import requests
from bs4 import BeautifulSoup
import urllib2
import re

url = "http://softsmith.com/"
page = urllib2.urlopen(url)
f = open('E:\Testing\PerfTest\links.txt','w')
soup = BeautifulSoup(page,"lxml")

d = {
	'a':'href',
	'img':'src',
	'link':'href',
	'script':'src'
}

for key in d:
	
	for link in soup.findAll(key):
		if link.get(d[key]):
			src = link.get(d[key])
			if not 'http' in src:
				f.write(link.get(d[key])+'\n')
			else:
				f.write(link.get(d[key])+'\n')


f.close()

# response = requests.get(url)
# # parse html
# page = str(BeautifulSoup(response.content))


# def getURL(page):
#     start_link = page.find("a href")
#     if start_link == -1:
#         return None, 0
#     start_quote = page.find('"', start_link)
#     end_quote = page.find('"', start_quote + 1)
#     url = page[start_quote + 1: end_quote]
#     return url, end_quote

# while True:
#     url, n = getURL(page)
#     page = page[n:]
#     if url:
#         print url
#     else:
#         break