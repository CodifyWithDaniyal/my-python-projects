# This program checks whether the entered marks are enough to pass.
# If marks are 40 or above, it prints "Pass"; otherwise, it prints "Fail".
# It uses a one-line conditional expression for simplicity.
mark=int(input("Please enter your marks:"))
print("Pass") if mark>=40 else print("Fail")