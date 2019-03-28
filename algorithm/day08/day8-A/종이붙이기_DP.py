import sys

sys.stdin = open('종이붙이기_input.txt', 'r')  # 파일에서 읽는 경우
T = int(input())

m = [1, 1]                          # f(0) = 1, f(1) = 1
for i in range(2, 31):              # 문제의 조건에서 f(30)까지 필요
    m.append(m[i-1] + 2*m[i-2])     # 점화식 f(n) = f(n-1) + 2*f(n-2)

for tc in range (1, T+1):
    N = int(input())//10            # 10의 배수를 종이의 폭으로 나눔
    print('#{} {}'.format(tc, m[N]))