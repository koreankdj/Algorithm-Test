import sys

n = int(sys.stdin.readline())

words = []
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if word not in words:
        words.append(word)
        
words.sort(key = lambda x : (len(x), x))

for word in words:
    print(word)