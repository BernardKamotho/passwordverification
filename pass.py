import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return "Must be eight characters"

    elif not re.search("[a-z]", password):
        return "Must have at least one small letter"

    elif not re.search("[A-Z]", password):
        return "Must have at least one capital letter"

    elif not re.search("[0-9]", password):
        return "Must have at least one number"

    elif not re.search("[_@#$]", password):
        return "Must have at least one symbol"

    else:
        common_patterns = [
            r'(?i)password',
            r'(?i)123456',
            r'(?i)qwerty',
            r'(?i)admin',
            r'(?i)root',
            # Add more common patterns as needed
        ]
        
        for pattern in common_patterns:
            if re.search(pattern, password):
                return "Password too Simple"
        
        # If all criteria are met, return "Password correct"
        return "Password Correct - Strong Password"

# Example usage:
password = input("Enter your password: ")
print(check_password_strength(password))
