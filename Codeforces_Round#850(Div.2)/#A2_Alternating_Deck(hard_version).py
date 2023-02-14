import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    cur = 1
    a, b, c, d = 0, 0, 0, 0
    while n:
        if n - cur < 0:
            break
        if a + b <= c + d:
            a += cur//2 + 1
            b += cur//2
        else:
            c += cur//2
            d += cur//2 + 1
        n -= cur
        cur += 4
    if a + b <= c + d:
        if n & 1:
            a += n//2 + 1
            b += n//2
        else:
            a += n//2
            b += n//2
    else:
        if n & 1:
            c += n//2
            d += n//2 + 1
        else:
            c += n//2
            d += n//2
    print(a, b, c, d)
