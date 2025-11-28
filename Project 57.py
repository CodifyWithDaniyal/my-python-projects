# This program defines a Car class that stores details about a car.
# - Attributes include brand name, number of backlights, number of front lights, and car model.
# - When an instance is created, it prints a descriptive message showing all these details.
class Car:
    def __init__(self,brandn,backlights,frontlights,car):
        self.brandn=brandn
        self.backlights=backlights
        self.frontlights=frontlights
        self.car=car
        print(f"{self.brandn} is a very good brand and it's {self.car} has {self.frontlights} lights on the front and {self.backlights} lights on it's back ")
a=Car("Toyota",2,4,"Corolla")