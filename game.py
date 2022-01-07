import random

playerInput = input("Choose rock, paper, or scissor: ")

userName = input("Choose your username: ")

possibleAction = ["rock", "paper", "scissor"]

computerAction = random.choice(possibleAction)


print(f"{userName} chose {playerInput} while the bot chose {computerAction}.")

if playerInput == computerAction:
    print("It's a tie")
elif computerAction == 'scissor':
    if playerInput == 'rock':
        print(f"{userName} wins by beating scissor with a rock.")
    else:
        print(f"{userName} lost the game!")
elif computerAction == 'paper':
    if playerInput == 'scissor':
        print(f"{userName} wins")
    else: 
        print("You lose")
elif computerAction == 'rock':
    if playerInput == 'paper':
        print(f"{userName} wins by beating paper while a computer chose a rock LOL.")
    else:
        print("You lose.")

