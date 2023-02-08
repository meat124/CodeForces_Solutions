import sys
from bisect import bisect_right
input = sys.stdin.readline
MOD = [2**i for i in range(31)]


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    result = []
    # 10의 배수 단위로 조절
    for i in range(n):
        if a[i] in MOD:
            continue
        to = MOD[bisect_right(MOD, a[i])]
        st = a[i]
        while a[i] != to:
            d = min(st, to - a[i])
            a[i] += d
            result.append([i + 1, d])
    print(len(result))
    for i in result:
        print(*i)
