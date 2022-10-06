''' Rock , Papers , Scissors Game with computer '''

# By Laksh


import random
import time

def game(com , player):
    if player == com:
        return None
    elif com == "r":
        if player == "s":
            return False
        elif player == "p":
            return True    
    elif com == "s":
        if player == "p":
            return False
        elif player == "r":
            return True    
    elif com == "p":
        if player == "r":
            return False
        elif player == "s":
            return True    


randNo = random.randint(1 , 3)
if randNo == 1:
    comp = "r"
elif randNo == 2:
    comp = "p"
elif randNo == 3:
    comp = "s"


while True:
    print("Welcome To Rock , Papers , Scissors Game ... \n Starting Game , Please wait....")
    time.sleep(2)

    print("\nComputer Has Already Chosen his move")
    time.sleep(1)
    player = input("Your Turn: Rock [ r ] , Papers [ p ] , Scissors [ s ] : \n")
    result = game( comp , player)

    if comp == "r":
        comp_chance = "Rock"
    elif comp == "p":
        comp_chance = "Paper"
    elif comp == "s":
        comp_chance = "Scissors"

    if player == "r":
        player_chance = "Rock"
    elif player == "p":
        player_chance = "Paper"
    elif player == "s":
        player_chance = "Scissors"
    elif player == "quit":
        print("Total Wins : " , wins)
        exit()

    print("Computer chose " , comp_chance)
    print("You chose " , player_chance)

    wins = 0

    print("\n Predicting Result......")
    time.sleep(0.5)
    if result == None:
        print("\n The game is tied")
    elif result:
        print("\n You Won")
        wins = wins + 1
    else:
        print("\n You Lose")

    print("Type quit to exit the Game\n")
    time.sleep(1)
    print("Thanks For playing this Game \n This game was made by Laksh :) ")



