# This program defines a Temperature class with static methods for temperature conversion.
# - F_converter(c) converts Celsius to Fahrenheit.
# - C_converter(f) converts Fahrenheit to Celsius.
# - Both methods are static because they don't use self or class attributes.
# - They can be called directly from the class without creating an instance.
# Example:
#   print(Temperature.C_converter(98.6))  # Output: 37.0
#   print(Temperature.F_converter(37))    # Output: 98.6
class Temperature:
    @staticmethod
    def F_converter(c):
        return (c*9)/5+32
    @staticmethod
    def C_converter(f):
        return (f-32)*5/9
print(Temperature.C_converter(98.6))