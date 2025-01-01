class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the restaurant name and type."""
        print(f"The restaurant name is {self.name}.")
        print(f"The restaurant type is {self.type}.")

    def open_restaurant(self):
        """Print a statement to describe if restaurant is open or closed."""
        print(f"The restaurant is open now.")

    def set_number_served(self, number):
        """A method that let you set the number of customers
        that have been served."""
        self.number_served = number

    def increment_number_served(self, number):
        """A method that lets you increment the number
        of customers who've been served."""
        self.number_served += number
        return number


my_restaurant = Restaurant('Aadhiraa', 'Veg')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(23)
increment_number = my_restaurant.increment_number_served(3)
print(f"\nThe total number of customers we served are {my_restaurant.number_served}.")

print(f"\nThe number of customers we served today are {increment_number}")