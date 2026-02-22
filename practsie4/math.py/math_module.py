"""
The Math Module

Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:

"""
#import math

"""
When you have imported the math module, 
you can start using methods and constants of the module.

The math.sqrt() method for example, returns the square root of a number:

"""
import math

x = math.sqrt(64)

print(x)

"""
The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor()
method rounds a number downwards to its nearest integer, and returns the result:

"""
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#The math.pi constant, returns the value of PI (3.14...):
import math

x = math.pi

print(x)