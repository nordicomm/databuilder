from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import re

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "https://www.nanit.com/blog/baby-sleep-schedule/3-month-baby-sleep-schedule/"

# opens the connection and downloads html page from url
uClient = uReq(page_url)


# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
containers = page_soup.findAll("div", {"class": "month-schedule-chart"})

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

    print("baby age: " + baby_age[0])
    print("Schedule Time: " + schedule_time)
    print("Schedule Name: " + schedule_name)
    print("schedule description: " + schedule_description.text + "\n")

    if schedule_time == "":
        print("empty")

    # writes the dataset to file
    f.write(baby_age[0] + ", " + schedule_name + ", " + schedule_time + ", " + schedule_description.text + "\n")


f.close()  # Close the file
