array = [[0]*4 for i in range (4)]

for i in range(0,16) :
    array[i//4][i%4] = i

for i in range(4) :
    print(array[i])