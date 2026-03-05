"""
Generators

Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

The code inside the function is not executed yet, it is only compiled. 
The function only executes when you iterate over the generator.

"""

#A simple generator function:
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

"""
The yield Keyword

The yield keyword is what makes a function a generator.

When yield is encountered, the function's state is saved,
and the value is returned. The next time the generator is called, 
it continues from where it left off.

"""

#Generator that yields numbers:
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)


