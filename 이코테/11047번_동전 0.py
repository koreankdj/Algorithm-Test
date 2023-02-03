n, k = map(int, input().split())
values = []

for _ in range(n):
    values.append(int(input()))
    
values.reverse()
count = 0

for value in values:
    if k == 0:
        break
    
    # = 빼먹어서 고생함.
    if k >= value:
        count += k // value
        k %= value
    
print(count)