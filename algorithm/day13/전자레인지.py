import sys
sys.stdin = open("전자레인지.txt")
T = int(input())
A = 300
B = 60
C = 10
count_A = 0
count_B = 0
count_C = 0

if T % 10:
    print('-1')

else:
    while T != 0:
        if T >= A:
            T = T-A
            count_A += 1
        else:
            if T >= B:
                T = T-B
                count_B += 1
            else:
                if T >= C:
                    T = T-C
                    count_C += 1
                    if T == 0:
                        break
    print(count_A, count_B, count_C)


'''
T=int(input())
A = T//300
T %= 300
B = T//60
T %= 60
C = T//10
T %= 10
if T:
    print(-1)
else:
    print(A, B, C)
'''