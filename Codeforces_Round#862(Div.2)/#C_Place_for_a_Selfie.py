from math import sqrt
import sys
input = sys.stdin.readline


for t in range(int(input())):
    n, m = map(int, input().split())
    K = sorted([int(input()) for i in range(n)])
    F = [list(map(int, input().split())) for i in range(m)]

    for i in range(m):
        st, en = 0, n - 1
        a, b, c = F[i][0], F[i][1], F[i][2]
        if c < 0:
            print('NO')
            continue
        flag = 'NO'
        result = -1
        st, en = 0, n - 1
        while st <= en:
            mid = (st + en)//2
            if b - sqrt(4*a*c) < K[mid] < b + sqrt(4*a*c):
                flag = 'YES'
                result = K[mid]
                break
            elif K[mid] <= b - sqrt(4*a*c):
                st = mid + 1
            else:
                en = mid - 1
        print(flag)
        if flag == 'YES':
            print(result)
    print()
