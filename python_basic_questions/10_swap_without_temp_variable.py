# Write a Python program to swap two variables without temp variable.

variable1 = int(input("Enter the value of variable1: ")) # 5
variable2 = int(input("Enter the value of variable2: ")) # 4

print("Before Swapping")
print(f"variable 1: {variable1}, variable 2: {variable2}")

variable1 =  variable1 * variable2 # 5 * 4 = 20
variable2 = variable1 / variable2 # 20 / 4 = 5
variable1 = variable1 / variable2 # 20 / 5 = 4


# with addition
# variable1 = variable1 - variable2 #5 + 4 =  9
# variable2 = variable1 - variable2 # 9 - 4 = 5
# variable1 = variable1 - variable2

# simple solution in python
# variable1, variable2 = variable2, variable1

print("After Swapping")
print(f"variable 1: {variable1}, variable 2: {variable2}")