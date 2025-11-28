# This program defines a Salon class that stores a customer's name, service, and price.
# When an instance is created, it prints a message showing which customer received which service and its price.
# Example: Ms. Abeera got Keratin treatment and their total price is Rs 6000
class Salon:
    def __init__(self,name,service,price):
        self.name=name
        self.service=service
        self.price=price
        print(f"Ms. {name} got {service} and their total price is Rs {price}")
Salon("Abeera","Keratin treatment","6000")
Salon("Zainab","Hair dye","5000")