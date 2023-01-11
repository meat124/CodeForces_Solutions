import sys
n, m, a, b = map(int, sys.stdin.readline().split())
print(min(n*a, b*(n//m) + b, b*(n//m) + a*(n % m)))
