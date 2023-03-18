import sys
from functools import reduce
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    print(2022*(reduce(lambda x, y: x*y, A) + n - 1))
