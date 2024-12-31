car = 'audi'

if car == 'audi':
    print(car)

if car != 'subaru':
    print('wtf')

if car.lower() == 'Audi':
    print('True')
else:
    print('False')

cars = ['audi', 'tesla', 'hyundai', 'honda']

if 'bmw' in cars:
    print('BMW is present.')
if 'bmw' not in cars:
    print('BMW is not present. ')