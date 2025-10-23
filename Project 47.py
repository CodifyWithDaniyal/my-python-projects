#This program only prints the even indices of the list
marks=[87,97,92,45,87,50,64,99]
for i,mark in enumerate(marks,start=1):
    if i%2==0:
        print(i,mark)