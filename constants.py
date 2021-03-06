import json

NUMBER_OF_DAYS_DATA = 7  # date generated for each baby.

# default wakeup time for the baby
DEFAULT_WAKEUP_TIME_HOUR = 6
DEFAULT_WAKEUP_TIME_MINUTES = 15

# minimum/maximum wakeup-time and bedtime for the baby
MIN_WAKEUP_TIME_HOUR = 5
MIN_WAKEUP_TIME_MINUTES = 0

MAX_WAKEUP_TIME_HOUR = 9
MAX_WAKEUP_TIME_MINUTES = 0

MIN_BEDTIME_HOUR = 6
MIN_BEDTIME_MINUTES = 0

MAX_BEDTIME_HOUR = 10
MAX_BEDTIME_HOUR = 0

INTERVAL_BW_MAX_AND_MIN = 16
# baby sleep limit requirements


baby_sleep_per_day = []

BABY_AGE_IN_MONTHS = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# includes the constant  values of
# [age_in_months, total_sleep, daytime_sleep, nighttime_sleep, daytime_naps_number, nighttime_naps_number]
BABY_SLEEP_REQ = [[3, 15, 8, 7, 4, 3],
                  [4, 14, 5, 9, 4, 3],
                  [5, 14, 5, 9, 3, 2],
                  [6, 13, 3, 10, 2, 1],
                  [7, 13, 3, 10, 2, 1],
                  [8, 13, 3, 10, 2, 1],
                  [9, 12, 2, 10, 2, 1],
                  [11, 12, 2, 10, 2, 1],
                  [12, 13, 2, 11, 2, 1],
                  [13, 13, 2, 11, 2, 1],
                  [14, 13, 2, 11, 2, 1],
                  [15, 13, 2, 11, 2, 1],
                  [16, 13, 2, 11, 2, 1],
                  [17, 13, 2, 11, 2, 1],
                  [18, 13, 2, 11, 2, 1],
                  [19, 13, 2, 11, 2, 1],
                  [20, 13, 2, 11, 2, 1],
                  [21, 13, 2, 11, 2, 1],
                  [22, 13, 2, 11, 2, 1],
                  [23, 13, 2, 11, 2, 1],
                  [24, 13, 2, 11, 2, 1]]


# function to get baby sleep requirements.

def get_baby_requirements(_baby_age):
    baby_sleep_req = []
    for req in BABY_SLEEP_REQ:
        sleep_req = {'baby_age': req[0], 'total_sleep': req[1], 'daytime_sleep': req[2], 'nighttime_sleep': req[3],
                     'daytime_naps_number': req[4], 'nighttime_naps_number': req[5]}
        baby_sleep_req.append(sleep_req)

    baby_requirements = {}  # need to change as initialization of day variables
    for n_index in baby_sleep_req:
        if n_index['baby_age'] == _baby_age:
            baby_requirements = {'baby_age': n_index['baby_age'],
                                 'total_sleep': n_index['total_sleep'],
                                 'daytime_sleep': n_index['daytime_sleep'],
                                 'nighttime_sleep': n_index['nighttime_sleep'],
                                 'daytime_naps_number': n_index['daytime_naps_number'],
                                 'nighttime_naps_number': n_index['nighttime_naps_number']}
            break
    return baby_requirements


TIMEZONE = ['GMT+5', 'GMT+2']

for index in BABY_SLEEP_REQ:
    baby_data_ = {}
    baby_data_['age_in_months'] = index[0]
    baby_data_['total_sleep'] = index[1]
    baby_data_['daytime_sleep'] = index[2]
    baby_data_['nighttime_sleep'] = index[3]
    baby_data_['daytime_naps_number'] = index[4]
    baby_data_['nighttime_naps_number'] = index[5]
    baby_sleep_per_day.append(baby_data_)

# ******** Build JSON for Constants
# fh = open("sleep_constants.json", "a+")
# fh.write(json.dumps(baby_sleep_per_day, indent=4, sort_keys=True))
# fh.close()
