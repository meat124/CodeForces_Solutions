import sys
input = sys.stdin.readline
for t in range(int(input())):
    n, t = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = -1
    cur_t, cur_val = 0, 0
    for i in range(n):
        if cur_val < B[i] and A[i] + i <= t:
            result = i + 1
            cur_val = B[i]
    print(result)
