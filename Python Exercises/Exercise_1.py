""" Create a program that asks the user to enter their name and their age. Print out a message addressed
to them that tells them the year that they will turn 100 years old."""

strName = input("Please enter your name: ")
intAge = int(input("Please enter you age: "))
intCount = int(input("How many times you want to display the message: "))
intYear = (2014-intAge) + 100

count = 0
while count < intCount:
    print("Hello " + strName + ".You will turn 100 years old in the year " + str(intYear))
    count = count + 1
