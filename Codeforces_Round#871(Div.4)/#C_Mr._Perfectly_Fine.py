import sys
input = sys.stdin.readline
MAX = int(2*10**6 + 5)
for t in range(int(input())):
    n = int(input())
    # 01,10,11 cost
    L = [MAX]*3
    for i in range(n):
        m, s = input().split()
        if s == '01':
            L[0] = min(L[0], int(m))
        elif s == '10':
            L[1] = min(L[1], int(m))
        elif s == '11':
            L[2] = min(L[2], int(m))
    if (L[0] == MAX or L[1] == MAX) and L[2] == MAX:
        print(-1)
    else:
        print(min(L[0]+L[1], L[2]))
