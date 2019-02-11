import sys

sys.stdin = open("글자수_input.txt")  # 파일에서 입력받는 경우 사용
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    count = dict.fromkeys(str1, 0)  # Dictionary 생성
    # count = {}.fromkeys(str1, 0)

    for ch in str2:                 # str2의 각 글자 확인
        if ch in count:
             count[ch] += 1         # Dictionary에 있는 경우 개수 증가

    print('#{} {}'.format(tc, max(count.values()))) # 최대 개수 출력