i=1
sum=0
while True :
    if(i%2==1) :
        sum+=i
    else :
        sum-=i
    
    if(sum>=100) :
        print('마지막 숫자는 : ',i)
        break
    
    i+=1
