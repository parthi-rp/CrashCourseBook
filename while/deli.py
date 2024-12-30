sandwich_orders = ['chicken', 'egg', 'veggies', 'beef', 'tuna']

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order.title()} sandwich. ")

    finished_sandwiches.append(current_order)
print("\nThe following is the list of sandwiches made:")
for item in finished_sandwiches:
    print(f"\t{item.title()}")