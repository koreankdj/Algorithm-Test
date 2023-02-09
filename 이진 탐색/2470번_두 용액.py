n = int(input())

arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr) - 1

# 합이 가장 클 경우 check
answer = 2000000000

result = []
while (start < end):
    s_start = arr[start]
    s_end = arr[end]
    
    sum = s_start + s_end
    
    if abs(sum) < answer:
        answer = abs(sum)
        result = [s_start, s_end]
        
    if sum < 0:
        start += 1
    else:
        end -= 1
        
print(result[0], result[1])