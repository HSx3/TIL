import sys
sys.stdin = open("minmax_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    minmax = 0
    N = int(input())
    data = list(map(int, input().split()))
    for i in range(len(data) - 1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                minmax = data[-1] - data[0]
    print("#{} {}".format(test_case, minmax))

# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''



'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
# import sys
# sys.stdin = open("sample_input.txt")
# T = int(input())
# # data = list(map(int, input().split()))
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# # for test_case in range(3):
# for test_case in range(1, T + 1):
#     minmax=0
#     result = []
#     N = int(input())
#     data = list(map(int, input().split()))
#     for i in range(len(data) - 1, 0, -1):
#         for j in range(0, i):
#             if data[j] > data[j + 1]:  # > : 작은 것부터, 오름차순 // < : 큰 것부터, 내림차순
#                 data[j], data[j + 1] = data[j + 1], data[j]
#                 minmax = data[-1] - data[0]
#     print("#{} {}".format(test_case, minmax))

    # for i in range(1, len(data)):
    #     for j in range(1, len(data))
    #     result.append(data[i-1] - data[i])
    # print(data)
    # print(minmax)
    # for i in range(1, T*2):

    # test_case = list(map(int, input().split()))
    # print(test_case)

    # print("#{} {}".format(test_case, minmax))

# import sys
#
# sys.stdin = open("view_input.txt")
# T = 10
# for tc in range(10):
#     ans = 0
#     N = int(input())
#     data = list(map(int, input().split()))
#     for i in range(2, len(data) - 1):
#         if data[i] > data[i - 1] and data[i] > data[i - 2] and data[i] > data[i + 1] and data[i] > data[i + 2]:
#             ans += data[i] - max(data[i - 1], data[i - 2], data[i + 1], data[i + 2])
#     print("#{} {}".format(tc + 1, ans))


# 3
# 5
# 477162 658880 751280 927930 297191
# 5
# 565469 851600 460874 148692 111090
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175





