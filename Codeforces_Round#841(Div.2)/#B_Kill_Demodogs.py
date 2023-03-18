import sys
input = sys.stdin.readline
MOD = 10**9 + 7

for t in range(int(input())):
    n = int(input())
    print(2022*(n*(n + 1)*(4*n - 1)//6) % MOD)
