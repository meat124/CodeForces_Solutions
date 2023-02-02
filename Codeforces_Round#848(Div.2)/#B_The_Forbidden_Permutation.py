import sys
input = sys.stdin.readline
MAX = int(1e5 + 5)


def Not_Good(i, d):
    if pos[a[i]] < pos[a[i + 1]] <= pos[a[i]] + d:
        return True
    return False


for t in range(int(input())):
    n, m, d = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    pos = [0]*(n + 1)
    for i in range(n):
        pos[p[i]] = i
    not_good = False
    result = MAX
    for i in range(m - 1):
        if pos[a[i]] >= pos[a[i + 1]] or pos[a[i + 1]] > pos[a[i]] + d:
            result = 0
            break
        gap = abs(pos[a[i + 1]] - pos[a[i]])
        result = min(result, gap)
        if d < n - 1:
            result = min(result, d + 1 - gap)
    print(result)
