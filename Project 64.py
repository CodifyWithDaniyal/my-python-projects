# This program defines a Student class to store student information.
# - Instance variables: name and age (specific to each student)
# - Class variable: University_name (shared across all students)
# - The ShowDetail() method prints the student's details along with the university name.
# Example:
#   a = Student("Max", 20)
#   a.ShowDetail()
# Output:
#   The name of the student is Max, his/her age is 20.
#   The university in which he/she studies is Standford University.
class Student:
    University_name="Standford university"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def ShowDetail(self):
        print(f"The name of the student is {self.name} his/her age is {self.age}.The university in which he/she studies is {Student.University_name}")
a=Student("Max","20")
a.ShowDetail()