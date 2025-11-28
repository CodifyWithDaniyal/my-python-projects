# This program repeatedly asks the user to enter a number and checks if it is even or odd.
# If the user enters 0, the program exits the loop and prints a message indicating the exit.
while(True):
    num=int(input("Enter a number to check even or odd press 0 to exit the program:"))
    if(num==0):
        print("You just exited the program")
        break
    if(num%2==0):
        print("Even")
    else:
        print("odd")
