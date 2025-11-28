# This program asks the user for their name, age, and hobby,
# then prints a self-introduction sentence using the format() method.
# The name is capitalized for better presentation.
name=input("What's your name:")
age=input("What's your age:")
hobby=input("What's your hobby:")
print("My name is {} and i am {} years old and i love {}.".format(name.capitalize(),age,hobby))