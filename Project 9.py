# This program performs basic arithmetic operations based on user input.
# The user enters two numbers and an operator (+, -, *, /).
# The program uses match–case to determine which operation to perform and prints the result.
# If the operator is invalid, it prints an error message.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
op=input("Enter the operator you want to perform e.g -+/*:")
match op:
    case "-":
        print(a-b)
    case "+":
        print(a+b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _ :
        print("You entered an invalid operator")