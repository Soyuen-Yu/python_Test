num = list((input('세 수를 입력하세요. 공백으로 세 수를 구분합니다. : ').split(' ')))

for i in range(len(num)) :
    num[i]=int(num[i])

num.sort()

print('가장 큰 숫자는 {}, 중간 숫자는 {}, 가장 작은 숫자는 {}입니다.'.format(num[0],num[1],num[2]))