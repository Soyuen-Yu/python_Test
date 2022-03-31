col = list(input('좌표를 입력하세요 : ').split(','))

for i in range(len(col)) :
    col[i] = int(col[i])

if(50<col[0]<100) :
    if(40<col[1]<80) :
        print('사각형 안에 있습니다.')
    else :
        print('사각형 밖에 있습니다.')
else :
    print('사각형 밖에 있습니다.')