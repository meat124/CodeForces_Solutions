import sys
input = sys.stdin.readline

for t in range(int(input())):
    m, x = map(int, input().split())
    b = list(map(int, input().split()))
    S = set(range(1, 100)) - set(b)
    cur = 0
    result = 'NO'
    for i in S:
        cur += i
        b.append(i)
        if cur == x and len(b) == max(b):
            result = 'YES'
            break
        elif cur > x:
            break
    print(result)
