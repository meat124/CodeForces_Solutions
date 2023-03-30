import sys
input = sys.stdin.readline


def Operation(idx):
    if A[idx] == -1:
        return -2
    for i in range(n):
        if i == idx:
            continue
        while A[i] > A[idx]:
            A[i] = A[i]//A[idx] if A[i] % A[idx] == 0 else A[i]//A[idx] + 1
            result.append([i + 1, idx + 1])
        if A[i] < A[idx]:
            return i
    return -1


for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if A.count(A[0]) == n:
        print(0)
        continue
    result = []
    min_idx = A.index(min(A))
    if A[min_idx] == 1:
        print(-1)
        continue
    flag = False
    nxt_idx = Operation(min_idx)
    while nxt_idx != -1:
        nxt_idx = Operation(nxt_idx)
        if nxt_idx == -2:
            flag = True
            break
    if flag:
        print(-1)
        continue
    print(len(result))
    for i in range(len(result)):
        print(*result[i])
