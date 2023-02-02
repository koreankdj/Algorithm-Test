import math

num = int(input())

for _ in range(num):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    # 두 원 중심 사이의 거리
    distance = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

    # 두 원의 중심이 같은 경우
    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:       # 두 원의 중심이 다른 경우
        if distance == (r1 + r2) or distance == abs(r1 - r2):
            print(1)
        elif distance < (r1 + r2) and distance > abs(r1 - r2):
            print(2)
        else:
            print(0)
