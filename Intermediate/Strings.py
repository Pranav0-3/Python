# Strings
#**************************************************************************************************************************



#*******************************************________STRINGS________*****************************************************



# Strings
# A string is a sequence of characters. 
# String literals in Python are enclosed by either double or single quotes.

# my_string = 'Hello'

# Python strings are immutable which means they cannot be changed after they are created.

# Creation
# use singe or double quotes
my_string = 'Hello'
my_string = "Hello"
my_string = "I' m  a 'Geek'"

# escaping backslash
my_string = 'I\' m  a "Geek"'
my_string = 'I\' m a \'Geek\''
print(my_string)

# triple quotes for multiline strings
my_string = """Hello
World"""
print(my_string)

# backslash if you want to continue in the next line
my_string = "Hello \
World"
print(my_string)


# I' m a 'Geek'
# Hello
# World
# Hello World


# Access characters and substrings
my_string = "Hello World"

# get character by referring to index
b = my_string[0]
print(b)

# Substrings with slicing
b = my_string[1:3] # Note that the last index is not included
print(b)
b = my_string[:5] # from beginning
print(b)
b = my_string[6:] # until the end
print(b)
b = my_string[::2] # start to end with every second item
print(b)
b = my_string[::-1] # reverse the string with a negative step:
print(b)

# H
# el
# Hello
# World
# HloWrd
# dlroW olleH






# Concatenate two or more strings
# concat strings with +

greeting = "Hello"
name = "Tom"
sentence = greeting + ' ' + name
print(sentence)

# Hello Tom






# Iterating
# Iterating over a string by using a for in loop
my_string = 'Hello'
for i in my_string:
    print(i)
# H
# e
# l
# l
# o








# Check if a character or substring exists

if "e" in "Hello":
    print("yes")
if "llo" in "Hello":
    print("yes")

# yes
# yes







# Useful methods
my_string = "     Hello World "

# remove white space
my_string = my_string.strip()
print(my_string)

# number of characters
print(len(my_string))

# Upper and lower cases
print(my_string.upper())
print(my_string.lower())

# startswith and endswith
print("hello".startswith("he"))
print("hello".endswith("llo"))

# find first index of a given substring, -1 otherwise
print("Hello".find("o"))

# count number of characters/substrings
print("Hello".count("e"))

# replace a substring with another string (only if the substring is found)
# Note: The original string stays the same
message = "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)

# split the string into a list
my_string = "how are you doing"
a = my_string.split() # default argument is " "
print(a)
my_string = "one,two,three"
a = my_string.split(",")
print(a)

# join elements of a list into a string
my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print(a)


# Hello World
# 11
# HELLO WORLD
# hello world
# ['how', 'are', 'you', 'doing']
# ['one', 'two', 'three']
# True
# True
# 4
# 1
# Hello Universe
# How are you doing









# Format
# New style is with .format() and old style is with % operator.

# use braces as placeholders
a = "Hello {0} and {1}".format("Bob", "Tom")
print(a)

# the positions are optional for the default order
a = "Hello {} and {}".format("Bob", "Tom")
print(a)

a = "The integer value is {}".format(2)
print(a)

# some special format rules for numbers
a = "The float value is {0:.3f}".format(2.1234)
print(a)
a = "The float value is {0:e}".format(2.1234)
print(a)
a = "The binary value is {0:b}".format(2)
print(a)

# old style formatting by using % operator
print("Hello %s and %s" % ("Bob", "Tom")) # must be a tuple for multiple arguments
val =  3.14159265359
print("The decimal value is %d" % val)
print("The float value is %f" % val)
print("The float value is %.2f" % val)


# Hello Bob and Tom
# Hello Bob and Tom
# The integer value is 2
# The float value is 2.123
# The float value is 2.123400e+00
# The binary value is 10
# Hello Bob and Tom
# The decimal value is 10
# The float value is 10.123450
# The float value is 10.12








# f-Strings
# New since Python 3.6. Use the variables directly inside the braces.

name = "Eric"
age = 25
a = f"Hello, {name}. You are {age}."
print(a)
pi = 3.14159
a = f"Pi is {pi:.3f}"
print(a)
# f-Strings are evaluated at runtime, which allows expressions
a = f"The value is {2*60}"
print(a)


# Hello, Eric. You are 25.
# Pi is 3.142
# The value is 120
# More on immutability and concatenation


# since a string is immutable, adding strings with +,  or += always 
# creates a new string, and therefore is expensive for multiple operations
# --> join method is much faster

from timeit import default_timer as timer
my_list = ["a"] * 1000000

# bad
start = timer()
a = ""
for i in my_list:
    a += i
end = timer()
print("concatenate string with + : %.5f" % (end - start))

# good
start = timer()
a = "".join(my_list)
end = timer()
print("concatenate string with join(): %.5f" % (end - start))


# concat string with + : 0.34527
# concat string with join(): 0.01191