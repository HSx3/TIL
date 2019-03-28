import sys
sys.stdin = open("이진탐색_input.txt")

def binarySearch(P, A, B):
    start = 1
    count_A, count_B = 0, 0
    end = P
    pages = list(range(P))

    while start <= end:
        middle = (start + end) // 2
        if A == pages[middle]:
            count_A += 1
            break
        elif A < pages[middle] :
            count_A += 1
            end = middle - 1
        else:
            count_A += 1
            start = middle + 1

    start, middle, end = 0, 0, P
    while start <= end:
        middle = (start + end) // 2
        if B == pages[middle]:
            count_B += 1
            break
        elif B < pages[middle] :
            count_B += 1
            end = middle - 1
        else:
            count_B += 1
            start = middle + 1

    if count_A > count_B:
        return 'B'
    elif count_A == count_B:
        return 0
    else:
        return 'A'


T = int(input()) # input line1
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    print(f'#{test_case} {binarySearch(P, A, B)}')
