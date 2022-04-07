data = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
data = list(data)

string = list(input('Enter the sentence : ').upper())

for i in data :
    if not(i in string) :
        print(i, end='')