import sys
sys.stdin = open("sum_input.txt")
T = int(input())
for test_case in range(1, T + 1):
# for test_case in range(1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    sums_max = 0
    sums_min = 987654321
    ans = 0
    # print(len(data))
    for i in range(N-M+1):
        sums = 0
        for j in range(M):
            sums += data[i+j]
        if sums_min > sums:
            sums_min = sums
        if sums_max < sums:
            sums_max = sums
    ans = sums_max - sums_min
    print("#{} {}".format(test_case, ans))


            # for_sum.append(data[i+j])
            # if i+j % 3 == 2:
            # for_sum.append(sum(data[:M:1]))

            # for_sum.append(data[i+j])

            # for_sum.append(sum(data[i+j:M]))
    # print(for_sum)





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