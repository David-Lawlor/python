number = 42;  ## All variables in python are objects

# print out the value of the variable
print("This is the value of the variable  " + str(number));

# prints the id of the variable
print("This is the id of the variable  " + str(id(number)));

# prints the type of the varible
print("This is the type of the varible  " + str(type(number)));

# data types int
a = 50;
print(type(a), a)

# data type float
b = 50.0
print(type(b), b)

# example of casting
c = int(50.0)
print(type(c), c)

# example of rounding
d = round(45.8)
print(type(d), d)

e = "This is a string"
print(e)

f = '''This is a multi-line
quote. Triple single quotes allow
a string to span multiple lines'''
print(f)

g = "This is a single line quote \nwith a new line character"
print(g)

# This method is specific to python2
firstName = "David"
surname = "Lawlor"
print("This is a strng which will allow the input of a variable such as a name, Hello %s" % firstName)

# This is the method is specific this will work in later versions of python2 and python3
print("This is a strng which will allow the input of a variable such as a name, Hello {} {}".format(firstName, surname))

# This is a tuple, a tuple is a list of numbers which cannot be modified(immutable). this is the main difference between a
# list and a tuple.
# An index cannot be specified in a tuple
tuple = (5, 4, 3, 2, 1)
print(type(tuple), tuple)

# This is an example of a list. Note square bracket not parentheses.
list = [5, 4, 3, 2, 1]
print(type(list), list)

# this is appending to a list
list.append(6)
print(type(list), list)

# this is printing out an certain index in the list
print(list[0])

# This is printing a range from within a list last element is last index plus one.
# This is because when a range is specified it is not inclusive of the last index specified
print(list[3:6])

# if the first index of the list is omitted then it will start at the first location
print(list[:3])

# Working in the same way at omitting the first index. This can be done be ommitting the second index
# which will print out to the last index
print(list[3:])