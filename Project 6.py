# This program determines if the room temperature is "cold" or "hot".
# It uses a one-line conditional with tuple indexing: ("cold", "hot")[temp > 30].
# If temp > 30, it prints "hot"; otherwise, it prints "cold".
temp=int(input("Please enter the temperature of your room:"))
result=("cold","hot")[temp>30]
print(result)