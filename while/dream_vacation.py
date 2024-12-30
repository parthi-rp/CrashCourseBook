responses = {}

polling_active = True

while polling_active:
    name = input("\nPlease enter your name: ")
    response = input("\nIf you could visit one place in the world, where would you go? ")
    responses[name] = response

    repeat = input("Would you like to ask more person? (y/n): ")

    if repeat == 'no':
        polling_active = False

print("--- Test Results ---")
for name, response in responses.items():
    print(f"\n{name.title()} would like to visit {response.title()}")
