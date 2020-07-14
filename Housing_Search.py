import smtplib
import ssl

import bs4 as bs
import pandas as pd
import requests

from time import sleep
from fake_useragent import UserAgent
from credentials import sender_email, password, receiver_email


def soups_on(url):
    """returns bs object for HTML parsing"""
    # Set headers so we don't get bugged by captchas
    ua = UserAgent()

    headers = {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ua.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }
    source = requests.get(url, headers=headers)
    return bs.BeautifulSoup(source.content, 'lxml')


def get_zillow(url):
    # Get Zillow listing urls
    print("Trying to connect to Zillow", end="")
    while True:
        zillow_soup = soups_on(url)
        # Check for captcha, try again
        for h5 in zillow_soup.find_all('h5'):
            if "Please verify you're a human to continue" in h5.text:
                sleep(0.5)
                print(".", end="")
                continue
        break
    print('\n')

    # Check title for '0 Rentals'. Zillow gives 'similar results nearby' in this case which we ignore
    zero_rentals = False
    for h3 in zillow_soup.find_all('title'):
        if '0 Rentals' in h3.text:
            zero_rentals = True

    if not zero_rentals:
        return [listing['href'] for listing in zillow_soup.find_all('a', attrs={'class': 'list-card-link list-card-img'})]
    else:
        return []


def get_craigslist(url):
    # Get Craigslist urls
    print("Trying to connect to Craigslist")
    criagslist_soup = soups_on(url)

    # I haven't run into a captcha on craigslist, but I know they exist.
    # This is an attempt at capturing data if we think we ran into one
    # If we suspect a captcha in criagslist, make an error dump and alert via text
    if criagslist_soup.find(text='Captcha'):
        debug_msg = f"""
    Maybe found a captcha
    
    Craigslist url:
    {criagslist_url}
    
    html dump:
    {criagslist_soup.prettify()}
    """
        with open(r"C:\Users\lewi0\Desktop\Personal_Scripts\Housing_Search\error_log.txt", 'w', encoding="utf-8") as log:
            log.writelines(debug_msg)
        return ['check error log' + str(pd.to_datetime('today'))]

    return [listing['href'] for listing in criagslist_soup.find_all('a', attrs={'class': 'result-image gallery'})]


# Version Number
version = 0.1
debug = 0

# Urls
zillow_url = r'https://www.zillow.com/homes/for_rent/1-_beds/1.0-_baths/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-93.50802635404175%2C%22east%22%3A-93.10633873197143%2C%22south%22%3A44.868132495735146%2C%22north%22%3A45.062947488470165%7D%2C%22mapZoom%22%3A12%2C%22customRegionId%22%3A%222df575f09eX1-CR14087aax9bs72_uh1re%22%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A282815%2C%22max%22%3A450470%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22sqft%22%3A%7B%22min%22%3A700%7D%2C%22doz%22%3A%7B%22value%22%3A%221%22%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1000%2C%22max%22%3A1700%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22cat%22%3A%7B%22value%22%3Atrue%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22sdog%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
criagslist_url = r'https://minneapolis.craigslist.org/search/apa?sort=date&hasPic=1&postedToday=1&bundleDuplicates=1&search_distance=4&postal=55402&min_price=1000&max_price=1700&minSqft=600&maxSqft=1400&availabilityMode=0&pets_cat=1&pets_dog=1&no_smoking=1&sale_date=all+dates'
apts_url =r'https://www.apartments.com/houses/minneapolis-mn/min-1-bedrooms-1-bathrooms-1000-to-1700-pet-friendly/?bb=0gtmxlgn9K-t1tirG&so=8'

# Main
listings = get_zillow(zillow_url) + get_craigslist(criagslist_url)

# read csv
csv_path = r"C:\Users\lewi0\Desktop\Personal_Scripts\Housing_Search\seen_listings.csv"
seen_listings_df = pd.read_csv(csv_path)

# set datetime
seen_listings_df['date'] = pd.to_datetime(seen_listings_df['date'])

# get listings we haven't seen before
new_listings = [url for url in listings if url not in seen_listings_df['url'].values]

# send text for each new listing
if len(new_listings) > 0:
    # Open connection
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)

        for url in new_listings:
            message = f"""
            New Listing:
            {url}"""
            server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

# add new listings to df
for url in new_listings:
    seen_listings_df = seen_listings_df.append({'url': url, 'date': pd.to_datetime('today').floor('D')}, ignore_index=True)

# remove listings three days or older from df and if
seen_listings_df = seen_listings_df[seen_listings_df['date'] > pd.Timestamp('now').floor('D') + pd.offsets.Day(-7)]

# overwrite csv with df
seen_listings_df.to_csv(csv_path, index=False)
