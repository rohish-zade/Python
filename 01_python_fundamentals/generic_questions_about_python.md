### 1. What is the maximum possible value of an integer in Python ?
- In Python, value of an integer is not restricted by the number of bits and can expand to the limit of the available memory (Sources : [this](https://docs.python.org/2/library/stdtypes.html) and [this](http://cs.utexas.edu/~mitra/csSpring2016/cs313/lectures/math.html)). 
- Thus we never need any special arrangement for storing large numbers (Imagine doing above arithmetic in C/C++).
- As a side note, in Python 3, there is only one type "int" for all type of integers. In Python 2.7. there are two separate types "int" (which is 32 bit) and "long int" that is same as "int" of Python 3.x, i.e., can store arbitrarily large numbers.

### 2. Difference between == and is operator in Python
- The Equality operator (==) is a comparison operator in Python that compare values of both the operands and checks for value equality. Whereas the 'is' operator is the  identity operator that checks whether both the operands refer to the same object or not (present in the same memory location).

### 3. `__name__` (A Special variable) in Python
- Since there is no main() function in Python, when the command to run a python program is given to the interpreter, the code that is at level 0 indentation is to be executed. However, before doing that, it will define a few special variables. __name__ is one such special variable. 
- If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name. __name__ is a built-in variable which evaluates to the name of the current module. 
- Thus it can be used to check whether the current script is being run on its own or being imported somewhere else by combining it with if statement, as shown below.

  ```python
  # File1.py 
  
  print ("File1 __name__ = %s" %__name__) 
  
  if __name__ == "__main__": 
      print ("File1 is being run directly")
  else: 
      print ("File1 is being imported")
  
  # Output:
    # `File1 __name__ = __main__`
    # `File1 is being run directly
  ```
