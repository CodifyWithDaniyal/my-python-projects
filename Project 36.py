# This program generates a simple bill for three items.
# It asks the user to input the name and price of each item,
# then prints a formatted bill showing each item with its price
n1=input("Enter the first item:")
p1=int(input("Enter it's price:"))
n2=input("Enter the name of second item:")
p2=int(input("Enter it's price:"))
n3=input("Enter the name of third item:")
p3=int(input("Enter it's price:"))
print(f"Items    price\n{n1}    {p1}\n{n2}  {p2}\n{n3}  {p3}\nTotal={p1+p2+p3}")