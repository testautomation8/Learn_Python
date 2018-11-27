"""Ask the user for a number and determine whether the number is prime or not. Use Functions"""

def prime(number):
    flag = ""
    for x in range(number):
        if x != 0 and x != 1:
            flag = True
            if number/x == 0 or number % x == 0:
                flag = False

    if flag:
        return str(number) + " is a prime number."
    else:
        return str(number) + " is not a prime number."


number = int(input("Please enter the integer: "))
print(prime(number))



