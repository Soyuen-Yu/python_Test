import random

num = [0,1,2,3]

for i in range(4) :
    num[i] = random.randrange(9,21)

avg = sum(num)/4

print(num)

if(avg >= 15) :
    print('Big')
else :
    print('Small')