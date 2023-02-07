n = int(input())
m = int(input())

# 처음에 []안에 0 넣어서 dfs 안에 cnt가 하나씩 계속 늘었음
coms = [[] * n for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    coms[a].append(b)
    coms[b].append(a)

cnt = 0
visit_list = [0] * (n + 1)

def dfs(x):
    global cnt
    visit_list[x] = 1
    
    for i in coms[x]:
        if visit_list[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)
