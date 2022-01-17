userInput = input("Say something like 'hello.': ")


def reply(response):
    if 'hello' == userInput:
        print("Hello")   
    else:
        print("Sorry, I only know the word 'hello.'")
    return response   

reply(userInput)