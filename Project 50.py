# This program is a number guessing game.
# It generates a random number between 1 and 10 using the random module.
# The user is asked to guess the number. If the guess is correct, it prints a success message;
# otherwise, it shows the correct number.
import random as r
num=r.randint(1,10)
a=int(input("Guess a number between 1-10:"))
if a==num:
    print(f"You guessed it right the number was {num}")
else:
    print(f"You guessed it wrong the right number was {num}")