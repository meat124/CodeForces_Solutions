import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    if not n & 1:
        print('No')
        continue
    print('Yes')
    pairs = []
    cur = 1+2*n - n//2
    for i in range(2, n, 2):
        pairs.append([i, cur - i])
        cur += 1
    for i in range(1, n + 1, 2):
        pairs.append([i, cur - i])
        cur += 1
    for i in range(n):
        print(*pairs[i])
