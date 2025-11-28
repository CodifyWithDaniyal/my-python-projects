# This program defines a Students class that collects a new student's details.
# - It asks for the student's name, age, and grade.
# - When an instance is created, it prints a welcome message showing the student's information.
class Students:
    def __init__(self):
        self.name=input("Enter your name sir:")
        self.age=input("Enter your age sir:")
        self.grade=input("Enter your grades sir:")
        print(f"Welcome to your new class {self.name} You are {self.age} years old and your grades are {self.grade}")
Students()