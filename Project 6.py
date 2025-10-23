#This program takes temperature and tells if its hot or cold using clever if
temp=int(input("Please enter the temperature of your room:"))
result=("cold","hot")[temp>30]
print(result)