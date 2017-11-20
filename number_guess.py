#
###################################
# PROLOG SECTION
# number_guess_basic.py
# A game to guess a number between 1 and 10.
# This is the basic version of the program:
# - Accepts user input.
# - Checks that input is numeric.
# - Converts numeric input to an integer.
# - Checks that the guess is in the range of valid numbers (1-10).
# - Uses the randint() random number function to pick the number.
# - Sets the maximum number as a variable (number_max).
# - Uses a while loop to give the user 3 tries to get the right answer.
# - The while statement goes ahead of the raw_input() statement.
# - The while loop requires the programmer to reindent various blocks.
# - The while loop requires the programmer to reword some of the messages.
#
# Tested with Python 3.3.0 on Windows 7
# Fri Apr  5, 2013
#
# Copyright 2009-2015 National Academy Foundation. All rights reserved.
#
# Possible future enhancements:
# Unresolved bugs:
###################################

###################################
# PROCESSING INITIALIZATION SECTION
###################################
# pick the winning number
the_number = 5
# initialize the guess to an incorrect answer
guess = 0
# print the rules for the game
print()
print("You have 1 try to guess a number between 1 and 10.")
print("If you guess wrong, I'll tell you if your guess was too high or too low.")
print()

###################################
# PROCESSING SECTION
# Branching code: if/else
###################################
#
# get the user's guess and process it
#
guess_string = str(input("Enter your numeric guess: "))
# test to make sure we got numeric input
if guess_string.isdigit():
    # convert the string entered to an integer
    guess = int(guess_string)
else:
    # error, the input was not a number
    print("Please enter a numeric guess.")

###################################   
# CLEANUP, TERMINATION, AND EXIT SECTION
###################################
#
# print winning and losing messages
#
# print winning message
if guess == the_number:
    print("Congratulations, you guessed the number.")
# print losing message
else:
    print("Try playing the game again.")
