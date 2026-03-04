#---------------LIBRARY IMPORTS-------------------------------------------
#---------------SYSTEM INFORMATION----------------------------------------
import sys
print(sys.version)

#------------COMMENTS------------------------------------------------------
# This is a Comment 

# Comments placed at end of line allow rest of the line to be ignored 
print("Hello, World!") #This is a comment

"""
This is a block comment
"""
#-------------OUTPUT-------------------------------------------------------
# print() to display output text or output values 
# Each call prints a new line by default 
# Text must be inside double or single quotes 
print("This will work!")
print('This will also work!')

# Bad Code: Error Forgetting quotes 
"""
print(This will cause an error)
"""

# printing on the same line without a newline 
# use the end parameter
print("Hello World!", end=" ")
print("I will print on the same line.")

# printing numbers 
# numbers don't get put inside quotes 
print(3)
print(358)
print(50000)

# can perform mathmatical operations inside print()
print(3 + 3)
print(2 * 5)

# can print a mix of text and numbers
print("I am", 35, "years old.")

#------------STATEMENT OPERATORS-----------------------------------------------
# py uses newlines to complete a command as opposed to other end of command operators ; ()
# Statements are executed one by one in the order they are written
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")

# Semicolons are optional and only used when writing multiple statements on one line 
print("Hello"); print("How are you?"); print("Bye bye!")

# Error Missing Semicolon between statements
"""
print("Python is fun!") print("Really!")
"""

# -----------INDENTATION-------------------------------------------------------
# Uses Indentation to Indicate a Block of Code (How Python Handles Scope for Loops, Functions, and Classes)
# Good Example of Indentation
# Number of Spaces is Up To Programmer : Need At Least 1 , Standard is 4
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

# Bad Example of Indentation Sytanx Error 
"""
if 5 > 2:
print("Five is greater than two!")
"""
# Bad Example of Indentation Error
# You Have To Use Same Number of Spaces In the Same Block of Code 
"""
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
"""

#----------------VARIABLES----------------------------------------
# Containers for storing data values
# Variables are created when you assign a value to it
# No Command for delcaring a variable 
x = 5
y = "Hello, World!"
x = 5
y = "John"
print(x)
print(y)

# Variables dont need to be declared with any particular type and can change type after they have been set
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# If you want to specify the variable type you can type cast it
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Getting data type of variable with type function 
x = 5
y = "John"
print(type(x))
print(type(y))

# String variables can be declared using single or double quotes 
x = "John"
# is the same as
x = 'John'

# Case Sensitive 
# Will Create two different variables 
a = 4
A = "Sally"
#A will not overwrite a

# Variable Names 
#A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# Variable Names are case sensitive 
"""
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Bad variable names
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

# Multiword variable names 
# Camel Case: Each word, except the first, starts with a capital letter:
myVariableName = "John"
# Pascal Case: Each word starts with a capital letter:
MyVariableName = "John"
# Snake Case: Each word is separated by an underscore character:
my_variable_name = "John"

#Assign Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
#number of variables must match number of values otherwise error 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Assign one value to multiple variables 
#can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpacking a collection 
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
# Unpacking a list 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables 
# print function is used to output variables
x = "Python is awesome"
print(x)

# output multiple variables, separated by a comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# can also use the + operator to output multiple variables
# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# Multi Variable Error
# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error
"""
x = 5
y = "John"
print(x + y)
"""
#best way to output multiple variables in the print() function is to separate them with commas, which even support different data types
x = 5
y = "John"
print(x, y)

# Global Variables 
# Variables that are created outside of a function: can be used by everyone, both inside of functions and outside.
# Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

