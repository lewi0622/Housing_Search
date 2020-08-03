from support import soups_on


def get_apartments(url):
    # Get Apartments.com urls
    print("Trying to connect to Apartments.com")
    apartments_soup = soups_on(url)

    try:
        return [listing['href'] for listing in apartments_soup.find_all('a', attrs={'class': 'placardTitle js-placardTitle'})]
    except:
        return []
