import re

def check_input_is_email(input_str):
    # Regular expression pattern for email validation
    email_pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    
    # Check if the input string matches the email pattern
    return re.match(email_pattern, input_str) is not None


# Example usage:
user_input = input("Enter an email address: ")
if check_input_is_email(user_input):
    print("Input is a valid email address.")
else:
    print("Input is not a valid email address.")