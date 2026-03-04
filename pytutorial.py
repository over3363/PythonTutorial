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

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Global Keyword 
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword
# If you use the global keyword, the variable belongs to the global scope
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#----------------------DATA TYPES--------------------
# Built in Data Types 
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
# Getting Data Types
# You can get the data type of any object by using the type() function
# Print the data type of the variable x
x = 5
print(type(x))

# Setting Data Type 
# the data type is set when you assign a value to a variable:
x = 20
#display x:
print(x)
#display the data type of x:
print(type(x)) 

# Setting Specific Data Type 
# want to specify the data type, you can use constructor functions
x = int(20)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

#------------------PYTHON NUMBERS--------------------------------
"""
There are three numeric types in Python:
int
float
complex
"""
# Variables of numeric types are created when you assign a value to them
x = 1    # int
y = 2.8  # float
z = 1j   # complex
# To verify the type of any object in Python, use the type() function
print(type(x))
print(type(y))
print(type(z))

#INT
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

#FLOAT
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
#Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#COMPLEX 
# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#Type Conversion 
# can convert from one type to another with the int(), float(), and complex() methods
#  cannot convert complex numbers into another number type.
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#Random Numbers
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers
import random
print(random.randrange(1, 10))

#-----------------------TYPE CASTING----------------------------------
# There may be times when you want to specify a type on to a variable. This can be done with casting
# Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
# Casting in python is therefore done using constructor functions:
"""
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
#ints 
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#floats 
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#strings 
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#-------------------STRINGS--------------------------------------
