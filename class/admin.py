from user import User
class Privileges:
    """A simple class to store the list of admin privileges."""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """A method that list administrator's privileges."""
        print(f"\nThe privileges of the admin are: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(User):
    """A simple attempt to model the admin."""

    def __init__(self, first_name, last_name):
        """Initialize the admin attributes."""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()



