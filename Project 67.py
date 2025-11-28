# This program defines an Employee class that keeps track of the total number of employees.
# - Each Employee object has a name.
# - A class variable 'counter' is incremented every time a new Employee is created.
# - The class method get_total() returns the total number of Employee instances.
# Example:
#   a = Employee("Dani")
#   b = Employee("Ali")
#   print(Employee.get_total())  # Output: 2
class Employee:
    counter=0
    def __init__(self,name):
        self.name=name
        Employee.counter +=1
    @classmethod
    def get_total(cls):
        return cls.counter
a=Employee("Dani")
b=Employee("Ali")
print(Employee.get_total())