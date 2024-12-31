current_users = ['pp', 'vithu', 'aadhiraa', 'kavi', 'mani']
new_users = ['PP', 'aadhiraa', 'mom', 'dad','aa' ]

for user in new_users:
    if user in current_users:
        print("Sorry, the username is already taken.")
    else:
        print("The username is available.")