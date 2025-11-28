# Simple ATM Simulation
# ---------------------
# This program simulates a basic ATM interface.
# The user is asked to choose an option:
#   1 -> Withdraw
#   2 -> Deposit
#   3 -> Check balance
#
# The program uses Python's match–case statement to handle each choice.
# If the user enters an invalid option, it prints "Wrong choice".
#
# Example:
# Input: 2
# Output: deposit

print("Welcome to the ATM!\n")
a=int(input("Choose 1 for withdraw,2 for deposit and 3 for check balance"))
match a:
    case 1:
        print("withdraw")
    case 2:
        print("deposit")
    case 3:
        print("check balance")
    case _ :
        print("Wrong choice")