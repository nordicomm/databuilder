# databuilder
This project will help us to build the baby schedule, to help us test the server side application.

It is designed also to test data visualization part of the project. 

*Pre-req to run the code*
- install the names project to generate the names https://pypi.org/project/names/#modal-close
 


## Part 1: Building a Jason for Expected Baby Schedule. 
On "Nanit" and other related websites we could fetch the data of the baby. 

Link:  https://www.nanit.com/blog/baby-sleep-schedule/3-month-baby-sleep-schedule/

First, we need to compile the JSON for being usable by our database. 

The data elements in each row should be: 
- baby_name (baby name is generated through random names generateor at https://pypi.org/project/names/#modal-close
 )
- baby_gender (we can use the same "names" library to create baby gender as well.)
- on_bed_start_time (datetime variable)
- on_bed_end_time (datetime variable)
- sleep_time (difference between end time and start time in hour and minutes, datetime.time variable)
- bed_time (ention whether the sleep time needs to include bedtime or not, more explanation later)
- is_night_sleep (flag to mark the nap as night time sleep)
- timezone (GMT+3 format, and can be used by tzinfo variable in datetime data type)



