import sys
input = sys.stdin.readline

for t in range(int(input())):
    a, b = map(int, input().split())
    a, b = abs(a), abs(b)
    common = min(a, b)
    a -= common
    b -= common
    result = 2*common + 2*(a+b)
    result -= 1 if a != b else 0
    print(result)
