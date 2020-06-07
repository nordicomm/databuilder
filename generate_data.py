import constants
import datetime

import sleep_identifiers

# what are data sequences
# 0. Normal, as per baby guidelines
# 1. creating sleep quality issues, and testing the user data with it
# 2. creating nighttime sleep duration issues
# 3. fluctuating number of time awake
# 4. fluctuating the actual time baby was awake during the night.
# 5. bedtime issues, and seeing how parents see need of Push Sleep
# 6. Changing the going to bedtime, adding fluctuations in it.
# 7. fluctuating the daytime sleep duration
# 8. changing the number of naps per day, and their duration
# 9. Changing the morning wakeup time, and seeing the effect
# 10. building a scenario where Push Sleep show results
# 11. building a scenario where Easy Dream show results
# 12. Push Sleep not working
# 13. Easy Dream not working

data_sequence = 0;
baby_age = 6

def generate_normal_sequence_6months():


    startDate = day_obj.get_date()

    print(startDate)
    #wakeup_time = start_time = datetime.time(6, 15)
    #pointer = datetime.datetime.combine(startDate, start_time)

    # moving time two hours
    #pointer = pointer + datetime.timedelta(hours=2)

    # start time pointer of the nap
    #start_time = pointer
    # endtime pointer of the nap
    #pointer = pointer + datetime.timedelta(hours=1)
    #nap_time.append([start_time, pointer])

    # recording first feeding time
    #feed_time = [pointer]

    # moving time two hour plus
    # pointer = pointer + datetime.timedelta(hours=2)

    # recording second nap of the day, for one hour
    # start time pointer of the nap
    # start_time = pointer
    # endtime pointer of the nap
    #pointer = pointer + datetime.timedelta(hours=1)
    #nap_time.append([start_time, pointer])

    # recording second feeding time
    #feed_time.append(pointer)

    # moving time two hour plus
    #pointer = pointer + datetime.timedelta(hours=1)

    # recording third nap of the day, for one hour
    # start time pointer of the nap
    #start_time = pointer
    # endtime pointer of the nap
    #pointer = pointer + datetime.timedelta(hours=1)
    #nap_time.append([start_time, pointer])

    # recording third feeding time
    #feed_time.append(pointer)

    # moving time two hour and 15 minutes
    #pointer = pointer + datetime.timedelta(hours=2, minutes=15)

    #bath_time = pointer

    # moving time 30 minutes
    #pointer = pointer + datetime.timedelta(minutes=30)

    #feed_time.append(pointer)

    # moving time 30 minutes
   # pointer = pointer + datetime.timedelta(minutes=30)

    #go_to_bedtime = pointer


def generate_data(day_obj):

    generate_normal_sequence_6months(day_obj[0])

    #for index in range(constants.NUMBER_OF_DAYS_DATA):
        #generate_day_data(day_obj[0], data_sequence, baby_age)
        #generate_night_data(day_obj[0], data_sequence)
