import random
import os
import sys

def choicePlayer(playerName, myChoice):
    playerName = input("What's your name?: ")
    myChoice = input("Choose rock, paper, or scissors: ")
    return myChoice, playerName

def computerChoose():
    computerChoice = [
        'rock',
        'paper',
        'scissors'
    ]
    randomActionC = random.choice(computerChoice)
    return randomActionC

# declare global variables by using a dictionary
randomActionC = computerChoose()
myChoice, playerName = choicePlayer(playerName=True, myChoice=True)

def checkStringResponse():
    print(playerName + " has chosen " + myChoice + " while the computer chose " + randomActionC)
    if myChoice != str and myChoice == float:
        return False # doesn't execute 

print("--------------------------------------------------------------------------------------")

def inAction():
    while True:
        if myChoice == randomActionC:
            print(f'{playerName} has tied with the computer!')
        elif myChoice == 'rock':
            if randomActionC == 'scissors':
                print(f'{playerName} has won against the computer by choosing rock while the computer chose a scissor.')
            else:
                print("You lost cuz the computer chose paper.")
        elif myChoice == 'paper':
            if randomActionC == 'rock':
                print(f'{playerName} has won against the computer by choosing paper while the computer chose a rock.')
            else:
                print('YOU LOST, LOL! The computer chose scissor to beat your fucking ass.')
        elif myChoice == 'scissors':
            if randomActionC == 'paper':
                print(f'{playerName} has won against the computer by choosing scissors while the computer choose paper.')
            else:
                print("YOU LOST BECAUSE THE COMPUTER CHOSE ROCK.")
        else:
            print("Try again, the word you've inputed makes me not understand what you're trying to say. Try to input a word within the directions.")

        if myChoice.isdigit():
            print("Do not input a number.")
        # ask user to play again
        play_again = input("Do you want to play again? Type 'no' if you don't want to play or type 'yes' if you want to: ")
        if play_again == 'no':
            print("See you next time.")
            break
        else:
            print("Have fun!")
            os.execl(sys.executable, os.path.abspath('/home/doormat/wife/functionsrps.py'), *sys.argv)               
inAction()
