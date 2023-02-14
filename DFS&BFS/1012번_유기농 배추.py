import sys
from collections import deque
input = sys.stdin.readline

times = int(input())
for _ in range(times):
    n, m, amount = map(int, input().split())

    graph = [[0] * (m+1) for _ in range(n+1)]

    # 방문했는지 확인하는 리스트
    visited = [[0] * (m+1) for _ in range(n+1)]

    for i in range(amount):
        a, b = map(int, input().split())
        graph[a][b] = 1
        
    # 상, 하, 좌, 우 만들기
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 지렁이 개수를 저장할 변수

    ji = 0

    def findji(x, y, visited):
        
        global ji
        
        if graph[x][y] == 1 and visited[x][y] == 0:
            
            ji += 1
            # print("[%d] : [%d][%d]에서 ji 추가됨!" %(ji, x, y))
            
            q = deque()
            q.append((x,y))
            
            visited[x][y] = 1
            
            while q:
                (x, y) = q.popleft()
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx >= n or nx < 0 or ny < 0 or ny >= m:
                        continue
                    if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
                        # print("[%d][%d] 방문함 ! "%(nx,ny))
                        
        return visited
                        
    for i in range(n):
        for j in range(m):
            findji(i, j, visited)
            
    print(ji)