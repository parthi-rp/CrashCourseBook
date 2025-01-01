class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}.")
        print(f"The restaurant type is {self.type}.")

    def open_restaurant(self):
        print(f"The restaurant is open now.")
