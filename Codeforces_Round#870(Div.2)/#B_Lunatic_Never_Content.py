from math import gcd
import sys
input = sys.stdin.readline


for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    L = []
    for i in range(n//2):
        L.append(abs(A[i] - A[n - i - 1]))
    print(gcd(*L))
