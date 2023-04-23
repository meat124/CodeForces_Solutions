from collections import Counter
import sys
input = sys.stdin.readline


def Get_MEX(A_):
    n = len(A_)
    seen = [False]*(n + 1)
    for x in A_:
        if x < n + 1:
            seen[x] = True
    for i in range(n + 1):
        if not seen[i]:
            return i
    return n + 1


for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    mex = Get_MEX(A)
    # MEX == 0 이면 모든 원소를 0으로 변경하면 가능하다.
    if mex == 0:
        print('YES')
        continue
    l, r = n, -1
    for i in range(n):
        if A[i] == mex + 1:
            l, r = min(l, i), max(r, i)
    cnt = Counter(A)
    result = 'NO'
    # A[i] == mex + 1 인 i 가 존재하지 않았다면
    if l == n and r == -1:
        for a in A:
            # mex 보다 큰 수가 있거나 또는 여분의 변경할 수가 존재하면 mex 로 바꾸면 된다.
            if a > mex or cnt[a] > 1:
                result = 'YES'
        print(result)
    else:
        for i in range(l, r + 1):
            A[i] = mex
        n_mex = Get_MEX(A)
        print('YES') if mex + 1 == n_mex else print('NO')
