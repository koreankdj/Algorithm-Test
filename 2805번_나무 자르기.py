import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)

# 이진 탐색 구현
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    
    for i in arr:
        # 크다면 잘라서 더하기
        if i > mid:
            total += i - mid
        
    # 부족한 경우    
    if total < m:
        end = mid - 1
    # 충분한 경우
    else:
        result = mid
        start = mid + 1

print(result)