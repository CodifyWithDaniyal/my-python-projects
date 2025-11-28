# This program calculates the sum of all numbers from 1 up to a user-entered number.
# It uses a for-loop to add each number to a total, then prints the total sum.
num=int(input("Enter a number:"))
total=0
for i in range(1,num+1):
    total=total+i
print(total)