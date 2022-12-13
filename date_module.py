# There are 3 module for date
# 1- time
# 2- datetime
# 3- calender

import datetime;
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("date: %d-%m-%Y, time: %H:%M:%S"));

import time;
print(time.time());
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())


# Calender
import calendar;

cal = calendar.month(2001, 10);
print(cal)