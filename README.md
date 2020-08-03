# Housing_Search

Minneapolis has a very competitive housing and rental market. 
Staying on top of new postings can be time consuming and missing a posting by even one day can result in a missed opportunity.

This series of scripts scrapes popular sites for rental listings, compares against ones you've already seen, and alerts you via text using __[Google FI's email to text function](https://support.google.com/fi/answer/6356597?hl=en#:~:text=Send%20emails%20via%20text%20message&text=You%20can%20send%20text%20messages,.fi.google.com.)__

## Disclaimer:
As this project utilizes web scraping, it will eventually go out of date as websites update. 
Currently Zillow is the most strict with their captchas, but others may follow and break everything.

## How to use:
* Install non-standard python packages
* If using Google FI, apply your credentials in the demo_credentials.py
    * If you cannot text via email, explore using Twilio as an sms service
* Change the name of "demo_credentials" to "credentials"
* Manually set up a search in browser for one or more of the following sites:
    * Apartments.com
    * Craigslist
    * Trulia
    * Zillow
* Place the search url and site name in the urls.py list
* Run Housing_Search.py
* I suggest running the batch file included with Windows Task Scheduler every hour or two
    * Place your script path in the batch file


## Further info:
* __[Setting up a gmail account for python scripting](https://realpython.com/python-send-email/)__
* Tips for a good housing search:
    * Show only records posted within the last day
        * Or sort by newest
    * Zoom in as far as possible to restrict unnecessary results
        * Take advantage of the fact you can set up multiple urls to get just the areas you car about 