import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    a = 1
    A, B = [2*n], []
    for i in range(n - 1):
        if i & 1:
            B.append(n + a)
            A.append(n + a + 1)
        else:
            B.append(a)
            A.append(a + 1)
        if i & 1:
            a += 2
    B.append(2*n - 1)
    print(*A)
    print(*B)
