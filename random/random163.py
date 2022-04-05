import random

num = random.randrange(1,2)

user = int(input('level1 (1~2) : '))

if(user == num) :
    print('Correct!')

    num = random.randrange(1,4)
    user = int(input('level2 (1~4) : '))

    if(user == num) :
        print('Correct!')
        
        num = random.randrange(1,8)
        user = int(input('level3 (1~8) : '))

        if(user == num) :
            print('Lucky!')
        else :
            print('Failure!\nAnswer is : {}'.format(num))
    else :
        print('Failure!\nAnswer is : {}'.format(num))
else :
    print('Failure!\nAnswer is : {}'.format(num))