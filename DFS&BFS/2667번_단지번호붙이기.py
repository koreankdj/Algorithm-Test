from collections import deque

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
       
# 상 하 좌 우 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 했는지 확인
visit = [[0] * (n+1) for _ in range(n+1)]

dan = 0
count = 1

lists = []

def bfs(x, y, lists):

    global dan
    global count
    count = 0
    
    # graph 1이고 방문한 적이 없는 경우에만 확인. 단지수를 쉽게 확인하기 위함임
    if graph[x][y] == 1 and visit[x][y] == 0:
        dan += 1
        count = 1
        q = deque()
        q.append((x,y))
        
        visit[x][y] = 1
        
        while q:
            (x, y) = q.popleft()
            
            # 상, 하, 좌, 우로 1과 처음 방문한 곳이 있는지 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i] 
                
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny] == 1 and visit[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
                    # x = nx
                    # y = ny
                    count += 1
    
    if count > 0:
        # 숫자가 있는 경우             
        lists.append(count)
        
    return lists

for i in range(n):
    for j in range(n):
        bfs(i, j, lists)

print(len(lists))
lists.sort()

for l in lists:
    print(l)