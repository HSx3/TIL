def paper(n):
    if n < 2:
        return 1
    else:
        return paper(n-1) + 2*paper(n-2)

import sys
sys.stdin = open("종이붙이기_input.txt")

N = int(input())
for test_case in range(N):
    data = int(input())
    n = int(data/10)
    # print(n)
    print(f'#{test_case+1} {paper(n)}')