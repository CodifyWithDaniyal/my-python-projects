# This program demonstrates a decorator that wraps a function.
# - The decorator prints messages before and after the function execution.
# - It works with functions that have arguments and returns values correctly.

def deco(func):
    def wrap(*args, **kwargs):
        print("This is the starting of this function")
        result = func(*args, **kwargs)
        print("This is the ending of this function")
        return result
    return wrap

@deco
def hello():
    print("Hello World")

hello()

@deco
def add(a, b):
    return a + b

a = add(1, 23)
print(a)  # Correctly prints 24
