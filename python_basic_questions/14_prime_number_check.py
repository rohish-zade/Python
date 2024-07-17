# Write a Python Program to Check Prime Number
"""
A prime number is a whole number that cannot be evenly divided by any other number
except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
cannot be divided by any other positive integer except for 1 and their own value.
"""

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number")
    exit()

for i in range(2, num+1):
    


"""
When the system comes across the quit() function, it exits the Python program by closing the Python file itself. 
The quit() command also requires the site.py module to be imported. 
The SystemExit exception is raised by the quit() command in the background.
"""