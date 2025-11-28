# This program checks whether a given number is even or odd.
# It defines a function 'ch(a)' that prints "EVEN" if the number is divisible by 2,
# otherwise it prints "ODD". The user is prompted to enter a number, which is passed to the function.
def ch(a):
    if a % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

n = int(input("Enter the number: "))
ch(n)
