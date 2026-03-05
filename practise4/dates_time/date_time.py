"""
Python Dates

A date in Python is not a data type of its own, 
but we can import a module named datetime to work with dates as date objects.

"""
#Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()
print(x)

"""
Date Output

When we execute the code from the example above the result will be:

2026-02-22 15:02:39.885158
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:

"""

#Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))