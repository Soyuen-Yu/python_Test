a = int(input('Enter the 1st number : '))
b = int(input('Enter the 2st number : '))

if a>b :
    temp = a
    a = b
    b = temp 

sum = 0

for i in range(a, b) :
    if(i%3==0) :
        sum+=i

print(a,'부터',b,'까지의 3의 배수의 합은? : ',sum)