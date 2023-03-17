import sys
input = sys.stdin.readline

for t in range(int(input())):
    # sector 개수, 현재 arrow 위치, 당기는 최대 힘
    n, x, p = map(int, input().split())
    result = 'NO'
    MOD = ((n - x) % n)
    for i in range(1, min(2*n, p) + 1):
        if (i + 1)*i//2 % n == MOD:
            result = 'YES'
            break
    print(result)
