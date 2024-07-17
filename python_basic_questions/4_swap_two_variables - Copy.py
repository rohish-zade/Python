# Write a Python program to swap two variables
variable_1 = int(input("Enter the value of first variable: "))
variable_2 = int(input("Enter the value of second variable: "))

print(f"Before swapping:\n variable_1: {variable_1}\n variable_2: {variable_2}")

temp = variable_1
variable_1 = variable_2
variable_2 = temp

print(f"After swapping:\n variable_1: {variable_1}\n variable_2: {variable_2}")
