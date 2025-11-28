# This program categorizes the room temperature as Hot, Cold, or Mild.
# - Hot  → temperature > 30
# - Cold → temperature < 10
# - Mild → temperature between 10 and 30 inclusive
# The program uses if-elif-else statements to determine and print the category.
tem=int(input("Please enter the temperature of your room:"))
if(tem>30):
    print("Hot")
elif(tem<10):
    print("Cold")
else:
    print("Mild")
