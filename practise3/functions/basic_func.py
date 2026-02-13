#In Python, a function is defined using the def keyword, followed by a function name and parentheses:

def my_function():
  print("Hello from a function")

#This creates a function named my_function that prints "Hello from a function" when called.

#To call a function, write its name followed by parentheses:

def my_function():
  print("Hello from a function")

my_function()


'''
Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)
'''
#Valid func names:
#calculate_sum()
#_private_function()
#myFunction2()

"""
Why Use Functions?
Imagine you need to convert temperatures from Fahrenheit to Celsius several 
times in your program. Without functions, you would have to write the same 
calculation code repeatedly:

"""

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))