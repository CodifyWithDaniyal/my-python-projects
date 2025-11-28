# This program checks whether the entered age is valid.
# - If the age is negative, it raises a custom NegativeAgeError.
# - If the age is unrealistically high (greater than 120), it raises a custom UnrealisticAgeError.
age=int(input("Enter your age:"))
class NegativeAgeError(Exception):
    pass
class UnrealisticAgeError(Exception):
    pass
if age<0:
    raise NegativeAgeError("Age can't be negative")
if age>120:
    raise UnrealisticAgeError("Age can't be that high")