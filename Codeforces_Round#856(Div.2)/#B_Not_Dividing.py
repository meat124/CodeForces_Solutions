import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    for i in range(n):
        if A[i] == 1:
            A[i] = 2
    for i in range(n - 1):
        if A[i + 1] % A[i] != 0 or A[i + 1] < A[i]:
            continue
        A[i + 1] += 1
    print(*A)
