print("The deli has run out of pastrami.")
sandwich_orders = ['chicken', 'egg','pastrami', 'veggies', 'beef','pastrami', 'tuna', 'pastrami']
finished_sandwiches = []
active = True

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order.title()} sandwich. ")

    finished_sandwiches.append(current_order)
print("\nThe following is the list of sandwiches made:")
for item in finished_sandwiches:
    print(f"\t{item.title()}")

print(sandwich_orders)
print(finished_sandwiches)