import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    result = a[0]
    a = sorted(a[1:])
    for i in range(n - 1):
        if a[i] <= result:
            continue
        d = a[i] - result
        result += d//2 if d % 2 == 0 else d//2 + 1
    print(result)
