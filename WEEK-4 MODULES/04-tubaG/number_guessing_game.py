'''Devoloper : Tuba GÜMÜS ESMEK
   Date      : 28.12.2022
   Subjeckt  : Number Guessing Game

'''
#Number Guessing Game

#As a player, I want to play a game which I can guess a number the computer chooses in the range I chose. 
# So that I can try to find the correct number which was selected by computer.
#Acceptance Criteria:
#Computer must randomly pick an integer from user selected a range, i.e., from A to B, 
# where A and B belong to Integer. 
# Your program should prompt the user for guesses if the user guesses incorrectly, 
# it should print whether the guess is too high or too low. If the user guesses correctly, 
# the program should print total time and total number of guesses.
#  You must import some required modules or packages You can assume that the user will enter valid input. 
# (use import random and time)

import random

import time
time.time()



# random number generated by the computer
number = random.randint(1,100)
beginning = time.time() # first guesses paly time begins
#print(number)
spiel = 0 #number of games


while True:   #trying to find number with while loop
    guess = int(input("guess a number")) # the player's guessed number

    spiel+=1
    if number > guess:  
        print("guess is low:increase")
        

    elif number< guess:
        print("guess is high:reuce")

    else:
        print("found the number")
        print(spiel,"  : number of guesses!" )
        finish = time.time()     #the game end time
        print(finish-beginning)  #to find the total time of the game
        break