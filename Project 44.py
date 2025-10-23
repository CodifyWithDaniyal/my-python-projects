#Password strength checker
passs=input("Enter your password:")
class TooShortError(Exception):
    pass
if len(passs)<10:
    raise TooShortError("Your password is too short it shouild contain atleast 10 characters")
else:
    print("Your password is strong!")