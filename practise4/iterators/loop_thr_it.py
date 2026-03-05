#We can also use a for loop to iterate through an iterable object:

#Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#Iterate the characters of a string:
mystr = "banana"

for x in mystr:
  print(x)

#The for loop actually creates an iterator object
#and executes the next() method for each loop.
