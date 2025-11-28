# This program repeatedly prompts the user to enter a password ("dani").
# It continues looping until the correct password is entered.
# If the user enters an empty string, the program asks again.
# Once the correct password is entered, it prints a success message and exits.
while(True):
    passs=input("Enter your password:")
    if(passs=="dani"):
        break
    elif(passs==""):
        continue
print("You entered your password correctly")