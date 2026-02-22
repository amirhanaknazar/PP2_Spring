"""
Generator Expressions
Similar to list comprehensions, you can create generators using 
generator expressions with parentheses instead of square brackets:

"""

#List comprehension vs generator expression:
# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

#Using a generator expression with sum:
# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

"""
Fibonacci Sequence Generator

Generators can be used to create the Fibonacci sequence.

It can continue generating values indefinitely, without running out of memory:

"""

#Generate 100 Fibonacci numbers:
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

"""
Generators have special methods for advanced control:

send() Method

The send() method allows you to send a value to the generator:

"""
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

#The close() method stops the generator:
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()