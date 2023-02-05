import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        a[i] = a[i] + i + 1
    a.sort()
    total = 0
    cnt = 0
    for i in range(n):
        if total + a[i] <= c:
            total += a[i]
            cnt += 1
        else:
            break
    print(cnt)
