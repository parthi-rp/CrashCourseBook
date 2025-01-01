class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}.")
        print(f"The restaurant type is {self.type}.")

    def open_restaurant(self):
        print(f"The restaurant is open now.")

class IceCreamStand(Restaurant):

    """A simple attempt to model a specific kind of restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to icecream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'chocolate', 'pistachio']

    def display_flavors(self):
        """A method to print the flavors."""
        print(f"\nThe available flavors are:")
        for flavor in self.flavors:
            print(f"\t\t{flavor}")

my_restaurant = IceCreamStand('aa', 'ss')
my_restaurant.display_flavors()
