import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    even, odd = 0, 0
    for a in A:
        if a & 1:
            odd += a
        else:
            even += a
    print('YES') if even > odd else print('NO')
