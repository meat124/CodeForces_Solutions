import sys
from itertools import permutations, combinations
import bisect
import heapq
import math
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    cnt = [0]*(51)
    seg = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        if seg[i][0] <= k <= seg[i][1]:
            for j in range(seg[i][0], seg[i][1] + 1):
                cnt[j] += 1
    print('YES') if cnt.count(cnt[k]) == 1 else print('NO')
