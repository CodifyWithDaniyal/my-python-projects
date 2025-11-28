# This program prints all marks in a list along with their position using the enumerate() function.
# The enumeration starts at 1, so the output shows "1 -> mark", "2 -> mark", etc.
marks=[87,97,92,45,87,50,64,99]
for index,mark in enumerate(marks,start=1):
    print(index,"->",mark)