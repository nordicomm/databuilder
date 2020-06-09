
from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# data scraping with urlib

def webscraping_urlib(page_url):
    # URl to web scrap from.
    # page_url = "https://www.nanit.com/blog/baby-sleep-schedule/3-month-baby-sleep-schedule/"

    # opens the connection and downloads html page from url
    uClient = uReq(page_url)
    print("url" + page_url)

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    return page_soup

