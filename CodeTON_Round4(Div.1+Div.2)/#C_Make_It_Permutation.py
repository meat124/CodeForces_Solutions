import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, c, d = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    result = n*c + d
    # 연속 원소의 개수
    consec = 0
    for i in range(n):
        if i > 0 and A[i] == A[i - 1]:
            consec += 1
        cur = (n - 1 - i + consec)*c + (A[i] - (i + 1 - consec))*d
        result = min(result, cur)
    print(result)
