def quickSort(start, end, x):
    if start >= end:
        return
    else:
        pivot = end
        target = start

        for left in range(start, end):
            if x[left] < x[pivot]:
                x[target] , x[left] = x[left], x[target]
                target += 1

        x[target] , x[pivot] = x[pivot], x[target]
        quickSort(start, target-1, x)
        quickSort(target+1, end, x)

def mergeSort(s, e):
    if s >= e: return         # 원소 하나 단위로 쪼갰으면 리턴
    m = (s + e)//2
    mergeSort(s, m)           # 왼쪽 쪼개기
    mergeSort(m+1, e)         # 오른쪽 쪼개기
    L, R, T = s, m+1, s
    while L <= m and R <= e:
        if arr[L] < arr[R]:   # 왼쪽 영역이 작으면 왼쪽 영역 값을 임시 버퍼로
            temp[T] = arr[L]
            T += 1
            L += 1
        else:                 # 아니면 오른쪽 값을 임시 버퍼로
            temp[T] = arr[R]
            T += 1
            R += 1
    while L <= m:             # L쪽이 남은경우 그대로 버퍼에 넣기
        temp[T] = arr[L]
        T += 1
        L += 1
    while R <= e:             # R쪽이 남은경우 그대로 버퍼에 넣기
        temp[T] = arr[R]
        T += 1
        R += 1
    for i in range(s, e+1):   # 원본에 복사하기
        arr[i] = temp[i]


# main
N = int(input())
arr = list(map(int, input().split()))
# arr = [30, 24, 19, 17, 8, 6, 11, 18]
# N = len(arr)
temp = [0]*N

mergeSort(0, len(arr)-1)
print(*arr)