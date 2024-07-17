# Write a Python program to solve quadratic equation.

"""
The standard form of a quadratic equation is:
    ax^2 + bx + c = 0
where
    a, b and c are real numbers and a ≠ 0

The solutions of this quadratic equation is given by
    x = [-b ± √(b^2 - 4ac)]/2a.

"""
import math

a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient a: "))
c = float(input("Enter the value of coefficient a: "))

#calculate the descriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b/(2*a)
    print(f"Root: {root}")
else:
    # complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_part} +  {imaginary_part}i")
    print(f"Root 2: {real_part} + {imaginary_part}i")






