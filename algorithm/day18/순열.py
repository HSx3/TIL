def Perm(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            # a[r], a[i] = a[i], a[r]
            a[i], a[n-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            Perm(n-1, r-1, q)
            # a[r], a[i] = a[i], a[r]
            a[i], a[n-1] = a[n-1], a[i]
def myprint(q):
    while q != 0:
        q = q-1
        print(" %d" % (t[q]), end='')
    print("")

t = [0] * 10
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4]

Perm(3, 2, 2)





# def PrintArr(n):
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()
#
# def perm(n, k):
#     if k == n:
#         PrintArr(n)
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(n, k + 1)
#             arr[k], arr[i] = arr[i], arr[k]
#
# arr = [1, 2, 3]
# perm(3, 0)