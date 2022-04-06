num1=int(input('Enter the 1st number : '))
num2=int(input('Enter the 2st number : '))

if(num1>num2) :
    temp=num2
    num1=num2
    num2=temp

sum = 0

for i in range(num1, num2+1) :
    if(i%2==0) :
        print('-',i,end=' ')
        sum-=i
    else :
        print('+',i,end=' ')
        sum+=i

print('\n=',sum )