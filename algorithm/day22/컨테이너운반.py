import sys
sys.stdin = open("컨테이너운반_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N : 컨테이너 수 / M : 트럭 수
    cw = list(map(int, input().split()))    # cw : 화물무게
    lc = list(map(int, input().split()))    # lc : 적재용량

    cw = sorted(cw)
    lc = sorted(lc)
    weight = 0

    while len(cw) != 0 and len(lc) != 0:
        if cw[-1] <= lc[-1]:
            weight += cw[-1]
            cw.pop()
            lc.pop()
        elif cw[-1] > lc[-1]:
            cw.pop()
    print('#{} {}'.format(test_case, weight))