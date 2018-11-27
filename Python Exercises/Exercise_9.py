"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out"""

import random
choice = "Y"
cnt = 1
while choice.strip() == "Y":
    usrNumber = int(input("Please guess the number between 1 to 9: "))
    rndNumber = random.randint(1, 9)
    if usrNumber == rndNumber:
        print("You have guessed exactly right!!")
        break
    elif usrNumber > rndNumber:
        print("You have guessed too high!!")
        cnt = cnt + 1
    else:
        print("You have guessed too low!!")
        cnt = cnt + 1
    choice = input("Would you like to continue(Y/N):")

print("You have taken " + str(cnt) + " chances to guess right")
