import sys
input = sys.stdin.readline
n = int(input())
b = list(map(int, input().split()))
m = int(input())
g = list(map(int, input().split()))
b.sort()
g.sort()
vis = [False]*m
result = 0
for i in b:
    for j in range(m):
        if vis[j]:
            continue
        if abs(i - g[j]) <= 1:
            vis[j] = True
            result += 1
            break
print(result)
