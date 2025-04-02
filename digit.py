def check_input_is_digit(input_str):
    return input_str.isdigit()

# Example usage:
user_input = input("Enter a string to check if it's a digit: ")
if check_input_is_digit(user_input):
    print("Input is a digit.")
else:
    print("Input is not a digit.")