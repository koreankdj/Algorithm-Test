# 이분 탐색 문제\
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()

def binary(i):
    first = 0
    end = n-1
    
    while first <= end:
        mid = (first + end) / 2
        if arr1[mid] == i:
            return True
        if i < arr1[mid]:
            end = mid - 1
        elif i > arr1[mid]:
            first = mid + 1
            
for i in range(m):
    if binary(arr2[i]):
        print(1)
    else:
        print(0)