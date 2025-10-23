#This program takes a list of items from the user and prints each item with its number
items=[]
a=input("Enter your first item:")
b=input("Enter your second item:")
c=input("Enter your third item:")
d=input("Enter your fourth item:")
i=[a,b,c,d]
items.extend(i)
for index,i in enumerate(items,start=1):
    print(index,i)