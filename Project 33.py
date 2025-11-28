# This program checks whether a given list is a palindrome.
# A list is a palindrome if it reads the same forwards and backwards.
# The program creates a copy of the list, reverses it, and compares it
# with the original to determine if it is a palindrome.
li=[1,2,1]
a=li.copy()
a.reverse()
if(a==li):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")