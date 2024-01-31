# Write a Python Program to Check Leap Year.
# Check if the year variable is divisible by 400.
# Check if the year variable is divisible only by 4 and not 100.
# If theabove mentioned conditions are satisfied, 
# prints “Leap Year”, print “Not a Leap Year” otherwise.

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("{0} is a lear yaer".format(year))
else:
    print("{0} is a not lear yaer".format(year))