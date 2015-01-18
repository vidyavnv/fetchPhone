import csv,json
from bs4 import BeautifulSoup
import urllib2,urllib
import sys
from itertools import islice

url  = "http://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&q={0}"
hdr = {'User-Agent': 'Mozilla/5.0'}

## dictionary to store key: url of the phone and value as name of the phone
phoneInfo = {}

## To remove parts of href after sep keyword to make href unique
sep = '&otracker='

## Only checks for Samsung phones
with open("phonesFromSanpdeal.csv",'rb') as phoneList:
	phonereader = csv.reader(islice(phoneList,1284,1538))

	for phone in phonereader:
		quoted_query = urllib.quote(phone[0])
		url_page = url.format(quoted_query)
		print url_page
		try:
			req = urllib2.Request(url_page,headers=hdr)
			page = urllib2.urlopen(req)

			soup = BeautifulSoup(page)
			## Check if it doesn't match any search on Flipkart else fetch the href links to the product
			if soup.find("div",{"id":"redirectMessage"}):
				print "phones are not available for %s " % phone[0]
			else:
				print "phones are available for ",phone[0]
				fetchPhones = soup.findAll("div",{"class":"pu-title"})
				print "%d number of phones area available for %s" % (len(fetchPhones),phone[0])
				for fetchPhone in fetchPhones:
					phoneName = fetchPhone.find('a')['title']
					phoneID = fetchPhone.find('a')['href']
					phoneInfo.update({phoneID.split(sep,1)[0]:phoneName})
		except:
			data = json.dumps(phoneInfo)

			with open('dataFinalNew.txt', 'w') as outfile:
			    outfile.write(data)

			sys.exit()



data = json.dumps(phoneInfo)

with open('IDsFromFlipkart.txt', 'w') as outfile:
    outfile.write(data)

