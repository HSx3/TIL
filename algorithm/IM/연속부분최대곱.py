import sys
sys.stdin = open("연속부분최대곱.txt")

N = int(input())
data = []
for i in range(N):
    data.append(float(input()))
'''
data_mul = data[0]
max_mul = data[0]

for i in range(1, len(data)):
    data_mul = max(data_mul*data[i], data[i])
    max_mul = max(data_mul, max_mul)

print('%.3f' % max_mul)

'''

start = 1
max_mul = 0

for i in range(len(data)):
    start = 1
    for j in range(i, len(data)):
        start = start*data[j]
        if max_mul < start:
            max_mul = start
print('%.3f' % max_mul)