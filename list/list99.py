import numbers


numbers = [14.26, 5, 426.3, 0.221]

print(len(numbers)) #리스트에 들어있는 항목의 개수를 리턴
print(max(numbers)) #리스트에 들어있는 항목 중 최대값을 리턴
print(min(numbers)) #리스트에 들어있는 항목 중 최솟값을 리턴
print(sum(numbers)) #리스트에 들어있는 항목들의 합을 리턴
print(sorted(numbers)) #정렬이된 리스트를 리턴

string = 'python'
print(list(string)) #괄호안의 객체를 리스트로 만든다. 