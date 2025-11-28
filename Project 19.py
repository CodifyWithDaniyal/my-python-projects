# This program displays a simple menu with three options:
# 1 -> Add two numbers
# 2 -> Subtract two numbers
# 3 -> Exit the program
# The menu repeats until the user selects option 3, which exits the program.
a=int(input("1=Add two number\n2=Subtract two number\n3=Exit\n"))
while(a!=3):
    a=int(input("1=Add two number\n2=Subtract two number\n3=Exit\n"))
print("You exited the program")