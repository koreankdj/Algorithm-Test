from collections import deque

n, m = map(int, input().split())

# 상, 하, 좌, 우 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2차원 리스트의 맵 정보 입력받기
mz = []
for i in range(n):
    mz.append(list(map(int, input())))

# BFS 코드
def bfs(x, y):
    # 큐 구현
    q = deque()
    q.append((x, y))
    
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어난 경우 무시
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            # 벽인 경우 무시
            if mz[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 거리 기록
            if mz[nx][ny] == 1:
                mz[nx][ny] = mz[x][y] + 1
                q.append((nx, ny))
                
    return mz[n-1][m-1]



print(bfs(0, 0))