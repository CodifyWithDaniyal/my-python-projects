# This program checks whether the entered number is even or odd using the modulus operator (%).
# It prints "even" if the number is divisible by 2, otherwise it prints "odd".
m = int(input("Please enter a number:"))
if m % 2 == 0:
    print("The number you entered is even")
else:
    print("The number you entered is odd")