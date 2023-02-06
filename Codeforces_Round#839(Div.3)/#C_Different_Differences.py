import sys
input = sys.stdin.readline

for t in range(int(input())):
    k, n = map(int, input().split())
    result = []
    st, d = 1, 1
    for i in range(k):
        result.append(st)
        st += d
        d += 1
        if st > n:
            break
        if n - st < k - i - 2:
            break
    for i in range(k - len(result)):
        result.append(result[-1] + 1)
    print(*result)
