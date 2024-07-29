# Write a Python Program to Check Prime Number
"""
A prime number is a whole number that cannot be evenly divided by any other number
except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
cannot be divided by any other positive integer except for 1 and their own value.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

num = int(input("Enter the number:"))
print(is_prime(num))