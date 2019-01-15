import sys
sys.stdin = open("bus_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    print(data)
    bus_stop = 0
    recharge = 0