from math import factorial
import sys
input = sys.stdin.readline
MOD = int(1e9 + 7)


def Sum(k):
    if k & 1:
        return (1+k)*(k//2) + (1+k)//2
    return (1+k)*(k//2)


for t in range(int(input())):
    n = int(input())
    # 1 2 2 1 >> 2개
    # 1 2 3 3 2 1 >> 1+2+2+1 = 6개
    # 1 2 3 4 4 3 2 1 >> 1+2+3+3+2+1 = Sum(n - 1)*2
    inversion_cnt = Sum(n - 1)*2
    print((inversion_cnt*(factorial(n) % MOD)) % MOD)
