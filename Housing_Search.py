import pandas as pd
import os
import support

from apartments import get_apartments
from craigslist import get_craigslist
from trulia import get_trulia
from zillow import get_zillow

from urls import urls

# ********************************************************************
# Version Number
version = 0.3

# Known Issues
# Occasional Trulia postings with houses for sale instead of rentals
# ********************************************************************

listings = []
for url in urls:
    site = [*url][0]
    path = url[site]
    if site == 'apartments':
        listings += get_apartments(path)
    elif site == 'craigslist':
        listings += get_craigslist(path)
    elif site == 'trulia':
        listings += get_trulia(path)
    elif site == 'zillow':
        listings += get_zillow(path)

# read csv
csv_path = os.getcwd() + r"\seen_listings.csv"
seen_listings_df = pd.read_csv(csv_path, parse_dates=['date'], infer_datetime_format=True)

# get listings we haven't seen before
new_listings = [url for url in listings if url not in seen_listings_df['url'].values]

# Notify user
support.send_listing_sms(listings)

# add new listings to df
for url in new_listings:
    seen_listings_df = seen_listings_df.append({'url': url, 'date': pd.to_datetime('today').floor('D')}, ignore_index=True)

# remove listings three days or older from df and if
seen_listings_df = seen_listings_df[seen_listings_df['date'] > pd.Timestamp('now').floor('D') + pd.offsets.Day(-7)]

# overwrite csv with df
seen_listings_df.to_csv(csv_path, index=False)
