# Module Dates is very important for every type of application
# date, time, datetime, timezones, timedelta

# main module working with dates is datetime
# difference between naive vs. aware times
# naive date/time give us simple result, does not have details (easy to use)
# aware date/time give us the date with details like timezone/daylight (hard to use)

import datetime

# Dealing with date

# Set Regular Date
d = datetime.date(2021, 10, 16);
print(d);

# Print Current Date
tday = datetime.date.today();
print(tday);

# specific info
print(tday.year)
print(tday.month)
print(tday.day)

# 

print(tday.weekday())
print(tday.isoweekday())

# difference between them only first >  monday start with 0 ... 6
# and second > monday start with 1 ... 7

# TimeDelta
# is more useful when we want do operation on our dates/times

tdelta = datetime.timedelta(days=7, weeks=1); # 7 + 1(7days) = 2 weeks
print(tdelta)

print(tday + tdelta)
# what it did?
# it does operation on dates
# we add 7 days on today and give us result
# today after two weeks

# date = date1 + timedelta
# _timedelta = date1 + date2
# when we do operation on dates, the result is "timedelta"

date1 = datetime.date(2000, 10, 10)
date2 = datetime.date(2000, 11, 10)
# result = date1 + date2; # cannot do plus operation
# print(result)


# calculate birthday
currnt_date = datetime.date.today();
birth_date = datetime.date(2023, 10, 16); # next birthday celebrate

delta_time = birth_date - currnt_date;
print(delta_time)


# dealing with time
t = datetime.time(10, 30, 9);
# by default it is not give us timezone, then it is naive
# but we can get timezone by tzinfo property
print(t)
print(t.tzinfo)


# we can use most common uses (datetime.datetime())

full_date = datetime.datetime(2021, 10,16, 12, 20,9);
print(full_date)
print(full_date.date())
print(full_date.year)
print(full_date.date().year)
print(full_date.time())

# 
print("################################")
print(full_date)
fdelta = datetime.timedelta(days=5, hours=10);

result = fdelta + full_date;
print(result)

# compare

date_today = datetime.datetime.today()
# give us current local date time with time zone of none

date_now = datetime.datetime.now()
# if you didn't specify timezone in .now() method
# it would work exactly same .today()
###################################################
# utcnow > aware date > give us UTC time, tz is none
date_utcnow = datetime.datetime.utcnow()

print(date_today)
print(date_now)
print(date_utcnow)

import pytz;

# when you work with "pytz" module, it is recommended to use UTC
# create aware time zone using UTC

date1_time = datetime.datetime(2002, 10, 16, 10, 30, 2, tzinfo=pytz.UTC);
date2_time = datetime.datetime.now(tz=pytz.UTC); # (Recommended)
date3_time = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC);

print(date1_time)
print(date2_time)
print(date3_time)

# Local UTC

date4_time = datetime.datetime.now(tz=pytz.UTC);
date4_time = date4_time.astimezone(pytz.timezone("Egypt"))
print(date4_time)

# print(pytz.all_timezones);
# for tz in pytz.all_timezones:
#      print(tz)

# [](https://youtu.be/eirjjyP2qcQ?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&t=1295)

# WATCH OUT
# datetime.datetime.now() is a naive date, then cannot applied on it pytz timezone
# solution is : datetime.datetime.now(tz=pytz.UTC);
# solution2 is : using <timezone>.localize(<datetime>)

# format1 = date1_time.isoformat()
format1 = date1_time.strftime("%B %d, %Y");
print(format1)
opposit_format1 = datetime.datetime.strptime(format1, "%B %d, %Y")
# second parameter tells python what format you used to make this format1
print(opposit_format1)


# Arrow Package is easy to use for dealing with dates