# Example of Tuple unpacking
myTuple = ("one", 2, "three")
a, b, c = myTuple
print(a)
print(b)
print(c)

# Can be used for exchanging values
myTuple = (1, 2)
x, y = myTuple
print(x)
print(y)
x, y = y, x
print(x)
print(y)
