from whoosh.index import create_in
from whoosh.qparser import QueryParser
from whoosh.fields import *
from whoosh.query import Term
from whoosh.analysis import StandardAnalyzer
import yaml
import csv
from bs4 import BeautifulSoup
import urllib2,urllib
import os

def getPhoneDetails(user_query):
	phones = {}
	url  = "http://www.flipkart.com{0}"
	hdr = {'User-Agent': 'Mozilla/5.0'}

	# Set index, we index title and content as texts and tags as keywords.
	# We store inside index only titles and ids.
	analyzer =StandardAnalyzer(stoplist=None, minsize=1)
	schema = Schema(title=TEXT(analyzer=analyzer, stored=True), content=STORED)
	 
	# Create index dir if it does not exists.
	if not os.path.exists("indexNew"):
	    os.mkdir("indexNew")

	ix = create_in("indexNew", schema)
	writer = ix.writer()

	with open("flipkartIDs.txt",'rb') as phoneList:
		json_data = yaml.load(phoneList)

	for links in json_data:
		writer.add_document(title=unicode(json_data[links],"utf-8"),content=unicode(links,"utf-8"))

	writer.commit()

	with ix.searcher() as searcher:
		query = QueryParser("title", ix.schema).parse(user_query)
		results = searcher.search(query, limit=6)
		print results
		for result in results:
			print result['title']
			url_page = url.format(result['content'])
			print url_page
			req = urllib2.Request(url_page,headers=hdr)
			page = urllib2.urlopen(req)

			soup = BeautifulSoup(page)
			try:
				price = str(soup.find('span',{'class':"selling-price omniture-field"}).text)
				print price
			except AttributeError,e:
				price = "NA"
			keyFeatures = soup.find('div',{'class':"productSpecs specSection"})
			phoneDetails = keyFeatures.text
			phones.update({result['title']:{'Price':price,'Specifications':"".join(line.strip() for line in phoneDetails.split("\t"))}})
	return phones