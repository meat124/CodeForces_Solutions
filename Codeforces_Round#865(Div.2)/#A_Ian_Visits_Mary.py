import sys
input = sys.stdin.readline
for t in range(int(input())):
    a, b = map(int, input().split())
    if a > 1 and b > 1:
        print(2)
        print(a - 1, 1)
        print(a, b)
    else:
        print(1)
        print(a, b)
