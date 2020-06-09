from nanitWebScraping.nanit_detailed_info_parser import parser_function
from nanitWebScraping.nanit_baby_schedule import baby_schedule_scraper
from nanitWebScraping.selenium_webscraping import selenium_webscraping_function

import time # to add dealy

#nanit data extractor
page_url_list = ["https://www.nanit.com/blog/baby-sleep-schedule/3-month-baby-sleep-schedule/",
                 "https://www.nanit.com/blog/baby-sleep-schedule/4-month-baby-sleep-schedule/",
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



for page_url in page_url_list:

    # webscraping using only beautiful soup
    # page_soup = webscraping_urlib(page_url)

    # webscraping using selenium
    page_soup = selenium_webscraping_function(page_url)

    # baby schedule saver function, and return baby_age for parser
    baby_age_return = baby_schedule_scraper(page_soup)

    # detailed parser function
    parser_function(page_soup, baby_age_return)

    print("Age: " + baby_age_return + " data extracted")
    time.sleep(5)

print("\n\n\n ---- Data scrapping complete ...")
