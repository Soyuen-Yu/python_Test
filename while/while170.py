num=[]

num.append(int(input('first num : ')))
num.append(int(input('Second num : ')))

num.sort()

i = (5 - (num[0]%5))+num[0]

while i<num[1] :
    print(i)
    i+=5