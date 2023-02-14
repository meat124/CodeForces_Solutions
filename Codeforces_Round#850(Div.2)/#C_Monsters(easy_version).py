import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    result = a[0] - 1
    a[0] = 1
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            continue
        if a[i] + 1 == a[i + 1]:
            continue
        result += a[i + 1] - a[i] - 1
        a[i + 1] = a[i] + 1
    print(result)
