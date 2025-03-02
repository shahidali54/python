# Strings and Conditional Statements
# String is Data Type that stores sequence of characters

single_quote_string = 'This is a single quoted string'
double_quote_string = "This is a double quoted string"
triple_quote_string = '''This is a triple quoted string'''

# its generally due to the fact. for example, we use apostrophe in a string

# python will throw an error if we use single quote in a single quoted string
#'this is a string's with an apostrophe'

# Valid String with apostrophe
"this is a string's with an apostrophe"

# escap sequences character, tab, new line, backslash
# line breaks in string
line_breaks = "This is a string. \nwith line breaks"
print(line_breaks)


# Basic String Operations (Concatenation, lenth, indexing, slicing)

# Adding two strings together using + operator, it will concatenate them.
string1 = "Hello"
string2 = "World"
string3 = string1 + " " + string2
print(string3)


# Length
print(len(string3))


# Indexing (Accessing individual characters in a string), index starts from 0

# Indexing of characters in a string starts from 0.

# Index helping to access characters.

# H e l l o _ W o r l d
# 0 1 2 3 4 5 6 7 8 9 10

indexing = "Hello_World"
print(indexing[0]) # output: H
print(indexing[1]) # output: e
print(indexing[2]) # output: l
print(indexing[3]) # output: l
print(indexing[4]) # output: o


# Slicing (Accessing part of a string)
slicing = "Hello_World"
print(slicing[1:4])               # output: ell
print(slicing[6:12])              # output: World
print(slicing[6:len(slicing)])    # output: World
print(slicing[6:])                # output: World
print(slicing[:5])                # output: Hello

# negative indexing
print(slicing[-4: -1])   # output: orl
print(slicing[-11:5])    # output: Hello
print(slicing[-5:])      # output: World



# String Functions (endswith(), capitalize(), replace(), find(), count().)

# The endswith() method returns True if string ends with substring, otherwise False.

# endswith() function
substring = "i am studying python from GIAIC"
print(substring.endswith("AIC"))     # output: True
print(substring.endswith("py"))      # output: False

# Capitalize function capitalizes the first letter of the string.
# Capitalize()
capitalize = "python"
# original string remains unchanged
print(capitalize.capitalize())  # output: Python
# orignal string modified
capitalize = capitalize.capitalize()
print(capitalize)               # output: Python


# replace() function, replaces all occurrences of old

# replace() function
replace = "I am studying python from GIAIC"
print(replace.replace("python", "Java"))  # output: I am studying java from GIAIC
print(replace)                            # output: I am studying python from GIAIC


# find() function, returns the 1st index of the first occurrence

# find() function
find_function = "I am studying python from GIAIC"
print(find_function.find("st")) # output: 5
print(find_function.find("python")) # output: 14


# count() function, returns the number of occurrences
# count() function
count_function = "I am studying python from GIAIC"
print(count_function.count("y")) # output: 1
print(count_function.count("a")) # output: 1

