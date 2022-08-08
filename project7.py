"""
Isabella Lemus - Project 7

Design a programming solution that lets the user play a game of 
Rock-Paper-Scissors-Lizard-Spock against the computer.

When the program begins, a random number in the range of 1-5 is 
generated. Numbers correspond to the plays by the computer.

The user enters their selection by typing one of the options.
USe input validation with case-insensitive comparison to make sure
the user enters one of those strings only.

The computers choice is then displayed. 

The program then displays a messag indicating whether the user
or the computer is the winner.

"""

import random

gamePlay = ["rock", "paper", "scissors", "lizard", "spock"]

def printIntro():
    print ("\nLet's play Rock-Paper-Scissors-Lizard-Spock!")

def correctEntry(usr, comp):
    print ("\nYou played " + usr, end ='')
    print (" and the computer played " + comp)

    if usr == comp:
        printWinner(0)
    if usr == "scissors":
        if comp == "paper" or comp == "lizard":
            printWinner(1)
    if usr == "paper":
        if comp == "rock" or comp == "spock":
            printWinner(1)
    if usr == "rock":
        if comp == "lizard" or comp == "scissors":
            printWinner(1)
    if usr == "lizard":
        if comp == "spock" or comp == "paper":
            printWinner(1)
    if usr == "spock":
        if comp == "scissors" or comp == "rock":
            printWinner(1)
    else:
        printWinner(2)

def printWinner(num):
    print (num)
    if num == 0:
        print ("You tied! Better luck next time")
    elif num == 1: 
        print ("You win! The computer loses")
    else: 
        print ("You lose. That's too bad :(")

    printExit()

def printExit():
    print ("Thanks for playing!\n")

def playGame():

    valid = False
    while(not valid):

        user = str(input("Make your play or type 'q' to quit the game: "))

        computer = ""
        computer = gamePlay[random.randint(0,4)]

        if user.lower() == "rock" or user.lower() == "paper" or user.lower() == "scissors" or user.lower() == "lizard" or user.lower() == "spock":
            correctEntry(user.lower(), computer)
            valid = True

        elif user.lower() == "q":
            valid = True
            printExit()

        else:
            print ("Please enter one of the following options: Rock, Paper, Scissors, Lizard, Spock ")


printIntro()
playGame()