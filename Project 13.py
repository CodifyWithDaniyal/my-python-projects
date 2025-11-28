# This program prints all odd numbers from 1 up to a user-entered number.
# It uses a for-loop with a step of 2 to generate the odd numbers.
num=int(input("Enter a number:"))
for i in range(1,num+1,2):
    print(i)
