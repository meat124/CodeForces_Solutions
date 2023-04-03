import sys
input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    C = []
    for i in range(n):
        C.append(list(map(int, input().split())))
    L = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(C[j][i])
        L.append(sorted(tmp))
    result = 0
    L_prefix = []
    # prefix 생성
    for i in range(m):
        tmp = [L[i][0]]
        for j in range(1, n):
            tmp.append(tmp[-1] + L[i][j])
        L_prefix.append(tmp)
    for i in range(m):
        for j in range(n):
            result += L[i][j]*(j + 1) - L_prefix[i][j]
    print(result)
