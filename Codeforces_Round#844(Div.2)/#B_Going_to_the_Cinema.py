from collections import Counter
import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    result = 0
    if a[0] > 0:
        result += 1
    for i in range(1, n):
        if a[i] > i and a[i - 1] < i:
            result += 1
    if a[-1] < n:
        result += 1
    print(result)
