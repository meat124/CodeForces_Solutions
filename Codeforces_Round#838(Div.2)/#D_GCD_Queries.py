import sys
input = sys.stdin.readline


def Solve():
    n = int(input())
    l, r = 1, 2
    for i in range(3, n + 1):
        print('?', l, i)
        sys.stdout.flush()
        ql = int(input())
        print('?', r, i)
        sys.stdout.flush()
        qr = int(input())
        if ql > qr:
            r = i
        elif ql < qr:
            l = i
    print('!', l, r)
    sys.stdout.flush()
    input()


for t in range(int(input())):
    Solve()
    sys.stdout.flush()
