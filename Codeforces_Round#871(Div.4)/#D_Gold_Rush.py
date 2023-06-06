from collections import deque
import sys
input = sys.stdin.readline
for t in range(int(input())):
    n, m = map(int, input().split())
    S = deque([n])
    result = 'NO'
    while S:
        cur = S.popleft()
        if cur == m:
            result = 'YES'
            break
        if cur % 3 != 0:
            continue
        S.append(cur//3)
        S.append(2*cur//3)
    print(result)
