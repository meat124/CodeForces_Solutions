from math import gcd
import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    beautiful = False
    # 서로소인 수가 하나라도 존재하면 가능하다
    for i in range(n - 1):
        for j in range(i + 1, n):
            if gcd(a[i], a[j]) <= 2:
                beautiful = True
                break
        if beautiful:
            break
    print('YES') if beautiful else print('NO')
