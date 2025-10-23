#This program takes a number and  prints it's table and if you press zero it exits
while(True):
    n=int(input("Enter a number:"))
    if(n==0):
         print("You exited the loop by pressing zero")
         break
    for i in range(1,11):
        print(n,"X by",i,"is",n*i)