import sys
input = sys.stdin.readline

for t in range(int(input())):
    x, y = map(int, input().split())
    result = list(range(y, x + 1)) + list(range(x - 1, y, -1))
    print(len(result))
    print(*result)
