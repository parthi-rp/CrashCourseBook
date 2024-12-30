prompt = "Welcome to the cinema. Please enter your age: \n"
prompt += "Enter 'quit' to end.\n"

ticket_price = 0
active = True

while active:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            age = int(age)
            ticket_price += 0
        elif age < 12:
            ticket_price += 10
        elif age > 12:
            ticket_price += 15
        else:
            "Please enter valid input."

        print(f"Your total ticket costs: ${ticket_price}. Want to add more?.")
    print("Enjoy your cinema.")