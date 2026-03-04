# Resources & References : https://www.w3schools.com/python

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

#------------STATEMENTS-----------------------------------------------
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
# Strings in python are surrounded by either single quotation marks, or double quotation marks. 'hello' is the same as "hello".
# You can display a string literal with the print() function:
print("Hello")
print('Hello')

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

#You can assign a multiline string to a variable by using three quotes:
a = """hello,
my name is ,
tori
over3363."""
print(a)
# or single quotes
a = '''i love,
this class,
cyb2200
and coding.'''
print(a)

# Strings as Arrays 
# strings in Python are arrays of unicode characters.
# Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

# Looping through strings 
#Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# String Length 
# To get the length of a string, use the len() function
a = "Hello, World!"
print(len(a))

# Check String 
# check if a certain phrase or character is present in a string, we can use the keyword in
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if Not present in string 
# check if a certain phrase or character is NOT present in a string, we can use the keyword not in
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)
#print only if "expensive" is NOT present
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slicing Strings
# can return a range of characters by using the slice syntax
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])

# slicing from start 
# By leaving out the start index, the range will start at the first character
# Get the characters from the start to position 5 (not included)
b = "Hello, World!"
print(b[:5])

# slice to the end 
# By leaving out the end index, the range will go to the end
# Get the characters from position 2, and all the way to the end
b = "Hello, World!"
print(b[2:])

# Negative Indexing 
# Use negative indexes to start the slice from the end of the string
"""
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2)
"""
b = "Hello, World!"
print(b[-5:-2])

# Modifying Strings
# Python has a set of built-in methods that you can use on strings

# UpperCase
#The upper() method returns the string in upper case
a = "Hello, World!"
print(a.upper())

# LowerCase
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# Remove Whitespace 
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space
# The strip() method removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replacing Strings
# The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

# Split Strings
# The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation 
# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c
a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " "
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Formatting 
# cannot combine strings and numbers like this
# Error 
"""
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
"""

# Fstrings 
#can combine strings and numbers by using f-strings or the format() method
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
# Create an f-string
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
# placeholder can contain variables, operations, functions, and modifiers to format the value
# Add a placeholder for the price variable
price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can include a modifier to format the value
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
# Display the price with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# placeholder can contain Python code, like math operations
# Perform a math operation in the placeholder, and return the result
txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape Characters
# To insert characters that are illegal in a string, use an escape character
# An escape character is a backslash \ followed by the character you want to insert

# example of an illegal character is a double quote inside a string that is surrounded by double quotes
# You will get an error if you use double quotes inside a string that is surrounded by double quotes
"""
txt = "We are the so-called "Vikings" from the north."
"""

# The escape character allows you to use double quotes when you normally would not be allowed
txt = "We are the so-called \"Vikings\" from the north."

# Escape Characters 
#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value

# single quote 
txt = 'It\'s alright.'
print(txt) 
# backslash
txt = "This will insert one \\ (backslash)."
print(txt) 
# newline 
txt = "Hello\nWorld!"
print(txt) 
# Carriage Return
txt = "Hello\rWorld!"
print(txt) 
# Tab
txt = "Hello\tWorld!"
print(txt) 
# Backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
# Octal Value 
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 
#Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# String Methods 
# All string methods return new values. They do not change the original string
"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

#----------------BOOLEANS---------------------------------
# Booleans represent one of two values: True or False
# You can evaluate any expression in Python, and get one of two answers, True or False
# When you compare two values, the expression is evaluated and Python returns the Boolean answer
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, Python returns True or False
# Print a message based on whether the condition is True or False
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables 
# The bool() function allows you to evaluate any value, and give you True or False in return
# Evaluate a string and a number
print(bool("Hello"))
print(bool(15))

# Evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False
# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions Returning Boolean Values 
# can create functions that returns a Boolean Value
# Print the answer of a function
def myFunction() :
  return True

print(myFunction())

# You can execute code based on the Boolean answer of a function
# Print "YES!" if the function returns True, otherwise print "NO!"
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type
# Check if an object is an integer or not
x = 200
print(isinstance(x, int))

#---------------------OPERATORS--------------------------------------------
# Operators are used to perform operations on variables and values
# use the + operator to add together two values
print(10 + 5)

# Although the + operator is often used to add together two values, like in the example above, it can also be used to add together a variable and a value, or two variables
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

# Artithmatic Operators 
"""
Operator	Name	Example	
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	
"""
x = 5
y = 3
print(x + y)
x = 5
y = 3
print(x - y)
x = 5
y = 3
print(x * y)
x = 12
y = 3
print(x / y)
x = 5
y = 2
print(x % y)
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2
x = 15
y = 2
print(x // y)
#the floor division // rounds the result down to the nearest whole 

x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Divsion 
"""
Python has two division operators:
/ - Division (returns a float)
// - Floor division (returns an integer)
"""
#Division always returns a float:
x = 12
y = 5
print(x / y)
# Floor division always returns an integer.
#It rounds DOWN to the nearest integer
x = 12
y = 5
print(x // y)

# Assignment Operators 
# Assignment operators are used to assign values to variables
"""
Operator	Example	Same As
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)
"""
x = 5
print(x)
x = 5
x += 3
print(x)
x = 5
x += 3
print(x)
x = 5
x *= 3
print(x)
x = 5
x /= 3
print(x)
x = 5
x%=3
print(x)
x = 5
x//=3
print(x)
x = 5
x **= 3
print(x)
x = 5
x &= 3
print(x)
x = 5
x |= 3
print(x)
x = 5
x ^= 3
print(x)
x = 5
x >>= 3
print(x)
x = 5
x <<= 3
print(x)
print(x := 3)

# Walrus Operator 
#Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression
#The count variable is assigned in the if statement, and given the value 5
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Comparison Operator 
#Comparison operators are used to compare two values
# Comparison operators return True or False based on the comparison
"""
Operator	Name	Example	
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""
x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3
x = 5
y = 3
print(x != y)
# returns True because 5 is not equal to 3
x = 5
y = 3
print(x > y)
# returns True because 5 is greater than 3
x = 5
y = 3
print(x < y)
# returns False because 5 is not less than 3
x = 5
y = 3
print(x >= y)
# returns True because five is greater, or equal, to 3
x = 5
y = 3
print(x <= y)
# returns False because 5 is neither less than or equal to 3
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Chaining Comparison Operators 
#Python allows you to chain comparison operators
x = 5
print(1 < x < 10)
print(1 < x and x < 10)

# Logical Operators 
# Logical operators are used to combine conditional statements
"""
Operator	Description	Example	
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10
x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

# Test if a number is greater than 0 and less than 10
x = 5
print(x > 0 and x < 10)
#Test if a number is less than 5 or greater than 10
x = 5
print(x < 5 or x > 10)
#Reverse the result with not:
x = 5
print(not(x > 3 and x < 10))

#Identity Operators 
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
"""
Operator	Description	Example	
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# The is operator returns True if both variables point to the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

# The is not operator returns True if both variables do not point to the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)

# Difference between is and ==
"""
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
"""
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# Python Membership Operators 
