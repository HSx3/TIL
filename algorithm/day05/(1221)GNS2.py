import sys
sys.stdin =open("(1221)GNS_input.txt", "r")
T = int(input())

digit = ["ZRO", "ONE","TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(T):
    temp = input()  #dummy
    data = list(map(str, input().split()))
    count = [0 for _ in range(10)]
    for i in range(len(data)):
        if data[i] == digit[0]: count[0] += 1
        elif data[i] == digit[1]: count[1] += 1
        elif data[i] == digit[2]: count[2] += 1
        elif data[i] == digit[3]: count[3] += 1
        elif data[i] == digit[4]: count[4] += 1
        elif data[i] == digit[5]: count[5] += 1
        elif data[i] == digit[6]: count[6] += 1
        elif data[i] == digit[7]: count[7] += 1
        elif data[i] == digit[8]: count[8] += 1
        elif data[i] == digit[9]: count[9] += 1

    print(f"#{tc+1}", end=" ")
    for i in range(10):
        for j in range(count[i]):
            print(digit[i], end = " ")
    print()
