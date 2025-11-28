# This program repeatedly prompts the user to enter a password.
# The correct password is "python". The loop continues until the user
# enters the correct password, after which it prints "Access granted" and exits.
while(True):
    pa=input("Enter your password:")
    if(pa=="python"):
        print("Access granted")
        break