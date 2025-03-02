# Conditional Statements, if-elif-else (SYNTAX)

light = "green"

if light == "green":
    print("Go")

elif light == "yellow":
    print("Slow Down")

elif light == "red":
    print("Stop")

elif light == "flashing":
    print("Proceed with caution")

else:
    print("Invalid light color")


Age = 17

if Age >= 18:
    print("You are an adult")

else:
    print("Invalid age")


marks = int(input("Enter Your Marks To Check Your Result: "))

if(marks >= 90 and marks < 100):
    print("Grade A")

elif(marks >= 80 and marks < 89):
    print("Grade B")

elif(marks >= 70 and marks < 79):
    print("Grade C")

elif(marks >= 60 and marks < 69):
    print("Grade D")

elif(marks >= 50 and marks < 59):
    print("Grade E")

else:
    print("Sorry, you have failed")

    
# Nested if-else (SYNTAX)
# Nesting multiple if-else statements inside another if-else statement
age = 35

if age >= 18:
    if age >= 80:
        print("Can not drive")

    else:
        print("Can drive")

else:
    print("Can not drive")     


# ODD or Even (SYNTAX)
# Check if a number is odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")

else:
    print("Odd number")   


# To find the greatest of three numbers entered by the user (SYNTAX)
# Find the largest number among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))  
c = int(input("Enter third number: "))

if(a >= b and a >= c):
    print(a, "is the largest number")

elif(b >= c):
    print(b, "is the largest number")

else:
    print(c, "is the largest number")


# To check if a number is a multiple of 7 (SYNTAX)
x = int(input("Enter a number: "))

if(x % 7 == 0):
    print("multiple of 7")

else:
    print("Not a multiple of")