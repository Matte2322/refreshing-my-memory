import random

playerInput = input("Choose rock, paper, or scissor: ")

userName = input("Choose your username: ")

possibleAction = ["rock", "paper", "scissor"]

computerAction = random.choice(possibleAction)


print(f"{userName} chose {playerInput} while the bot chose {computerAction}.")

if playerInput == computerAction:
    print("It's a tie")
elif playerInput == 'scissor':
    if computerAction == 'rock':
        print(f"{userName} lost the game!.")
    else:
        print(f"{userName} you win!")
elif playerInput == 'paper':
    if computerAction == 'scissor':
        print(f"{userName} loses!")
    else: 
        print("You win")
elif playerInput == 'rock':
    if playerInput == 'paper':
        print(f"{userName} loses by beating paper while a computer chose a rock LOL.")
    else:
        print("You win.")

