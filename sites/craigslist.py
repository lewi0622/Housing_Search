from support import soups_on
import pandas as pd


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
    {url}
    
    html dump:
    {criagslist_soup.prettify()}
    """
        with open(r"C:\Users\lewi0\Desktop\Personal_Scripts\Housing_Search\error_log.txt", 'w', encoding="utf-8") as log:
            log.writelines(debug_msg)
        return ['check error log' + str(pd.to_datetime('today'))]

    try:
        return [listing['href'] for listing in criagslist_soup.find_all('a', attrs={'class': 'result-image gallery'})]
    except:
        return []
