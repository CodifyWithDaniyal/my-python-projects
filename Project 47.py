# This program prints the elements of a list that are at even indices.
# It uses enumerate() starting from 1 and prints the index and value if the index is even.
marks=[87,97,92,45,87,50,64,99]
for i,mark in enumerate(marks,start=1):
    if i%2==0:
        print(i,mark)