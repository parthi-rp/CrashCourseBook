number = input("Enter the number to find if it is multiples of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is multiples of 10.")
else:
    print(f"\nThe number {number} is not multiples of 10.")