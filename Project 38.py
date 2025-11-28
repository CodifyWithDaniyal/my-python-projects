# This program converts a temperature from Celsius to Fahrenheit.
# It prompts the user to enter a temperature in Celsius, stores it in variable 'i',
# then calculates the equivalent Fahrenheit temperature using the formula: (Celsius * 9/5) + 32.
# Finally, it prints the result in a readable format using an f-string.
i=int(input("Enter the celsius to convert it into fahrenheight:"))
print(f"{i} converted to fahrenheight is equals to {(i*9/5)+32} degrees")
