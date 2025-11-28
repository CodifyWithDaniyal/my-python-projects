# This program prints a right-angled triangle pattern of stars (*).
# The user enters the number of rows, and each row contains as many stars as its row number.
row=int(input("Enter number of rows:"))
for i in range(1,row+1):
    print("*"*i)