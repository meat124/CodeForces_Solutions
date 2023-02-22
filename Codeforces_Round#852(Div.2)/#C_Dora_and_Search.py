import sys
input = sys.stdin.readline
MAX = 2*10**5 + 5

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l, r = 0, n-1
    # permutation a 에는 1~n 까지 존재한다.
    mn, mx = 1, n
    while l <= r:
        if a[l] == mn:
            l += 1
            mn += 1
        elif a[l] == mx:
            l += 1
            mx -= 1
        elif a[r] == mn:
            r -= 1
            mn += 1
        elif a[r] == mx:
            r -= 1
            mx -= 1
        else:
            break
    if l <= r:
        print(l + 1, r + 1)
    else:
        print(-1)
