print('세 정수를 입력하세요 : ', end='')
num = list((input().split(' ')))

for i in range(len(num)) :
    num[i]=int(num[i])

print(min(num))
