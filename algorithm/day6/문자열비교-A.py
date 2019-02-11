def BruteForce(p, t):
    i = 0 #t의 인덱스
    j = 0 #p의 인덱스
    M = len(p) #찾을 패턴의 길이
    N = len(t) #전체 텍스트의 길이
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1

    if j == M : return 1 #검색 성공
    else : return 0         #검색 실패

import sys
sys.stdin = open("문자열비교_input.txt")

T = int(input())

for test_case in range(1, T + 1):
    pattern = input()
    text = input()

    print("#{} {}".format(test_case, BruteForce(pattern, text)))