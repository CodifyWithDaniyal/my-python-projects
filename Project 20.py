# This program asks the user to guess a secret number (3) between 1 and 10.
# The loop continues until the user guesses correctly, giving feedback after each wrong guess.
# Once the correct number is guessed, it prints a success message and exits.
a=int(input("Guess the number between 1-10:"))
while(a!=3):
    a=int(input("You guessed it wrong try again:"))
    if(a==3):
        break
print("You got it right!")