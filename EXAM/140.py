str1 = "This is my best"
str2 = "Do your best"
str1 = set(str1.split(' '))
str2 = set(str2.split(' '))

print(str1.intersection(str2))