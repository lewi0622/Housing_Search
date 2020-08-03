from support import soups_on
import re


def get_trulia(url):
    # Get Trulia urls
    print("Trying to connect to Trulia")
    trulia_soup = soups_on(url)

    base_url = r'trulia.com'

    try:
        trulia_listings = [base_url + listing['href'] for listing in trulia_soup.find_all(href=re.compile(r'/p/mn/minneapolis'))]
        # remove duplicates
        return list(dict.fromkeys(trulia_listings))
    except:
        return []
