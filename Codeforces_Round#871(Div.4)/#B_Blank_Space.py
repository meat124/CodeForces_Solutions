import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    result, cur = 0, 0
    for i in range(n):
        if A[i] == 0:
            cur += 1
        else:
            cur = 0
        result = max(result, cur)
    print(result)
