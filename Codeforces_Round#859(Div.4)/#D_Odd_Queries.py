import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    # prefix[i] = A[0] ~ A[i] 까지 합
    prefix = [A[0]]
    for i in range(1, n):
        prefix.append(prefix[-1] + A[i])
    for i in range(q):
        l, r, k = map(int, input().split())
        l -= 1
        r -= 1
        if l == 0:
            print('YES') if (prefix[n - 1] - prefix[r] +
                             (r - l + 1)*k) & 1 else print('NO')
        else:
            print('YES') if ((prefix[l - 1]) + (r - l + 1)*k +
                             (prefix[n - 1] - prefix[r])) & 1 else print('NO')
