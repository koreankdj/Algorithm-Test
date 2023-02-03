# 백준 알고리즘 그리디 알고리즘 - 11399번 ATM

num = int(input())
l1 = list(map(int, input().split()))

l1.sort()
sum = 0

for k in range(num):
    sum += l1[k] * (num-k)
    
print(sum)
