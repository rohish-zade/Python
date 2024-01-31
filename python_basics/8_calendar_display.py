# Write a Python program to display calendar
# calendar module in python: https://docs.python.org/3/library/calendar.html, https://www.geeksforgeeks.org/python-calendar-module/

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

cal = calendar.month(year, month)

print(cal)
