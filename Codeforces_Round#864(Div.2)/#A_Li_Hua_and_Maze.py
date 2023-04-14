import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    corner = [[1, 1], [1, m], [n, 1], [n, m]]
    x1, y1, x2, y2 = map(int, input().split())
    if [x1, y1] in corner or [x2, y2] in corner:
        print(2)
    else:
        result = 4
        if x1 in [1, n] or x2 in [1, n] or y1 in [1, m] or y2 in [1, m]:
            result = 3
        print(result)
