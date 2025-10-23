#Calculator using match case 
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