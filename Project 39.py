# This function 'sum' takes two arguments a and b, calculates their sum, 
# and prints a formatted message showing the result. 
# The function also includes a docstring that describes its purpose, 
# which can be accessed using sum.__doc__.

def sum(a, b):
    '''Returns a message showing the sum of two numbers.'''
    print(f"The sum of {a} and {b} is {a+b}")

sum(45, 5)
print(sum.__doc__)