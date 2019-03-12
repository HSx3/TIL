def PI(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            PI(n, r-1, q)
            a[i], a[n-1] = a[n-1], a[i]

def myprint(q):
    while q != 0:
        q = q-1
        print(" %d" % (t[q]), end='')
    print("")

t = [0] * 3
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4]

PI(3, 2, 2)
