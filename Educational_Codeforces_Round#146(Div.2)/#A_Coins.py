import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    if n % 2 and k % 2:
        print('YES')
    elif n % 2 == 0:
        print('YES')
    else:
        print('NO')
