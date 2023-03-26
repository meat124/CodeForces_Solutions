import sys
input = sys.stdin.readline


def Solve(n, k):
    if n == 0:
        return []
    if k < n:
        cur = [-1]*n
        if k > 0:
            cur[k - 1] = 200
        cur[k] = -400
    else:
        cur = Solve(n - 1, k - n)
        cur.append(1000)
    return cur


for t in range(int(input())):
    n, k = map(int, input().split())
    result = Solve(n, k)
    print(*result)
