import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    A = sum(a)
    if A % 2 == 0:
        print(0)
    else:
        result = 10**9
        for i in range(n):
            st = a[i] % 2
            cur = a[i]//2
            cnt = 1
            while st == (cur % 2):
                cnt += 1
                cur //= 2
                if cur == 0:
                    break
            result = min(result, cnt)
        print(result)
