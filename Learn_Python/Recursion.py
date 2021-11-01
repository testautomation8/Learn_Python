def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


num = int(input("Please enter the number: "))
print("The factorial of {} is {}".format(num, factorial(num)))
