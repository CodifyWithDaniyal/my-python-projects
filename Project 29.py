# This program calculates the average percentage of four subjects.
# It asks the user to input the percentages, then uses a function 'avg(a, b, c, d)'
# to compute and return the average, which is printed at the end.
a=int(input("Enter your percentage of first subject:"))
b=int(input("Enter your percentage of second subject:"))
c=int(input("Enter your percentage of third subject:"))
d=int(input("Enter your percentage of fourth subject:"))
def avg(a,b,c,d):
    return (a+b+c+d)/4
f=avg(a,b,c,d)
print(f,"%")