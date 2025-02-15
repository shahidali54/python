# operators in python
# An operator is a symbol that performs a certain operation between operands 

# Arithmetic Operators
print(5 + 4) # Addition

print(8 - 3) # Subtraction

print(4 * 2) # Multiplication

print(20 / 2) # Division

print(2 ** 3) # Exponentiation  2 * 2 = 4; 4 * 2 = 8

print(3 % 2)  # Modulus



# Relational/Comparison Operators

value1 = 11
value2 = 18

print(value1 == value2)  # False
print(value1 != value2)  # True
print(value1 >= value2)  # False
print(value1 <= value2)  # True
print(value1 < value2)  # True
print(value1 > value2)  # False


# Assignment Operators

a = 20
a += 6
print(a)

a -= 6
print(a)

a *= 2
print(a)

a /= 10
print(a)

a %= 10
print(a)

a **= 10
print(a)



# Logical Operators
# and operator

c = 10 
d = 20
print(c > d and d > c)  # False
print(c < d and d > c)  # True


# or operator

print(c > d or d < c)  # False
print(c < d or d < c)  # True


# not operator

e = 10
f = 20
print(not e < f)


# Type Conversion
# python auto conversion

x = 10        # integer
y = 20.22     # float
print(x + y)
print(type(x + y))  # 10.00 + 20.22


# manual conversion

g = int("10")      # str
h = 20        # integer
# print(g + h) # error

g = int("10")      # str
h = 20             # integer
print(g + h)



# input

z = input("Enter Your Name: ")
print (z)


val1 = input("Enter First Number: ")
val2 = input("Enter Second Number: ")
print(val1 + val2)
# Ans in str by default butt changend type in python manually

# Type Casting
val3 = int(input("Enter First Number: "))
val4 = int(input("Enter Second Number: "))
print(val3 + val4)