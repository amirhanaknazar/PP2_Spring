"""
Generators Saves Memory

Generators are memory-efficient because they generate values on-the-fly instead of 
storing everything in memory.

For large datasets, generators save memory:

"""

#Generator for large sequences:
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

#You can manually iterate through a generator using the next() function:
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#When there are no more values to yield, the generator raises a StopIteration exception:
def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) # This will raise StopIteration