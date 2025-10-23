#This program takes a number and counts to 1 from it and if you enter zero it exits
while(True):
    n=int(input("Enter a number:"))
    for i in range(n,0,-1):
        print(i)
    if(n==0):
        print("You exited the program by pressing zero")
        break