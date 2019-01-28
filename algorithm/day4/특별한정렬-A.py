def find(data):
    for i in range (0, 10): # 10개의 구간까지 정렬
        mIdx = i
        if i % 2 == 0:        		# 구간의 시작이 짝수인 경우 최대값
            for j in range (i+1,N):
                if data[mIdx] < data[j]:
                    mIdx = j
        else:
            for j in range (i+1,N):
                if data[mIdx] > data[j]:
                    mIdx = j
        # t = data[i]            			# 구간의 맨 앞에 최대나 최소를 가져옴
        # data[i] = data[mIdx]
        # data[mIdx] = t
        data[i], data[mIdx] = data[mIdx], data[i]
        
    return 

import sys
sys.stdin = open("특별한정렬_input.txt")
T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    find(data)

    print("#{}".format(t), end=" ")
    for i in range(10):
        print(data[i], end=" ")
    print()