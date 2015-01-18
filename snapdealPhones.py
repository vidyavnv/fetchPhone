from bs4 import BeautifulSoup
import urllib2
import csv

countPhones = 0
url = "http://www.snapdeal.com/products/mobiles-mobile-phones?sort=plrty&page={0}&start={1}"
hdr = {'User-Agent': 'Mozilla/5.0'}

phones = []

## Number of pages as on 14 January 2015 were 314
for i in range(0,314):
	start = i * 20
	page = i
	url_page = url.format(page,start)
	try:
		req = urllib2.Request(url_page,headers=hdr)
		page = urllib2.urlopen(req)

		soup = BeautifulSoup(page)
		## fetching phone names from Snapdeal
		divs = soup.findAll("div",{"class":"product-title"})

		for div in divs:
			phones.append(div.find("a").contents[0].strip())
			countPhones = countPhones + 1
	except:
		pass

## Write to a csv file
with open('phonesFromSanpdeal.csv', 'wb') as csvfile:
	phonelist = csv.writer(csvfile, lineterminator='\n')
	for phone in phones:
		phonelist.writerow([phone])