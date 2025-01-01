class User:
    """A simple attempt to model the users."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"\nThe user's name is {self.first_name} {self.last_name}.")

    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name}. Welcome onboard.")
