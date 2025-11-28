# This program asks the user to guess a secret number (7).
# The loop continues until the user guesses correctly,
# then prints a success message and exits.
while(True):
    a=int(input("Guess the number:"))
    if(a==7):
        print("You got it right!")
        break