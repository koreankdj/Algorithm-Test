import sys
n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    numbers.append(list(map(int, sys.stdin.readline().split())))
    
numbers.sort(key = lambda x: (x[0], x[1]))

for number in numbers:
    print(number[0], number[1])