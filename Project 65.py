# This program defines a MathTools class with static utility methods.
# - The is_even(a) method checks whether a number is even.
# - It is defined as a @staticmethod because it doesn't use instance or class data.
# - Static methods can be called directly from the class without creating an object.
# Example:
#   print(MathTools.is_even(6))  # Output: True
class MathTools:
    @staticmethod
    def is_even(a):
        return a%2==0
print(MathTools.is_even(6))