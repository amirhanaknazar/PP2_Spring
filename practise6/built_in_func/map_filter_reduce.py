#len(object, /)

#Return the length (the number of items) of an object. 
#The argument may be a sequence (such as a string, bytes, tuple, list, or range) or
#a collection (such as a dictionary, set, or frozen set).

a = 'asd'
print(len(a))

#sum(iterable, /, start=0)

#Sums start and the items of an iterable from left to right and returns the total. 
#The iterable’s items are normally numbers, 
#and the start value is not allowed to be a string.

ar = [1, 2, 3, 4]
print(sum(ar))

#min(iterable, /, *, key=None)
#min(iterable, /, *, default, key=None)
#min(arg1, arg2, /, *args, key=None)
#Return the smallest item in an iterable or the smallest of two or more arguments.

ar = [1, 2, 3, 4]
print(min(ar))

#max(iterable, /, *, key=None)
#max(iterable, /, *, default, key=None)
#max(arg1, arg2, /, *args, key=None)
#Return the largest item in an iterable or the largest of two or more arguments.

ar = [1, 2, 3, 4]
print(max(ar))

#map(function, iterable, /, *iterables, strict=False)

"""Return an iterator that applies function to every item of iterable, 
yielding the results. If additional iterables arguments are passed, 
function must take that many arguments and is applied to the items 
from all iterables in parallel. With multiple iterables, 
the iterator stops when the shortest iterable is exhausted. 
If strict is True and one of the iterables is exhausted before the others,
a ValueError is raised. For cases where the function inputs are already 
arranged into argument tuples,see itertools.starmap()."""

a, b = map(int, input().split())

numbers = [1, 2, 3]

result = map(lambda x: x*2, numbers)

print(list(result))

#filter(function, iterable, /)

'''Construct an iterator from those elements of iterable for which function is true. 
iterable may be either a sequence, a container which supports iteration, or an iterator. 
If function is None, the identity function is assumed, that is, all elements of iterable 
that are false are removed.'''

numbers = [1,2,3,4,5]

result = filter(lambda x: x%2==0, numbers)

print(list(result))

#reduce: gradually combines the list items into a single value.

#You need to import:

#from functools import reduce

from functools import reduce

numbers = [1,2,3,4]

result = reduce(lambda a,b: a+b, numbers)

print(result)

#sorted(iterable, /, *, key=None, reverse=False)
#Return a new sorted list from the items in iterable.

numbers = [5,1,3,2]

print(sorted(numbers))

#reverse

sorted(numbers, reverse=True)

#type conversion functions
"""
int()	to an integer
float()	to a fractional number
str()	to a string
list()	to the list
tuple()	into a tuple
set()	into a set

"""

x = "10"

a = int(x)
b = float(x)
c = str(25)

print(a, b, c)