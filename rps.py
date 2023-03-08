import random


userInput = input("Please enter rock paper or scissors") 

compOptions = [
    "rock", "paper", "scissors"
]
compInput = random.choice(compOptions)

def play_again():
    play()

def play(): 
    if userInput == compInput: 
        print("It's a draw")
        
        #this condition is gonna be when user picks rocks 
    elif userInput == "rock":
        if compInput == "scissors":
            print("You chose"+ userInput + "and computer chose"+ compInput)
            print("You won") 
        else:
            print("You chose"+ userInput + "and computer chose"+ compInput)
            print("You lose")

            #this condition is gonna be when user picks paper
    elif userInput == "paper":
        if compInput == "scissors":
            print("You chose"+ userInput + "and computer chose"+ compInput)
            print("You lose") 
        else:
            print("You chose"+ userInput + "and computer chose"+ compInput)
            print("You won") 

             #this condition is gonna be when user picks scissors 
    elif userInput == "scissors":
        if compInput == "rock":
            print("You chose"+ userInput + "and computer chose"+ compInput)
            print("You lose") 
        else:
            print("You chose"+ userInput + "and computer chose"+ compInput)
            print("You won")

    else:
        print("Please make a valid choice")
        play_again()

play()