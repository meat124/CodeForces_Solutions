import sys
input = sys.stdin.readline
# E_Interview
for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + A[i])
    l, r = 1, n
    while l != r:
        mid = (l + r)//2
        print(f"? {mid - l + 1}", end=' ')
        for i in range(l, mid + 1):
            print(i, end=' ')
        print('\n')
        sys.stdout.flush()
        x = int(input())
        if x == prefix[mid] - prefix[l - 1]:
            l = mid + 1
        else:
            r = mid
    print(f'! {l}')
    sys.stdout.flush()
