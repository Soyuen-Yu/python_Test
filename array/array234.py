string = input('Enter the sentence : ')
count = len(string)-1
j=0
a=0
for i in range(count) :
    if(string[i]!=string[count-j]) :
        a+=1
    j+=1

if(a==0) :
    print('handsome')