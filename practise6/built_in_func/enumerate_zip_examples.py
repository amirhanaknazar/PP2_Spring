#enumerate(iterable, start=0)

"""Return an enumerate object. iterable must be a sequence,
an iterator, or some other object which supports iteration.
The __next__() method of the iterator returned by enumerate()
returns a tuple containing a count (from start which defaults to 0) and
the values obtained from iterating over iterable."""

names = ["Ali", "John", "Sara"]

for i, name in enumerate(names):
    print(i, name)

#zip(*iterables, strict=False)

#Iterate over several iterables in parallel, producing tuples with an item from each one.

#Example:

for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)
