# This program allows the user up to three attempts to enter the correct password.
# If the correct password ("my_password") is entered within three tries, it prints a success message.
# If all three attempts fail, it prints a failure message and exits.
tries=1
while tries<=3:
    tries+=1
    num=input("Enter your password:")
    if(num=="my_password"):
        print("You entered the correct password")
        break
else:
    print("Sorry you entered wrong password 3 times try again tomorrow!")