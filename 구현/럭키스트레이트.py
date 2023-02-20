# 한 자리씩 입력 받는 법(제발 암기)

number = input()
num_list = list(map(int, str(number)))

n1 = 0
n2 = 0

for i in range(len(num_list)):
    if i < len(num_list) // 2 :
        n1 += num_list[i]
    else:
        n2 += num_list[i]
        
# 책에서는 결과 변수(int형)를 하나 정하고, 중간까지 더하고 그 뒤로는 빼줘서 0이랑 비교.

if n1 == n2:
    print("LUCKY")
else:
    print("READY")