def process_solution(a, k, sum):
    if sum != 10 : return
    global cnt

    for i in range(1, k+1):
        if a[i] : print(data[i], end=" ")
    print()
    cnt += 1

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input, sum):
    if sum > 10 : return  #가지치기

    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k, sum) #답이면 원하는 작업을 한다.
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            if a[k]: #가지치기
                backtrack(a, k, input, sum + data[k])
            else:
                backtrack(a, k, input, sum)
    total_cnt += 1
    
MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 10, 0)
print(f"count:{cnt}")
print(f"total_count:{total_cnt}")