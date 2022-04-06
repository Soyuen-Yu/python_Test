num = int(input('Enter the number : '))
a = (num+5)%7

for i in range(a) :
    if(num+2*i) % 2 ==0 :
        num = (num+i)//2
    else :
        num +=1

print('result : ',num)