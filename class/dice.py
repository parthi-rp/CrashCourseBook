from random import randint
class Die:
    """A simple attempt to model Dice"""

    def __init__(self, sides=6):
        """Initialize the attributes of Dice"""
        self.sides = sides

    def roll_die(self):
        """Prints a random number b/n 1 and 6"""
        result = randint(1, self.sides)
        print(f"The result is: {result}.")


my_die = Die()
for i in range(1, 11):
    my_die.roll_die()
print("///////////////////////")

my_die = Die(10)
for i in range(1, 11):
    my_die.roll_die()
print("///////////////////////")

my_die = Die(20)
for i in range(1, 11):
    my_die.roll_die()
print("///////////////////////")