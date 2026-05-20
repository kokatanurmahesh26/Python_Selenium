import re

def validate_password(password):
    if len(password) < 8:
        return "Password too short"

    if not re.search(r'[A-Z]', password):
        return "Missing uppercase letter"

    if not re.search(r'[a-z]', password):
        return "Missing lowercase letter"

    if not re.search(r'[0-9]', password):
        return "Missing number"

    return "Valid password"