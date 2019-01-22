import sys
sys.stdin = open("특별한 정렬_input.txt")

def select(data):
    k = len(data)
    for i in range(0, k):
        maxIndex = i
        if maxIndex % 2 == 0:
            for j in range(i+1, len(data)):
                if data[maxIndex] < data[j]:
                    maxIndex = j
            data[i], data[maxIndex] = data[maxIndex], data[i]

        else:
            for j in range(i+1, len(data)):
                if data[maxIndex] > data[j]:
                    maxIndex = j
            data[i], data[maxIndex] = data[maxIndex], data[i]
    return ' '.join(str(i) for i in data[0:10])

T = int(input()) # input line1
for test_case in range(1, T + 1):
    N = int(input())  # 줄 수
    data = list(map(int, input().split()))
    print(f'#{test_case} {select(data)}')
