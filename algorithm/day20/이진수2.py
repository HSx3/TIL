import sys
sys.stdin = open("이진수2_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = float(input())
    ans = []
    count = 0

    while N != 0:
        if int(N*2) == 1:
            ans.append(str(int(N*2)))
            N = N*2 - int(N*2)
            count += 1
        elif int(N*2) == 0:
            ans.append(str(int(N*2)))
            N = N*2 - int(N*2)
            count += 1
    print(count)
    print('#{}'.format(test_case), end=" ")
    if count > 12:
        print('overflow')
    else:
        print(''.join(ans))