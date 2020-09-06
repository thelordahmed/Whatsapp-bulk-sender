#################
# ALARM ALGORITHM
#################

import datetime
from time import sleep


current_time = datetime.datetime.today()
# this is the choosen time from interface
choosen_time = datetime.datetime(current_time.year, current_time.month, current_time.day, 3)
sleep_duration = choosen_time - current_time
# will check if there are negative days -> that means the choosen time is in the next day
# so we add those days on the choosen time then get total_seconds to wait
if sleep_duration.days < 0:
    choosen_time = choosen_time + datetime.timedelta(days=sleep_duration.days.__abs__())
    sleep_duration = choosen_time - current_time



print(sleep_duration.total_seconds())
print(sleep_duration)
