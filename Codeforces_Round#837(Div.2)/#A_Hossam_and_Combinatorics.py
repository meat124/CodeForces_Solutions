import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    min_a, max_a = min(a), max(a)
    cnt_min, cnt_max = a.count(min_a), a.count(max_a)
    if min_a == max_a:
        print(n*(n - 1)//2)
    else:
        print(2*cnt_min*cnt_max)
