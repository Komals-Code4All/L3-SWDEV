# Guess My Number
# =========================================

import random

myNumber = random.randint(1,20) + 1     # get a random number between 1 and 20

# Start by setting variables as needed
yourNumber = int(0)                     # what the user guessed
attempts  = int(0)                      # number of attempts at guessing

# Print instructions
print('I have thought of a number between 1 and 20.')
print('\nTry guessing what it is ')


# While they dont guess myNumber...
while yourNumber != myNumber:
    attempts = attempts + 1
    yourNumber = int(input('Whats your guess? '))

    if yourNumber > myNumber:
        print('\nToo high ')
    elif yourNumber < myNumber:
        print('\nToo Low ')
    else:
        print('Well Done!' )


# They got it
print("You got it in ", attempts, "attempts")










        


