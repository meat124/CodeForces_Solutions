import sys
input = sys.stdin.readline
for t in range(int(input())):
    n, k = map(int, input().split())
    P = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if abs(P[i] - (i + 1)) % k != 0:
            cnt += 1
    if cnt == 0:
        print('0')
    elif cnt > 2:
        print('-1')
    else:
        print('1')
