import sys
from math import lcm, gcd
input = sys.stdin.readline


for t in range(int(input())):
    n = int(input())
    # A[i] : 상점에 있는 i번 사탕의 개수
    # B[i] : i번 캔디의 가격
    A, B = [], []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    result = 1
    g, l = 0, 1
    for i in range(n):
        g = gcd(g, A[i]*B[i])
        l = lcm(l, B[i])
        if g % l:
            result += 1
            g = A[i]*B[i]
            l = B[i]
    print(result)
