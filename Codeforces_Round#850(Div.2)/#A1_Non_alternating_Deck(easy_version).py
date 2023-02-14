import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    cur = 1
    a, b = 0, 0
    while n:
        if n - cur < 0:
            break
        if a <= b:
            a += cur
        else:
            b += cur
        n -= cur
        cur += 4
    if a <= b:
        a += n
    else:
        b += n
    print(a, b)
