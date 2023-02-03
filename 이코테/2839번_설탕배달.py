# 큰 수로 나누기 위해서는 작은수로 계속 빼가면서 큰 수의 배수를 찾는 과정이 필요하다.
# while 뒤에 else 쓰는 것도 너무 오랜만이라 착각했음

sw = int(input())

cnt = 0
while sw >= 0:
    if sw % 5 == 0:
        cnt += sw // 5
        print(cnt)
        break
    sw -= 3
    cnt += 1
else:
    print(-1)
    
