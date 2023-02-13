# 1697번 : 숨바꼭질
from collections import deque

def bfs():
    q = deque()             
    q.append(n)             
    check[n] = True
    dist[n] = 0
    
    while  q:
        x = q.popleft()     
        
        if x == k:
            print(dist[x])
            break
        if x * 2 <= MAX and check[x*2] == False:        # 순간이동
            q.append(x*2) 
            check[x*2] = True
            dist[x*2] = dist[x]
        if x + 1 <= MAX and check[x+1] == False:
            q.append(x+1)
            check[x+1] = True
            dist[x+1] = dist[x] + 1
        if x - 1 >= 0 and check[x-1] == False:
            q.append(x-1)
            check[x-1] = True
            dist[x-1] = dist[x] + 1
    return 

MAX = 100,000               # 시간초과 안나게 수 제한
check = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)      # 이동하는 거리를 알기 위한 변수
n, k = map(int, input().split())

bfs()
