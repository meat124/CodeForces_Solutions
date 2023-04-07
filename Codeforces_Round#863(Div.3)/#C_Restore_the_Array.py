import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    B = list(map(int, input().split()))
    A = [0]*n
    A[0] = B[0]
    for i in range(n - 2):
        A[i + 1] = min(B[i], B[i + 1])
    A[n - 1] = B[-1]
    print(*A)
