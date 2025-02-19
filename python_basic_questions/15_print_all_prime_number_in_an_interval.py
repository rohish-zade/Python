"""
A prime number is a whole number that cannot be evenly divided by any other number
except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
cannot be divided by any other positive integer except for 1 and their own value.
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for num in range(a, b+1):
    # all prime number's are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i)==0:
                break
        else: # This block executes only if the loop completes without a break
            print(num)