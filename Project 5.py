# This program checks whether a number is even or odd using a one-line conditional.
# It uses tuple indexing: ("odd", "even")[num % 2 == 0].
# If num % 2 == 0 is True, it prints "even"; otherwise, it prints "odd".
num=int(input("Please enter a number:"))
result=("odd","even")[num%2==0]
print(result)