"""Create a program that asks the user for a number and
then prints out a list of all the divisors of that number. """

intNum = int(input("Please enter the number: "))
cnt=1
list_divisors=[]
while cnt <= intNum:
    if intNum % cnt == 0:
        list_divisors.append(cnt)
    cnt = cnt + 1

print("The divisors of " + str(intNum) + " is/are " + str(list_divisors))