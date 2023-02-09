import sys
input = sys.stdin.readline


def Get_Inversion():
    cur = 0
    inversion = 0
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            cur += 1
        if a[i] == 1:
            inversion += cur
    return inversion


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    zero = a.count(0)
    one = n - zero
    result = 0
    if zero == 0 or one == 0:
        result = n - 1
    else:
        result = Get_Inversion()
        # 0 to 1
        for i in range(n):
            if a[i] == 0:
                a[i] = 1
                result = max(result, Get_Inversion())
                a[i] = 0
                break
        # 1 to 0
        for i in range(n - 1, -1, -1):
            if a[i] == 1:
                a[i] = 0
                result = max(result, Get_Inversion())
                a[i] = 1
                break
    print(result)
