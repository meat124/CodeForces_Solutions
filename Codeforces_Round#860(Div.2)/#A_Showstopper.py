import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 'YES'
    for i in range(n - 1):
        if A[i] <= A[-1] and B[i] <= B[-1]:
            continue
        if A[i] <= B[-1] and B[i] <= A[-1]:
            continue
        result = 'NO'
    print(result)
