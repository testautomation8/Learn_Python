"""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate."""

def fibonacci(usr_rng):
    fib_series = []
    cnt = 0
    temp = 0
    fib = 1
    while len(fib_series) < usr_rng:

        fib_series.append(fib)
        fib = temp + fib_series[cnt]
        cnt = cnt + 1
        temp = fib_series[cnt-1]

    return fib_series


usr_rng = int(input("How many Fibonnaci numbers you want to generate: "))
print(fibonacci(usr_rng))