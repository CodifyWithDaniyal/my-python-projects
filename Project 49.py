# This program takes a string input from the user and prints each character along with its index.
# It uses the enumerate() function to display the index and corresponding character.
a=input("Enter your character")
for index,i in enumerate(a):
    print(index,i)