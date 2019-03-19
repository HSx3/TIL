# 0F97A3
# 000011111001011110100011
# 7 101 116 3

asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F

def aToh(c):
    if c <= '9' : return ord(c) - ord('0')
    else : return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])

t = []
arr = "0F97A3"
for i in range(len(arr)):
       makeT(aToh(arr[i]))

n = 0
for i in range(len(t)):
    n = n * 2 + t[i]
    if i % 7 == 6:
        print(n, end=", ")
        n = 0

if i % 7 != 6 :
    print(n)