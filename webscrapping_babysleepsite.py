from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import re

import json

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    c_tag = 'a'
    info = []

    def handle_starttag(self, tag, attrs):
        if tag in ['h2', 'p']:
            self.c_tag = tag

    def handle_endtag(self, tag):
        if tag in ['h2', 'p']:
            self.c_tag = 'a'

    def handle_data(self, data):
        if self.c_tag == 'h2':
            self.info.append('Titl3: ' + data)

        if self.c_tag == 'p':
            self.info.append('D3scr1ption: ' + data)


    def print_list(self):
        for x in self.info:
            print(str(x) + "\n")

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


# URl to web scrap from.
page_url = "https://www.nanit.com/blog/baby-sleep-schedule/3-month-baby-sleep-schedule/"

# opens the connection and downloads html page from url
uClient = uReq(page_url)


# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
containers = page_soup.findAll("div", {"class": "month-schedule-chart"})
information = page_soup.findAll("div", {"class": "article-pure-content clearfix"})

parser_info = MyHTMLParser()
parser_info.feed(str(information[0]))


# name the output file to write to local disk
out_filename = "babyschedule.csv"

# header of csv file to be written
headers = "baby_age,baby_schedule_name,baby_schedule_time, baby_schedule_description \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

# baby_age from the header
baby_age_container = containers[0].findAll("div", {"class": "month-schedule-chart-title"})
baby_age = re.findall(r'\d+', baby_age_container[0].text)

baby_schedule_container = containers[0].findAll("div", {"class": "month-schedule-chart-row"})

# loops over each product and grabs attributes about
# each product
for container in baby_schedule_container:

    # Finds all the tags "span" from within the div
    schedule_extract = container.select("span")

    #Grab the schedule name, and time from the text
    schedule_name = schedule_extract[0].text
    schedule_time = schedule_extract[1].text

    #Grab the description of the schedule
    schedule_description = container.p

    # prints the dataset to console

    #print("baby age: " + baby_age[0])
    #print("Schedule Time: " + schedule_time)
    #print("Schedule Name: " + schedule_name)
    #print("schedule description: " + schedule_description.text + "\n")


    # writes the dataset to file
    f.write(baby_age[0] + ", " + schedule_name + ", " + schedule_time + ", " + schedule_description.text + "\n")

output_list = []

# baby age tag
baby_age_tag = {}
baby_age_tag["baby_age"] = str(baby_age)
output_list.append(baby_age_tag)

addtitle = {}
p_index = 0
substring_title = 'Titl3:'
substring_desc = 'D3scr1ption:'

fh = open("baby_schedule_details.json", "a+")

for x in parser_info.info:
    # find title, and add as
    # print("data: " + x)
    title = {}
    if substring_title in x:
        if p_index > 0:
            title.update(addtitle)
            output_list.append(title)
            p_index = 0

        addtitle['title'] = x.replace(substring_title, '')

    #find if paragraph
    if substring_desc in x:
        if p_index > 0:
            addtitle['description'] += x.replace(substring_desc, '')

        else:
            addtitle['description'] = x.replace(substring_desc, '')
            p_index = p_index + 1

output_list.append(addtitle)

for x1 in output_list:
    print("\n\n output list" + str(x1))

fh.write(json.dumps(output_list, indent=4, sort_keys=True)) # added an extra ')'.. code will now work

fh.close()
f.close()  # Close the file
