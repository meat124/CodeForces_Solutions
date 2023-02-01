import sys
import math
input = sys.stdin.readline


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    prefix_sum = [a[0]]
    for i in range(1, n):
        prefix_sum.append(prefix_sum[-1] + a[i])
    A = sum(a)
    result = 1
    for i in range(0, n - 1):
        result = max(result, math.gcd(prefix_sum[i], A - prefix_sum[i]))
    print(result)
