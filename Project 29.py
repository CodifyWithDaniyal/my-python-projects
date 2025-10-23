#This program takes the percentage of 4 subjects and print their average
a=int(input("Enter your percentage of first subject:"))
b=int(input("Enter your percentage of second subject:"))
c=int(input("Enter your percentage of third subject:"))
d=int(input("Enter your percentage of fourth subject:"))
def avg(a,b,c,d):
    return (a+b+c+d)/4
f=avg(a,b,c,d)
print(f,"%")