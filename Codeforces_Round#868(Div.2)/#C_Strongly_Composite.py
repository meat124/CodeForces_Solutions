import sys
input = sys.stdin.readline


def Solve(x):
    i = 2
    while i**2 <= x:
        while x % i == 0:
            x //= i
            if i in A:
                A[i] += 1
            else:
                A[i] = 1
        i += 1
    if x != 1:
        if x in A:
            A[x] += 1
        else:
            A[x] = 1


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    A = {}
    for x in a:
        Solve(x)
    result, tmp = 0, 0
    for i in A:
        result += A[i]//2
        tmp += A[i] % 2
    result += tmp//3
    print(result)
