array = [[0]*5 for i in range(3)]
array[0] = [5,8,10,6,4]
array[1] = [11,20,1,13,2]
array[2] = [7,9,14,22,3]

for i in range(3) :
    for j in range(5) :
        print('%2d' %array[i][j],end='   ')
    print()