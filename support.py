import bs4 as bs
from fake_useragent import UserAgent
import requests
import smtplib
import ssl

from settings.credentials import sender_email, password, receiver_email


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


def send_listing_sms(new_listings):
    """Using a gmail address/password from credentials, sends an sms with each listing to phone number from
    credentials """
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
