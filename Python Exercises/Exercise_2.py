"""Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user."""

Num = input("Please enter the number: ")
intNum = 0
try:
    intNum = int(Num)
    if intNum > 0:
        if intNum % 2 == 0:
            print("The number " + str(intNum) + " is Even")
        else:
            print("The number " + str(intNum) + " is Odd")
    else:
        print("Please enter positive integer more than 0.")
except ValueError:
    print("ERROR:Please enter an integer")



