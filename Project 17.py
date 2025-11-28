# This program repeatedly asks the user to enter a number and prints its multiplication table from 1 to 10.
# If the user enters 0, the program exits the loop and prints a message indicating the exit.
while(True):
    n=int(input("Enter a number:"))
    if(n==0):
         print("You exited the loop by pressing zero")
         break
    for i in range(1,11):
        print(n,"X by",i,"is",n*i)