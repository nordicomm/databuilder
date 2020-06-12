import datetime
import constants
import json

from datetime import datetime as dt


import re
# Currently we have 10 sleep identifiers
# sleep_quality: (percentage)
# dur_nighttime_sleep: (hour, min)
# number_of_time_awake: (number)
# dur_awake_during_night: (hour, min)
# dur_bedtime_before_first_nighttime_sleep: (hour, min)
# go_to_bedtime: (time variable)
# dur_daytime_sleep: (hour, min)
# number_of_daytime_naps: (number)
# morning_wakeup_time: (time variable)
# sleep_technique_in_progress: indicater for the sleep technique in action


# sleep quality
# we have a current day data, and sleep quality will be part of it.
class duration:
    def __init__(self, dur_hours, dur_minutes, dur_seconds):
        self.dur_hours = dur_hours
        self.dur_minutes = dur_minutes
        self.dur_seconds = dur_seconds

# each class object will have one day data of the baby.
class baby_day:
    def __init__(self, log_date):
        #date of the day
        self.start_log_date = log_date
        self.end_log_date = log_date + datetime.timedelta(days=1)

        # time pointer to describe the current position of time
        self.pointer = self.start_log_date

        # morning wakeup and go to bedtime for log_date
        self.morning_wakeup_time = datetime.datetime.today() - datetime.datetime.today()
        self.go_to_bedtime = datetime.datetime.today() - datetime.datetime.today()

        #identifiers values such
        self.sleep_quality = 0; #sleep quality
        self.dur_nighttime_sleep = duration( 0, 0, 0) #nightime sleep duration
        self.number_of_time_awake = 0; #number of time baby was awake
        self.dur_awake_during_night = duration( 0, 0, 0) #how much time the baby was awake during the night
        self.dur_bedtime_before_first_nighttime_sleep = duration( 0, 0, 0) #bedtime before the first sleep during the night

        self.dur_daytime_sleep = duration( 0, 0, 0) #daytime sleep duration
        self.number_of_daytime_naps = 0 #number of naps during the day
        self.sleep_technique_in_progress = 0 #Push Sleep (1) / Easy Dream (2) / None (0)

        #naps records of the baby. This will include all the naps the baby had during log_date
        self.nap_time = []

        # feed times of the baby
        self.feed_time = []

        #bath time before the sleep
        self.bathtime_before_sleep = datetime.datetime.today() - datetime.datetime.today()

    def increment_pointer(self, hrs):
        self.pointer = self.pointer + datetime.timedelta(hours=hrs)

    def print_date(self):
        print(self.start_log_date, "sleep data")

    #def get_date(self):
        #return self.pointer.date()

# define the list of day object
day = [] # list of day, for which data is generated

def night_sleep_check(start_sleep, end_sleep):
    timestamp = datetime.datetime(year=1900, month=1, day=1, hour=18, minute=00)
    if start_sleep.time() > timestamp.time():
        return True
    elif end_sleep.time() > timestamp.time():
        if (end_sleep.time() - timestamp) > (timestamp - start_sleep.time()):
            return True
    else:
        return False

def initialize_objects():

    # computing the first date
    next_date = datetime.date.today() - datetime.timedelta(days=constants.NUMBER_OF_DAYS_DATA)

    # initializing the objects for all days, for which data is required
    for index in range(constants.NUMBER_OF_DAYS_DATA):
        day.append(baby_day(next_date))
        next_date = next_date + datetime.timedelta(days=1) # going to next day

        # checkpoint for object creation
        day[index].print_date()

# NOTE: I was working on generating a normal sequence with classes

def generate_data_for_baby(baby_age, sleep_data, timezone):
    # create nap_time for different days, and add them with the date
    # get_object date range
    # get normal data
    # append normal data with each date
    # add wakeup time
    # add bedtime

    # extract original data for sleep first
    sleep_normal_data = []
    for s_index in sleep_data:
        if baby_age == s_index['baby_age']:
            sleep_normal_data.append(s_index)

    print(sleep_normal_data)
    print(len(sleep_normal_data))
    print(sleep_normal_data[4])

    day[0].morning_wakeup_time = sleep_normal_data[0]['wakeup_time']
    day[0].go_to_bedtime = sleep_normal_data[len(sleep_normal_data)-1]['bed_time']

    nap_time = []
    # extract start and end time of naps
    for entry in sleep_normal_data:
        if len(entry) >= 3:
            add_baby_sleep = {}
            add_baby_sleep['on_bed_start_time'] = entry['on_bed_start_time'].replace(year=day[0].start_log_date.year,
                                                                                     month=day[0].start_log_date.month,
                                                                                     day=day[0].start_log_date.day)
            add_baby_sleep['on_bed_end_time'] = entry['on_bed_end_time'].replace(year=day[0].start_log_date.year,
                                                                                 month=day[0].start_log_date.month,
                                                                                 day=day[0].start_log_date.day)

            add_baby_sleep['sleep_time'] = add_baby_sleep['on_bed_end_time'] - add_baby_sleep['on_bed_start_time']

            add_baby_sleep['is_night_sleep'] = night_sleep_check(entry['on_bed_start_time'], entry['on_bed_end_time'])
            add_baby_sleep['timezone'] = timezone
            day[0].nap_time.append(add_baby_sleep)

    # note: next step is to generalize it

    print(day[0].nap_time)

def extract_sleep_data_from_nanit_json(data):
    sleep_data = []

    for index in data:

        s_data = {}
        s_data['baby_age'] = int(re.search(r'\d+', index['baby_age']).group(0))

        if index['baby_schedule_name'] == "Naptime":
            time_split = index['baby_schedule_time'].split(' - ')
            s_data['on_bed_start_time'] = dt.strptime(str(time_split[0]), '%I:%M %p')
            s_data['on_bed_end_time'] = dt.strptime(str(time_split[1]), '%I:%M %p')

            # append data
            sleep_data.append(s_data)

        if index['baby_schedule_name'] == "Bedtime":
            s_data['bed_time'] = dt.strptime(str(index['baby_schedule_time']), '%I:%M %p')
            sleep_data.append(s_data)

        if index['baby_schedule_name'] == "Wake and Milk Feed":
            s_data['wakeup_time'] = dt.strptime(str(index['baby_schedule_time']), '%I:%M %p')
            sleep_data.append(s_data)



    # note: remember to replace the date, using variable.replace function
    # print(sleep_data)
    return(sleep_data)




def generate_normal_sequence_6months():
    startDate = day[0].pointer
    # print start data
    print(startDate, "General")



