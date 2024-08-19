# Initialize an empty list to store the inputs
inputs_list = []

# Keep asking for input until the user types 'done'
while True:
    user_input = input("Enter a value (or type 'done' to finish): ")
    
    if user_input.lower() == 'done':
        break
    else:
        inputs_list.append(user_input)

# Print the list of inputs
print("You entered:", inputs_list)
