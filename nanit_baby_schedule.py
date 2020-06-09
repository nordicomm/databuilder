import json
import re

def baby_schedule_scraper(page_soup):

    # finds baby schedule data
    containers = page_soup.findAll("div", {"class": "month-schedule-chart"})

    # name the output file to write to local disk
    out_filename = "baby_schedule.json"

    # header of csv file to be written
    headers = "baby_age,baby_schedule_name,baby_schedule_time, baby_schedule_description \n"

    # opens file, and writes headers
    fh = open("baby_schedule.json", "a+") #open JSON file

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

    fh.write(json.dumps(output_list, indent=4, sort_keys=True)) # dump the list to JSON file

    fh.close()  # Close the file
    return baby_age[0]