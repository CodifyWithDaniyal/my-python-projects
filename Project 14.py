# This program prints all even numbers from 2 up to a user-entered number.
# It uses a for-loop with a step of 2 to generate the even numbers.
num=int(input("Enter a number:"))
for i in range(2,num+1,2):
    print(i)