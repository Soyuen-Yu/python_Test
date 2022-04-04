from operator import truediv
from pickle import TRUE


colors = ['red', 'orange', 'blue', 'green', 'white', 'black', 'dark blue', 'purple']

test = input('Enter the color : ')

if((test in colors) == True) :
    print('sorry')
else :
    colors.append(test)
    print(colors)