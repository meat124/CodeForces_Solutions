import sys
input = sys.stdin.readline
for t in range(int(input())):
    n, k = map(int, input().split())
    x = -1
    for i in range(n + 1):
        a, b = i*(i - 1)//2, (n - i)*(n - i - 1)//2
        if a + b == k:
            x = i
            break
    if x == -1:
        print('NO')
    else:
        print('YES')
        tmp = []
        for i in range(n):
            if i < x:
                tmp.append(1)
            else:
                tmp.append(-1)
        print(*tmp)
