# This program converts an amount of money from one currency to another.
# It asks the user for the amount and the conversion rate,
# then uses a function 'convert(amount, rate)' to calculate and return the converted value.
a=float(input("Enter your amount:"))
b=float(input("Enter today's rate:"))
def convert(amount,rate):
    return amount*rate
print(convert(a,b))