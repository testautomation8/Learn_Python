"""Ask the user for a string and print out whether this string is a palindrome or not. """

tstString = input("Please enter the String: ")
revString = ""
cnt = 1
while cnt <= len(tstString):
    revString = revString+tstString[len(tstString)-cnt]
    cnt = cnt+1
if tstString == revString:
    print("String is a Palindrome")
else:
    print("String is not a Palindrome")