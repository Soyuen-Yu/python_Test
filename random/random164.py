import random

cars = ['Hyundai', 'Kia', 'BMW', 'Benz']
print('original : {}'.format(cars))

random.shuffle(cars)
print('change   : {}'.format(cars))
if(cars[0]=='Hyundai') :
    print('True')
else :
    print('False')
