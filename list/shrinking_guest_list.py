diner_list = ['Kavi', 'Mani', 'Murugan']
print(f'Hello {diner_list[0]}, Welcome to the party!!!')
print(f'Hello {diner_list[1]}, Welcome to the party!!!')
print(f'Hello {diner_list[2]}, Welcome to the party!!!')

print(f"Hello guys! {diner_list[1]} can't make to the dinner.\n ")

diner_list[1] = 'Raja'

print(f'Hello {diner_list[0]}, Welcome to the party!!!')
print(f'Hello {diner_list[1]}, Welcome to the party!!!')
print(f'Hello {diner_list[2]}, Welcome to the party!!!\n')

print(f"Guys! we've found a bigger table. So, more people can join us!\n")
diner_list.insert(0, 'Dinesh')
diner_list.insert(0, 'Ram')
diner_list.append('Gaja')


print(f'Hello {diner_list[0]}, Welcome to the party!!!')
print(f'Hello {diner_list[1]}, Welcome to the party!!!')
print(f'Hello {diner_list[2]}, Welcome to the party!!!')
print(f'Hello {diner_list[3]}, Welcome to the party!!!')
print(f'Hello {diner_list[4]}, Welcome to the party!!!')
print(f'Hello {diner_list[5]}, Welcome to the party!!!\n')

print(f'Sorry guys! we can only take two of you!\n')
print(f"Dear {diner_list.pop()}, sorry for that. We'll see you later!")
print(f"Dear {diner_list.pop()}, sorry for that. We'll see you later!")
print(f"Dear {diner_list.pop()}, sorry for that. We'll see you later!")
print(f"Dear {diner_list.pop()}, sorry for that. We'll see you later!\n")

print(f"Hello, {diner_list[0]}! Sorry for the hiccup. We'll start the party now.")
print(f"Hello, {diner_list[1]}! Sorry for the hiccup. We'll start the party now.")

del diner_list[0]
del diner_list[0]
print(diner_list)