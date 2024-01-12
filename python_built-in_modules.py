# Python program to import 'Python Built-in Modules' 

#importing built-in module math 
import math 

# Using square root('sqrt()') cantained in math module 
print(math.sqrt(529))

# Using pi ('pi()') function contained in math module 
print(math.pi)

# 2 radians = 114.59 degrees 
print(math.degrees(2))

# 60 degrees = 1.04 radians 
print(math.radians(60))

# sin of 2 radians 
print(math.sin(2))

# cos of 0.5 radians 
print(math.cos(0.5))

# tangent of 0.23 radians 
print(math.tan(0.23))

# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))


# importing built-in module random 
import random 

# printing random integer between 0 and 5 
print(random.randint(0,5))

# print random floating point number between 0 and 1 
print(random.random())

# random number between 0 and 100 
print(random.random()*100)

# creating a list as 'li'
li = [1, 4, True, 800, "Python", 23, "Hello"]

# using choice function in random module for choosing 
#a random element from a set such as a list 
print(random.choice(li))

# importing built-in module datetime 
import datetime
from datetime import date
import time

# Return the number of seconds since the Unix, Epoch, January 1st 1970.
print(time.time())

#Converts a number of seconds to a date object 
print(date.fromtimestamp(454554))