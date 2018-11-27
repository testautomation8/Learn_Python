"""Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than the number user enters."""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num=int(input("Please enter the number: "))
for x in a:
    if x < num:
        b.append(x)
print("The original list is:" + str(a))
print("Number less than " + str(num)+" in the list are:" + str(b))