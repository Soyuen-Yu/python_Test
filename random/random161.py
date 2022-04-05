import random

print('두 정수를 입력하세요 : ',end='')

num = list(input().split(' '))

for i in range(len(num)) :
    num[i]=int(num[i])

num.sort()

if(num[1]-num[0] <= 1) :
    print('no integer between two numbers')
else :
    print(random.randrange(num[0], num[1]))