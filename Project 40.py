# This code checks if the input number 'a' is prime. 
# It does so by testing divisibility from 2 up to a-1. 
# If any number divides 'a' evenly, it prints "Not a prime" and stops. 
# If no divisors are found, it prints "prime".

a=int(input("Enter your number"))
for i in range(2,a):
    if(a%i==0):
        print("Not a prime")
        break
else:
     print("prime")