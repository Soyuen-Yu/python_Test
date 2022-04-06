from ast import Num
import random

num=[]

for i in range(4) :
    num.append(random.randrange(10,20))

avg = sum(num)/4

print(num)

if(avg >= 15) :
    print('Big')
else :
    print('Small')