from support import soups_on
from time import sleep


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
    print()

    # Make a copy of soup
    zillow_soup_copy = zillow_soup.__copy__()

    # Locate the 'search-list-relaxed-results'
    relaxed_results = zillow_soup_copy.find('div', attrs={'class': 'search-list-relaxed-results'})
    if relaxed_results:
        # remove relaxed results from tree
        relaxed_results.extract()
        return [listing['href'] for listing in zillow_soup_copy.find_all('a', attrs={'class': 'list-card-link list-card-img'})]
    return [listing['href'] for listing in zillow_soup.find_all('a', attrs={'class': 'list-card-link list-card-img'})]
