import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not email:
        return "Email cannot be empty"

    if not re.match(pattern, email):
        return "Invalid email format"

    return "Valid email"