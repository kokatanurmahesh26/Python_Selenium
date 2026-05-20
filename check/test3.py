import re

def validate_username(username):
    if not username:
        return "Username cannot be empty"

    if not re.match(r'^[A-Za-z][A-Za-z0-9]{4,11}$', username):
        return "Invalid username format"

    return "Valid username"

    user_input = input("Enter username: ")
result = validate_username("Nishi")
print(result)