import json
import datetime

start_hr = 6
end_min = 15
time_pointer = datetime.time(wakeup_time_hr, wakeup_time_min)

wakeup_time = time_pointer
#moving a time an hour plus
time_pointer = time_pointer + datetime.timedelta(hours=1)

#recording first nap of the day, for one hour
nap_time = [time_pointer, time_pointer + datetime.timedelta(hours=1)]

#moving time pointer to one hour plus
time_pointer = time_pointer + datetime.timedelta(hours=1)

#recording first feeding time
feed_time = time_pointer

#moving time two hour plus
time_pointer = time_pointer + datetime.timedelta(hours=2)

#recording second nap of the day, for one hour
nap_time.append( time_pointer, time_pointer + datetime.timedelta(hours=1))

#recording second feeding time
feed_time.append(time_pointer)

#moving time two hour plus
time_pointer = time_pointer + datetime.timedelta(hours=2)

#recording second nap of the day, for one hour
nap_time.append( time_pointer, time_pointer + datetime.timedelta(hours=1))

#recording third feeding time
feed_time.append(time_pointer)

#moving time two hour and 15 minutes
time_pointer = time_pointer + datetime.timedelta(hours=2) + datetime.timedelta(minutes=15)

bath_time = time_pointer

#moving time 30 minutes
time_pointer = time_pointer + datetime.timedelta(minutes=30)

feed_time.append(time_pointer)

#moving time 30 minutes
time_pointer = time_pointer + datetime.timedelta(minutes=30)

go_to_bedtime = time_pointer

fh = open("baby_6months.json", "a+")
fh.write(json.dumps({"prime": prime_numbers, "not_prime": not_prime}))
fh.close()