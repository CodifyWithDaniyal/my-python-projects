# This program prints the multiplication table of a user-entered number from 1 to 10.
# It uses a for-loop to multiply the number by values from 1 to 10 and prints each result.
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)