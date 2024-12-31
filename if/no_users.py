user_name = []

if user_name:
    for user in user_name:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello, {user}. Welcome to the website. Thank you {user} for logging in again.")
else:
    print("We need to find some users.")