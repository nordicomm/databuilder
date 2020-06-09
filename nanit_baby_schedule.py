
import re

def baby_schedule_scraper(page_soup):

    # finds baby schedule data
    containers = page_soup.findAll("div", {"class": "month-schedule-chart"})

    # name the output file to write to local disk
    out_filename = "baby_schedule.csv"

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

        # Grab the schedule name, and time from the text
        schedule_name = schedule_extract[0].text
        schedule_time = schedule_extract[1].text

        # Grab the description of the schedule
        schedule_description = container.p

        # prints the datasets to console

        # print("baby age: " + baby_age[0])
        # print("Schedule Time: " + schedule_time)
        # print("Schedule Name: " + schedule_name)
        # print("schedule description: " + schedule_description.text + "\n")

        # writes the dataset to file
        f.write(baby_age[0] + ", " + schedule_name + ", " + schedule_time + ", " + schedule_description.text + "\n")

        #end of "container" for loop

    f.close()  # Close the file
    return baby_age[0]