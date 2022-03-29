colors = ['red','yellow','blue']
print(colors)

colors.sort() #리스트를 구성하는 항목들을 정렬
print(colors)

colors.reverse() #리스트를 구성하는 항목들을 거꾸로 정렬
print(colors)

print(colors.pop()) #리스트의 맨 마지막 항목을 리턴한 뒤, 삭제
print(colors)

colors.remove('red') #리스트에서 해당 요소를 삭제
print(colors)

print(colors.count('yellow')) #리스트에서 해당 요소의 개수를 리턴