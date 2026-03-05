"""
Creating Date Objects

To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

"""
#Create a date object:
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), 
#but they are optional, and has a default value of 0, (None for timezone).
