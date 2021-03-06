import datetime
import constants
import json

from datetime import datetime as dt

import re

import numpy as np
from constants import get_baby_requirements


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


# each class object will have one day data of the baby.
class baby_day:
    baby_age = 1
    baby_name = "Unknown"

    def __init__(self, log_date):
        # date of the day

        self.start_log_date = log_date
        self.end_log_date = log_date + datetime.timedelta(days=1)

        # time pointer to describe the current position of time
        self.pointer = self.start_log_date

        # morning wakeup and go to bedtime for log_date
        self.morning_wakeup_time = datetime.datetime.today() - datetime.datetime.today()
        self.go_to_bedtime = datetime.datetime.today() - datetime.datetime.today()

        self.next_morning_late_wakeup_flag = False  # next morning late wakeup flag
        self.pointer = self.start_log_date  # last day wakeup pointer

        # identifiers values such
        self.sleep_quality = 0;  # sleep quality
        self.dur_nighttime_sleep = datetime.timedelta()  # nightime sleep duration
        self.number_of_time_awake = 0;  # number of time baby was awake
        self.dur_bedtime_before_first_nighttime_sleep = datetime.timedelta(
            minutes=14)  # bedtime before the first sleep during the night
        self.dur_awake_during_night = datetime.timedelta(
            hours=1) + self.dur_bedtime_before_first_nighttime_sleep  # how much time the baby was awake during the night

        self.dur_daytime_sleep = datetime.datetime.today() - datetime.datetime.today()  # daytime sleep duration
        self.number_of_daytime_naps = 0  # number of naps during the day
        self.sleep_technique_in_progress = 0  # Push Sleep (1) / Easy Dream (2) / None (0)

        # naps records of the baby. This will include all the naps the baby had during log_date
        self.nap_time = []
        self.nap_timezone = 0

        # feed times of the baby
        # self.feed_time = []

    def increment_pointer(self, hrs):
        self.pointer = self.pointer + datetime.timedelta(hours=hrs)

    def print_date(self):
        print(self.start_log_date, "sleep data")

    # def get_date(self):
    # return self.pointer.date()


# define the list of day object
day = []  # list of day, for which data is generated


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
        next_date = next_date + datetime.timedelta(days=1)  # going to next day

        # checkpoint for object creation
        day[index].print_date()


# NOTE: I was working on generating a normal sequence with classes

def generate_normal_data_for_baby(baby_age_info, baby_name_info, timezone, sleep_data):
    # create nap_time for different days, and add them with the date
    # get_object date range
    # get normal data
    # append normal data with each date
    # add wakeup time
    # add bedtime

    for index in range(0, len(day)):
        # extract original data for sleep first
        sleep_normal_data = []
        for s_index in sleep_data:
            if baby_age_info == s_index['baby_age']:
                sleep_normal_data.append(s_index)

        day[index].baby_age = sleep_normal_data[0]['baby_age']
        day[index].baby_name = baby_name_info

        day[index].morning_wakeup_time = sleep_normal_data[0]['wakeup_time'].replace(
            year=day[index].start_log_date.year,
            month=day[index].start_log_date.month,
            day=day[index].start_log_date.day)

        day[index].go_to_bedtime = sleep_normal_data[len(sleep_normal_data) - 1]['bed_time'].replace(
            year=day[index].start_log_date.year,
            month=day[index].start_log_date.month,
            day=day[index].start_log_date.day)
        day[index].nap_timezone = timezone

        nap_time = []
        # extract start and end time of naps
        for entry in sleep_normal_data:
            if len(entry) >= 3:
                add_baby_sleep = {}
                add_baby_sleep['on_bed_start_time'] = entry['on_bed_start_time'].replace(
                    year=day[index].start_log_date.year,
                    month=day[index].start_log_date.month,
                    day=day[index].start_log_date.day)
                add_baby_sleep['on_bed_end_time'] = entry['on_bed_end_time'].replace(
                    year=day[index].start_log_date.year,
                    month=day[index].start_log_date.month,
                    day=day[index].start_log_date.day)

                add_baby_sleep['sleep_time'] = add_baby_sleep['on_bed_end_time'] - add_baby_sleep['on_bed_start_time']

                add_baby_sleep['is_night_sleep'] = night_sleep_check(entry['on_bed_start_time'],
                                                                     entry['on_bed_end_time'])
                day[index].nap_time.append(add_baby_sleep)

        # note: next step is to generalize it
        # print("date: " + str(day[index].start_log_date) + "--- data: " + str(day[index].nap_time))


