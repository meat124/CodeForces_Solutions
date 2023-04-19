import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if n == 2:
        print(max(sum(A), abs(A[0] - A[1])*2))
    elif n == 3:
        print(max(sum(A), A[0]*3, A[2]*3,
              abs(A[1] - A[0])*3, abs(A[2] - A[1])*3))
    else:
        print(max(A)*n)
