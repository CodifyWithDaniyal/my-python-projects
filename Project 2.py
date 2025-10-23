#This program takes temperature and tells if its hot,cold or mild
tem=int(input("Please enter the temperature of your room:"))
if(tem>30):
    print("Hot")
elif(tem<10):
    print("Cold")
else:
    print("Mild")
