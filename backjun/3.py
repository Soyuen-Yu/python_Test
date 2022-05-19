"""
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

입력 : 지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

출력 : 각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.
"""
import collections 
import sys 

input = sys.stdin.readline
 
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

MIIS = lambda: map(int, input().split()) 

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

n, m = MIIS() # n : 세로 m : 가로
arr = list(list(MIIS()) for _ in range(n))  # map : 리스트 안의 요소들을 지정된 함수로 처리해주는 함수로 여기서는 int로 datatype을 변환하는 용도로 사용했다.

for i in range(n): 
    for j in range(m): 
        if arr[i][j] == 2: 
            start_i = i
            start_j = j

visited = [[-1] * m for _ in range(n)] # bfs에서 방문한 곳을 체크하기 위한 배열

q = collections.deque() # bfs 구현을 위한 queue datatype

q.append((start_i, start_j))

visited[start_i][start_j] = 0 

while q: # 큐가 비어있을 때 까지 반복

    i, j = q.popleft() 
    
    for k in range(4): 
        ni, mj = i + directions[k][0], j + directions[k][1] # 해당 위치의 상하좌우 위치를 계산
        
        if 0 <= ni < n and 0 <= mj < m and visited[ni][mj] == -1: # ni값이 2차원배열의 세로 길이보다 작고 mj의 값이 2차원배열의 가로 길이보다 작고 방문하지 않았다면
            if arr[ni][mj] == 1: # 갈 수 있는 땅이면 
                visited[ni][mj] = visited[i][j] + 1 #i와 j에 인접한 땅이므로 해당 땅의 값보다 1 증가시킨다.
                q.append((ni, mj)) 
            elif arr[ni][mj] == 0: # 갈 수 없는 땅이라도 방문 체크 
                visited[ni][mj] = 0 

# 출력 
print("\n")
for i in range(n): 
    for j in range(m): 
        if arr[i][j] == 0: # 원래 갈 수 없는 땅인 위치는 항상 0 출력 
            print(0, end=' ') 
        else: 
            print(visited[i][j], end=' ') 
    print()