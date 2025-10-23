#This program acts as an ATM
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