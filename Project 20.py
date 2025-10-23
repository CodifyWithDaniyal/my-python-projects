#Number guessing game
a=int(input("Guess the number between 1-10:"))
while(a!=3):
    a=int(input("You guessed it wrong try again:"))
    if(a==3):
        break
print("You got it right!")