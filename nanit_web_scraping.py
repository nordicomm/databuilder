from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

from nanit_detailed_info_parser import parser_function
from nanit_baby_schedule import baby_schedule_scraper

import time # to add dealy

#nanit data extractor
page_url_list = ["https://www.nanit.com/blog/baby-sleep-schedule/3-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/4-month-baby-sleep-schedule/",
                 ]
'''
                 "https://www.nanit.com/blog/baby-sleep-schedule/5-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/6-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/7-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/8-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/9-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/10-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/11-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/12-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/13-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/14-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/15-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/16-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/17-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/18-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/19-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/20-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/21-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/22-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/23-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/24-month-baby-sleep-schedule/"
                 ]
'''

for page_url in page_url_list:
    # URl to web scrap from.
    #page_url = "https://www.nanit.com/blog/baby-sleep-schedule/3-month-baby-sleep-schedule/"

    # opens the connection and downloads html page from url
    uClient = uReq(page_url)
    print("url" + page_url)

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    # baby schedule saver function, and return baby_age for parser
    baby_age_return = baby_schedule_scraper(page_soup)

    # detailed parser function
    parser_function(page_soup, baby_age_return)

    print("Age: " + baby_age_return + " data extracted")
    time.sleep(10)

print("\n\n\n ---- Data scrapping complete ...")
