people_count = input("How many people are there in your group? ")
people_count = int(people_count)

if people_count > 8:
    print("\nYou have to wait for a table.")
else:
    print("\nYour table is ready.")
