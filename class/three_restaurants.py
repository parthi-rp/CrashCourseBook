class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.name}.")
        print(f"The restaurant type is {self.type}.")

    def open_restaurant(self):
        print(f"\nThe restaurant is open now.")

my_restaurant1 = Restaurant('Aadhiraa', 'Veg')
my_restaurant2 = Restaurant('Vithu', 'non-veg')
my_restaurant3 = Restaurant('Pp', 'Hybrid')
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()
my_restaurant1.open_restaurant()