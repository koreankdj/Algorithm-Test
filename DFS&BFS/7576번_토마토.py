from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
q = deque()

for i in range(n):
    graph.append(list(map(int, input().split())))

# 상, 하, 좌, 우 입력
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

day = 0

# 1인 부분 먼저 찾아서 큐에 넣기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])

# bfs 방식
def tomato():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue      
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
                
tomato()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
    
print(day - 1)