#Using *args to accept any number of arguments:
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")


#In this example, "Hello" is assigned to greeting, and the rest are collected in names.
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
#This way, the function will receive a dictionary of arguments and can access the items accordingly:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


#Combining *args and **kwargs
#You can use both *args and **kwargs in the same function.

#The order must be:

#regular parameters
#*args
#**kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")