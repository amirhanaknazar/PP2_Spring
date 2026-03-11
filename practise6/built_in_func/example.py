#BUILT-IN FUNCTIONS
#map_filter_reduce.py

from functools import reduce

numbers = [1,2,3,4,5]

# map
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even:", even)

# reduce
total = reduce(lambda a,b: a+b, numbers)
print("Sum:", total)

#enumerate_zip_examples.py
names = ["Ali", "John", "Sara"]
scores = [85, 90, 95]

# enumerate
for index, name in enumerate(names):
    print(index, name)

# zip
for name, score in zip(names, scores):
    print(name, score)

# type checking
x = 10
print(type(x))

# type conversion
a = "25"
b = int(a)

print(b, type(b))