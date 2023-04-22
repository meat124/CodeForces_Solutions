import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A_ = list(map(int, input().split()))
    l, r = -1, -1
    for i in range(n):
        if A[i] != A_[i]:
            if l == -1:
                l = i
            else:
                r = i
    while l > 0:
        if A_[l - 1] <= A_[l]:
            l -= 1
        else:
            break
    while r < n - 1:
        if A_[r] <= A_[r + 1]:
            r += 1
        else:
            break
    print(l + 1, r + 1)
