import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    MAX = n*(n + 1)//2
    B = []
    st, en = 0, n - 1
    for i in range(n):
        if len(B) % 2:
            B.append(en)
            en -= 1
        else:
            B.append(st)
            st += 1
    b = [n]
    flag = False
    for i in range(1, n):
        if B[i - 1] < B[i]:
            b.append(b[-1] + B[i] - B[i - 1])
        else:
            b.append(b[-1] + n + B[i] - B[i - 1])
        if b[-1] > MAX:
            flag = True
            break
    if flag:
        print(-1)
        continue
    a = [n]
    for i in range(1, n):
        a.append(b[i] - b[i - 1])
    print(*a)
