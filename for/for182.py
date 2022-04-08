list_num = ['1','2','3','4','5','6','7','8','9','0','.']
a = input()
tmp = a
for x in range(len(list_num)):
    a= str(a)
    a = a.replace(list_num[x],"")
    
if a:
    print(False)
else:
    print(tmp)