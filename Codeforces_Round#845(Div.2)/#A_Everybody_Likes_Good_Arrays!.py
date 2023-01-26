import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    result = 0
    while i < n:
        st = a[i]
        j = i + 1
        len = 0
        while j < n and (st & 1) == (a[j] & 1):
            len += 1
            j += 1
            i = j - 1
        result += len
        i += 1
    print(result)
