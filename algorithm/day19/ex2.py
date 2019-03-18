# 0F97A3
# 01D06079861D79F99F

asc = [[0, 0, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 1, 0, 0],
       [0, 1, 0, 1],
       [0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 0, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 1, 0],
       [1, 1, 1, 1]]

def aToh(c):
    if c <= '9': return ord(c) - ord('0')
    else: return ord(c) - ord('A') + 10

def makeT(x):
    global pos
    for i in range(4):
        t.append(asc[x][i])

t = []
arr = "0F97A3"
for i in range(len(arr)):
    makeT(aToh(arr[i]))

for i in range(len(t)):
   print(t[i], end='')
print()

n = 0
for i in range(len(t)):
    n = n * 2 + t[i]
    if i % 7 == 6:
        print(n, end=", ")
        n = 0
if i % 7 != 6:
    print(n)