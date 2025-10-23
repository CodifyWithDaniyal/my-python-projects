#This program checks a number if its odd or even and by pressing 0 you can exit the program
while(True):
    num=int(input("Enter a number to check even or odd press 0 to exit the program:"))
    if(num==0):
        print("You just exited the program")
        break
    if(num%2==0):
        print("Even")
    else:
        print("odd")
