def check_input_is_empty(input_str):
    return len(input_str.strip()) == 0

# Example usage:
user_input = input("Enter something: ")
if check_input_is_empty(user_input):
    print("Input is empty.")
else:
    print("Input is not empty.")
    