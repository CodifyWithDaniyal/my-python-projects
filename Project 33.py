#This program tells if the list is a palindrome or not
li=[1,2,1]
a=li.copy()
a.reverse()
if(a==li):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")