from random import choice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
lottery = []
my_ticket = ['a', 'a', 5, 7]
loop_count = 0

def roll():
    for i in range(0, 4):
        lottery.append(choice(numbers))
    print(lottery)

while my_ticket != lottery:
    roll()
    loop_count += 1
    if my_ticket != lottery:
        lottery = []
    else:
        print("We got it.")
        print(f"It takes {loop_count} counts.")



