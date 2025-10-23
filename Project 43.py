#Safe division calculator
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