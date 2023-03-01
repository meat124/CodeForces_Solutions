import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    pv = [list(map(int, input().split())) for i in range(m)]
    appear = [-1]*(n+m+1)
    cnt = [0]*(n+m+1)
    for i in a:
        appear[i] += 1
    for i in range(m):
        p, v = pv[i]
        cnt[a[p - 1]] += (i + 1) - appear[a[p - 1]]
        appear[a[p - 1]] = -1
        appear[v] = i + 1
        a[p - 1] = v
    for i in range(n + m + 1):
        if appear[i] != -1:
            cnt[i] += m + 1 - appear[i]
            appear[i] = -1
    result = 0
    base = (m*(m+1))//2
    for i in cnt:
        result += base - (m+1-i)*(m-i)//2
    print(result)
