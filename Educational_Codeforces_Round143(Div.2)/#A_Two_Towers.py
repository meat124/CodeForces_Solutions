import sys
from itertools import permutations, combinations
import bisect
import heapq
import math
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input().rstrip()
    t = input().rstrip()
    cnt = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            cnt += 1
    for i in range(m - 1):
        if t[i] == t[i + 1]:
            cnt += 1
    if cnt == 0:
        print('YES')
    elif cnt == 1:
        if s[-1] == t[-1]:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
