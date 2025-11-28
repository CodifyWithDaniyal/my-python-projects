# This program collects four items from the user, stores them in a list,
# and then prints each item along with its position using enumerate().
# The enumeration starts at 1, so output shows "1 item", "2 item", etc.
items=[]
a=input("Enter your first item:")
b=input("Enter your second item:")
c=input("Enter your third item:")
d=input("Enter your fourth item:")
i=[a,b,c,d]
items.extend(i)
for index,i in enumerate(items,start=1):
    print(index,i)