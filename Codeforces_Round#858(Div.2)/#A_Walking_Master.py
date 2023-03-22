import sys
input = sys.stdin.readline

for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    c -= a
    d -= b
    if d < 0:
        print(-1)
    elif d == 0 and c > 0:
        print(-1)
    elif d > 0 and c > d:
        print(-1)
    else:
        print(2*d - c)
