num = int(input('Enter the number : '))
count = 0
for i in range(2,num) :
    if(num%i==0) :
        count +=1
        break

if(count==0) :
    print(num,'is prime number')
else :
    print(num,'is not prime number')