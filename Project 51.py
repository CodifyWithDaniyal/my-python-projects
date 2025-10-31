#Math factorial quiz 
from math import factorial
import random as r
num=r.randint(1,5)
a=int(input(f"What's the factorial of {num}?"))
if a==factorial(num):
    print("Congratulations! You got it right")
else:
    print(f"Sorry your answer is wrong the correct answer was {factorial(num)}")