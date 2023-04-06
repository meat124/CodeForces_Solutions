import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, x1, y1, x2, y2 = map(int, input().split())
    fir = min(x1, y1, n + 1 - x1, n + 1 - y1)
    sec = min(x2, y2, n + 1 - x2, n + 1 - y2)
    print(abs(fir - sec))
