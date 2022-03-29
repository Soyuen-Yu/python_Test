#in 연산자는 해당 요소가 리스트안에 존재하는지 검색한 뒤, True 또는 False로 결과값을 반환한다. 

colors = ['red', 'yellow', 'blue']
print(colors)

print('yellow의  위치', colors.index('yellow'))
print('blue의 위치', colors.index('blue'))
print()

colors.append('purple')
print(colors)

colors.insert(2,'pink') #해당 index값 위치에 요소를 삽입

colors.extend(['white','black'])
print(colors)

bool='red' in colors
print(bool)

bool='orange' in colors
print(bool)