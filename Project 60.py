# This program defines a Student class that manages a student's marks safely.
# - Attributes: name, mathm, sciencem, englishm.
# - Each subject uses @property and setter to ensure marks are between 0 and 100.
# - The 'total' property calculates the sum of all subject marks (read-only).
# - Attempting to set marks outside 0-100 raises a ValueError.
# Example:
#   a = Student("Daniyal", 100, 98, 9)
#   print(a.total)  # Output: 207
class Student:
    def __init__(self,name,mathm,sciencem,englishm):
        self.name=name
        self.mathm=mathm
        self.sciencem=sciencem
        self.englishm=englishm
    @property
    def mathm(self):
        return self._mathm
    @mathm.setter
    def mathm(self,value):
        if value<0 or value>100:
            raise ValueError("Math marks must be between 0-100!")
        self._mathm=value
    @property
    def sciencem(self):
        return self._sciencem
    @sciencem.setter
    def sciencem(self,value):
        if value<0 or value>100:
            raise ValueError("Science marks must be between 0-100!")
        self._sciencem=value
    @property
    def englishm(self):
        return self._englishm
    @englishm.setter
    def englishm(self,value):
        if value<0 or value>100:
            raise ValueError("English marks must be between 0-100!")
        self._englishm=value
    @property
    def total(self):
        return self._mathm+self._sciencem+self._englishm
a=Student("Daniyal",100,98,9)
print(a.total)