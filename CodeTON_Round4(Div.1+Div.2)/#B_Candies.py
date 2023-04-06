import sys
input = sys.stdin.readline

for t in range(int(input())):
    m = int(input())
    if m % 2 == 0:
        print(-1)
        continue
    result = []
    while m != 1 and len(result) < 40:
        if (m + 1)//2 & 1:
            m = (m + 1)//2
            result.append(1)
        else:
            m = (m - 1)//2
            result.append(2)
    if len(result) > 40:
        print(-1)
    else:
        print(len(result))
        print(*reversed(result))
