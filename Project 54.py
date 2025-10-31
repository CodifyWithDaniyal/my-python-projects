#Rock,Paper and Scissors game
a="Welcome to Rock,Paper and Scissors game"
print(a.center(78,"-"))
uc=input("Enter your choise e.g Rock,Paper or Scissors:")
import random
ran=random.randint(0,2)
li=["Rock","Paper","Scissors"]
l=li[ran]
if (l==uc):
    print(f"Its a Draw because you choosed {l} and computer also choosed {l}")
elif(l=="Rock" and uc=="Scissors" or l=="Paper" and uc=="Rock"):
    print(f"You lose because you choosed {uc} and computer choosed {l}")
else:
    print(f"You won because you choosed {uc} and computer choosed {l}")