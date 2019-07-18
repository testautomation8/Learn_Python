"""Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order"""

def revString(usrString):

    x = usrString.split()
    x.reverse()
    return " ".join(x)


usrString = input("Please enter the string : ")

print("Actual string is : " + usrString)
print("Reverse string is : " + revString(usrString))
