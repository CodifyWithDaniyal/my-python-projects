#Currency convertor with functions
a=float(input("Enter your amount:"))
b=float(input("Enter today's rate:"))
def convert(amount,rate):
    return amount*rate
print(convert(a,b))