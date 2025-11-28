# This program defines a CalAge class that validates a person's age.
# - The age attribute uses @property and a setter to ensure it is non-negative.
# - If a negative age is provided, a ValueError is raised.
# Example:
#   a = CalAge(20)
#   print(a.age)  # Output: 20
class CalAge:
    def __init__(self,age):
        self.age=age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        if value<0:
            raise ValueError("Age can't be negative")
        self._age=value
a=CalAge(10)
print(a.age)