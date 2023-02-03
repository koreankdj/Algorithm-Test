k = int(input())
num = list(map(int, input().split()))
sum = [num[0]]

for i in range(len(num) - 1):
    sum.append(max(sum[i] + num[i + 1], num[i + 1]))

print(max(sum))
