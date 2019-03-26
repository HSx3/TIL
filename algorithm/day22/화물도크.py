import sys
sys.stdin = open("화물도크_input.txt")

def check(data):
    schedule = [0] * 24
    count = 0
    for i in range(len(data)):
        if 1 in schedule[data[i][0]:data[i][1]]:
            pass
        else:
            count += 1
            for j in range(data[i][0], data[i][1]):
                schedule[j] += 1
    return count

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = []
    for i in range(N):
        s, e = map(int, input().split())
        data.append((s, e))
    data.sort(key=lambda x:x[1])

    print('#{} {}'.format(test_case, check(data)))

'''
def myprint(n):
    global for_answer
    count = 0
    schedule = [0] * 24

    for i in range(len(data)):
        if 1 in schedule[data[i][0]:data[i][1]]:
            pass
        else:
            count += 1
            for j in range(data[i][0], data[i][1]):
                schedule[j] += 1

    for_answer.append(count)

def perm(n, k):
    if n == k:
        myprint(n)
    else:
        for i in range(k, n):
            data[i], data[k] = data[k], data[i]
            perm(n, k+1)
            data[i], data[k] = data[k], data[i]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = []
    for_answer = []
    for i in range(N):
        s, e = map(int, input().split())
        data.append((s, e))
    perm(len(data), 0)

    print('#{} {}'.format(test_case, max(for_answer)))
'''