import re

def check_input_follows_pattern(input_str):
    # Define the pattern using regular expression
    pattern = r'^KD[A-Z][0-9]{3}[A-Z]$'
    
    # Check if the input string matches the pattern
    return re.match(pattern, input_str) is not None

# Example usage:
user_input = input("Enter something: ")
if check_input_follows_pattern(user_input):
    print("Input follows the pattern.")
else:
    print("Input does not follow the pattern.")