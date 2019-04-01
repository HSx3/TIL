import sys
sys.stdin = open('(5203)베이비진게임_input.txt', 'r')
T = int(input())

def game():
    card1 = [0 for i in range(10)]
    card2 = [0 for i in range(10)]
    for i in range(12):
        n = lst[i]
        if i % 2 == 0:  # player1
            card1[n] += 1
            if card1[n] == 3:  # triplet 검사
                return 1
            if run_test(card1) == 1:  # run_test 검사
                return 1
        else:  # player2
            card2[n] += 1
            if card2[n] == 3:  # triplet 검사
                return 2
            if run_test(card2) == 1:  # run_test 검사
                return 2
    return 0  # 승자가 없는 경우


def run_test(card):
    for i in range(8):
        if card[i] >= 1 and card[i + 1] >= 1 and card[i + 2] >= 1:
            return 1

for tc in range(T):
    lst = list(map(int, input().split()))  # 12장의 카드 정보

    print('#{} {}'.format(tc + 1, game()))

