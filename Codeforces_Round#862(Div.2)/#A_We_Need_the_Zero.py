import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    result = -1
    for x in range(2**8):
        cur = 0
        for a in A:
            cur ^= (a ^ x)
        if cur == 0:
            result = x
            break
    print(result)
