# This program checks the strength of a password based on its length.
# - If the password has fewer than 10 characters, it raises a custom TooShortError.
# - If the password is 10 characters or longer, it prints a success message indicating the password is strong.
passs=input("Enter your password:")
class TooShortError(Exception):
    pass
if len(passs)<10:
    raise TooShortError("Your password is too short it shouild contain atleast 10 characters")
else:
    print("Your password is strong!")