import sys
n, l = map(int, sys.stdin.readline().split())
loc = list(map(int, sys.stdin.readline().split()))
loc.sort()
max_dist = 0
for i in range(n - 1):
    max_dist = max(max_dist, loc[i + 1] - loc[i])
max_dist = max(loc[0], l - loc[-1], max_dist / 2)
print(max_dist)
