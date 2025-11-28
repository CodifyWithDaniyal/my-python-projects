# This program repeatedly asks the user to enter a number and counts down from that number to 1.
# If the user enters 0, the program exits the loop and prints a message indicating the exit.
while(True):
    n=int(input("Enter a number:"))
    for i in range(n,0,-1):
        print(i)
    if(n==0):
        print("You exited the program by pressing zero")
        break