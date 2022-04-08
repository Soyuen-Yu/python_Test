array = input('Enter the number : ').split()
num=[0]*10

for i in range(len(array)) :
    if(array[i]=='1') :
        num[0]+=1
    elif(array[i]=='2') :
        num[1]+=1
    elif(array[i]=='3') :
        num[2]+=1
    elif(array[i]=='4') :
        num[3]+=1
    elif(array[i]=='5') :
        num[4]+=1
    elif(array[i]=='6') :
        num[5]+=1
    elif(array[i]=='7') :
        num[6]+=1
    elif(array[i]=='8') :
        num[7]+=1
    elif(array[i]=='9') :
        num[8]+=1
    elif(array[i]=='10') :
        num[9]+=1
    else :
        print('error!')

for i in range(10) :
    print(i+1,'의 개수 : ',num[i])