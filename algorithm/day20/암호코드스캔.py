import sys
sys.stdin = open("암호코드스캔_input.txt")

code = [[0, 0, 0, 0],  #0
        [0, 0, 0, 1],  #1
        [0, 0, 1, 0],  #2
        [0, 0, 1, 1],  #3
        [0, 1, 0, 0],  #4
        [0, 1, 0, 1],  #5
        [0, 1, 1, 0],  #6
        [0, 1, 1, 1],  #7
        [1, 0, 0, 0],  #8
        [1, 0, 0, 1],  #9
        [1, 0, 1, 0],  #A
        [1, 0, 1, 1],  #B
        [1, 1, 0, 0],  #C
        [1, 1, 0, 1],  #D
        [1, 1, 1, 0],  #E
        [1, 1, 1, 1]]  #F

# T = int(input())

# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#
#     data =
T = int(input())
for tc in range(1):
    N, M = map(int, input().split())
    # 2진수 저장
    data = []
    for i in range(N):
        a = list(map(str, input()))
        b = ''
        for j in range(len(a)):
            if a[j] <= '9':
                b += ''.join(map(str, code[int(a[j])]))
            else:
                b += ''.join(map(str, code[ord(a[j]) - ord('A') + 10]))
        data.append(list(map(int, b)))
    print(data)