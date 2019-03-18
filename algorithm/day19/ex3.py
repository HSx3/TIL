asc = [[0, 0, 0, 0], # 0
       [0, 0, 0, 1], # 1
       [0, 0, 1, 0], # 2
       [0, 0, 1, 1], # 3
       [0, 1, 0, 0], # 4
       [0, 1, 0, 1], # 5
       [0, 1, 1, 0], # 6
       [0, 1, 1, 1], # 7
       [1, 0, 0, 0], # 8
       [1, 0, 0, 1], # 9
       [1, 0, 1, 0], # A
       [1, 0, 1, 1], # B
       [1, 1, 0, 0], # C
       [1, 1, 0, 1], # D
       [1, 1, 1, 0], # E
       [1, 1, 1, 1]] # F

password = [[0,0,1,1,0,1],  #0
            [0,1,0,0,1,1],  #1
            [1,1,1,0,1,1],  #2
            [1,1,0,0,0,1],  #3
            [1,0,0,0,1,1],  #4
            [1,1,0,1,1,1],  #5
            [0,0,1,0,1,1],  #6
            [1,1,1,1,0,1],  #7
            [0,1,1,0,0,1],  #8
            [1,0,1,1,1,1]]  #9

def aToh(c):
    if c <= '9': return ord(c) - ord('0')
    else: return ord(c) - ord('A') + 10

def makeT(x):
    global pos
    for i in range(4):
        t.append(asc[x][i])

t = []
arr = "0DEC"
for i in range(len(arr)):
    makeT(aToh(arr[i]))

for i in range(len(t)):
   print(t[i], end='')
print()

result = []
k = len(t)-1
while k >= 5:
    if t[k] == 1:
        if t[k-5 : k+1] in password:
            result.append(password.index(t[k-5:k+1]))
            k -= 5
    k -= 1

result.reverse()
print(*result)