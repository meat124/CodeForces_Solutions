import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    upper_bound, lower_bound = 10**9, 0
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            upper_bound = min((a[i] + a[i + 1])//2, upper_bound)
        if a[i] > a[i + 1]:
            lower_bound = max((a[i] + a[i + 1] + 1)//2, lower_bound)
    print(upper_bound) if lower_bound <= upper_bound else print(-1)
