# This program demonstrates a simple decorator in Python.
# - The decorator `deco` wraps a function, printing messages before and after the function call.
# - The `best` function is decorated with `@deco`, so calling it prints the wrapper messages along with the function's output.
def deco(f):
    def wrapper(*args,**kwargs):
        print("Looks good")
        f(*args,**kwargs)
        print("Hope for the best")
    return wrapper
@deco
def best(a=1,b=66):
    print(f"Is it {a+b}")
best()