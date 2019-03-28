import sys
sys.stdin = open("반복문자지우기_input.txt")

N = int(input())
for test_case in range(N):
    data = list(input())
    # print(data)

    check = data[:]
    for i in range(len(data)):
        for i in range(len(check)-1):
            if check[i] == check[i+1]:
                check.pop(i)
                check.pop(i)
                check = check
                break
        # print(check)

    print(f'#{test_case+1} {len(check)}')
