# import module_1
import module_1 as m #we can give alias as well
import module_2 as m2
from module_1 import my_info # we can import specific variable for function as well

# import module3 as m3 # This wont help as its inside the mypackage folder so it wil throw import error
# from mypackages import module3, module4 
from mypackages import *


# print(module_1.get_sum(5, 9))
print(m.get_sum(5, 9))
print(m.get_product(5, 9))
print(m.my_info)
print(m.pi)


# accessing module 2
m2.say_hello("Rohish")
print(m2.get_remainder(23, 4))
print(m2.name, m2.profession)


# accesing functions and variables from mypackages folder
print(module3.function1())
print(module3.function2())
print(module4.function3())
print(module4.function4())


