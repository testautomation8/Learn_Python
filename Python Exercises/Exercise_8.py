"""Make a two-player Rock-Paper-Scissors game.Ask for player plays (using input), compare them, print out a message of
congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock """

choice = "Yes"

while choice.strip() != "No":

    player1 = input("Please enter your choice Player_1: ")
    player2 = input("Please enter your choice Player_2: ")

    if player1 == "Rock":
        if player2 == "Scissors":
            print("Congratulations - Player_1 is the winner")
        elif player2 == "Paper":
            print("Congratulations - Player_2 is the winner")
        else:
            print("Try Again - No one is winner")

    elif player1 == "Scissors":
        if player2 == "Rock":
            print("Congratulations - Player_2 is the winner")
        elif player2 == "Paper":
            print("Congratulations - Player_1 is the winner")
        else:
            print("Try Again - No one is winner")

    elif player1 == "Paper":
        if player2 == "Scissors":
            print("Congratulations - Player_2 is the winner")
        elif player2 == "Rock":
            print("Congratulations - Player_1 is the winner")
        else:
            print("Try Again - No one is winner")


    choice = input("Would you like to start a new game? Yes/No:")