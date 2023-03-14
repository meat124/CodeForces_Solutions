import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    result = []
    for i in range(n):
        l, r = 1, i + 1
        while l <= r:
            mid = (l + r) // 2
            if A[i - mid + 1] >= mid:
                l = mid + 1
            else:
                r = mid - 1
        result.append(r)
    print(*result)
