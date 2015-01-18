Get details of the phones from Flipkart
=======================================

### Link to Application
<https://fetchphone.herokuapp.com>

## OVERVIEW

1. snapdealPhones.py fetches a list of all the mobiles hosted on their website. (As on 14th January there were 6000 mobiles) and stores it in phonesFromSanpdeal.csv (As a sample snapdealphones.csv is on the repository ordered in reverse)
2. flipkartDetails.py searches unique href corresponding to the list phones (csv created above) and creates a dictionary to store href as key and name of the phones(as searched by flipkart) as value and stores this dictionary in IDsFromFlipkart.txt (flipkartIDs.txt is just a sample which has nearly 200 records for all phones from Samsung )
3. createIndex.py uses whoosh module to search for descriptions as given by user.

## How to run the code
0. Install all the dependencies by running:
		$ pip install -r requirements.txt
1. To get phones from snapdeal:
		$ python snapdealPhones.py  
	This creates a csv file phonesFromSanpdeal.csv
2. To get the links corresponding to the phones from Snapdeal from Flipkart, run:
		$ python flipkartDetails.py
	This creates a csv file IDsFromFlipkart.txt
3. To search for a term, run:
		$ python get_details.py
	Open http://127.0.0.1:5000/ and enter the serach query