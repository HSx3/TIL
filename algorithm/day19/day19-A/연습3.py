# 0DEC
# 0 2
# 0269FAC9A0
# 1 1 7 8 0

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

code = [[[[[[0 for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]
code[0][0][1][1][0][1] = 0
code[0][1][0][0][1][1] = 1
code[1][1][1][0][1][1] = 2
code[1][1][0][0][0][1] = 3
code[1][0][0][0][1][1] = 4
code[1][1][0][1][1][1] = 5
code[0][0][1][0][1][1] = 6
code[1][1][1][1][0][1] = 7
code[0][1][1][0][0][1] = 8
code[1][0][1][1][1][1] = 9

def aToh(c):
    if c <= '9' : return ord(c) - ord('0')
    else : return ord(c) - ord('A') + 10

def makeT(x):
    global pos
    for i in range(4):
        t.append(asc[x][i])

t = []
arr = "0269FAC9A0"

ans = []
pos = -1

for i in range(len(arr)):
       makeT(aToh(arr[i]))

# 뒤에서 1 찾기
for i in range(len(t)-1, -1, -1):
    if t[i] == 1:
        pos = i
        break

while pos - 6 > 0:
    x = code[t[pos-5]][t[pos-4]][t[pos-3]][t[pos-2]][t[pos-1]][t[pos]]
    ans.append(x)
    pos -= 6

for i in range(len(ans)):
    print(ans.pop(), end=" ")
print()
