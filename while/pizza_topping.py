prompt = "\nPlease enter the topping you want to add to your pizza. \n"
prompt += "(Please enter 'quit' to stop.)\n"

topping = ''
while topping != 'quit':

    topping = input(prompt)


    if topping != 'quit':
        print(f"\nAdding {topping.title()} to your pizza.")
