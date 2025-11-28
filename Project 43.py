# This program performs division of two numbers with error handling.
# - It prompts the user to enter two numbers.
# - If the input is invalid (not a number), it raises a ValueError.
# - If the second number is zero, it raises a ZeroDivisionError.
# - The finally block prints a message indicating that the calculation is complete.
try:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    num1/num2
except ValueError:
    print("You entered wrong input")
except ZeroDivisionError:
    print("Sorry can't divide by zero")
finally:
    print("Calculation completed!")