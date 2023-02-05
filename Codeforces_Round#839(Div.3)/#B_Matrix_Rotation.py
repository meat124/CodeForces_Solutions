import sys
input = sys.stdin.readline


def Is_Beautiful(a, b, c, d):
    if a >= b or c >= d or a >= c or b >= d:
        return False
    return True


for t in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if Is_Beautiful(a, b, c, d) or Is_Beautiful(c, a, d, b) or Is_Beautiful(d, c, b, a) or Is_Beautiful(b, d, a, c):
        print('YES')
    else:
        print('NO')
