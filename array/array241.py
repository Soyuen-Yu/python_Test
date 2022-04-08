str1 = list(input('Enter first : '))
str2 = list(input('Enter second : '))

if ((len(str1)) != (len(str2))) :
    print('Not Same')
else :
    str1 = str1.sort()
    str2 = str2.sort()
    if(str1==str2) :
        print('Same')
    else :
        print('Not Same')