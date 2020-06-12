from selenium_webscraping import selenium_webscraping_function

import time  # to add dealy
import json
from html.parser import HTMLParser
import re

# TAGS to separate title from paragraph descriptions
SUBSTRING_TITLE_TAG = 'Titl3: '
SUBSTRING_DESCRIPTION_TAG = 'D3scr1ption: '


# class to help us separate start tags, end tags, data, and print outcomes
class MyHTMLParser(HTMLParser):
    c_tag = 'a'  # tag is used to figure out whether data belongs to header tag/paragraph tag
    info = []  # varialble to store info.
    line_counter = 0

    # class function called on receiving start of tag as argument
    def handle_starttag(self, tag, attrs):
        if tag in ['tr', 'td', 'th']:
            self.c_tag = tag

    # class function called on receiving end of tag as argument
    def handle_endtag(self, tag):
        if self.c_tag == 'tr':
            self.c_tag = 'a'
        self.line_counter = 0

    # class function called on receiving tag's data as argument
    def handle_data(self, data):
        if self.c_tag in ['td', 'th']:
            if not data.isspace():
                if self.line_counter == 0:
                    self.info.append(data.rstrip("\n"))
                    self.line_counter = self.line_counter + 1

    def print_list(self):  # print function
        index = 0
        for x in self.info:
            index = index + 1
            print(" line" + str(index) + " - data: " + str(x) + "\n")


def baby_schedule_scraper(page_soup):
    output_list = []
    # finds baby schedule data
    containers = page_soup.findAll("div", {"class": "entry-content"})
    tables = containers[0].findAll("table")
    print(len(tables))

    baby_schedule = []

    for table in tables[1:]:
        parser_info = MyHTMLParser()
        parser_info.feed(str(table))

        # find the header first
        start_parser = 0
        baby_week_number = 0
        for index in range(0, len(parser_info.info)-1):
            if "Week" in parser_info.info[index]:
                baby_week_number = str(int(re.search(r'\d+', parser_info.info[index]).group(0)))

            if parser_info.info[index] == 'Time':
                start_parser = index + 2

        baby_schedule.append({'baby_Schedule_Age_Weeks': baby_week_number})
        # parse the data
        for index in range(start_parser, len(parser_info.info)-1, 2):

                baby_activity = {'Activity': parser_info.info[index + 1], 'Time': parser_info.info[index]}
                baby_schedule.append(baby_activity)
                print(baby_week_number + " Week" + str(baby_activity))

    return baby_schedule
    # in the loop, we are trying to skip the first table
    # for table in tables[1:]:


'''
    # baby_age from the header
    baby_age_container = containers[0].findAll("div", {"class": "month-schedule-chart-title"})
    baby_age = re.findall(r'\d+', baby_age_container[0].text)

    baby_schedule_container = containers[0].findAll("div", {"class": "month-schedule-chart-row"})

    output_list = []
    # loops over each product and grabs attributes about
    # each product
    for container in baby_schedule_container:
        schedule = {} # loop's local variable

        # Finds all the tags "span" from within the div
        schedule_extract = container.select("span")

        # extract description of the schedule
        description = container.findAll("div", {"class": "month-schedule-chart-col3"})


        # add baby age for each schedule
        schedule['baby_age'] = str(baby_age)
        # Grab the schedule name, and time from the text
        schedule['baby_schedule_name'] = schedule_extract[0].text
        schedule['baby_schedule_time'] = schedule_extract[1].text

        # Grab the description of the schedule
        schedule['baby_schedule_description'] = description[0].text.replace('\n', ' ') # replacing \n in the text

        output_list.append(schedule)
        #end of "container" for loop

    # for x1 in output_list: # print the output list data
    #   print("\n\n output list" + str(x1))
'''
# ---------------------------
# end of baby schedule scraper

# baby sleep data extractor
page_url_list = ["https://www.babysleepsite.com/newborns/newborn-sleep-schedules-by-week/#1week"]

json_output_list = []

# name the output file to write to local disk
out_filename = "babysleepsite_schedule.json"
# opens file, and writes headers
fh = open(out_filename, "w+")  # open JSON file

for page_url in page_url_list:
    # webscraping using only beautiful soup
    # page_soup = webscraping_urlib(page_url)

    # webscraping using selenium
    page_soup = selenium_webscraping_function(page_url)
    jason_output_list = baby_schedule_scraper(page_soup)
    fh.write(json.dumps(jason_output_list, indent=4, sort_keys=True))  # dump the list to JSON file

    # time.sleep(5)

fh.close()  # Close the file

print("\n\n\n ---- Data scrapping complete ...")
