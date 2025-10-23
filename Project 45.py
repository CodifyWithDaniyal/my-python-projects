#Valid Age checker
age=int(input("Enter your age:"))
class NegativeAgeError(Exception):
    pass
class UnrealisticAgeError(Exception):
    pass
if age<0:
    raise NegativeAgeError("Age can't be negative")
if age>120:
    raise UnrealisticAgeError("Age can't be that high")