def SelectionSort(ary, s, e):
    mini = s
    if s == e:
        return
    for j in range(s+1, e, 1):
        if ary[j] < ary[mini]:
            mini = j
    ary[s], ary[mini] = ary[mini], ary[s]

    SelectionSort(ary, s+1, e)

A = [5, 1, 3, 2, 4]
s = 0
e = len(A)
SelectionSort(A, s, e)
print(A)