def generate_normal_nighttime_data_for_baby():
    for index in range(0, len(day)):

        # get baby sleep requirements based on current age
        baby_requirements = get_baby_requirements(day[0].baby_age)

        # initialize the day variable that will be needed to comput
        day[index].dur_bedtime_before_first_nighttime_sleep = datetime.timedelta(minutes=14)

        # calculating baby daytime naps
        for nap in day[index].nap_time:
            day[index].dur_daytime_sleep += nap['sleep_time']

        print("Nighttime Checkpoint: Intitialization")

        # calculate how much sleep is required for the nighttime
        nighttime_sleep_required = datetime.timedelta(hours=baby_requirements['total_sleep']) - day[
            index].dur_daytime_sleep

        # ad a day, and wakeup time for next day wakeup time.
        next_day_wakeup = day[index].morning_wakeup_time + datetime.timedelta(days=1)

        # total time available to place the night time naps
        bedtime_and_wakeup_time_difference = next_day_wakeup - day[index].go_to_bedtime

        # duration on bed calculated including nighttime sleep, and duration awake during the night.
        # important: duration awake during the night includes ths bedtime before first sleep as well
        duration_on_bed_required = nighttime_sleep_required + day[index].dur_awake_during_night

        print("Nighttime Checkpoint: Calculations")

        # check if the time difference between goto_bedtime and wakeup time is enough for baby to wakeup on right time
        # next day
        if bedtime_and_wakeup_time_difference < duration_on_bed_required:
            day[index].next_morning_late_wakeup_flag = True  # baby will be waking up late

        # generating random nap sessions, as per requirements
        nap_session = np.random.multinomial(nighttime_sleep_required.seconds,
                                            np.ones(baby_requirements['nighttime_naps_number']) /
                                            baby_requirements['nighttime_naps_number'], size=1)[0]

        print(nap_session)

        if baby_requirements['nighttime_naps_number'] > 1:
            print("enter awake session calculation")
            awake_session = np.random.multinomial(day[index].dur_awake_during_night.seconds,
                                                  np.ones(baby_requirements['nighttime_naps_number'] - 1) /
                                                  (baby_requirements['nighttime_naps_number'] - 1), size=1)[0]
            print("1. Nap Session: " + awake_session)

        else:
            print('enter awake session calculation <= 1')
            awake_session = day[index].dur_awake_during_night.seconds
            print("1. Nap Session: " + str(awake_session))


        end_point = day[index].go_to_bedtime  # needed to have a start time at start of every loop

        print('Nighttime Checkpoint: session calculations')

        for nap_number in range(0, baby_requirements['nighttime_naps_number']):
            nap = {}
            if nap_number == 0:
                # calculating for first nap
                nap['on_bed_start_time'] = end_point
                nap['on_bed_end_time'] = nap['on_bed_start_time'] + datetime.timedelta(
                    seconds=int(nap_session[nap_number]))
                nap['is_night_sleep'] = True
                nap['sleep_time'] = nap['on_bed_end_time'] - nap['on_bed_start_time']
                nap['sleep_time'] -= day[index].dur_bedtime_before_first_nighttime_sleep
                end_point = nap['on_bed_end_time']
            else:
                # calculating naps after first nap
                nap['on_bed_start_time'] = end_point + datetime.timedelta(seconds=int(awake_session[nap_number - 1]))
                nap['on_bed_end_time'] = nap['on_bed_start_time'] + datetime.timedelta(
                    seconds=int(nap_session[nap_number]))
                nap['is_night_sleep'] = True
                nap['sleep_time'] = nap['on_bed_end_time'] - nap['on_bed_start_time']
                end_point = nap['on_bed_end_time']

            day[index].nap_time.append(nap)

        day[index].pointer = end_point
        # print(day[index].start_log_date)
        # print(day[index].nap_time)

    # end of day for loop

    # if bedtime_and_wakeup_time_difference > nighttime_sleep_required


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
    return (sleep_data)


def create_baby_day_sleep_date_for_json():
    baby_info = []
    for index in range(0, len(day)):
        for nap in day[index].nap_time:
            add_baby_sleep = {'baby_in_months': str(day[index].baby_age), 'baby_name': str(day[index].baby_name),
                              'sleep_time': str(nap['sleep_time']), 'on_bed_start_time': str(nap['on_bed_start_time']),
                              'on_bed_end_time': str(nap['on_bed_end_time']),
                              'is_night_sleep': str(nap['is_night_sleep']),
                              'timezone': str(day[index].nap_timezone)}

            baby_info.append(add_baby_sleep)
    # end of day for loop
    return baby_info


'''
    for sleep in baby_sleep_data:
        if baby_info_start['baby_age'] == sleep['baby_age']:
            if len(sleep) >= 3:  # it is a small hack to see if the sleep variable contains sleep start and end values
                add_baby_sleep = {}
                add_baby_sleep['baby_in_months'] = str(sleep['baby_age'])
                add_baby_sleep['baby_name'] = baby_info_start['baby_name']
                # date needed to be changed
                add_baby_sleep['sleep_time'] = str(sleep['on_bed_end_time'] - sleep['on_bed_start_time'])
                add_baby_sleep['on_bed_start_time'] = str(sleep['on_bed_start_time'])
                add_baby_sleep['on_bed_end_time'] = str(sleep['on_bed_end_time'])
                add_baby_sleep['is_night_sleep'] = night_sleep_check(sleep['on_bed_start_time'],
                                                                     sleep['on_bed_end_time'])
                add_baby_sleep['timezone'] = baby_info_start['timezone']
                baby_info.append(add_baby_sleep)
'''
