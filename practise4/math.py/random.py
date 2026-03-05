"""
What is a Random Number?
Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

Pseudo Random and True Random.
Computers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.

If there is a program to generate random number it can be predicted, thus it is not truly random.

Random numbers generated through a generation algorithm are called pseudo random.

Can we make truly random numbers?

Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.

We do not need truly random numbers, unless it is related to security (e.g. encryption keys) or the basis of application is the randomness (e.g. Digital roulette wheels).

In this tutorial we will be using pseudo random numbers.

"""
#NumPy offers the random module to work with random numbers.
#Generate a random integer from 0 to 100:
from numpy import random

x = random.randint(100)

print(x)

#The random module's rand() method returns a random float between 0 and 1.
#Generate a random float from 0 to 1:
from numpy import random

x = random.rand()

print(x)

"""
Generate Random Number From Array

The choice() method allows you to generate a random value based on an array of values.

The choice() method takes an array as a parameter and randomly returns one of the values.

"""
#Return one of the values in an array:
from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)

"""
The choice() method also allows you to return an array of values.

Add a size parameter to specify the shape of the array.

"""
#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)

"""
Random Permutations of Elements

A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

The NumPy Random module provides two methods for this: shuffle() and permutation().

"""
#Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
#Randomly shuffle elements of following array:
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)

#The shuffle() method makes changes to the original array.