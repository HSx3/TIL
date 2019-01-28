def binarySearch(a, key, page):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        cnt += 1
        if key == a[middle]: #검색성공
            return cnt
        elif key < a[middle] :
            end = middle
        else:
            start = middle
    #return False # 검색실패

import sys
sys.stdin = open("이진탐색_input.txt")
T = int(input())

arr = [0] * 1001
for i in range(1, 1001):
    arr[i] = i

for t in range(1, T+1):
    ans = '0'
    P, A, B = map(int, input().split())

    a = binarySearch(arr, A, P)
    b = binarySearch(arr, B, P)

    if(a > b): ans = 'B'
    elif(a < b) : ans = 'A'
    else: ans = '0'

    print("#{} {}".format(t, ans))