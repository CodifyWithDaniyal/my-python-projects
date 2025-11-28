# This program defines a Car class that tracks the total number of cars in a showroom.
# - Each car has a name and model.
# - A class variable 'count' keeps track of how many Car objects have been created.
# - When a Car object is instantiated, it prints its details and the current total car count.
# Example:
#   a = Car("Buggati", "Chiron")
#   a = Car("Toyota", "Corolla")
#   a = Car("Honda", "City")
class Car:
    count=0
    def __init__(self,name,model):
        Car.count +=1
        self.name=name
        self.model=model
        print(f"The name of the car is {self.name} and it's model is {self.model}")
        print("Number of cars in the showroom are: ",Car.count)
a=Car("Buggati","Chiron")
a=Car("Toyota","Corolla")
a=Car("Honda","City")