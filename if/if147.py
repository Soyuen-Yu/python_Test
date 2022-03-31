score = input('학점을 입력하세요 : ')

if((score=='A') or (score=='B')) :
    print('참 잘했습니다.')
elif((score=='c') or (score=='C')) :
    print('좀 더 노력하세요')
elif(score=='F') :
    print('다음 학기에 다시 수강하세요')
else :
    print('정확하지 않은 학점입니다.')