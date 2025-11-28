# This program prints the day of the week based on a number input (1-7).
# The user enters a number, and match–case is used to determine the corresponding day.
# If the number is outside 1-7, it prints "Invalid choice".
week=int(input("Please enter a number between 1-7: "))
match week:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")   
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid choice")