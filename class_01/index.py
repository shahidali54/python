# First program
print("Hello, World!")
print("My name is Shahid Ali,","And I am 25 years old")

# Variables, A variable is a name given to a memory location in a program.
name = "Shahid Ali"         
age = 25    
print("My name is", name)
print("I am", age, "years old")  

# Data Types, string, integer, float, boolean, None, list, tuple, dictionary, set

my_name = "Shahid Ali"                                        # String Data Type
my_age = 25                                                   # Integer Data Type
height = 175.5                                                # Float Data Type
is_student = True                                             # Boolean Data Type
a = None                                                      # None type Data Type
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                           # List Data Type
c = {"name": "Shahid Ali", "age": 25, "is_student": True}     # Dictionary Data Type
d = frozenset([1, 2, 3, 4, 5])                                # Frozenset Data Type
e = (1, 2, 3, 4, 5)                                           # Tuple Data Type

print(type(my_name), type(my_age), type(height), type(is_student), type(a), type(b), type(c), type(d), type(e))                                        

# Comments
# This is a single line comment

"""
This is a
multi-line
comment
"""

# Keywords, Python's keywords are the reserved words that cannot be used as variable names,
# function names, or any other identifier.

import keyword
print(keyword.kwlist)
"""
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif,
else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, 
pass, raise, return, try, while, with, yield

"""
# Operators
"""
An operator is a symbol that performs a certain operation between operands.
Types of operators:

1. Arithmetic Operators:  (+, -, *, /, %, **)
2. Assignment Operators:  (=, +=, -=, *=, /=, %=, **=)
3. Comparison Operators:  (==, !=, >, <, >=, <=)
4. Logical Operators:     (and, or, not)

"""

# Arithmetic Operators
x = 5
y = 2
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

# Assignment Operators
num = 10
num += 5

num1 = 15
num1 -= 5

num2 = 20
num2 *= 5

num3 = 20
num3 /= 5

num4 = 20
num4 %= 5

num5 = 20
num5 **= 5
print("num:", num)
print("num1 -= :", num1)
print("num2 *= :", num2)
print("num3 /= :", num3)
print("num4 %= :", num4)
print("num5 **= :", num5)

# Relationa/Comparison Operators
p = 10
q = 5
print("p == q:", p == q)   # False
print("p!= q:", p!= q)     # True
print("p >= q:", p >= q)   # True
print("p > q:", p > q)     # True
print("p <= q:", p <= q)   # False
print("p < q:", p < q)     # False


# Logical Operators
# not Operator
print(not True)   # False
print(not False)  # True

# and Operator
value1 = True
value2 = True
print("value1 and value2:", value1 and value2)  # True

# or Operator

value3 = True
value4 = False
print("value3 or value4:", value3 or value4)  # True

# Nested Logical Operators
value5 = True
value6 = False
value7 = True
print("value5 and value6 or value7:", (value5 and value6) or value7)  # True


# Type Conversion and Type Casting
# Type Conversion
val1 = 10
val2 = 22.55
sum = val1 + val2
print("Sum:", sum) # 10.0 + 22.55 = 32.55, which is of float type, so it is automatically converted


# Type Casting
# Convert string to float
val3 = int("5")
val4 = 22.55
print(type(val3))
print("Sum:",(val3) + val4)

# Convert float to string
val5 = 10.55
val5 = str(val5)
print(type(val5))


# input in Python, input() statement is used to get user input, result for input() is always a string
name1 = input("Enter your name: ")
print("Hello", name1)

# User Input as Integer
val6 = int(input("Enter any value: "))
print(type(val6), "Value:", val6)

# User Input as Float
val7 = float(input("Enter any value: "))
print(type(val7), "Value:", val7)

# User Input as str, int, and float are all valid inputs for input() function
Name = str(input("Enter your name: "))
Age = int(input("Enter your age: "))
Marks = float(input("Enter your marks: "))
print("Name:", Name)
print("Age:", Age)
print("Marks:", Marks)


