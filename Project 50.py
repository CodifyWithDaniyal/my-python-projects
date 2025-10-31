#Number guessing game with random module
import random as r
num=r.randint(1,10)
a=int(input("Guess a number between 1-10:"))
if a==num:
    print(f"You guessed it right the number was {num}")
else:
    print(f"You guessed it wrong the right number was {num}")