from random import choice
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
lottery = []

i = 0
while i < 4:
    i += 1
    lottery.append(choice(numbers))

print(lottery)
print(f"The lottery winner is: {lottery[0]}{lottery[1]}{lottery[2]}{lottery[3]}")