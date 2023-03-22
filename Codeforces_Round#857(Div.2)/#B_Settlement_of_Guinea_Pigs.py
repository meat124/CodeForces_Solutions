import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    B = list(map(int, input().split()))
    cur = 0
    result = 0
    max_result = 0
    for i in range(n):
        if B[i] == 1:
            cur += 1
            result += 1
        else:
            if cur == 0:
                continue
            result = cur//2 + cur % 2 if cur & 1 else cur//2 + cur % 2 + 1
        max_result = max(max_result, result)
    print(max_result)
