#This program takes the user's password in three tries
tries=1
while tries<=3:
    tries+=1
    num=input("Enter your password:")
    if(num=="my_password"):
        print("You entered the correct password")
        break
else:
    print("Sorry you entered wrong password 3 times try again tomorrow!")