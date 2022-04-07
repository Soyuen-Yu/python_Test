import random
sum = 0
array = [[0]*5 for i in range (5)]
for i in range(5) :
    for j in range(5) :
        array[i][j]=random.randrange(1,25)
        sum+=array[i][j]

for i in range(5) :
    print(array[i])

sum = sum/25

if(sum>=12.5) :
    print('Big')
else :
    print('Small')