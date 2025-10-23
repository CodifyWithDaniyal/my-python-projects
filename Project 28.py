#Calculator with fuctions
def add(a,b):
    print("The sum of ",a,"and",b,"is",a+b)
def sub(a,b):
    print("The subraction of ",a,"and",b,"is",a-b)
def mul(a,b):
    print("The multiplicaton of ",a,"and",b,"is",a*b)
def div(a,b):
    print("The division of ",a,"and",b,"is",a/b)
c=int(input("Enter the first number:"))
d=int(input("Enter the second number:"))
e=input("Enter the operator:")
if e==("+"):
    add(c,d)
elif e==("-"):
    sub(c,d)
elif e==("*"):
    mul(c,d)
elif e==("/"):
    div(c,d)