# n 입력받기
n = int(input())

# 결과 저장 DP 테이블 초기화
d = [0] * 1001

# Dynamic Programming
d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-2] * 2 + d[i-1]) % 796796
    
# 계산된 결과 출력
print(d[n])