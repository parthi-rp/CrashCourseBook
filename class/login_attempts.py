class User:
    """A simple attempt to create a user model."""
    def __init__(self, first_name, last_name):
        """Initialize the attributes to model the user info."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """A method to describe the username by print."""
        print(f"\nThe user's name is {self.first_name} {self.last_name}.")

    def greet_user(self):
        """A method to greet the user by print."""
        print(f"\nHello {self.first_name} {self.last_name}. Welcome onboard.")

    def increment_login_attempts(self):
        """A method that increase the login by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """A method that resets the value of the login to 0."""
        self.login_attempts = 0


user1 = User('Parthi', 'ban')
user2 = User('Vithu', 'Pp')
user3 = User('Aadhiraa', 'Pp')

user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(f"\nThe number of login attempts by the user: {user3.login_attempts}")
user3.reset_login_attempts()
print(f"\nThe login attempts of the user reset now. The current login attempts are: {user3.login_attempts}")