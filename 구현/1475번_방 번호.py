k = int(input())

k_list = list(map(int, str(k)))

def solution(a, b):
    if (a + b) % 2 == 0:
        return (a + b) // 2
    else:
        return (a + b) // 2 + 1

number = [0] * 10

for a in k_list:
    number[a] += 1

temp = solution(number[6], number[9])

number[6] = temp
number[9] = temp

max_num = 0
for i in range(10):
    max_num = max(max_num, number[i])

print(max_num)