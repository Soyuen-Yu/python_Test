def ismulThree(n) :
    if(n%3==0) :
        return True
def ismulFive(n) :
    if(n%5==0) :
        return True
sum = 0
for i in range(0, 100001) :
    if(ismulThree(i) or ismulFive(i) == True) :
        sum+=i

print(sum)