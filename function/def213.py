def sumnumber(string) :
    sum=0
    for i in range(0,len(string)) :
        sum+=int(string[i])
        print('+',string[i],end=' ')
    print('=',sum)

    return sum

num = input('Enter the number : ')

data = sumnumber(num)

while True :
    data = sumnumber(str(data))
    if(data<=9) :
        break