"""
Q : 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력 : 
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력 :
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
"""

from cv2 import sort


def search(target, arr, start, end) :
    if start > end :
        return 0
    
    m = (start+end)//2

    if target == arr[m] : 
        return arr[start:end+1].count(target)
    elif target < arr[m] :
        return search(target, arr, start, m-1)
    else :
        return search(target, arr, m+1, end)
    


numN = int(input("상근이가 가지고있는 숫자 카드의 개수 : "))
arrN = list(map(int, input("숫자 카드에 적혀있는 정수 : ").split()))

arrN.sort()

numM = int(input("구분해야 할 숫자 카드의 개수 : "))
arrM = list(map(int, input("숫자 카드에 적혀있는 정수 : ").split()))

N_dictect = {}

for i in arrN :
    start = 0
    end = len(arrN) - 1

    if arrN[i] not in N_dictect :
        N_dictect[i] = search(i, arrN, start, end)

print(' '.join(str(N_dictect[a]) if a in N_dictect else '0' for a in arrM))