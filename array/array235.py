num = input('enter the two number : ').split()
array=[]
for i in range(10) :
    if(i==0)or(i==1) :
        array.append(int(num[i]))
    else :
        array.append((array[i-1]*array[i-2])%10)

print(array)