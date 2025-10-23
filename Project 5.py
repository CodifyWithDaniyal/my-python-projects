# this program takes a number and displays if its even or odd using clever if
num=int(input("Please enter a number:"))
result=("odd","even")[num%2==0]
print(result)