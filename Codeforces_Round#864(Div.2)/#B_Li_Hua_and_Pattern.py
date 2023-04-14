import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    top = [list(map(int, input().split())) for i in range(n//2)]
    ctr = list(map(int, input().split())) if n & 1 else []
    bottom = [list(map(int, input().split())) for i in range(n//2)]
    if n == 1:
        print('YES')
        continue
    rev_bottom = [[0]*n for i in range(n//2)]
    for i in range(n//2):
        for j in range(n):
            rev_bottom[i][j] = bottom[n//2 - 1 - i][n - 1 - j]
    result = 0
    for i in range(n//2):
        for j in range(n):
            result += 1 if top[i][j] != rev_bottom[i][j] else 0
    if n & 1:
        for i in range(n//2):
            result += 1 if ctr[i] != ctr[n - 1 - i] else 0
        print('YES') if k - result >= 0 else print('NO')
    else:
        print('YES') if k - result >= 0 and not ((k - result) & 1) else print('NO')
