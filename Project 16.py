# This program calculates the factorial of a user-entered number.
# It uses a for-loop to multiply all integers from 1 up to the number,
# then prints the resulting factorial.
num=int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)