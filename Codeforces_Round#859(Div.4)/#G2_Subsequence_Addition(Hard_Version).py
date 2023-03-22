import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    if c[0] != 1:
        print('NO')
    else:
        cur = c[0]
        result = 'YES'
        for i in range(1, n):
            if c[i] > cur:
                result = 'NO'
                break
            cur += c[i]
        print(result)
