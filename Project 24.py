# This program displays a simple menu with three options:
# 1 -> Say hello
# 2 -> Print name
# 3 -> Exit the program
# The menu repeats until the user chooses option 3, which exits the program.
while(True):
    n=int(input("1.Say hello\n2.print name\n3.exit\n"))
    if(n==3):
        print("You exited the program")
        break

