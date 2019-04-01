import sys
sys.stdin = open("(5201)컨테이너운반_input.txt")
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  #컨테이너, 트럭
    w = list(map(int, input().split())) #화물무게
    t = list(map(int, input().split())) #트럭용량
    w.sort(reverse=True)
    t.sort(reverse=True)
    c = 0;
    total = 0;
    for i in range(M):
        while  c < N and w[c] > t[i] :            # 컨테이너 C가 트럭 i의 적재용량보다 크면
            c += 1                                   # 다음 컨테이너 비교
        if c < N:
            total += w[c]                           # 적재용량 이내면 운반
            c += 1
        else:
            break
    print('#{} {}'.format(tc, total))