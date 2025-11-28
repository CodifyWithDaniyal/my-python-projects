# This program quizzes the user on the factorial of a randomly chosen number.
# - It selects a random number between 1 and 5 using the random module.
# - The user is asked to calculate its factorial.
# - If the answer is correct, it prints a success message; otherwise, it shows the correct answer.
from math import factorial
import random as r
num=r.randint(1,5)
a=int(input(f"What's the factorial of {num}?"))
if a==factorial(num):
    print("Congratulations! You got it right")
else:
    print(f"Sorry your answer is wrong the correct answer was {factorial(num)}")