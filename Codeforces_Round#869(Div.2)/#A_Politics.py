import sys
input = sys.stdin.readline
for t in range(int(input())):
    n, k = map(int, input().split())
    opinion = []
    for i in range(n):
        opinion.append(input().rstrip())
    cnt = 1
    for i in range(1, n):
        if opinion[i] == opinion[0]:
            cnt += 1
    print(cnt)
