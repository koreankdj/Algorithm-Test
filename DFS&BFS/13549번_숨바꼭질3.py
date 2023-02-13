import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
# 100000 넣으면 런타임 에러 뜬다. 100001 넣어줘야함
road = [0] * 100000

q = deque()
q.append(n)
road[n] = 1

while q:
    x = q.popleft()
    if x == k:
        print(road[k]-1)
        break
    for new in (2*x, x-1, x+1):
        if 0 <= new < 100001 and road[new] == 0:
            if new == 2*x:      # 순간이동 하는 경우는 맨 앞으로 넣어준다
                road[new] = road[x]
                q.appendleft(new)
            else:
                road[new] = road[x] + 1
                q.append(new)